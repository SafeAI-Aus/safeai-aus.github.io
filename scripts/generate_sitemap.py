#!/usr/bin/env python3
"""Generate a deterministic sitemap from rendered canonical HTML pages."""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
EXCLUDED_PATH_PREFIXES = ("/plans/", "/brainstorms/")


class SitemapError(RuntimeError):
    """Raised when rendered output cannot produce a trustworthy sitemap."""


@dataclass(frozen=True)
class SitemapResult:
    url_count: int


class SitemapSignalsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.review_dates: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value for name, value in attrs}
        tag = tag.lower()
        if tag == "link" and "canonical" in set((attributes.get("rel") or "").split()):
            href = attributes.get("href")
            if href:
                self.canonicals.append(href)
        if tag == "time" and "data-seo-last-reviewed" in attributes:
            value = attributes.get("datetime")
            if value:
                self.review_dates.append(value)


def _read_signals(path: Path) -> tuple[str | None, str | None]:
    parser = SitemapSignalsParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()

    if len(parser.canonicals) > 1:
        raise SitemapError(f"{path}: expected at most one canonical link")
    if len(parser.review_dates) > 1:
        raise SitemapError(f"{path}: expected at most one rendered review date")
    if not parser.canonicals:
        return None, None

    canonical = parser.canonicals[0]
    parsed = urlsplit(canonical)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SitemapError(f"{path}: canonical URL must be absolute HTTP(S): {canonical}")

    reviewed = parser.review_dates[0] if parser.review_dates else None
    if reviewed:
        try:
            parsed_date = date.fromisoformat(reviewed)
        except ValueError as error:
            raise SitemapError(f"{path}: invalid rendered review date: {reviewed}") from error
        if parsed_date.isoformat() != reviewed:
            raise SitemapError(f"{path}: invalid rendered review date: {reviewed}")
    return canonical, reviewed


def generate_sitemap(site: Path, output: Path) -> SitemapResult:
    if not site.is_dir():
        raise SitemapError(f"site directory does not exist: {site}")

    entries: dict[str, str | None] = {}
    for path in sorted(site.rglob("*.html")):
        if path.relative_to(site).as_posix() == "404.html":
            continue
        canonical, reviewed = _read_signals(path)
        if not canonical:
            continue
        canonical_path = urlsplit(canonical).path
        if canonical_path.startswith(EXCLUDED_PATH_PREFIXES):
            continue
        if canonical in entries:
            raise SitemapError(f"{path}: duplicate canonical URL: {canonical}")
        entries[canonical] = reviewed

    if not entries:
        raise SitemapError(f"no canonical HTML pages found under {site}")

    ET.register_namespace("", SITEMAP_NAMESPACE)
    root = ET.Element(ET.QName(SITEMAP_NAMESPACE, "urlset"))
    for canonical in sorted(entries):
        url = ET.SubElement(root, ET.QName(SITEMAP_NAMESPACE, "url"))
        ET.SubElement(url, ET.QName(SITEMAP_NAMESPACE, "loc")).text = canonical
        reviewed = entries[canonical]
        if reviewed:
            ET.SubElement(url, ET.QName(SITEMAP_NAMESPACE, "lastmod")).text = reviewed

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output, encoding="utf-8", xml_declaration=True)
    with output.open("ab") as handle:
        handle.write(b"\n")
    return SitemapResult(url_count=len(entries))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--output", type=Path, default=Path("site/sitemap.xml"))
    args = parser.parse_args()
    result = generate_sitemap(args.site, args.output)
    print(f"Generated sitemap with {result.url_count} canonical URL(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
