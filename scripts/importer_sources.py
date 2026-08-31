"""Copie sans écrasement et extrait les huit sources fournies (pypdf requis)."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ("I-MD", "MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md"),
    ("O-MD", "manuel_orchestration_logicielle.md"),
    ("S-MD", "MANUEL_ARCHITECTURE_SYSTEMIQUE_COMPLET.md"),
    ("SF-MD", "MANUEL_ARCHITECTURE_SYSTEMIQUE_COMPLET_EDITION_FINALE.md"),
    ("S-PDF", "manuel_architecture_systemique_complet.pdf"),
    ("O-PDF", "manuel_orchestration_logicielle.pdf"),
    ("O1-PDF", "manuel_orchestration_logicielle (1).pdf"),
    ("O2-PDF", "manuel_orchestration_logicielle (2).pdf"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path)
    args = parser.parse_args()
    from pypdf import PdfReader

    original = ROOT / "sources/originaux"
    extracts = ROOT / "sources/extraits"
    original.mkdir(parents=True, exist_ok=True)
    extracts.mkdir(parents=True, exist_ok=True)
    records = []
    for ident, name in FILES:
        source = args.source_dir / name
        target = original / name
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                raise SystemExit(f"Refus d'écraser une source différente : {target}")
        else:
            shutil.copy2(source, target)
        record = {"id": ident, "fichier": name, "sha256": digest, "octets": target.stat().st_size}
        if target.suffix == ".pdf":
            reader = PdfReader(target)
            pages = [p.extract_text() or "" for p in reader.pages]
            content = "\n\n".join(f"<!-- page {n} -->\n{text}" for n, text in enumerate(pages, 1))
            record["pages"] = len(pages)
            record["mots_par_page"] = [len(p.split()) for p in pages]
        else:
            content = target.read_text(encoding="utf-8-sig")
            record["lignes"] = len(content.splitlines())
        record["mots_extraits"] = len(content.split())
        record["extrait"] = f"sources/extraits/{ident}.txt"
        (extracts / f"{ident}.txt").write_text(content, encoding="utf-8")
        records.append(record)
    (ROOT / "sources/inventaire.json").write_text(
        json.dumps({"date_analyse": "2026-08-31", "documents": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for r in records:
        print(f"{r['id']}: {r['octets']} octets, {r.get('pages', '-')} pages, {r['mots_extraits']} mots, SHA256 {r['sha256']}")


if __name__ == "__main__":
    main()
