"""Vérifie hors réseau les liens, ancres et ressources d'un rendu Hugo."""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.h1 = 0
        self.language = None
        self.title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "title":
            self.title = True
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in {"img", "script"} and "src" in attrs:
            self.links.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.links.append(attrs["href"])


def verify_html(directory, base_path="/"):
    directory = directory.resolve()
    base_path = "/" + base_path.strip("/") + "/" if base_path.strip("/") else "/"
    pages = {}
    errors = []
    for path in directory.rglob("*.html"):
        parsed = Page()
        parsed.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parsed
        if parsed.h1 != 1 or parsed.language != "fr" or not parsed.title:
            errors.append(f"Structure HTML incorrecte : {path.relative_to(directory)}")
        for ident, count in Counter(parsed.ids).items():
            if count > 1:
                errors.append(f"Ancre dupliquée : {path.relative_to(directory)}#{ident}")
    if not pages:
        errors.append("Aucune page HTML à vérifier ; exécuter Hugo d'abord.")
    checked = 0
    for path, parsed in pages.items():
        current = base_path + path.relative_to(directory).as_posix()
        for target in parsed.links:
            parts = urlsplit(target)
            if parts.scheme in {"http", "https", "mailto", "tel"} or target.startswith("//"):
                continue
            if parts.scheme:
                errors.append(f"Protocole inattendu : {target}")
                continue
            resolved = urlsplit(urljoin(current, target))
            decoded = unquote(resolved.path)
            if not decoded.startswith(base_path):
                errors.append(f"Lien hors base {base_path} : {target}")
                continue
            destination = (directory / decoded[len(base_path):]).resolve()
            if not destination.is_relative_to(directory):
                errors.append(f"Lien hors site : {target}")
                continue
            if destination.is_dir():
                destination /= "index.html"
            if not destination.is_file():
                errors.append(f"Lien cassé : {path.relative_to(directory)} -> {target}")
            elif resolved.fragment and destination.suffix == ".html":
                if unquote(resolved.fragment) not in pages[destination].ids:
                    errors.append(f"Ancre absente : {path.relative_to(directory)} -> {target}")
            checked += 1
    return errors, len(pages), checked


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=ROOT / "public")
    parser.add_argument("--base-path", default="/")
    args = parser.parse_args()
    errors, count, links = verify_html(args.directory, args.base_path)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"OK : {count} pages HTML ; {links} liens, ancres et ressources internes vérifiés.")
    print("Les liens externes sont conservés, mais ne sont pas interrogés par ce contrôle hors réseau.")
