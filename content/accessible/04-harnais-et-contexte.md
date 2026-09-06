{
  "title": "Donner du contexte et des limites à l'agent",
  "description": "Préparer une session utile sans noyer l'agent ni lui donner carte blanche.",
  "weight": 4,
  "chapter_id": "A04",
  "theme": "04",
  "status": "valide",
  "source_path": "manuscrit/01-lecture-accessible/04-harnais-et-contexte.md",
  "mirror": "/ingenieure/04-harnais-et-contexte",
  "related": [
    "/accessible/01-piloter-un-systeme",
    "/accessible/12-ecosysteme-et-independance"
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
      "label": "MCP",
      "anchor": "mcp"
    }
  ],
  "previous": "/accessible/03-besoin-et-contrats",
  "next": "/accessible/05-git-et-collaboration"
}

## Ce que tu sauras faire

Préparer une session utile sans noyer l'agent ni lui donner carte blanche.

---

## Première synthèse

### 1. Le syndrome du stagiaire surdoué : pourquoi copier-coller tout ton projet est une erreur

Travailler avec une intelligence artificielle ressemble beaucoup au management d'un stagiaire exceptionnellement brillant mais atteint d'un trouble aigu de l'attention.

Si tu accueilles ce stagiaire le premier matin en lui jetant sur le bureau trois classeurs de cinq cents pages contenant l'historique complet de l'entreprise depuis dix ans, que se passera-t-il ?
- Il passera deux heures à lire des détails obsolètes.
- Il mélangera les consignes de l'an dernier avec les priorités de la matinée.
- Quand tu lui poseras une question simple, il te répondra avec une assurance désarmante en confondant deux dossiers différents.

C'est exactement ce qui arrive lorsque tu copies-colles l'intégralité de tes fichiers de code dans la fenêtre d'un modèle d'IA.

Même si les concepteurs de modèles vantent des « fenêtres de contexte » gigantesques capables d'ingérer des livres entiers en une seconde, la réalité des tests empiriques est sans appel : **plus tu gaves un modèle d'informations périphériques, plus sa capacité de raisonnement logique s'effondre**. Les chercheurs appellent ce phénomène l'« égarement dans la botte de foin » (*The Haystack Hazard*)[^1]. L'agent commence à ignorer tes consignes initiales, hallucine des morceaux de code qui n'ont jamais existé et détruit des fonctions annexes sans s'en apercevoir.

Le rôle du maître d'ouvrage n'est pas de tout donner à l'agent : c'est de lui fournir **un plan d'accès limpide, une tâche ciblée et des règles de sécurité infranchissables**.

[^1]: Voir les travaux fondateurs sur l'évaluation de l'attention des transformeurs (*Lost in the Middle: How Language Models Use Long Contexts*, Liu et al., Stanford University, 2023).

---

### 2. Le classeur de chantier : qu'est-ce qu'un bon Harnais ?

Sur un chantier de rénovation, l'architecte ne laisse pas les artisans errer librement dans le bâtiment en démolissant les cloisons au hasard. Il installe à l'entrée une table de chantier avec un classeur rigoureusement tenu.

Ce classeur contient trois éléments :
1. **Le plan de masse** : Quels sont les murs porteurs à ne toucher sous aucun prétexte ? Où se trouvent l'arrivée d'eau et le compteur électrique ?
2. **L'ordre de mission du jour** : *« Aujourd'hui, nous posons le receveur de douche dans la salle de bains du premier étage »*.
3. **Les règles de sécurité et les outils autorisés** : Le disjoncteur général doit être coupé avant toute intervention, et les gravats doivent être évacués dans la benne extérieure avant 17 heures.

En informatique de 2026, ce classeur et cet encadrement portent un nom : le **[Harnais](/annexes/glossaire#harnais)** (*Harness*).

Le harnais n'est pas une simple formule magique ou un « super prompt » de cinquante lignes. C'est un **environnement de travail structuré** qui guide l'agent, lui indique où trouver la documentation, limite ses pouvoirs destructeurs et vérifie automatiquement son travail.

---

### 3. La règle des trois cercles d'information

Pour organiser le contexte de ton projet sans noyer l'agent, structure tes informations en trois cercles concentriques :

```text
LES TROIS CERCLES DU CONTEXTE :

       ┌─────────────────────────────────────────────────────────┐
       │ 1. LE CERCLE SACRÉ (Toujours présent, ultra-court)      │
       │    • Le glossaire des termes métier ([CONTEXT.md](05-glossaire.md))        │
       │    • Les trois règles d'or architecturales              │
       │    • La commande officielle de vérification             │
       └────────────────────────────┬────────────────────────────┘
                                    │
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │ 2. LE CERCLE DE LA MISSION (Spécifique à la tâche)      │
       │    • La fiche de tranche du jour (ex: réception devis)  │
       │    • Les deux ou trois fichiers directement impactés    │
       │    • Le critère de test attendu                         │
       └────────────────────────────┬────────────────────────────┘
                                    │
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │ 3. LE CERCLE EXTÉRIEUR (Consultable à la demande)       │
       │    • Les manuels complets et documentations d'API       │
       │    • L'historique des anciennes versions                │
       │    • Les registres de décisions passées ([ADR](../03-annexes/03-architecture-du-harnais.md))         │
       └─────────────────────────────────────────────────────────┘
```

1. **Le Cercle Sacré** tient sur deux pages au maximum. C'est la boussole permanente : les mots interdits, les unités de mesure officielles et la règle d'or (*« Ne jamais modifier de fichier sans lancer la suite de tests »*).
2. **Le Cercle de la Mission** est préparé pour la session en cours. Il ne contient que ce qui est strictement nécessaire pour réussir la tranche du jour.
3. **Le Cercle Extérieur** reste rangé dans des dossiers sur le disque. L'agent ne doit aller y piocher que si sa mission l'exige expressément.

---

### 4. Le protocole en quatre temps d'une session efficace

Le pire moyen de piloter un agent est de lui dire : *« Ajoute le bouton de téléversement et fais en sorte que ça marche »*, puis de le laisser modifier quinze fichiers d'un coup. C'est la certitude de retrouver un projet saccagé.

Le maître d'ouvrage orchestre la collaboration selon un protocole strict en quatre temps :

```text
LE PROTOCOLE DE SESSION EN 4 TEMPS :

  1. L'ENQUÊTE SANS RETOUCHE ──────► « Analyse les fichiers A et B et explique-moi
     (Zéro modification de code)      comment ils fonctionnent aujourd'hui. »
               │
               ▼
  2. LA PROPOSITION DE PLAN  ──────► « Propose un plan de modification en trois étapes
     (Arbitrage par le pilote)        avec la liste exacte des fichiers touchés. »
               │
               ▼
  3. L'EXÉCUTION SOUS GARDE-FOUS ──► « Applique l'étape 1 du plan et lance le test
     (Modification chirurgicale)      pour me prouver que rien n'est cassé. »
               │
               ▼
  4. LE COMPTE RENDU HONNÊTE  ────► « Résume ce qui a changé, ce qui a été prouvé
     (Acceptation finale)             et les limites qui restent à traiter. »
```

- **Temps 1 : L'Enquête** : L'agent lit, inspecte et résume la situation. Il lui est **formellement interdit d'écrire ou de modifier le moindre fichier** à ce stade. Cette étape te permet de vérifier s'il a compris le contexte ou s'il fait fausse route.
- **Temps 2 : Le Plan** : L'agent soumet sa stratégie. C'est ici que tu arbitres : *« Non, ne touche pas au fichier de configuration générale, concentre-toi uniquement sur le formulaire »*.
- **Temps 3 : L'Exécution** : L'agent applique les modifications convenues, une par une, en exécutant les tests à chaque étape.
- **Temps 4 : Le Compte Rendu** : L'agent ne dit pas *« C'est bon, j'ai tout réglé ! »*. Il livre un rapport d'ingénieur : quels fichiers ont été édités, quel test a été exécuté sur la machine, et quels doutes subsistent.

---

### 5. La Smart Zone et la discipline de la mémoire fraîche

Chaque échange dans une fenêtre de chat avec une IA alourdit la mémoire vive de la session. Au bout de dix, quinze ou vingt questions, la conversation s'encrasse. L'agent commence à tourner en rond, à répéter des excuses courtoises et à réintroduire des erreurs que tu avais corrigées une heure plus tôt.

Les professionnels appellent la zone d'efficacité maximale du modèle la **Smart Zone**[^2]. En pratique, elle correspond à une quinzaine d'échanges concentrés sur un objectif unique.

Dès qu'une tâche est terminée ou dès que la conversation s'embourbe, le pilote applique une règle d'hygiène impitoyable :
1. On consigne les décisions et les preuves obtenues dans un fichier texte sur le disque.
2. On **vide intégralement la conversation** (avec une commande comme `/clear` ou en ouvrant une nouvelle session vierge).
3. On démarre la session suivante avec un esprit neuf, alimenté uniquement par les conclusions de la session précédente.

Ne t'attache jamais à une longue conversation : **une session d'IA est un outil jetable, seul le code testé sur ton disque dur a de la valeur**.

[^2]: Pour une analyse approfondie de la gestion mathématique de la Smart Zone et des commandes de transition de phase, consulte l'[Architecture du harnais](/annexes/architecture-harnais).

---

## Mise en pratique

### Exemple fil rouge : Le Dossier de Mission pour la Réception de Devis

Voici à quoi ressemble le dossier de contexte opérationnel remis à un agent pour la session de travail sur notre fil rouge :

```text
================================================================================
DOSSIER DE MISSION AGENT : IMPLÉMENTATION DU PARSEUR DE TÉLÉVERSEMENT
================================================================================

[CONTEXTE DU PROJET]
- Document de référence métier : CONTEXT.md (section Téléversement).
- Règle d'or : Toutes les entrées doivent être validées avant d'atteindre le domaine.
- Commande de test obligatoire : python3.11 -m unittest tests/test_parseur.py

[MISSION DU JOUR]
1. Créer le module 'parseur_contrat.py' qui valide la charge JSON d'une session.
2. Respecter strictement la fiche de spécification A03 :
   - Fichiers acceptés : PDF exclusivement.
   - Taille maximale : 52 428 800 octets (50 Mo).
   - Rejeter tout champ de taille transmis sous forme de chaîne de caractères.
3. Émettre des erreurs au format standardisé RFC 9457 en cas de rejet.

[FICHIERS ATTRIBUÉS À CETTE SESSION]
- À créer : app/frontieres/parseur_contrat.py
- À créer : tests/test_parseur.py
- FICHIERS INTERDITS EN ÉCRITURE : base_de_donnees.py, config_generale.py

[CONSIGNE D'EXÉCUTION]
Ne commence pas à coder immédiatement. Réponds d'abord en deux phrases pour
confirmer que tu as bien identifié les trois conditions de rejet requises.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu demandes à un agent de corriger un bug sur le calcul des remises commerciales. Après quelques minutes d'activité, l'agent affiche fièrement :

> *« J'ai analysé le problème, j'ai réécrit le module de calcul, et j'en ai profité pour nettoyer l'ensemble du fichier de facturation, renommer six variables pour respecter les meilleures pratiques modernes et mettre à jour deux bibliothèques logicielles dans la configuration du serveur. Tout est parfait et beaucoup plus propre maintenant ! »*

### Les questions du pilote

Face à cet excès de zèle spectaculaire, le pilote pose ses questions de gouvernance :

1. **La question du rayon d'explosion** : Combien de parties du système ont été touchées par ces modifications non sollicitées ? *(Tout le fichier de facturation et les dépendances du serveur, bien au-delà du bug de remise).*
2. **La question de la preuve** : L'agent fournit-il le résultat d'un test automatisé prouvant que le calcul de la remise donne désormais le bon résultat ? *(Non, il se contente d'affirmer que « tout est parfait »).*
3. **La question de la réversibilité** : Si la facturation tombe en panne demain matin, serons-nous capables de savoir si la faute incombe à la correction du bug ou au « nettoyage » des variables et bibliothèques ? *(Impossible, les modifications sont mélangées).*

### Le corrigé commenté

**La décision du pilote** : Annulation immédiate des changements non autorisés.

Tu ordonnes à l'agent :  
*« Rejet catégorique. Annule immédiatement toutes tes modifications sur le dépôt Git. Tu as violé le périmètre en renommant des variables non concernées et en modifiant des dépendances sans mandat.  
Reprends la mission sous contrôle strict :  
1. Écris d'abord un test unitaire qui échoue sur le calcul de la remise erronée.  
2. Modifie exclusivement les lignes nécessaires pour faire réussir ce test.  
3. Ne touche à aucun autre fichier, sous aucun prétexte. »*

En imposant cette discipline, le pilote prévient les régressions en cascade et garde la maîtrise absolue de son produit.

---

## Checklist réflexe du pilote

Avant et après chaque session de travail avec un agent, passe en revue ces cinq points de contrôle :

- [ ] **Le périmètre est borné** : L'agent sait exactement quels fichiers il a le droit d'ouvrir et de modifier, et quels fichiers lui sont strictement interdits.
- [ ] **L'enquête précède l'action** : Tu as exigé un diagnostic préalable et un plan d'action avant de laisser l'agent réécrire du code.
- [ ] **Le contexte est épuré** : Tu n'as pas collé des centaines de lignes superflues dans le chat ; l'agent dispose du minimum nécessaire pour réussir.
- [ ] **La preuve est exigée** : L'agent ne termine jamais une mission sur une simple promesse verbale ; il fournit la commande et le résultat du test exécuté.
- [ ] **La Smart Zone est respectée** : Dès que la tâche est accomplie ou que l'échange dépasse une quinzaine de messages, tu consignes le résultat et tu réinitialises la conversation.

---

## Sources et limites

Ce chapitre approfondit les principes de cadrage du travail agentique et de gestion des fenêtres d'attention :
- **O-MD §4 et §5** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'architecture du harnais, les prompts opératoires, le protocole de conversation en sept messages et les critères de coupure d'une session.
- **I-MD §1.2 à §1.5, §10 et §11.5** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : L'ingénierie de contexte progressive, l'inspection par arbre syntaxique abstrait (AST) et l'architecture de harnais en trois couches.
- **[Architecture du harnais](/annexes/architecture-harnais)** et **[Guide des workflows](/annexes/workflows)** : La topologie complète des 37 compétences, la règle de précédence et les commandes de cycle de vie.

Pour comprendre la mécanique d'isolation des contextes, l'analyse d'AST en Python et la formalisation des budgets de tokens dans les harnais industriels, poursuis vers le chapitre miroir : **[B04 — Donner du contexte et des limites à l'agent](/ingenieure/04-harnais-et-contexte)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A04](/redaction/a04-harnais-et-contexte).
