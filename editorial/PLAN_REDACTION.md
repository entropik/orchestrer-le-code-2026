# Plan de rédaction par chapitre

## Unité de travail

Une tranche = une lecture d'un chapitre. Une paire = Axx + Bxx sur le même sujet. Les fiches sont des missions locales prêtes à utiliser, pas des issues déjà créées sur GitHub.

Ordre conseillé : traiter A01 puis B01, harmoniser la paire, poursuivre avec A02 puis B02. L'ordre de lecture publié reste A01 à A12, puis B01 à B12. Une passe finale relit chaque partie indépendamment pour vérifier qu'elle se suffit à elle-même.

## File des 24 tranches

| Tranche | Lecture | Mission | Prérequis | État initial |
|---|---|---|---|---|
| A01 | accessible | [Piloter un système, pas une génération de code](../tranches/A01-piloter-un-systeme.md) | aucun | amorce |
| A02 | accessible | [Organiser l'architecture et les responsabilités](../tranches/A02-architecture-et-frontieres.md) | A01 | amorce |
| A03 | accessible | [Transformer le besoin en contrat vérifiable](../tranches/A03-besoin-et-contrats.md) | A02 | amorce |
| A04 | accessible | [Donner du contexte et des limites à l'agent](../tranches/A04-harnais-et-contexte.md) | A03 | amorce |
| A05 | accessible | [Garder une histoire fiable avec Git](../tranches/A05-git-et-collaboration.md) | A04 | amorce |
| A06 | accessible | [Demander des preuves, pas seulement du code](../tranches/A06-tests-et-preuves.md) | A05 | amorce |
| A07 | accessible | [Faire travailler le système sans perdre les opérations](../tranches/A07-asynchronisme-et-reprises.md) | A06 | amorce |
| A08 | accessible | [Protéger les données et faire évoluer leur structure](../tranches/A08-donnees-et-migrations.md) | A07 | amorce |
| A09 | accessible | [Passer du poste local à un service réel](../tranches/A09-livraison-et-production.md) | A08 | amorce |
| A10 | accessible | [Observer, améliorer et rétablir le service](../tranches/A10-exploitation-et-evolution.md) | A09 | amorce |
| A11 | accessible | [Appliquer ORCHESTRE du besoin à la résolution](../tranches/A11-methode-et-cas-pratiques.md) | A10 | amorce |
| A12 | accessible | [Choisir ses outils et préserver son indépendance](../tranches/A12-ecosysteme-et-independance.md) | A11 | amorce |
| B01 | ingenieure | [Piloter un système, pas une génération de code](../tranches/B01-piloter-un-systeme.md) | A01 | amorce |
| B02 | ingenieure | [Organiser l'architecture et les responsabilités](../tranches/B02-architecture-et-frontieres.md) | A02, B01 | amorce |
| B03 | ingenieure | [Transformer le besoin en contrat vérifiable](../tranches/B03-besoin-et-contrats.md) | A03, B02 | amorce |
| B04 | ingenieure | [Donner du contexte et des limites à l'agent](../tranches/B04-harnais-et-contexte.md) | A04, B03 | amorce |
| B05 | ingenieure | [Garder une histoire fiable avec Git](../tranches/B05-git-et-collaboration.md) | A05, B04 | amorce |
| B06 | ingenieure | [Demander des preuves, pas seulement du code](../tranches/B06-tests-et-preuves.md) | A06, B05 | amorce |
| B07 | ingenieure | [Faire travailler le système sans perdre les opérations](../tranches/B07-asynchronisme-et-reprises.md) | A07, B06 | amorce |
| B08 | ingenieure | [Protéger les données et faire évoluer leur structure](../tranches/B08-donnees-et-migrations.md) | A08, B07 | amorce |
| B09 | ingenieure | [Passer du poste local à un service réel](../tranches/B09-livraison-et-production.md) | A09, B08 | amorce |
| B10 | ingenieure | [Observer, améliorer et rétablir le service](../tranches/B10-exploitation-et-evolution.md) | A10, B09 | amorce |
| B11 | ingenieure | [Appliquer ORCHESTRE du besoin à la résolution](../tranches/B11-methode-et-cas-pratiques.md) | A11, B10 | amorce |
| B12 | ingenieure | [Choisir ses outils et préserver son indépendance](../tranches/B12-ecosysteme-et-independance.md) | A12, B11 | amorce |

## Jalons

1. Paire pilote A01/B01 : valider le ton et la différence de profondeur avant extension.
2. Paires 02 à 06 : concevoir, encadrer et vérifier.
3. Paires 07 à 10 : maîtriser données, opérations et exploitation.
4. Paires 11 et 12 : relier la méthode aux cas complets et aux choix d'écosystème.
5. Relecture transversale : cohérence des termes et des exemples, tests des extraits de code, vérification des références et droits de diffusion.
6. Édition finale : relecture humaine des deux parcours ; mise en page PDF/EPUB éventuelle dans une tâche dédiée.

## États

`amorce` → `redaction` → `relecture` → `valide`. Le manifeste [chapitres.json](chapitres.json) est la source de vérité. Un chapitre n'est validé qu'après satisfaction de la fiche ; un build réussi ne valide pas son contenu technique.

## Charge éditoriale indicative

12 chapitres accessibles de 1 200 à 1 800 mots et 12 approfondis généralement de 2 500 à 4 000 mots, avec marge pour les cas et l'exploitation. Ordre de grandeur : 45 000 à 72 000 mots hors annexes. C'est une cible de planification, ni un décompte du contenu livré ni un engagement de délai.
