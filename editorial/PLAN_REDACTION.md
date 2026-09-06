# Plan de rédaction par chapitre

## Unité de travail

Une tranche = une lecture d'un chapitre. Une paire = Axx + Bxx sur le même sujet. Les fiches sont des missions locales prêtes à utiliser, pas des issues déjà créées sur GitHub.

Ordre conseillé : traiter A01 puis B01, harmoniser la paire, poursuivre avec A02 puis B02. L'ordre de lecture publié reste A01 à A12, puis B01 à B12. Une passe finale relit chaque partie indépendamment pour vérifier qu'elle se suffit à elle-même.

## File des 24 tranches

| Tranche | Lecture | Mission | Prérequis | Statut |
|---|---|---|---|---|
| A01 | accessible | [Piloter un système, pas une génération de code](../tranches/A01-piloter-un-systeme.md) | aucun | validé |
| A02 | accessible | [Organiser l'architecture et les responsabilités](../tranches/A02-architecture-et-frontieres.md) | A01 | validé |
| A03 | accessible | [Transformer le besoin en contrat vérifiable](../tranches/A03-besoin-et-contrats.md) | A02 | validé |
| A04 | accessible | [Donner du contexte et des limites à l'agent](../tranches/A04-harnais-et-contexte.md) | A03 | validé |
| A05 | accessible | [Garder une histoire fiable avec Git](../tranches/A05-git-et-collaboration.md) | A04 | validé |
| A06 | accessible | [Demander des preuves, pas seulement du code](../tranches/A06-tests-et-preuves.md) | A05 | validé |
| A07 | accessible | [Faire travailler le système sans perdre les opérations](../tranches/A07-asynchronisme-et-reprises.md) | A06 | validé |
| A08 | accessible | [Protéger les données et faire évoluer leur structure](../tranches/A08-donnees-et-migrations.md) | A07 | validé |
| A09 | accessible | [Passer du poste local à un service réel](../tranches/A09-livraison-et-production.md) | A08 | validé |
| A10 | accessible | [Observer, améliorer et rétablir le service](../tranches/A10-exploitation-et-evolution.md) | A09 | validé |
| A11 | accessible | [Appliquer ORCHESTRE du besoin à la résolution](../tranches/A11-methode-et-cas-pratiques.md) | A10 | validé |
| A12 | accessible | [Choisir ses outils et préserver son indépendance](../tranches/A12-ecosysteme-et-independance.md) | A11 | validé |
| B01 | ingenieure | [Piloter un système, pas une génération de code](../tranches/B01-piloter-un-systeme.md) | A01 | validé |
| B02 | ingenieure | [Organiser l'architecture et les responsabilités](../tranches/B02-architecture-et-frontieres.md) | A02, B01 | validé |
| B03 | ingenieure | [Transformer le besoin en contrat vérifiable](../tranches/B03-besoin-et-contrats.md) | A03, B02 | validé |
| B04 | ingenieure | [Donner du contexte et des limites à l'agent](../tranches/B04-harnais-et-contexte.md) | A04, B03 | validé |
| B05 | ingenieure | [Garder une histoire fiable avec Git](../tranches/B05-git-et-collaboration.md) | A05, B04 | validé |
| B06 | ingenieure | [Demander des preuves, pas seulement du code](../tranches/B06-tests-et-preuves.md) | A06, B05 | validé |
| B07 | ingenieure | [Faire travailler le système sans perdre les opérations](../tranches/B07-asynchronisme-et-reprises.md) | A07, B06 | validé |
| B08 | ingenieure | [Protéger les données et faire évoluer leur structure](../tranches/B08-donnees-et-migrations.md) | A08, B07 | validé |
| B09 | ingenieure | [Passer du poste local à un service réel](../tranches/B09-livraison-et-production.md) | A09, B08 | validé |
| B10 | ingenieure | [Observer, améliorer et rétablir le service](../tranches/B10-exploitation-et-evolution.md) | A10, B09 | validé |
| B11 | ingenieure | [Appliquer ORCHESTRE du besoin à la résolution](../tranches/B11-methode-et-cas-pratiques.md) | A11, B10 | validé |
| B12 | ingenieure | [Choisir ses outils et préserver son indépendance](../tranches/B12-ecosysteme-et-independance.md) | A12, B11 | validé |

## Jalons

1. **Paire pilote A01/B01** : Validée. Ton et différence de profondeur étalonnés.
2. **Paires 02 à 06** : Validées. Architecture, contrats, harnais, Git et tests opérationnels.
3. **Paires 07 à 10** : Validées. Asynchronisme, données, livraison et observabilité en place.
4. **Paires 11 et 12** : Validées. Cas pratiques de bout en bout et indépendance d'écosystème.
5. **Relecture transversale & schémas** : Validée. 61 planches techniques transposées, cohérence conceptuelle et tests automatisés.
6. **Édition & publication** : Validée. Déploiement continu du site statique, exports complets et validation HTML déterministe.

## États

`amorce` → `redaction` → `relecture` → `valide`. Le manifeste [chapitres.json](chapitres.json) est la source de vérité. Un chapitre n'est validé qu'après satisfaction de la fiche ; un build réussi ne valide pas son contenu technique.

## Charge éditoriale réalisée

12 chapitres accessibles (26 244 mots) et 12 chapitres approfondis (29 888 mots), complétés par l'Avant-propos opérationnel et les 6 annexes communes. Le manuscrit compte 56 132 mots rédigés dans les deux lectures miroirs et 61 schémas graphiques intégrés.
