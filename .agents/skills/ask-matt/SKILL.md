---
name: ask-matt
description: Aiguilleur de session universel pour orchestrer le code avec des agents. Détermine le skill ou le flux adapté à votre situation (idée, bug, triage, brouillard, jargon, secrets).
disable-model-invocation: true
---

# Ask Matt — Routeur d'ingénierie agentique

Vous ne pouvez pas retenir chaque compétence par cœur, alors demandez l'aiguillage.

Une session efficace ne commence jamais par du code improvisé. Elle s'inscrit dans un **flux** prévisible. La quasi-totalité du travail emprunte un **ruban principal** (*Main Flow*), complété par trois **voies d'insertion** (*On-ramps*), cinq choix aux **frontières de phases** (*Phase boundaries*), et trois **outils de déblocage d'urgence**.

---

## 1. Le Ruban Principal : De l'Idée à la Production (Idea → Ship)

Le parcours nominal lorsque vous avez une intention et que vous voulez la construire :

1. **`/grill-with-docs [votre intention]`** :
   - Établit l'interview contradictoire serrée.
   - Fouille le code avant chaque question. Pose **une seule question à la fois** avec sa recommandation.
   - Aligne les définitions métier dans `CONTEXT.md`.
   - Rédige un ADR dans `docs/adr/` si une décision lourde et difficilement réversible est actée.
   - *Aucun code de production n'est écrit ici.*

2. **Embranchement : Le doute exige-t-il une réponse exécutable ?**
   - Si la question concerne l'ergonomie (UI) ou un automate logique complexe :
     - `/handoff` vers une session propre.
     - `/prototype` sur une branche dédiée `prototype/<nom>` pour répondre par du code jetable lancé en une commande.
     - `/handoff` des conclusions vers le fil de discussion initial.

3. **Embranchement : Le chantier dépasse-t-il une session ?**
   - **Oui (multi-sessions)** :
     - `/to-prd` (ou `/to-spec`) : synthèse des acquis du grilling sans relancer de questions.
     - `/to-issues` (ou `/to-tickets`) : découpage en tranches verticales étanches (*tracer bullets* : schéma, logique, API, UI, test e2e) avec liens de blocage stricts.
     - `/clear` du contexte.
     - Pour chaque ticket : session neuve avec `/implement`.
   - **Non (mono-session)** :
     - Lancement direct de `/implement` dans la même session.

4. **Fabrication sous preuve & Barrière de péage** :
   - `/implement` pilote en interne `/tdd` (cycle rouge à la frontière publique → vert minimal → refactor).
   - Clôture obligatoire par `/review` : audit automatisé sur deux axes (Axe 1 : Standards de code ; Axe 2 : Respect strict de la Spécification).

---

## 2. Les Trois Voies d'Insertion (On-Ramps)

Des situations initiales qui génèrent du travail avant de rejoindre le ruban principal :

- **Bugs et demandes entrantes qui s'accumulent** $\rightarrow$ **`/triage`** :
  - Analyse l'antériorité contre `.out-of-scope/`.
  - Reproduit la panne ou valide la PR, puis classe (`needs-info`, `ready-for-agent`, `wontfix`).
  - *Règle d'or : Ne JAMAIS trier des tickets générés par `/to-issues` (ils sont déjà prêts pour l'agent).*

- **Un bug dur, une régression ou un test flaky** $\rightarrow$ **`/diagnosing-bugs`** :
  - Refuse toute hypothèse sans une commande unique déterministe qui reproduit le rouge à 100%.
  - Minimise le cas de reproduction.
  - Pose 3 à 5 hypothèses falsifiables, vérifiées par des sondes étiquetées `[DEBUG-xxxx]`.
  - Écrit le test de non-régression, corrige à la frontière publique, nettoie les sondes.
  - Si aucune couture (*seam*) n'existait, passe le relais à `/improve-codebase-architecture`.

- **Chantier massif et brumeux (greenfield, refonte d'envergure)** $\rightarrow$ **`/wayfinder`** *(ou `/decision-mapping`)* :
  - Ne produit pas de code mais une carte partagée de tickets de décisions (`DECISION_MAP.md`).
  - Une session = un seul ticket résolu, clôturé impérativement par `/handoff`.
  - Quand le brouillard est dissipé, bascule vers `/to-prd` puis `/to-issues`.

---

## 3. L'Arbitrage aux Frontières de Phases & Smart Zone

À chaque fin d'étape d'ingénierie, arbitrez parmi les 5 options :

1. **Continue** : rester dans la même session si vous êtes largement sous le seuil de saturation cognitive.
2. **`/clear`** : vider intégralement la mémoire lorsque l'étape précédente n'a plus d'utilité immédiate (ex: entre le découpage en tickets et l'implémentation du premier ticket).
3. **`/handoff`** : écrire une passerelle portable hors dépôt (`/tmp/`) lors d'un changement de harnais, de répertoire ou de transfert à un collègue.
4. **Sous-agent** : déléguer une tâche bornée de lecture ou de vérification dans un contexte isolé et récupérer une synthèse nette.
5. **`/compact`** : compresser l'historique quand la session approche des ~100k-120k tokens (*Smart Zone*).

---

## 4. Les 3 Outils de Secours Immédiat

- **`/wait-what`** : quand l'agent répond avec du jargon ou perd le fil. L'agent stoppe tout et ré-explique clairement en français avec le vocabulaire de `CONTEXT.md`.
- **`/to-questionnaire`** : quand le bloqueur est dans la tête d'un tiers (client, expert métier, collègue). Génère un questionnaire ciblé prêt à être envoyé.
- **`/wizard`** : quand l'agent atteint une limite physique (cliquer dans une console Cloud, générer des identifiants OAuth, payer un abonnement). Génère un script Bash interactif qui guide l'humain et stocke les secrets dans `.env`.

---

## Instruction pour l'agent lors d'un `/ask-matt`

Quand l'utilisateur invoque `/ask-matt` :
1. Identifiez sa situation réelle en 1 à 2 phrases.
2. Nommez immédiatement le **prochain skill exact** à appeler et écrivez la commande complète prête à copier.
3. Donnez la séquence complète des 3 à 5 étapes suivantes.
4. Énoncez explicitement le piège mortel à éviter dans cette situation.
5. Ne commencez **jamais** à implémenter du code vous-même au sein d'un tour `/ask-matt`.