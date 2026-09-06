import hashlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from preparer_hugo import build_files, numbered_sections, slug
from verifier_html import verify_html


class HugoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = build_files(ROOT)

    def test_content_synchronised(self):
        for name, content in self.files.items():
            self.assertEqual((ROOT / name).read_text(encoding="utf-8"), content, name)

    def test_all_manuscrit_ascii_diagrams_transposed(self):
        manuscrit_diagrams = json.loads(self.files["data/diagrams/manuscrit.json"])
        self.assertEqual(len(manuscrit_diagrams), 61)
        for sha, diag in manuscrit_diagrams.items():
            self.assertEqual(len(sha), 64)
            self.assertEqual(sha, diag["source_sha256"])
            self.assertTrue(diag["id"])
            self.assertTrue(diag["title"])
            card_count = len(diag["parts"]) if len(diag["parts"]) >= 2 else len(diag["parts"][0].get("items", []))
            self.assertGreaterEqual(card_count, 2)
        found_hashes = set()
        for path in (ROOT / "manuscrit").rglob("*.md"):
            for m in re.finditer(r"```text\n(.*?)```", path.read_text(encoding="utf-8"), re.DOTALL):
                if any(c in m[1] for c in "┌┬└┼─│"):
                    found_hashes.add(hashlib.sha256(m[1].encode()).hexdigest())
        self.assertEqual(found_hashes, set(manuscrit_diagrams.keys()))

    def test_twelve_pairs_with_symmetric_mirrors(self):
        decoder = json.JSONDecoder()
        pages = {}
        for name, content in self.files.items():
            meta, _ = decoder.raw_decode(content)
            if "chapter_id" in meta:
                pages[meta["chapter_id"]] = (name, meta)
        self.assertEqual(len(pages), 24)
        for ident, (name, meta) in pages.items():
            mirror_id = ("B" if ident[0] == "A" else "A") + ident[1:]
            mirror_name, mirror = pages[mirror_id]
            self.assertEqual("content" + meta["mirror"] + ".md", mirror_name)
            self.assertEqual("content" + mirror["mirror"] + ".md", name)
            self.assertEqual(meta["title"], mirror["title"])
            self.assertGreaterEqual(len(meta["related"]), 2)

    def test_section_parser_ignores_code(self):
        sections = numbered_sections("# 1. Sujet\n```sh\n# 9. Commande\n```\n## 1.2 Détail")
        self.assertEqual(set(sections), {"1", "1.2"})

    def test_source_12_is_linkable(self):
        self.assertIn("{#section-12-6}", self.files["content/references/sources/i-md.md"])
        for prefix in ("accessible", "ingenieure"):
            content = self.files[f"content/{prefix}/12-ecosysteme-et-independance.md"]
            self.assertIn("/references/sources/i-md#section-12-1", content)
            self.assertIn("/references#ref-codestral", content)

    def test_glossary_anchors(self):
        mesh = json.loads((ROOT / "editorial/maillage.json").read_text(encoding="utf-8"))
        glossary = self.files["content/annexes/glossaire.md"]
        for theme in mesh["themes"].values():
            for term in theme["notions"]:
                self.assertIn("{#" + slug(term) + "}", glossary)

    def test_html_checker_detects_missing_anchor(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text('<html lang="fr"><title>T</title><h1>T</h1><a href="#absent">Lien</a></html>', encoding="utf-8")
            errors, count, links = verify_html(root)
            self.assertEqual((count, links), (1, 1))
            self.assertTrue(any("Ancre absente" in e for e in errors))

    def test_html_checker_supports_subdirectory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text('<html lang="fr"><title>T</title><h1 id="titre">T</h1><a href="/manuel/#titre">Lien</a></html>', encoding="utf-8")
            self.assertEqual(verify_html(root, "/manuel/")[0], [])

    def test_html_checker_detects_duplicates_and_missing_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text('<html lang="fr"><title>T</title><h1 id="x">T</h1><p id="x">T</p><a href="absent.html">Lien</a></html>', encoding="utf-8")
            errors, _, _ = verify_html(root)
            self.assertTrue(any("dupliquée" in e for e in errors))
            self.assertTrue(any("Lien cassé" in e for e in errors))

    def test_local_tufte_fonts_and_license(self):
        for name in ("roman", "italic", "bold"):
            font = ROOT / f"assets/fonts/et-book/{name}.woff"
            self.assertEqual(font.read_bytes()[:4], b"wOFF")
        license_text = (ROOT / "static/fonts/et-book/LICENSE.txt").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2015 Dmitry Krasny", license_text)

    def test_external_links_open_in_protected_tab(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / "index.html"
            for href in ("https://example.org/", "http://example.org/", "//example.org/"):
                for attrs in ('', 'target="_blank"', 'target="_blank" rel="noopener"'):
                    page.write_text(f'<html lang="fr"><title>T</title><h1>T</h1><a href="{href}" {attrs}>Externe</a></html>', encoding="utf-8")
                    self.assertTrue(any("nouvel onglet protégé" in e for e in verify_html(root)[0]))
                page.write_text(f'<html lang="fr"><title>T</title><h1 id="titre">T</h1><a href="{href}" target="_blank" rel="external noopener noreferrer">Externe</a><a href="#titre">Interne</a></html>', encoding="utf-8")
                self.assertEqual(verify_html(root)[0], [])

    def test_css_fonts_and_preloads_under_prefix(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text('<html lang="fr"><title>T</title><h1>T</h1><link rel="stylesheet" href="/manuel/style.css"><link rel="preload" href="/manuel/roman.woff" as="font"></html>', encoding="utf-8")
            (root / "style.css").write_text('@font-face{src:url("/manuel/italic.woff")}p{background:url(data:image/png;base64,AA)}', encoding="utf-8")
            errors, _, _ = verify_html(root, "/manuel/")
            self.assertTrue(any("roman.woff" in e for e in errors))
            self.assertTrue(any("italic.woff" in e for e in errors))
            (root / "roman.woff").write_bytes(b"wOFF")
            (root / "italic.woff").write_bytes(b"wOFF")
            self.assertEqual(verify_html(root, "/manuel/")[0], [])
            (root / "style.css").write_text('@font-face{src:url("/italic.woff")}', encoding="utf-8")
            self.assertTrue(any("hors base" in e for e in verify_html(root, "/manuel/")[0]))


if __name__ == "__main__":
    unittest.main()
