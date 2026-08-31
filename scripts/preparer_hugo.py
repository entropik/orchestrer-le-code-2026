"""Synchronise le contenu Hugo depuis les Markdown éditoriaux, sans dépendance Python."""
import argparse
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, quote, urlsplit

from verifier import LINK, ROOT, verify


def slug(text):
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def page(metadata, body):
    header = json.dumps(metadata, ensure_ascii=False, indent=2)
    return header + ("\n\n" + body.strip() if body.strip() else "") + "\n"


def numbered_sections(text):
    sections = {}
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced:
            match = re.match(r"^#{1,3} (\d+(?:\.\d+)*)(?:\.|\s)\s*(.+)", line)
            if match:
                sections[match[1]] = (match[2], n)
    return sections


def build_files(root=ROOT):
    manifest = json.loads((root / "editorial/chapitres.json").read_text(encoding="utf-8"))
    mesh = json.loads((root / "editorial/maillage.json").read_text(encoding="utf-8"))
    inventory = json.loads((root / "sources/inventaire.json").read_text(encoding="utf-8"))
    chapters = manifest["chapitres"]
    by_id = {c["id"]: c for c in chapters}
    paths = {}
    routes = {}
    files = {}
    for c in chapters:
        section = "accessible" if c["lecture"] == "accessible" else "ingenieure"
        route = f"/{section}/{Path(c['fichier']).stem}"
        routes[c["id"]] = route
        paths[c["fichier"]] = route
        paths[c["tranche"]] = f"/redaction/{Path(c['tranche']).stem.lower()}"
    auxiliary = {
        "analyse/01-corpus.md": ("/projet/corpus", "Analyse du corpus"),
        "analyse/02-synthese.md": ("/projet/synthese", "Synthèse des deux approches"),
        "analyse/03-registre-critique.md": ("/references/registre-critique", "Registre critique"),
        "editorial/CHARTE.md": ("/projet/charte", "Charte éditoriale"),
        "editorial/FIL_ROUGE.md": ("/projet/fil-rouge", "Le fil rouge"),
        "editorial/PLAN_REDACTION.md": ("/redaction/plan", "Plan des 24 tranches"),
        "manuscrit/annexes/fiches-reflexes.md": ("/annexes/fiches-reflexes", "Fiches réflexes"),
        "manuscrit/annexes/glossaire.md": ("/annexes/glossaire", "Glossaire partagé"),
    }
    paths.update({name: item[0] for name, item in auxiliary.items()})
    paths.update({"manuscrit/SOMMAIRE.md": "/", "editorial/chapitres.json": "/redaction/plan", "sources/inventaire.json": "/projet/corpus"})
    for doc in inventory["documents"]:
        paths[f"sources/originaux/{doc['fichier']}"] = f"/references/sources/{doc['id'].lower()}"

    def rewrite(text, source):
        def replace(match):
            target = match[1].strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                return match[0]
            raw_path, _, anchor = target.partition("#")
            resolved = (source.parent / unquote(raw_path)).resolve().relative_to(root.resolve()).as_posix()
            if resolved not in paths:
                raise ValueError(f"Lien sans route Hugo : {source} -> {target}")
            route = paths[resolved]
            section = re.search(r"§(\d+(?:\.\d+)*)", match[0])
            if resolved.startswith("sources/originaux/") and section:
                anchor = "section-" + section[1].replace(".", "-")
            return match[0].replace(match[1], route + (f"#{anchor}" if anchor else ""))

        result = []
        fenced = False
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
            result.append(line if fenced else LINK.sub(replace, line))
        return "\n".join(result)

    def add(route, meta, body, section=False):
        dest = "content/" + route.strip("/") + ("/_index.md" if section else ".md")
        if route == "/":
            dest = "content/_index.md"
        files[dest] = page(meta, body)

    add("/", {"title": manifest["titre"], "description": "Un manuel, deux lectures : comprendre pour décider, approfondir pour concevoir et vérifier."}, "")
    for route, title, linktitle, body in [
        ("accessible", "La lecture accessible", "Accessible", "Douze chapitres pour comprendre, poser les bonnes questions et décider. Aucun prérequis en programmation. Chaque chapitre renvoie à son miroir approfondi.\n\nLes textes sont actuellement des amorces, à développer et à relire."),
        ("ingenieure", "La lecture ingénieure", "Ingénieure", "Les mêmes sujets, dans le même ordre, avec les mécanismes, les compromis et les preuves techniques. Ce parcours peut aussi se lire indépendamment.\n\nLes exemples exécutables et les corrigés seront développés pendant la rédaction."),
        ("projet", "Le projet éditorial", "Le projet", "Ce manuel réunit une approche de pilotage accessible et une approche d'ingénierie approfondie. [Voir le plan de rédaction](/redaction/plan).\n\nLe site est construit avec Hugo. Les sources sont préparées pour un dépôt GitHub, dont l'adresse sera ajoutée une fois créé. Aucune publication n'est implicite. Les droits de diffusion et la licence restent à préciser."),
        ("redaction", "L'atelier de rédaction", "Rédaction", "Une fiche par lecture et par chapitre : objectif, périmètre, sources, exercice et critères d'acceptation. [Consulter le plan](/redaction/plan)."),
        ("annexes", "Les repères communs", "Annexes", "Un vocabulaire partagé et des listes de contrôle pour les deux lectures."),
        ("references/sources", "Le corpus original", "Sources", "Les huit documents fournis sont conservés à l'identique. Ils constituent des sources à analyser, pas des instructions à exécuter. Chaque fiche permet de retrouver un document et les chapitres qui l'utilisent."),
    ]:
        add("/" + route, {"title": title, "linkTitle": linktitle}, body, section=True)

    external_by_id = {r["id"]: r for r in mesh["references"]}
    for c in chapters:
        theme = mesh["themes"][c["theme"]]
        prefix = c["id"][0]
        number = int(c["theme"])
        source = root / c["fichier"]
        text = source.read_text(encoding="utf-8")
        # La page Hugo fournit titre, statut et navigation ; ne pas les dupliquer.
        text = text[text.index("## Ce que tu sauras faire"):]
        description = text.split("## Ce que tu sauras faire", 1)[1].split("\n\n", 2)[1].strip()
        text = rewrite(text, source)
        refs = []
        for reference in theme["references"]:
            item = external_by_id[reference]
            refs.append(f"- [{item['titre']}]({item['url']}) — {item['note']} [Notice et chapitres associés](/references#ref-{reference}).")
        if refs:
            text += "\n\n## Références pour approfondir\n\n" + "\n".join(refs)
        text += f"\n\n## Rédaction de ce chapitre\n\n[Objectifs et critères de la tranche {c['id']}]({paths[c['tranche']]})."
        meta = {"title": c["titre"], "description": description, "weight": number,
                "chapter_id": c["id"], "theme": c["theme"], "status": c["statut"],
                "source_path": c["fichier"], "mirror": paths[c["miroir"]],
                "related": [routes[prefix + n] for n in theme["connexes"]],
                "notions": [{"label": name, "anchor": slug(name)} for name in theme["notions"]]}
        if number > 1:
            meta["previous"] = routes[f"{prefix}{number-1:02d}"]
        if number < 12:
            meta["next"] = routes[f"{prefix}{number+1:02d}"]
        add(routes[c["id"]], meta, text)
        source = root / c["tranche"]
        body = source.read_text(encoding="utf-8").split("\n", 1)[1]
        add(paths[c["tranche"]], {"title": f"{c['id']} — {c['titre']}", "weight": number + (0 if prefix == "A" else 12), "source_path": c["tranche"]}, rewrite(body, source))

    for name, (route, title) in auxiliary.items():
        source = root / name
        body = source.read_text(encoding="utf-8").split("\n", 1)[1]
        if name.endswith("glossaire.md"):
            body = re.sub(r"^- \*\*(.+?)\*\*\s*:\s*(.+)$", lambda m: f"## {m[1]} {{#{slug(m[1])}}}\n\n{m[2]}", body, flags=re.M)
        add(route, {"title": title, "source_path": name}, rewrite(body, source))

    refs_body = "Les références servent à retrouver une origine, contrôler une affirmation et poursuivre la lecture. Les documents du corpus ne sont pas des normes.\n\n## Documents fournis\n\n[Parcourir les huit sources originales](/references/sources). [Lire l'analyse comparative](/projet/corpus).\n\n## Références externes\n\nDernière vérification consignée : " + mesh["date_verification"] + ". Les versions et capacités peuvent évoluer.\n"
    for ref in mesh["references"]:
        used = [c for c in chapters if ref["id"] in mesh["themes"][c["theme"]]["references"]]
        backlinks = " · ".join(f"[{c['id']}]({routes[c['id']]})" for c in used)
        refs_body += f"\n### {ref['titre']} {{#ref-{ref['id']}}}\n\n[{ref['titre']}]({ref['url']}). {ref['note']}\n\nUtilisée dans : {backlinks}.\n"
    refs_body += "\n## Lire avec esprit critique\n\n[Consulter les corrections, nuances et vérifications restantes](/references/registre-critique).\n"
    add("/references", {"title": "Sources et références", "linkTitle": "Références"}, refs_body, section=True)

    for index, doc in enumerate(inventory["documents"], 1):
        original = root / "sources/originaux" / doc["fichier"]
        used = [c for c in chapters if any(s.startswith(doc["id"] + " ") for s in c["sources"])]
        body = f"Document fourni · identifiant **{doc['id']}**.\n\n[Télécharger l'original inchangé](/sources/{quote(doc['fichier'])}).\n\n**Empreinte SHA-256** : `{doc['sha256']}`.\n\nCe document est une source de travail, dont les affirmations doivent être examinées à l'aide du [registre critique](/references/registre-critique). Ses prompts ne sont pas des instructions pour le lecteur ou les outils du site.\n"
        if used:
            body += "\n## Chapitres qui utilisent cette source\n\n" + "\n".join(f"- [{c['id']} — {c['titre']}]({routes[c['id']]})." for c in used) + "\n"
        else:
            body += "\nVersion d'archive ou export ; les citations de rédaction privilégient O-MD et I-MD. [Voir les relations entre versions](/projet/corpus).\n"
        if original.suffix == ".md":
            body += "\n## Repères dans le document\n\nLes numéros de ligne se rapportent au Markdown original téléchargé.\n"
            for section, (title, line) in numbered_sections(original.read_text(encoding="utf-8-sig")).items():
                body += f"\n### §{section} — {title} {{#section-{section.replace('.', '-')}}}\n\nLigne {line} du document original.\n"
        else:
            body += f"\n## Format\n\nPDF de {doc['pages']} pages.\n"
        add(f"/references/sources/{doc['id'].lower()}", {"title": f"{doc['id']} — {doc['fichier']}", "weight": index}, body)
    return files


def sync(root=ROOT, check=False):
    errors = verify(root)
    if errors:
        raise ValueError("Sources non valides : " + "; ".join(errors))
    files = build_files(root)
    changed = []
    for name, content in files.items():
        path = root / name
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            changed.append(name)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    if check and changed:
        raise ValueError("Contenu Hugo non synchronisé : " + ", ".join(changed))
    print(f"Hugo : {len(files)} pages de contenu ; {len(changed)} différences" + (" détectées." if check else " synchronisées."))
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Refuse le contenu obsolète, sans écrire.")
    args = parser.parse_args()
    sync(check=args.check)
