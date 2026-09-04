{
  "title": "Transformer le besoin en contrat vérifiable",
  "description": "Écrire une demande que deux personnes peuvent comprendre et vérifier de la même manière.",
  "weight": 3,
  "chapter_id": "A03",
  "theme": "03",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/03-besoin-et-contrats.md",
  "mirror": "/ingenieure/03-besoin-et-contrats",
  "related": [
    "/accessible/02-architecture-et-frontieres",
    "/accessible/06-tests-et-preuves"
  ],
  "notions": [
    {
      "label": "Contrat",
      "anchor": "contrat"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    },
    {
      "label": "API",
      "anchor": "api"
    }
  ],
  "previous": "/accessible/02-architecture-et-frontieres",
  "next": "/accessible/04-harnais-et-contexte"
}

## Ce que tu sauras faire

Écrire une demande que deux personnes peuvent comprendre et vérifier de la même manière.

---

## Première synthèse

### 1. Le piège du « Fais-moi un truc moderne » : pourquoi l'IA comble les vides

Lorsque tu demandes à un être humain : *« Prépare-moi un bon café »*, son cerveau utilise des années de contexte partagé. Il sait quelle tasse tu préfères, si tu prends du sucre, et qu'il ne doit pas te servir de l'eau tiède avec du sel.

Face à une intelligence artificielle générative, cette intuition sociale n'existe pas. Un modèle de langage ne « devine » pas ton intention : il calcule des probabilités statistiques sur les mots qui se succèdent le plus fréquemment.

Si tu écris à un agent :
> *« Crée une fonction pour que les clients puissent téléverser leurs devis au format PDF. »*

La phrase semble limpide. Pourtant, pour une machine, elle laisse une centaine de choix invisibles dans le vide le plus total :
- Quelle est la taille maximale d'un fichier ? 2 mégaoctets ou 4 gigaoctets ?
- Que se passe-t-il si le client a une coupure de réseau à 98 % du transfert ?
- Le fichier doit-il écraser un document déjà existant ou créer une nouvelle version ?
- Le client d'une entreprise rivale peut-il deviner l'adresse du document et le lire en cachette ?
- Quel message exact doit s'afficher si le document n'est pas un vrai PDF mais une vidéo renommée ?

En l'absence de directives explicites, l'agent **comble automatiquement tous les vides** avec des hypothèses statistiques par défaut. Il choisira souvent la solution la plus rapide à écrire dans l'instant, sans mesurer ses conséquences pour la survie de ton entreprise.

Le rôle du pilote n'est pas d'écrire des lignes de code : son métier consiste à **éliminer l'ambiguïté avant que le premier fichier ne soit créé**.

---

### 2. Le devis de l'artisan : la métaphore du contrat de chantier

Imagine que tu fasses rénover la toiture de ta maison. Si tu signes un devis d'une seule ligne indiquant : *« Rénovation complète de la toiture pour 15 000 euros »*, tu t'exposes à une catastrophe. L'artisan pourra poser des tuiles en plastique bas de gamme, laisser les gouttières percées, et te réclamer légitimement son paiement puisque la toiture aura été « rénovée ».

Un devis professionnel ne fonctionne jamais ainsi. Il détaille :
- La marque et la référence exacte des ardoises naturelles,
- Le traitement hydrofuge appliqué sur la charpente,
- La date de livraison et les pénalités de retard,
- Et, tout aussi capital, les **exclusions de garantie** : *« Ne comprend pas le remplacement des chevrons intérieurs ni la réfection de la cheminée »*.

Dans le pilotage logiciel, ce devis s'appelle un **[Contrat](/annexes/glossaire#contrat)**. Un contrat logiciel est un accord bilatéral inviolable entre toi et la machine. Il stipule avec une précision chirurgicale ce qui entre, ce qui sort, les lois qui ne plient jamais, et ce qui est formellement exclu du travail immédiat.

---

### 3. La Tranche Verticale : découper le gâteau de haut en bas

Face à un grand projet, le réflexe classique de l'ingénieur comme de l'amateur est de construire « en couches horizontales » :
1. Mois 1 : Concevoir toute la base de données de l'entreprise.
2. Mois 2 : Écrire tous les calculs internes.
3. Mois 3 : Dessiner tous les écrans.

Cette méthode est un piège redoutable lorsqu'on travaille avec des agents IA. Pendant trois mois, tu ne vois rien fonctionner. Au moment d'assembler les morceaux, rien ne s'emboîte, les hypothèses du début se révèlent fausses et l'agent s'emmêle dans des milliers de lignes de code mortes.

La méthode d'orchestration moderne impose le travail en **Tranches Verticales** :

```text
CONCEPTION HORIZONTALE (À PROSCRIRE)      TRANCHE VERTICALE (MÉTHODE DU PILOTE)
┌────────────────────────────────┐         ┌───────┐
│ Tous les écrans du site (Mois 1)│         │Écran  │ ◄─ Une seule interface simple
├────────────────────────────────┤         ├───────┤
│ Toutes les règles métier (Mois 2)│        │Règle  │ ◄─ Un seul calcul utile
├────────────────────────────────┤         ├───────┤
│ Toute la base de données (Mois 3)│        │Stock  │ ◄─ Une seule table minimale
└────────────────────────────────┘         └───────┘
  (Rien ne fonctionne avant la fin)          (Résultat visible et testé en 1 jour)
```

Une tranche verticale découpe une part de gâteau qui traverse **juste assez d'écran, juste assez de règle métier et juste assez de stockage pour délivrer un résultat humain observable**.

Exemple : plutôt que de créer « le grand module de facturation », la première tranche sera simplement : *« Permettre au gérant de générer un PDF contenant une ligne d'article et de le télécharger »*. Une fois cette tranche testée et validée, on passe à la suivante.

---

### 4. L'Anatomie d'une Fiche de Spécification en six points

Pour donner à un agent une mission qu'il ne pourra ni déformer ni bâcler, le pilote rédige une **Fiche de Spécification** (souvent appelée *SPEC*[^1]). Elle tient sur une page et s'articule autour de six questions cardinales :

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. L'INTENTION                                                         │
│    Pour qui ce travail est-il fait ? Quel problème résout-il ?         │
│    Quel est le bénéfice concret et immédiat ?                          │
├────────────────────────────────────────────────────────────────────────┤
│ 2. LE SCÉNARIO NOMINAL                                                 │
│    Le chemin idyllique par beau temps, étape par étape :               │
│    « L'utilisateur clique sur X -> Le système vérifie Y ->             │
│       Le document Z est créé ».                                        │
├────────────────────────────────────────────────────────────────────────┤
│ 3. LES RÈGLES D'OR                                                     │
│    Les calculs précis, les plafonds, les autorisations et les formats.│
│    (Chiffres exacts, unités sans ambiguïté).                           │
├────────────────────────────────────────────────────────────────────────┤
│ 4. LES CAS LIMITES & INCIDENTS                                         │
│    Que fait le système en cas de coupure de réseau, de fichier corrompu│
│    ou de double-clic frénétique sur le bouton de paiement ?            │
├────────────────────────────────────────────────────────────────────────┤
│ 5. LES CRITÈRES D'ACCEPTATION OBSERVABLES                              │
│    La liste des tests que n'importe qui peut observer sur son écran    │
│    pour prouver que le travail est réellement achevé.                  │
├────────────────────────────────────────────────────────────────────────┤
│ 6. LE HORS PÉRIMÈTRE EXPLICITE                                         │
│    La liste sacrée de ce que cette tranche NE DOIT PAS faire.          │
│    (Évite que l'agent ne passe sa nuit à inventer des options inutiles)│
└────────────────────────────────────────────────────────────────────────┘
```

[^1]: Dans le jargon professionnel des projets informatiques, la *SPEC* (pour *Spécification fonctionnelle*) est le document d'exigence contractuelle qui prime sur toute écriture de code.

---

### 5. Les Invariants : les lois physiques de ton entreprise

Dans chaque entreprise, il existe des principes intangibles. En programmation, ces vérités immuables portent un nom précis : les **[Invariants](/annexes/glossaire#invariant)**.

Un invariant est une loi qui doit rester vraie à **chaque instant de la vie du logiciel**, sans aucune exception tolérée :
- *« Le total d'une facture doit toujours être égal à la somme exacte de ses lignes, centime pour centime. »*
- *« Une commande payée doit posséder un identifiant de transaction bancaire unique. »*
- *« Un utilisateur de l'entreprise Alpha ne peut jamais voir, même par erreur, le moindre document appartenant à l'entreprise Bêta. »*

Les invariants sont les piliers de ta forteresse. Lorsque tu énonces clairement un invariant à un agent d'IA, tu lui donnes une consigne de surveillance automatique : s'il écrit un morceau de code qui menace cet invariant, le système de contrôle doit faire retentir l'alarme immédiatement.

---

### 6. Le Journal des Décisions (ADR) : ne perds jamais la mémoire

Lorsque plusieurs personnes (ou toi et des agents IA successifs) collaborent sur un projet, un danger mortel guette : **l'amnésie architecturale**.

Six mois après avoir démarré, un nouvel agent arrive sur le projet. Il voit que les fichiers sont stockés localement sur le disque dur. Trouvant cela démodé, il décide d'effacer le code pour le remplacer par une base de données cloud complexe... sans savoir que tu avais délibérément choisi le disque local pour des raisons impérieuses de confidentialité juridique.

Pour éviter ces retours en arrière destructeurs, le pilote tient un **Registre de Décisions d'Architecture** (*Architecture Decision Record*, ou **ADR**[^2]). Un ADR tient sur une simple feuille et résume :
1. **Le Contexte** : Quel problème devions-nous résoudre ?
2. **La Décision prise** : Quelle solution avons-nous choisie ?
3. **Les Alternatives rejetées** : Pourquoi n'avons-nous pas retenu l'option B ou C ?
4. **Les Conséquences** : Quels avantages et quelles contraintes cette décision impose-t-elle pour l'avenir ?

Grâce à ces courtes fiches, ton projet conserve sa mémoire vive, et aucun agent ne viendra défaire un choix mûrement réfléchi.

[^2]: Voir l'ADR de référence du dépôt dans le fichier source `docs/adr/0001-harnais-agentique-en-trois-couches.md` et sa modélisation dans l'[Architecture du harnais](/annexes/architecture-harnais).

---

## Mise en pratique

### Exemple fil rouge : La Fiche de Réception d'un Devis

Voici un modèle complet de fiche de spécification pour notre fil rouge (le téléversement d'un document par un client). Ce document est prêt à être confié à un agent :

```text
================================================================================
FICHE DE TRANCHE : RÉCEPTION ET VÉRIFICATION D'UN DOCUMENT CLIENT
================================================================================

1. INTENTION :
   Permettre à un client authentifié de déposer son devis au format PDF afin
   que notre atelier puisse en chiffrer la réalisation.

2. SCÉNARIO NOMINAL :
   a. Le client sélectionne un fichier PDF sur son ordinateur.
   b. Le client clique sur "Envoyer le document".
   c. Le système calcule l'empreinte de sécurité et enregistre le fichier.
   d. La page affiche un accusé de réception vert avec le numéro de référence.

3. RÈGLES D'OR & INVARIANTS :
   - Format accepté : exclusivement PDF (vérifié par les premiers octets du fichier).
   - Taille maximale : 50 mégaoctets (soit exactement 52 428 800 octets).
   - Invariant d'isolation : Un fichier déposé par l'organisation X est tagué
     avec l'identifiant "org_id" de l'organisation X et ne peut être lu que par elle.

4. GESTION DES CAS LIMITES & ERREURS :
   - Si la taille dépasse 50 Mo : Rejet immédiat avec message "Fichier trop lourd".
   - Si le fichier est corrompu ou n'est pas un PDF : Rejet avec message "Format invalide".
   - Si la connexion coupe avant la fin : Le fichier partiel est automatiquement
     détruit du disque temporaire pour ne pas encombrer le serveur de résidus morts.

5. LES 5 CRITÈRES D'ACCEPTATION OBSERVABLES :
   [✓] 1. Un PDF valide de 2 Mo déposé par un utilisateur connecté affiche le message
          "Document enregistré sous la référence DEV-XXXXX" en moins de 3 secondes.
   [✓] 2. Une tentative de dépôt d'un fichier .exe ou .png de 100 Ko est bloquée
          avec le message "Format refusé : seuls les fichiers PDF sont acceptés".
   [✓] 3. Un fichier de 55 Mo est rejeté avant le téléversement complet avec l'alerte
          "La taille maximale autorisée est de 50 Mo".
   [✓] 4. Après un double-clic rapide sur "Envoyer", un seul document est créé sur
          le disque, sans génération de doublon.
   [✓] 5. Un utilisateur déconnecté tentant d'accéder au lien de téléversement est
          redirigé vers la page de connexion.

6. HORS PÉRIMÈTRE EXPLICITE (Ce qui est strictement exclu de cette tranche) :
   - [EXCLU] La conversion automatique du PDF en images miniatures.
   - [EXCLU] L'envoi d'une notification par SMS au client (seul l'écran web compte).
   - [EXCLU] La signature électronique du document.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu demandes à un agent de créer le formulaire d'inscription pour de nouveaux partenaires commerciaux. Une demi-heure plus tard, l'agent te répond :

> *« J'ai terminé ! J'ai créé un formulaire d'inscription ultra-complet. Il demande le nom, le prénom, le numéro de SIRET, le bilan comptable des trois dernières années, le compte Twitter de l'entreprise, et j'ai déjà raccordé une intelligence artificielle qui analyse la réputation en ligne du partenaire avant de lui envoyer un SMS de bienvenue via Twilio. »*

### Les questions du pilote

Face à ce travail débordant d'initiatives non sollicitées, le pilote examine la situation :

1. **La question du périmètre** : Avions-nous demandé une analyse de réputation en ligne ou un envoi de SMS dans cette première tranche ? *(Non, le besoin initial était simplement de collecter un nom, un email et un SIRET).*
2. **La question du risque et de la dépendance** : L'agent a introduit un compte Twilio payant et une API d'analyse de réputation sans autorisation préalable. Que se passe-t-il si ces services tombent en panne ? *(L'inscription des partenaires est totalement bloquée).*
3. **La question de la vérifiabilité** : Sommes-nous capables de vérifier si le formulaire fonctionne sans avoir à payer des crédits d'API externes ? *(Non, la vérification est devenue dépendante de services tiers).*

### Le corrigé commenté

**La décision du pilote** : Rejet immédiat de la dérive de périmètre (*Scope Creep*).

Tu ordonnes à l'agent :  
*« Stop. Tu as violé la règle d'or du hors-périmètre. Supprime immédiatement l'analyse de réputation en ligne et l'envoi de SMS. Reviens strictement à la tranche verticale définie : enregistrer le nom, l'email et le SIRET dans la base locale, et afficher un message de confirmation à l'écran. Aucune dépendance externe payante ne doit être ajoutée sans mon accord formel dans une fiche d'arbitrage. »*

Cette fermeté évite que ton projet ne devienne une usine à gaz ingérable, coûteuse et fragile dès la première semaine.

---

## Checklist réflexe du pilote

Avant de donner le feu vert à un agent pour coder une fonctionnalité, vérifie que ta demande respecte ces cinq règles d'or :

- [ ] **L'intention est humaine** : La demande décrit ce qu'un utilisateur réel veut accomplir, pas une suite de termes techniques jargonneux.
- [ ] **Les critères sont observables** : Chaque critère d'acceptation peut être vérifié de visu sur un écran ou par une commande simple (« Je clique sur A, je dois voir B »).
- [ ] **Les limites chiffrées sont fixées** : Les tailles maximales, les durées d'attente et les formats acceptés sont écrits noir sur blanc avec leurs unités précises.
- [ ] **Le hors-périmètre est verrouillé** : La liste de ce que l'agent n'a PAS le droit de faire est aussi claire que celle de ses tâches.
- [ ] **Les invariants sont proclamés** : Les règles absolues (confidentialité des comptes, cohérence financière) sont posées comme des frontières inviolables.

---

## Sources et limites

Ce chapitre approfondit les méthodologies d'expression du besoin et de formalisation contractuelle :
- **O-MD §3 et §12** ([Manuel d'Orchestration Logicielle](/references/sources/o-md)) : La conception de la tranche verticale, la fiche de fonctionnalité, les ADR et les invariants produit.
- **I-MD §3, §9.3 et §10.2** ([Manuel d'Ingénierie Logicielle](/references/sources/i-md)) : L'échec du langage naturel non contraint, l'isomorphisme de Curry-Howard, le parsing runtime aux frontières réseau et la formalisation des erreurs selon la RFC 7807/9457.

Pour comprendre la traduction mathématique de ces contrats dans les compilateurs, le typage statique strict et la validation hermétique aux frontières en Python, poursuis vers le chapitre miroir : **[B03 — Transformer le besoin en contrat vérifiable](/ingenieure/03-besoin-et-contrats)**.

## Références pour approfondir

- [TypeScript — assertions de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) — Les assertions de type ne vérifient pas les données à l'exécution. [Notice et chapitres associés](/references#ref-typescript).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A03](/redaction/a03-besoin-et-contrats).
