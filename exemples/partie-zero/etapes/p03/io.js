import { open, readFile, stat } from "node:fs/promises";
import { resolve } from "node:path";

export async function lireCommande(chemin) {
  return JSON.parse(await readFile(resolve(chemin), "utf8"));
}

export async function inspecterDocument(chemin) {
  const informations = await stat(resolve(chemin));
  const fichier = await open(resolve(chemin), "r");
  try {
    const debut = Buffer.alloc(5);
    await fichier.read(debut, 0, 5, 0);
    return { chemin, tailleOctets: informations.size, signature: debut.toString("ascii") };
  } finally {
    await fichier.close();
  }
}
