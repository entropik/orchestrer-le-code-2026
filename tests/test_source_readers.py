import json
import re
import sys
import unittest
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from lecture_sources import markdown_integral, pdf_pages
from preparer_hugo import build_files
from preparer_schemas import build as build_diagrams


class IntegralSourcesTests(unittest.TestCase):
    def test_all_diagrams_generated_and_source_words_preserved(self):
        registry = build_diagrams()  # vérifie chaque empreinte et chaque mot du texte
        saved = json.loads((ROOT / 'data/diagrams/registry.json').read_text(encoding='utf-8'))
        self.assertEqual(registry, saved)
        self.assertEqual(len(registry), 17)
        counts = []
        for path in (ROOT / 'sources/originaux').glob('*.md'):
            count = 0
            for m in re.finditer(r'^```([^\n]*)\n(.*?)^```\s*$',path.read_text(encoding='utf-8-sig'),re.M|re.S):
                if re.search('[┌┬└┼─│]',m[2]):
                    self.assertIn(hashlib.sha256(m[2].encode()).hexdigest(),registry)
                    count += 1
            counts.append(count)
        self.assertEqual(sorted(counts), [0,12,16,17])

    def test_graphic_harness_preserves_all_source_words(self):
        diagram = json.loads((ROOT / 'data/diagrams/harnais.json').read_text(encoding='utf-8'))
        source = (ROOT / 'sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md').read_text(encoding='utf-8-sig')
        block = re.search(r'```text\n(.*?ANATOMIE DU HARNAIS AGENTIQUE.*?)```', source, re.S)[1]
        self.assertEqual(hashlib.sha256(block.encode()).hexdigest(), diagram['source_sha256'])
        labels = [diagram['title']]
        for step in diagram['steps']:
            labels.append(step['title'])
            labels.extend(step.get('items', []))
            if 'output' in step:
                labels.append(step['output'])
        for outcome in diagram['outcomes']:
            labels.extend(outcome.values())
        # Tous les mots, nombres et identifiants, avec leurs occurrences :
        # aucun libellé oublié, dupliqué ou reformulé dans la transposition.
        self.assertEqual(Counter(re.findall(r'\w+', block)), Counter(re.findall(r'\w+', ' '.join(labels))))
        self.assertEqual(len(diagram['steps']), 4)
        self.assertEqual([o['title'] for o in diagram['outcomes']], ['ÉCHEC', 'SUCCÈS'])

    def test_every_markdown_line_preserved_except_presentation(self):
        files = build_files(ROOT)
        for original in (ROOT / "sources/originaux").glob("*.md"):
            source = original.read_text(encoding="utf-8-sig")
            rendered = markdown_integral(source)
            self.assertTrue(any(rendered.strip() in p for p in files.values()), original.name)
            self.assertEqual(len(source.splitlines()), len(rendered.splitlines()))
            for before, after in zip(source.splitlines(), rendered.splitlines()):
                # Seules les modifications mécaniques documentées sont permises.
                after = re.sub(r" \{#section-[\d-]+\}$", "", after)
                if before.startswith("#") and after.startswith("#"):
                    after = re.sub(r"^#+", re.match(r"^#+", before)[0], after)
                after = after.replace(' {{< source-break >}} ', '<br>')
                before = re.sub(r"\]\(#\d+(?:\.\d+)*-[^)]+\)", "](#NAV)", before)
                after = re.sub(r"\]\(#section-[\d-]+\)", "](#NAV)", after)
                self.assertEqual(before, after, original.name)

    def test_code_and_nested_fence_markers_are_literal(self):
        text = '# 1. Titre\n````markdown\n```python\n# 1. Pas un titre\n```\n````\n## 1.1 Suite\n'
        result = markdown_integral(text)
        self.assertIn('````markdown\n```python\n# 1. Pas un titre\n```\n````', result)
        self.assertEqual(result.count('{#section-1}'), 1)
        self.assertIn('{#section-1-1}', result)
        with self.assertRaises(ValueError):
            markdown_integral('{{< execute >}}')

    def test_chapter_anchor_not_overwritten_by_numbered_subtitle(self):
        result = markdown_integral('# 1. Chapitre\n### 1. Sous-liste\n')
        self.assertEqual(result.count('{#section-1}'), 1)

    def test_all_pdf_characters_and_pages_preserved(self):
        files = build_files(ROOT)
        inventory = json.loads((ROOT / 'sources/inventaire.json').read_text(encoding='utf-8'))
        count = 0
        for doc in inventory['documents']:
            if 'pages' not in doc:
                continue
            text = (ROOT / doc['extrait']).read_text(encoding='utf-8')
            pages = pdf_pages(text, doc['pages'])
            self.assertEqual(json.loads(files[f"data/source_pages/{doc['id'].lower()}.json"]), pages)
            canonical = next(d['id'].lower() for d in inventory['documents'] if d['sha256'] == doc['sha256'])
            content = files[f"content/projet/references/sources/{doc['id'].lower()}.md"]
            for n, body in enumerate(pages, 1):
                self.assertTrue(body.strip(), f"{doc['id']} page {n} vide")
                self.assertIn(f'{{#page-{n}}}', content)
                image = ROOT / f'static/source-pages/{canonical}/page-{n:02d}.png'
                self.assertEqual(image.read_bytes()[:8], b'\x89PNG\r\n\x1a\n')
            count += len(pages)
        self.assertEqual(count, 166)

    def test_missing_pdf_page_rejected(self):
        with self.assertRaises(ValueError):
            pdf_pages('<!-- page 1 -->\nTexte', 2)


if __name__ == '__main__':
    unittest.main()
