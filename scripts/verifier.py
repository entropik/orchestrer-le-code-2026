"""Contrôles structurels hors réseau ; ne valide pas la justesse du livre."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)")


def without_code(text):
    lines = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            lines.append(line)
    return "\n".join(lines)


def local_links(text):
    for match in LINK.finditer(without_code(text)):
        target = match.group(1).strip().strip("<>")
        if not target.startswith("#") and not urlsplit(target).scheme:
            yield unquote(target.split("#", 1)[0])


def validate_manifest(chapters):
    errors = []
    ids = [c["id"] for c in chapters]
    expected = {f"{p}{n:02d}" for p in "AB" for n in range(1, 13)}
    if len(ids) != len(set(ids)) or set(ids) != expected:
        errors.append("Le manifeste doit contenir exactement A01-A12 et B01-B12, sans doublon.")
    by_id = {c["id"]: c for c in chapters}
    paths = [c["fichier"] for c in chapters]
    if len(paths) != len(set(paths)):
        errors.append("Deux chapitres partagent le même fichier.")
    for c in chapters:
        if c["statut"] not in {"amorce", "redaction", "relecture", "valide"}:
            errors.append(f"{c['id']}: statut inconnu.")
        counterpart = ("B" if c["id"].startswith("A") else "A") + c["theme"]
        mirror = by_id.get(counterpart)
        if not mirror or mirror["titre"] != c["titre"] or mirror["fichier"] != c["miroir"]:
            errors.append(f"{c['id']}: miroir manquant ou incohérent.")
        for dep in c["dependances"]:
            if dep not in by_id:
                errors.append(f"{c['id']}: dépendance absente {dep}.")
    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            errors.append(f"Cycle de dépendance : {ident}.")
            return
        if ident in visited or ident not in by_id:
            return
        visiting.add(ident)
        for dep in by_id[ident]["dependances"]:
            visit(dep)
        visiting.remove(ident)
        visited.add(ident)

    for ident in by_id:
        visit(ident)
    for ident in ("A12", "B12"):
        if not any(s.startswith("I-MD §12") for s in by_id.get(ident, {}).get("sources", [])):
            errors.append(f"{ident}: le chapitre 12 de la référence complète n'est pas rattaché.")
    return errors


def verify(root=ROOT):
    manifest = json.loads((root / "editorial/chapitres.json").read_text(encoding="utf-8"))
    chapters = manifest["chapitres"]
    errors = validate_manifest(chapters)
    for c in chapters:
        for field in ("fichier", "miroir", "tranche"):
            if not (root / c[field]).is_file():
                errors.append(f"{c['id']}: fichier absent {c[field]}.")
        chapter_path = root / c["fichier"]
        if chapter_path.is_file():
            content = chapter_path.read_text(encoding="utf-8")
            for heading in ("## Ce que tu sauras faire", "## Première synthèse", "## Mise en pratique", "## Sources et limites"):
                if heading not in content:
                    errors.append(f"{c['id']}: section absente {heading}.")
            if c["statut"] == "valide" and "Amorce de synthèse" in content:
                errors.append(f"{c['id']}: annoncé valide mais encore marqué comme amorce.")
    source_ids = set()
    inventory = json.loads((root / "sources/inventaire.json").read_text(encoding="utf-8"))
    for doc in inventory["documents"]:
        source_ids.add(doc["id"])
        original = root / "sources/originaux" / doc["fichier"]
        if not original.is_file():
            errors.append(f"Source absente : {doc['fichier']}")
        elif hashlib.sha256(original.read_bytes()).hexdigest() != doc["sha256"]:
            errors.append(f"Source altérée : {doc['fichier']}")
        if not (root / doc["extrait"]).is_file():
            errors.append(f"Extraction absente : {doc['id']}")
    if len(inventory["documents"]) != 8 or "I-MD" not in source_ids:
        errors.append("Le corpus doit contenir les huit documents dont I-MD.")
    for c in chapters:
        for source in c["sources"]:
            if source.split()[0] not in source_ids:
                errors.append(f"{c['id']}: source inconnue {source}.")
    authored = [root / "README.md", root / "CONTRIBUTING.md"]
    for directory in ("analyse", "editorial", "manuscrit", "tranches"):
        authored.extend((root / directory).rglob("*.md"))
    for path in authored:
        content = path.read_text(encoding="utf-8")
        if sum(line.lstrip().startswith("```") for line in content.splitlines()) % 2:
            errors.append(f"Bloc de code non fermé : {path.relative_to(root)}")
        for target in local_links(content):
            if not (path.parent / target).resolve().exists():
                errors.append(f"Lien cassé : {path.relative_to(root)} -> {target}")
    return errors


def main():
    errors = verify()
    if errors:
        for error in errors:
            print(f"ERREUR : {error}")
        raise SystemExit(1)
    print("OK : 8 sources intactes, 12 paires, 24 tranches, dépendances et liens locaux valides.")
    print("Limites : pas de contrôle des ancres Markdown, des liens web ni de la justesse technique.")


if __name__ == "__main__":
    main()
