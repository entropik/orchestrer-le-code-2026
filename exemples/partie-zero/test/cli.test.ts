import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

const programme = resolve("dist/src/index.js");

function lancer(fixture?: string) {
  return spawnSync(process.execPath, [programme, ...(fixture ? [fixture] : [])], { encoding: "utf8" });
}

test("la commande valide retourne 0", () => {
  const resultat = lancer("fixtures/commande-valide.json");
  assert.equal(resultat.status, 0, resultat.stderr);
  assert.equal(JSON.parse(resultat.stdout).etat, "valide");
});

test("un rejet métier retourne 1", () => {
  const resultat = lancer("fixtures/commande-rejetee.json");
  assert.equal(resultat.status, 1, resultat.stderr);
  assert.equal(JSON.parse(resultat.stdout).etat, "rejete");
});

test("un fichier absent retourne 2", () => {
  const resultat = lancer("fixtures/commande-introuvable.json");
  assert.equal(resultat.status, 2);
  assert.match(resultat.stderr, /ENOENT/);
});

test("un argument absent retourne 2 et explique l'usage", () => {
  const resultat = lancer();
  assert.equal(resultat.status, 2);
  assert.match(resultat.stderr, /Usage/);
});
