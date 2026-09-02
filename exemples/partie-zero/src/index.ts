import { resolve } from "node:path";
import { inspecterDocument, lireCommande } from "./io.js";
import { evaluerDocument } from "./validation.js";

async function main(): Promise<void> {
  const argument = process.argv[2];
  if (!argument) {
    console.error("Usage : npm run start -- fixtures/commande-valide.json");
    process.exitCode = 2;
    return;
  }

  try {
    const commande = await lireCommande(resolve(argument));
    const rapport = evaluerDocument(await inspecterDocument(commande.document));
    console.log(JSON.stringify(rapport, null, 2));
    process.exitCode = rapport.etat === "valide" ? 0 : 1;
  } catch (erreur) {
    console.error(erreur instanceof Error ? erreur.message : String(erreur));
    process.exitCode = 2;
  }
}

await main();
