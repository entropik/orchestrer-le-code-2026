import { scopes, normalize, prepareEntries, findEntries, excerpt, createIndexLoader } from "./search-core.mjs";

const searchLink = document.querySelector("[data-search-link]");
const form = document.querySelector("#manual-search");
const input = document.querySelector("#search-query");

// Même raccourci que Digest, sans intercepter les champs de saisie.
document.addEventListener("keydown", (event) => {
  if (event.key !== "/" || event.ctrlKey || event.metaKey || event.altKey || event.isComposing ||
      event.target.closest("input, textarea, select, [contenteditable], [role=textbox]") ||
      document.querySelector("dialog[open]")) return;
  if (input) { event.preventDefault(); input.focus(); }
  else if (searchLink) { event.preventDefault(); window.location.assign(searchLink.href); }
});

if (form) {
  const scope = document.querySelector("#search-scope");
  const results = document.querySelector("#search-results");
  const status = document.querySelector("#search-status");
  const more = document.querySelector("#search-more");
  const retry = document.querySelector("#search-retry");
  const clear = document.querySelector("#search-clear");
  const pageSize = 20;
  let revision = 0;
  let limit = pageSize;
  let matches = [];
  let renderedQuery = "";
  const loadIndex = createIndexLoader(form.dataset.indexUrl,
    (entries) => prepareEntries(entries, window.location.origin, form.dataset.baseUrl));

  function updateURL() {
    const url = new URL(window.location.href);
    input.value.trim() ? url.searchParams.set("q", input.value.trim()) : url.searchParams.delete("q");
    scope.value !== "all" ? url.searchParams.set("scope", scope.value) : url.searchParams.delete("scope");
    window.history.replaceState(null, "", url);
  }

  function render(append = false) {
    const offset = append ? results.children.length : 0;
    if (!append) results.replaceChildren();
    const fragment = document.createDocumentFragment();
    for (const entry of matches.slice(offset, limit)) {
      const item = document.createElement("li");
      const meta = document.createElement("p");
      meta.className = "search-result-meta";
      meta.textContent = [entry.i, scopes[entry.c]].filter(Boolean).join(" · ");
      const heading = document.createElement("h2");
      const link = document.createElement("a");
      link.href = entry.u;
      link.textContent = entry.t;
      heading.append(link);
      const summary = document.createElement("p");
      summary.className = "search-excerpt";
      summary.textContent = excerpt(entry, renderedQuery);
      item.append(meta, heading, summary);
      fragment.append(item);
    }
    results.append(fragment);
    const count = matches.length;
    status.textContent = count
      ? `${count} résultat${count > 1 ? "s" : ""} pour « ${renderedQuery} »${count > limit ? ` · ${limit} affichés` : ""}.`
      : `Aucun résultat pour « ${renderedQuery} ». Essaie un terme plus simple ou un autre parcours.`;
    more.hidden = count <= limit;
    if (append) results.children[offset]?.querySelector("a")?.focus();
  }

  async function search({ syncURL = true } = {}) {
    const request = ++revision;
    const query = input.value.slice(0, 160).trim();
    const selectedScope = scope.value;
    if (syncURL) updateURL();
    clear.hidden = !query && selectedScope === "all";
    retry.hidden = true;
    more.hidden = true;
    results.replaceChildren();
    limit = pageSize;
    if (!normalize(query)) {
      results.removeAttribute("aria-busy");
      status.textContent = "Saisis quelques mots pour explorer le manuel.";
      return;
    }
    status.textContent = "Recherche en cours…";
    results.setAttribute("aria-busy", "true");
    try {
      const entries = await loadIndex();
      if (request !== revision) return;
      matches = findEntries(entries, query, selectedScope);
      renderedQuery = query;
      render();
    } catch {
      if (request !== revision) return;
      status.textContent = "L’index de recherche n’a pas pu être chargé. Tu peux réessayer ou revenir au sommaire.";
      retry.hidden = false;
    } finally {
      if (request === revision) results.removeAttribute("aria-busy");
    }
  }

  function restoreQuery() {
    const params = new URL(window.location.href).searchParams;
    input.value = (params.get("q") || "").slice(0, 160);
    scope.value = Object.keys(scopes).includes(params.get("scope")) ? params.get("scope") : "all";
    void search({ syncURL: false });
  }

  form.addEventListener("submit", (event) => { event.preventDefault(); void search(); });
  input.addEventListener("input", () => { void search(); });
  scope.addEventListener("change", () => { void search(); });
  clear.addEventListener("click", () => { input.value = ""; scope.value = "all"; void search(); input.focus(); });
  retry.addEventListener("click", () => { void search(); });
  more.addEventListener("click", () => { limit += pageSize; render(true); });
  window.addEventListener("popstate", restoreQuery);
  restoreQuery();
}
