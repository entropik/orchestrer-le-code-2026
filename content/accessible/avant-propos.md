{
  "title": "Avant la première ligne : L'art de l'introspection, du terrain et du choix des armes",
  "source_path": "manuscrit/01-lecture-accessible/00-avant-la-premiere-ligne.md",
  "weight": 0,
  "description": "Avant le premier prompt : introspection, cadrage du besoin, choix d'une stack sobre et cas vécu du moteur de carnet photo.",
  "next": "/accessible/01-piloter-un-systeme",
  "eyebrow": "Avant-propos opérationnel",
  "theme": "00"
}

> Lecture accessible · Avant-propos opérationnel.

[Sommaire](/) · [Chapitre 01 : Piloter un système](/accessible/01-piloter-un-systeme) · [Glossaire partagé](/annexes/glossaire)

## Ce que tu sauras faire

Savoir questionner son métier, clarifier son besoin réel avant le premier prompt, choisir un environnement sobre en 2026 et utiliser l'agent en miroir socratique plutôt qu'en générateur impulsif de code fragile.

### Préambule : L'illusion de la vitesse et la vérité du terrain

Ouvre un outil d'intelligence artificielle agentique, écris trois phrases au hasard pour demander un service web, et regarde l'écran s'animer. Les fichiers s'ouvrent, des centaines de lignes de code défilent à toute allure, un serveur local s'allume et une interface moderne apparaît dans ton navigateur. La scène dure moins d'une minute. Elle procure une euphorie grisante : celle d'être devenu démiurge sans effort. C'est la promesse scintillante du *« vibe coding »*.

Puis, au bout de quelques jours, le réel frappe à la porte.

Un premier utilisateur dépose une image trop lourde et le système se fige en silence. Une mise à jour impromptue écrase les profils enregistrés la veille. La facture de la plateforme d'hébergement s'envole inexplicablement parce que le code réclame trois serveurs là où un simple script suffirait. Et quand tu demandes à l'agent de corriger le tir, il modifie trois fichiers au hasard, répare le bouton gauche, brise la sauvegarde droite et t'abandonne devant un écran d'erreur incompréhensible.

Que s'est-il passé ? 

La machine n'a commis aucune trahison. Elle a exécuté à la lettre ce que tu lui as demandé. Mais elle l'a bâti sur du sable.

Dans 99 % des tutoriels et des discours promotionnels sur l'intelligence artificielle, on commence au moment du *prompt*, c'est-à-dire quand les doigts touchent le clavier. On te montre comment demander du code, jamais **comment savoir ce qu'il faut demander**, ni pourquoi. On te vend la vitesse de la frappe en oubliant que courir très vite dans une mauvaise direction reste le moyen le plus sûr de se perdre.

Voici la première loi de ce manuel :

> **L'intelligence artificielle accélère la frappe de manière spectaculaire, mais elle n'accélérera jamais la maturation de ta pensée.**

Ce chapitre introductif explore cette phase invisible que tout le monde saute et dont dépend pourtant la survie de ton projet : l'amont absolu, l'introspection du besoin, la résistance des matériaux numériques et le choix raisonné de tes outils.

---

## Première synthèse

### 1. Le cas vécu : Deux mois de silence avant le premier prompt

Pour comprendre la puissance de l'introspection, quittons les théories abstraites pour un cas d'artisanat numérique authentique : la conception d'un **moteur d'édition en ligne de carnets photo**.

De loin, le projet a l'air d'une évidence : *« Une page web où l'utilisateur téléverse des photos, les dispose sur des pages et commande son album »*. N'importe quel modèle d'IA peut te générer une ébauche de ce service en trente secondes.

Pourtant, la gestation de ce moteur a exigé **plus de deux mois de réflexion quotidienne, de calepin, d'entretiens et d'esquisses sans écrire la moindre ligne de code ni envoyer un seul prompt**.

Pourquoi deux mois de retenue ? Parce que le métier d'éditeur d'images et de livres physiques est truffé de lois inviolables que la machine ignore totalement :

1. **L'asynchronisme du flux humain** : Un client ne compose pas un album de cinquante pages en une séance de vingt minutes. Il commence le mardi soir sur son ordinateur portable, reprend le jeudi sur sa tablette, hésite entre deux clichés de vacances, part dîner, subit une micro-coupure de connexion Wi-Fi. Si l'enregistrement ne se fait pas de manière continue, locale, silencieuse et déterministe, le client perd deux heures de travail artistique au premier rafraîchissement d'onglet. L'expérience est alors morte.
2. **La tyrannie du volume et des ratios** : Les téléphones et boîtiers modernes produisent des photographies pesant entre 10 et 45 mégaoctets, dans des ratios d'aspect hétérogènes (4:3, 3:2, 16:9, panoramiques). Manipuler cinquante images brutes dans un navigateur web sature instantanément la mémoire vive de la machine si l'on ne prévoit pas dès la conception un pipeline de vignettes allégées pour la mise en page écran.
3. **Le grand gouffre physique : du pixel à la feuille de papier** : C'est ici que réside le piège mortel. Sur un écran, on vit dans l'univers léger du pixel, en couleurs RVB (Rouge, Vert, Bleu), avec une densité d'affichage de 72 à 96 points par pouce (DPI), sans contrainte d'épaisseur. Mais un livre physique obéit à la physique de l'atelier d'impression :
   - Les encres sont imprimées en quadrichromie CMJN (Cyan, Magenta, Jaune, Noir)[^1] ;
   - La finesse minimale exigée est de 300 DPI sous peine d'obtenir des visages pixelisés ;
   - La presse et le massicot de coupe exigent un **fond perdu** (*bleed*) de 3 millimètres tout autour de la page pour éviter un liseré blanc si la lame dévie d'un demi-millimètre ;
   - Le pli central de la reliure (*le mors*) engloutit une partie de l'image si la marge intérieure n'est pas scrupuleusement calculée.

[^1]: Le modèle RVB (émis par la lumière des diodes d'un écran) possède un espace de couleurs (*gamut*) plus vaste que l'encre CMJN déposée sur une fibre de papier. Si la conversion n'est pas modélisée en amont, les bleus éclatants de la Méditerranée se transforment en grisaille terne à l'impression.

Si tu demandes à une IA : *« Crée-moi un éditeur de carnet photo »*, elle dessinera de ravissants rectangles bleus sur ton écran. Mais quand ton premier client enverra son projet à l'imprimerie, le livre sortira flou, rogné au ras des visages et avec des couleurs délavées.

Ces deux mois d'analyse n'étaient pas une perte de temps. Ils ont permis de poser sur le papier chaque transition d'état, chaque format d'image, chaque règle de repli en cas de coupure réseau, et la formule exacte de conversion des coordonnées écran en millimètres d'imprimerie.

Le jour où le dialogue avec l'agent a commencé, le modèle mental était si net, si verrouillé, que le moteur a été assemblé, testé et éprouvé en quelques jours. **L'IA n'a pas conçu le produit : elle a prêté ses mains d'orfèvre à une pensée déjà mature.**

---

## 2. La maïeutique du besoin : de la douleur au cahier des charges vivant

Avant d'allumer le moteur de l'IA, tu dois passer par ce que Socrate appelait la *maïeutique* : l'art de faire accoucher les esprits de leurs vérités cachées.

### La douleur quotidienne contre le fantasme technologique
Un projet logiciel durable naît presque toujours d'une irritation tenace dans ton travail réel :
- Tu recopies les mêmes données à la main entre deux tableurs chaque vendredi après-midi ;
- Tes clients t'envoient des pièces justificatives incomplètes par courriel et tu passes des heures à les relancer ;
- Ton équipe oublie une étape critique dans le suivi d'un dossier client ;
- Tu as besoin d'offrir à ton audience un outil sur mesure introuvable dans le commerce logiciel standard.

Si ton envie part d'un fantasme (*« J'aimerais faire une plateforme communautaire avec de l'intelligence artificielle décentralisée »*), arrête-toi tout de suite. Si tu ne peux pas identifier un être humain en chair et en os qui souffre d'un problème concret aujourd'hui, aucun code ne viendra le sauver.

### Le test du papier et du tableur
Pose-toi cette question impitoyable : **sais-tu résoudre ce problème à la main avec une feuille de papier, un stylo et un tableau de trois colonnes ?**

Si le processus est confus dans ta tête, l'ordinateur ne fera que démultiplier la confusion à la vitesse de la lumière. Le logiciel ne crée pas l'ordre ; il ne fait qu'automatiser une méthode préexistante. Écris d'abord ton flux sous forme de phrases simples :
- Quand un client arrive, que remplit-il ?
- Quelles informations sont indispensables et lesquelles sont superflues ?
- Qui a le droit de lire quoi ?
- Où se range le dossier une fois validé ?

### La règle du refus libérateur (*Ce que mon outil ne fera JAMAIS*)
La cause numéro un de mort des projets numériques est le gonflement des fonctionnalités (*feature creep*). 

Dès que l'on commence à dialoguer avec une IA, on est tenté d'ajouter des options : *« Et si on ajoutait un chat en direct ? Et un mode sombre ? Et une passerelle de paiement en crypto-monnaies ? Et des notifications sur mobile ? »*.

Pour rester maître de ton navire, dresse immédiatement la liste des **refus délibérés** :
- *« Cet outil ne gérera pas les paiements en ligne : la facturation restera manuelle par devis. »*
- *« Cet outil ne fonctionnera pas sur smartphone la première année : nos clients travaillent exclusivement au bureau sur grand écran. »*
- *« Cet outil ne proposera pas dix polices de caractères : il n'en proposera que deux, parfaitement calibrées pour la lisibilité. »*

Chaque refus est une victoire. Chaque porte fermée est un paquet de complexité en moins, et la garantie que ce qui reste fonctionnera sans jamais flancher.

---

## 3. Le mode « Plan » et l'IA en miroir socratique

Lorsque tu abordes une tâche complexe, l'agent ne doit surtout pas coder. Tu dois le placer dans une posture de **contradicteur impitoyable**.

En 2026, la quasi-totalité des environnements de développement modernes propose un mode « Plan » (ou un rôle de consultant en amont). Dans ce mode, l'agent a accès à tous tes documents, mais ses outils de modification de code sont verrouillés. Il ne peut qu'analyser, questionner et structurer.

```text
CYCLE DE L'AVANT-CODE : DU TERRAIN AU CONTRAT

┌────────────────────────────────────────────────────────────────────────┐
│ 1. INTROSPECTION (L'Artisan et son terrain)                             │
│    • Notes de terrain, écoute de la douleur réelle, refus délibérés    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. MIROIR SOCRATIQUE (L'Agent en contradicteur)                        │
│    • Interdiction de coder, attaque du plan, traque des angles morts   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. ARCHITECTURE VALIDÉE (Le contrat du système)                        │
│    • Contrats d'interface posés, choix de la stack sobre, code prêt    │
└────────────────────────────────────────────────────────────────────────┘
```

### Transformer le commis en avocat du diable
Si tu écris à l'agent : *« Regarde mon idée, c'est génial non ? »*, il te répondra avec une servilité parfaite : *« Absolument, c'est une idée remarquable ! Voici le code pour commencer »*. C'est un poison mortel.

Tu dois formuler l'ordre inverse :

> *« Je te présente mon idée d'outil et le parcours de mes utilisateurs. Ne génère pas une seule ligne de code. Endosse le rôle d'un directeur technique sceptique et exigeant. Analyse mon texte et pose-moi cinq questions dures sur mes angles morts, la fragilité de mes données, les cas où l'utilisateur fera une fausse manipulation et ce qui se passera si la machine plante au milieu. »*

Ce dialogue socratique est le moment le plus rentable de la vie d'un projet. En dix minutes d'échange textuel, l'agent pointera du doigt :
- Une ambiguïté dans la gestion de deux clients portant le même nom ;
- L'absence de procédure si une image téléversée est corrompue ;
- Un risque juridique sur la conservation des données personnelles ;
- La confusion entre un prix hors taxes et toutes taxes comprises.

Résoudre ces questions par quelques phrases dans un document texte coûte zéro euro et trente secondes. Les résoudre une fois le code écrit coûte des semaines de refonte douloureuse.

---

## 4. Le choix des armes en 2026 : l'environnement et la stack « IA-friendly »

Pour un béotien qui souhaite s'émanciper, le vocabulaire technique ressemble souvent à une forteresse imprenable. Démystifions ensemble les outils réels dont tu as besoin sur ton bureau.

### 1. Le poste de travail et le terminal
Tu n'as besoin ni d'une machine de gamer surpuissante, ni d'un serveur d'entreprise dans ton salon. Un ordinateur portable personnel récent (sous macOS, Linux ou Windows avec le sous-système WSL2) suffit amplement. L'intelligence artificielle tourne dans les datacenters des fournisseurs de modèles ; ton ordinateur local n'est que l'atelier où s'exécute le résultat.

Dans cet atelier, tu croiseras deux compagnons constants :
- **L'[Éditeur de code](/annexes/glossaire#agent)** : C'est ton tableau de bord. En 2026, des outils comme Cursor, VS Code équipé d'extensions agentiques, Claude Code ou Roo Code permettent d'avoir sous les yeux à la fois tes fichiers, la discussion avec l'agent et la visualisation de ton travail.
- **Le [Terminal](/annexes/glossaire#terminal) (la console)** : C'est ce fameux rectangle noir où défilent des lignes de texte blanc ou vert. Ne le crains pas. Le terminal n'est pas réservé aux pirates de cinéma : c'est simplement le moyen le plus direct, le plus honnête et le plus précis de parler à ton ordinateur. Quand tu cliques sur une icône avec ta souris, l'ordinateur fait semblant de déplacer un objet graphique ; dans le terminal, tu lui dis directement *« Démarre le serveur »* ou *« Lance les tests »*. L'agent adore le terminal parce qu'il n'y a aucune ambiguïté visuelle.

### 2. La pile technique (la « Stack ») : la maturité plutôt que la mode
Le grand piège du débutant consiste à vouloir utiliser la technologie dont tout le monde parle sur les réseaux sociaux depuis quarante-huit heures. C'est une erreur fatale pour deux raisons :
1. Les technologies trop récentes sont instables et changent de syntaxe tous les six mois.
2. **L'IA ne les connaît pas bien.** Un modèle de langage a été entraîné sur l'histoire d'Internet. Il est infiniment plus brillant et fiable sur des technologies qui ont dix ou vingt ans d'existence solide, documentées par des millions de discussions de qualité, que sur la bibliothèque expérimentale sortie la semaine passée.

Pour bâtir un projet avec une IA en tant que créateur indépendant, privilégie une pile technique **sobre, éprouvée et « IA-friendly »** :

| Domaine | Le choix sage en 2026 | Pourquoi ce choix protège le projet | Ce qu'il faut fuir au démarrage |
|---|---|---|---|
| **Logique & Scripting** | **Python** | Langage limpide, proche de l'anglais courant, maîtrisé à la perfection par toutes les IA de la planète, riche en bibliothèques pour tout faire. | Les langages exotiques ou à typage obscur pour un débutant. |
| **Interface Web** | **HTML pur + Tailwind CSS** ou un framework minimal (type FastAPI / Vite) | Composants universels, affichage rapide sur tous les navigateurs, facile à inspecter visuellement. | Les architectures frontend complexes à micro-services distribués. |
| **Base de données** | **SQLite**[^2] | Un trésor d'ingénierie : toute ta base de données tient dans **un seul fichier** sur ton disque. Pas de serveur de base de données à installer, sauvegarder consiste à copier un fichier. Capable d'encaisser des dizaines de milliers de requêtes par seconde sans broncher. | Les clusters de bases NoSQL dans le nuage avec facturation à la requête. |
| **Mémoire du projet** | **Git** | L'appareil photo de ton projet : il prend un cliché (*commit*) de ton code à chaque étape réussie. Si l'agent fait une bêtise, on revient en arrière en une seconde. | Les dossiers renommés à la main `projet_v2_final_final.zip`. |

[^2]: SQLite est sans doute le logiciel le plus déployé au monde (présent dans chaque smartphone, chaque navigateur web, chaque voiture). C'est le joyau absolu de l'artisan autonome.

> [!NOTE]
> **Dans l'atelier de l'auteur : le setup réel qui a forgé ce manuel**  
> Pour concevoir, éprouver et orchestrer la fabrication de cet ouvrage, l'auteur Marc Tallec n'a pas utilisé un simple chatbot solitaire dans un onglet de navigateur. Ce livre est lui-même le produit d'un atelier agentique moderne et rigoureux :
> - **L'ADE (*Agentic Development Environment*)** : [Orca](/annexes/ressources-utiles#1-orca--lade-agentic-development-environment-multi-agents), qui permet de piloter une flotte d'agents en parallèle, chacun enfermé dans un [Git worktree](/annexes/glossaire#worktree) strictement isolé, avec son propre terminal et son navigateur d'inspection (zéro collision de branches et exécution concurrente fluide).
> - **La spécialisation des modèles** : **Google Gemini** pour la maïeutique, la vue synoptique d'ensemble et l'absorption de corpus massifs ; **OpenAI Codex** pour la rigueur d'implémentation algorithmique, l'exactitude syntaxique et la couverture par les tests.
> - **Le harnais de gouvernance** : L'intégration de la doctrine en trois couches et des compétences méthodologiques de Matt Pocock (accessibles via `.agents/skills/` et documentées dans l'[architecture du harnais](/annexes/architecture-harnais)), un fichier `AGENTS.md` contraignant la mémoire vive et une suite de tests unitaires déterministes validant chaque génération.

---

## 5. La jauge de faisabilité en solo

Avant d'investir ton temps, sache mesurer ce qui est à ta portée avec un agent en tant que pilote solo, et ce qui réclame encore une armée d'ingénieurs spécialisés :

```text
JAUGE DE FAISABILITÉ : PROJET SOLO VS ÉQUIPE SPÉCIALISÉE

┌──────────────────────────────────────┐    ┌──────────────────────────────────────┐
│ FAISABILITÉ IMMÉDIATE EN SOLO        │    │ EXIGE UNE ÉQUIPE SPÉCIALISÉE         │
│ • Outils internes d'automatisation   │    │ • Systèmes bancaires directs         │
│ • Portails de dossiers clients       │    │ • Moteurs de jeux 3D temps réel      │
│ • Génération documentaire (PDF)      │    │ • Applications haute fréquence       │
│ • Tableaux de bord & métriques       │    │ • Cryptographie sur mesure           │
│ • Petits commerces & catalogues      │    │ • Systèmes médicaux critiques        │
└──────────────────────────────────────┘    └──────────────────────────────────────┘
```

Si ton projet se situe dans la colonne de gauche, tu disposes aujourd'hui de tous les leviers pour le mener à bien, de la première étincelle jusqu'à la mise en ligne opérationnelle.

---

## Mise en pratique

### Le dialogue d'accouchement d'un nouveau projet

Voici la trame exacte à copier-coller dans ton environnement d'agent lorsque tu as une nouvelle idée. Cet ordre de mission interdit formellement à l'agent de produire du code et le force à agir comme un architecte conseil.

```markdown
# ORDRE DE MISSION : MAÏEUTIQUE ET AUDIT DU PROJET

Tu es mon contradicteur en chef et le maître d'œuvre de mon architecture.
Je souhaite concevoir un outil logiciel pour mon activité professionnelle.
Voici la description brute de mon métier, de mon problème et de mes utilisateurs :

[COLLER ICI TON TEXTE LIBRE : ton quotidien, ce qui t'agace, qui utilisera l'outil]

RÈGLES D'ENGAGEMENT :
1. Tu as l'interdiction formelle d'écrire du code, des commandes shell ou de créer des fichiers sources.
2. Tu dois agir en miroir socratique : analyse ce que je viens de t'exposer et traque la complexité inutile.
3. Rédige ta réponse en quatre temps :
   a) Reformulation synthétique : ce que tu as compris de mon intention et de la vraie valeur ajoutée.
   b) Le périmètre négatif : propose-moi 3 choses évidentes que nous devrions REFUSER de faire au début.
   c) Les 5 questions couperet : les zones d'ombre sur mes données, mes utilisateurs et les cas limites.
   d) La stack minimale recommandée : les outils les plus sobres et éprouvés pour ce problème.

Attends mes réponses avant de passer à l'étape suivante.
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Un artisan menuisier ébéniste souhaite concevoir un service web pour permettre à ses clients de configurer des bibliothèques sur mesure dans leur salon, afin de générer un devis automatique et la liste de découpe du bois pour l'atelier.

Il ouvre son agent et formule son idée. Au bout de trente secondes, l'agent lui répond avec enthousiasme :

> *« Formidable projet ! J'ai imaginé une superbe application en rendu 3D interactif dans le navigateur avec WebGL. Le client pourra tourner autour du meuble en temps réel, choisir la texture du chêne ou du noyer, puis payer directement par carte bancaire via Stripe pour lancer la fabrication. Souhaites-tu que je commence à coder le moteur 3D ? »*

### Les questions du pilote lucide

1. **La question de valeur réelle** : Le client a-t-il besoin d'un jeu vidéo 3D pour commander une bibliothèque sur mesure, ou a-t-il besoin de vérifier que le meuble rentrera sous sa soupente sans heurter la plinthe ?
2. **La question du terrain physique** : Que se passe-t-il si le mur du client n'est pas droit (ce qui arrive dans 95 % des logements anciens) ? La 3D idéale de l'agent en tient-elle compte ?
3. **La question de maintenance** : Qui maintiendra un moteur 3D WebGL complexe et une intégration bancaire quand l'artisan sera à l'établi en train de raboter des planches ?

### Le corrigé commenté

**L'arbitrage de l'artisan** : Refus catégorique de la proposition de l'agent.

L'artisan reprend le volant et recadre fermement la machine :
> *« Stop. Nous refusons formellement la 3D et le paiement en ligne. Ce sont des pièges à complexité. 
> Mon métier repose sur la justesse des cotes : ce dont j'ai besoin, c'est d'un configurateur en 2D schématique vue de face. L'utilisateur renseigne la largeur du mur, la hauteur sous plafond, la présence de plinthes et le nombre d'étagères souhaitées. 
> L'outil calcule trois choses :
> 1. La faisabilité mécanique (les étagères ne doivent pas fléchir sous le poids des livres) ;
> 2. La liste exacte de découpe des panneaux pour l'atelier ;
> 3. Une estimation du coût des matériaux pour moi.
> Le client ne paie rien en ligne : il télécharge une fiche récapitulative au format PDF pour que nous en discutions ensemble à l'atelier. Recommence en proposant une architecture sobre basée sur ce besoin réel. »*

En un seul message, l'artisan a ramené le projet sur terre. Il a évité six mois de cauchemar technique pour se concentrer sur ce qui fait battre le cœur de son entreprise : la justesse de son travail de bois.

---

## Checklist réflexe de l'avant-première-ligne

Avant d'écrire ton tout premier prompt de génération de code, vérifie que chaque point ci-dessous est validé :

- [ ] **Le test de la feuille blanche** : Le flux de travail a été décrit avec des mots ordinaires, sans jargon technique, et testé mentalement avec des cas concrets.
- [ ] **La liste des refus délibérés** : Tu as écrit au moins trois fonctionnalités séduisantes que ton outil s'interdit formellement de faire pour sa première version.
- [ ] **L'identification des contraintes physiques** : Si l'outil touche au monde réel (poids d'images, impression papier, cotes de chantier, formats légaux), les règles mathématiques et les conversions ont été identifiées.
- [ ] **Le miroir socratique** : Tu as soumis ton plan à l'agent avec l'interdiction de coder, et tu as répondu à ses questions les plus inconfortables sur tes cas limites.
- [ ] **Le choix de la stack sobre** : Tu as privilégié des technologies mûres (Python, HTML/Tailwind, SQLite, Git) sur lesquelles les modèles de langage possèdent une immense mémoire d'entraînement.
- [ ] **La clarté du poste de travail** : Ton éditeur de code et ton terminal sont ouverts, et tu es prêt à piloter l'agent sous mandat sans jamais le laisser deviner tes intentions.

---

## Sources et limites

Ce chapitre puise ses racines dans les principes fondamentaux de l'ingénierie et de la maïeutique logicielle :
- **O-MD §1 et §4** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'art du mandat délimité, le refus du code spontané et la supériorité du modèle mental sur la frappe brute.
- **I-MD §1 et §2** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : La thermodynamique du logiciel, la dette technique précoce et l'importance des invariants de domaine.

Pour passer de cette phase d'amont à la mise en œuvre pratique de ton système, poursuis ta lecture avec le **[Chapitre 01 — Piloter un système, pas une génération de code](/accessible/01-piloter-un-systeme)**.
