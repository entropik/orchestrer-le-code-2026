# ADR 0003 : Système iconographique Lucide et proscription des émojis système

- **Statut** : Accepté
- **Date** : 2026-09-04
- **Contexte** : L'interface du simulateur interactif d'aiguillage (`/annexes/`) et les boutons de copie du catalogue de compétences utilisaient initialement des émojis système Unicode (🎯, 🐞, 📥, 🌫️, 🛑, 👥, 🔐, 🔀, 🔗). Ce rendu hétérogène et bariolé, variable selon les systèmes d'exploitation (macOS, Windows, Linux, mobile), entrait en contradiction directe avec la charte graphique et la sobriété typographique du manuel (Tufte, Georgia, palette naturelle papier/encre/forêt).

## Décision

Nous adoptons **Lucide Icons** comme standard unique et exclusif d'iconographie pour l'ensemble du projet :

1. **Architecture Zero-Runtime** : Les icônes sont stockées localement au format SVG vectoriel sous `assets/icons/<name>.svg`. Aucune dépendance applicative lourde, aucune police d'icône et aucun appel CDN tiers ne sont ajoutés en production.
2. **Injection Hugo Native** :
   - Dans les templates et shortcodes HTML : `{{ partial "icon.html" (dict "name" "target" "class" "btn-icon") }}`.
   - Dans les fichiers Markdown : `{{< icon "link-2" >}}`.
   - Les SVG sont injectés directement dans l'arbre DOM au moment de la compilation Hugo (`hugo --minify`), garantissant un affichage instantané sans décalage de mise en page (CLS = 0).
3. **Contrôle Typographique & CSS** : Les icônes utilisent `stroke="currentColor"` et héritent des variables de couleur du livre (`var(--ink)`, `var(--muted)`, `var(--accent)`), avec une épaisseur de trait harmonisée (1.75 à 2px).
4. **Règle formelle de conception** : Les émojis système Unicode sont formellement proscrits des interfaces interactives, des boutons d'action et des fiches documentaires du site.

## Options Considérées

- **Conserver les émojis système Unicode** : Rejeté. Rendu visuel disparate, enfantin, impossible à styliser via CSS et non aligné sur l'exigence de design du livre.
- **Charger une bibliothèque cliente JavaScript (Lucide JS via CDN ou bundle dynamique)** : Rejeté pour respecter l'invariant de sobriété technique du projet et les exigences de contrôle hors réseau (`python scripts/verifier_html.py public`).
- **Phosphor Icons ou Heroicons** : Rejetés au profit de Lucide dont le vocabulaire pour les concepts de développement logiciel (`git-merge`, `terminal`, `bug`, `cloud-fog`, `inbox`, `shield-alert`, `key-round`) est le plus cohérent et complet.

## Conséquences

- **Pureté et élégance visuelle** : L'interface gagne une allure professionnelle, épurée et strictement alignée sur le design éditorial.
- **Zéro surcharge réseau** : 0 KB de JavaScript additionnel pour les icônes, vérification hors réseau intacte.
- **Mémoire pérenne du projet** : Tout contributeur ou agent travaillant sur le dépôt doit utiliser `assets/icons/` et `icon.html` pour tout nouveau besoin d'icône, en s'interdisant tout émoji.
