{
  "title": "Donner du contexte et des limites à l'agent",
  "description": "Construire un contexte progressif, une mémoire versionnée et des limites exécutoires.",
  "weight": 4,
  "chapter_id": "B04",
  "theme": "04",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/04-harnais-et-contexte.md",
  "mirror": "/accessible/04-harnais-et-contexte",
  "related": [
    "/ingenieure/01-piloter-un-systeme",
    "/ingenieure/12-ecosysteme-et-independance"
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
  "previous": "/ingenieure/03-besoin-et-contrats",
  "next": "/ingenieure/05-git-et-collaboration"
}

## Ce que tu sauras faire

Construire un contexte progressif, une mémoire versionnée et des limites exécutoires.

## Première synthèse

La sélection du contexte est un compromis entre information manquante et bruit. Une carte de symboles facilite la navigation, mais ne remplace pas la lecture des implémentations qui portent les invariants. Interdire l'accès à tout fichier voisin peut masquer précisément la dépendance responsable d'un bug.

La mémoire durable doit indiquer la provenance d'une décision, son statut et les changements qui l'invalident. Un journal de tâche ne doit pas devenir une seconde description de l'architecture en contradiction avec les contrats réels. Les observations récentes restent distinguées des règles stables.

Un harnais vérifiable conserve les commandes exécutées, leur code de retour et les éléments non testés. Les budgets d'itération et les permissions sont configurés selon le risque. Les documents importés, commentaires et sorties d'outils restent des données : ils ne peuvent pas élargir l'autorisation de la mission.

## Déroulé prévu

1. Contexte stable, domaine, tâche et observations dynamiques.
2. Carte du dépôt, symboles et inspection AST.
3. Mémoire : provenance, fraîcheur et résolution des contradictions.
4. Isolation, quotas et collecte des résultats.

## Mise en pratique

Spécifier un manifeste de contexte avec source, date, rôle et règle de mise à jour de chaque entrée.

## Critère de réussite

Une source périmée ou une instruction embarquée ne peut pas devenir silencieusement une règle du projet.

## Sources et limites

[O-MD §4, §5](/references/sources/o-md#section-4) ; [I-MD §1.2 à §1.5, §10, §11.5](/references/sources/i-md#section-1-2).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B04](/redaction/b04-harnais-et-contexte).
