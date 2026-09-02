import test from "node:test";
import assert from "node:assert/strict";
import { evaluerDocument, TAILLE_MAXIMALE } from "../src/validation.js";

test("accepte un PDF non vide à la taille maximale", () => {
  const rapport = evaluerDocument({ chemin: "affiche.pdf", tailleOctets: TAILLE_MAXIMALE, signature: "%PDF-" });
  assert.equal(rapport.etat, "valide");
  assert.deepEqual(rapport.raisons, []);
});

test("distingue un document vide", () => {
  const rapport = evaluerDocument({ chemin: "vide.pdf", tailleOctets: 0, signature: "%PDF-" });
  assert.equal(rapport.etat, "rejete");
  assert.deepEqual(rapport.raisons, ["Le document est vide."]);
});

test("cumule les raisons de rejet", () => {
  const rapport = evaluerDocument({ chemin: "affiche.txt", tailleOctets: TAILLE_MAXIMALE + 1, signature: "texte" });
  assert.equal(rapport.etat, "rejete");
  assert.equal(rapport.raisons.length, 3);
});

test("rejette une signature absente", () => {
  const rapport = evaluerDocument({ chemin: "affiche.pdf", tailleOctets: 1234, signature: "-----" });
  assert.deepEqual(rapport.raisons, ["La signature PDF est absente."]);
});
