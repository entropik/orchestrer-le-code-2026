// Adaptation du moteur maison de Digest : normalisation, tous les termes,
// cache de l'index et nouvelle tentative après échec. Aucun service distant.
export const scopes = {
  all: "Tout le manuel",
  commencer: "Partie zéro",
  accessible: "Lecture accessible",
  ingenieure: "Lecture ingénieure",
  references: "Références et annexes",
  redaction: "Projet et rédaction",
};

export const normalize = (value = "") =>
  String(value).normalize("NFD").replace(/\p{Diacritic}/gu, "")
    .toLowerCase().replace(/œ/g, "oe").replace(/æ/g, "ae").trim();

export function prepareEntries(entries, origin, basePath = "/") {
  if (!Array.isArray(entries)) throw new Error("INDEX_INVALID");
  const base = new URL(basePath, origin);
  const unique = new Map();
  for (const entry of entries) {
    if (!entry || !["t", "u", "c", "d", "x", "i"].every((key) => typeof entry[key] === "string")) {
      throw new Error("INDEX_INVALID");
    }
    const url = new URL(entry.u, base);
    if (url.origin !== base.origin || !url.pathname.startsWith(base.pathname) ||
        !["http:", "https:"].includes(url.protocol) || !Object.keys(scopes).includes(entry.c) || entry.c === "all" ||
        (entry.g !== undefined && (!Array.isArray(entry.g) || !entry.g.every((term) => typeof term === "string")))) {
      throw new Error("INDEX_INVALID");
    }
    const title = normalize(entry.t);
    unique.set(url.href, {
      ...entry, u: url.pathname + url.search + url.hash, title,
      searchable: normalize([entry.i, entry.t, scopes[entry.c], entry.d, entry.x, ...(entry.g || [])].join(" ")),
    });
  }
  return [...unique.values()];
}

export function findEntries(entries, query, scope = "all") {
  const terms = normalize(query).split(/\s+/).filter(Boolean);
  if (!terms.length) return [];
  return entries.filter((entry) =>
    (scope === "all" || entry.c === scope) && terms.every((term) => entry.searchable.includes(term)),
  ).map((entry) => ({
    entry,
    score: terms.reduce((score, term) => score + (entry.title.includes(term) ? 10 : 0), 0) +
      (entry.i ? 2 : 0),
  })).sort((a, b) => b.score - a.score || a.entry.t.localeCompare(b.entry.t, "fr") || a.entry.u.localeCompare(b.entry.u))
    .map(({ entry }) => entry);
}

export function excerpt(entry, query, length = 230) {
  const text = entry.x || entry.d;
  const terms = normalize(query).split(/\s+/).filter(Boolean);
  const normalized = normalize(text);
  const first = terms.map((term) => normalized.indexOf(term)).filter((index) => index >= 0);
  let start = first.length ? Math.max(0, Math.min(...first) - 65) : 0;
  if (start) {
    const boundary = text.indexOf(" ", start);
    if (boundary !== -1) start = boundary + 1;
  }
  const fragment = text.slice(start, start + length).trim();
  return (start ? "… " : "") + fragment + (start + length < text.length ? "…" : "");
}

export function createIndexLoader(url, prepare, fetcher = fetch) {
  let pending;
  return () => {
    if (!pending) {
      pending = Promise.resolve().then(() => fetcher(url, {
        credentials: "same-origin", headers: { Accept: "application/json" },
      })).then((response) => {
        if (!response.ok) throw new Error(`INDEX_${response.status}`);
        return response.json();
      }).then(prepare).catch((error) => {
        pending = undefined;
        throw error;
      });
    }
    return pending;
  };
}
