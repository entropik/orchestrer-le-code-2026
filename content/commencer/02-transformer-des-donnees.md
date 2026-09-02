{
  "title": "Transformer des données avec des règles",
  "description": "Construire un premier programme avec un agent sans lui abandonner sa compréhension.",
  "weight": 2,
  "prerequisite_id": "P02",
  "status": "redaction",
  "source_path": "manuscrit/00-prendre-la-main/02-transformer-des-donnees.md",
  "previous": "/commencer/01-faire-executer",
  "next": "/commencer/03-lire-et-decouper"
}

## Situation et résultat observable

Afficher un nom ne dit pas si le document peut être accepté. L'atelier fixe trois règles pédagogiques : le nom se termine par `.pdf`, la taille est strictement positive et elle ne dépasse pas 500 000 000 octets. Nous allons transformer des données en décision explicable.

## Ta prédiction

Prévois le résultat pour `affiche.pdf` de 12 000 octets, `affiche.txt` de 12 000 octets, `vide.pdf` de 0 octet et `grand.pdf` de 500 000 001 octets. Une frontière exacte mérite sa propre ligne : que doit-il arriver à 500 000 000 ?

## Valeurs et noms

Une chaîne représente du texte, un nombre une quantité, un booléen `true` ou `false`. `undefined` indique souvent qu'aucune valeur n'a été fournie. Un tableau conserve une suite ordonnée ; un objet regroupe des propriétés nommées.

```js
const commande = {
  commandeId: "CMD-001",
  organisationId: "ORG-DEMO",
  document: { nom: "affiche.pdf", tailleOctets: 12_000 }
};
```

Les noms du domaine sont français mais restent sans accents dans le code. Les noms d'APIs standard, comme `console.log` ou `endsWith`, ne sont pas traduits.

### Valeur et variable ne sont pas synonymes

La valeur `"CMD-001"` existe indépendamment du nom `commandeId` choisi pour la désigner. Deux variables peuvent référencer le même objet. Modifier cet objet par l'une peut donc être visible par l'autre, même si les variables sont déclarées avec `const`. `const` interdit la réassignation du nom ; il ne rend pas récursivement toutes les données immuables.

Pour commencer, préfère créer une nouvelle sortie plutôt que modifier silencieusement l'entrée. Cette convention simplifie la prédiction et rend les diffs plus faciles à lire.

## Une fonction transforme

```js
const TAILLE_MAXIMALE = 500_000_000;

function raisonsDeRejet(document) {
  const raisons = [];
  if (!document.nom.toLowerCase().endsWith(".pdf")) {
    raisons.push("Le nom ne se termine pas par .pdf.");
  }
  if (document.tailleOctets <= 0) {
    raisons.push("Le document est vide.");
  }
  if (document.tailleOctets > TAILLE_MAXIMALE) {
    raisons.push("Le document est trop grand.");
  }
  return raisons;
}
```

Le paramètre `document` est l'entrée. Le tableau `raisons` accumule les règles violées. `return` rend la sortie à l'appelant. La fonction ne lit aucun fichier et n'affiche rien : avec la même entrée, elle retourne la même sortie. Cette propriété la rend facile à raisonner et à tester.

### Portée et durée des noms

`TAILLE_MAXIMALE` est visible dans le module. `raisons` n'existe que pendant l'appel de la fonction. `document` désigne l'argument courant. Si tu déclares un second `raisons` dans un bloc intérieur, il peut masquer le premier : le programme reste parfois valide mais sa lecture devient trompeuse. Des noms précis évitent de compenser une mauvaise structure par des commentaires.

Une fonction doit soit retourner une information, soit produire volontairement un effet. Une fonction qui modifie une variable cachée, affiche parfois et retourne parfois une valeur est plus difficile à prévoir.

## Conditions et frontières

Une condition n'est pas une phrase approximative. `<= 0` inclut zéro ; `> TAILLE_MAXIMALE` autorise exactement la limite. Inverser un seul signe change le contrat. Lis une condition en français avant de l'accepter.

Les conversions implicites sont dangereuses pour un débutant : le texte `"12000"` n'est pas le nombre `12000`. Aux frontières, vérifie la forme des données au lieu d'espérer que JavaScript choisira la bonne interprétation.

### Vrai, faux et valeurs « falsy »

JavaScript traite certaines valeurs comme fausses dans une condition : `false`, `0`, la chaîne vide, `null`, `undefined` et `NaN`. Cette commodité peut mélanger des situations différentes. Dans une règle métier, écris la comparaison qui porte le sens : `tailleOctets <= 0` explique mieux l'intention que `!tailleOctets`.

De même, `==` peut convertir les opérandes avant comparaison. Utilise par défaut `===`, qui compare sans cette conversion. Le but n'est pas un dogme de style : c'est de réduire les résultats surprenants.

## Répéter sans perdre le fil

Une boucle applique une opération à plusieurs éléments. Elle n'est utile que si plusieurs valeurs doivent réellement être parcourues :

```js
for (const raison of raisonsDeRejet(commande.document)) {
  console.log(`Rejet : ${raison}`);
}
```

Avant une boucle, identifie la collection, l'élément courant et la condition d'arrêt. Préfère une écriture simple à une chaîne compacte que tu ne peux pas expliquer.

### Tracer manuellement une exécution

Pour `affiche.txt` de taille nulle, construis un tableau sur papier : condition évaluée, résultat booléen, contenu de `raisons` après l'étape. La première condition ajoute l'extension ; la seconde ajoute le fichier vide ; la troisième n'ajoute rien. Le résultat final contient deux raisons.

Cette simulation manuelle semble lente. Elle devient pourtant un outil puissant lorsque l'agent livre une expression compacte. Si tu ne peux pas la dérouler pour une entrée simple, demande une forme plus lisible.

## Dialogue avec l'agent

Utilise une mission en quatre temps :

> Reformule les trois règles sans coder. Propose ensuite les entrées et la sortie d'une fonction pure. N'ajoute aucune bibliothèque. Attends mon accord avant de produire le code.

Compare sa reformulation à tes prédictions. Si elle interdit la taille exacte, corrige le contrat avant le code. Si elle propose une bibliothèque pour reconnaître une extension, demande pourquoi l'API standard ne suffit pas.

## Modification limitée et diff

Autorise ensuite un seul fichier. Après le patch, cherche dans le diff : une fonction, les trois conditions, aucune installation et aucune modification hors périmètre. Exécute les quatre exemples prévus, puis compare les sorties à la table initiale.

## Erreurs à diagnostiquer

1. Remplacer `<= 0` par `< 0` accepte silencieusement le fichier vide.
2. Remplacer `>` par `>=` rejette la taille exacte pourtant autorisée.
3. Écrire `document.taille` au lieu de `document.tailleOctets` fournit `undefined`.
4. Passer `"12000"` masque un défaut de données même si certaines comparaisons semblent fonctionner.

Pour chacune, nomme l'entrée la plus petite qui révèle le défaut.

### Laboratoire de tables de décision

Écris les règles en colonnes et les cas en lignes. Ajoute les combinaisons : mauvaise extension et vide ; PDF trop grand ; mauvaise extension trop grande. Vérifie que les raisons peuvent se cumuler. Puis pose une question éditoriale : voulons-nous toutes les raisons ou seulement la première ? Les deux comportements sont possibles, mais ils ne donnent pas la même aide à l'utilisateur. Le contrat doit trancher avant l'implémentation.

Demande ensuite à l'agent de générer des cas, pas leur résultat. Tu restes responsable de l'oracle. Rejette les exemples redondants qui n'exercent aucune nouvelle frontière.

## Sous le capot — représentation des nombres

JavaScript utilise principalement des nombres en virgule flottante. Les entiers sont exacts jusqu'à une limite très supérieure à 500 000 000, donc notre taille pédagogique ne subit pas ici d'arrondi. Cette propriété n'autorise pas à représenter n'importe quelle quantité de la même façon : les montants financiers demandent par exemple une unité entière explicite, comme les centimes.

Une unité fait partie du nom et du contrat. `tailleOctets` est plus sûr que `taille`, qui pourrait signifier kilo-octets, mégaoctets ou nombre de pages.

## Exercice autonome

Ajoute un motif distinct `Le document est vide.` sans modifier les deux autres règles. Explique les trois issues : accepté, rejeté pour une raison, rejeté pour plusieurs raisons. Ne demande pas à l'agent d'écrire la solution avant d'avoir écrit ta propre condition.

{{< correction >}}
La condition attendue est `document.tailleOctets <= 0`. Elle produit une raison indépendante ; le programme peut donc cumuler extension incorrecte, taille excessive ou absence de contenu. L'acceptation correspond à un tableau vide, pas à un message particulier affiché à l'écran.
{{< /correction >}}

## Porte de sortie

- [ ] Je distingue texte, nombre, booléen, tableau et objet.
- [ ] Je peux nommer entrée, transformation et sortie.
- [ ] Je lis une condition à sa frontière exacte.
- [ ] Je sais pourquoi cette fonction est dite pure.
- [ ] Je peux prévoir plusieurs sorties avant l'exécution.

Formule finale : « Cette fonction reçoit …, vérifie … et retourne … ; elle n'agit pas sur … »

## Références de l'étape

[Guide JavaScript de MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide) · [Référence des nombres JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Number). Pages vérifiées le 1er septembre 2026.
