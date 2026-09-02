import { open, readFile, stat } from "node:fs/promises";
import { resolve } from "node:path";
import type { Commande, InformationsDocument } from "./types.js";

function exigerTexte(objet: Record<string, unknown>, propriete: string): string {
  const valeur = objet[propriete];
  if (typeof valeur !== "string" || valeur.trim() === "") {
    throw new Error(`La propriété ${propriete} doit être un texte non vide.`);
  }
  return valeur;
}

export async function lireCommande(chemin: string): Promise<Commande> {
  const valeur: unknown = JSON.parse(await readFile(chemin, "utf8"));
  if (typeof valeur !== "object" || valeur === null || Array.isArray(valeur)) {
    throw new Error("La commande doit être un objet JSON.");
  }
  const objet = valeur as Record<string, unknown>;
  return {
    commandeId: exigerTexte(objet, "commandeId"),
    organisationId: exigerTexte(objet, "organisationId"),
    document: exigerTexte(objet, "document")
  };
}

export async function inspecterDocument(chemin: string): Promise<InformationsDocument> {
  const cheminAbsolu = resolve(chemin);
  const informations = await stat(cheminAbsolu);
  const fichier = await open(cheminAbsolu, "r");
  try {
    const debut = Buffer.alloc(5);
    await fichier.read(debut, 0, debut.length, 0);
    return { chemin, tailleOctets: informations.size, signature: debut.toString("ascii") };
  } finally {
    await fichier.close();
  }
}
