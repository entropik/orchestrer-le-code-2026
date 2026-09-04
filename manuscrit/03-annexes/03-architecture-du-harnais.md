# Architecture du harnais & Gestion de la Smart Zone

En ingénierie assistée par agents, le harnais d'orchestration ne doit jamais être conçu comme un bloc monolithique ou lié à un outil propriétaire (Claude, OpenAI Codex, Google Gemini, Kimi, Cursor). Il s'organise selon une **architecture hybride en trois couches distinctes**, complétée par une discipline stricte de la mémoire de travail (*Smart Zone*).

---

## 1. Déploiement : Racine de Projet (.agents/) ou Configuration Globale (~/.) ?

Une interrogation récurrente concerne le point d'ancrage physique des compétences : **faut-il installer les skills à la racine de chaque projet Git (sous `.agents/skills/`), ou globalement sur sa machine de travail (sous `~/.gemini/` ou `~/.claude/`) ?**

Il ne s'agit pas d'opposer ces deux approches, mais de mettre en œuvre une **architecture hybride en couches** (*Layered Architecture*).

### Tableau comparatif synthétique

| Critère d'évaluation | À la racine du projet (`.agents/skills/`) | Globalement sur la machine (`~/.`) |
| :--- | :--- | :--- |
| **Partage en équipe & Étudiants** | **Immédiat** : un `git clone` suffit pour que tout le monde dispose exactement des mêmes skills. | **Nul** : chaque collaborateur ou apprenant doit installer et configurer sa machine à la main. |
| **Reproductibilité & Versioning Git** | **Parfait** : les compétences évoluent avec les commits du projet et restent calées sur sa version. | **Risque de dérive** : une mise à jour globale non rétrocompatible peut casser un ancien projet. |
| **Spécialisation au contexte** | **Totale** : les skills intègrent les commandes exactes du projet (`pytest`, `vitest`, Hugo, conventions d'ADR). | **Générique** : obligé de rester abstrait pour ne pas créer d'effets de bord sur d'autres projets. |
| **Disponibilité sur nouveaux projets** | Nécessite d'initialiser le dossier `.agents/` sur chaque nouveau dépôt. | **Omniprésent** : disponible instantanément sur n'importe quel scratchpad ou dépôt tiers. |
| **Maintenance multi-dépôts** | Demande un effort de synchronisation si vous gérez 20 dépôts distincts. | **Centralisée** : une seule mise à jour profite instantanément à tous vos terminaux locaux. |
| **CI/CD & Agents autonomes** | Les runners distants (GitHub Actions) et conteneurs Docker y ont accès immédiatement. | Inexistant sur les machines distantes ou les serveurs d'intégration continue. |

---

## 2. Les Trois Piliers d'Ingénierie

### 1. Pourquoi la racine (`.agents/`) est indispensable pour les équipes et les formations
- **Élimination radicale du syndrome « Ça marche sur ma machine »** : Si vos compétences résident uniquement dans votre répertoire personnel `~/`, l'étudiant ou le collègue qui clone le projet voit son agent échouer ou improviser sans filet.
- **Le concept de « Repository-as-Code »** : Le dépôt Git embarque son propre harnais d'orchestration (`.agents/skills/`, `.agents/rules/`, `CONTEXT.md`). Quiconque rejoint le dépôt hérite instantanément de la discipline de l'équipe.
- **L'alignement sur les outils réels** : Sur ce manuel, la validation repose sur `python3.11 -m unittest` et la compilation sur Hugo. Un skill local `/implement` sait précisément quelles commandes de test exécuter.

### 2. Pourquoi la configuration globale (`~/.`) reste utile au quotidien
- **L'ancrage des réflexes cognitifs universels** : Des compétences comme `/ask-matt` (l'aiguilleur), `/grill-me` (l'interview hors dépôt), `/wait-what` (l'arrêt d'urgence anti-jargon) et `/teach` sont purement méthodologiques et indépendantes de tout projet.
- **Le confort immédiat** : Disponible dès l'ouverture d'un terminal dans `/tmp/` ou lors de l'inspection d'une bibliothèque open-source tierce.

### 3. Le Modèle Hybride en 3 Couches & Règle de Précédence (*Shadowing*)

Les moteurs d'agents contemporains appliquent une règle stricte : **le local surcharge toujours le global (*shadowing*)**. Si une compétence `/ask-matt` existe dans votre dossier global mais qu'un fichier `.agents/skills/ask-matt/SKILL.md` est présent à la racine du dépôt actif, c'est la version locale du projet qui s'impose avec ses règles spécifiques.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. COUCHE GLOBALE (Machine développeur : ~/.gemini/ ou ~/.claude/)    │
│    - Rôle : Vos réflexes personnels, navigation et apprentissage      │
│    - Exemples : ask-matt, grill-me, wait-what, teach, obsidian-vault  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼ (Surcharge locale prioritaire)
┌────────────────────────────────────────────────────────────────────────┐
│ 2. COUCHE PROJET (Dépôt Git : .agents/skills/ à la racine)             │
│    - Rôle : Gouvernance d'équipe, contrats et preuves de fabrication  │
│    - Exemples : setup-skills, grill-with-docs, to-prd, to-issues,     │
│                 implement, tdd, review, diagnosing-bugs, wizard       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. COUCHE RUNTIME / MÉMOIRE VIVE (CONTEXT.md, docs/adr/, tickets)     │
│    - Rôle : Les artefacts vivants produits par les agents et l'équipe │
│    - Exemples : Modèle de domaine, ADRs actés, backlog d'issues       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Gestion de la Smart Zone & Frontières de Phases

La mémoire de travail d'un agent n'est pas infinie. Au-delà de ~100k à 120k tokens (la **Smart Zone**), la précision de raisonnement du modèle s'érode. À la fin de chaque étape, l'ingénieur arbitre explicitement entre 5 postures :

| Posture aux frontières de phases | Quand l'utiliser | Ce qu'elle produit |
| :--- | :--- | :--- |
| **Continue** | La tâche courante est modeste et la session reste sous les ~40k-50k tokens. | Zéro friction, continuité immédiate. |
| **`/clear`** | L'étape précédente est archivée dans un artefact pérenne (ex: PRD validé, tickets créés). | Contexte vidé à 100 %, session vierge prête pour `/implement`. |
| **`/handoff`** | Changement de répertoire, de harnais d'agent, ou transmission à un collègue. | Note Markdown temporaire dans `/tmp/` résumant l'état exact et les compétences à appeler. |
| **Sous-agent** | Recherche documentaire ou exploration de code isolée en arrière-plan. | Rapport synthétique injecté dans la session principale sans charger le contexte de tokens inutiles. |
| **`/compact`** | La session approche des 100k tokens avant la fin du cadrage. | Résumé condensé de l'historique pour poursuivre sans dégradation cognitive. |

---

## 4. Les 3 Règles d'Or de l'Ingénierie Agnostique

1. **L'hygiène de la *Smart Zone*** :
   - Au-delà de ~100k-120k tokens, les modèles dégradent leur raisonnement.
   - Les phases de cadrage (`/grill-with-docs` → `/to-prd` → `/to-issues`) se tiennent en une seule session.
   - Dès l'émission des tickets, **on vide le contexte** (ou on utilise `/handoff`). Chaque `/implement` s'exécute dans une session vierge dédiée à son ticket unitaire.
2. **La pyramide des artefacts** :
   - **Pérenne** : `CONTEXT.md` (glossaire métier) et `docs/adr/` (décisions engageantes).
   - **Éphémère de cycle** : PRD et tickets d'issues (vivent le temps du chantier).
   - **Jetable instantané** : prototypes (`/prototype`) et rapports HTML (`/tmp/*.html`).
3. **La primauté des preuves observables** :
   - L'agent ne livre pas du code : il livre une **preuve vérifiable** (test unitaire/d'intégration passant à l'interface publique d'un module profond).

---

*Pour découvrir comment ces règles s'articulent dans les flux opérationnels, consulter le [Guide des workflows](02-guide-des-workflows.md). Pour explorer les fiches détaillées des 37 compétences, consulter le [Catalogue des skills](04-catalogue-des-skills.md).*
