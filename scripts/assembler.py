"""Assemble les deux lectures Markdown, sans exécuter les exemples du corpus."""
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from verifier import LINK, ROOT, verify


def relocate(text, source, destination):
    def replace(match):
        target = match.group(1).strip().strip("<>")
        if target.startswith("#") or urlsplit(target).scheme:
            return match.group(0)
        path, sep, anchor = target.partition("#")
        absolute = (source.parent / unquote(path)).resolve()
        relative = Path(os.path.relpath(absolute, destination.parent)).as_posix()
        suffix = sep + anchor if sep else ""
        return match.group(0).replace(match.group(1), f"<{relative}{suffix}>")

    output, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and not line.lstrip().startswith("```"):
            line = LINK.sub(replace, line)
            line = re.sub(r"^(#{1,4}) ", r"##\1 ", line)
        output.append(line)
    return "\n".join(output)


def build(root=ROOT):
    errors = verify(root)
    if errors:
        raise ValueError("Assemblage refusé : " + "; ".join(errors))
    manifest = json.loads((root / "editorial/chapitres.json").read_text(encoding="utf-8"))
    chapters = manifest["chapitres"]
    output = root / "dist"
    output.mkdir(exist_ok=True)
    variants = [("orchestrer-le-code-2026.md", chapters),
                ("lecture-accessible.md", [c for c in chapters if c["lecture"] == "accessible"]),
                ("lecture-ingenieure.md", [c for c in chapters if c["lecture"] == "ingenieure"])]
    for filename, selected in variants:
        destination = output / filename
        validated = sum(c["statut"] == "valide" for c in selected)
        status = "Chapitres validés" if validated == len(selected) else "Manuscrit de travail - amorces et rédaction en cours"
        parts = [f"# {manifest['titre']}\n\n{status}.\n\n{validated}/{len(selected)} chapitres validés.\n\nLes renvois locaux restent liés au dépôt ; ce fichier n'est pas une édition autonome publiée."]
        previous = None
        for c in selected:
            if c["lecture"] != previous:
                parts.append("## Partie I - Lecture accessible" if c["lecture"] == "accessible" else "## Partie II - Lecture ingénieure")
                previous = c["lecture"]
            source = root / c["fichier"]
            parts.append(relocate(source.read_text(encoding="utf-8"), source, destination))
        parts.append("## Annexes communes")
        for source in sorted((root / "manuscrit/annexes").glob("*.md")):
            parts.append(relocate(source.read_text(encoding="utf-8"), source, destination))
        destination.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
        print(f"Créé : {destination.relative_to(root)} ({len(selected)} chapitres, {validated} validés)")
    return [output / name for name, _ in variants]


if __name__ == "__main__":
    build()
