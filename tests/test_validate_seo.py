import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

from scripts.generate_sitemap import SITEMAP_NAMESPACE
from scripts.validate_seo import _normalise_non_substantive_body, validate_project


ORG_ID = "https://safeaiaus.org/#organization"
OPERATOR_ID = "https://safeaiaus.org/#legal-operator"
WEBSITE_ID = "https://safeaiaus.org/#website"


def graph(canonical: str, reviewed: str | None, breadcrumb: bool = False) -> dict:
    page = {
        "@id": f"{canonical}#article",
        "@type": "Article",
        "headline": "Useful AI Guide",
        "url": canonical,
        "mainEntityOfPage": {"@id": canonical},
        "description": "Practical Australian guidance.",
        "image": "https://safeaiaus.org/logo.png",
        "inLanguage": "en-AU",
        "author": {"@id": ORG_ID},
        "publisher": {"@id": ORG_ID},
        "isPartOf": {"@id": WEBSITE_ID},
    }
    if reviewed:
        page["dateModified"] = reviewed
    nodes = [
        {
            "@id": ORG_ID,
            "@type": ["Organization", "Project"],
            "name": "SafeAI-Aus",
            "parentOrganization": {"@id": OPERATOR_ID},
        },
        {
            "@id": OPERATOR_ID,
            "@type": "Organization",
            "name": "Safe AI Australia Inc",
            "legalName": "Safe AI Australia Inc",
            "description": "The incorporated not-for-profit association that operates SafeAI-Aus.",
        },
        {
            "@id": WEBSITE_ID,
            "@type": "WebSite",
            "name": "SafeAI-Aus",
            "publisher": {"@id": ORG_ID},
        },
        page,
    ]
    if breadcrumb:
        breadcrumb_id = f"{canonical}#breadcrumb"
        page["breadcrumb"] = {"@id": breadcrumb_id}
        nodes.append(
            {
                "@id": breadcrumb_id,
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": "https://safeaiaus.org/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Useful AI Guide",
                        "item": canonical,
                    },
                ],
            }
        )
    return {"@context": "https://schema.org", "@graph": nodes}


def html_page(canonical: str, reviewed: str | None, *, breadcrumb: bool = False) -> str:
    review = (
        f'<strong>Last reviewed:</strong><time datetime="{reviewed}" '
        f'data-seo-last-reviewed>{reviewed}</time><strong>Review cycle:</strong> Quarterly'
        if reviewed
        else "Substantive review pending"
    )
    path = (
        '<nav class="md-path"><a class="md-path__link" href="../">Home</a></nav>'
        if breadcrumb
        else ""
    )
    return f"""<!doctype html><html><head>
    <link rel="canonical" href="{canonical}">
    <meta name="description" content="Practical Australian guidance.">
    <meta property="og:type" content="article">
    <title>Useful AI Guide - SafeAI-Aus</title>
    <script id="safeai-general-schema" type="application/ld+json">{json.dumps(graph(canonical, reviewed, breadcrumb))}</script>
    </head><body>{path}<article><h1>Useful AI Guide<a class="headerlink">¶</a></h1></article>
    <aside data-seo-provenance>Published by: SafeAI-Aus {review}
    <a href="/about/#editorial-methodology">Editorial methodology</a></aside>
    </body></html>"""


class SeoValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.docs = root / "docs"
        self.site = root / "site"
        self.docs.mkdir()
        self.site.mkdir()
        self.sitemap = self.site / "sitemap.xml"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_fixture(
        self,
        *,
        reviewed: str = "2026-07-01",
        pending: bool = False,
        breadcrumb: bool = False,
    ) -> None:
        status = '\nreview-status: "pending"' if pending else ""
        self.docs.joinpath("guide.md").write_text(
            f'''---\ntitle: "Useful AI Guide"\ndescription: "Practical Australian guidance."\nlast-reviewed: "{reviewed}"\nreview-cycle: "quarterly"\nog_type: "article"{status}\n---\n# Useful AI Guide\n''',
            encoding="utf-8",
        )
        canonical = "https://safeaiaus.org/guide/"
        output = self.site / "guide" / "index.html"
        output.parent.mkdir()
        output.write_text(
            html_page(canonical, None if pending else reviewed, breadcrumb=breadcrumb),
            encoding="utf-8",
        )
        namespace = SITEMAP_NAMESPACE
        ET.register_namespace("", namespace)
        root = ET.Element(ET.QName(namespace, "urlset"))
        entry = ET.SubElement(root, ET.QName(namespace, "url"))
        ET.SubElement(entry, ET.QName(namespace, "loc")).text = canonical
        if not pending:
            ET.SubElement(entry, ET.QName(namespace, "lastmod")).text = reviewed
        ET.ElementTree(root).write(self.sitemap, encoding="utf-8", xml_declaration=True)

    def test_accepts_consistent_reviewed_page_and_breadcrumb(self) -> None:
        self.write_fixture(breadcrumb=True)

        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))

        self.assertEqual(result.errors, [])
        self.assertEqual(result.ranking_pages, 1)

    def test_pending_page_must_withhold_review_freshness(self) -> None:
        self.write_fixture(pending=True)
        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))
        self.assertEqual(result.errors, [])

        page = self.site / "guide" / "index.html"
        page.write_text(html_page("https://safeaiaus.org/guide/", "2026-07-01"), encoding="utf-8")
        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))

        self.assertTrue(any("pending" in error.lower() for error in result.errors))

    def test_overdue_review_is_warning_only(self) -> None:
        self.write_fixture(reviewed="2026-01-01")

        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))

        self.assertEqual(result.errors, [])
        self.assertTrue(any("overdue" in warning.lower() for warning in result.warnings))

    def test_rejects_identity_and_sitemap_date_drift(self) -> None:
        self.write_fixture()
        page = self.site / "guide" / "index.html"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                '"legalName": "Safe AI Australia Inc"',
                '"legalName": "Different Entity"',
            ),
            encoding="utf-8",
        )
        self.sitemap.write_text(
            self.sitemap.read_text(encoding="utf-8").replace("2026-07-01", "2026-06-01"),
            encoding="utf-8",
        )

        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))

        self.assertTrue(any("legalname" in error.lower() for error in result.errors))
        self.assertTrue(any("sitemap" in error.lower() for error in result.errors))

    def test_rejects_metadata_budget_and_invalid_source_date(self) -> None:
        self.write_fixture(reviewed="not-a-date")
        page = self.site / "guide" / "index.html"
        page.write_text(
            page.read_text(encoding="utf-8").replace(
                "Useful AI Guide - SafeAI-Aus",
                "An excessively long generated search title that is well beyond sixty characters - SafeAI-Aus",
            ),
            encoding="utf-8",
        )

        result = validate_project(self.docs, self.site, self.sitemap, today=date(2026, 7, 21))

        self.assertTrue(any("last-reviewed" in error for error in result.errors))
        self.assertTrue(any("title" in error.lower() and "60" in error for error in result.errors))

    def test_review_label_cleanup_is_not_treated_as_substantive(self) -> None:
        old = "Always verify current status. Last reviewed: April 2026.\n*Last updated: 6 July 2026. This is not legal advice.*\n**Last reviewed:** January 2026\n**Focus:** Australia"
        new = "Always verify current status.\n*This is not legal advice.*\n**Focus:** Australia"

        self.assertEqual(
            _normalise_non_substantive_body(old),
            _normalise_non_substantive_body(new),
        )


if __name__ == "__main__":
    unittest.main()
