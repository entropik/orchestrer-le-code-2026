{
  "title": "Choisir ses outils et préserver son indépendance",
  "description": "Comparer cloud et local selon l'usage, les coûts et les données plutôt que selon une promesse.",
  "weight": 12,
  "chapter_id": "A12",
  "theme": "12",
  "status": "amorce",
  "source_path": "manuscrit/01-lecture-accessible/12-ecosysteme-et-independance.md",
  "mirror": "/ingenieure/12-ecosysteme-et-independance",
  "related": [
    "/accessible/04-harnais-et-contexte",
    "/accessible/06-tests-et-preuves"
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
  "previous": "/accessible/11-methode-et-cas-pratiques"
}

## Ce que tu sauras faire

Comparer cloud et local selon l'usage, les coûts et les données plutôt que selon une promesse.

## Première synthèse

Le modèle produit des réponses ; l'agent organise des actions ; les outils lui permettent d'inspecter ou de modifier un environnement. Changer l'un ne garantit pas que les autres se comporteront de la même façon. Pour choisir, pars d'une tâche représentative de ton projet.

Un modèle téléchargeable n'est pas forcément utilisable sans restriction. Il faut regarder la licence de la version exacte. L'exécution locale peut réduire certains transferts de données, mais elle exige encore de maîtriser les connexions, les journaux, les accès et les mises à jour.

L'indépendance se prépare en conservant ses documents, ses critères et ses tests dans des formats réutilisables. Compare la qualité obtenue, le temps de correction et le coût total, y compris l'exploitation. Un outil gratuit à télécharger peut demander beaucoup de matériel et d'attention pour rendre un service fiable.

## Déroulé prévu

1. Modèle, agent, moteur d'exécution et connecteur.
2. Poids accessibles et liberté d'usage : des questions différentes.
3. Cloud, local ou hybride : qui exploite quoi ?.
4. Essayer sur ses tâches et garder une possibilité de sortie.

## Mise en pratique

Comparer deux solutions sur trois tâches factices, sans envoyer de données confidentielles.

## Critère de réussite

La fiche distingue licence, hébergement, qualité observée, coût complet et possibilité de remplacement.

## Sources et limites

[O-MD §2, §4](/references/sources/o-md#section-2) ; [I-MD §12.1 à §12.6](/references/sources/i-md#section-12-1).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](/references/registre-critique). Les exemples techniques restent à développer et à tester dans la tranche.

## Références pour approfondir

- [Mistral — fiche Codestral 24.05](https://docs.mistral.ai/models/codestral-24-05) — Exemple historique de licence MNPL, pas une recommandation de modèle actuel. [Notice et chapitres associés](/references#ref-codestral).
- [MCP — autorisation, spécification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) — Distinguer transport, autorisation et permissions effectives. [Notice et chapitres associés](/references#ref-mcp).
- [OpenAI — construire une évaluation](https://developers.openai.com/api/docs/guides/evals) — Définir tâches, données et critères ; cette référence n'établit aucun classement. [Notice et chapitres associés](/references#ref-evals).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A12](/redaction/a12-ecosysteme-et-independance).
