import { extname } from "node:path";

export const TAILLE_MAXIMALE = 500_000_000;

export function evaluerDocument(document) {
  const raisons = [];
  if (extname(document.chemin).toLowerCase() !== ".pdf") raisons.push("Le nom du document ne se termine pas par .pdf.");
  if (document.tailleOctets <= 0) raisons.push("Le document est vide.");
  if (document.tailleOctets > TAILLE_MAXIMALE) raisons.push("Le document dépasse 500 000 000 octets.");
  if (document.signature !== "%PDF-") raisons.push("La signature PDF est absente.");
  return { etat: raisons.length ? "rejete" : "valide", chemin: document.chemin, tailleOctets: document.tailleOctets, raisons };
}
