import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from verifier import local_links, validate_manifest, verify
from assembler import build, relocate


class EditorialTests(unittest.TestCase):
    def setUp(self):
        self.chapters = json.loads((ROOT / "editorial/chapitres.json").read_text(encoding="utf-8"))["chapitres"]

    def test_repository(self):
        self.assertEqual(verify(ROOT), [])

    def test_five_prerequisites_are_separate_from_pairs(self):
        manifest = json.loads((ROOT / "editorial/chapitres.json").read_text(encoding="utf-8"))
        preamble = json.loads((ROOT / manifest["prerequis"]["manifeste"]).read_text(encoding="utf-8"))
        self.assertEqual([u["id"] for u in preamble["unites"]], ["P01", "P02", "P03", "P04", "P05"])
        self.assertEqual(len(self.chapters), 24)

    def test_missing_pair_rejected(self):
        self.assertTrue(validate_manifest(self.chapters[:-1]))

    def test_bad_mirror_rejected(self):
        altered = copy.deepcopy(self.chapters)
        altered[0]["miroir"] = "absent.md"
        self.assertTrue(any("miroir" in e for e in validate_manifest(altered)))

    def test_cycle_rejected(self):
        altered = copy.deepcopy(self.chapters)
        altered[0]["dependances"] = ["A02"]
        self.assertTrue(any("Cycle" in e for e in validate_manifest(altered)))

    def test_complete_chapter_12_required(self):
        altered = copy.deepcopy(self.chapters)
        next(c for c in altered if c["id"] == "B12")["sources"] = ["O-MD §2"]
        self.assertTrue(any("chapitre 12" in e for e in validate_manifest(altered)))

    def test_local_links_with_spaces(self):
        text = '[a](<../un fichier.pdf>) [b](https://example.org) [c](#section)\n```text\n[d](inexistant)\n```'
        self.assertEqual(list(local_links(text)), ["../un fichier.pdf"])

    def test_relocation_preserves_code(self):
        source = ROOT / "manuscrit/01-lecture-accessible/test.md"
        destination = ROOT / "dist/test.md"
        text = '# Titre\n[x](../SOMMAIRE.md)\n```python\n# intact\n```'
        result = relocate(text, source, destination)
        self.assertIn("../manuscrit/SOMMAIRE.md", result)
        self.assertIn("### Titre", result)
        self.assertIn("\n# intact\n", result)

    def test_build_order_and_status(self):
        paths = build(ROOT)
        full = paths[0].read_text(encoding="utf-8")
        validated = sum(c["statut"] == "valide" for c in self.chapters)
        self.assertIn(f"{validated}/24 chapitres validés", full)
        self.assertLess(full.index("### A12"), full.index("### B01"))
        self.assertIn("### B12", full)
        self.assertLess(full.index("### P01"), full.index("### A01"))
        for path in paths:
            for target in local_links(path.read_text(encoding="utf-8")):
                self.assertTrue((path.parent / target).resolve().exists(), target)


if __name__ == "__main__":
    unittest.main()
