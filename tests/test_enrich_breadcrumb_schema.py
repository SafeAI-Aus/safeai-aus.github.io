import json
import tempfile
import unittest
from pathlib import Path

from scripts.enrich_breadcrumb_schema import EnrichmentError, enrich_site


def page_html(*, path_markup: str = "", graph_extra: list[dict] | None = None) -> str:
    canonical = "https://safeaiaus.org/guides/current/"
    graph = [
        {
            "@id": f"{canonical}#article",
            "@type": "Article",
            "headline": "Current guide",
        },
        *(graph_extra or []),
    ]
    return f"""<!doctype html>
<html><head>
<link rel="canonical" href="{canonical}">
<script id="safeai-general-schema" type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph})}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage"}}</script>
</head><body>
{path_markup}
<article class="md-content__inner md-typeset"><h1>Current &amp; safe <a class="headerlink">¶</a></h1></article>
</body></html>"""


def visible_path(*, hidden: bool = False) -> str:
    hidden_attr = " hidden" if hidden else ""
    return f"""<nav class="md-path" aria-label="Navigation"{hidden_attr}>
<ol class="md-path__list">
<li><a class="md-path__link" href="../.."><span>Home</span></a></li>
<li><a href="../" class="md-path__link"><span>Guides</span></a></li>
</ol></nav>"""


class BreadcrumbEnrichmentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.site = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_page(self, relative: str, html: str) -> Path:
        path = self.site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        return path

    def graph(self, path: Path) -> dict:
        html = path.read_text(encoding="utf-8")
        start = html.index(">", html.index('id="safeai-general-schema"')) + 1
        end = html.index("</script>", start)
        return json.loads(html[start:end])

    def test_enriches_visible_rendered_path_and_preserves_specialist_schema(self) -> None:
        path = self.write_page("guides/current/index.html", page_html(path_markup=visible_path()))
        specialist_before = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage"}</script>'

        result = enrich_site(self.site)

        self.assertEqual(result.processed_pages, 1)
        self.assertEqual(result.breadcrumb_pages, 1)
        document = path.read_text(encoding="utf-8")
        self.assertIn(specialist_before, document)
        graph = self.graph(path)["@graph"]
        article = next(node for node in graph if node.get("@type") == "Article")
        self.assertEqual(
            article["breadcrumb"],
            {"@id": "https://safeaiaus.org/guides/current/#breadcrumb"},
        )
        breadcrumb = next(node for node in graph if node.get("@type") == "BreadcrumbList")
        self.assertEqual(
            [(item["position"], item["name"], item["item"]) for item in breadcrumb["itemListElement"]],
            [
                (1, "Home", "https://safeaiaus.org/"),
                (2, "Guides", "https://safeaiaus.org/guides/"),
                (3, "Current & safe", "https://safeaiaus.org/guides/current/"),
            ],
        )

    def test_hidden_path_removes_stale_breadcrumb_and_is_idempotent(self) -> None:
        canonical = "https://safeaiaus.org/guides/current/"
        stale = {
            "@id": f"{canonical}#breadcrumb",
            "@type": "BreadcrumbList",
            "itemListElement": [],
        }
        path = self.write_page(
            "guides/current/index.html",
            page_html(path_markup=visible_path(hidden=True), graph_extra=[stale]),
        )
        initial = self.graph(path)
        initial["@graph"][0]["breadcrumb"] = {"@id": f"{canonical}#breadcrumb"}
        html = path.read_text(encoding="utf-8")
        start = html.index(">", html.index('id="safeai-general-schema"')) + 1
        end = html.index("</script>", start)
        path.write_text(html[:start] + json.dumps(initial) + html[end:], encoding="utf-8")

        enrich_site(self.site)
        once = path.read_text(encoding="utf-8")
        enrich_site(self.site)

        self.assertEqual(path.read_text(encoding="utf-8"), once)
        graph = self.graph(path)["@graph"]
        self.assertNotIn("breadcrumb", graph[0])
        self.assertFalse(any(node.get("@type") == "BreadcrumbList" for node in graph))

    def test_appends_current_page_even_when_rendered_path_links_to_same_url(self) -> None:
        canonical = "https://safeaiaus.org/guides/current/"
        markup = f'<nav class="md-path"><a class="md-path__link" href="{canonical}">Guides</a></nav>'
        path = self.write_page("guides/current/index.html", page_html(path_markup=markup))

        enrich_site(self.site)

        breadcrumb = next(
            node for node in self.graph(path)["@graph"] if node.get("@type") == "BreadcrumbList"
        )
        self.assertEqual(
            [item["item"] for item in breadcrumb["itemListElement"]],
            [canonical, canonical],
        )

    def test_skips_404_without_canonical_or_general_graph(self) -> None:
        self.write_page("404.html", "<html><body><h1>Not found</h1></body></html>")

        result = enrich_site(self.site)

        self.assertEqual(result.processed_pages, 0)

    def test_rejects_duplicate_canonical_links(self) -> None:
        html = page_html(path_markup=visible_path()).replace(
            "</head>",
            '<link rel="canonical" href="https://safeaiaus.org/other/"></head>',
        )
        self.write_page("guides/current/index.html", html)

        with self.assertRaisesRegex(EnrichmentError, "canonical"):
            enrich_site(self.site)

    def test_rejects_canonical_page_without_graph_regardless_of_attribute_style(self) -> None:
        self.write_page(
            "guides/current/index.html",
            "<html><head><link href='https://safeaiaus.org/guides/current/' rel='canonical'></head></html>",
        )

        with self.assertRaisesRegex(EnrichmentError, "marked general schema"):
            enrich_site(self.site)


if __name__ == "__main__":
    unittest.main()
