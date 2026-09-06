{
  "title": "I-MD — MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md",
  "weight": 1,
  "source_document": true,
  "aliases": [
    "/references/sources/i-md"
  ]
}

Lecture intégrale · **I-MD**. [Télécharger l'original inchangé](/sources/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Le texte ci-dessous est celui du Markdown original, sans résumé ni correction. Seuls sa présentation et ses liens de navigation sont adaptés au site.

---

## TRAITÉ SYSTÉMIQUE & MANUEL DE RÉFÉRENCE DE L'INGÉNIEUR ARCHITECTE
## ARCHITECTURE LOGICIELLE & HARNAIS DE VIBE CODING DÉTERMINISTE

> **Traité exhaustif d'ingénierie logicielle pour décideurs, orchestrateurs et architectes de flottes agentiques.**  
> Théorie fondamentale des abstractions, modularité profonde d'Ousterhout, points de couture de Feathers, isolation Git Worktree concurrente, vérification formelle par TDD inversé, systèmes asynchrones distribués, persistance relationnelle sans coupure, méthode KISS intégrale, bibliothèque opérationnelle de prompts et écosystème libre/agnostique 2026.

---

#### TABLE DES MATIÈRES ANALYTIQUE

1. [Épistémologie du Vibe Coding & Théorie du Harnais Déterministe](#section-1)
   - 1.1 La thermodynamique du code IA et l'illusion de la vélocité brute
   - 1.2 La dérive entropique et la dispersion d'attention (Context Dilution)
   - 1.3 Anatomie fondamentale du Harnais Déterministe
   - 1.4 L'analyse syntaxique (AST) contre l'hallucination textuelle
   - 1.5 Protocoles d'isolation d'exécution (Sandboxing)
2. [Théorie Fondamentale des Abstractions & Modularité Systémique](#section-2)
   - 2.1 La profondeur des modules selon John Ousterhout
   - 2.2 Anatomie d'une interface minimale
   - 2.3 Les Points de Couture (Seams de Michael Feathers)
   - 2.4 Domain-Driven Design : Entités, Value Objects & Agrégats
   - 2.5 L'Architecture Hexagonale (Ports & Adapters) appliquée aux LLM
3. [L'Approche Schema-First & La Rigueur du Typage Invariant](#section-3)
   - 3.1 Pourquoi le langage naturel échoue sans contrat
   - 3.2 Formalisation des interfaces (OpenAPI, JSON Schema, TypeBox)
   - 3.3 Le typage statique comme borne mathématique
   - 3.4 La validation runtime étanche aux frontières réseau
4. [Ingénierie Git Industrielle pour Flottes d'Agents IA](#section-4)
   - 4.1 Git Worktrees : Orchestration concurrente sans collision
   - 4.2 Stacked Pull Requests & Confinement de contexte
   - 4.3 Git Bisect automatisé pour la traque de régressions
   - 4.4 Rebase interactif, Squashing et atomicité des commits
5. [Stratégie de Vérification, Métamétrie & TDD Inversé](#section-5)
   - 5.1 La pyramide de vérification déterministe
   - 5.2 Le protocole du TDD Inversé pour l'IA
   - 5.3 Property-Based Testing (fast-check / Hypothesis)
   - 5.4 Mutation Testing (Stryker) pour l'élimination des faux positifs
6. [Concurrence, Asynchronisme & Systèmes Distribués](#section-6)
   - 6.1 Pourquoi la boucle synchrone détruit la résilience
   - 6.2 Modèle de files de messages & Workers d'arrière-plan
   - 6.3 Idempotence absolue et gestion des déduplications
   - 6.4 Le Transactional Outbox Pattern
7. [Persistance Relationnelle, Base de Données & Migrations Zero-Downtime](#section-7)
   - 7.1 Niveaux d'isolation transactionnelle et anomalies de concurrence
   - 7.2 Verrous pessimistes vs optimistes
   - 7.3 Le Pattern Expand-Contract pour les migrations sans coupure
   - 7.4 Sauvegardes continues et réplication WAL
8. [Cycle Complet de Déploiement : Du Poste Local au VPS](#section-8)
   - 8.1 La chaîne d'assemblage continue (Pipeline CI/CD Matrix)
   - 8.2 Topologie moderne d'un VPS autohébergé
   - 8.3 Configuration du Reverse Proxy Edge avec Caddy
   - 8.4 Gestion des Secrets POSIX et Isolation des Variables
9. [La Méthode KISS Intégrale : De l'Idée au Déploiement](#section-9)
   - 9.1 Le minimalisme radical contre la complexité accidentelle
   - 9.2 Le Workflow Universel en 6 Phases Séquentielles
   - 9.3 Détail Opérationnel des 6 Phases
   - 9.4 La Boîte à Outils Minimale de l'Orchestrateur
   - 9.5 Les 4 Compétences Souveraines du Décideur Non-Codeur
10. [Bibliothèque Opérationnelle de Prompts Déterministes & Protocoles d'Exécution](#section-10)
    - 10.1 Philosophie d'Ingénierie des Prompts pour Harnais Agentique
    - 10.2 Prompts Prêts à l'Emploi pour les 6 Phases KISS
    - 10.3 Prompts Spécialisés pour la Maintenance & Résolution de Crise
    - 10.4 Grille d'Évaluation Décisionnelle de l'Architecte (Checklist PR)
11. [Ingénierie de Production Avancée, Observabilité & Résilience Systémique](#section-11)
    - 11.1 L'Observabilité Active : Télémétrie, Logs Structurés & Tracing Distribué
    - 11.2 Résilience Distribuée : Circuit Breakers, Backoff Exponentiel & Jitter
    - 11.3 Gestion des Échecs Asynchrones : Dead Letter Queues (DLQ) & Poison Pills
    - 11.4 Performance & Optimisation des Données : Indexation & Connection Pooling
    - 11.5 Le Protocole de Mémoire Contextuelle Long-Terme (Agent Memory Bank)
    - 11.6 Le Plan de Reprise d'Activité (PRA / Disaster Recovery)
12. [Écosystème Technologique Agnostique, Modèles Libres & Open Source (Septembre 2026)](#section-12)
    - 12.1 Souveraineté & Paradigme Agnostique : L'Interface Standardisée
    - 12.2 Panorama des Modèles Libres & Open Weights (2026)
    - 12.3 Runtimes d'Inférence & Quantization pour l'Auto-Hébergement
    - 12.4 Moteurs & Outils d'Orchestration Agentique Open Source
    - 12.5 Le Standard Ouvert MCP & Serveurs Locaux Auto-Hébergés
    - 12.6 Matrice d'Arbitrage Éthique & Technique : Propriétaire vs Open Source

---


## 1. Épistémologie du Vibe Coding & Théorie du Harnais Déterministe {#section-1}

### 1.1 La thermodynamique du code IA et l'illusion de la vélocité brute {#section-1-1}
L'avènement des modèles de langage de grande taille (LLM) appliqués à l'ingénierie logicielle a donné naissance à une pratique séduisante mais périlleuse, popularisée sous le nom de *vibe coding*. L'opérateur formule des intentions en langage naturel, et l'agent conversationnel produit instantanément des blocs entiers de code exécutable. Lors des premières heures d'un projet, cette approche confère un sentiment grisant d'omnipotence et de rapidité absolue.

Cependant, du point de vue de la thermodynamique des systèmes logiciels, cette accélération initiale masque un transfert massif d'entropie. Un modèle de langage est un optimiseur statistique de surface : il génère la séquence de symboles la plus probable pour satisfaire la demande textuelle immédiate. Il n'a aucune conscience de l'histoire du système, de ses invariants critiques, de son cycle de vie sur dix ans, ni des compromis de performance sous charge.

En l'absence d'une gouvernance rigoureuse, le code généré par IA adopte la trajectoire de moindre résistance :
* **Duplication opportuniste :** Plutôt que d'abstraire un concept existant, l'agent recopie des fragments entiers avec de légères variations, dispersant la logique métier.
* **Fuite d'abstractions :** Les détails d'implémentation (requêtes SQL, configurations HTTP, protocoles de chiffrement) se mélangent directement à la logique de domaine.
* **Érosion silencieuse des cas d'erreur :** L'agent implémente le "chemin heureux" (happy path) et masque les exceptions par des blocs génériques silencieux (`catch (e) { return null; }`), rendant le système inauditable en production.

Le rôle du directeur technique et de l'architecte n'est plus d'écrire la syntaxe, mais de devenir le **concepteur d'un harnais déterministe**. L'agent IA n'est pas un architecte : c'est un moteur à combustion textuelle ultra-rapide qui doit impérativement être monté sur un châssis mécanique d'une rigidité absolue.

### 1.2 La dérive entropique et la dispersion d'attention (Context Dilution) {#section-1-2}
La limite fondamentale de l'orchestration de modèles de langage réside dans la mécanique interne de leur transformeur. Bien que les fenêtres de contexte s'étendent désormais à des centaines de milliers de tokens, la **qualité de l'attention** ne croît pas de manière linéaire avec la taille du contexte.

> **Théorème de la Dilution d'Attention (The Haystack Hazard) :**  
> Lorsque l'on charge l'intégralité d'un référentiel de code (50 ou 100 fichiers) dans le contexte d'un agent pour lui demander une modification ponctuelle, le modèle subit une dégradation d'attention critique sur les détails intermédiaires. Le taux d'hallucination de variables, l'écrasement de méthodes périphériques et l'oubli des contraintes de sécurité augmentent de manière exponentielle.

Pour contrer cette dilution, l'architecte applique le principe du **confinement chirurgical** : l'agent ne doit jamais être exposé à l'intégralité de l'arbre source. Le harnais sélectionne et présente exclusivement :
1. Le contrat formel du composant ciblé (ses interfaces d'entrée et de sortie).
2. Le fichier de test unitaire décrivant le comportement attendu.
3. Le fichier unique d'implémentation interne en cours d'édition.

Tout le reste du système doit être masqué derrière des abstractions stables. L'agent n'a pas besoin de savoir comment fonctionne le moteur de base de données pour coder une règle de calcul arithmétique de remise commerciale.

### 1.3 Anatomie fondamentale du Harnais Déterministe {#section-1-3}
Un **harnais agentique** est un ensemble d'outils, de processus et de scripts automatisés qui enveloppent l'agent IA. Il opère comme un sas d'interception et de validation en boucle fermée.

```text
+───────────────────────────────────────────────────────────────────────────────────────────+
|                                ANATOMIE DU HARNAIS AGENTIQUE                              |
|                                                                                           |
|  [ CAHIER DES CHARGES FORMEL (Markdown / SPEC.md) ]                                       |
|                           │                                                               |
|                           ▼                                                               |
|  [ CONSTRUCTEUR DE CONTEXTE CHIRURGICAL ]                                                 |
|    ├── Extraction des Types & Schémas d'API (Zod / TypeBox / OpenAPI)                     |
|    ├── Extraction de l'AST ciblé (Arbre Syntaxique Abstrait sans corps de fonction)       |
|    └── Injection de la Banque de Mémoire (activeContext.md & systemPatterns.md)          |
|                           │                                                               |
|                           ▼                                                               |
|  [ MOTEUR AGENTIQUE (LLM) ] ──> Génération d'un UNIFIED DIFF (Patch atomique)             |
|                           │                                                               |
|                           ▼                                                               |
|  [ SAS DE VÉRIFICATION MÉCANIQUE DÉTERMINISTE ]                                           |
|    ├── Étape 1 : Analyse Syntaxique & Validation AST (Tree-sitter)                        |
|    ├── Étape 2 : Vérification Statique des Types (tsc --strict --noEmit)                  |
|    ├── Étape 3 : Analyse des Invariants de Sécurité & Fuite de Secrets (.gitleaks)        |
|    └── Étape 4 : Exécution de la Suite de Tests Unitaires en Boîte Noire                  |
|                           │                                                               |
|         ┌─────────────────┴─────────────────┐                                             |
|         ▼                                   ▼                                             |
|     [ ÉCHEC ]                           [ SUCCÈS ]                                        |
|         │                                   │                                             |
|         ├── Réinjection automatique         └── Commit Atomique formaté                   |
|         │   du message d'erreur brut            sur Git Worktree isolé                    |
|         │   au LLM (Max 3 cycles)                   │                                     |
|         │                                           ▼                                     |
|         └── Si échec persistant :           [ PR / Revue Humaine ]                        |
|             Interruption & Alerte Humain                                                  |
+───────────────────────────────────────────────────────────────────────────────────────────+
```

#### Les 4 Composants Cruciaux du Harnais :
1. **Le Constructeur de Contexte Réduit :** Extrait les déclarations de types et les signatures de fonctions via l'arbre syntaxique abstrait (AST), sans charger le corps inutile des fonctions tierces.
2. **L'Application par Patch Unifié (Diff Atomique) :** Interdiction formelle donnée à l'agent de réécrire des fichiers complets. L'agent ne produit que des blocs de modification ligne par ligne.
3. **La Boucle de Rétroaction Fermée :** Lorsque le compilateur ou la suite de tests échoue, le message d'erreur exact est renvoyé à l'agent pour autocorrection (limité à 3 itérations pour éviter les boucles infinies de divagation).
4. **Le Journal d'Architecture Persistant :** Fichiers de mémoire structurés (`systemPatterns.md`, `activeContext.md`) que l'agent consulte obligatoirement et met à jour à chaque étape.

### 1.4 L'analyse syntaxique (AST) contre l'hallucination textuelle {#section-1-4}
Les approches naïves d'interaction avec l'IA demandent à l'agent de réécrire un fichier complet de 400 lignes pour modifier une condition de 3 lignes. Cette méthode est catastrophique : lors de la régénération intégrale, l'agent introduit couramment des régressions accidentelles, supprime des imports nécessaires ou modifie subtilement des variables sans rapport.

Le harnais moderne impose l'utilisation de **l'Arbre Syntaxique Abstrait (AST)** et du **patch unifié (Unified Diff)** :
* **Le format Diff Unifié :** L'agent ne fournit que les lignes supprimées (`-`) et ajoutées (`+`), repérées par des blocs de contexte (hunks `@@ -x,y +x,y @@`). Le harnais applique le patch via des bibliothèques déterministes. Si le patch ne s'applique pas proprement, la proposition est rejetée sans altérer le disque.
* **L'inspection AST (Tree-sitter / Babel / ESLint) :** Le harnais analyse la structure syntaxique du code modifié. Il vérifie que l'agent n'a pas introduit de variables globales, n'a pas enfreint les règles d'encapsulation (ex: importer un module réseau dans un fichier de domaine métier pur) et respecte scrupuleusement les conventions de nommage du projet.

### 1.5 Protocoles d'isolation d'exécution (Sandboxing) {#section-1-5}
Un agent de code moderne n'est pas un simple moteur de texte : il invoque des outils externes (exécution de scripts, installations de packages npm/pip, lancements de serveurs de tests). Laisser un agent exécuter des commandes non filtrées sur l'environnement de développement local de l'opérateur est une faille de gouvernance critique.

| Niveau d'Isolation | Mécanisme Sous-jacent | Risques Neutralisés |
| :--- | :--- | :--- |
| **Isolation Système de Fichiers (Git Worktrees)** | Création d'un répertoire miroir physiquement séparé sur le disque, rattaché au même dépôt `.git`. | Empêche l'agent de modifier les fichiers ouverts dans l'éditeur de l'opérateur humain pendant son exécution. |
| **Isolation Processus (Docker / Podman Sandbox)** | Exécution de toutes les commandes de build, de test et de formatage dans des conteneurs Linux non privilégiés (rootless). | Empêche toute modification de variables d'environnement système globales, toute corruption du système d'exploitation hôte ou toute fuite de fichiers locaux hors du projet. |
| **Isolation Réseau & Micro-VMs (Firecracker / gVisor)** | Isolation au niveau du noyau Linux avec coupure totale de l'accès à Internet lors de l'exécution des tests. | Neutralise les attaques de chaîne d'approvisionnement (Supply Chain Attacks) issues de paquets malveillants tentant d'exfiltrer des clés SSH ou des secrets locaux. |


---

## 2. Théorie Fondamentale des Abstractions & Modularité Systémique {#section-2}

### 2.1 La profondeur des modules selon John Ousterhout {#section-2-1}
Dans son ouvrage de référence *A Philosophy of Software Design*, le professeur John Ousterhout (Université de Stanford) formule le principe fondamental distinguant une architecture pérenne d'un bourbier technique : la **profondeur des modules (Deep Modules)**.

Dans la conception logicielle classique, la complexité est inévitable. Cependant, la mauvaise conception disperse cette complexité sous forme de **modules superficiels (Shallow Modules)**, alors que la bonne conception la concentre et la dissimule à l'intérieur de **modules profonds**.

> **Formulation Mathématique de la Valeur d'un Module :**  
> La valeur $V$ apportée par un module est directement proportionnelle à la complexité de la fonctionnalité qu'il implémente ($C_{interne}$) et inversement proportionnelle à la complexité de son interface publique ($C_{interface}$) :
> $$V = \frac{C_{interne}}{C_{interface}}$$  
> Un module profond maximise $V$ en offrant une interface $C_{interface}$ extrêmement réduite pour un bénéfice fonctionnel $C_{interne}$ maximal. Un module superficiel a une interface presque aussi complexe que son implémentation ($V \approx 1$), n'apportant aucun gain d'abstraction.

```text
COMPARAISON VISUELLE DE PROFONDEUR ARCHITECTURALE :

      MODULE PROFOND (Idéal pour l'IA)               MODULE SUPERFICIEL (Anti-pattern)
   +─────────────────────────────────────+        +─────────────────────────────────────+
   | INTERFACE MINIMALE : 2 FONCTIONS    |        | INTERFACE LARGE : 12 MÉTHODES       |
   | read(id), write(id, payload)        |        | init(), config(), setBuff(), auth(),|
   +─────────────────────────────────────+        | lock(), flush(), verify(), clear()..|
   |                                     |        +─────────────────────────────────────+
   | COMPLEXITÉ INTERNE FORTE (MASQUÉE)  |        | COMPLEXITÉ INTERNE MINIME           |
   | • Gestion des pools de connexion DB |        | (Ne fait que relayer les paramètres |
   | • Mise en cache LRU mémoire         |        |  vers un autre micro-composant sans |
   | • Détection des collisions & Locks  |        |  véritable transformation)          |
   | • Retry exponentiel sur panne       |        |                                     |
   | • Chiffrement AES-256 au vol        |        +─────────────────────────────────────+
   +─────────────────────────────────────+
```

#### Pourquoi ce principe est vital avec des agents de code IA :
Les modèles de langage sont particulièrement mauvais lorsqu'ils doivent naviguer dans des architectures "superficielles". Lorsqu'une action nécessite d'orchestrer 15 petits fichiers passe-plats de 10 lignes chacun, l'agent perd le fil conducteur, sature sa fenêtre d'attention et produit des bugs d'assemblage.

En imposant des modules profonds, l'architecte offre à l'agent un **point d'appui inébranlable**. L'agent peut refondre l'intégralité de l'algorithme interne d'un module profond sans toucher à la moindre ligne du reste du système, car l'interface publique reste strictement identique.

### 2.2 Anatomie d'une interface minimale {#section-2-2}
Une interface logicielle bien conçue doit répondre à quatre critères d'excellence formelle :
1. **L'Omniprésence des Valeurs par Défaut Sensées :** L'interface doit fonctionner parfaitement dans 95% des cas sans exiger de paramètres de configuration exotiques.
2. **L'Absence d'Exceptions d'Implémentation Fuiteuses :** Un module de stockage ne doit jamais laisser s'échapper une erreur brute de pilote PostgreSQL ou une erreur de socket réseau. Il capture les erreurs techniques internes et émet exclusivement des erreurs de domaine typées et documentées (ex: `DocumentNotFoundError`, `StorageQuotaExceededError`).
3. **La Cohérence Temporelle (Statelessness) :** Une fonction ne doit pas exiger que d'autres fonctions soient appelées dans un ordre temporel occulte et non vérifiable par le compilateur (ex: interdiction d'exiger `module.init()` avant `module.process()` si le compilateur ne peut pas l'imposer à la compilation).
4. **L'Immutabilité des Paramètres :** Les structures de données passées en argument ne doivent jamais être mutées directement à l'intérieur du module (élimination stricte des effets de bord cachés).

### 2.3 Les Points de Couture (Seams de Michael Feathers) {#section-2-3}
Dans son ouvrage capital *Working Effectively with Legacy Code*, Michael Feathers formalise la notion de **Point de Couture (Seam)** : un endroit d'un programme où l'on peut altérer son comportement sans modifier le code source situé à cet endroit.

Pour un décideur pilotant une flotte d'agents IA, les Seams représentent les **charnières de testabilité et de substitution** indispensables pour valider le code généré en isolation totale :
* **1. Object Seams (Polymorphisme & Injection de Dépendances) :** Le module ne crée pas directement ses dépendances (`new PostgresDatabase()`), mais les reçoit sous forme d'une interface générique (`IDatabase`) dans son constructeur. Permet au harnais de tests d'injecter une implémentation en mémoire (`InMemoryDatabase`) ultra-rapide sans base de données réelle.
* **2. Link Seams (Résolution au Moment du Build) :** L'interception s'opère au niveau de la résolution des paquets par le chargeur de modules (Node.js `module-alias`, TypeScript `paths`, Python `sys.path`). Permet de court-circuiter tous les modules de paiement (Stripe, PayPal) ou d'envoi d'emails (Resend, SendGrid) lors des tests de l'agent.
* **3. Preprocessing Seams (Variables d'Environnement & Compilation Conditionnelle) :** L'évaluation logique dépend de constantes injectées avant l'exécution. Permet d'activer des traces télémétriques hyper-détaillées uniquement lorsque l'agent est en phase d'investigation de bug autonome.

### 2.4 Domain-Driven Design : Entités, Value Objects & Agrégats {#section-2-4}
Le Domain-Driven Design (DDD), conceptualisé par Eric Evans, fournit le langage formel indispensable pour modéliser un système sans ambiguïté :

| Concept DDD | Définition Sémantique | Règles d'Implémentation pour l'Agent IA |
| :--- | :--- | :--- |
| **Value Object (VO)** | Objet immuable défini strictement par la totalité de ses attributs. Ne possède aucun identifiant unique. Deux VO ayant les mêmes valeurs sont strictement identiques. | Doit être instancié via une méthode de fabrique qui valide les invariants (`EmailAddress.create("user@domain.com")`). Interdiction de modifier les champs après création. |
| **Entité (Entity)** | Objet défini par une identité continue qui traverse le temps (un identifiant unique persistant), même si ses propriétés internes mutent continuellement. | Possède un ID immuable (UUID v7 ou NanoID). Les mutations d'état ne se font jamais par assignation directe (`user.age = 20`) mais par des méthodes métier explicites (`user.celebrateBirthday()`). |
| **Agrégat (Aggregate)** | Grappe d'entités et de Value Objects traitée comme une unité cohérente pour les modifications de données. Délimite une frontière transactionnelle stricte. | Accessible uniquement via son **Aggregate Root** (racine d'agrégat). Aucun objet extérieur ne peut modifier directement une entité interne sans passer par la racine. |

### 2.5 L'Architecture Hexagonale (Ports & Adapters) {#section-2-5}
Créée par Alistair Cockburn, l'architecture hexagonale est la structure de référence absolue pour les projets développés avec des agents IA. Elle garantit que le cœur métier du logiciel est totalement indépendant des technologies périphériques.

```text
                       TOPOLOGIE HEXAGONALE COMPLÈTE :
                       
   [ CLIENT HTTP ]      [ CRON TRIGGER ]      [ WEBHOOK EXT ]
          │                    │                     │
          ▼                    ▼                     ▼
   ┌─────────────────────────────────────────────────────────────┐
   │             ADAPTATEURS PRIMAIRES (DRIVING)                 │
   │   (Fastify Controller, CLI Command, Message Consumer)       │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                   PORTS D'ENTRÉE (INBOUND)                  │
   │               (Interfaces de Cas d'Usage)                   │
   │   ex: ICreateOrderUseCase, IGeneratePrintPdfUseCase         │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                    CŒUR DE DOMAINE PUR                      │
   │   • Entités Métier (Commande, LivrePhoto, Page)             │
   │   • Value Objects (Dimensions, CouleurCMJN, PrixTTC)        │
   │   • Règles de validation arithmétiques & contraintes        │
   │   • ZÉRO DÉPENDANCE VERS LE RÉSEAU, SQL OU NPM EXTERNE      │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                   PORTS DE SORTIE (OUTBOUND)                │
   │             (Interfaces d'Infrastructure Requises)          │
   │   ex: IOrderRepository, IStorageProvider, IPaymentGateway   │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
   ┌─────────────────────────────────────────────────────────────┐
   │            ADAPTATEURS SECONDAIRES (DRIVEN)                 │
   │   (PostgreSQL Drizzle/Prisma, Redis BullMQ, S3/R2 SDK)      │
   └─────────────────────────────────────────────────────────────┘
```

#### Les 3 Lois Inviolables de l'Hexagone pour l'IA :
1. **La Loi d'Isolation Radicale :** Le répertoire `core/domain` ne doit contenir aucun import de bibliothèque externe (pas d'Express, pas de Fastify, pas de SQL, pas de Docker). C'est du code TypeScript ou Python pur et mathématique.
2. **L'Inversion de Contrôle Totale :** Ce n'est pas le domaine qui appelle la base de données, c'est le domaine qui définit une interface (le Port), et l'infrastructure implémente cette interface (l'Adaptateur).
3. **L'Interchangeabilité sans Impact :** Changer de moteur de base de données (ex: migrer de PostgreSQL vers SQLite) ne modifie pas une seule virgule dans le dossier de domaine métier.


---

## 3. L'Approche Schema-First & La Rigueur du Typage Invariant {#section-3}

### 3.1 Pourquoi le langage naturel échoue sans contrat {#section-3-1}
Le langage naturel est saturé d'imprécisions, de non-dits et de glissements sémantiques. Lorsque l'on demande à un agent : *"Crée une fonction qui valide une commande utilisateur"*, le modèle comble les vides par inférence statistique :
* Que contient un utilisateur ? Un ID entier ou un UUID ?
* Le prix est-il un nombre à virgule flottante ou un entier en centimes ?
* Que se passe-t-il si la liste d'articles est vide ? Renvoie-t-on une erreur ou un objet vide ?

Si ces questions ne sont pas tranchées dans un **contrat formel de données**, chaque agent IA produira une interprétation divergente à chaque itération. Le système finit par s'effondrer sous le poids des incohérences de types aux frontières des modules.

### 3.2 Formalisation des interfaces (OpenAPI, JSON Schema, TypeBox) {#section-3-2}
L'ingénierie **Schema-First** impose de rédiger et figer le schéma de données avant d'écrire la moindre logique de calcul. Le schéma est la source unique de vérité (Single Source of Truth) dont découlent automatiquement le typage statique, la validation runtime et la documentation de l'API.

```typescript
import { Type, Static } from '@sinclair/typebox';

// 1. Définition du schéma d'entrée strictement contraint
export const OrderItemSchema = Type.Object({
  sku: Type.String({ 
    pattern: '^[A-Z0-9]{4}-[0-9]{3}$', 
    description: 'Format normalisé du SKU (ex: BOOK-001)' 
  }),
  quantity: Type.Integer({ 
    minimum: 1, 
    maximum: 100, 
    description: 'Quantité unitaire commandée' 
  }),
  unitPriceCents: Type.Integer({ 
    minimum: 0, 
    description: 'Prix unitaire en centimes entiers (évite les erreurs de float)' 
  }),
});

export const CreateOrderRequestSchema = Type.Object({
  customerId: Type.String({ format: 'uuid' }),
  items: Type.Array(OrderItemSchema, { minItems: 1, maxItems: 50 }),
  currency: Type.Union([Type.Literal('EUR'), Type.Literal('USD')]),
  shippingAddress: Type.Object({
    street: Type.String({ minLength: 5, maxLength: 150 }),
    postalCode: Type.String({ minLength: 3, maxLength: 10 }),
    city: Type.String({ minLength: 2, maxLength: 100 }),
    countryCode: Type.String({ minLength: 2, maxLength: 2, pattern: '^[A-Z]{2}$' }),
  }),
});

// 2. Dérivation automatique des types statiques pour le compilateur
export type OrderItem = Static<typeof OrderItemSchema>;
export type CreateOrderRequest = Static<typeof CreateOrderRequestSchema>;
```

### 3.3 Le typage statique comme borne mathématique {#section-3-3}
Le système de types d'un langage moderne (TypeScript en mode `strict: true`, Rust, OCaml, Go) n'est pas un simple accessoire d'autocomplétion pour l'éditeur : c'est un **système de démonstration automatique de théorèmes**.

En vertu de l'isomorphisme de Curry-Howard, un type correspond à une proposition logique, et le programme correspond à la preuve de cette proposition. Si l'agent IA produit un code qui viole les types (par exemple en oubliant de gérer le cas `undefined` ou en passant un tableau au lieu d'un objet), le compilateur rejette formellement la preuve.

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}
```

### 3.4 La validation runtime étanche aux frontières réseau {#section-3-4}
Une erreur mortelle consiste à croire que parce que le code est typé en TypeScript, les données circulant sur le réseau sont automatiquement valides. À l'exécution, le JavaScript généré n'a plus aucune notion de type statique.

Le harnais impose le principe du **parseur de frontière (Parse, Don't Validate)** : aucune donnée externe (provenant du payload HTTP d'un client, d'un webhook Stripe, d'une ligne d'un fichier CSV ou d'un enregistrement en base de données) n'est injectée dans le domaine métier sans avoir été préalablement parsée et instanciée par un validateur de schéma.

```text
FLUX DE VALIDATION AUX FRONTIÈRES :

[ Flux Brut Non Sécurisé (JSON HTTP) ]
                │
                ▼
  [ Parseur Runtime (TypeBox / Zod) ]
                │
        ┌───────┴───────┐
        ▼               ▼
   [ INVALIDE ]    [ CONFORME ]
        │               │
        ▼               ▼
  Rejet 400 Immédiat   [ Type Statique Garanti Invariant ]
  (Zéro propagation)    │
                        ▼
                [ Domaine Métier Pur ]
```


---

## 4. Ingénierie Git Industrielle pour Flottes d'Agents IA {#section-4}

### 4.1 Git Worktrees : Orchestration concurrente sans collision {#section-4-1}
Dans l'ingénierie logicielle traditionnelle, un développeur utilise une copie de travail unique et bascule d'une branche à l'autre via la commande `git checkout` ou `git switch`. Cette méthode est incompatible avec l'utilisation d'agents IA autonomes opérant en tâche de fond.

Si un agent modifie des fichiers sur le disque pendant que l'opérateur humain examine du code ou effectue une relecture, les fichiers entrent en collision dans l'IDE, créant des pertes de modifications et des corruptions d'état.

La solution standard de l'industrie repose sur les **Git Worktrees**. Un dépôt Git local est composé de deux entités distinctes :
1. **Le répertoire d'objets (`.git`) :** La base de données immuable contenant l'intégralité de l'historique, des commits, des arbres et des blobs.
2. **L'arbre de travail (Worktree) :** Le répertoire physique contenant les fichiers réels extraits pour une branche spécifique.

```text
TOPOLOGIE D'EXÉCUTION PARALLÈLE AVEC GIT WORKTREES :

                      BASE DE DONNÉES CENTRALE GIT (.git)
                      [ Historique, Objets SHA-1/SHA-256, Refs ]
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
  WORKTREE PRINCIPAL           WORKTREE AGENT-ALPHA           WORKTREE AGENT-BETA
  Dossier: ~/src/app-main      Dossier: ~/src/agent-pdf       Dossier: ~/src/agent-auth
  Branche: main                Branche: feat/pdf-engine       Branche: fix/session-timeout
  [Opérateur Humain / Lead]    [Agent IA - Tâche A]           [Agent IA - Tâche B]
  Éditeur ouvert sur VS Code   Compilation / Tests en boucle  Linter / AST Analysis en cours
```

#### Guide Opérationnel des Commandes Worktree :
```bash
# 1. Créer un nouvel espace de travail complètement étanche pour une tâche assignée à l'agent
git worktree add ../agent-task-pdf -b feat/pdf-render-engine

# 2. L'agent IA est exécuté avec pour répertoire racine STRICT ~/src/agent-task-pdf
# L'agent lit, écrit, exécute les tests unitaires et commite de manière totalement isolée

# 3. Une fois la Pull Request validée et intégrée sur main :
git worktree remove ../agent-task-pdf

# 4. Nettoyage des références administratives internes
git worktree prune
```

### 4.2 Stacked Pull Requests & Confinement de contexte {#section-4-2}
L'un des plus grands écueils du vibe coding consiste à laisser l'agent créer des "méga-branches" touchant à 45 fichiers simultanément. Ces PR massives sont impossibles à auditer pour un humain et masquent des régressions critiques.

L'architecte impose la méthode des **Stacked Pull Requests (PRs Empilées)** : chaque grande fonctionnalité est découpée en une séquence linéaire de micro-branches atomiques de moins de 150 lignes chacune.

```text
SÉQUENCE LINÉAIRE DE STACKED PULL REQUESTS :

  [ Branche: main ] (Production Stable)
         ▲
         │ (Merge PR #101 : 40 lignes)
  [ PR #1 : feat/order-schema ] ──> Définition exclusive des contrats Zod & types TypeScript
         ▲
         │ (Merge PR #102 : 90 lignes)
  [ PR #2 : feat/order-domain ] ──> Logique métier pure + Tests unitaires (In Memory)
         ▲
         │ (Merge PR #103 : 80 lignes)
  [ PR #3 : feat/order-db-adapter ] ──> Adaptateur PostgreSQL Drizzle + Migrations SQL
         ▲
         │ (Merge PR #104 : 60 lignes)
  [ PR #4 : feat/order-http-routes ] ──> Contrôleur HTTP Fastify + Validation frontières
```

### 4.3 Git Bisect automatisé pour la traque de régressions {#section-4-3}
Lorsque plusieurs agents ou développeurs intègrent des dizaines de modifications par jour, il arrive qu'un bug furtif s'insinue dans la base de code sans être détecté immédiatement par les tests unitaires locaux.

La commande `git bisect` met en œuvre un algorithme de **recherche dichotomique binaire** dans le graphe orienté acyclique (DAG) des commits pour identifier mathématiquement le commit coupable en $O(\log N)$ étapes :

```bash
# 1. Démarrer la session de recherche dichotomique
git bisect start

# 2. Marquer le commit actuel (contenant le bug) comme mauvais
git bisect bad

# 3. Marquer le dernier tag de version stable connue comme bon
git bisect good v2.4.0

# 4. Lancer l'exécution automatisée de la suite de tests de non-régression
git bisect run npm test -- test/regression/order-calculation.test.ts

# Git traverse automatiquement l'arbre, teste chaque commit intermédiaire,
# et affiche en quelques secondes : "a1b2c3d is the first bad commit"
git bisect reset
```

### 4.4 Rebase interactif, Squashing et atomicité des commits {#section-4-4}
Les agents IA génèrent un historique Git désordonné lorsqu'ils itèrent pour corriger leurs propres erreurs de syntaxe (ex: messages de commit du type *"fix typo", "retry test", "adjust import", "test again"*). Laisser ces micro-commits polluer la branche principale est une faute professionnelle.

Avant toute fusion, le harnais ou l'architecte impose un **Rebase Interactif (`git rebase -i`)** avec **Squashing** :
* Toutes les micro-étapes intermédiaires sont condensées en un commit unique, auto-suffisant et atomique.
* Le message de commit final respecte scrupuleusement la spécification **Conventional Commits** (ex: `feat(order): implement volume discount calculation rules`).
* L'historique de la branche `main` reste parfaitement linéaire, propre et réversible en production en cas de rollback d'urgence.


---

## 5. Stratégie de Vérification, Métamétrie & TDD Inversé {#section-5}

### 5.1 La pyramide de vérification déterministe {#section-5-1}
L'architecture de tests d'un système piloté par IA ne doit rien laisser au hasard. La distribution des efforts de vérification doit respecter une pyramide d'automatisation rigoureusement proportionnée.

```text
                    PYRAMIDE COMPLÈTE DE VÉRIFICATION SYSTÉMIQUE :

                        /                        /   \       <-- TESTS E2E (Playwright / Cypress)
                      / E2E \          Couverture : < 5% | Durée : 2-5 min | Coût : Élevé
                     /───────\         Vérifient le parcours navigateur utilisateur complet.
                    /                            /   INTEG   \   <-- TESTS D'INTÉGRATION (DB Réelle, Redis, Seams)
                  /             \      Couverture : ~20% | Durée : 10-30s | Coût : Moyen
                 /───────────────\     Vérifient l'assemblage entre le domaine et l'infrastructure.
                /                                /    UNITAIRES      \ <-- TESTS UNITAIRES EN BOÎTE NOIRE (Vitest / Pytest)
              /                     \    Couverture : > 75% | Durée : < 1s | Coût : Minime
             /───────────────────────\   Vérifient la pureté arithmétique et les règles métier.
            /                                    /     ANALYSE STATIQUE      \ <-- ANALYSE STATIQUE, LINTER & AST (tsc, ESLint)
          /                             \    Couverture : 100% | Durée : Immédiate | Zéro exécution
         /───────────────────────────────\   Prouvent l'absence d'erreurs de syntaxe et de types.
```

### 5.2 Le protocole du TDD Inversé pour l'IA {#section-5-2}
Le Test-Driven Development (TDD) traditionnel exige du développeur qu'il écrive le test unitaire avant d'écrire le code fonctionnel. Dans le paradigme du vibe coding supervisé, cette méthode se transforme en une **arme de gouvernance absolue : le TDD Inversé**.

1. **Étape 1 : Rédaction de la Spécification Formelle (Humain)**  
   L'architecte formalise les exigences et les cas d'angle dans un document Markdown succinct mais sans équivoque (ex: *"Une commande supérieure à 100€ bénéficie de la livraison gratuite sauf si elle contient des articles en promotion ou dépasse 15 kg"*).
2. **Étape 2 : Génération Exclusive de la Suite de Tests (Agent IA)**  
   L'agent reçoit l'ordre strict de produire *uniquement* le fichier de test unitaire (`shippingCost.test.ts`). Il lui est formellement interdit de créer ou modifier le fichier de logique métier.
3. **Étape 3 : Audit & Verrouillage du Test (Humain)**  
   L'architecte lit le fichier de test. Comme un test unitaire est court et purement déclaratif, sa relecture prend moins de 60 secondes. L'architecte s'assure que tous les cas limites sont testés. Une fois validé, le fichier est marqué en **lecture seule** pour l'agent.
4. **Étape 4 : Implémentation sous Contrainte Mécanique (Agent IA)**  
   L'agent reçoit l'ordre d'implémenter la logique métier jusqu'à ce que la commande `vitest run` renvoie un code de sortie `0`. L'agent ne peut pas "tricher" en modifiant le test pour masquer son incompétence.

### 5.3 Property-Based Testing (fast-check / Hypothesis) {#section-5-3}
Les tests unitaires classiques souffrent d'un biais cognitif majeur : ils ne testent que les valeurs imaginées par l'humain (ex: `age = 25`, `price = 10.0`). Les bugs critiques en production surviennent systématiquement sur des données inattendues.

Le **Property-Based Testing (PBT)** inverse cette approche. On ne teste pas des exemples, mais des **propriétés invariantes** sur des milliers de données générées pseudo-aléatoirement :

```typescript
import { test, expect } from 'vitest';
import * as fc from 'fast-check';
import { compressData, decompressData } from './compression';

// Propriété invariante : La décompression de la compression doit être strictement idempotente
test('Propriété Invariante : decompress(compress(x)) === x pour toute chaîne Unicode', () => {
  fc.assert(
    fc.property(fc.fullUnicodeString(), (inputString) => {
      const compressed = compressData(inputString);
      const restored = decompressData(compressed);
      expect(restored).toBe(inputString);
    }),
    { numRuns: 5000 } // Exécute 5 000 tests sur des cas extrêmes (caractères nuls, émojis, dépassements)
  );
});
```

### 5.4 Mutation Testing (Stryker) pour l'élimination des faux positifs {#section-5-4}
Un écueil redoutable lors du pilotage d'agents IA est le phénomène des **tests coquilles vides** : l'agent produit une suite de tests avec 100% de couverture de code, mais sans aucune assertion réelle ou avec des assertions toujours vraies (ex: `expect(true).toBe(true)`).

Pour auditer la robustesse réelle d'une suite de tests, le harnais applique le **Mutation Testing** via des outils comme Stryker :
1. Le framework injecte des altérations syntaxiques délibérées dans le code de production (les "mutants"), par exemple en remplaçant `a > b` par `a >= b` ou en supprimant une instruction `return`.
2. La suite de tests est exécutée contre chaque mutant.
3. Si au moins un test échoue, le mutant est déclaré **"Tué" (Killed)** : le test est robuste.
4. Si tous les tests continuent de passer avec succès, le mutant a **"Survécu" (Survived)** : la suite de tests est défaillante. Le harnais rejette la contribution de l'agent.


---

## 6. Concurrence, Asynchronisme & Systèmes Distribués {#section-6}

### 6.1 Pourquoi la boucle synchrone détruit la résilience {#section-6-1}
Une anomalie d'architecture fréquente produite par les agents de code est le traitement synchrone des tâches consommatrices de ressources directement dans le fil d'exécution de la requête HTTP principale (ex: générer un PDF haute résolution, envoyer un email de confirmation, redimensionner une image bitmap, appeler une API distante lente).

Cette pratique engendre un effondrement immédiat du serveur sous charge :
* **Saturation de la boucle d'événements (Event Loop Lag) :** Le serveur devient incapable de traiter les requêtes entrantes légères.
* **Timeouts Clients en Cascade :** Si le client interrompt sa connexion réseau avant la fin du calcul, le serveur continue inutilement son travail dans le vide.
* **Perte Sèche de Données en Cas de Crash :** Si le processus redémarre pendant le traitement, la tâche est définitivement perdue sans reprise possible.

### 6.2 Modèle de files de messages & Workers d'arrière-plan {#section-6-2}
La règle architecturale fondamentale impose de scinder tout traitement dépassant 50 millisecondes en un flux **asynchrone découpé par une file de messages persistante** (Redis BullMQ, RabbitMQ, PostgreSQL LISTEN/NOTIFY).

```text
TOPOLOGIE DU DÉCOUPAGE ASYNCHRONE INDUSTRIEL :

   [ CLIENT WEB / APP ]
            │
            ├── 1. HTTP POST /documents/generate ────────────────────────┐
            │                                                            │
            ▼                                                            ▼
   [ SERVEUR API FASTIFY ]                                      [ RETOUR IMMÉDIAT (10ms) ]
      • Valide le contrat d'entrée (Zod Schema)                 HTTP 202 Accepted
      • Écrit la commande en base SQL (State: QUEUED)           Payload: { jobId: "job_99",
      • Publie le message dans Redis BullMQ                                status: "PENDING" }
            │
            ▼
   [ FILE REDIS PERSISTANTE (BullMQ) ]
      • Stockage en mémoire avec persistance disque RDB/AOF
      • Gestion des priorités, retries exponentiels et dead-letter queue
            │
            ▼ (Consommation asynchrone concurrente)
   [ WORKER DE TRAITEMENT DÉDIÉ (GOF PDF Engine) ]
      • Dépile le message de manière exclusive
      • Exécute le rendu lourd (Calculs vectoriels, Canvas, Rasterisation)
      • Téléverse le document final sur le stockage objet chiffré (Cloudflare R2 / S3)
      • Met à jour l'enregistrement SQL (State: COMPLETED, Url: "https://...")
      • Émet une notification de fin (Server-Sent Events / Webhook)
```

### 6.3 Idempotence absolue et gestion des déduplications {#section-6-3}
Dans tout système distribué ou réseau sans fil, la garantie de livraison d'un message est au mieux de type **Au moins une fois (At-least-once delivery)**. En raison des coupures réseau et des réessais automatiques, le serveur est garanti de recevoir des requêtes dupliquées.

> **Théorie de l'Idempotence en Génie Logiciel :**  
> Une opération $f$ est dite **idempotente** si son application répétée produit exactement le même effet sur le système qu'une application unique :  
> $$\forall x, \quad f(f(x)) = f(x)$$  
> Tout appel d'écriture critique (débit bancaire, création de commande, réservation de stock) doit impérativement exiger un en-tête `Idempotency-Key` unique fourni par le client.

#### Mécanisme d'implémentation de la Clé d'Idempotence :
1. Le serveur reçoit la requête avec l'en-tête `Idempotency-Key: uuid-123`.
2. Dans une transaction Redis ou SQL atomique, il tente d'acquérir un verrou sur cette clé (`SET key status NX EX 300`).
3. Si la clé existe déjà avec le statut `COMPLETED`, le serveur renvoie immédiatement le résultat mis en cache **sans réexécuter la logique métier**.
4. Si la clé n'existe pas, il exécute la logique, sauvegarde la réponse dans le cache d'idempotence et libère le verrou.

### 6.4 Le Transactional Outbox Pattern {#section-6-4}
L'un des bugs les plus destructeurs dans les architectures asynchrones est le **problème de la double écriture non atomique** : le code enregistre une commande en base SQL, puis tente de publier un message dans Redis. Si le serveur plante exactement entre ces deux opérations, la commande est en base mais ne sera jamais traitée.

Le **Transactional Outbox Pattern** résout mathématiquement cette incohérence en éliminant les transactions distribuées (2PC) :

```text
FONCTIONNEMENT DU PATTERN TRANSACTIONAL OUTBOX :

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                 TRANSACTION SQL ATOMIQUE UNIQUE (ACID)                  │
  │                                                                         │
  │   1. INSERT INTO orders (id, customer, total) VALUES ('ord_1', ...);    │
  │   2. INSERT INTO outbox (id, event_name, payload, status)               │
  │      VALUES ('evt_1', 'OrderCreated', '{"id":"ord_1"}', 'PENDING');     │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                        COMMIT LOCAL RÉUSSI EN BASE
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                   PROCESSUS DE DÉPONTAGE (OUTBOX RELAY)                 │
  │                                                                         │
  │   • Lit périodiquement les lignes PENDING dans la table outbox          │
  │   • Publie le message dans Redis / Kafka avec garantie de livraison     │
  │   • Marque la ligne comme PROCESSED ou la supprime                      │
  └─────────────────────────────────────────────────────────────────────────┘
```


---

## 7. Persistance Relationnelle, Base de Données & Migrations Zero-Downtime {#section-7}

### 7.1 Niveaux d'isolation transactionnelle et anomalies de concurrence {#section-7-1}
La persistance des données ne doit jamais être abandonnée aux abstractions superficielles d'un ORM généré par IA. Une mauvaise compréhension des verrous et de l'isolation transactionnelle mène à des corruptions silencieuses de base de données.

| Niveau d'Isolation SQL | Anomalies Tolérées / Interdites | Comportement & Recommandation |
| :--- | :--- | :--- |
| **Read Uncommitted** | Tolère les Dirty Reads, Non-Repeatable Reads, Phantoms. | À bannir formellement. Permet de lire des données en cours de modification par une transaction non commitée qui va être annulée. |
| **Read Committed (Défaut PostgreSQL)** | Empêche les Dirty Reads. Tolère les Non-Repeatable Reads et Phantoms. | Standard recommandé pour 90% des requêtes de consultation. Chaque instruction SQL au sein d'une transaction ne voit que les données commitées avant son début. |
| **Repeatable Read** | Empêche les Dirty Reads et Non-Repeatable Reads. Élimine les Phantoms dans PostgreSQL. | Garantit qu'une ligne relue plusieurs fois dans la même transaction aura exactement les mêmes valeurs. Indispensable pour les rapports financiers cohérents. |
| **Serializable** | Empêche TOUTES les anomalies de concurrence de manière absolue. | Simule une exécution strictement séquentielle. Peut provoquer des erreurs d'échec de sérialisation (code `40001`) nécessitant un mécanisme de retry applicatif obligatoire. |

### 7.2 Verrous pessimistes vs optimistes {#section-7-2}
* **Verrouillage Optimiste (Optimistic Concurrency Control) :**  
  Chaque ligne possède une colonne `version: integer`. Lors de la mise à jour, la requête SQL vérifie que la version n'a pas changé :  
  `UPDATE accounts SET balance = 100, version = version + 1 WHERE id = 'acc_1' AND version = 5;`  
  Si aucune ligne n'est mise à jour, un tiers a modifié l'enregistrement entre-temps : l'application rejette l'opération ou recommence. Idéal pour les systèmes à fort trafic en lecture.
* **Verrouillage Pessimiste (Pessimistic Locking) :**  
  La ligne est physiquement verrouillée en écriture par le moteur SQL dès sa lecture :  
  `SELECT * FROM inventory WHERE product_id = 'prod_9' FOR UPDATE;`  
  Toute autre transaction tentant d'accéder à cette ligne est mise en attente jusqu'à la validation du commit. Indispensable pour la gestion de stocks stricts et les débits bancaires.

### 7.3 Le Pattern Expand-Contract pour les migrations sans coupure {#section-7-3}
Sur un serveur en production, exécuter une migration SQL destructive (comme renommer une colonne `ALTER TABLE users RENAME COLUMN phone TO phone_number;`) provoque une **panne immédiate de service**. Pendant le temps où l'ancienne version du code tourne encore avant le rechargement complet, toutes ses requêtes échouent.

Le standard industriel absolu pour les déploiements continus est le **Pattern Expand-Contract (Élargir-Transiter-Contracter)** en trois phases découplées :

```text
LE CYCLE ZERO-DOWNTIME DU PATTERN EXPAND-CONTRACT :

  PHASE 1 : ÉLARGISSEMENT (EXPAND)
  ├── 1. Migration SQL : Création de la nouvelle colonne "phone_e164" (NULLABLE) sans toucher à "phone"
  └── 2. Version applicative V1 en production : Continue de lire et écrire sur l'ancienne colonne "phone"
  
  PHASE 2 : TRANSITION & DOUBLE ÉCRITURE
  ├── 3. Déploiement Version applicative V2 :
  │      • Écrit SIMULTANÉMENT sur "phone" ET "phone_e164"
  │      • Lit en priorité sur "phone_e164" (avec fallback sur "phone")
  └── 4. Script de fond (Backfill) : Migre les anciennes données historiques vers "phone_e164"
  
  PHASE 3 : CONTRACTION (CONTRACT)
  ├── 5. Déploiement Version applicative V3 : Utilise EXCLUSIVEMENT "phone_e164"
  └── 6. Migration SQL finale : Suppression sécurisée de l'ancienne colonne "phone" (DROP COLUMN)
```

### 7.4 Sauvegardes continues et réplication WAL {#section-7-4}
Un dump quotidien de base de données (`pg_dump` à 2h du matin) n'est pas une stratégie de sauvegarde moderne. En cas de crash disque à 17h, 15 heures de transactions clients sont définitivement anéanties (RPO de 15h inacceptable).

L'architecture de persistance exige l'archivage continu des **Write-Ahead Logs (WAL)** vers un stockage objet distant chiffré (Cloudflare R2 / AWS S3) via des outils comme `pgBackRest` ou `WAL-G`. Cette approche permet le **Point-in-Time Recovery (PITR)** : la capacité mathématique de restaurer la base de données à la milliseconde exacte précédant un incident ou une fausse manipulation humaine.


---

## 8. Cycle Complet de Déploiement : Du Poste Local au VPS {#section-8}

### 8.1 La chaîne d'assemblage continue (Pipeline CI/CD Matrix) {#section-8-1}
Le déploiement professionnel est une chaîne d'assemblage entièrement déterministe où aucune intervention manuelle par SSH ou FTP n'est tolérée. Chaque modification traverse une succession d'usines logicielles de validation.

```text
FLUX COMPLET DE LIVRAISON CONTINUE (DE LA LIGNE DE CODE AU SERVEUR FINAL) :

  [ POSTE LOCAL DÉVELOPPEUR ]
    │
    ├── 1. Git Pre-commit Hook (Lefthook) : Linter, Formatage (Prettier/Biome), Secret Scan
    └── 2. Git Push origin feat/order-service
    
  [ SERVEUR SAAS GIT (GitHub / GitLab) ]
    │
    ├── 3. Ouverture de la Pull Request & Contrôle des Invariants
    └── 4. Déclenchement de la MATRIX CI (GitHub Actions) :
           ├── Job 1 : Analyse Statique & Typecheck strict (tsc --strict --noEmit)
           ├── Job 2 : Suite de Tests Unitaires & Propriétés (Vitest / fast-check)
           ├── Job 3 : Tests d'Intégration sur conteneur éphémère PostgreSQL
           └── Job 4 : Audit de Sécurité Dépendances (CVE Scanner / Trivy)
           
  [ SAS DE VALIDATION & MERGE ]
    │
    ├── 5. Revue Humaine du Diff & Approbation obligatoire
    ├── 6. Squash & Merge sur la branche "main"
    └── 7. Construction de l'image Docker Multi-Stage Build ultra-sécurisée
           Tagguée par le commit SHA immuable : ghcr.io/org/app:a1b2c3d
           
  [ PIPELINE DE DÉPLOIEMENT CONTINU (CD) ]
    │
    ├── 8. Notification chiffrée vers le serveur de production VPS
    └── 9. Déclenchement du runner de déploiement sécurisé
    
  [ SERVEUR DE PRODUCTION VPS (Linux Ubuntu LTS) ]
    │
    ├── 10. Pull de la nouvelle image Docker validée
    ├── 11. Exécution des migrations SQL (Phase Expand)
    ├── 12. Démarrage du nouveau conteneur en parallèle (Instance Green)
    ├── 13. Validation du Healthcheck HTTP interne (/healthz renvoie 200 OK)
    ├── 14. Bascule dynamique du Reverse Proxy Caddy (Zero-Downtime Reload)
    └── 15. Arrêt propre (Graceful Shutdown avec drain des connexions) de l'ancien conteneur
```

### 8.2 Topologie moderne d'un VPS autohébergé {#section-8-2}
* **Système d'Exploitation :** Linux Ubuntu LTS ou Debian Stable, durci au niveau du noyau (Hardened Kernel, `sysctl` optimisé pour la gestion réseau).
* **Pare-feu Réseau Hôte (UFW / Iptables) :** Tous les ports d'entrée sont fermés par défaut. Seuls les ports `80` (HTTP), `443` (HTTPS) et le port d'administration SSH customisé (avec authentification exclusive par clé Ed25519) sont autorisés.
* **Passerelle Web & Reverse Proxy Edge (Caddy Server) :** Reçoit l'intégralité du trafic public, négocie le chiffrement TLS avec Let's Encrypt / ZeroSSL, compresse les flux (Zstandard / Brotli) et applique une limitation de débit par IP (Rate Limiting).
* **Réseau Virtuel Interne Isolé (Docker Bridge Network) :** PostgreSQL, Redis et les conteneurs applicatifs communiquent sur un réseau virtuel privé (`172.20.0.0/16`) totalement invisible depuis l'Internet public. Aucun port de base de données (`5432` ou `6379`) n'est exposé sur l'IP du VPS.

### 8.3 Configuration du Reverse Proxy Edge avec Caddy {#section-8-3}
Contrairement aux anciens serveurs web nécessitant des centaines de lignes de configuration complexe et des cron jobs manuels pour renouveler les certificats SSL, **Caddy Server** intègre nativement la gestion du protocole ACME en mémoire.

```caddyfile
app.mondomaine.com {
    # 1. En-têtes de sécurité stricts (HSTS, Anti-Clickjacking, XSS Protection)
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "DENY"
        Referrer-Policy "strict-origin-when-cross-origin"
    }

    # 2. Compression dynamique ultra-rapide
    encode zstd gzip

    # 3. Routage inverse vers le conteneur applicatif interne isolé
    reverse_proxy web-service:3000 {
        health_uri /healthz
        health_interval 5s
        health_timeout 2s
        health_status 200
    }
}
```

### 8.4 Gestion des Secrets POSIX et Isolation des Variables {#section-8-4}
Une règle d'or inviolable de l'ingénierie logicielle stipule : **Aucun secret, mot de passe, clé d'API ou token ne doit jamais être commité dans un dépôt Git**, même privé.

Les secrets de production sont gérés exclusivement sur le serveur hôte via des fichiers d'environnement protégés par le système de permissions POSIX :
```bash
# Sur le serveur de production VPS :
chown root:docker-runner /etc/app/.env.production
chmod 600 /etc/app/.env.production

# Injection déclarative au démarrage du conteneur dans docker-compose.yml :
# env_file:
#   - /etc/app/.env.production
```


---

## 9. La Méthode KISS Intégrale : De l'Idée au Déploiement {#section-9}

### 9.1 Le minimalisme radical contre la complexité accidentelle {#section-9-1}
La loi de Gall stipule : *"Un système complexe qui fonctionne est invariablement le résultat de l'évolution d'un système simple qui fonctionnait."*

La plus grande menace lors de l'orchestration d'agents IA est la **complexité accidentelle**. Les LLM ont une propension naturelle à sur-ingénierer les solutions : ils proposent des microservices prématurés, des bibliothèques tierces obsolètes, des patrons de conception alambiqués et des couches d'abstractions inutiles.

L'architecte applique le principe **KISS (Keep It Simple, Stupid)** comme une arme de salubrité technique : chaque ligne de code, chaque abstraction et chaque dépendance doit prouver son utilité vitale sous peine de rejet immédiat.

### 9.2 Le Workflow Universel en 6 Phases Séquentielles {#section-9-2}

```text
LE WORKFLOW UNIVERSEL EN 6 PHASES SÉQUENTIELLES :

  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 1 : SPÉCIFICATION & PÉRIMÈTRE FORMEL (L'HUMAIN SEUL)             │
  │ • Rédaction de SPEC.md : Problème métier, Scope strict, Invariants.      │
  │ • Exclusion formelle de tout détail d'implémentation prématuré.         │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 2 : CONTRATS DE DONNÉES & SCHÉMAS (HUMAIN AUDITE & FIGE)          │
  │ • Génération des schémas d'échanges (TypeBox, Zod, OpenAPI).            │
  │ • Verrouillage des fichiers de contrats : Socle immuable.               │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 3 : TDD INVERSÉ & SUITE DE PREUVES (AGENT ÉCRIT, HUMAIN VALIDE)   │
  │ • Création du Git Worktree isolé : git worktree add ../task-test        │
  │ • L'agent génère exclusivement les tests unitaires et de propriétés.    │
  │ • L'humain relit et fige les tests en lecture seule.                    │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 4 : IMPLÉMENTATION DANS LE HARNAIS (AGENT CODE EN BOUCLE FERMÉE)  │
  │ • L'agent produit le code métier pur jusqu'au passage au vert (Exit 0). │
  │ • Validation déterministe automatique : Linter > Typecheck > Tests.     │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 5 : INTÉGRATION PÉRIPHÉRIQUE & REVUE DU DIFF (L'HUMAIN DÉCIDE)    │
  │ • Raccordement des adaptateurs (Fastify, PostgreSQL, React).            │
  │ • Inspection chirurgicale de la Pull Request via la vue Unified Diff.   │
  │ • Rebase interactif, Squash atomique et Merge sur la branche main.      │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ PHASE 6 : DÉPLOIEMENT CONTINU DÉTERMINISTE (AUTOMATISATION TOTALE)       │
  │ • Matrix CI distante > Build Docker multi-étapes immuable.              │
  │ • Migration SQL Expand-Contract > Bascule dynamique Reverse Proxy.      │
  └─────────────────────────────────────────────────────────────────────────┘
```

### 9.3 Détail Opérationnel des 6 Phases {#section-9-3}

#### Phase 1 — Spécification & Frontières Formelles
L'erreur initiale classique consiste à ouvrir un outil d'IA et à prompter au hasard. La Phase 1 s'effectue sans IA. L'architecte rédige un fichier `SPEC.md` à la racine du projet, structuré selon le canevas suivant :
* **Intention Fondamentale :** Quel est le problème réel résolu pour l'utilisateur final ?
* **Périmètre Inclus (In-Scope) :** Les 3 seules fonctionnalités livrées dans cette itération.
* **Périmètre Exclu (Out-of-Scope) :** La liste formelle de tout ce qui est explicitement interdit d'implémenter pour le moment (ex: pas d'authentification multi-rôles, pas d'envoi d'emails, pas de système de thèmes).
* **Invariants de Sécurité & Métier :** Les règles absolues qui ne doivent jamais être enfreintes (ex: *"Le total TTC doit toujours égaler la somme exacte des lignes HT plus la TVA calculée ligne par ligne sans arrondi prématuré"*).

#### Phase 2 — Contrats de Données & Schémas
L'architecte transmet `SPEC.md` à l'agent avec une consigne stricte : *"Génère exclusivement les schémas de données TypeBox/Zod décrivant les entrées, sorties et erreurs de ce cas d'usage. N'écris aucun code fonctionnel."*

L'architecte inspecte les types produits. Si les structures sont limpides, les fichiers sont enregistrés dans `core/contracts/` et verrouillés.

#### Phase 3 — TDD Inversé & Sas de Tests
L'architecte ouvre un **Git Worktree isolé** :
```bash
git worktree add ../task-tests -b task/order-logic-tests
cd ../task-tests
```
L'agent est instruit : *"À partir des contrats dans `core/contracts/` et des règles de `SPEC.md`, écris la suite complète de tests unitaires dans `core/domain/order.test.ts`. Couvre le chemin nominal et tous les cas d'angles (quantité zéro, valeurs négatives, débordements). N'écris pas le fichier d'implémentation."*

L'architecte relit le fichier de test. Une fois satisfait, il protège le fichier en lecture seule.

#### Phase 4 — Implémentation sous Contrainte Mécanique
L'agent reçoit l'ordre d'écrire `core/domain/order.ts`. Le harnais de validation tourne en boucle fermée :
```bash
# Commande unique exécutée par le harnais :
npx tsc --noEmit && npx vitest run core/domain/order.test.ts
```
Tant que cette commande échoue, le harnais réinjecte la trace d'erreur à l'agent. Dès que la commande renvoie `0`, la phase d'implémentation est déclarée terminée.

#### Phase 5 — Intégration Périphérique & Revue du Diff
L'agent raccorde le domaine aux adaptateurs secondaires (base SQL, contrôleurs d'API). Une Pull Request est créée.

L'architecte ouvre la vue **Unified Diff** de la PR. C'est son poste de commandement. Il applique la grille d'audit suivante :
1. Y a-t-il des fichiers modifiés en dehors du scope prévu ? (Si oui : rejet).
2. L'agent a-t-il introduit de nouvelles dépendances dans `package.json` sans autorisation préalable ? (Si oui : suppression).
3. Le code de domaine est-il resté exempt de tout import réseau ou SQL ? (Si oui : validation).

L'architecte exécute un rebase interactif, fusionne la PR sur `main` et détruit le worktree temporaire.

#### Phase 6 — Pipeline CI/CD & Livraison VPS
La fusion sur `main` déclenche l'automatisation totale : la CI distante rejoue tous les tests sur une machine vierge, construit l'image Docker multi-étapes immuable et la déploie sur le VPS avec rechargement sans interruption de service (Zero-Downtime Reload).

### 9.4 La Boîte à Outils Minimale de l'Orchestrateur {#section-9-4}

| Catégorie Logique | Outil Recommandé | Rôle Systémique & Justification |
| :--- | :--- | :--- |
| **Éditeur & Moteur Agentique** | VS Code / Claude Code / Aider | Environnement d'orchestration pilotant l'agent par modifications atomiques (Unified Diffs) et commandes shell contrôlées. |
| **Isolation Locale** | Git Worktrees | Permet d'exécuter plusieurs agents en arrière-plan sur des répertoires distincts sans collision avec le code de l'opérateur. |
| **Contrôle Statique & AST** | TypeScript (Strict) / Biome / ESLint | Démonstrateur automatique de théorèmes logiques bloquant immédiatement toute hallucination de propriétés ou de types. |
| **Harnais de Vérification** | Vitest / fast-check / Stryker | Suite déterministe combinant tests unitaires instantanés, tests basés sur les propriétés et élimination des faux positifs par mutation. |
| **Conteneurisation & Runtime** | Docker & Docker Compose | Standardisation absolue de l'environnement d'exécution garantissant l'identité stricte entre le poste local, la CI et la production. |
| **Passerelle Web & Edge** | Caddy Server | Reverse proxy moderne avec gestion automatique des certificats SSL ACME en mémoire, terminaison TLS et rate limiting. |

### 9.5 Les 4 Compétences Souveraines du Décideur Non-Codeur {#section-9-5}
Pour piloter efficacement une flotte d'agents de code sans taper chaque instruction au clavier, le décideur moderne doit cultiver quatre compétences fondamentales :
1. **La Pensée Modulaire (Abstraction & Découpage) :** La capacité d'analyser un problème complexe et de le fractionner en sous-systèmes autonomes dotés d'interfaces minuscules (modules profonds).
2. **La Rigueur Contractuelle (Schema-First) :** L'exigence de modéliser les formats de données et les règles invariantes avant toute tentative d'écriture algorithmique.
3. **L'Acuité Visuelle du Diff Git :** La compétence de relire un patch unifié ligne par ligne pour repérer immédiatement les dérives, les fuites de responsabilités ou le code mort.
4. **Le Refus Inconditionnel de l'Approximation :** L'intransigeance absolue face au code non prouvé : tout composant non accompagné de sa suite de tests déterministes et de son typage strict est considéré comme défaillant par défaut.


---

## 10. Bibliothèque Opérationnelle de Prompts Déterministes & Protocoles d'Exécution {#section-10}

### 10.1 Philosophie d'Ingénierie des Prompts pour Harnais Agentique {#section-10-1}
Un prompt destiné à un agent de code ne doit jamais ressembler à une conversation informelle. Il doit être rédigé comme un **ordre de mission militaire ou une spécification aéronautique** : délimitation stricte du périmètre, interdiction formelle d'effets de bord, format de sortie imposé et critères d'arrêt vérifiables.

Chaque prompt ci-dessous est conçu selon le principe de la **moindre surprise** et force l'agent à opérer dans le respect absolu des modules profonds, du typage strict et de l'architecture hexagonale.

### 10.2 Prompts Prêts à l'Emploi pour les 6 Phases de la Méthode KISS {#section-10-2}

#### Prompt Phase 1 — Cadrage & Génération du Document d'Intention (SPEC.md)
*Contexte d'utilisation : À soumettre au tout début, lorsque vous avez une idée brute et souhaitez la convertir en spécification formelle sans écrire une seule ligne de code.*

```markdown
Tu agis en tant qu'Architecte Logiciel Principal et Spécialiste des Systèmes Déterministes.
Je souhaite concevoir la fonctionnalité suivante : [DÉCRIRE L'IDÉE / LE BESOIN MÉTIER].

Ta mission unique est de rédiger le fichier formel "SPEC.md" à la racine du projet.
Tu ne dois écrire AUCUNE ligne de code d'implémentation (pas de TypeScript, pas de SQL, pas de HTML).

Structure obligatoire de ton document "SPEC.md" :
1. INTENTION & OBJECTIF MÉTIER : Problème résolu et valeur pour l'utilisateur.
2. PÉRIMÈTRE STRICT (IN-SCOPE) : Les 3 sous-fonctionnalités indispensables maximum.
3. EXCLUSIONS FORMELLES (OUT-OF-SCOPE) : Liste explicite de ce qui est STRICTEMENT INTERDIT
   d'implémenter dans cette itération (pas d'auth complexe, pas d'emails, pas d'optimisation prématurée).
4. INVARIANTS SYSTÉMIQUES & CAS LIMITES :
   - Formats et unités des données (ex: prix toujours en centimes entiers, pas de float).
   - Comportement exact face aux valeurs nulles, négatives ou collections vides.
   - Règles d'erreurs métier typées attendues.
5. CONTRAT DE PORTS (HEXAGONAL) : Liste des données entrant dans le domaine et des dépendances
   sortantes requises (Storage, DB, Queue), formulées sous forme conceptuelle pure.

Adopte un ton direct, exhaustif, mathématiquement rigoureux et sans ambiguïté.
```

#### Prompt Phase 2 — Génération des Contrats de Données (Schema-First)
*Contexte d'utilisation : Une fois le fichier SPEC.md validé. Force l'agent à créer les types et schémas immuables dans `core/contracts/`.*

```markdown
Tu agis en tant qu'Architecte de Contrats et Spécialiste du Typage Invariant.
Prends connaissance du fichier "SPEC.md" ci-joint.

Ta mission est de créer EXCLUSIVEMENT le fichier "core/contracts/[nom_domaine].schema.ts".
Règles absolues d'exécution :
1. Utilise la bibliothèque TypeBox (ou Zod) pour définir les schémas d'entrée, de sortie et d'erreurs.
2. Dérive automatiquement les types statiques TypeScript via Static<typeof Schema>.
3. Applique des contraintes d'intégrité maximales sur chaque champ :
   - Chaînes : regex pattern, minLength, maxLength, format (uuid, email, date-time).
   - Nombres : minimum, maximum, type entier (Integer).
   - Tableaux : minItems, maxItems.
4. Définis l'enum ou l'union des erreurs métier possibles (ex: DomainErrorSchema).
5. N'IMPLÉMENTE AUCUNE LOGIQUE FONCTIONNELLE. AUCUN CODE MÉTIER.
6. Ne crée aucun adaptateur (pas de Fastify, pas de SQL).

Fournis uniquement le code complet du fichier de schéma avec ses exports propres.
```

#### Prompt Phase 3 — TDD Inversé : Génération Exclusive des Tests Unitaires
*Contexte d'utilisation : Dans un Git Worktree dédié (`git worktree add ../task-test -b task/tests`). Les tests sont générés et verrouillés avant le code.*

```markdown
Tu agis en tant qu'Ingénieur QA & Vérification Formelle.
Consulte "SPEC.md" et le fichier de contrat "core/contracts/[nom_domaine].schema.ts".

Ta mission est d'écrire EXCLUSIVEMENT le fichier de tests unitaires "core/domain/[nom_domaine].test.ts".
Règles absolues :
1. Utilise Vitest (ou Jest).
2. Interdiction formelle de créer ou modifier le fichier d'implémentation "core/domain/[nom_domaine].ts".
3. Couvre rigoureusement l'ensemble des scénarios décrits dans SPEC.md :
   - Chemin nominal (Happy path).
   - Tous les cas limites (quantités nulles, montants négatifs, dépassements de quotas, chaînes vides).
   - Vérification que les bonnes erreurs typées sont levées avec les bons codes.
4. Rédige au moins un test basé sur les propriétés (Property-Based Testing avec fast-check)
   prouvant l'invariance mathématique des calculs.
5. Fais des assertions strictes et explicites (interdiction d'assertions creuses comme expect(true).toBe(true)).

Fournis uniquement le code complet du fichier de test.
```

#### Prompt Phase 4 — Implémentation du Domaine Métier sous Contrainte Mécanique
*Contexte d'utilisation : Après validation humaine des tests. L'agent doit faire passer les tests au vert sans modifier les tests.*

```markdown
Tu agis en tant qu'Ingénieur d'Implémentation Core Domain.
Tu as à ta disposition :
- Le cahier des charges : "SPEC.md"
- Les schémas formels : "core/contracts/[nom_domaine].schema.ts"
- La suite de tests unitaires (VERROUILLÉE EN LECTURE SEULE) : "core/domain/[nom_domaine].test.ts"

Ta mission est de créer le fichier "core/domain/[nom_domaine].ts" pour faire passer 100% des tests au vert.
Contraintes strictes du Domaine Métier :
1. INTERDICTION FORMELLE DE MODIFIER LE FICHIER DE TEST.
2. ZÉRO dépendance externe (pas d'Express, pas de Fastify, pas de SQL, pas de fetch réseau).
   C'est du TypeScript pur.
3. Conçois un MODULE PROFOND : une interface minuscule (1 à 3 fonctions pures exportées),
   masquant toute la complexité algorithmique interne.
4. Respecte le principe d'immutabilité : aucune mutation directe des objets passés en arguments.
5. Si une dépendance externe est nécessaire (stockage, persistance), définis un Port TypeScript
   (interface abstraite) que le domaine recevra par injection de dépendance (Object Seam).

Exécute la commande de validation : "npx vitest run core/domain/[nom_domaine].test.ts".
Fournis le code complet du fichier jusqu'à l'obtention du code de retour 0.
```

#### Prompt Phase 5 — Raccordement des Adaptateurs & Création de la Pull Request
*Contexte d'utilisation : Branchement sur l'infrastructure (API Fastify, Drizzle SQL, Redis) et préparation de la revue du Diff.*

```markdown
Tu agis en tant qu'Ingénieur Système & Adaptateurs d'Infrastructure.
Le domaine métier "core/domain/[nom_domaine].ts" est validé et testé.

Ta mission est de créer les adaptateurs secondaires et primaires :
1. "infra/db/[nom_domaine].repository.ts" : Implémente le port de persistance avec Drizzle/PostgreSQL.
2. "infra/http/[nom_domaine].controller.ts" : Expose la route HTTP Fastify en validant le payload
   entrant avec le schéma Zod/TypeBox (Parse, Don't Validate).
3. Rédige un test d'intégration "infra/http/[nom_domaine].integration.test.ts" simulant une requête HTTP
   complète sur une base de données de test éphémère.

Règles de propreté Git & Pull Request :
- Ne touche à aucun fichier existant hors de la fonctionnalité.
- Prépare un message de commit atomique respectant la convention Conventional Commits :
  "feat([domaine]): implement [nom_fonctionnalité] endpoints and repository adapter"
- Résume dans ta réponse le "Diff" exact des fichiers créés pour inspection humaine.
```

#### Prompt Phase 6 — Déploiement Zero-Downtime & Configuration Caddy / Docker
*Contexte d'utilisation : Configuration du conteneur et du reverse proxy pour la mise en production sur le VPS.*

```markdown
Tu agis en tant qu'Ingénieur DevOps & Site Reliability Engineer (SRE).
Nous préparons la livraison de l'application sur le serveur VPS de production.

Génère la configuration complète et sécurisée pour :
1. DOCKERFILE MULTI-STAGE BUILD :
   - Stage 1 (Builder) : Compilation TypeScript, exclusion des devDependencies.
   - Stage 2 (Runner) : Image Alpine/Distroless ultra-légère, utilisateur non-root (UID 10001),
     zéro outil de compilation, healthcheck interne configuré sur /healthz.
2. DOCKER-COMPOSE.PROD.YML :
   - Isolation du conteneur sur un réseau de pont virtuel privé (internal-bridge).
   - Limitation stricte des ressources CPU et Mémoire (deploy.resources.limits).
   - Injection sécurisée des variables d'environnement via env_file: /etc/app/.env.production.
3. CADDYFILE :
   - Configuration du reverse-proxy avec gestion TLS automatique (Let's Encrypt).
   - En-têtes de sécurité stricts (HSTS, X-Frame-Options DENY, nosniff).
   - Politiques de compression Zstandard/Gzip et rate-limiting au niveau IP.

Fournis les configurations brutes prêtes à être déployées sur Ubuntu LTS.
```

### 10.3 Prompts Spécialisés pour la Maintenance & Résolution de Crise {#section-10-3}

#### Prompt A — Refactoring Sûr par Point de Couture (Seam Insertion)
```markdown
Tu agis en tant qu'Expert en Dette Technique & Refactoring (Méthode Michael Feathers).
Voici un fichier legacy monolithique : [CHEMIN_DU_FICHIER].

Notre objectif est d'extraire la fonctionnalité [NOM_FONCTIONNALITÉ] SANS CASSER L'EXISTANT.
Procédure obligatoire :
1. Identifie le "Point de Couture" (Seam) le plus approprié (Object Seam via injection d'interface).
2. Rédige d'abord des "Characterization Tests" (tests de caractérisation) qui figent le comportement
   actuel du composant, y compris ses bizarreries historiques.
3. Extrais la logique dans un module profond indépendant doté d'une interface pure.
4. Raccorde le code legacy à la nouvelle interface sans modifier son comportement externe.
5. Fournis un Unified Diff chirurgical.
```

#### Prompt B — Traque de Régression Automatisée (Git Bisect Harness)
```markdown
Un bug a été signalé en production : [DESCRIPTION_EXACTE_DU_BUG].
Le commit actuel [HASH_ACTUEL] est défaillant. La version stable était [TAG_STABLE].

Ta mission :
1. Rédige un script de test de non-régression unitaire ultra-court "test/repro-bug.test.ts"
   qui échoue actuellement (Exit code 1) et réussissait sur la version stable.
2. Fournis la commande exacte pour lancer "git bisect run npm test -- test/repro-bug.test.ts".
3. Une fois le commit fautif localisé, analyse le Diff de ce commit spécifique et propose
   un patch correctif minimal (moins de 10 lignes) respectant les invariants du domaine.
```

#### Prompt C — Migration SQL Zero-Downtime (Pattern Expand-Contract)
```markdown
Nous devons modifier la structure de la table [NOM_TABLE] en production :
Ancienne structure : [COLONNE_ACTUELLE]
Nouvelle structure souhaitée : [NOUVELLE_COLONNE]

Rédige les 3 scripts de migration distincts selon le pattern Expand-Contract :
1. "migration_01_expand.sql" : Ajout de la nouvelle colonne en mode NULLABLE ou avec valeur par défaut,
   sans verrou bloquant (ex: CREATE INDEX CONCURRENTLY si index nécessaire).
2. "migration_02_backfill.sql" : Script de recopie par lots (Batch processing de 1000 lignes) pour
   migrer l'historique sans saturer le WAL ni verrouiller la table en écriture.
3. "migration_03_contract.sql" : Suppression sécurisée de l'ancienne colonne après bascule applicative V3.
```

### 10.4 Grille d'Évaluation Décisionnelle de l'Architecte (Checklist PR) {#section-10-4}

| Statut | Point de Contrôle Invariant | Critère de Rejet Immédiat (Dealbreaker) |
| :---: | :--- | :--- |
| `[ ]` | **Confinement du Périmètre** | La PR modifie plus de 3 fichiers ou contient plus de 150 lignes modifiées hors fichiers de lock. |
| `[ ]` | **Pureté du Domaine** | Le répertoire `core/domain/` contient des imports de bibliothèques tierces, de pilotes SQL ou de framework web. |
| `[ ]` | **Intégrité des Tests** | L'agent a modifié un fichier de test unitaire existant sans autorisation formelle de l'architecte. |
| `[ ]` | **Absence de Dépendances Cachées** | Des packages ont été ajoutés à `package.json` sans justification architecturale indispensable. |
| `[ ]` | **Étanchéité des Secrets** | Présence de chaînes en clair ressemblant à des clés d'API, tokens ou mots de passe (détecté par `gitleaks`). |
| `[ ]` | **Linéarité de l'Historique** | Présence de micro-commits désordonnés (*"fix typo", "retry"*) non squashés avant intégration sur `main`. |


---

## 11. Ingénierie de Production Avancée, Observabilité & Résilience Systémique {#section-11}

### 11.1 L'Observabilité Active : Télémétrie, Logs Structurés & Tracing Distribué {#section-11-1}
Le déploiement sans coupure n'est pas le point final du cycle de vie logiciel : c'est le point de départ de son exploitation sous charge réelle. Dans un système en production, l'absence de crash visible ne prouve pas le bon fonctionnement du programme. Des pannes silencieuses (dégradation progressive de la latence, fuites de mémoire lentes, épuisement discret de pools de connexions) peuvent paralyser une application sans lever d'exceptions fatales.

L'observabilité moderne ne repose pas sur de simples messages textuels verbeux disséminés au hasard (`console.log("here")`), mais sur les trois piliers formels de la télémétrie unifiée :

```text
LES TROIS PILIERS DE L'OBSERVABILITÉ INDUSTRIELLE :

  ┌─────────────────────────┐   ┌─────────────────────────┐   ┌─────────────────────────┐
  │  1. LOGS STRUCTURÉS     │   │  2. MÉTRIQUES RED       │   │  3. TRACING DISTRIBUÉ   │
  │     (JSON Contextualisé)│   │     (Rate, Errors, Dur.)│   │     (OpenTelemetry / W3C│
  ├─────────────────────────┤   ├─────────────────────────┤   ├─────────────────────────┤
  │ Événements discrets et  │   │ Valeurs agrégées        │   │ Propagation d'un ID de  │
  │ enrichis (Timestamp,    │   │ numériques scalaires    │   │ corrélation (trace_id)  │
  │ LogLevel, trace_id,     │   │ temporelles (Compteurs, │   │ à travers les frontières│
  │ userId, duration_ms).   │   │ Histogrammes, Gauges).  │   │ réseau et files Redis.  │
  └─────────────────────────┘   └─────────────────────────┘   └─────────────────────────┘
```

#### Standardisation du Log Structuré en JSON :
Chaque composant doit émettre des journaux sous forme d'objets JSON stricts sur la sortie standard (stdout), capturés par le moteur de conteneurs Docker et indexés par un collecteur (Grafana Loki, Vector, FluentBit) :

```json
{
  "timestamp": "2026-08-31T10:45:12.104Z",
  "level": "warn",
  "service": "order-service",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "request_id": "req_01J6G7K9Q2",
  "event": "PAYMENT_GATEWAY_SLOW_RESPONSE",
  "latency_ms": 1420,
  "gateway": "stripe",
  "customer_id": "usr_99a8b7",
  "msg": "Payment verification took longer than standard threshold (1000ms)"
}
```

### 11.2 Résilience Distribuée : Circuit Breakers, Backoff Exponentiel & Jitter {#section-11-2}
Dans une architecture distribuée, les dépendances externes (passerelles de paiement, APIs tierces, services de rendu) connaissent inévitablement des pannes partielles, des ralentissements et des micro-coupures réseau. Un logiciel mal architecturé tente alors de réexécuter en boucle les requêtes en échec, provoquant deux catastrophes majeures :
1. **L'Effet Thundering Herd (Troupeau Affolé) :** Des milliers de clients réessayent exactement au même intervalle fixe (ex: toutes les 1 000 ms), submergeant le service tiers dès son redémarrage.
2. **L'Épuisement des Ressources Locales (Cascading Failure) :** Les threads et sockets réseau locaux restent bloqués en attente de réponse (timeout), saturant la mémoire du serveur et paralysant les fonctionnalités non liées.

> **Modèle d'État du Disjoncteur (Circuit Breaker Pattern) :**  
> Le disjoncteur intercepte tous les appels vers une ressource distante instable et régule le flux selon une machine à trois états finis :
> * **FERMÉ (Closed - Nominal) :** Toutes les requêtes traversent normalement. Le disjoncteur calcule le taux d'échec sur une fenêtre glissante (ex: 50 dernières requêtes).
> * **OUVERT (Open - Protection Active) :** Si le taux d'échec dépasse 50%, le disjoncteur bascule en état OUVERT. Tout appel ultérieur est immédiatement rejeté localement (Fast-Fail en 0.1ms) sans toucher au réseau. Une réponse dégradée (Fallback) est retournée au client.
> * **SEMI-OUVERT (Half-Open - Sondage) :** Après un délai de refroidissement (ex: 30s), le disjoncteur laisse passer une unique requête test. Si elle réussit, le circuit se referme ; si elle échoue, le délai de protection est réinitialisé.

```text
MACHINE D'ÉTATS FINIS DU CIRCUIT BREAKER :

           ┌──────────────────────────────────────────────┐
           │                                              │
           ▼                                              │ (Succès du test)
   ┌───────────────┐      Taux d'échec > 50%      ┌───────────────┐
   │    FERMÉ      │ ───────────────────────────> │    OUVERT     │
   │  (Nominal)    │                              │ (Protection)  │
   └───────────────┘                              └───────┬───────┘
           ▲                                              │
           │                                              │ (Délai de cooldown expiré)
           │              (Échec du test)                 ▼
           │       ┌────────────────────────────── ┌───────────────┐
           └───────┤                              │  SEMI-OUVERT  │
                   └───────────────────────────── │   (Sondage)   │
                                                  └───────────────┘
```

#### Algorithme de Retries avec Backoff Exponentiel & Jitter Décorrélé :
Pour chaque réessai réseau, le temps d'attente $T$ doit être calculé de manière exponentielle avec ajout d'une composante aléatoire (Jitter) pour étaler la charge sur l'axe temporel :
$$T_{attente} = \min\left(T_{max}, \; T_{base} 	imes 2^{tentative} + 	ext{random}(0, 	ext{Jitter})
ight)$$

### 11.3 Gestion des Échecs Asynchrones : Dead Letter Queues (DLQ) & Poison Pills {#section-11-3}
Lors du traitement de tâches en arrière-plan par des files de messages (Redis BullMQ / RabbitMQ), un message malformé (payload corrompu, bug de parsing) ou une ressource inaccessible peut faire échouer le worker à chaque exécution. Ce type de message est appelé une **Poison Pill (Pilule Empoisonnée)**.

Sans mécanisme de quarantaine, la tâche est replacée en début de file indéfiniment, saturant les workers et bloquant le traitement de toutes les commandes valides suivantes.

```text
GESTION DU CYCLE DE VIE DES MESSAGES AVEC DEAD LETTER QUEUE (DLQ) :

  [ File Principale : pdf-generation ]
                │
                ├── Worker tente le traitement (Tentative 1/3) ──> [ Échec ]
                ├── Worker retente avec Backoff (Tentative 2/3) ──> [ Échec ]
                └── Worker retente (Tentative 3/3) ──────────────> [ Échec Définitif ]
                                                                          │
                                                                          ▼
  [ Quarantaine Immédiate : Dead Letter Queue (DLQ) ] <───────────────────┘
    • Le message fautif est extrait de la file de production.
    • La pile d'erreur exacte et le contexte d'exécution sont attachés au payload.
    • Une alerte d'astreinte est émise.
    • La file principale continue de dépiler les messages sains sans latence.
    • Après correction du bug, l'opérateur exécute un script de rejeu (Re-drive DLQ).
```

### 11.4 Performance & Optimisation des Données : Indexation & Connection Pooling {#section-11-4}

#### 1. Anatomie de l'Indexation SQL Avancée :
Une application ne doit jamais exécuter de parcours séquentiel intégral (`Seq Scan`) sur une table de plus de 10 000 lignes. L'architecte supervise la création d'index spécialisés :
* **Index B-Tree Composites :** Pour les requêtes combinant filtres et tris. L'ordre des colonnes dans l'index doit respecter la règle d'or : *Égalité d'abord, Inégalité ensuite, Tri en dernier* (`CREATE INDEX idx_orders_cust_date ON orders (customer_id, created_at DESC);`).
* **Index Partiels (Partial Indexes) :** N'indexent qu'une fraction de la table correspondant à un prédicat fréquent, réduisant la taille mémoire de l'index de 90% (`CREATE INDEX idx_orders_pending ON orders (created_at) WHERE status = 'PENDING';`).
* **Index GIN (Generalized Inverted Index) :** Indispensables pour les recherches textuelles et les colonnes de données semi-structurées JSONB.

#### 2. Gouvernance du Connection Pooling (PgBouncer) :
Chaque connexion directe à un moteur PostgreSQL alloue un processus serveur dédié consommant entre 5 et 10 Mo de RAM. Si 50 workers démarrent en parallèle avec un pool local de 10 connexions chacun, le serveur subit 500 connexions concurrentes, provoquant un écroulement par contention mémoire et context-switching.

La règle architecturale impose l'interposition d'un gestionnaire de pool centralisé (**PgBouncer** en mode `Transaction Pooling`) maintenant un pool fixe de 20 à 30 connexions réelles vers PostgreSQL tout en accueillant des milliers de clients applicatifs éphémères.

### 11.5 Le Protocole de Mémoire Contextuelle Long-Terme (Agent Memory Bank) {#section-11-5}
Lorsqu'un projet s'étend sur plusieurs semaines, la mémoire de travail de l'agent IA est réinitialisée à chaque nouvelle session de développement. En l'absence d'une structure de persistance cognitive, l'agent perd la trace des choix d'architecture historiques, réintroduit des patterns obsolètes et entre en contradiction avec le code existant.

L'architecture de gouvernance impose la mise en place d'un **Memory Bank formel** stocké dans un répertoire `.context/` à la racine du dépôt Git, composé de 5 fichiers de référence obligatoires :

| Fichier de Mémoire | Rôle & Contenu Sémantique | Protocole de Lecture / Écriture |
| :--- | :--- | :--- |
| `projectbrief.md` | Vision macroscopique, proposition de valeur fondamentale et contraintes non négociables. | Rédigé par l'humain au lancement. Immuable (lecture seule pour l'agent). |
| `systemPatterns.md` | Catalogue des patrons d'architecture adoptés (Hexagonale, TypeBox, Caddy, BullMQ) et conventions de code. | Lu par l'agent au début de chaque session pour calibrer ses générations. Enrichi lors de choix structurants. |
| `techContext.md` | Versions exactes des runtimes (Node 22 LTS, PostgreSQL 16), contraintes du VPS hôte et variables d'environnement requises. | Mis à jour lors des montées de version d'infrastructure ou de dépendances. |
| `activeContext.md` | Journal de bord de la tâche en cours : objectif immédiat, décisions récentes, bloqueurs et prochaines étapes. | Mis à jour obligatoirement par l'agent à la fin de chaque tâche validée. |
| `progress.md` | Tableau récapitulatif des fonctionnalités terminées, des tests validés et de la dette technique restante. | Source de vérité pour l'arbitrage des priorités de développement. |

### 11.6 Le Plan de Reprise d'Activité (PRA / Disaster Recovery) {#section-11-6}
En ingénierie de production, un axiome fondamental régit la sécurité des données : *« Une sauvegarde non testée n'existe pas. »*

L'architecture de résilience doit permettre de reconstruire un environnement de production complet à partir de zéro (Bare Metal Restoration) en moins de 15 minutes sur un nouveau VPS en cas de sinistre majeur sur le datacenter d'origine :

```text
SÉQUENCE DU PLAN DE REPRISE D'ACTIVITÉ EN 4 PHASES :

  PHASE 1 : PROVISIONNEMENT RAPIDE DE LA NOUVELLE MACHINE (0-3 min)
  ├── 1. Création d'un VPS vierge Ubuntu LTS chez n'importe quel fournisseur cloud.
  └── 2. Exécution du script déclaratif de configuration (cloud-init / Ansible minimal) :
         Installation de Docker, Docker Compose, Git, UFW, durcissement SSH.
  
  PHASE 2 : RESTAURATION DE LA PERSISTANCE & DES SECRETS (3-8 min)
  ├── 3. Rapatriement chiffré des secrets (.env.production) depuis le gestionnaire sécurisé.
  └── 4. Restauration PITR de PostgreSQL à partir des archives WAL stockées sur Cloudflare R2 / S3.
  
  PHASE 3 : DÉPLOIEMENT DES CONTENEURS IMMUABLES (8-12 min)
  ├── 5. Clone du dépôt Git sur la branche stable "main".
  └── 6. Docker Compose Pull & Up : Téléchargement des images conteneurisées depuis le Registry privé.
  
  PHASE 4 : BASCULE DNS & CERTIFICATS TLS AUTOMATIQUES (12-15 min)
  ├── 7. Mise à jour de l'enregistrement DNS A vers la nouvelle adresse IP du VPS.
  └── 8. Caddy négocie instantanément les nouveaux certificats SSL Let's Encrypt. Service rétabli.
```


---

## 12. Écosystème Technologique Agnostique, Modèles Libres & Open Source (Septembre 2026) {#section-12}

### 12.1 Souveraineté & Paradigme Agnostique : L'Interface Standardisée {#section-12-1}
La plus grande menace pour une organisation pilotant des flottes d'agents est l'enfermement propriétaire (*Vendor Lock-in*). Lier l'architecture de ses harnais à l'API fermée d'un seul fournisseur expose l'entreprise à des ruptures de service, des dérives tarifaires et des risques critiques de confidentialité sur la propriété intellectuelle du code source.

L'ingénierie moderne impose une **couche d'abstraction agnostique universelle** : tout le harnais communique exclusivement via des protocoles ouverts et des interfaces standardisées (norme OpenAI-compatible API, standard JSON-RPC et protocole MCP). L'architecte peut ainsi interchanger instantanément le modèle sous-jacent (LLM cloud propriétaire ou modèle ouvert auto-hébergé sur GPU local) sans modifier une seule ligne du harnais de test ou des scripts de validation.

```text
ARCHITECTURE DE ROUTAGE AGNOSTIQUE ET SOUVERAINE :

                               [ HARNAIS AGENTIQUE SOUVERAIN ]
                               (Aider / Claude Code / Roo Code / OpenHands)
                                              │
                                              ▼ (Standard OpenAI / OpenTelemetry)
                       ┌──────────────────────────────────────────────┐
                       │     ROUTEUR LOCAL UNIFIÉ (LiteLLM / Ollama)   │
                       └──────────────────────┬───────────────────────┘
                                              │
                   ┌──────────────────────────┼──────────────────────────┐
                   ▼                          ▼                          ▼
      [ MOTEURS PROPRIÉTAIRES ]      [ INFÉRENCE LOCALE / VPS ]     [ SERVEURS DISTANTS DÉDIÉS ]
      • Claude (Anthropic API)       • vLLM / SGLang (GPU Nvidia)   • Hugging Face TGI / RunPod
      • OpenAI (o-series / GPT)      • Ollama / llama.cpp (Apple/CPU)• Modèles Open Weights hébergés
```

### 12.2 Panorama des Modèles Libres & Open Weights (2026) {#section-12-2}
En 2026, la frontière de performance entre modèles propriétaires fermés et modèles à poids ouverts (Open Weights) s'est effondrée. Les modèles sous licences permissives (Apache 2.0, MIT, Llama Community) permettent une inférence locale sans fuite de données et sans censure de contexte.

| Famille de Modèles Libres | Architecture & Spécificités Techniques | Rôle Idéal dans le Harnais |
| :--- | :--- | :--- |
| **DeepSeek (R1 / V3 / Coder)** {{< source-break >}} *Licence MIT / Ouverte* | Architecture Mixture-of-Experts (MoE) ultra-efficace, raisonnement formel délibératif (Chain-of-Thought natif) et maîtrise parfaite de la génération de patches de code. | **Raisonnement & Refactoring Lourd :** Capable de concevoir des suites de tests TDD complexes et de résoudre des bugs d'invariants en local sans coût de token API. |
| **Meta Llama (Llama 3.3 / Llama 4)** {{< source-break >}} *Licence Communautaire Ouverte* | Fenêtre de contexte native jusqu'à 128k/256k tokens, stabilité syntaxique exceptionnelle sur TypeScript, Rust, Python et SQL. Support massif de toutes les bibliothèques d'inférence. | **Moteur d'Exécution Généraliste :** Idéal pour l'implémentation de domaine (Phase 4), la conversion Schema-First et la rédaction de documentation technique. |
| **Qwen (Qwen 2.5 Coder / QwQ)** {{< source-break >}} *Licence Apache 2.0* | Entraîné sur plus de 5 500 milliards de tokens de code et mathématiques. Excellente précision sur les formats de sortie stricts (JSON Schema, YAML, unified diff). | **Spécialiste de la Précision Syntaxique :** Génération chirurgicale de contrats de données, de migrations SQL Expand-Contract et de scripts shell. |
| **Mistral / Codestral** {{< source-break >}} *Licence Apache 2.0* | Optimisation FIM (Fill-in-the-Middle) de pointe, latence d'inférence ultra-faible et empreinte mémoire réduite pour exécution sur stations de travail locales. | **Complétion & Édition Rapide :** Génération de tests unitaires atomiques et refactoring de micro-modules. |

### 12.3 Runtimes d'Inférence & Quantization pour l'Auto-Hébergement {#section-12-3}
L'exécution locale de modèles de 14B, 32B ou 70B paramètres repose sur des runtimes d'inférence open-source hautement optimisés :
* **vLLM & SGLang (Haute Concurrence sur Serveur / VPS GPU) :** Moteurs Python/C++ utilisant l'algorithme *PagedAttention* pour éliminer la fragmentation de mémoire VRAM. Permettent de servir plusieurs agents simultanément avec un débit 4 à 8 fois supérieur aux serveurs classiques.
* **Ollama & llama.cpp (Simplicité & Postes de Travail) :** Exécution multi-plateforme (Linux, macOS Apple Silicon, Windows) en C/C++ pur. Permet de charger un modèle d'un simple fichier en mémoire unifiée sans configuration complexe.
* **Formats de Quantization (GGUF / AWQ / EXL2) :** Techniques de compression numérique réduisant la précision des poids de 16 bits à 4 ou 8 bits (ex: `Q4_K_M`, `Q8_0`) avec une dégradation de raisonnement inférieure à 1%, divisant par trois les besoins en mémoire VRAM.

### 12.4 Moteurs & Outils d'Orchestration Agentique Open Source {#section-12-4}
Pour préserver l'indépendance de sa chaîne de production logicielle, l'orchestrateur s'appuie sur des outils de développement dont le code source est auditable et sous licence libre :

| Outil Agentique Open Source | Type d'Interface & Fonctionnement | Avantage Décisif pour le Harnais |
| :--- | :--- | :--- |
| **Aider (Licence Apache 2.0)** | CLI terminal agnostique, interfaçable avec n'importe quel endpoint OpenAI/vLLM/Ollama. | Gestionnaire Git natif, cartographie AST automatique (Tree-sitter Repo Map) et génération de commits atomiques conventionnels. |
| **OpenHands / SWE-Agent** | Plateforme agentique conteneurisée autonome opérant dans des bacs à sable Docker étanches. | Exécute des boucles de résolution complètes (de l'issue GitHub au commit validé par les tests) en isolation totale. |
| **Roo Code & Cline (VS Code)** | Extensions open source multi-fournisseurs avec approbation explicite de chaque commande shell. | Contrôle pas à pas des fichiers touchés, bascule instantanée entre modèles cloud et serveurs locaux vLLM. |
| **Goose (Block / Apache 2.0)** | Agent autonome extensible par plugins MCP via terminal ou éditeur. | Conçu spécifiquement pour étendre ses capacités via des serveurs MCP locaux sécurisés. |

### 12.5 Le Standard Ouvert MCP & Serveurs Locaux Auto-Hébergés {#section-12-5}
Le protocole **Model Context Protocol (MCP)** permet d'exécuter des outils d'inspection sans jamais donner un accès shell total ou non filtré à l'agent :
* `mcp-server-git` : Expose uniquement les primitives Git autorisées (diff, log, status, worktree add/remove) en bloquant tout `push --force`.
* `mcp-server-postgres` : Permet à l'agent d'inspecter les schémas de tables (`information_schema`) et d'exécuter des requêtes `EXPLAIN` sans droits d'écriture sur les tables de production.
* `mcp-server-tree-sitter` : Analyse syntaxiquement les fichiers sources pour renvoyer à l'agent la carte des types et des signatures sans charger les corps de fonctions inutiles.
* `mcp-server-docker` : Contrôle le lancement de conteneurs de tests éphémères en environnement isolé.

### 12.6 Matrice d'Arbitrage Éthique & Technique : Propriétaire vs Open Source {#section-12-6}

| Critère | Modèles Propriétaires Cloud (Anthropic / OpenAI) | Modèles Libres & Open Weights (DeepSeek / Llama / Qwen) |
| :--- | :--- | :--- |
| **Confidentialité** | Flux de données transitant par des serveurs tiers (soumis aux politiques d'utilisation cloud). | **Étanchéité Totale :** 100% des flux s'exécutent sur la machine locale ou le VPS privé chiffré. |
| **Coût à l'Usage** | Facturation par token consommé (peut devenir élevé lors de boucles de tests intensives). | **Coût Marginal Nul :** Facturation fixe de l'infrastructure matérielle (GPU/Serveur). |
| **Résilience / Disponibilité** | Dépend de la disponibilité de l'API distante et des limitations de débit (Rate Limits). | **Disponibilité Absolue :** Fonctionne hors-ligne sans connexion Internet requise. |
| **Pérennité & Reproductibilité** | Le fournisseur peut mettre à jour ou déprécier une version de modèle sans préavis. | **Reproductibilité Éternelle :** Les poids du modèle (`.gguf` / safetensors) sont figés et archivés. |


---

## À propos de cette source {#notice-source}

**Empreinte SHA-256 de l'original** : `26a9359d96595daa72da4f01626df2fdd14691c13f6481dae0c86725a54c5ee1`.

Les affirmations et prompts sont reproduits comme éléments du document, sans validation ni exécution. [Consulter le registre critique](/projet/references/registre-critique).

## Chapitres qui utilisent cette source

- [A01 — Piloter un système, pas une génération de code](/accessible/01-piloter-un-systeme).
- [A02 — Organiser l'architecture et les responsabilités](/accessible/02-architecture-et-frontieres).
- [A03 — Transformer le besoin en contrat vérifiable](/accessible/03-besoin-et-contrats).
- [A04 — Donner du contexte et des limites à l'agent](/accessible/04-harnais-et-contexte).
- [A05 — Garder une histoire fiable avec Git](/accessible/05-git-et-collaboration).
- [A06 — Demander des preuves, pas seulement du code](/accessible/06-tests-et-preuves).
- [A07 — Faire travailler le système sans perdre les opérations](/accessible/07-asynchronisme-et-reprises).
- [A08 — Protéger les données et faire évoluer leur structure](/accessible/08-donnees-et-migrations).
- [A09 — Passer du poste local à un service réel](/accessible/09-livraison-et-production).
- [A10 — Observer, améliorer et rétablir le service](/accessible/10-exploitation-et-evolution).
- [A11 — Appliquer ORCHESTRE du besoin à la résolution](/accessible/11-methode-et-cas-pratiques).
- [A12 — Choisir ses outils et préserver son indépendance](/accessible/12-ecosysteme-et-independance).
- [B01 — Piloter un système, pas une génération de code](/ingenieure/01-piloter-un-systeme).
- [B02 — Organiser l'architecture et les responsabilités](/ingenieure/02-architecture-et-frontieres).
- [B03 — Transformer le besoin en contrat vérifiable](/ingenieure/03-besoin-et-contrats).
- [B04 — Donner du contexte et des limites à l'agent](/ingenieure/04-harnais-et-contexte).
- [B05 — Garder une histoire fiable avec Git](/ingenieure/05-git-et-collaboration).
- [B06 — Demander des preuves, pas seulement du code](/ingenieure/06-tests-et-preuves).
- [B07 — Faire travailler le système sans perdre les opérations](/ingenieure/07-asynchronisme-et-reprises).
- [B08 — Protéger les données et faire évoluer leur structure](/ingenieure/08-donnees-et-migrations).
- [B09 — Passer du poste local à un service réel](/ingenieure/09-livraison-et-production).
- [B10 — Observer, améliorer et rétablir le service](/ingenieure/10-exploitation-et-evolution).
- [B11 — Appliquer ORCHESTRE du besoin à la résolution](/ingenieure/11-methode-et-cas-pratiques).
- [B12 — Choisir ses outils et préserver son indépendance](/ingenieure/12-ecosysteme-et-independance).
