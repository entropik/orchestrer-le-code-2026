"""Contrôle le texte PDF et le code Markdown dans le HTML réellement construit."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

from lecture_sources import pdf_pages

ROOT = Path(__file__).resolve().parents[1]


class ReaderText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pdf = {}
        self.blocks = []
        self.capture = None
        self.buffer = []
        self.diagrams = []
        self.math = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'figure' and 'data-diagram' in attrs:
            self.diagrams.append(attrs['data-source-sha256'])
        if 'data-source-tex' in attrs:
            self.math.append(attrs['data-source-tex'])
        if tag == 'div' and 'data-source-page' in attrs:
            self.capture = ('pdf', int(attrs['data-source-page']))
            self.buffer = []
        elif tag == 'pre':
            self.capture = ('code', None)
            self.buffer = []

    def handle_data(self, data):
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if not self.capture:
            return
        kind, number = self.capture
        if kind == 'pdf' and tag == 'div':
            if number in self.pdf:
                raise ValueError(f'Page PDF dupliquée : {number}')
            self.pdf[number] = ''.join(self.buffer)
            self.capture = None
        elif kind == 'code' and tag == 'pre':
            self.blocks.append(''.join(self.buffer))
            self.capture = None


def verify(site):
    inventory = json.loads((ROOT / 'sources/inventaire.json').read_text(encoding='utf-8'))
    count = 0
    blocks = 0
    diagrams = 0
    formulas = 0
    for doc in inventory['documents']:
        parsed = ReaderText()
        parsed.feed((site / f"references/sources/{doc['id'].lower()}/index.html").read_text(encoding='utf-8'))
        if 'pages' in doc:
            pages = pdf_pages((ROOT / doc['extrait']).read_text(encoding='utf-8'), doc['pages'])
            expected = dict(enumerate(pages, 1))
            if parsed.pdf != expected:
                raise ValueError(f"{doc['id']} : texte PDF altéré ou manquant dans le HTML")
            count += len(pages)
        else:
            original = (ROOT / 'sources/originaux' / doc['fichier']).read_text(encoding='utf-8-sig')
            expected = re.findall(r'^```[^\n]*\n(.*?)^```\s*$', original, re.M | re.S)
            # Le renderer peut ajouter une fin de ligne terminale, jamais réécrire le code.
            if [b.rstrip('\n') for b in parsed.blocks] != [b.rstrip('\n') for b in expected]:
                raise ValueError(f"{doc['id']} : bloc de code altéré ou manquant dans le HTML")
            blocks += len(expected)
            import hashlib
            expected_diagrams = [hashlib.sha256((b.rstrip('\n')+'\n').encode()).hexdigest() for b in expected if re.search('[┌┬└┼─│]', b)]
            if parsed.diagrams != expected_diagrams:
                raise ValueError(f"{doc['id']} : schéma graphique absent, dupliqué ou désordonné")
            diagrams += len(expected_diagrams)
            prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', original, flags=re.M|re.S)
            expressions = re.findall(r'\$\$(.*?)\$\$|(?<!\$)\$([^$\n]+)\$', prose, re.S)
            expected_math = [re.sub(r'^> ?', '', block or inline, flags=re.M).strip(' \r\n') for block,inline in expressions]
            if parsed.math != expected_math:
                raise ValueError(f"{doc['id']} : expression LaTeX originale absente ou modifiée : {parsed.math!r} != {expected_math!r}")
            formulas += len(expected_math)
    print(f'OK : {count} pages PDF, {blocks} blocs de code, {diagrams} schémas et {formulas} expressions LaTeX vérifiés dans le HTML.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    verify(parser.parse_args().site)
