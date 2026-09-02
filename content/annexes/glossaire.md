{
  "title": "Glossaire partagé",
  "source_path": "manuscrit/annexes/glossaire.md"
}

## Agent {#agent}

système qui utilise un modèle et des outils pour accomplir une tâche.
## Argument {#argument}

valeur transmise à une commande ou à une fonction pour préciser son travail.
## API {#api}

interface permettant à des logiciels d'échanger selon un contrat.
## ADR {#adr}

note expliquant le contexte, les options et les conséquences d'une décision d'architecture.
## Artefact {#artefact}

résultat construit et identifiable que l'on peut livrer.
## CI {#ci}

vérifications automatiques déclenchées lors de changements.
## Contrat {#contrat}

description des entrées, résultats, erreurs et garanties d'une interaction.
## Code de sortie {#code-de-sortie}

nombre rendu par un processus à son appelant ; il distingue ici succès, rejet métier et erreur technique.
## Diff {#diff}

comparaison structurée montrant les lignes ajoutées, retirées ou remplacées.
## Effet de bord {#effet-de-bord}

interaction avec le monde extérieur, par exemple lire un fichier, afficher ou appeler un service.
## Fixture {#fixture}

donnée d'exemple stable préparée pour un test.
## Harnais {#harnais}

contexte, outils, permissions et contrôles qui entourent le travail d'un agent.
## Idempotence {#idempotence}

répétition d'une même opération sans effet métier supplémentaire dans le périmètre défini.
## Invariant {#invariant}

propriété que les opérations du système doivent préserver.
## MCP {#mcp}

protocole d'échange entre une application hôte et des serveurs exposant des capacités ; ce n'est pas une garantie de sécurité par lui-même.
## Migration {#migration}

changement versionné du schéma ou des données.
## Module {#module}

fichier ou unité de code qui expose des capacités et possède une responsabilité identifiable.
## Modèle à poids ouverts {#modele-a-poids-ouverts}

modèle dont les paramètres sont accessibles ; les droits d'usage dépendent de sa licence.
## Outbox {#outbox}

stockage transactionnel d'une intention d'émission, relayée ensuite vers un autre système.
## Port {#port}

capacité abstraite attendue par un composant, mise en œuvre par un adaptateur.
## Processus {#processus}

exécution vivante d'un programme à laquelle le système attribue notamment mémoire et accès aux fichiers.
## PR {#pr}

proposition d'intégration d'une branche avec description, vérifications et revue.
## RPO {#rpo}

objectif de perte maximale de données acceptable.
## RTO {#rto}

objectif de durée maximale de rétablissement.
## Runtime d'inférence {#runtime-d-inference}

logiciel qui exécute le modèle.
## Runtime {#runtime}

environnement qui exécute un programme ; Node.js exécute ici le JavaScript construit.
## SLO {#slo}

objectif mesurable de niveau de service.
## Tranche verticale {#tranche-verticale}

petit comportement utilisateur complet traversant les composants nécessaires.
## Type {#type}

description d'un ensemble de valeurs et d'opérations possibles ; un type statique ne valide pas à lui seul une donnée externe.
## Worktree {#worktree}

répertoire de travail supplémentaire lié à un dépôt Git ; pas une sandbox de sécurité.

Glossaire initial à enrichir avec les chapitres. Les précisions techniques sont renvoyées au registre critique et aux références de chaque tranche.
