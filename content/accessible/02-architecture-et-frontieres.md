{
  "title": "Organiser l'architecture et les responsabilités",
  "description": "Reconnaître un découpage compréhensible et éviter la complexité prématurée.",
  "weight": 2,
  "chapter_id": "A02",
  "theme": "02",
  "status": "valide",
  "source_path": "manuscrit/01-lecture-accessible/02-architecture-et-frontieres.md",
  "mirror": "/ingenieure/02-architecture-et-frontieres",
  "related": [
    "/accessible/03-besoin-et-contrats",
    "/accessible/08-donnees-et-migrations"
  ],
  "notions": [
    {
      "label": "Port",
      "anchor": "port"
    },
    {
      "label": "Contrat",
      "anchor": "contrat"
    },
    {
      "label": "ADR",
      "anchor": "adr"
    }
  ],
  "previous": "/accessible/01-piloter-un-systeme",
  "next": "/accessible/03-besoin-et-contrats"
}

## Ce que tu sauras faire

Reconnaître un découpage compréhensible et éviter la complexité prématurée.

---

## Première synthèse

### 1. Le syndrome de la chambre d'adolescent : pourquoi le code se mélange

Lorsqu'un agent d'intelligence artificielle commence à travailler sur une demande, son réflexe naturel est de tout entasser au même endroit.

Tu lui demandes d'enregistrer une commande ? En quelques secondes, il rédige un fichier unique où se côtoient :
- Le dessin du bouton sur la page web,
- La vérification du numéro de téléphone,
- Le calcul de la TVA et de la remise commerciale,
- Le mot de passe de connexion à la base de données,
- Et l'ordre direct d'envoyer un courriel de confirmation.

Sur ton écran, la démonstration fonctionne. Mais sur le plan architectural, c'est l'équivalent d'une chambre d'adolescent où les chaussettes sales, les livres d'école, la brosse à dents et les restes de pizza s'empilent sur le même bureau.

Tant que le projet compte cinquante lignes, cette pagaille est supportable. Mais dès que tu souhaites modifier le calcul de la remise, l'agent casse l'envoi du courriel. Dès que tu veux changer la couleur du bouton, l'accès à la base de données ne répond plus. Le modèle d'IA lui-même, submergé par ce mélange confus, commence à perdre le fil, à halluciner des variables et à détruire ce qui fonctionnait la veille.

Une bonne architecture logicielle ne relève pas de la virtuosité technique. Elle répond à un principe d'hygiène élémentaire : **séparer les responsabilités pour que chaque modification reste locale, prévisible et sans danger pour le reste du bâtiment**.

---

### 2. Les quatre pièces de la maison logicielle

Pour organiser ton application sans te perdre dans le jargon, imagine une maison bien tenue, découpée en quatre espaces étanches :

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. LE GUICHET (Présentation)                                           │
│    L'écran que l'utilisateur voit, touche et clique.                   │
│    Rôle : Accueillir poliment, afficher les données, capter l'action.  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. LE CHEF DE BUREAU (Application)                                     │
│    L'orchestrateur des démarches : "Créer un devis", "Régler facture". │
│    Rôle : Coordonner les étapes sans faire les calculs lui-même.       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. LE REGISTRE DES RÈGLES (Domaine)                                    │
│    Le cœur souverain de ton métier.                                    │
│    Rôle : Calculer, vérifier les règles d'or, appliquer les lois.      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. L'ARMOIRE FORTE & LES COURSIERS (Infrastructure)                   │
│    Le stockage physique et les liaisons avec le monde extérieur.       │
│    Rôle : Disque dur, base de données, envoi de SMS, terminaux bancaires│
└────────────────────────────────────────────────────────────────────────┘
```

1. **La Présentation (Le Guichet)** : C'est la vitrine. Elle ne doit jamais calculer une réduction commerciale ni décider si un client est solvable. Son seul rôle est de transmettre proprement la demande au bureau intérieur.
2. **L'Application (Le Chef de bureau)** : C'est le chef d'orchestre des scénarios du quotidien. Il reçoit la demande du guichet et dit : *« D'abord nous vérifions le client, ensuite nous calculons la somme avec le registre, et enfin nous rangeons le dossier dans l'armoire »*.
3. **Le Domaine (Le Registre métier)** : C'est l'âme de ton entreprise. C'est ici que sont écrites les règles fondamentales : *« Une commande ne peut pas être validée si le panier est vide »*, *« La TVA sur ce produit est de 20 % »*. Ce registre est **sacré** : il ne sait même pas si l'utilisateur utilise un iPhone, un ordinateur sous Windows ou un terminal texte. Il applique la règle, purement.
4. **L'Infrastructure (L'Armoire et les Coursiers)** : C'est la logistique lourde. Les disques où s'écrivent les octets, les serveurs de base de données, les raccordements réseau à Stripe ou aux opérateurs de télécommunication.

Cette séparation n'exige pas quatre ordinateurs différents ni des mois de travail. Dans un projet bien tenu, ce sont simplement quatre dossiers clairement nommés sur ton disque dur.

---

### 3. La tentation du château de cartes : le piège des micro-services

Quand tu demandes à un agent d'organiser une application, il a souvent tendance à te proposer ce qu'il a lu dans les publications des géants de la Silicon Valley :
> *« Nous allons découper ton projet en six micro-services indépendants : un pour l'authentification, un pour la facturation, un pour les fichiers, un pour les notifications, chacun hébergé sur son propre serveur dans le cloud avec sa propre base de données ! »*

Pour un décideur ou un créateur indépendant, ce conseil est un **piège mortel**.

Des entreprises comme Netflix ou Amazon utilisent des micro-services parce qu'elles emploient des milliers d'ingénieurs répartis sur trois continents et que leurs équipes ne peuvent pas travailler sur le même fichier en même temps. Les micro-services résolvent un problème d'organisation humaine à grande échelle, pas un problème d'ingénierie de départ.

Pour ton projet, multiplier les serveurs dès le premier jour apporte :
- Une facture d'hébergement multipliée par cinq.
- Des pannes réseau invisibles (le serveur A n'arrive plus à parler au serveur B).
- L'impossibilité de tester ton application sur ton propre ordinateur portable sans lancer une usine à gaz.

> [!IMPORTANT]
> **La doctrine par défaut du pilote : Le Monolithe Modulaire**  
> Une seule application, un seul déploiement, une seule base de données, mais des **cloisons intérieures d'une propreté chirurgicale**.  
> Tu n'extrairas un composant sur un serveur séparé que le jour où une mesure chiffrée le rendra incontournable (par exemple, un traitement vidéo lourd qui saturerait la machine principale).

---

### 4. Prises murales et appareils : la notion de Port et d'Adaptateur

Pour rendre ton projet durable face au temps et aux caprices des technologies, tu dois comprendre une notion centrale : **l'inversion des dépendances**, que les ingénieurs appellent l'architecture en [Ports](/annexes/glossaire#port) et Adaptateurs[^1].

Regarde les prises électriques murales de ta maison. La prise murale délivre un courant standardisé à 230 volts. C'est un **[Port](/annexes/glossaire#port)** : une spécification abstraite et immuable. 

Tu peux y brancher une lampe de chevet, un aspirateur ou le chargeur de ton téléphone. Ces appareils sont des **Adaptateurs**. Si ton aspirateur tombe en panne ou si tu décides d'en changer pour un modèle plus récent, tu n'as pas besoin d'abattre le mur du salon pour refaire tout le câblage électrique de la maison : tu débranches simplement l'ancien appareil et tu branches le nouveau.

Dans ton logiciel, le cœur de métier doit fonctionner exactement comme cette prise murale :
- Ton registre métier déclare un port : *« J'ai besoin d'une capacité pour stocker un document et retrouver son empreinte »*. C'est le [Contrat](/annexes/glossaire#contrat).
- Au début, l'adaptateur est un simple dossier sur ton ordinateur de bureau.
- Plus tard, si ton activité grandit, tu pourras brancher un adaptateur vers un service de stockage géant dans le cloud (comme Amazon S3 ou Cloudflare R2).

Le cœur de ton entreprise ne change pas d'une seule virgule : seule la prise extérieure a été réorientée.

[^1]: Ce modèle a été formalisé sous le nom d'*Architecture Hexagonale* par l'informaticien Alistair Cockburn au début des années 2000 pour libérer les applications de la tyrannie des interfaces graphiques et des bases de données.

---

## Mise en pratique

### Cartographier les responsabilités sans écrire de code

Voici l'exercice d'architecture que tout pilote doit savoir mener sur un coin de table ou un tableau blanc avant de lancer un agent.

Prenons un besoin universel : **recevoir un document de client, calculer son coût de traitement et lui renvoyer un accusé de réception**.

Voici comment le maître d'ouvrage découpe la feuille de route pour son agent :

```text
┌─────────────────────────┬────────────────────────────────────────────────────────┐
│ PIÈCE DU SYSTÈME        │ MISSION ATTRIBUÉE (ET CE QUI LUI EST INTERDIT)         │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. Guichet Web          │ Affiche la jauge de dépôt.                             │
│    (Présentation)       │ INTERDIT : Ne calcule aucun tarif, ne touche pas au SQL│
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ 2. Scénario Déposer     │ Coordonne : réceptionne le flux, sollicite le devis,   │
│    (Application)        │ commande l'archivage, puis déclenche la confirmation.  │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ 3. Règle Tarifaire      │ Calcule le montant exact selon la taille et le format. │
│    (Domaine)            │ INTERDIT : Ne sait pas comment le fichier est stocké.  │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ 4. Adaptateur Disque    │ Enregistre physiquement les octets et calcule le SHA.  │
│    (Infrastructure)     │ INTERDIT : N'a aucun avis sur le prix du document.     │
└─────────────────────────┴────────────────────────────────────────────────────────┘
```

En fournissant ce tableau à ton agent d'IA, tu lui donnes une **boussole architecturale**. Il ne peut plus mélanger le calcul du prix avec l'écriture sur le disque : chaque fonction sait dans quel tiroir elle a le droit de vivre.

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu développes un outil de réservation de créneaux pour des rendez-vous professionnels. L'agent avec lequel tu travailles te présente son plan :

> *« Pour que le système soit moderne et ultra-rapide, j'ai créé trois projets distincts :  
> 1. Un service d'agenda sur un serveur Node.js.  
> 2. Un service d'envoi d'emails sur un serveur Python.  
> 3. Une base de données Redis séparée pour la synchronisation en temps réel.  
> Pour tester l'ensemble sur ton ordinateur, il suffit d'installer Docker, de configurer trois fichiers d'environnement et de lancer un réseau virtuel local. »*

### Les questions du pilote

Face à cette surenchère technique, le maître d'ouvrage pose ses trois questions de bon sens :

1. **La question du volume réel** : Combien de réservations attendons-nous par jour au démarrage ? *(Une trentaine de rendez-vous quotidiens, soit un volume dérisoire qu'une montre connectée pourrait traiter en un dixième de seconde).*
2. **La question de la friction opérationnelle** : Suis-je capable de lancer et de tester ce projet en une seule commande simple sur ma machine de travail sans y passer mon après-midi ? *(Non, l'agent impose trois environnements, Docker et un réseau virtuel).*
3. **La question du point de rupture** : Si le serveur de messagerie tombe en panne au milieu d'une réservation, comment la base de l'agenda est-elle prévenue ? *(L'agent a créé un risque de désynchronisation réseau entre deux serveurs au lieu d'un appel direct en mémoire).*

### Le corrigé commenté

**La décision du pilote** : Rejet ferme de l'architecture dispersée.

Tu ordonnes à l'agent :  
*« Ce découpage est prématuré et injustifié. Rassemble l'intégralité du projet dans une **seule application déployable (monolithe modulaire)**. L'agenda et les emails vivront dans deux dossiers distincts du même projet, exécutés par la même machine, partageant une base de données unique et simple. L'ensemble doit pouvoir être exécuté et testé localement avec une seule commande standard, sans aucune machinerie réseau complexe. »*

Grâce à cette décision, ton projet reste lisible, testable en trois secondes, réparable par n'importe qui et hébergeable pour quelques euros par mois.

---

## Checklist réflexe du pilote

Avant de valider l'architecture proposée par un agent, vérifie ces cinq règles d'or :

- [ ] **Une seule application au départ** : Le projet tient dans une seule base de code déployable, sans dispersion en micro-services inutiles.
- [ ] **Les règles métier sont étanches** : Le calcul de tes tarifs et de tes processus d'entreprise ne dépend d'aucune marque d'écran ni d'aucun fournisseur de base de données.
- [ ] **Les prises sont standardisées ([Ports](/annexes/glossaire#port))** : Tu peux changer de prestataire de stockage ou d'envoi de courriels en remplaçant un seul fichier d'adaptation, sans réécrire la logique du produit.
- [ ] **Le test local est instantané** : N'importe qui peut cloner le projet et lancer les vérifications en une seule ligne de commande sur son poste.
- [ ] **Chaque dossier a un rôle unique** : Si tu demandes à l'agent *« Où vit le calcul de ma règle X ? »*, il peut te désigner un fichier précis, court et compréhensible.

---

## Sources et limites

Ce chapitre s'appuie sur les principes fondamentaux de conception logicielle et de séparation des responsabilités :
- **O-MD §1 et §2** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'organisation en couches fonctionnelles, la primauté du monolithe modulaire et la gestion rigoureuse des dépendances.
- **I-MD §2** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : La théorie des modules profonds de John Ousterhout, les points de couture (*Seams*) de Michael Feathers et l'architecture hexagonale d'Alistair Cockburn.

Pour explorer les mécanismes mathématiques de modularité, les interfaces minimales et l'injection de dépendances exécutable en Python, poursuis vers le chapitre miroir : **[B02 — Organiser l'architecture et les responsabilités](/ingenieure/02-architecture-et-frontieres)**.

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A02](/redaction/a02-architecture-et-frontieres).
