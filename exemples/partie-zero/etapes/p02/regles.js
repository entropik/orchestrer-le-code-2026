export const TAILLE_MAXIMALE = 500_000_000;

export function raisonsDeRejet(document) {
  const raisons = [];
  if (!document.nom.toLowerCase().endsWith(".pdf")) raisons.push("Le nom ne se termine pas par .pdf.");
  if (document.tailleOctets <= 0) raisons.push("Le document est vide.");
  if (document.tailleOctets > TAILLE_MAXIMALE) raisons.push("Le document est trop grand.");
  return raisons;
}

const exemple = { nom: "affiche.pdf", tailleOctets: 12_000 };
if (raisonsDeRejet(exemple).length) throw new Error("L'exemple nominal devrait être accepté.");
console.log("P02 : règles exécutées.");
