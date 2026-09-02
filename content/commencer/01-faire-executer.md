{
  "title": "Faire exécuter un programme",
  "description": "Construire un premier programme avec un agent sans lui abandonner sa compréhension.",
  "weight": 1,
  "prerequisite_id": "P01",
  "status": "redaction",
  "source_path": "manuscrit/00-prendre-la-main/01-faire-executer.md",
  "previous": "/commencer",
  "next": "/commencer/02-transformer-des-donnees"
}

## Situation et résultat observable

L'atelier vient de recevoir `affiche.pdf`. Pour l'instant, notre programme doit seulement afficher ce nom. Ce résultat minuscule permet d'observer toute la chaîne : un fichier contient du code, Node.js le lit, un processus s'exécute et le terminal reçoit une sortie.

## Ta prédiction

Avant de lancer quoi que ce soit, complète : « quand j'exécute `node bonjour.js`, je pense que … ». Note aussi le nom du fichier que tu t'attends à voir modifié si le message change.

## Fichiers, dossiers et chemins

Un **fichier** est une suite de données nommée. Un **dossier** organise des fichiers et d'autres dossiers. L'extension `.js` indique ici l'usage attendu ; elle ne transforme pas magiquement le contenu en programme. Un **chemin** localise un élément : `src/bonjour.js` part du dossier courant, tandis qu'un chemin absolu part de la racine du système.

Le terminal possède toujours un dossier courant. C'est depuis ce point que les chemins relatifs sont résolus. Beaucoup d'erreurs attribuées au code sont simplement des commandes exécutées depuis le mauvais dossier.

## Le premier programme

```js
const nomDocument = "affiche.pdf";
console.log(`Document reçu : ${nomDocument}`);
```

`const` associe un nom à une valeur qui ne sera pas réassignée. `console.log` demande à l'environnement d'afficher une valeur. Le texte entre accents graves contient une interpolation : `${nomDocument}` est remplacé par la valeur.

Enregistre ce code dans `bonjour.js`, puis lance :

```sh
node bonjour.js
```

La commande est `node`; `bonjour.js` est son argument. Node crée un processus, lit le fichier, évalue les instructions et rend la main au terminal. Le texte source reste dans le fichier ; la sortie affichée n'est pas enregistrée dans ce fichier.

## Installer et vérifier l'environnement

Utilise une version **Node.js 24 LTS**. La version de référence du projet est 24.20.0, datée du 26 août 2026. Télécharge-la depuis le site officiel de Node.js ou utilise le gestionnaire de versions habituel de ton système. Sous Windows, macOS et Linux, les contrôles sont identiques :

```sh
node --version
npm --version
```

Une version différente de Node 24 n'est pas automatiquement une panne, mais les résultats du livre sont vérifiés sur cette ligne LTS. N'utilise pas une version arrivée en fin de support pour un nouveau projet.

### Trois terminaux, les mêmes idées

Sous Windows, tu peux employer PowerShell ; sous macOS et Linux, un shell comme `zsh` ou `bash`. Les commandes Node et npm du livre restent identiques. En revanche, afficher le dossier courant ou lister les fichiers peut varier. Utilise l'interface de ton éditeur si cette différence te détourne de l'objectif : savoir quel dossier est actif et quel fichier sera exécuté.

Les espaces dans un chemin nécessitent parfois des guillemets. Ne retire pas un espace du nom réel pour « aider » une commande. Apprends plutôt à distinguer le chemin transmis du chemin interprété.

## Sous le capot — le processus

Le fichier n'agit pas seul. Quand tu appelles Node, le système d'exploitation crée un **processus**. Celui-ci reçoit notamment des arguments, un dossier courant, un environnement et trois flux conventionnels : entrée, sortie normale et sortie d'erreur. À la fin, il rend un code numérique.

```js
console.log("Résultat normal");
console.error("Problème à examiner");
process.exitCode = 2;
```

La sortie d'erreur ne signifie pas nécessairement que l'ordinateur est cassé. C'est un canal destiné aux diagnostics. Le code de sortie permet à une personne ou à un autre programme de distinguer succès et échec sans lire une phrase française. Notre projet réservera `0` à la validation, `1` au rejet d'un document et `2` à une erreur technique ou d'usage.

Ne commence pas par appeler `process.exit()` partout : l'arrêt immédiat peut empêcher une opération en attente de finir. Attribuer `process.exitCode` laisse Node terminer proprement ce qui est déjà engagé.

## Lire le programme caractère par caractère

Dans `console.log(...)`, les parenthèses délimitent l'argument de la fonction. Le point relie l'objet `console` à sa capacité `log`. Le point-virgule marque la fin de l'instruction ; JavaScript sait parfois l'inférer, mais une convention stable évite certaines ambiguïtés. Les accolades de `${nomDocument}` n'ont pas le même rôle que celles d'un bloc de code : ici elles insèrent une expression dans une chaîne délimitée par des accents graves.

Tu n'as pas besoin de mémoriser ces noms immédiatement. Tu dois pouvoir pointer le fragment qui choisit la valeur et celui qui produit l'effet.

## Lire trois erreurs simples

- « commande introuvable » signifie que le terminal ne trouve pas Node ; le programme n'a pas commencé.
- « module introuvable » suivi du nom de `bonjour.js` signifie souvent que le chemin du fichier est faux.
- `SyntaxError` signifie que Node a trouvé le fichier mais ne peut pas interpréter sa forme.

Lis toujours le type d'erreur, le premier message et le premier chemin appartenant à ton projet. Une longue trace n'est pas une condamnation : c'est une piste ordonnée.

## Premier dialogue avec l'agent

Demande :

> Lis `bonjour.js` sans le modifier. Explique la valeur, l'instruction qui produit un effet visible et le résultat attendu. Signale ce que tu ne peux pas savoir sans exécuter.

Cette mission sépare analyse et modification. Si l'agent change le fichier malgré l'interdiction, le problème n'est pas la qualité du code : c'est le non-respect du périmètre.

## Inspecter le changement

Dans un dépôt Git, utilise :

```sh
git status --short
git diff -- bonjour.js
```

La première commande nomme les fichiers modifiés. La seconde montre les lignes retirées et ajoutées. À ce stade, Git sert de miroir ; l'histoire complète viendra au chapitre 5.

## Erreur à diagnostiquer

Exécute volontairement `node bonjours.js`. Ne corrige pas immédiatement. Compare le chemin demandé au nom réel. Classe l'erreur : environnement, syntaxe, donnée ou chemin ? Puis formule la correction la plus petite.

### Laboratoire de variations

Effectue quatre essais séparés et annule chacun avant le suivant :

1. retire le guillemet final ;
2. remplace le nom de variable à un seul endroit ;
3. lance la commande depuis le dossier parent ;
4. ajoute un second `console.log`.

Pour chaque essai, note si Node commence à exécuter le fichier, si une sortie apparaît avant l'erreur et quel chemin ou numéro de ligne est cité. Deux messages différents peuvent avoir la même cause générale, mais n'invente pas la cause à partir de la catégorie : vérifie le détail.

## Signaux d'alerte dans une réponse d'agent

- Il affirme avoir exécuté sans montrer la commande ni le résultat.
- Il installe une bibliothèque pour afficher une chaîne.
- Il modifie plusieurs fichiers alors qu'une seule ligne suffit.
- Il corrige une erreur de chemin en déplaçant tout le projet.
- Il confond le message affiché avec le code de sortie.

Réponds par une demande précise : « montre le diff », « explique pourquoi cette dépendance est nécessaire » ou « quelle observation prouve que le fichier a été exécuté ? »

## Exercice autonome

Modifie le message pour obtenir `Document prêt à inspecter : affiche.pdf`. Exécute, retrouve le fichier changé avec Git et explique avec tes mots la différence entre le fichier source, le processus et la sortie.

{{< correction >}}
La modification utile ne touche qu'à la chaîne passée à `console.log`. `git status --short` doit nommer `bonjour.js`; le diff doit montrer une ligne remplacée. Le fichier est la description persistante, le processus est l'exécution temporaire et la sortie est l'effet observable dans le terminal.
{{< /correction >}}

## Porte de sortie

- [ ] Je sais dans quel dossier je me trouve.
- [ ] Je distingue commande et argument.
- [ ] Je peux lancer un programme et décrire son résultat.
- [ ] Je reconnais une erreur survenue avant l'exécution du code.
- [ ] Je peux montrer le changement exact sans dire seulement « ça marche ».

Formule finale : « Le programme commence lorsque … ; le résultat apparaît dans … ; le fichier modifié est … »

## Références de l'étape

[Versions maintenues de Node.js](https://nodejs.org/en/about/previous-releases) · [Documentation de `git diff`](https://git-scm.com/docs/git-diff). Versions et pages vérifiées le 1er septembre 2026.
