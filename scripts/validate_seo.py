#!/usr/bin/env python3
"""Validate SafeAI-Aus source metadata and final rendered SEO contracts."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit


ORIGIN = "https://safeaiaus.org"
ORG_ID = f"{ORIGIN}/#organization"
OPERATOR_ID = f"{ORIGIN}/#legal-operator"
WEBSITE_ID = f"{ORIGIN}/#website"
LEGAL_PATHS = {"/LICENSE/", "/NOTICE/"}
EXCLUDED_PREFIXES = ("/plans/", "/brainstorms/", "/templates/")
REVIEW_CYCLES = {"quarterly": 3}
TITLE_LIMIT = 60
DESCRIPTION_LIMIT = 165
SPECIALISED_SCHEMA = {
    "/business-resources/ai-grants-funding-australia/": {"FAQPage"},
    "/governance-templates/ai-risk-assessment-checklist/": {"FAQPage", "HowTo"},
    "/governance-templates/policy-template-library/": {"FAQPage", "ItemList"},
    "/resources/glossary/": {"DefinedTermSet"},
}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    ranking_pages: int = 0
    canonical_pages: int = 0


@dataclass(frozen=True)
class SourcePage:
    path: Path
    metadata: dict[str, str]
    body: str
    canonical: str
    legal: bool


@dataclass
class RenderedPage:
    path: Path
    canonicals: list[str] = field(default_factory=list)
    title: str = ""
    description: str | None = None
    provenance_text: str = ""
    review_dates: list[str] = field(default_factory=list)
    h1: str = ""
    path_hidden: bool = False
    breadcrumb_links: list[tuple[str, str]] = field(default_factory=list)
    scripts: list[tuple[str | None, str]] = field(default_factory=list)


def _attributes(attrs: list[tuple[str, str | None]]) -> dict[str, str | None]:
    return {name.lower(): value for name, value in attrs}


def _classes(attributes: dict[str, str | None]) -> set[str]:
    return set((attributes.get("class") or "").split())


class SeoHtmlParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.page = RenderedPage(path=path)
        self._title = False
        self._title_parts: list[str] = []
        self._script = False
        self._script_id: str | None = None
        self._script_parts: list[str] = []
        self._provenance_depth = 0
        self._provenance_parts: list[str] = []
        self._path_depth = 0
        self._path_hidden = False
        self._anchor = False
        self._anchor_href: str | None = None
        self._anchor_parts: list[str] = []
        self._h1_depth = 0
        self._h1_parts: list[str] = []
        self._headerlink_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = _attributes(attrs)
        tag = tag.lower()
        if tag == "link" and "canonical" in set((attributes.get("rel") or "").split()):
            href = attributes.get("href")
            if href:
                self.page.canonicals.append(href)
        if tag == "meta" and attributes.get("name") == "description":
            self.page.description = attributes.get("content")
        if tag == "title":
            self._title = True
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._script = True
            self._script_id = attributes.get("id")
            self._script_parts = []
        if "data-seo-provenance" in attributes:
            self._provenance_depth = 1
        elif self._provenance_depth:
            self._provenance_depth += 1
        if tag == "time" and "data-seo-last-reviewed" in attributes:
            value = attributes.get("datetime")
            if value:
                self.page.review_dates.append(value)
        if tag == "nav" and "md-path" in _classes(attributes):
            self._path_depth = 1
            self._path_hidden = "hidden" in attributes
            self.page.path_hidden = self._path_hidden
        elif self._path_depth:
            self._path_depth += 1
        if self._path_depth and not self._path_hidden and tag == "a" and "md-path__link" in _classes(attributes):
            self._anchor = True
            self._anchor_href = attributes.get("href")
            self._anchor_parts = []
        if tag == "h1" and not self.page.h1:
            self._h1_depth = 1
        elif self._h1_depth:
            self._h1_depth += 1
            if tag == "a" and "headerlink" in _classes(attributes):
                self._headerlink_depth = self._h1_depth

    def handle_data(self, data: str) -> None:
        if self._title:
            self._title_parts.append(data)
        if self._script:
            self._script_parts.append(data)
        if self._provenance_depth:
            self._provenance_parts.append(data)
        if self._anchor:
            self._anchor_parts.append(data)
        if self._h1_depth and not self._headerlink_depth:
            self._h1_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title" and self._title:
            self._title = False
            self.page.title = _collapse(self._title_parts)
        if tag == "script" and self._script:
            self.page.scripts.append((self._script_id, "".join(self._script_parts)))
            self._script = False
        if self._anchor and tag == "a":
            self.page.breadcrumb_links.append((_collapse(self._anchor_parts), self._anchor_href or ""))
            self._anchor = False
        if self._h1_depth:
            if self._headerlink_depth == self._h1_depth:
                self._headerlink_depth = 0
            self._h1_depth -= 1
            if not self._h1_depth:
                self.page.h1 = _collapse(self._h1_parts)
        if self._path_depth:
            self._path_depth -= 1
        if self._provenance_depth:
            self._provenance_depth -= 1

    def close(self) -> None:
        super().close()
        self.page.provenance_text = _collapse(self._provenance_parts)


def _collapse(parts: list[str]) -> str:
    return " ".join("".join(parts).split())


def parse_frontmatter(path: Path, text: str | None = None) -> tuple[dict[str, str], str]:
    source = path.read_text(encoding="utf-8") if text is None else text
    lines = source.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, source
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as error:
        raise ValueError("unterminated frontmatter") from error
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, raw = line.split(":", 1)
        value = raw.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        metadata[key.strip()] = value
    return metadata, "\n".join(lines[end + 1 :])


def _source_canonical(path: Path, docs: Path, metadata: dict[str, str]) -> str:
    permalink = metadata.get("permalink")
    if permalink:
        return urljoin(f"{ORIGIN}/", permalink)
    relative = path.relative_to(docs).with_suffix("").as_posix()
    if relative == "index":
        route = "/"
    elif relative.endswith("/index"):
        route = f"/{relative.removesuffix('/index')}/"
    else:
        route = f"/{relative}/"
    return f"{ORIGIN}{route}"


def _load_sources(docs: Path, result: ValidationResult) -> dict[str, SourcePage]:
    pages: dict[str, SourcePage] = {}
    for path in sorted(docs.rglob("*.md")):
        relative = path.relative_to(docs)
        if relative.parts and relative.parts[0] in {"plans", "brainstorms", "templates"}:
            continue
        try:
            metadata, body = parse_frontmatter(path)
        except ValueError as error:
            result.errors.append(f"{path}: {error}")
            continue
        canonical = _source_canonical(path, docs, metadata)
        legal = urlsplit(canonical).path in LEGAL_PATHS
        if canonical in pages:
            result.errors.append(f"{path}: duplicate source canonical {canonical}")
        pages[canonical] = SourcePage(path, metadata, body, canonical, legal)
    return pages


def _load_rendered(site: Path, result: ValidationResult) -> dict[str, RenderedPage]:
    pages: dict[str, RenderedPage] = {}
    for path in sorted(site.rglob("*.html")):
        if path.relative_to(site).as_posix() == "404.html":
            continue
        parser = SeoHtmlParser(path)
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        page = parser.page
        if not page.canonicals:
            continue
        if len(page.canonicals) != 1:
            result.errors.append(f"{path}: expected exactly one canonical link")
            continue
        canonical = page.canonicals[0]
        parsed = urlsplit(canonical)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            result.errors.append(f"{path}: canonical must be an absolute HTTP(S) URL")
            continue
        if parsed.path.startswith(EXCLUDED_PREFIXES):
            continue
        if canonical in pages:
            result.errors.append(f"{path}: duplicate rendered canonical {canonical}")
        pages[canonical] = page
    return pages


def _iso_date(value: str, label: str, errors: list[str]) -> date | None:
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid ISO date {value!r}")
        return None
    if parsed.isoformat() != value:
        errors.append(f"{label}: invalid ISO date {value!r}")
        return None
    return parsed


def _subtract_months(value: date, months: int) -> date:
    month_index = value.year * 12 + value.month - 1 - months
    year, month_zero = divmod(month_index, 12)
    month = month_zero + 1
    month_lengths = [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return date(year, month, min(value.day, month_lengths[month - 1]))


def _load_sitemap(path: Path, result: ValidationResult) -> dict[str, str | None]:
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        result.errors.append(f"{path}: cannot parse sitemap: {error}")
        return {}
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries: dict[str, str | None] = {}
    for element in root.findall("s:url", namespace):
        location = element.findtext("s:loc", namespaces=namespace)
        if not location:
            result.errors.append(f"{path}: sitemap entry is missing loc")
            continue
        if location in entries:
            result.errors.append(f"{path}: duplicate sitemap URL {location}")
        entries[location] = element.findtext("s:lastmod", namespaces=namespace)
        if element.find("s:priority", namespace) is not None or element.find("s:changefreq", namespace) is not None:
            result.errors.append(f"{path}: priority and changefreq are not allowed")
    if list(entries) != sorted(entries):
        result.errors.append(f"{path}: sitemap URLs are not sorted")
    return entries


def _parse_jsonld(page: RenderedPage, result: ValidationResult) -> tuple[list[dict], dict | None]:
    objects: list[dict] = []
    marked: list[dict] = []
    for script_id, body in page.scripts:
        try:
            value = json.loads(body)
        except json.JSONDecodeError as error:
            result.errors.append(f"{page.path}: malformed JSON-LD: {error}")
            continue
        if not isinstance(value, dict):
            result.errors.append(f"{page.path}: JSON-LD root must be an object")
            continue
        objects.append(value)
        if script_id == "safeai-general-schema":
            marked.append(value)
    if len(marked) != 1:
        result.errors.append(f"{page.path}: expected exactly one safeai-general-schema graph")
        return objects, None
    return objects, marked[0]


def _validate_graph(
    source: SourcePage,
    page: RenderedPage,
    expected_review: str | None,
    result: ValidationResult,
) -> None:
    objects, general = _parse_jsonld(page, result)
    if general is None:
        return
    graph = general.get("@graph")
    if not isinstance(graph, list):
        result.errors.append(f"{page.path}: general schema must contain an @graph array")
        return
    nodes = {node.get("@id"): node for node in graph if isinstance(node, dict) and node.get("@id")}
    if len(nodes) != sum(1 for node in graph if isinstance(node, dict) and node.get("@id")):
        result.errors.append(f"{page.path}: duplicate @id in general graph")
    org = nodes.get(ORG_ID, {})
    if org.get("name") != "SafeAI-Aus" or set(org.get("@type", [])) != {"Organization", "Project"}:
        result.errors.append(f"{page.path}: invalid SafeAI-Aus Organization/Project identity")
    if org.get("parentOrganization") != {"@id": OPERATOR_ID}:
        result.errors.append(f"{page.path}: SafeAI-Aus parentOrganization must reference the legal operator")
    if "foundingDate" in org or "hasOfferCatalog" in org:
        result.errors.append(f"{page.path}: unverified Organization properties are present")
    operator = nodes.get(OPERATOR_ID, {})
    if operator.get("name") != "Safe AI Australia Inc" or operator.get("legalName") != "Safe AI Australia Inc":
        result.errors.append(f"{page.path}: legalName must be Safe AI Australia Inc")
    if "incorporated not-for-profit association" not in operator.get("description", ""):
        result.errors.append(f"{page.path}: legal operator description is missing its legal form")
    if "nonprofitStatus" in operator:
        result.errors.append(f"{page.path}: unverified nonprofitStatus is not allowed")
    website = nodes.get(WEBSITE_ID, {})
    if website.get("@type") != "WebSite" or website.get("publisher") != {"@id": ORG_ID}:
        result.errors.append(f"{page.path}: invalid WebSite identity or publisher")

    page_type = "Article" if source.metadata.get("og_type") == "article" else "WebPage"
    suffix = "#article" if page_type == "Article" else "#webpage"
    page_id = f"{source.canonical}{suffix}"
    page_node = nodes.get(page_id)
    if not page_node or page_node.get("@type") != page_type:
        result.errors.append(f"{page.path}: missing canonical {page_type} node {page_id}")
        return
    if page_node.get("url") != source.canonical or page_node.get("mainEntityOfPage") != {"@id": source.canonical}:
        result.errors.append(f"{page.path}: page entity canonical URL drift")
    for field_name in ("author", "publisher"):
        if page_node.get(field_name) != {"@id": ORG_ID}:
            result.errors.append(f"{page.path}: {field_name} must reference SafeAI-Aus")
    if "datePublished" in page_node:
        result.errors.append(f"{page.path}: unverified datePublished is not allowed")
    if page_node.get("dateModified") != expected_review:
        state = "pending page" if source.metadata.get("review-status") == "pending" else "page"
        result.errors.append(f"{page.path}: {state} dateModified does not match visible review date")

    breadcrumb_id = f"{source.canonical}#breadcrumb"
    breadcrumb = nodes.get(breadcrumb_id)
    visible = bool(page.breadcrumb_links) and not page.path_hidden
    if not visible:
        if breadcrumb or "breadcrumb" in page_node:
            result.errors.append(f"{page.path}: breadcrumb schema exists without a visible path")
    else:
        expected = [
            (name, urljoin(source.canonical, href))
            for name, href in page.breadcrumb_links
        ] + [(page.h1, source.canonical)]
        items = breadcrumb.get("itemListElement", []) if isinstance(breadcrumb, dict) else []
        actual = [
            (item.get("name"), item.get("item"), item.get("position"))
            for item in items if isinstance(item, dict)
        ]
        wanted = [(name, item, index) for index, (name, item) in enumerate(expected, 1)]
        if page_node.get("breadcrumb") != {"@id": breadcrumb_id} or actual != wanted:
            result.errors.append(f"{page.path}: BreadcrumbList does not match rendered .md-path and H1")

    required = SPECIALISED_SCHEMA.get(urlsplit(source.canonical).path)
    if required:
        present = {value.get("@type") for value in objects if value is not general}
        missing = sorted(required - present)
        if missing:
            result.errors.append(f"{page.path}: missing specialised schema: {', '.join(missing)}")


def _normalise_non_substantive_body(body: str) -> str:
    body = re.sub(
        r"<!--\s*JSON-LD:.*?<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>.*?</script>",
        "",
        body,
        flags=re.DOTALL,
    )
    body = re.sub(r"<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>.*?</script>", "", body, flags=re.DOTALL)
    body = re.sub(r"^.*\bLast (?:reviewed|updated):.*$", "", body, flags=re.MULTILINE | re.IGNORECASE)
    return " ".join(body.split())


def _validate_substantive_edits(base_ref: str, docs: Path, sources: dict[str, SourcePage], result: ValidationResult) -> None:
    process = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD", "--", str(docs)],
        capture_output=True,
        text=True,
    )
    if process.returncode:
        result.errors.append(f"cannot compare substantive edits with {base_ref}: {process.stderr.strip()}")
        return
    by_path = {str(page.path): page for page in sources.values()}
    for changed in process.stdout.splitlines():
        current = by_path.get(changed) or by_path.get(str(Path(changed).resolve()))
        if not current or current.legal or current.metadata.get("review-status") == "pending":
            continue
        old = subprocess.run(
            ["git", "show", f"{base_ref}:{changed}"],
            capture_output=True,
            text=True,
        )
        if old.returncode:
            continue
        try:
            old_meta, old_body = parse_frontmatter(Path(changed), old.stdout)
        except ValueError:
            continue
        if _normalise_non_substantive_body(old_body) != _normalise_non_substantive_body(current.body):
            if old_meta.get("last-reviewed") == current.metadata.get("last-reviewed"):
                result.errors.append(f"{changed}: substantive content changed without advancing last-reviewed")


def validate_project(
    docs: Path,
    site: Path,
    sitemap: Path,
    *,
    today: date | None = None,
    base_ref: str | None = None,
) -> ValidationResult:
    result = ValidationResult()
    today = today or date.today()
    sources = _load_sources(docs, result)
    rendered = _load_rendered(site, result)
    sitemap_entries = _load_sitemap(sitemap, result)
    result.ranking_pages = sum(not page.legal for page in sources.values())
    result.canonical_pages = len(rendered)

    source_set = set(sources)
    rendered_set = set(rendered)
    sitemap_set = set(sitemap_entries)
    for missing in sorted(source_set - rendered_set):
        result.errors.append(f"{sources[missing].path}: no rendered canonical page for {missing}")
    for extra in sorted(rendered_set - source_set):
        result.errors.append(f"{rendered[extra].path}: rendered canonical has no public Markdown source: {extra}")
    if rendered_set != sitemap_set:
        for missing in sorted(rendered_set - sitemap_set):
            result.errors.append(f"sitemap is missing {missing}")
        for extra in sorted(sitemap_set - rendered_set):
            result.errors.append(f"sitemap contains non-canonical page {extra}")

    seen_titles: dict[str, str] = {}
    seen_descriptions: dict[str, str] = {}
    for canonical, source in sorted(sources.items()):
        page = rendered.get(canonical)
        metadata = source.metadata
        if source.legal:
            expected_review = None
        else:
            for field_name in ("title", "description", "last-reviewed", "review-cycle"):
                if not metadata.get(field_name):
                    result.errors.append(f"{source.path}: missing required {field_name}")
            cycle = metadata.get("review-cycle")
            if cycle and cycle not in REVIEW_CYCLES:
                result.errors.append(f"{source.path}: unsupported review-cycle {cycle!r}")
            parsed_review = None
            if metadata.get("last-reviewed"):
                parsed_review = _iso_date(metadata["last-reviewed"], f"{source.path}: last-reviewed", result.errors)
                if parsed_review and parsed_review > today:
                    result.errors.append(f"{source.path}: last-reviewed cannot be in the future")
            pending = metadata.get("review-status") == "pending"
            if metadata.get("review-status") not in {None, "pending"}:
                result.errors.append(f"{source.path}: unsupported review-status {metadata['review-status']!r}")
            expected_review = None if pending else metadata.get("last-reviewed")
            if pending:
                result.warnings.append(
                    f"{source.path}: substantive review pending; freshness signals are withheld"
                )
            if parsed_review and cycle in REVIEW_CYCLES and not pending:
                if parsed_review < _subtract_months(today, REVIEW_CYCLES[cycle]):
                    result.warnings.append(f"{source.path}: overdue {cycle} review ({parsed_review.isoformat()})")
        if not page:
            continue
        if not source.legal:
            if len(page.title) > TITLE_LIMIT:
                result.errors.append(f"{source.path}: rendered title exceeds {TITLE_LIMIT} characters ({len(page.title)})")
            if page.description is None:
                result.errors.append(f"{source.path}: missing rendered meta description")
            elif len(page.description) > DESCRIPTION_LIMIT:
                result.errors.append(f"{source.path}: rendered description exceeds {DESCRIPTION_LIMIT} characters ({len(page.description)})")
            for value, seen, label in (
                (page.title, seen_titles, "title"),
                (page.description or "", seen_descriptions, "description"),
            ):
                if value in seen:
                    result.errors.append(f"{source.path}: duplicate rendered {label} also used by {seen[value]}")
                seen[value] = str(source.path)
        if len(page.review_dates) > 1:
            result.errors.append(f"{page.path}: expected at most one visible review date")
        actual_review = page.review_dates[0] if page.review_dates else None
        if actual_review != expected_review:
            if metadata.get("review-status") == "pending":
                result.errors.append(f"{page.path}: pending page must not emit a visible review date")
            else:
                result.errors.append(f"{page.path}: visible review date does not match source metadata")
        if "Published by: SafeAI-Aus" not in page.provenance_text or "Editorial methodology" not in page.provenance_text:
            result.errors.append(f"{page.path}: visible organisation provenance is incomplete")
        if expected_review and ("Last reviewed:" not in page.provenance_text or "Review cycle: Quarterly" not in page.provenance_text):
            result.errors.append(f"{page.path}: readable review provenance is incomplete")
        if metadata.get("review-status") == "pending" and "Substantive review pending" not in page.provenance_text:
            result.errors.append(f"{page.path}: pending review state is not visible")
        if sitemap_entries.get(canonical) != expected_review:
            result.errors.append(f"{canonical}: sitemap lastmod does not match visible review date")
        _validate_graph(source, page, expected_review, result)

    if base_ref:
        _validate_substantive_edits(base_ref, docs, sources, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=Path("docs"))
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--sitemap", type=Path, default=Path("site/sitemap.xml"))
    parser.add_argument("--base-ref")
    args = parser.parse_args()
    result = validate_project(args.docs, args.site, args.sitemap, base_ref=args.base_ref)
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if result.errors:
        print(f"SEO validation failed with {len(result.errors)} error(s).", file=sys.stderr)
        return 1
    print(
        f"SEO validation passed for {result.canonical_pages} canonical page(s) "
        f"and {result.ranking_pages} ranking page(s); {len(result.warnings)} freshness warning(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
