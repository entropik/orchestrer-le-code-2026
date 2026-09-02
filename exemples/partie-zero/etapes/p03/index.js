import { lireCommande, inspecterDocument } from "./io.js";
import { evaluerDocument } from "./validation.js";

const cheminCommande = process.argv[2];
if (!cheminCommande) throw new Error("Indique le chemin de la commande.");
const commande = await lireCommande(cheminCommande);
const rapport = evaluerDocument(await inspecterDocument(commande.document));
console.log(JSON.stringify(rapport, null, 2));
