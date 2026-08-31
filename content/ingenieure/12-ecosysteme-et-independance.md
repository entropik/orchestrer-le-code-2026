{
  "title": "Choisir ses outils et préserver son indépendance",
  "description": "Évaluer la portabilité effective des modèles et des outils, y compris MCP et l'inférence locale.",
  "weight": 12,
  "chapter_id": "B12",
  "theme": "12",
  "status": "amorce",
  "source_path": "manuscrit/02-lecture-ingenieure/12-ecosysteme-et-independance.md",
  "mirror": "/accessible/12-ecosysteme-et-independance",
  "related": [
    "/ingenieure/04-harnais-et-contexte",
    "/ingenieure/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "MCP",
      "anchor": "mcp"
    },
    {
      "label": "Modèle à poids ouverts",
      "anchor": "modele-a-poids-ouverts"
    },
    {
      "label": "Runtime d'inférence",
      "anchor": "runtime-d-inference"
    }
  ],
  "previous": "/ingenieure/11-methode-et-cas-pratiques"
}

## Ce que tu sauras faire

Évaluer la portabilité effective des modèles et des outils, y compris MCP et l'inférence locale.

## Première synthèse

Une compatibilité d'API ne prouve pas l'équivalence du comportement : schémas d'outils, erreurs, streaming, limites et états de conversation doivent être testés. La couche d'adaptation doit isoler ces différences. MCP concerne l'exposition de capacités et de ressources ; il ne constitue ni un moteur d'inférence ni une garantie automatique de permission minimale.

Pour une exécution locale, archiver la révision des poids, le tokenizer, le runtime, la configuration et le matériel utilisé. La quantification se juge sur les tâches retenues ; aucune perte de qualité universellement inférieure à un pour cent n'est établie par le corpus. Le coût inclut mémoire, énergie, supervision et temps de maintenance.

Le panorama de la source daté de septembre 2026 doit être traité comme une liste de candidats historiques à revérifier. Par exemple, la fiche officielle de Codestral 24.05 indique MNPL, ce qui interdit de classer toute la famille Codestral sous Apache 2.0. Une décision d'adoption requiert l'identifiant exact, sa licence et une évaluation datée, non un jugement global sur une famille.

## Déroulé prévu

1. Protocoles de génération, appels d'outils, JSON-RPC et MCP.
2. Licence par artefact, modèle exact et provenance.
3. Runtime, quantification, mémoire, débit et qualité.
4. Autorisations des connecteurs, données sortantes et évaluation de migration.

## Mise en pratique

Définir un protocole comparatif et une matrice de permissions d'un connecteur Git en lecture seule.

## Critère de réussite

Version, licence, capacités testées, refus attendus, mesures et risques résiduels sont consignés.

## Sources et limites

[O-MD §2, §4](/references/sources/o-md#section-2) ; [I-MD §12.1 à §12.6](/references/sources/i-md#section-12-1).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [Mistral — fiche Codestral 24.05](https://docs.mistral.ai/models/codestral-24-05) — Exemple historique de licence MNPL, pas une recommandation de modèle actuel. [Notice et chapitres associés](/references#ref-codestral).
- [MCP — autorisation, spécification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) — Distinguer transport, autorisation et permissions effectives. [Notice et chapitres associés](/references#ref-mcp).
- [OpenAI — construire une évaluation](https://developers.openai.com/api/docs/guides/evals) — Définir tâches, données et critères ; cette référence n'établit aucun classement. [Notice et chapitres associés](/references#ref-evals).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche B12](/redaction/b12-ecosysteme-et-independance).
