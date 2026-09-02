{
  "title": "Lire, découper et modifier sans se perdre",
  "description": "Construire un premier programme avec un agent sans lui abandonner sa compréhension.",
  "weight": 3,
  "prerequisite_id": "P03",
  "status": "redaction",
  "source_path": "manuscrit/00-prendre-la-main/03-lire-et-decouper.md",
  "previous": "/commencer/02-transformer-des-donnees",
  "next": "/commencer/04-enqueter-et-prouver"
}

## Situation et résultat observable

Notre programme doit maintenant lire une commande JSON, inspecter le fichier indiqué et présenter un rapport. Tout placer dans un seul fichier rendrait chaque lecture plus difficile. Nous allons donner une responsabilité claire à chaque module sans changer le résultat observable.

## Ta prédiction

Dessine trois boîtes : lire, contrôler, présenter. Relie-les par les données qui circulent. Quel module devrait connaître le disque ? Lequel pourrait fonctionner uniquement avec un nom, une taille et une signature ?

## Trouver le point d'entrée

Le point d'entrée est le fichier lancé par la commande. Il orchestre l'appel des capacités sans contenir toutes leurs règles :

```js
import { lireCommande, inspecterDocument } from "./io.js";
import { evaluerDocument } from "./validation.js";

const commande = await lireCommande(process.argv[2]);
const informations = await inspecterDocument(commande.document);
const rapport = evaluerDocument(informations);
console.log(JSON.stringify(rapport, null, 2));
```

Lis ce passage de haut en bas : argument du terminal, commande structurée, informations du fichier, rapport, affichage. Chaque nom doit te permettre de raconter l'étape avant d'ouvrir son implémentation.

## Modules et responsabilités

`io.js` lit le monde extérieur : JSON, chemin et fichier. `validation.js` transforme des informations déjà disponibles. `index.js` coordonne puis choisit le code de sortie. `export` rend une capacité disponible ; `import` la nomme chez l'appelant.

Séparer ne signifie pas créer un fichier par ligne. Une bonne frontière permet de tester une règle sans ouvrir un vrai fichier et de changer la présentation sans réécrire la validation.

## Effets de bord

Lire le disque, afficher, consulter l'heure ou appeler le réseau sont des effets : ils dépendent du monde extérieur et peuvent échouer. Ils sont nécessaires, mais les placer aux bords protège le raisonnement central. `evaluerDocument` reste pur ; `inspecterDocument` peut rencontrer un fichier absent ou un droit insuffisant.

## Chemins et dossier courant

`fixtures/affiche.pdf` est résolu depuis le dossier où la commande est lancée, pas depuis le fichier JavaScript qui contient le texte. Pour vérifier une hypothèse, affiche temporairement `process.cwd()` ou demande au terminal son dossier courant. Ne remplace pas immédiatement tous les chemins par des chemins absolus : comprends d'abord la référence choisie.

## Lire une trace

Une erreur asynchrone peut afficher plusieurs cadres. Commence par le message, puis remonte au premier fichier de `src/`. Note le fichier, la ligne et la fonction. Les cadres internes à Node expliquent le trajet, mais ne sont généralement pas le premier endroit à modifier.

## Chercher un symbole

Avant de renommer `evaluerDocument`, cherche toutes ses occurrences. Un éditeur peut le faire ; dans un terminal équipé de ripgrep :

```sh
rg "evaluerDocument" .
```

Une recherche ne prouve pas que tous les appels sont corrects, mais elle réduit le risque d'oublier un import, un test ou un exemple.

## Mission bornée pour l'agent

> Propose un découpage en lecture de commande, validation pure et point d'entrée. Après mon accord, modifie au maximum trois fichiers. N'installe rien et conserve les messages, décisions et codes de sortie. Montre le diff et les commandes de vérification.

Le plan est une occasion de détecter un désaccord avant le patch. Le diff doit ensuite correspondre au plan. Une « amélioration » supplémentaire est un changement de périmètre, même si elle semble élégante.

## Revenir sans tout effacer

Avant l'intervention, observe `git status --short`. Après, utilise `git diff`. Si un fichier d'exercice contient uniquement une modification parasite et que tu as identifié exactement ce fichier, `git restore -- chemin` peut restaurer sa version suivie. Ne l'emploie pas sur un ensemble de fichiers ni sur un travail que tu n'as pas vérifié : la restauration détruit les modifications locales ciblées.

## Erreur volontaire

Lance le programme depuis le dossier parent du projet. Il ne trouve plus `fixtures/affiche.pdf`. Recueille trois faits : dossier courant, argument transmis, chemin final recherché. La cause n'est ni l'extension ni la règle de taille.

## Approfondir la lecture d'un projet

### Partir de la commande publique

Dans un projet inconnu, ne commence pas par ouvrir un fichier au hasard. Lis `package.json`, puis sa section `scripts`. La ligne associée à `start` révèle ici la construction et le fichier finalement exécuté. Suis ensuite les imports. Cette lecture « depuis la porte » évite de confondre un ancien exemple, un test et le véritable point d'entrée.

Un script npm n'est pas une capacité magique : c'est un nom pratique donné à une commande versionnée avec le projet. `npm run check` et `npm test` sont des interfaces publiques du dépôt. Lis leur définition avant de leur attribuer une garantie.

### Première rencontre avec l'asynchronisme

La lecture du disque ne répond pas instantanément. Une fonction marquée `async` rend une promesse de résultat futur ; `await` suspend ce scénario jusqu'à sa résolution.

```js
const commande = await lireCommande(chemin);
```

Cette ligne peut produire une commande ou lever une erreur. `await` ne supprime ni fichier absent, ni JSON invalide. Il permet d'écrire la suite de manière lisible. La concurrence et les reprises seront étudiées plus loin ; retiens ici qu'une opération extérieure a une durée et un mode d'échec.

### JSON n'est pas une donnée déjà fiable

JSON est un format texte. `JSON.parse` transforme un texte bien formé en valeur JavaScript, mais ne garantit pas la présence de `commandeId` ou la qualité d'un chemin. La syntaxe peut être valide et la donnée inutilisable. P03 sépare donc lecture et règles ; P05 validera explicitement cette frontière.

### Anatomie d'un diff

Un diff présente du contexte, des retraits préfixés par `-` et des ajouts préfixés par `+`. Il ne raconte pas automatiquement l'intention. Vérifie successivement les fichiers attendus, le comportement déplacé, les imports mis à jour, les messages inchangés et le code ancien réellement retiré.

Un grand bloc entièrement remplacé peut cacher une petite différence importante. Demande un patch plus local si le formatage masque le fond. Plusieurs petits changements cohérents peuvent toutefois être nécessaires pour déplacer une responsabilité sans la dupliquer.

### Laboratoire de réduction

Copie uniquement la résolution du chemin dans un fichier temporaire du dossier d'exercice et affiche son résultat. Compare deux dossiers courants. Cette expérience retire JSON, validation et rapport : si l'écart persiste, ils ne sont pas nécessaires à la reproduction.

Remets ensuite le programme normal et supprime ce fichier. Une réduction sert à isoler une cause, pas à devenir une architecture parallèle.

### Sous le capot — cohésion et couplage

Un module cohérent regroupe ce qui change pour la même raison. `validation` change avec les règles du document ; `io` avec la manière de lire les fichiers. Le couplage apparaît lorsqu'un module dépend des détails d'un autre. Transmettre de simples informations à la fonction pure limite ce lien.

Ces notions reviendront au chapitre d'architecture. Elles ne justifient pas ici cinq couches abstraites : trois modules suffisent à rendre le trajet visible.

## Exercice autonome

Retrouve le point d'entrée, dessine le flux jusqu'au rapport et justifie chaque fichier. Introduis ensuite une modification parasite dans un quatrième fichier, vérifie que le diff la révèle et retire uniquement celle-ci.

{{< correction >}}
Le flux attendu est `argument → lireCommande → inspecterDocument → evaluerDocument → JSON affiché`. Les effets de disque appartiennent à `io`; les règles à `validation`; l'ordre et le code de sortie au point d'entrée. Le contrôle Git doit nommer séparément la modification utile et la modification parasite avant toute restauration.
{{< /correction >}}

## Porte de sortie

- [ ] Je retrouve le point d'entrée depuis la commande.
- [ ] Je peux suivre une donnée à travers trois modules.
- [ ] Je distingue calcul pur et effet de bord.
- [ ] Je lis le premier cadre pertinent d'une trace.
- [ ] Je peux retirer un changement ciblé sans effacer le reste.

Formule finale : « Le programme commence dans … ; la donnée passe par … ; ce découpage permet de … »

## Références de l'étape

[Modules ECMAScript dans Node.js](https://nodejs.org/api/esm.html) · [API de fichiers asynchrone de Node.js](https://nodejs.org/api/fs.html#promises-api). Documentation vérifiée le 1er septembre 2026.
