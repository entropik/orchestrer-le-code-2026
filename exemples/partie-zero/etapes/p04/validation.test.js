import test from "node:test";
import assert from "node:assert/strict";
import { evaluerDocument, TAILLE_MAXIMALE } from "../p03/validation.js";

test("accepte la limite exacte", () => {
  assert.equal(evaluerDocument({ chemin: "affiche.pdf", tailleOctets: TAILLE_MAXIMALE, signature: "%PDF-" }).etat, "valide");
});

test("rejette le vide", () => {
  assert.deepEqual(evaluerDocument({ chemin: "vide.pdf", tailleOctets: 0, signature: "%PDF-" }).raisons, ["Le document est vide."]);
});

test("rejette la mauvaise extension", () => {
  assert.equal(evaluerDocument({ chemin: "affiche.txt", tailleOctets: 12, signature: "%PDF-" }).etat, "rejete");
});

test("rejette la signature absente", () => {
  assert.equal(evaluerDocument({ chemin: "affiche.pdf", tailleOctets: 12, signature: "texte" }).etat, "rejete");
});
