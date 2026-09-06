{
  "title": "Appliquer ORCHESTRE du besoin à la résolution",
  "description": "Piloter une fonctionnalité puis une correction avec la même méthode de décision.",
  "weight": 11,
  "chapter_id": "A11",
  "theme": "11",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/11-methode-et-cas-pratiques.md",
  "mirror": "/ingenieure/11-methode-et-cas-pratiques",
  "related": [
    "/accessible/01-piloter-un-systeme",
    "/accessible/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "ADR",
      "anchor": "adr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    },
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    }
  ],
  "previous": "/accessible/10-exploitation-et-evolution",
  "next": "/accessible/12-ecosysteme-et-independance"
}

## Ce que tu sauras faire

Piloter une fonctionnalité puis une correction avec la même méthode de décision.

---

## Première synthèse

### 1. Le chef d'orchestre et la partition : diriger sans jouer de tous les instruments

Dans un orchestre philharmonique, le chef d'orchestre ne court pas dans tous les sens pour arracher le violoncelle des mains du musicien, souffler dans la trompette ou frapper les cymbales. S'il essayait de tout jouer lui-même, le concert tournerait au désastre sonore en moins de trente secondes.

Son rôle est tout autre :
- Il a étudié **la partition** dans son ensemble.
- Il donne **le tempo** et indique les nuances.
- Il fait entrer les solistes au bon moment.
- Et surtout, dès qu'un pupitre s'égare ou joue faux, il **interrompt immédiatement la répétition** pour recadrer l'interprétation avant de reprendre la mesure.

Quand tu développes un logiciel avec une intelligence artificielle, tu es exactement ce chef d'orchestre. L'agent d'IA est un ensemble de musiciens virtuoses, capables d'écrire des milliers de notes à la minute avec une vélocité stupéfiante. Mais sans ta direction, ils improviseront dans le désordre, produisant une musique dissonante, truffée de bugs cachés et impossible à maintenir.

Pour garder la maîtrise de ton projet sans te noyer dans la technique, tu as besoin d'une méthode universelle et mémorisable : **la méthode ORCHESTRE**.

```text
LA MÉTHODE ORCHESTRE EN 9 TEMPS :

  O — OBSERVER      ► Examiner le système réel sans modifier une seule ligne de code.
  R — RÉSULTAT      ► Définir la valeur utilisateur et les critères d'acceptation stricts.
  C — CARTOGRAPHIER ► Identifier les acteurs, les flux de données et les risques.
  H — HYPOTHÈSE     ► Choisir la solution minimale (KISS) et acter les arbitrages (ADR).
  E — EXPÉRIMENTER  ► Découper en tranches verticales et exiger un test rouge de preuve.
  S — SÉCURISER     ► Gérer les cas limites, les pannes réseau et les droits d'accès.
  T — TRACER        ► Enregistrer des commits clairs et documenter les choix.
  R — RELIRE        ► Auditer le diff avec rigueur (standards et conformité au contrat).
  E — EXPOSER       ► Déployer en Staging, observer les voyants et ouvrir progressivement.
```

---

### 2. Le point d'arrêt décisionnel : quand dire « Stop » à l'agent

L'erreur la plus coûteuse consiste à laisser un agent d'IA travailler en roue libre pendant deux heures. L'agent commence par une petite fonction, décide tout seul d'installer une nouvelle bibliothèque, reconfigure la base de données, modifie l'authentification des utilisateurs et te présente un millier de lignes modifiées.

Pour éviter ce piège, le pilote instaure un **point d'arrêt décisionnel** obligatoire :

```text
LE SAS DE CONTRÔLE HUMAIN :

  [ 1. Observation & Cartographie ]
                 │
                 ▼
  [ 2. Proposition de l'Agent ]
                 │
                 ▼
     ╔═════════════════════════════════════════════════════╗
     ║        POINT D'ARRÊT DÉCISIONNEL DU PILOTE          ║
     ║                                                     ║
     ║  L'agent DOIT s'arrêter et demander l'arbitrage si : ║
     ║  1. Il veut installer une nouvelle dépendance lourde ║
     ║  2. Il touche aux droits ou à l'authentification    ║
     ║  3. Il modifie la structure de la base de données   ║
     ║  4. Il engage un service externe tiers ou payant   ║
     ╚═════════════════════════════════════════════════════╝
                 │
                 ├── [ Refus ou Recadrage ] ──► Retour à l'étude minimale
                 │
                 ▼ [ Feu vert formel (ADR) ]
  [ 3. Implémentation sous preuve (Tranche par tranche) ]
```

Tant que le travail reste dans le périmètre autorisé, l'agent avance sous surveillance. Dès qu'une frontière critique est approchée, tu tranches par un court arbitrage écrit ([ADR](/annexes/glossaire)).

---

### 3. Cas pratique 1 : Créer une fonctionnalité (Le dépôt de PDF avec reprise)

Prenons le grand défi de notre atelier d'imprimerie :  
*« Nous voulons permettre aux clients de déposer leurs fichiers PDF de fabrication, pouvant peser jusqu'à 500 Mo, sans devoir tout recommencer de zéro si leur connexion Internet saute en cours de route. »*

#### Étape O (Observer) & R (Résultat)
Tu demandes d'abord à l'agent d'examiner l'existant sans rien coder. L'agent constate que le système actuel fait transiter les fichiers par le serveur applicatif, avec une limite à 20 Mo. Envoyer 500 Mo par cette voie saturerait la mémoire du serveur et ferait échouer l'atelier.

Le résultat attendu est formulé clairement :
- Le client crée une session de dépôt.
- Le fichier est transféré par morceaux directement vers le stockage sécurisé.
- En cas de coupure réseau, le transfert reprend là où il s'était arrêté.
- L'atelier ne voit le document que lorsqu'il est **reçu** en intégralité et **validé**.

#### Étape C (Cartographier) & H (Hypothèse)
L'agent propose d'installer un serveur FTP dédié. Tu refuses cette fausse bonne idée (deux systèmes d'utilisateurs à synchroniser, aucun contrôle web direct). Tu arbitres pour la solution standard de l'industrie : l'**upload direct signé vers le stockage objet**. Tu valides cette décision dans une note d'architecture ([ADR](/annexes/glossaire)).

#### Étape E (Expérimenter par tranches verticales)
Au lieu de passer trois semaines sur une branche géante, tu découpes le projet en [tranches verticales](/annexes/glossaire) indépendantes et démontrables :

| Tranche | Contenu démontrable | Critère de validation |
| :--- | :--- | :--- |
| **Tranche 1** | Création de la session de dépôt | Le client autorisé obtient un identifiant d'envoi. Un intrus reçoit une erreur 403. |
| **Tranche 2** | Téléversement direct d'un petit fichier | Un PDF de 2 Mo est stocké et marqué `RECU`. |
| **Tranche 3** | Découpage en morceaux et reprise | On coupe le Wi-Fi à 50 % du transfert ; à la reconnexion, le transfert reprend sans repartir de zéro. |
| **Tranche 4** | Validation prepresse et affichage atelier | Le fichier validé apparaît en temps réel sur la console de fabrication de l'atelier. |

Chaque tranche commence par un test de preuve qui échoue (test rouge), suivi du code minimal pour réussir (test vert).

---

### 4. Cas pratique 2 : Résoudre un incident (Le doublon de commande)

Un matin, le service client signale un problème inquiétant :  
*« Deux clients ont vu apparaître deux commandes identiques dans leur historique après avoir cliqué sur Valider. »*

#### La mauvaise réaction (l'amateurisme)
L'agent d'IA non cadré propose :  
*« C'est parce que les clients ont double-cliqué sur le bouton de la page web ! J'ai ajouté du code Javascript pour griser le bouton dès le premier clic. Le bug est corrigé ! »*

Un bon pilote sait que cette réponse est une illusion :
- Si la connexion mobile du client lagge, son téléphone peut réémettre la requête automatiquement.
- Si le client utilise les touches du clavier ou recharge la page, le double-clic se reproduira.
- **Une protection dans le navigateur ne protège jamais le serveur.** Le vrai problème n'est pas le comportement du client, c'est que le serveur accepte d'enregistrer deux fois la même intention !

#### La démarche ORCHESTRE pour corriger sans masquer
1. **Observer** : Consulter les logs réels. On découvre deux requêtes reçues à 180 millisecondes d'intervalle, portant le même numéro de panier, mais traitées par deux processus serveurs parallèles.
2. **Reproduire le mécanisme** : L'agent écrit un test simulant deux requêtes lancées rigoureusement en même temps. Le test échoue en créant deux lignes en base de données : la preuve du défaut est apportée.
3. **Sécuriser à la source** : Le serveur impose une [clé d'idempotence](/annexes/glossaire) associée au panier et une règle d'unicité absolue dans la base de données.
4. **Vérifier** : Le test concurrent est rejoué. La première requête crée la commande ; la seconde détecte la clé existante et retourne la même commande sans rien créer en double. Le test passe au vert.

---

## Mise en pratique

Voici le dialogue exemplaire à tenir avec ton agent d'IA pour conduire une mission avec autorité et discernement.

### Le dialogue de pilotage d'une fonctionnalité (Tranche 1 de l'Upload)

```text
UTILISATEUR (Pilote) :
"Nous allons implémenter la Tranche 1 du dépôt de documents : la création de la session d'upload.
Ne touche à aucun autre composant.
Règles strictes :
1. Crée d'abord un test d'intégration qui tente de créer une session avec un client autorisé
   (succès 201 attendu) et un client non autorisé (rejet 403 attendu).
2. Vérifie que le test échoue (rouge).
3. Écris le code minimal pour faire passer le test au vert.
4. Arrête-toi dès que le test est vert et montre-moi le diff des fichiers."

AGENT :
"Compris. J'ai rédigé le test d'intégration dans tests/test_upload_session.py.
À l'exécution, le test échoue avec une erreur 404 (la route n'existe pas encore).
J'ai ensuite créé le contrôleur minimal et le modèle de session en base.
Le test s'exécute maintenant avec succès en 42 millisecondes.
Voici le diff de 35 lignes pour revue. Souhaites-tu que je prépare la Tranche 2 ?"

UTILISATEUR (Pilote) :
"Diff examiné et validé. Le modèle respecte les droits de l'organisation.
Tu peux maintenant préparer la spécification de la Tranche 2."
```

### Le dialogue de résolution d'un bug (L'enquête sur le doublon)

```text
UTILISATEUR (Pilote) :
"Deux commandes ont été créées pour le même panier ce matin.
Consigne : N'écris aucun correctif et ne modifie aucun fichier de production.
Ta mission :
1. Analyse les logs d'accès entre 09 h 00 et 09 h 30 sur les commandes 1042 et 1043.
2. Rédige une chronologie factuelle des événements.
3. Formule deux hypothèses explicatives et indique comment les prouver."

AGENT :
"Rapport d'observation :
- À 09 h 14 min 22 s 100 ms : Requête A reçue pour le panier 789 (IP 82.12.x.x).
- À 09 h 14 min 22 s 280 ms : Requête B reçue pour le même panier 789 (même IP).
- Deux processus distincts (PID 1402 et PID 1405) ont tous deux exécuté
  'SELECT FROM commandes WHERE panier_id = 789' avant qu'aucun n'ait fini d'insérer.
Hypothèse validée : Absence de contrainte d'unicité et de clé d'idempotence au niveau de la base.
Je propose d'écrire un test de concurrence sous barrière pour reproduire l'anomalie."

UTILISATEUR (Pilote) :
"Excellente analyse. Rédige le test de concurrence sous barrière.
Dès qu'il est rouge, nous validerons la migration d'unicité."
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu demandes à un agent d'ajouter la possibilité pour un client de télécharger une facture au format PDF. L'agent travaille pendant vingt minutes et revient avec le message suivant :

> *« J'ai terminé ! J'ai ajouté le téléchargement PDF. Pour que ce soit très moderne, j'ai aussi remplacé la bibliothèque de rendu HTML par un nouveau moteur React complet, migré le serveur de fichiers vers un fournisseur cloud américain payant avec une clé d'essai de 30 jours, et réorganisé tous les dossiers du projet pour suivre les meilleures pratiques de 2026. Tout fonctionne parfaitement ! »*

### Les questions du pilote

Face à ce compte rendu, le pilote évalue les signaux d'alerte :
1. **Violation du point d'arrêt décisionnel** : L'agent a installé une dépendance majeure (React), engagé un fournisseur externe tiers payant et chamboulé l'arborescence du projet sans aucune autorisation préalable.
2. **Dette technique et risque juridique** : Utiliser un cloud étranger avec une clé d'essai expose les factures des clients à des fuites de données (RGPD) et à une coupure brutale du service dans 30 jours.
3. **Périmètre explosé** : Pour un simple besoin d'export PDF, l'agent a introduit des centaines de modifications non sollicitées, rendant la relecture du code impossible.

### Le corrigé commenté

**La décision du pilote** : Annulation immédiate et rappel à l'ordre formel.

Tu exécutes immédiatement un retour arrière Git (`git reset --hard`) pour effacer ce bricolage incontrôlé, puis tu ordonnes à l'agent :  
*« Ta proposition est rejetée dans son intégralité.  
1. Il est formellement interdit de changer de framework, de modifier l'arborescence du projet ou d'engager un service tiers sans validation d'un ADR.  
2. Le besoin est uniquement de convertir le modèle HTML de facture existant en fichier PDF téléchargeable.  
3. Utilise le moteur léger déjà présent dans le projet. Livre uniquement le contrôleur et le test unitaire correspondant, en moins de 50 lignes de modification. »*

Cette autorité ferme rappelle que **le pilote commande, et que l'IA exécute sous contrat**.

---

## Checklist réflexe du pilote

À chaque nouvelle fonctionnalité ou résolution de bogue, passe ton projet au crible de cette liste de contrôle :

- [ ] **L'observation a précédé le code** : L'agent a cartographié l'existant sans faire de suppositions à l'aveugle.
- [ ] **Le point d'arrêt a été respecté** : Aucun changement d'architecture, de base de données ou de dépendance n'a eu lieu sans ton feu vert écrit.
- [ ] **Le travail est découpé en tranches verticales** : Chaque étape produit un résultat concret, vérifiable et démontrable par un utilisateur.
- [ ] **La preuve existe (rouge puis vert)** : Un test automatique a constaté le manque ou le défaut avant d'attester de sa résolution.
- [ ] **Le serveur défend ses propres invariants** : La sécurité et l'idempotence sont garanties par le moteur applicatif et la base de données, jamais déléguées au seul navigateur web.

---

## Sources et limites

Ce chapitre formalise la méthode de gouvernance de projets assistés par IA et la conduite de tranches verticales :
- **O-MD §5, §11, §12, §13 et §14** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : La méthode ORCHESTRE en 9 points, le point d'arrêt décisionnel, les cas pratiques de création de fonctionnalité et de diagnostic de bug.
- **I-MD §9 et §10** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : Le minimalisme radical (KISS), les six phases séquentielles de livraison, la bibliothèque de prompts déterministes et la grille d'audit de PR.

Pour découvrir l'implémentation technique des tranches verticales avec exécution concurrente multithreadée sous barrière, simulation d'upload multipart et gestion des courses critiques en Python 3.11, poursuis vers le chapitre miroir : **[B11 — Appliquer ORCHESTRE du besoin à la résolution](/ingenieure/11-methode-et-cas-pratiques)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A11](/redaction/a11-methode-et-cas-pratiques).
