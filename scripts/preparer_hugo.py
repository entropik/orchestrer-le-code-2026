"""Synchronise le contenu Hugo depuis les Markdown éditoriaux, sans dépendance Python."""
import argparse
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, quote, urlsplit

from verifier import LINK, ROOT, verify
from lecture_sources import markdown_integral, pdf_pages
from preparer_schemas_manuscrit import build_manuscrit_registry


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
        "editorial/CHARTE.md": ("/projet/charte", "Charte éditoriale & Droits"),
        "editorial/FIL_ROUGE.md": ("/projet/fil-rouge", "Le fil rouge"),
        "editorial/PLAN_REDACTION.md": ("/redaction/plan", "Plan des 24 tranches"),
        "manuscrit/01-lecture-accessible/00-avant-la-premiere-ligne.md": (
            "/accessible/avant-propos",
            "Avant la première ligne : L'art de l'introspection, du terrain et du choix des armes",
            0,
            "Avant le premier prompt : introspection, cadrage du besoin, choix d'une stack sobre et cas vécu du moteur de carnet photo.",
        ),
        "manuscrit/03-annexes/01-fiches-reflexes.md": ("/annexes/fiches-reflexes", "Fiches réflexes", 1, "Listes de contrôle communes pour lancer, vérifier et livrer."),
        "manuscrit/03-annexes/02-guide-des-workflows.md": ("/annexes/workflows", "Guide des workflows & Cas pratiques", 2, "Le ruban principal, l'arbre d'aiguillage et les 7 trames d'exécution pas à pas."),
        "manuscrit/03-annexes/03-architecture-du-harnais.md": ("/annexes/architecture-harnais", "Architecture du harnais & Smart Zone", 3, "Doctrine racine vs global, modèle 3 couches, gestion des tokens et règles d'or."),
        "manuscrit/03-annexes/04-catalogue-des-skills.md": ("/annexes/catalogue-skills", "Catalogue des 37 skills", 4, "Inventaire complet des compétences en fiches dépliables avec permaliens directs."),
        "manuscrit/03-annexes/05-glossaire.md": ("/annexes/glossaire", "Glossaire partagé", 5, "Définitions des termes clés du domaine et de l'architecture."),
        "manuscrit/03-annexes/06-ressources-utiles.md": (
            "/annexes/ressources-utiles",
            "Ressources utiles & Observatoire des modèles",
            6,
            "Bancs d'essai, comparateurs de modèles, observatoires de prix et outils de référence pour orchestrer le code.",
        ),
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
    add("/recherche", {"title": "Chercher dans le manuel", "linkTitle": "Rechercher", "layout": "search", "description": "Retrouver un chapitre, une notion ou une référence dans les deux lectures."}, "")
    for route, title, linktitle, body in [
        ("accessible", "La lecture accessible", "Accessible", "Douze chapitres pour comprendre, poser les bonnes questions et décider. Aucun prérequis en programmation. Chaque chapitre renvoie à son miroir approfondi."),
        ("ingenieure", "La lecture ingénieure", "Ingénieure", "Les mêmes sujets, dans le même ordre, avec les mécanismes, les compromis et les preuves techniques. Ce parcours peut aussi se lire indépendamment."),
        ("projet", "Le projet éditorial", "Le projet", "Ce manuel réunit une approche de pilotage accessible et une approche d'ingénierie approfondie. [Voir le plan de rédaction](/redaction/plan).\n\nLe site est propulsé par Hugo, sans traceur ni dépendance superflue. Le code et les sources sont suivis sur le [dépôt GitHub](https://github.com/entropik/orchestrer-le-code-2026). Les textes sont sous licence CC BY-NC-ND 4.0 et le code d'ingénierie sous licence MIT. [Consulter la charte éditoriale et les droits d'auteur](/projet/charte)."),
        ("redaction", "L'atelier de rédaction", "Rédaction", "Une fiche par lecture et par chapitre : objectif, périmètre, sources, exercice et critères d'acceptation. [Consulter le plan](/redaction/plan)."),
        ("annexes", "Les repères communs", "Annexes", "{{< ask_matt_simulator >}}\n\nUn vocabulaire partagé, une tour de contrôle d'aiguillage et les repères méthodologiques pour les deux lectures."),
        ("references/sources", "Le corpus original", "Sources", "Les huit documents sont lisibles intégralement ici et conservés à l'identique au téléchargement. Les Markdown se parcourent par sections ; les PDF, page par page, avec leur texte extrait et leur fac-similé. Aucun texte n'est résumé ni corrigé. Les instructions citées font partie des documents, pas du fonctionnement du site."),
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
        elif prefix == "A" and number == 1:
            meta["previous"] = "/accessible/avant-propos"
        if number < 12:
            meta["next"] = routes[f"{prefix}{number+1:02d}"]
        add(routes[c["id"]], meta, text)
        source = root / c["tranche"]
        body = source.read_text(encoding="utf-8").split("\n", 1)[1]
        add(paths[c["tranche"]], {"title": f"{c['id']} — {c['titre']}", "weight": number + (0 if prefix == "A" else 12), "source_path": c["tranche"]}, rewrite(body, source))

    for name, item in auxiliary.items():
        route, title = item[0], item[1]
        weight = item[2] if len(item) > 2 else None
        description = item[3] if len(item) > 3 else None
        source = root / name
        body = source.read_text(encoding="utf-8").split("\n", 1)[1]
        if name.endswith("glossaire.md"):
            body = re.sub(r"^- \*\*(.+?)\*\*\s*:\s*(.+)$", lambda m: f"## {m[1]} {{#{slug(m[1])}}}\n\n{m[2]}", body, flags=re.M)
        meta = {"title": title, "source_path": name}
        if weight is not None:
            meta["weight"] = weight
        if description is not None:
            meta["description"] = description
        if name.endswith("02-guide-des-workflows.md"):
            meta["aliases"] = ["/annexes/workflows-agentiques"]
        if name.endswith("CHARTE.md"):
            meta["aliases"] = ["/projet/droits"]
        if name.endswith("00-avant-la-premiere-ligne.md"):
            meta["next"] = routes["A01"]
            meta["eyebrow"] = "Avant-propos opérationnel"
            meta["theme"] = "00"
        add(route, meta, rewrite(body, source))

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
        body = f"Lecture intégrale · **{doc['id']}**. [Télécharger l'original inchangé](/sources/{quote(doc['fichier'])}).\n\n"
        if original.suffix == ".md":
            body += "Le texte ci-dessous est celui du Markdown original, sans résumé ni correction. Seuls sa présentation et ses liens de navigation sont adaptés au site.\n\n---\n\n"
            body += markdown_integral(original.read_text(encoding="utf-8-sig"))
        else:
            body += "Tout le texte extrait du PDF est reproduit ci-dessous, page par page, sans nettoyage ni reformulation. L'extraction peut déplacer des éléments ou restituer imparfaitement certains caractères et tableaux : le fac-similé de chaque page permet de lire la mise en page originale, sans téléchargement.\n\n"
            pages = pdf_pages((root / doc['extrait']).read_text(encoding="utf-8"), doc['pages'])
            # Les deux exports identiques partagent leurs images, pas leurs adresses.
            canonical = next(d['id'].lower() for d in inventory['documents'] if d['sha256'] == doc['sha256'])
            files[f"data/source_pages/{doc['id'].lower()}.json"] = json.dumps(pages, ensure_ascii=False, indent=2) + "\n"
            for n in range(1, len(pages) + 1):
                body += f'\n## Page {n} {{#page-{n}}}\n\n{{{{< source-pdf id="{doc["id"].lower()}" page="{n}" images="{canonical}" >}}}}\n'
        body += f"\n\n---\n\n## À propos de cette source {{#notice-source}}\n\n**Empreinte SHA-256 de l'original** : `{doc['sha256']}`.\n\nLes affirmations et prompts sont reproduits comme éléments du document, sans validation ni exécution. [Consulter le registre critique](/references/registre-critique).\n"
        if used:
            body += "\n## Chapitres qui utilisent cette source\n\n" + "\n".join(f"- [{c['id']} — {c['titre']}]({routes[c['id']]})." for c in used) + "\n"
        else:
            body += "\nVersion d'archive ou export ; les citations de rédaction privilégient O-MD et I-MD. [Voir les relations entre versions](/projet/corpus).\n"
        add(f"/references/sources/{doc['id'].lower()}", {"title": f"{doc['id']} — {doc['fichier']}", "weight": index, "source_document": True}, body)
    files["data/diagrams/manuscrit.json"] = json.dumps(build_manuscrit_registry(root), ensure_ascii=False, indent=2) + "\n"
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
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
    if check and changed:
        raise ValueError("Contenu Hugo non synchronisé : " + ", ".join(changed))
    print(f"Hugo : {sum(name.startswith('content/') for name in files)} pages de contenu ; {len(changed)} fichiers" + (" désynchronisés." if check else " synchronisés."))
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Refuse le contenu obsolète, sans écrire.")
    args = parser.parse_args()
    sync(check=args.check)
