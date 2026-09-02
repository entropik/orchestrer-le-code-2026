{
  "title": "Plan des 24 tranches",
  "source_path": "editorial/PLAN_REDACTION.md"
}

## Partie zéro — socle commun

| ID | Étape | Statut |
|---|---|---|
| P01 | Faire exécuter un programme | rédaction |
| P02 | Transformer des données avec des règles | rédaction |
| P03 | Lire, découper et modifier sans se perdre | rédaction |
| P04 | Enquêter et demander des preuves | rédaction |
| P05 | Passer à TypeScript et diriger une mission complète | rédaction |

Ces cinq unités partagent le [projet exécutable](/commencer) et précèdent les lectures miroirs. Elles ne changent pas le compte des 24 tranches A/B.

## Unité de travail

Une tranche = une lecture d'un chapitre. Une paire = Axx + Bxx sur le même sujet. Les fiches sont des missions locales prêtes à utiliser, pas des issues déjà créées sur GitHub.

Ordre conseillé : traiter A01 puis B01, harmoniser la paire, poursuivre avec A02 puis B02. L'ordre de lecture publié reste A01 à A12, puis B01 à B12. Une passe finale relit chaque partie indépendamment pour vérifier qu'elle se suffit à elle-même.

## File des 24 tranches

| Tranche | Lecture | Mission | Prérequis | État initial |
|---|---|---|---|---|
| A01 | accessible | [Piloter un système, pas une génération de code](/redaction/a01-piloter-un-systeme) | aucun | amorce |
| A02 | accessible | [Organiser l'architecture et les responsabilités](/redaction/a02-architecture-et-frontieres) | A01 | amorce |
| A03 | accessible | [Transformer le besoin en contrat vérifiable](/redaction/a03-besoin-et-contrats) | A02 | amorce |
| A04 | accessible | [Donner du contexte et des limites à l'agent](/redaction/a04-harnais-et-contexte) | A03 | amorce |
| A05 | accessible | [Garder une histoire fiable avec Git](/redaction/a05-git-et-collaboration) | A04 | amorce |
| A06 | accessible | [Demander des preuves, pas seulement du code](/redaction/a06-tests-et-preuves) | A05 | amorce |
| A07 | accessible | [Faire travailler le système sans perdre les opérations](/redaction/a07-asynchronisme-et-reprises) | A06 | amorce |
| A08 | accessible | [Protéger les données et faire évoluer leur structure](/redaction/a08-donnees-et-migrations) | A07 | amorce |
| A09 | accessible | [Passer du poste local à un service réel](/redaction/a09-livraison-et-production) | A08 | amorce |
| A10 | accessible | [Observer, améliorer et rétablir le service](/redaction/a10-exploitation-et-evolution) | A09 | amorce |
| A11 | accessible | [Appliquer ORCHESTRE du besoin à la résolution](/redaction/a11-methode-et-cas-pratiques) | A10 | amorce |
| A12 | accessible | [Choisir ses outils et préserver son indépendance](/redaction/a12-ecosysteme-et-independance) | A11 | amorce |
| B01 | ingenieure | [Piloter un système, pas une génération de code](/redaction/b01-piloter-un-systeme) | A01 | amorce |
| B02 | ingenieure | [Organiser l'architecture et les responsabilités](/redaction/b02-architecture-et-frontieres) | A02, B01 | amorce |
| B03 | ingenieure | [Transformer le besoin en contrat vérifiable](/redaction/b03-besoin-et-contrats) | A03, B02 | amorce |
| B04 | ingenieure | [Donner du contexte et des limites à l'agent](/redaction/b04-harnais-et-contexte) | A04, B03 | amorce |
| B05 | ingenieure | [Garder une histoire fiable avec Git](/redaction/b05-git-et-collaboration) | A05, B04 | amorce |
| B06 | ingenieure | [Demander des preuves, pas seulement du code](/redaction/b06-tests-et-preuves) | A06, B05 | amorce |
| B07 | ingenieure | [Faire travailler le système sans perdre les opérations](/redaction/b07-asynchronisme-et-reprises) | A07, B06 | amorce |
| B08 | ingenieure | [Protéger les données et faire évoluer leur structure](/redaction/b08-donnees-et-migrations) | A08, B07 | amorce |
| B09 | ingenieure | [Passer du poste local à un service réel](/redaction/b09-livraison-et-production) | A09, B08 | amorce |
| B10 | ingenieure | [Observer, améliorer et rétablir le service](/redaction/b10-exploitation-et-evolution) | A10, B09 | amorce |
| B11 | ingenieure | [Appliquer ORCHESTRE du besoin à la résolution](/redaction/b11-methode-et-cas-pratiques) | A11, B10 | amorce |
| B12 | ingenieure | [Choisir ses outils et préserver son indépendance](/redaction/b12-ecosysteme-et-independance) | A12, B11 | amorce |

## Jalons

1. Paire pilote A01/B01 : valider le ton et la différence de profondeur avant extension.
2. Paires 02 à 06 : concevoir, encadrer et vérifier.
3. Paires 07 à 10 : maîtriser données, opérations et exploitation.
4. Paires 11 et 12 : relier la méthode aux cas complets et aux choix d'écosystème.
5. Relecture transversale : cohérence des termes et des exemples, tests des extraits de code, vérification des références et droits de diffusion.
6. Édition finale : relecture humaine des deux parcours ; mise en page PDF/EPUB éventuelle dans une tâche dédiée.

## États

`amorce` → `redaction` → `relecture` → `valide`. Le manifeste [/redaction/plan](/redaction/plan) est la source de vérité. Un chapitre n'est validé qu'après satisfaction de la fiche ; un build réussi ne valide pas son contenu technique.

## Charge éditoriale indicative

12 chapitres accessibles de 1 200 à 1 800 mots et 12 approfondis généralement de 2 500 à 4 000 mots, avec marge pour les cas et l'exploitation. Ordre de grandeur : 45 000 à 72 000 mots hors annexes. C'est une cible de planification, ni un décompte du contenu livré ni un engagement de délai.
