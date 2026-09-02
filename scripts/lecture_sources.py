"""Présentation des sources intégrales ; aucune correction ni synthèse du texte."""
import re


def markdown_integral(text):
    """Ne change que niveaux/ancres de titres, cibles du sommaire et balises br.

    Les blocs de code restent identiques. Les numéros de chapitre sont pris
    sur h1/h2, jamais sur les sous-listes numérotées h3 (ex. indexation SQL).
    """
    result = []
    fence = None
    anchors = set()
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            result.append(line)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            result.append(line)
            continue
        # Ne jamais interpréter des shortcodes éventuellement ajoutés au corpus.
        if re.search(r"\{\{[<%]", line):
            raise ValueError("Shortcode dans une source : présentation littérale à prévoir")
        heading = re.match(r"^(#{1,6}) (.*?)(\r?\n)?$", line)
        if heading:
            level, title, newline = heading[1], heading[2], heading[3] or ""
            section = re.match(r"(\d+(?:\.\d+)*)(?:\.|\s)\s*", title)
            anchor = ""
            if section and len(level) <= 2:
                ident = "section-" + section[1].replace(".", "-")
                if ident in anchors:
                    raise ValueError(f"Section dupliquée : {ident}")
                anchors.add(ident)
                anchor = f" {{#{ident}}}"
            line = "#" * min(len(level) + 1, 6) + " " + title + anchor + newline
        line = re.sub(r"\]\(#(\d+(?:\.\d+)*)-[^)]+\)",
                      lambda m: "](#section-" + m[1].replace(".", "-") + ")", line)
        line = line.replace("<br>", ' {{< source-break >}} ')
        result.append(line)
    if fence:
        raise ValueError("Bloc de code non fermé dans la source")
    return "".join(result)


def pdf_pages(text, expected):
    """Découpe uniquement les marqueurs de l'import ; aucun caractère élagué."""
    matches = list(re.finditer(r"<!-- page (\d+) -->\n", text))
    if [int(m[1]) for m in matches] != list(range(1, expected + 1)):
        raise ValueError("Pagination de l'extraction PDF incomplète")
    if matches[0].start() != 0:
        raise ValueError("Texte inattendu avant la première page PDF")
    pages = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() - 2 if i + 1 < len(matches) else len(text)
        pages.append(text[match.end():end])
    reconstructed = "\n\n".join(f"<!-- page {i} -->\n{body}" for i, body in enumerate(pages, 1))
    if reconstructed != text:
        raise ValueError("Extraction non réversible")
    return pages
