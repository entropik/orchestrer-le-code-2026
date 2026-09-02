"""Vérifie l'extraction intégrale puis rend les PDF avec Poppler, sans les modifier.

Commande facultative de régénération : pypdf et pdftoppm requis.
Les images sont versionnées ; Hugo seul suffit ensuite pour les publier.
"""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader
from lecture_sources import pdf_pages

ROOT = Path(__file__).resolve().parents[1]


def main():
    renderer = shutil.which("pdftoppm")
    if not renderer:
        raise SystemExit("Installer Poppler (pdftoppm) pour régénérer les fac-similés.")
    inventory = json.loads((ROOT / "sources/inventaire.json").read_text(encoding="utf-8"))
    seen = set()
    for doc in inventory["documents"]:
        if not doc["fichier"].endswith(".pdf"):
            continue
        original = ROOT / "sources/originaux" / doc["fichier"]
        if hashlib.sha256(original.read_bytes()).hexdigest() != doc["sha256"]:
            raise ValueError(f"Original modifié : {doc['id']}")
        extracted = pdf_pages((ROOT / doc['extrait']).read_text(encoding="utf-8"), doc['pages'])
        actual = [p.extract_text() or "" for p in PdfReader(original).pages]
        if actual != extracted:
            raise ValueError(f"Extraction différente pour {doc['id']} : examiner avant de remplacer")
        if doc['sha256'] in seen:
            print(f"{doc['id']} : {len(actual)} pages vérifiées, fac-similés partagés.", flush=True)
            continue
        dest = ROOT / "static/source-pages" / doc['id'].lower()
        dest.mkdir(parents=True, exist_ok=True)
        subprocess.run([renderer, "-png", "-r", "120", str(original), str(dest / "page")], check=True)
        seen.add(doc['sha256'])
        print(f"{doc['id']} : {len(actual)} pages vérifiées et rendues.", flush=True)


if __name__ == "__main__":
    main()
