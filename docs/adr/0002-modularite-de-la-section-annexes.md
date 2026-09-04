# ADR 0002 : Modularisation de la section Annexes en micro-documents thématiques

- **Statut** : Accepté
- **Date** : 2026-09-04
- **Contexte** : La section Annexes concentrait l'ensemble des règles méthodologiques, des cas d'usage réels, du simulateur interactif et des 37 compétences d'ingénierie au sein d'une unique page monolithique de plus de 650 lignes (~25 minutes de lecture). Cette densité enfouissait les cas pratiques et empêchait le partage de liens directs ciblés lors de formations ou par email.

## Décision

Nous scindons la section Annexes en **cinq documents autonomes et ciblés**, adossés à une page d'atterrissage `/annexes/` faisant office de tableau de bord d'aiguillage :

1. **Tableau de Bord `/annexes/`** : Accueille le Simulateur interactif `ask-matt` en tête de section et oriente immédiatement le lecteur vers la ressource pertinente.
2. **`01-fiches-reflexes.md` (`/annexes/fiches-reflexes/`)** : Listes de contrôle opérationnelles avant de lancer, committer et livrer.
3. **`02-guide-des-workflows.md` (`/annexes/workflows/`)** : Le ruban principal d'ingénierie, l'arbre d'aiguillage et les 7 trames d'exécution pratiques pas à pas.
4. **`03-architecture-du-harnais.md` (`/annexes/architecture-harnais/`)** : La doctrine racine vs global, le modèle en 3 couches, la Smart Zone et les 3 règles d'or.
5. **`04-catalogue-des-skills.md` (`/annexes/catalogue-skills/`)** : Les 37 compétences regroupées en 6 familles sous forme d'accordéons compacts `<details>`, avec ancrage d'URL automatique pour le partage de liens directs.
6. **`05-glossaire.md` (`/annexes/glossaire/`)** : Le vocabulaire partagé et le modèle de domaine.

Un alias de redirection transparent garantit la rétro-compatibilité de l'ancienne URL `/annexes/workflows-agentiques/`.

## Options Considérées

- **Conserver la page unique monolithique avec table des matières latérale** : Rejetée car la charge cognitive reste excessive et les cas pratiques demeurent invisibles sans défilement prolongé.
- **Créer 37 pages individuelles pour chaque skill** : Rejetée car elle fragmenterait excessivement le contenu et compliquerait la vision d'ensemble des 6 familles de compétences.

## Conséquences

- **Temps de lecture maîtrisé** : Chaque document se consulte en 3 à 6 minutes.
- **Partage pédagogique ciblé** : Chaque compétence dispose d'un permalien direct (`#nom-du-skill`) ouvrant automatiquement la fiche et appliquant une surbrillance douce.
- **Hiérarchie éditoriale claire** : Séparation nette entre la *méthode* (Workflows), la *doctrine* (Harnais) et *l'outillage* (Catalogue).
