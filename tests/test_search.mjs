import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, statSync } from "node:fs";
import { resolve } from "node:path";
import { normalize, prepareEntries, findEntries, excerpt, createIndexLoader } from "../assets/js/search-core.mjs";

const origin = "https://manuel.example";
const raw = [
  { i: "A04", t: "Harnais et contexte", u: "/accessible/04/", c: "accessible", d: "Comprendre", x: "Limiter les permissions de l’agent." },
  { i: "B04", t: "Harnais et contexte", u: "/ingenieure/04/", c: "ingenieure", d: "Concevoir", x: "Contexte, permissions et mémoire versionnée." },
  { i: "", t: "Glossaire", u: "/annexes/glossaire/", c: "references", d: "", x: "Un harnais donne du contexte à l’agent." },
];
const entries = prepareEntries(raw, origin);

test("normalisation issue de Digest : accents, casse, espaces et ligatures", () => {
  assert.equal(normalize("  ÉVALUATION ŒUVRE  "), "evaluation oeuvre");
  assert.equal(normalize("me\u0301moire"), "memoire");
});
test("tous les mots, même répartis entre titre et texte", () => {
  assert.equal(findEntries(entries, "HARNAIS permissions").length, 2);
  assert.equal(findEntries(entries, "permissions memoire")[0].i, "B04");
  assert.equal(findEntries(entries, "harnais impossible").length, 0);
});
test("filtres, titre prioritaire et requête vide", () => {
  assert.equal(findEntries(entries, "contexte", "accessible")[0].i, "A04");
  assert.equal(findEntries(entries, "contexte", "ingenieure")[0].i, "B04");
  assert.equal(findEntries(entries, "contexte").at(-1).t, "Glossaire");
  assert.deepEqual(findEntries(entries, "   "), []);
});
test("extrait centré sur un terme et contenu conservé comme texte", () => {
  const result = excerpt({ x: "Introduction. ".repeat(70) + "Une transaction atomique." }, "transaction");
  assert.match(result, /transaction/);
  assert.ok(result.length < 240);
  assert.equal(excerpt({ x: "<img src=x onerror=alert(1)>" }, "img"), "<img src=x onerror=alert(1)>");
});
test("index invalide et destinations hors site refusés", () => {
  for (const invalid of [{}, [null], [{ t: "incomplet" }]]) {
    assert.throws(() => prepareEntries(invalid, origin), /INDEX_INVALID/);
  }
  for (const u of ["javascript:alert(1)", "https://ailleurs.example/", "//ailleurs.example/"]) {
    assert.throws(() => prepareEntries([{ ...raw[0], u }], origin), /INDEX_INVALID/);
  }
});
test("préfixe de publication conservé et doublons retirés", () => {
  const prefixed = { ...raw[0], u: "/livre/accessible/04/" };
  const result = prepareEntries([prefixed, prefixed], origin, "/livre/");
  assert.equal(result.length, 1);
  assert.equal(result[0].u, prefixed.u);
  assert.throws(() => prepareEntries(raw, origin, "/livre/"), /INDEX_INVALID/);
});
test("index chargé à la demande, une seule requête pour deux recherches", async () => {
  let calls = 0;
  const load = createIndexLoader("/index.json", (data) => data, async () => {
    calls++;
    return { ok: true, json: async () => raw };
  });
  assert.equal(calls, 0);
  const [a, b] = await Promise.all([load(), load()]);
  assert.equal(calls, 1);
  assert.equal(a, b);
});
test("après une erreur réseau, un clic peut réessayer", async () => {
  let calls = 0;
  const load = createIndexLoader("/index.json", (data) => data, async () => {
    calls++;
    if (calls === 1) return { ok: false, status: 503 };
    return { ok: true, json: async () => raw };
  });
  await assert.rejects(load(), /INDEX_503/);
  assert.deepEqual(await load(), raw);
  assert.equal(calls, 2);
});

test("index Hugo réel : 24 chapitres, glossaire, références et liens existants", () => {
  const site = resolve(process.env.MANUEL_SITE_DIR || "public");
  const searchHTML = readFileSync(resolve(site, "recherche/index.html"), "utf8");
  const indexURL = searchHTML.match(/data-index-url="([^"]+)"/)[1];
  const baseURL = searchHTML.match(/data-base-url="([^"]+)"/)[1];
  const indexPath = resolve(site, indexURL.slice(baseURL.length));
  assert.ok(statSync(indexPath).size < 750_000, "Budget index : 750 Ko maximum");
  const built = prepareEntries(JSON.parse(readFileSync(indexPath, "utf8")), origin, baseURL);
  assert.equal(built.filter((entry) => /^[AB]\d{2}$/.test(entry.i)).length, 24);
  assert.ok(built.some((entry) => entry.u.endsWith("/annexes/glossaire/")));
  assert.ok(built.some((entry) => entry.u.endsWith("/references/")));
  assert.ok(!built.some((entry) => entry.u.endsWith("/recherche/")));
  assert.ok(findEntries(built, "harnais", "accessible").some((entry) => entry.i === "A04"));
  assert.equal(findEntries(built, "contexte", "accessible")[0].i, "A04");
  assert.ok(findEntries(built, "quantification", "ingenieure").some((entry) => entry.i === "B12"));
  assert.ok(findEntries(built, "thermodynamique entropie", "references").some((entry) => entry.u.endsWith("/sources/i-md/")));
  assert.ok(findEntries(built, "roulette russe", "references").some((entry) => entry.u.endsWith("/sources/o-pdf/")));
  for (const entry of built) {
    assert.ok(statSync(resolve(site, decodeURIComponent(entry.u.slice(baseURL.length)), "index.html")).isFile());
  }
});
