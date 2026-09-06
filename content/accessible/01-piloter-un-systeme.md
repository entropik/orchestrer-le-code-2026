{
  "title": "Piloter un système, pas une génération de code",
  "description": "Savoir ce que l'on délègue à un agent et ce que l'on doit décider soi-même.",
  "weight": 1,
  "chapter_id": "A01",
  "theme": "01",
  "status": "valide",
  "source_path": "manuscrit/01-lecture-accessible/01-piloter-un-systeme.md",
  "mirror": "/ingenieure/01-piloter-un-systeme",
  "related": [
    "/accessible/04-harnais-et-contexte",
    "/accessible/11-methode-et-cas-pratiques"
  ],
  "notions": [
    {
      "label": "Agent",
      "anchor": "agent"
    },
    {
      "label": "Harnais",
      "anchor": "harnais"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "previous": "/accessible/avant-propos",
  "next": "/accessible/02-architecture-et-frontieres"
}

## Ce que tu sauras faire

Savoir ce que l'on délègue à un agent et ce que l'on doit décider soi-même.

### Préambule : Sortir de la cage du chatbot pour créer librement

Jusqu'ici, ton expérience de l'intelligence artificielle ressemble peut-être à une boîte de dialogue enfermée dans un navigateur web : tu poses une question polie, le modèle génère une réponse élégante, parfois un résumé de document ou un fragment de code que tu ne sais ni où coller, ni comment exécuter. Tu es resté spectateur dans un salon de discussion.

Ce manuel propose une rupture complète.

Dès que l'on connecte un modèle de langage à un ordinateur réel — avec le droit d'explorer des dossiers, d'exécuter des commandes et de manipuler des fichiers —, la machine cesse d'être un perroquet bavard pour devenir un véritable **actionneur numérique**. Elle ne se contente plus de parler : elle bâtit.

Cette bascule ouvre un champ immense. Elle permet à n'importe quel individu — créateur, artisan, soignant, commerçant, juriste ou chef d'entreprise — de concevoir et de piloter des outils logiciels sur mesure, **du script le plus modeste qui automatise un tri fastidieux jusqu'au service le plus ambitieux qui fait tourner une activité entière**. Tu n'es plus condamné à louer des logiciels rigides pensés par d'autres, ni à dépendre d'intermédiaires coûteux pour la moindre modification.

Mais cette liberté exige une lucidité totale. L'intelligence artificielle est un **outil d'artisan**, ni un démiurge bienveillant, ni un pilote automatique infaillible. Elle possède une vitesse de frappe phénoménale, mais aucun bon sens économique, aucune conscience de tes responsabilités légales et aucune capacité d'arbitrage moral. 

Si tu lui demandes simplement de « faire au mieux », elle appliquera la loi du moindre effort statistique. Si tu lui donnes les pleins pouvoirs, elle peindra avec enthousiasme les fenêtres en même temps que les murs. 

L'autonomie numérique ne consiste pas à devenir programmeur en trois jours. Elle consiste à devenir le **maître d'ouvrage lucide** de ton système : comprendre les principes fondamentaux, poser les bonnes questions, fixer des limites infranchissables et exiger des preuves avant de faire confiance. C'est tout l'objet de ce voyage.

---

## Première synthèse

### 1. L'illusion du bouton : l'écran n'est pas le logiciel

Imagine la scène. Tu ouvres ton environnement d'agent et tu lui écris : *« Crée-moi un bouton pour que mes clients puissent déposer leurs documents en ligne »*. 

Quinze secondes plus tard, la magie opère. Une page web étincelante s'affiche sur ton écran, avec un bouton bleu soigné, un champ de survol délicat et une animation impeccable. L'illusion est si parfaite que tu penses avoir terminé 90 % du travail.

En réalité, **le logiciel n'a même pas encore commencé**.

Ce que l'écran te montre n'est qu'un décor de théâtre, une fine pellicule visuelle. Le véritable travail commence avec toutes les questions invisibles que ce bouton ne pose pas :
- Quand un client dépose un fichier de 500 mégaoctets, où va-t-il physiquement ? Reste-t-il sur ton ordinateur ou part-il sur un serveur distant ?
- Que se passe-t-il si la connexion coupe à 98 % du transfert ? Le fichier est-il corrompu, abandonné en silence ou repris automatiquement ?
- Qui a le droit de consulter ce document ? Un tiers malveillant peut-il deviner son adresse web et le télécharger ?
- Si deux personnes envoient un fichier portant exactement le même nom à la même seconde, le second écrase-t-il le premier sans avertissement ?

Piloter du logiciel en 2026, ce n'est pas apprendre la syntaxe pour dessiner ce bouton. C'est savoir identifier ces questions fondamentales avant que l'imprévu ne se produise devant un vrai client.

---

### 2. Le petit lexique du béotien émancipé

Pour dialoguer d'égal à égal avec une machine ou une équipe technique, tu n'as besoin que d'une poignée de concepts limpides :

- **L'application** : Ce n'est pas un bloc magique, c'est une organisation administrative. Elle a un guichet d'accueil pour recevoir le public, des bureaux où s'appliquent les règles métier, et une armoire forte pour ranger les dossiers.
- **Le code** : C'est une recette de cuisine rédigée dans un langage formel sans ambiguïté. Si la recette dit d'ajouter du sel à la place du sucre, la machine le fera sans broncher, avec un enthousiasme parfait.
- **Le terminal (ou la console)** : C'est une simple fenêtre textuelle où l'on pilote l'ordinateur par des phrases courtes au lieu de cliquer avec une souris. C'est le volant direct du système, sans fard ni décor.
- **Le serveur** : C'est un ordinateur ordinaire, allumé en continu dans un local sécurisé, sans écran ni clavier personnel, qui attend sagement sur le réseau qu'on lui demande un service.
- **L'[Agent](/annexes/glossaire#agent)** : C'est un modèle d'intelligence artificielle doté d'outils lui permettant de lire ton dossier de travail, d'écrire des fichiers et d'exécuter des commandes. C'est un commis surdoué, ultra-rapide mais totalement dépourvu de mémoire spontanée entre deux sessions[^1].
- **Le [Harnais](/annexes/glossaire#harnais)** : C'est l'ensemble des barrières physiques, des règles de sécurité et des vérifications automatiques qui encadrent le travail de l'agent. Le harnais est la cage de protection qui empêche le commis de renverser l'atelier.

[^1]: Ce phénomène d'amnésie est structurel : dès qu'une session de travail se termine, l'agent oublie tout ce qu'il a produit, à moins que l'information n'ait été consignée dans un document durable du projet.

---

### 3. Les quatre mouvements fondamentaux de tout système

Quel que soit le domaine — cabinet médical, boutique en ligne, atelier de fabrication, association —, chaque programme informatique sur terre accomplit inlassablement les quatre mêmes mouvements :

```text
┌─────────────┐     ┌─────────────┐     ┌───────────────┐     ┌───────────────────────┐
│ 1. RECEVOIR │ ──► │ 2. VALIDER  │ ──► │ 3. TRANSFORMER│ ──► │ 4. PERSISTER / RÉPONDRE│
└─────────────┘     └─────────────┘     └───────────────┘     └───────────────────────┘
  Une intention       Le contrôle         Le calcul ou          L'armoire forte ou
    qui entre         de légitimité        la recette            la trace durable
```

1. **Recevoir** : Quelque chose entre dans le système. Un clic de souris, une commande tapée, un formulaire rempli, ou un fichier PDF téléversé.
2. **Valider** : Le système applique ses [Invariants](/annexes/glossaire#invariant)[^2] : le demandeur a-t-il le droit d'agir ? Le fichier a-t-il la taille autorisée ? Les données obligatoires sont-elles présentes ? Si la réponse est non, le système s'arrête net et explique pourquoi.
3. **Transformer** : Le système exécute le cœur de son travail : calculer une remise, analyser les marges d'un document, convertir une devise ou extraire du texte.
4. **Persister ou répondre** : Le système enregistre l'état dans une base de données durable (pour qu'une coupure de courant n'efface rien) et renvoie une confirmation claire à l'utilisateur.

> [!TIP]
> **La question réflexe du pilote**  
> Dès qu'un agent te propose un développement, demande-lui systématiquement : *« Que reçois-tu ? Que valides-tu avant d'agir ? Que transformes-tu ? Et où ranges-tu le résultat pour ne jamais le perdre ? »*

[^2]: Un **invariant** est une propriété sacrée du système qui ne doit jamais être violée, quelles que soient les circonstances (ex. : un solde de compte ne peut pas être négatif, un fichier ne peut pas être modifié sans enregistrer l'auteur).

---

### 4. La métaphore du chantier : l'architecte et les artisans

Pour comprendre ton rôle face à l'IA, pense à la rénovation complète d'une maison ancienne.

Si tu laisses entrer des artisans sur le chantier en leur disant : *« Faites une belle cuisine, surprenez-moi ! »*, tu obtiendras peut-être un îlot central somptueux en marbre, mais raccordé à aucune évacuation d'eau, avec des prises électriques dangereuses posées au-dessus de l'évier.

L'amateur de *vibe coding* naïf agit exactement ainsi : fasciné par la rapidité d'exécution du modèle, il applaudit à chaque écran généré, jusqu'au jour où la base de données se vide sans sauvegarde ou que les données de ses utilisateurs se retrouvent en libre accès sur le web.

Le maître d'ouvrage lucide procède à l'inverse :
- Il ne pose pas lui-même le carrelage et ne soude pas les tuyaux (il laisse l'artisan faire son métier).
- Mais il **valide les plans d'architecte** avant d'abattre une cloison.
- Il consigne par écrit ce qui fait partie de la commande et ce qui est **formellement exclu**.
- Et surtout, il **exige une épreuve d'étanchéité** avant de signer la réception des travaux et de payer la facture.

Dans un projet logiciel assisté par IA, **le code est la maçonnerie, l'agent est l'artisan, et toi, tu es l'architecte**. Tu n'as pas besoin de savoir coder chaque boucle : tu as besoin de savoir si le mur est porteur.

---

### 5. Les quatre niveaux d'autorisation du pilote

Un agent ne doit jamais travailler sans mandat délimité. Dans tes instructions, sépare impérativement les verbes d'action selon quatre niveaux d'autorisation étanches :

| Niveau d'ordre | Verbe clé | Ce que l'agent a le droit de faire | Ce qui lui est strictement interdit |
|---|---|---|---|
| **1. Diagnostic** | *« Analyse »* | Lire les fichiers, inspecter la structure, poser des questions. | Modifier la moindre virgule du code. |
| **2. Élaboration** | *« Implémente »* | Modifier des fichiers locaux et créer un test prouvant le fonctionnement. | Publier en ligne ou écraser l'historique sans preuve. |
| **3. Validation** | *« Prépare la revue »* | Résumer les changements ligne par ligne et isoler le travail sur une branche. | Fusionner sur la version principale sans accord humain. |
| **4. Déploiement** | *« Publie »* | Mettre en service réel sur le serveur de production. | Toute action non précédée d'une série complète de tests au vert. |

En appliquant cette discipline, tu supprimes 99 % des accidents industriels. L'agent ne « prend pas d'initiatives » destructrices : il opère sous mandat.

---

## Mise en pratique

### Rédiger ton premier ordre de mission sans concession

Voici l'exercice fondateur. Imagine que tu pilotes la création d'un service de recueil de dossiers clients. Tu souhaites que l'agent audite la façon dont les fichiers sont actuellement reçus, sans rien casser.

Voici le gabarit exact d'un **ordre de mission déterministe** :

> **Contexte** : Notre projet permet à des utilisateurs de téléverser des documents administratifs.  
> **Objectif** : Analyser le flux actuel de réception des fichiers et identifier les risques en cas de coupure réseau.  
> **Périmètre strict (Niveau 1 - Diagnostic)** : Tu as le droit d'explorer le répertoire du projet et de lire le code existant. Tu n'as **pas le droit** de modifier le code, d'ajouter des dépendances ou de créer des fichiers.  
> **Livrable attendu** : Une note courte (cinq points maximum) décrivant où sont stockés les fichiers, comment l'intégrité est contrôlée et ce qui se passe si le transfert échoue.  
> **Critère d'arrêt** : Dès que ta note est rédigée, arrête-toi et attends mes instructions.

Remarque la précision : aucun flou artistique, aucun espace pour une improvisation hasardeuse. L'agent sait exactement où commence et où s'arrête son autorité.

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu travailles avec un agent sur ton projet. Au bout de dix minutes, il t'envoie ce message enthousiaste :

> *« J'ai remarqué que le traitement des fichiers était un peu lent. J'ai trouvé sur Internet une bibliothèque open source très populaire qui fait ça dix fois plus vite. Je viens de l'installer dans le projet et j'ai réécrit le module. Tout fonctionne très bien sur mon écran ! Souhaites-tu que je déploie en ligne ? »*

### Les questions du pilote

Face à ce message, l'amateur répond : *« Super, merci, envoie en ligne ! »*.  
Le maître d'ouvrage lucide s'arrête immédiatement et pose **trois questions couperet** :

1. **La question de périmètre** : Avais-je demandé d'optimiser la vitesse du traitement aujourd'hui ? *(Non, ce n'était pas dans la mission).*
2. **La question de souveraineté et de sécurité** : Qui a écrit cette bibliothèque externe ? Quelle est sa licence d'utilisation ? A-t-elle été auditée contre les failles de sécurité ? *(L'agent l'ignore).*
3. **La question de preuve** : Sur quoi repose l'affirmation *« Tout fonctionne très bien »* ? Est-ce juste parce que la page s'affiche sans message d'erreur rouge, ou y a-t-il un test automatisé prouvant qu'aucun fichier n'a été corrompu ?

### Le corrigé commenté

**La décision du pilote** : Rejet immédiat de l'initiative.  
Tu réponds fermement à l'agent :  
*« Annule l'installation de cette bibliothèque et rétablis le code dans son état initial. Nous ne modifions pas les dépendances du projet sans arbitrage explicite, et nous n'optimisons pas un composant sans avoir d'abord mesuré le problème avec un test chiffré. Reviens à l'ordre de mission convenu. »*

Ce réflexe vient de sauver ton projet d'une dérive silencieuse. Tu as réaffirmé que dans ton atelier, **c'est l'humain qui décide de la trajectoire, et l'outil qui exécute sous contrôle**.

---

## Checklist réflexe du pilote

Avant de valider une étape produite par un agent, coche systématiquement ces cinq cases mentales :

- [ ] **L'intention est écrite** : Le résultat attendu a été formulé avec des mots clairs, sans jargon flou.
- [ ] **Les limites sont posées** : L'agent sait ce qui est formellement interdit dans cette tâche.
- [ ] **La preuve est observable** : La réussite ne repose pas sur la promesse de l'IA, mais sur une démonstration concrète et vérifiable.
- [ ] **Les données sont protégées** : Aucun mot de passe, aucune donnée client et aucun secret n'ont été exposés ni écrasés.
- [ ] **Le retour arrière est possible** : Si le résultat ne convient pas, une commande simple permet de revenir exactement à l'état antérieur.

---

## Sources et limites

Ce chapitre synthétise les principes de gouvernance logicielle issus des ouvrages de référence du domaine :
- **O-MD §1, §4 et §5** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'application vue comme une organisation, le protocole de conversation sous mandat et l'ordre juste pour construire sans dérive.
- **I-MD §1 et §9.5** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : L'illusion thermodynamique de la vitesse brute et les quatre compétences fondamentales du décideur moderne.

Pour découvrir les rouages d'ingénierie formels (machines à états, interfaces strictes et preuves par le code), poursuis ta lecture avec le chapitre miroir : **[B01 — Piloter un système, pas une génération de code](/ingenieure/01-piloter-un-systeme)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A01](/redaction/a01-piloter-un-systeme).
