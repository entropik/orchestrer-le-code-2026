export type EtatDocument = "prepare" | "en_cours" | "recu" | "valide" | "rejete";

export type Commande = {
  commandeId: string;
  organisationId: string;
  document: string;
};

export type InformationsDocument = {
  chemin: string;
  tailleOctets: number;
  signature: string;
};

export type Rapport = {
  etat: "valide" | "rejete";
  chemin: string;
  tailleOctets: number;
  raisons: string[];
};
