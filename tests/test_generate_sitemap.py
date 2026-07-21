import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from scripts.generate_sitemap import SitemapError, generate_sitemap


def html_page(canonical: str | None, reviewed: str | None = None) -> str:
    canonical_markup = f'<link rel="canonical" href="{canonical}">' if canonical else ""
    reviewed_markup = (
        f'<time data-seo-last-reviewed datetime="{reviewed}">{reviewed}</time>'
        if reviewed
        else ""
    )
    return f"<html><head>{canonical_markup}</head><body>{reviewed_markup}</body></html>"


class SitemapGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.site = Path(self.temp_dir.name) / "site"
        self.site.mkdir()
        self.output = self.site / "sitemap.xml"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_page(self, relative: str, html: str) -> None:
        path = self.site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")

    def entries(self) -> list[tuple[str, str | None]]:
        root = ET.parse(self.output).getroot()
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        return [
            (
                element.findtext("s:loc", namespaces=namespace) or "",
                element.findtext("s:lastmod", namespaces=namespace),
            )
            for element in root.findall("s:url", namespace)
        ]

    def test_uses_rendered_canonicals_dates_and_stable_sorting(self) -> None:
        self.write_page(
            "nested/physical-name.html",
            html_page("https://safeaiaus.org/z-custom/", "2026-07-19"),
        )
        self.write_page("index.html", html_page("https://safeaiaus.org/", "2026-07-21"))
        self.write_page("legal/index.html", html_page("https://safeaiaus.org/legal/"))
        self.write_page("asset.html", html_page(None))

        result = generate_sitemap(self.site, self.output)
        first = self.output.read_bytes()
        generate_sitemap(self.site, self.output)

        self.assertEqual(result.url_count, 3)
        self.assertEqual(self.output.read_bytes(), first)
        self.assertEqual(
            self.entries(),
            [
                ("https://safeaiaus.org/", "2026-07-21"),
                ("https://safeaiaus.org/legal/", None),
                ("https://safeaiaus.org/z-custom/", "2026-07-19"),
            ],
        )
        xml = first.decode("utf-8")
        self.assertNotIn("priority", xml)
        self.assertNotIn("changefreq", xml)

    def test_excludes_404_even_if_it_has_a_canonical(self) -> None:
        self.write_page("index.html", html_page("https://safeaiaus.org/"))
        self.write_page("404.html", html_page("https://safeaiaus.org/not-found/"))

        generate_sitemap(self.site, self.output)

        self.assertEqual(self.entries(), [("https://safeaiaus.org/", None)])

    def test_rejects_duplicate_canonical_urls(self) -> None:
        self.write_page("one/index.html", html_page("https://safeaiaus.org/duplicate/"))
        self.write_page("two/index.html", html_page("https://safeaiaus.org/duplicate/"))

        with self.assertRaisesRegex(SitemapError, "duplicate canonical"):
            generate_sitemap(self.site, self.output)

    def test_rejects_invalid_or_duplicate_review_dates(self) -> None:
        self.write_page("index.html", html_page("https://safeaiaus.org/", "July 2026"))
        with self.assertRaisesRegex(SitemapError, "review date"):
            generate_sitemap(self.site, self.output)

        self.write_page(
            "index.html",
            html_page("https://safeaiaus.org/", "2026-07-21").replace(
                "</body>",
                '<time data-seo-last-reviewed datetime="2026-07-20"></time></body>',
            ),
        )
        with self.assertRaisesRegex(SitemapError, "review date"):
            generate_sitemap(self.site, self.output)

    def test_rejects_empty_canonical_site(self) -> None:
        self.write_page("asset.html", html_page(None))

        with self.assertRaisesRegex(SitemapError, "no canonical"):
            generate_sitemap(self.site, self.output)


if __name__ == "__main__":
    unittest.main()
