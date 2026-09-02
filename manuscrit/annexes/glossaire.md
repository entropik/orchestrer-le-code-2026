# Glossaire partagé

- **Agent** : système qui utilise un modèle et des outils pour accomplir une tâche.
- **Argument** : valeur transmise à une commande ou à une fonction pour préciser son travail.
- **API** : interface permettant à des logiciels d'échanger selon un contrat.
- **ADR** : note expliquant le contexte, les options et les conséquences d'une décision d'architecture.
- **Artefact** : résultat construit et identifiable que l'on peut livrer.
- **CI** : vérifications automatiques déclenchées lors de changements.
- **Contrat** : description des entrées, résultats, erreurs et garanties d'une interaction.
- **Code de sortie** : nombre rendu par un processus à son appelant ; il distingue ici succès, rejet métier et erreur technique.
- **Diff** : comparaison structurée montrant les lignes ajoutées, retirées ou remplacées.
- **Effet de bord** : interaction avec le monde extérieur, par exemple lire un fichier, afficher ou appeler un service.
- **Fixture** : donnée d'exemple stable préparée pour un test.
- **Harnais** : contexte, outils, permissions et contrôles qui entourent le travail d'un agent.
- **Idempotence** : répétition d'une même opération sans effet métier supplémentaire dans le périmètre défini.
- **Invariant** : propriété que les opérations du système doivent préserver.
- **MCP** : protocole d'échange entre une application hôte et des serveurs exposant des capacités ; ce n'est pas une garantie de sécurité par lui-même.
- **Migration** : changement versionné du schéma ou des données.
- **Module** : fichier ou unité de code qui expose des capacités et possède une responsabilité identifiable.
- **Modèle à poids ouverts** : modèle dont les paramètres sont accessibles ; les droits d'usage dépendent de sa licence.
- **Outbox** : stockage transactionnel d'une intention d'émission, relayée ensuite vers un autre système.
- **Port** : capacité abstraite attendue par un composant, mise en œuvre par un adaptateur.
- **Processus** : exécution vivante d'un programme à laquelle le système attribue notamment mémoire et accès aux fichiers.
- **PR** : proposition d'intégration d'une branche avec description, vérifications et revue.
- **RPO** : objectif de perte maximale de données acceptable.
- **RTO** : objectif de durée maximale de rétablissement.
- **Runtime d'inférence** : logiciel qui exécute le modèle.
- **Runtime** : environnement qui exécute un programme ; Node.js exécute ici le JavaScript construit.
- **SLO** : objectif mesurable de niveau de service.
- **Tranche verticale** : petit comportement utilisateur complet traversant les composants nécessaires.
- **Type** : description d'un ensemble de valeurs et d'opérations possibles ; un type statique ne valide pas à lui seul une donnée externe.
- **Worktree** : répertoire de travail supplémentaire lié à un dépôt Git ; pas une sandbox de sécurité.

Glossaire initial à enrichir avec les chapitres. Les précisions techniques sont renvoyées au registre critique et aux références de chaque tranche.
