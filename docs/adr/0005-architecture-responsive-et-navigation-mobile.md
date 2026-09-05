# ADR 0005 : Architecture responsive, en-tête mobile et mini-sommaire interactif

- **Statut** : Accepté
- **Date** : 2026-09-05
- **Contexte** : L'expérience mobile du site présentait plusieurs limites ergonomiques :
  1. Le bandeau de navigation d'en-tête s'enroulait sous le logo sur plusieurs lignes, encombrant la partie supérieure de l'écran.
  2. La colonne latérale de navigation (`.reader-sidebar`) était intégralement masquée sur mobile (`display: none`), privant le lecteur sur smartphone de la liste des chapitres du parcours et du sommaire de page.
  3. Les échelles de taille des titres H1/H2 étaient trop volumineuses pour les petits écrans (320px–480px), provoquant des retours à la ligne abrupts et un déséquilibre optique.

## Décision

Nous refondons l'expérience responsive autour de 4 piliers d'ingénierie et d'accessibilité :

1. **En-tête mobile & Menu Hamburger accessible** :
   - Sur écrans ≤ 960px, le bandeau de liens est remplacé par un en-tête épuré et collant (`position: sticky`), doté d'un bouton déclencheur tactile conforme aux standards d'accessibilité (cible ≥ 44×44px, attributs `aria-expanded` et `aria-controls`).
   - Utilisation des icônes vectorielles Lucide `menu` et `x`.
   - Script léger (`assets/js/nav.js`) gérant l'ouverture, la fermeture au clic extérieur, la touche `Échap`, et la fermeture lors d'une navigation.
   - Préservation stricte de la barre de navigation inline sur desktop (> 960px).
2. **Mini-sommaire mobile interactif en tête d'article** :
   - Remplacement de la perte d'information par un composant rétractable natif (`.mobile-reader-menu` via `<details>` accessible).
   - Donne un accès direct, pliable et tactile à l'ensemble des 12 chapitres de la lecture active (« Accessible » ou « Ingénieure ») ainsi qu'aux sections de la page (`#MobileTableOfContents`).
   - Mise en surbrillance nette du chapitre en cours de lecture.
3. **Typographie fluide & Calibrage de lecture mobile** :
   - Titres H1, H2, H3 et chapitres dimensionnés avec des fonctions fluides `clamp()`.
   - Corps de texte (`.prose`) calibré entre 1.06rem et 1.18rem avec interlignage 1.65 pour un confort de lecture prolongée sur smartphone.
   - Blocs de code (`pre` / `code`) conteneurisés avec défilement tactile propre sans jamais déborder de la largeur d'écran.
   - Sécurisation du `body` avec `overflow-x: clip` pour supprimer tout défilement horizontal résiduel sans altérer le positionnement sticky de l'en-tête.
4. **Composants denses & Simulateur d'aiguillage** :
   - Grille du simulateur sur `/annexes/` adaptée en pile fluide, commande et bouton de copie avec cibles tactiles élargies, pipeline ordonné en étapes verticales compactes.
   - Matrice des chapitres de la page d'accueil avec choix de lecture adaptés au doigt.

## Conséquences

- **Lisibilité mobile irréprochable** : Le manuel offre un confort de lecture équivalent aux meilleures publications numériques.
- **Autonomie de parcours** : Le lecteur mobile peut changer de chapitre à tout moment sans faire défiler jusqu'au pied de page.
- **Zéro surcharge réseau** : Zéro bibliothèque CSS externe, un script vanilla de 1 KB compilé par Hugo, 100 % hors réseau et compatible avec les contrôles stricts de `verifier_html.py`.
