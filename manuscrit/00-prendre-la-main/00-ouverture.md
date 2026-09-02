# Partie zéro — Prendre la main

> Construire un premier programme avec un agent sans lui abandonner sa compréhension.

## Pourquoi commencer ici

Ce livre ne promet pas de faire de toi un développeur en accéléré. Il te demande pourtant de superviser un agent qui touche à du code, des fichiers et bientôt des données. On ne peut pas exercer cette responsabilité en regardant seulement le résultat final. Il faut savoir où commence un programme, comment une valeur le traverse, pourquoi il échoue et quelle preuve permet d'accepter une modification.

La syntaxe n'est donc pas une fin. Elle est l'alphabet minimum qui te permet de lire. L'agent peut te rappeler un mot ou produire un premier brouillon ; il ne doit pas faire disparaître l'effort de prévoir, d'observer et d'expliquer.

## Trois activités différentes

**Demander une réalisation**, c'est décrire un résultat et un périmètre. **Comprendre le mécanisme**, c'est pouvoir raconter ce que font les fichiers et les fonctions sans réciter chaque caractère. **Décider**, enfin, c'est comparer le résultat aux attentes et aux risques. Une personne peut réussir la première activité et manquer les deux autres. Cette partie zéro les réunit.

Un agent travaille avec le contexte qu'il voit. Il peut ignorer une règle qui n'est écrite nulle part, inventer une API plausible, ajouter une dépendance inutile ou modifier plus de fichiers que prévu. Sa proposition mérite donc la même discipline qu'une proposition humaine : plan, limites, diff, exécution et preuves.

## Le contrat d'apprentissage

À chaque étape, tu vas d'abord écrire une prédiction. Ensuite seulement, tu exécutes. Tu lis le changement avant de l'accepter. Quand un défaut apparaît, tu recueilles une observation avant de demander la correction. Enfin, tu reformules ce que tu as compris sans copier la réponse de l'agent.

L'agent gagne progressivement de l'autonomie : explication seule en P01, proposition de fonctions en P02, petit patch en P03, aide à l'enquête en P04, mission complète mais bornée en P05. À aucun moment une publication, un accès à des données personnelles ou l'installation d'un outil supplémentaire n'est implicite.

## Le projet miniature

Un atelier reçoit une commande et un document prétendument PDF. Notre outil local lit une commande fictive, inspecte le fichier, applique quelques règles et imprime un rapport. Il ne dépose rien sur Internet, n'ouvre aucun compte et ne traite aucun vrai document client.

À la fin, les commandes principales seront :

```text
npm run start -- fixtures/commande-valide.json
npm test
npm run check
npm run build
```

Le projet exécutable se trouve dans `exemples/partie-zero`. Les étapes commencent en JavaScript, puis P05 montre ce que TypeScript ajoute réellement.

## Diagnostic initial — sans note

Pour chaque affirmation, réponds « oui », « pas encore » ou « je ne sais pas ce que cela signifie » :

1. Je sais distinguer un fichier d'un dossier.
2. Je sais ouvrir un terminal dans un dossier choisi.
3. Je sais expliquer ce que fait une commande et reconnaître son argument.
4. Je sais lancer un fichier JavaScript avec Node.js.
5. Je sais retrouver le point d'entrée d'un petit programme.
6. Je sais lire les premières lignes utiles d'un message d'erreur.
7. Je sais comparer deux versions d'un fichier avec Git.
8. Je sais dire ce qu'un test automatique vérifie.

Tu n'as pas besoin d'obtenir huit « oui ». Les réponses servent de point de comparaison pour l'épreuve finale.

## Ta boussole

Après chaque étape, vérifie six verbes : **lire**, **prévoir**, **exécuter**, **modifier**, **diagnostiquer**, **expliquer**. Un résultat obtenu très vite mais impossible à expliquer n'est pas encore un apprentissage terminé.

## Comment travailler avec ce parcours

Prévois cinq séances de 60 à 90 minutes plutôt qu'une lecture continue. Garde un carnet séparé du dialogue avec l'agent. Écris-y les prédictions, les commandes réellement exécutées, les erreurs rencontrées et ta reformulation finale. Le carnet montre ton raisonnement ; l'historique de l'agent montre surtout ce qui lui a été demandé.

Quand un passage paraît évident, essaie de l'expliquer sans regarder. Quand un passage bloque, réduis l'exercice au lieu de multiplier les demandes. La difficulté momentanée fait partie de l'apprentissage : elle révèle précisément le concept qui manque.

Les corrigés sont repliés. Ouvre-les après une tentative observable, même incomplète. Comparer deux raisonnements est formateur ; recopier une solution avant d'avoir formulé le problème l'est beaucoup moins.

## Sécurité du terrain d'exercice

Travaille exclusivement dans `exemples/partie-zero`. Les commandes du parcours ne demandent ni droits administrateur, ni mot de passe, ni secret. Les documents sont fictifs. Une demande de l'agent visant un autre dossier, un service distant ou une installation non prévue doit interrompre l'exercice et déclencher une explication.

Une commande n'est jamais « seulement du texte » dès qu'elle est exécutée. Lis son programme, ses arguments et sa cible. Dans le doute, demande une explication sans exécution. Cette habitude vaut davantage qu'une liste de commandes prétendument sûres.

## Ce que cette partie ne cherche pas à couvrir

Tu ne vas pas apprendre ici le HTML, le CSS, les bases de données, les serveurs ou tous les mécanismes de JavaScript. Tu vas acquérir une carte suffisamment solide pour ne pas dépendre aveuglément d'un agent. Les douze chapitres apporteront ensuite architecture, contrats, Git collaboratif, tests avancés, livraison et exploitation.
