{
  "title": "Passer à TypeScript et diriger une mission complète",
  "description": "Construire un premier programme avec un agent sans lui abandonner sa compréhension.",
  "weight": 5,
  "prerequisite_id": "P05",
  "status": "redaction",
  "source_path": "manuscrit/00-prendre-la-main/05-typescript-et-mission.md",
  "previous": "/commencer/04-enqueter-et-prouver",
  "next": "/accessible/01-piloter-un-systeme"
}

## Situation et résultat observable

Le programme JavaScript sait contrôler un document, mais une faute comme `tailleOctet` à la place de `tailleOctets` n'est découverte qu'en exécutant le chemin concerné. TypeScript ajoute une description contrôlée des formes attendues. Il ne remplace ni la validation des données externes ni les tests.

## Ta prédiction

Classe ces problèmes : propriété mal orthographiée dans le code, champ absent dans un JSON, fichier introuvable, taille nulle, règle métier erronée. Lesquels le compilateur peut-il voir sans exécuter ? Lesquels exigent une validation ou un test ?

## De JavaScript à TypeScript

TypeScript conserve les expressions et fonctions JavaScript, puis ajoute des annotations supprimées lors de la construction :

```ts
type InformationsDocument = {
  chemin: string;
  tailleOctets: number;
  signature: string;
};

function evaluerDocument(document: InformationsDocument): Rapport {
  // mêmes règles qu'en JavaScript
}
```

Le type documente trois propriétés et permet au compilateur de refuser certains usages incohérents. Après compilation, Node exécute du JavaScript. Le projet épingle TypeScript 6.0.3, première version 6 stable réellement disponible dans le registre utilisé lors de la vérification.

## États et impossibilités visibles

Le parcours pédagogique reconnaît cinq états :

```ts
type EtatDocument = "prepare" | "en_cours" | "recu" | "valide" | "rejete";
```

Une faute comme `"validé"` est désormais refusée. Pour le rapport final, l'état est encore plus précis : `"valide" | "rejete"`. La fonction construit l'un ou l'autre selon la présence de raisons. Un document avec une raison de rejet ne peut donc pas être retourné comme valide par ce chemin sans contredire l'implémentation ou le type.

Un type réduit certains états représentables ; il ne prouve pas que la règle choisie est juste. Le compilateur accepterait parfaitement une condition métier inversée si elle retourne toujours les bons types.

## Les données externes restent inconnues

Le résultat de `JSON.parse` vient du monde extérieur. Écrire `as Commande` ordonne au compilateur de faire confiance au développeur ; cela ne vérifie aucun caractère du fichier. Le projet reçoit donc d'abord `unknown`, contrôle qu'il s'agit d'un objet et exige trois textes non vides.

Cette distinction est fondamentale : le type protège les usages internes après la frontière ; la validation établit ce qui a réellement franchi la frontière.

## Construire, contrôler, exécuter

Depuis `exemples/partie-zero` :

```sh
npm install
npm run check
npm run build
npm test
npm run start -- fixtures/commande-valide.json
```

`check` vérifie les types sans produire de fichier. `build` écrit le JavaScript dans `dist`. `test` construit puis exécute les tests avec Node. `start` construit puis lance le point d'entrée. Le fichier de verrouillage fixe les versions installées.

Le rapport attendu est un objet JSON comportant état, chemin, taille et raisons. Le code de sortie vaut `0` pour une validation, `1` pour un rejet métier et `2` pour une erreur d'usage ou technique. Ces catégories permettent à un autre programme de distinguer décision et panne.

## Préparer la mission finale

Une mission vérifiable précise :

- **résultat** : la propriété à préserver ;
- **périmètre** : fichiers et comportement concernés ;
- **interdictions** : aucune dépendance, publication ou autre refactorisation ;
- **preuves** : contrôle des types, test ciblé et suite complète ;
- **compte rendu** : changements, commandes, résultats et limites.

Mission :

> Garantir qu'un document possédant au moins une raison de rejet ne peut jamais produire un rapport `valide`. Travaille seulement dans les types, la validation et leurs tests. N'ajoute aucune dépendance. Présente d'abord ton plan. Après accord, implémente le changement, exécute `npm run check` et `npm test`, puis montre le diff et les limites restantes.

## Relire l'intervention

Avant d'accepter :

1. Le plan correspond-il à la règle ?
2. Le diff reste-t-il dans le périmètre ?
3. Les tests échoueraient-ils si la garantie était retirée ?
4. Les commandes ont-elles réellement été exécutées ?
5. Un type a-t-il été utilisé à la place d'une validation d'entrée ?
6. Le compte rendu distingue-t-il rejet métier et erreur technique ?

Ne demande pas « es-tu sûr ? ». Demande une observation reproductible.

## Approfondir les garanties de TypeScript

### Lire la configuration stricte

`tsconfig.json` indique la cible JavaScript, la convention de modules, les dossiers source et construit, puis active `strict`. `noUncheckedIndexedAccess` rappelle qu'un index peut ne rien trouver. `exactOptionalPropertyTypes` distingue une propriété absente d'une propriété présente avec `undefined`.

Ces options ne rendent pas le programme correct. Elles signalent davantage de zones ambiguës. Ne désactive pas un contrôle pour faire disparaître un message avant d'avoir compris l'incohérence.

### Une union comme vocabulaire fermé

Si l'état `expire` apparaît demain, les fonctions qui traitent exhaustivement les états doivent être revues. Cette friction est utile : elle rend visible l'impact de la décision. Elle ne choisit pas à notre place les transitions autorisées.

### Trois manières de faire taire le compilateur

Une assertion `as Commande`, le type `any` et `@ts-ignore` peuvent masquer un message sans résoudre sa cause. Ils ont des usages avancés, mais déplacent la responsabilité vers l'humain. Dans ce projet, leur apparition exige une justification et une vérification d'exécution.

Préférer `unknown` signifie « je ne sais pas encore ». Les contrôles successifs réduisent ensuite l'incertitude jusqu'au type interne fiable.

### Sources et artefacts construits

Le dossier `dist` est recréé par `npm run build`. Le fichier de verrouillage appartient au projet et fixe les versions exactes. Une revue porte d'abord sur `src`, les tests, la configuration et le verrouillage ; un artefact généré ne remplace pas la décision source.

Le projet n'ajoute que TypeScript et les définitions de Node comme dépendances de développement. Avant d'accepter un paquet proposé par l'agent, demande quelle API standard manque, s'il agit à l'exécution et comment il sera mis à jour ou retiré.

### Dossier d'acceptation minimal

Le compte rendu final tient en cinq blocs : résultat, fichiers modifiés, décisions, commandes réellement exécutées et risques non couverts. Il ne colle pas tout le dialogue et ne transforme pas une vérification future en vérification accomplie.

Si la machine n'exécute pas Node 24, l'agent doit le signaler. Des contrôles compatibles sur une autre version restent utiles, mais ne valident pas à eux seuls toute la cible annoncée.

## Épreuve finale sans agent

Prévois 45 à 60 minutes. Lance les quatre commandes publiques. Dessine le trajet `JSON → commande validée → fichier inspecté → règles → rapport → code de sortie`. Examine ensuite un diff où le test du fichier vide attend désormais `valide` : refuse cet affaiblissement et explique pourquoi le vert serait trompeur. Enfin, ajoute seul un test qui garantit que la taille exacte est autorisée.

Attribue-toi un point pour chacun des résultats suivants : commandes retrouvées sans aide, trajet expliqué, distinction type/validation, défaut du test repéré, frontière testée, limites formulées. Quatre points indiquent que tu peux poursuivre en gardant le socle à portée ; six indiquent que tu peux utiliser A01 comme mise en perspective plutôt que comme rattrapage.

{{< correction >}}
Le JSON doit être validé avant de devenir une `Commande`. L'inspection produit chemin, taille et signature ; la fonction pure construit les raisons puis l'état. Le test modifié change le contrat pour s'adapter au défaut : il doit être refusé. La frontière haute attend `TAILLE_MAXIMALE` et un rapport `valide`; `TAILLE_MAXIMALE + 1` doit produire un rejet.
{{< /correction >}}

## Ce que les preuves couvrent

Les tests établissent les règles codées pour les cas exécutés. Le contrôle TypeScript repère certaines incohérences de forme dans le code. L'essai de la commande relie fichier, parsing, inspection et affichage. Rien de cela ne démontre qu'un vrai PDF est imprimable, exempt de contenu dangereux ou isolé entre clients : ces sujets appartiennent aux chapitres suivants.

## Porte de sortie

- [ ] Je distingue type statique et validation à l'exécution.
- [ ] Je peux expliquer la construction puis l'exécution.
- [ ] Je sais borner une mission et lire son diff.
- [ ] Je refuse un test affaibli pour rendre le résultat vert.
- [ ] Je sais dire ce que les preuves ne couvrent pas.

Reprends maintenant le diagnostic initial. Si tu peux exécuter, lire, prédire, enquêter et expliquer ce petit système, tu es prêt pour **A01 — Piloter un système, pas une génération de code**.

## Références de l'étape

[Notes de version de TypeScript 6.0](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html) · [Options de configuration TypeScript](https://www.typescriptlang.org/tsconfig/). Documentation vérifiée le 1er septembre 2026. Le projet épingle la version 6.0.3 installée et testée ; il ne suit pas automatiquement la dernière version publiée.
