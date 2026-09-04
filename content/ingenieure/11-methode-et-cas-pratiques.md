{
  "title": "Appliquer ORCHESTRE du besoin à la résolution",
  "description": "Raccorder la méthode de pilotage ORCHESTRE aux étapes techniques et aux compétences d'ingénierie sans construire un cycle en cascade.",
  "weight": 11,
  "chapter_id": "B11",
  "theme": "11",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/11-methode-et-cas-pratiques.md",
  "mirror": "/accessible/11-methode-et-cas-pratiques",
  "related": [
    "/ingenieure/01-piloter-un-systeme",
    "/ingenieure/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "ADR",
      "anchor": "adr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    },
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    }
  ],
  "previous": "/ingenieure/10-exploitation-et-evolution",
  "next": "/ingenieure/12-ecosysteme-et-independance"
}

## Ce que tu sauras faire

Raccorder la méthode de pilotage ORCHESTRE aux étapes techniques et aux compétences d'ingénierie sans construire un cycle en cascade.

## Première synthèse

Les six phases KISS du traité organisent la fabrication : spécification, contrats, tests, implémentation, intégration et livraison. La méthode **ORCHESTRE** (Observation, Règle, Contrat, Harnais, Épreuve, Solution, Traçabilité, Révision, Évolution) organise la gouvernance cognitive, la décision et la preuve. Les deux grilles se combinent à l'intérieur d'une tranche verticale (*tracer bullet*) ; elles ne justifient jamais de construire toutes les couches horizontales avant le premier parcours utilisateur vérifiable.

Sur le plan opérationnel, ORCHESTRE s'articule directement avec le **Ruban Principal d'ingénierie agentique** (*Main Flow*) :

- **Observation & Règles (O & R)** : Pilotées par `/grill-with-docs`. L'agent refuse d'écrire du code : il fouille l'existant, pose une seule question contradictoire à la fois, stabilise le glossaire métier dans `CONTEXT.md` et consigne les choix structurants dans `docs/adr/`.
- **Contrats vérifiables (C)** : Traduits par `/to-prd` (spécification univoque, User Stories, périmètre exclu) puis `/to-issues` (découpage en tranches verticales indépendantes avec dépendances bloquantes déclarées).
- **Harnais & Frontières de phases (H)** : Discipline de la *Smart Zone* (~100k-120k tokens). Dès que les tickets sont émis, l'ingénieur vide la mémoire (`/clear`) ou génère une note temporaire (`/handoff`). Chaque ticket s'exécute dans une session vierge isolée.
- **Épreuve & Solution (E & S)** : Orchestrées par `/implement` adossé à `/tdd`. L'agent ne livre pas du code présomptif : il formule d'abord une preuve observable (test unitaire ou d'intégration rouge à la frontière publique d'un module profond) avant de coder la solution minimale.
- **Traçabilité & Révision (T & R)** : Barrière de péage `/review`. Un double audit automatisé et contradictoire (Axe 1 : Standards et sécurité ; Axe 2 : Respect scrupuleux de la spécification du ticket) précède impérativement tout commit ou fusion.
- **Évolution & Incidents (E)** : En cas d'anomalie ou de régression, bascule sur `/diagnosing-bugs` (obligation d'une commande rouge déterministe) et passage de relais à `/improve-codebase-architecture` si l'absence d'une couture (*seam*) a favorisé le bug.

Cette mécanique s'exécute de façon rigoureusement agnostique, que le moteur sous-jacent soit OpenAI Codex, Anthropic Claude, Google Gemini, Kimi ou les orchestrateurs locaux de Cursor.

Le cas fil rouge de réception de fichier PDF préserve les mêmes acteurs, états et contraintes que la lecture accessible. La version ingénieure ajoute les contrats stricts, les fenêtres de crash, les jeux d'essai déterministes et les procédures de livraison sans régression.

## Déroulé prévu

1. Correspondance détaillée entre ORCHESTRE, les six phases KISS et la chaîne d'outillage des agents.
2. Le cycle vertical complet : cadrage (`/grill-with-docs`), spécification (`/to-prd`), tranches (`/to-issues`), fabrication sous preuve (`/implement` + `/tdd`) et audit (`/review`) (formalisation exhaustive dans le [Guide des workflows agentiques](/annexes/workflows-agentiques)).
3. Upload et devis d'impression : session, droits, validation de fond perdu (bleed), finalisation et reprise après incident.
4. Détection de doublons : reproduction causale déterministe, contraintes d'intégrité, migration sans interruption et métriques de production.

## Mise en pratique

Produire deux dossiers de réalisation avec SPEC formelle, ADRs vivants, matrice de tests de frontière et plan de livraison orchestré.

## Critère de réussite

Chaque décision de la partie accessible trouve sa justification technique, chaque ligne de code produite est précédée d'un test rouge observable, et la trajectoire complète est reproductible quel que soit l'agent de code employé.

## Sources et limites

[O-MD §5, §11, §12, §13, §14](/references/sources/o-md#section-5) ; [I-MD §9, §10](/references/sources/i-md#section-9) ; [Guide des workflows agentiques](/annexes/workflows-agentiques).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B11](/redaction/b11-methode-et-cas-pratiques).
