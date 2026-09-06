{
  "title": "Charte éditoriale & Droits",
  "source_path": "editorial/CHARTE.md",
  "aliases": [
    "/projet/droits"
  ]
}

## 1. Intention éditoriale

Permettre à un décideur ou créateur autonome de piloter la fabrication d'un logiciel avec des agents, puis d'accéder aux mécanismes d'ingénierie qui justifient ses décisions. Le manuel n'est ni une collection de prompts magiques ni la défense commerciale d'un fournisseur ou d'un écosystème fermé.

## 2. Deux lectures pour chaque chapitre

La partie I contient A01 à A12 ; la partie II, B01 à B12. Chaque paire Axx et Bxx porte sur le même sujet, dans le même ordre et avec le même fil rouge applicatif. La première lecture ne réserve pas sa conclusion à la seconde : elle donne les clés pour décider. La seconde rappelle brièvement le problème pour être lisible indépendamment, puis approfondit les mécanismes, les limites et les preuves.

| Accessible (Partie I) | Ingénieure (Partie II) |
|---|---|
| Comprendre le problème et choisir une action. | Expliquer les mécanismes, concevoir et vérifier. |
| Situations concrètes et mots expliqués au premier usage. | Contrats, états, limites, modes de panne et preuves. |
| Peu de code ; exemples lisibles sans langage particulier. | Extraits exécutables lorsque utiles, environnement et versions précisés. |
| Questions à poser et signaux d'alerte. | Compromis, tests, contre-exemples et procédures de reprise. |
| Exercice de décision avec corrigé. | Exercice de conception ou de diagnostic avec corrigé. |

## 3. Ton & Style

- **Le tutoiement** : clair, direct, précis et non condescendant.
- **Expliquer avant de nommer** : démystifier le concept avant d'introduire le jargon.
- **Interdiction des arguments d'autorité creux** : ne jamais remplacer une justification par « industriel », « absolu », « souverain » ou « déterministe ».
- **La juste place de l'image** : une métaphore aide à comprendre mais ne constitue jamais un théorème de preuve.

## 4. Modèle canonique de chapitre

Chaque chapitre final s'articule autour d'une structure rigoureuse :  
Situation concrète → Objectif d'action → Raisonnement & invariants → Exemple du fil rouge → Limites et erreurs fréquentes → Exercice pratique → Corrigé commenté → Checklist réflexe → Sources et renvoi miroir.

## 5. Règles de preuve & Rigueur technique

- **Distinguer le statut des affirmations** : séparer clairement constat dans les sources, synthèse éditoriale et validation externe.
- **Traçabilité des sources** : indiquer le chapitre ou la section source ; préférer les textes Markdown natifs aux extractions PDF pour les détails fins.
- **Dater les éléments variables** : versions logicielles, licences, API, prix, capacités des modèles et compatibilité.
- **Aucune complaisance technique** : une configuration copiée d'une source n'est pas réputée testée sans exécution réelle.
- **Refus des illusions** : ne jamais promettre sécurité totale, absence de panne ou correction universelle par l'IA.
- **Volatilité des modèles** : les noms de modèles et de bibliothèques sont des exemples à vérifier, pas un classement permanent.

## 6. Colophon de fabrication : le harnais de l'artisan

Ce manuel et son site web ne sont pas le produit d'un chatbot solitaire interrogé au fil de l'eau, mais d'un atelier logiciel orchestré selon les principes mêmes enseignés dans ces pages (*dogfooding* intégral). La chaîne de production combine quatre couches complémentaires :

1. **L'environnement de développement agentique (ADE)** : **Orca**. Les agents s'exécutent en parallèle, chacun dans un Git worktree strictement cloisonné doté de son propre terminal et d'un navigateur d'inspection dédié. Cette isolation garantit l'absence totale de collisions sur l'arbre Git et permet d'explorer des hypothèses concurrentes sans pollution du tronc principal.
2. **Le tandem des modèles d'inférence** :
   - **Google Gemini** : mobilisé pour la maïeutique, l'analyse synoptique du corpus volumineux, la cohérence trans-chapitres et la dialectique contradictoire.
   - **OpenAI Codex** : sollicité pour la précision syntaxique, l'implémentation fine des algorithmes de transposition, les scripts déterministes et la génération de tests unitaires rigoureux.
3. **La gouvernance et les compétences de Matt Pocock** : Le harnais de pilotage applique la doctrine en trois couches (réflexes universels d'aiguillage, compétences locales de dépôt sous `.agents/skills/` telles que `writing-for-agents`, `diagnosing-bugs`, `tdd`, `code-review`, `domain-modeling`, et mémoire vive persistante via `AGENTS.md`).
4. **La chaîne de compilation et les oracles déterministes** :
   - Génération de contenu Hugo sans dépendance externe tierce (`python3.11`).
   - Moteur de rendu typographique respectant les normes de l'Imprimerie nationale (espaces insécables, anti-solitaires, ligatures).
   - Validation géométrique intégrale des schémas ASCII déterministes transposés en planches vectorielles responsive (`tests/test_hugo.py`).
   - Compilation statique stricte avec Hugo étendu (`--panicOnWarning`), audit de tous les hyperliens internes (`scripts/verifier_html.py`), et distribution mondiale sur Cloudflare Pages à latence minimale, sans traceurs ni cookies.

## 7. Droits d'auteur, Licences & Protection des Contenus

### Titulaire des droits et propriété intellectuelle

L'ouvrage ***Orchestrer le code en 2026*** (textes, structure pédagogique, architectures conceptuelles et illustrations) est une œuvre de l'esprit originale créée par :

**Marc Tallec**  
© 2026 Marc Tallec. Tous droits réservés pour l'édition imprimée et les exploitations commerciales.  
Site officiel de publication et de référence : [https://savoirs.keredit.com/](https://savoirs.keredit.com/).

---

### Licence de diffusion du contenu textuel : CC BY-NC-ND 4.0

Pour sa diffusion numérique en libre accès, le contenu textuel et pédagogique de ce manuel est mis à disposition du public sous les termes de la licence internationale **Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International (CC BY-NC-ND 4.0)**.

- **Attribution (BY)** : Vous devez obligatoirement créditer l'auteur (**Marc Tallec**), intégrer un lien direct vers l'œuvre originale ([https://savoirs.keredit.com/](https://savoirs.keredit.com/)) et indiquer si des citations ont été faites.
- **Pas d'Utilisation Commerciale (NC)** : Vous n'êtes pas autorisé à faire un usage commercial de cette œuvre, directement ou indirectement (vente d'e-books, inclusion dans une formation ou publication payante, diffusion sous paywall, monétisation publicitaire exclusive).
- **Pas de Modification (ND)** : Si vous remixez, transformez, tronquez ou adaptez le texte pour créer une œuvre dérivée, vous n'êtes pas autorisé à distribuer l'œuvre modifiée sans l'accord écrit exprès de l'auteur.

Texte officiel de la licence : [Creative Commons CC BY-NC-ND 4.0 Legal Code](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.fr).

---

### Exception pour le code source et les exemples exécutables : Licence MIT

Les extraits de code source exécutable (scripts Python 3.11, schémas de données SQL, configurations Docker et prototypes de test) conçus et présentés dans la **Partie II (Lecture Ingénieure)** sont mis à disposition sous licence **MIT**.

Les lecteurs et développeurs sont libres de réutiliser, copier et adapter ces blocs de code technique dans leurs propres logiciels personnels ou commerciaux, sous réserve de conserver la notice de copyright technique.

---

### Réserve expresse contre la fouille de données et l'entraînement d'IA (Opt-Out TDM)

Conformément aux dispositions de la **Directive européenne (UE) 2019/790** du Parlement européen et du Conseil du 17 avril 2019 sur le droit d'auteur et les droits voisins dans le marché unique numérique, et à sa transposition dans le droit français à l'**article L. 122-5-3 du Code de la propriété intellectuelle** :

> **Marc Tallec s'oppose expressément et formellement à toute utilisation, reproduction, extraction, moissonnage ou fouille automatisée de textes et de données (*Text and Data Mining*) portant sur les contenus, chapitres, sources et métadonnées de cet ouvrage, à des fins d'entraînement, d'ajustement (*fine-tuning*), d'évaluation ou d'alimentation de modèles d'intelligence artificielle ou d'apprentissage automatique (*Machine Learning*).**

Cette opposition est exprimée par les présentes mentions légales ainsi que par des moyens lisibles par machine :
- Directives d'interdiction dans le fichier standard `robots.txt` ciblant spécifiquement les robots d'indexation et d'aspiration d'intelligence artificielle.
- Balises méta conformes aux standards de l'industrie : `<meta name="robots" content="noai, noimageai">`.
- Protocole de réservation TDMRep W3C : `<meta name="tdm-reservation" content="1">`.

Tout acte d'aspiration ou d'incorporation non autorisé dans un jeu de données d'entraînement constitue une contrefaçon passible des sanctions civiles et pénales prévues par le Code de la propriété intellectuelle.

---

### Demandes d'autorisations spéciales

Pour toute demande d'adaptation, de traduction étrangère, d'exploitation commerciale, d'ateliers professionnels ou de droits d'édition papier, vous pouvez contacter directement l'auteur :

- **Auteur** : Marc Tallec  
- **Éditeur** : Keredit Éditions / Savoirs ([https://savoirs.keredit.com/](https://savoirs.keredit.com/))
