#!/usr/bin/env python3
"""Enrich SafeAI-Aus general JSON-LD graphs from rendered breadcrumbs."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


GENERAL_SCHEMA_ID = "safeai-general-schema"
SCRIPT_PATTERN = re.compile(
    r"(<script\b(?=[^>]*\bid=[\"']safeai-general-schema[\"'])[^>]*>)(.*?)(</script\s*>)",
    re.IGNORECASE | re.DOTALL,
)


class EnrichmentError(RuntimeError):
    """Raised when generated HTML violates the enrichment contract."""


@dataclass(frozen=True)
class EnrichmentResult:
    processed_pages: int
    breadcrumb_pages: int


class PageSignalsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.path_depth = 0
        self.path_links: list[tuple[str, str]] = []
        self.current_path_link: dict[str, object] | None = None
        self.h1_depth = 0
        self.h1_parts: list[str] = []
        self.headerlink_depth = 0

    @staticmethod
    def _attributes(attrs: list[tuple[str, str | None]]) -> dict[str, str | None]:
        return {name.lower(): value for name, value in attrs}

    @staticmethod
    def _classes(attributes: dict[str, str | None]) -> set[str]:
        return set((attributes.get("class") or "").split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = self._attributes(attrs)
        tag = tag.lower()

        if tag == "link" and "canonical" in set((attributes.get("rel") or "").split()):
            href = attributes.get("href")
            if href:
                self.canonicals.append(href)

        if self.path_depth:
            self.path_depth += 1
        elif tag == "nav" and "md-path" in self._classes(attributes) and "hidden" not in attributes:
            self.path_depth = 1

        if self.path_depth and tag == "a" and "md-path__link" in self._classes(attributes):
            if self.current_path_link is not None:
                raise EnrichmentError("nested breadcrumb links are not supported")
            self.current_path_link = {"href": attributes.get("href"), "parts": []}

        if not self.h1_parts and self.h1_depth == 0 and tag == "h1":
            self.h1_depth = 1
        elif self.h1_depth:
            self.h1_depth += 1
            if tag == "a" and "headerlink" in self._classes(attributes):
                self.headerlink_depth = self.h1_depth

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()

        if tag == "a" and self.current_path_link is not None:
            href = self.current_path_link["href"]
            parts = self.current_path_link["parts"]
            assert isinstance(parts, list)
            name = " ".join("".join(parts).split())
            if not href or not name:
                raise EnrichmentError("breadcrumb links require non-empty href and text")
            self.path_links.append((str(href), name))
            self.current_path_link = None

        if self.headerlink_depth and self.h1_depth == self.headerlink_depth and tag == "a":
            self.headerlink_depth = 0
        if self.h1_depth:
            self.h1_depth -= 1

        if self.path_depth:
            self.path_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.current_path_link is not None:
            parts = self.current_path_link["parts"]
            assert isinstance(parts, list)
            parts.append(data)
        if self.h1_depth and not self.headerlink_depth:
            self.h1_parts.append(data)

    @property
    def h1(self) -> str:
        return " ".join("".join(self.h1_parts).split())


def _safe_json(data: object) -> str:
    serialized = json.dumps(data, ensure_ascii=False, indent=2)
    return (
        serialized.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def _enrich_page(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    parser = PageSignalsParser()
    try:
        parser.feed(html)
        parser.close()
    except EnrichmentError as error:
        raise EnrichmentError(f"{path}: {error}") from error

    if not parser.canonicals:
        if SCRIPT_PATTERN.search(html):
            raise EnrichmentError(f"{path}: non-canonical page contains the general schema")
        return False
    if len(parser.canonicals) != 1:
        raise EnrichmentError(f"{path}: expected exactly one canonical link")
    canonical = parser.canonicals[0]

    matches = list(SCRIPT_PATTERN.finditer(html))
    if len(matches) != 1:
        raise EnrichmentError(f"{path}: expected exactly one marked general schema")
    match = matches[0]
    try:
        document = json.loads(match.group(2))
    except json.JSONDecodeError as error:
        raise EnrichmentError(f"{path}: malformed marked general schema: {error}") from error

    graph = document.get("@graph") if isinstance(document, dict) else None
    if not isinstance(graph, list):
        raise EnrichmentError(f"{path}: marked general schema must contain an @graph array")

    page_ids = {f"{canonical}#article", f"{canonical}#webpage"}
    page_nodes = [node for node in graph if isinstance(node, dict) and node.get("@id") in page_ids]
    if len(page_nodes) != 1:
        raise EnrichmentError(f"{path}: expected exactly one canonical Article or WebPage node")
    page_node = page_nodes[0]

    breadcrumb_id = f"{canonical}#breadcrumb"
    breadcrumb_nodes = [
        node
        for node in graph
        if isinstance(node, dict)
        and (node.get("@id") == breadcrumb_id or node.get("@type") == "BreadcrumbList")
    ]
    if len(breadcrumb_nodes) > 1:
        raise EnrichmentError(f"{path}: duplicate BreadcrumbList nodes")
    graph[:] = [node for node in graph if node not in breadcrumb_nodes]
    page_node.pop("breadcrumb", None)

    has_breadcrumb = bool(parser.path_links)
    if has_breadcrumb:
        if not parser.h1:
            raise EnrichmentError(f"{path}: breadcrumb page has no current-page H1")
        items = [
            {
                "@type": "ListItem",
                "position": position,
                "name": name,
                "item": urljoin(canonical, href),
            }
            for position, (href, name) in enumerate(parser.path_links, start=1)
        ]
        items.append(
            {
                "@type": "ListItem",
                "position": len(items) + 1,
                "name": parser.h1,
                "item": canonical,
            }
        )
        page_node["breadcrumb"] = {"@id": breadcrumb_id}
        graph.append(
            {
                "@id": breadcrumb_id,
                "@type": "BreadcrumbList",
                "itemListElement": items,
            }
        )

    replacement = f"{match.group(1)}\n{_safe_json(document)}\n{match.group(3)}"
    updated = f"{html[:match.start()]}{replacement}{html[match.end():]}"
    if updated != html:
        path.write_text(updated, encoding="utf-8")
    return has_breadcrumb


def enrich_site(site: Path) -> EnrichmentResult:
    if not site.is_dir():
        raise EnrichmentError(f"site directory does not exist: {site}")

    processed = 0
    breadcrumb_pages = 0
    for path in sorted(site.rglob("*.html")):
        if path.relative_to(site).as_posix() == "404.html":
            continue
        html = path.read_text(encoding="utf-8")
        if not SCRIPT_PATTERN.search(html) and "rel=\"canonical\"" not in html:
            continue
        try:
            has_breadcrumb = _enrich_page(path)
        except EnrichmentError as error:
            if str(error).startswith(str(path)):
                raise
            raise EnrichmentError(f"{path}: {error}") from error
        processed += 1
        breadcrumb_pages += int(has_breadcrumb)

    return EnrichmentResult(processed_pages=processed, breadcrumb_pages=breadcrumb_pages)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    args = parser.parse_args()
    result = enrich_site(args.site)
    print(
        f"Enriched {result.breadcrumb_pages} breadcrumb page(s) "
        f"across {result.processed_pages} canonical page(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
