{
  "title": "Faire travailler le système sans perdre les opérations",
  "description": "Comprendre les traitements différés, les réessais et la protection contre les doublons.",
  "weight": 7,
  "chapter_id": "A07",
  "theme": "07",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/07-asynchronisme-et-reprises.md",
  "mirror": "/ingenieure/07-asynchronisme-et-reprises",
  "related": [
    "/accessible/08-donnees-et-migrations",
    "/accessible/10-exploitation-et-evolution"
  ],
  "notions": [
    {
      "label": "Idempotence",
      "anchor": "idempotence"
    },
    {
      "label": "Outbox",
      "anchor": "outbox"
    },
    {
      "label": "Invariant",
      "anchor": "invariant"
    }
  ],
  "previous": "/accessible/06-tests-et-preuves",
  "next": "/accessible/08-donnees-et-migrations"
}

## Ce que tu sauras faire

Comprendre les traitements différés, les réessais et la protection contre les doublons.

---

## Première synthèse

### 1. Le restaurant et le carnet de commandes : l'asynchrone expliqué simplement

Imagine que tu dînes dans un restaurant gastronomique. Le serveur s'approche de ta table, prend ta commande pour un bœuf mijoté pendant cinq heures, puis... reste planté devant toi, immobile, pendant cinq heures consécutives, attendant que la viande soit cuite avant de te donner l'addition et de passer au client suivant.

Ce serait absurde et le restaurant ferait faillite dès le premier soir.

Pourtant, c'est **très exactement ce que font les programmes informatiques mal conçus**.

Lorsqu'un agent d'IA code une fonctionnalité lourde (comme vérifier un document PDF volumineux de cinquante mégaoctets, générer une facture ou envoyer des SMS à mille personnes), son réflexe par défaut est de faire tout le travail directement pendant que le navigateur de l'utilisateur attend. La page web affiche une petite roue qui tourne indéfiniment. Si la connexion saute à la vingtième seconde, l'opération plante, le serveur est saturé et l'utilisateur est furieux.

Dans un restaurant bien tenu, le serveur applique le principe du **traitement asynchrone** :
1. Il note ta commande sur son calepin et t'adresse un sourire : *« C'est bien noté, voici votre reçu n° 42 »*. Cette étape prend **deux secondes**.
2. Il dépose le ticket de commande sur le passe-plat de la cuisine (la **file d'attente**).
3. Les cuisiniers (les **travailleurs d'arrière-plan** ou *workers*) prennent les tickets les uns après les autres à leur propre rythme.
4. Pendant ce temps, le serveur continue d'accueillir d'autres clients sans jamais bloquer la salle.

---

### 2. Les quatre états d'une demande : rassurer l'utilisateur

Parce que le traitement ne se fait plus instantanément sous les yeux de l'utilisateur, ton logiciel doit être capable de raconter une histoire claire à chaque seconde.

Le maître d'ouvrage veille à ce que toute opération différée passe par **quatre états explicites** :

```text
LE CYCLE DE VIE D'UNE TÂCHE DIFFÉRÉE :

  1. REÇU (Ticket créé en 1 seconde)
     « Votre document de 45 Mo a bien été réceptionné sous la référence #892. »
     ► L'utilisateur est rassuré immédiatement et peut quitter la page.
              │
              ▼
  2. EN COURS DE TRAITEMENT (En cuisine)
     « Notre atelier vérifie la conformité des polices et des marges... »
     ► Une jauge ou un message signale que le système travaille activement.
              │
              ▼
  ┌───────────┴───────────┐
  ▼                       ▼
  3. VALIDÉ (Succès)      4. EN DIFFICULTÉ / REJETÉ (Échec documenté)
  « Document certifié ! » « Erreur : Le fichier dépasse le format autorisé. »
```

Cette transparence élimine le syndrome du « clic d'angoisse » : l'utilisateur ne clique pas dix fois de suite sur le bouton par peur que sa première tentative n'ait pas fonctionné.

---

### 3. La clé d'idempotence : l'antidote absolu contre les doublons

Considérons la situation la plus courante et la plus périlleuse d'Internet : **la micro-coupure réseau**.

Tu es sur ton smartphone, tu cliques sur *« Payer 150 € »*. La banque traite ton paiement, mais au moment exact où elle renvoie la confirmation à ton téléphone, ta connexion 4G saute sous un tunnel. Ton écran affiche : *« Erreur de connexion »*.

Que fais-tu ? Tu recliques sur *« Payer »*.

Si le système informatique a été bâti naïvement, tu seras **débité une deuxième fois de 150 €**.

Pour empêcher ce scandale, les ingénieurs utilisent une notion cardinale : **l'[Idempotence](/annexes/glossaire#idempotence)**[^1].

L'idempotence signifie qu'une opération produit **exactement le même résultat final, qu'on l'exécute une seule fois ou dix fois d'affilée**.

Comment cela fonctionne-t-il concrètement ?
- Dès que tu ouvres la page de paiement, le système génère un numéro d'intention unique au monde (souvent appelé **Clé d'idempotence**).
- La première requête part avec ce numéro : *« Traiter le paiement #XYZ-123 »*.
- Si la connexion coupe et que tu recliques, la deuxième requête part avec le **même numéro #XYZ-123**.
- Le serveur examine son registre et dit : *« Halte ! J'ai déjà encaissé le paiement #XYZ-123 il y a douze secondes. Je ne touche pas à la carte bancaire, je renvoie simplement le reçu de paiement déjà prêt »*.

Tu as cliqué deux fois, mais tu n'as payé qu'une seule fois. Ton entreprise est protégée contre les litiges.

[^1]: Du latin *idem* (même) et *potens* (pouvoir). Formalisé en mathématiques par Benjamin Peirce en 1870, le concept est au cœur des architectures distribuées modernes.

---

### 4. Que faire des tâches qui échouent toujours ? La boîte aux rebuts

Dans le monde réel, certaines pannes sont temporaires (un serveur d'envoi de courriels qui redémarre pendant 30 secondes), tandis que d'autres sont définitives (un fichier PDF endommagé dont les octets sont illisibles).

Face à une panne, le réflexe du novice est de faire réessayer la tâche en boucle infinie toutes les demi-secondes. Résultat : le serveur s'épuise à traiter une tâche condamnée d'avance et finit par planter totalement.

Le système professionnel applique deux principes d'hygiène :
1. **Les réessais espacés (*Exponential Backoff*)** : On réessaie après 2 secondes, puis après 4 secondes, puis après 8 secondes, puis après 16 secondes. Si le réseau était temporairement encombré, ce répit lui laisse le temps de respirer.
2. **La boîte aux rebuts (*Dead Letter Queue* ou Quarantaine)** : Si au bout de quatre tentatives le document ne peut toujours pas être lu, le système abandonne les réessais automatiques. Il range la tâche dans une boîte fermée et alerte un humain : *« Le document #892 est illisible, venez inspecter le dossier »*.

La cuisine ne se bloque pas : le plat défectueux a été mis de côté pour que les autres commandes continuent d'être servies.

---

## Mise en pratique

### Exemple fil rouge : Le parcours d'un devis face à une coupure réseau

Voici la chronique vécue de ce qui se passe sous le capot lors du téléversement d'un devis client de 40 Mo traversant une panne transitoire :

```text
================================================================================
CHRONOLOGIE D'UN TÉLÉVERSEMENT ASYNCHRONE RÉSILIENT
================================================================================

1. 14H02:00 : LE CLIENT DÉPOSE LE DEVIS
   Le client clique sur "Téléverser". Le guichet génère la clé : IDEM-DEV-7845.
   En 1,2 seconde, les octets sont stockés dans le coffre temporaire.
   L'écran affiche immédiatement : "Document reçu sous le n° 7845. Analyse en cours."

2. 14H02:02 : TRANSMISSION EN CUISINE (LA FILE D'ATTENTE)
   Un travailleur d'arrière-plan (worker) prend la tâche dans la file :
   "Contrôler la conformité PDF du document #7845".

3. 14H02:05 : LA PANNE TRANSITOIRE
   Le composant d'analyse PDF subit une surchauffe mémoire et s'arrête net.
   La tâche échoue. 
   Le système ne panique pas : il remet le ticket dans la file avec un délai de 5 secondes.

4. 14H02:10 : LE DEUXIÈME ESSAI RÉUSSI
   Un second travailleur disponible récupère le ticket. L'analyse s'exécute parfaitement.
   Le statut passe à : "VALIDÉ - Prêt pour fabrication".

5. 14H02:12 : LE CLIENT RECHARGÉ SA PAGE
   Inquiet de ne pas voir de résultat, le client clique à nouveau sur "Envoyer".
   Le système voit la clé IDEM-DEV-7845 :
   Au lieu de relancer toute l'analyse, il renvoie en 50 millisecondes :
   "Votre document #7845 est déjà validé et enregistré."
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Tu développes une plateforme de vente en ligne. L'agent d'IA vient de livrer la fonction de confirmation de commande :

> *« Lorsqu'un client valide son panier, ma fonction fait tout en une seule ligne :  
> 1. Elle débite la carte bancaire sur Stripe.  
> 2. Elle génère la facture au format PDF haute résolution (ce qui prend environ 8 secondes).  
> 3. Elle envoie un courriel de confirmation avec le PDF en pièce jointe.  
> 4. Elle met à jour les stocks dans la base de données.  
> Tout est regroupé dans la même fonction, c'est très compact et facile à lire ! »*

### Les questions du pilote

Face à ce château de cartes séquentiel, le pilote identifie les failles majeures :

1. **La question du temps de blocage** : L'utilisateur doit attendre 10 à 15 secondes devant son écran figé pour savoir si sa commande est prise en compte.
2. **La question de la panne intermédiaire** : Que se passe-t-il si la carte bancaire est débitée à l'étape 1, mais que le serveur de courriels tombe en panne à l'étape 3 ? *(Le client a payé, mais le stock n'est pas mis à jour et la commande n'apparaît nulle part !)*.
3. **L'absence totale de déduplication** : Si le client s'impatiente au bout de 6 secondes et clique à nouveau sur son écran, la fonction recommence depuis le début et le débite une seconde fois.

### Le corrigé commenté

**La décision du pilote** : Rejet catégorique de l'architecture synchrone en cascade.

Tu ordonnes à l'agent :  
*« Cette séquence est beaucoup trop fragile. Découpe immédiatement l'opération en deux temps distincts :  
1. **La phase synchrone ultra-courte (moins de 500 ms)** : Valider le panier, vérifier la clé d'idempotence, débiter la carte, enregistrer la commande en base et afficher la page de remerciement au client.  
2. **La phase asynchrone en arrière-plan** : Déposer un message dans une file d'attente pour que la génération du PDF et l'envoi de l'email soient pris en charge par un travailleur d'arrière-plan. Si le service d'email est en panne, la commande reste acquise et le travailleur réessaiera dans une minute sans impacter l'acheteur. »*

Cette séparation rend ton commerce invulnérable aux pannes temporaires de ses prestataires.

---

## Checklist réflexe du pilote

Avant d'autoriser la mise en production d'une tâche lourde, vérifie ces cinq règles de résilience :

- [ ] **Les opérations lourdes sont asynchrones** : Tout traitement dépassant une seconde (génération de document, emails en masse, calculs d'analyse) tourne en arrière-plan.
- [ ] **L'utilisateur a un ticket immédiat** : L'écran confirme la réception de la demande en moins d'une seconde avec un identifiant clair.
- [ ] **La clé d'idempotence protège les paiements** : Un double clic ou une reprise sur coupure de réseau ne crée jamais de transaction financière en double.
- [ ] **Les réessais sont intelligents** : Le système espace ses tentatives de reprise et ne bombarde pas un service en panne.
- [ ] **La mise en quarantaine existe** : Les tâches définitivement en échec sont stockées à l'écart avec une alerte sans bloquer le reste de l'activité.

---

## Sources et limites

Ce chapitre approfondit les mécanismes de découplage temporel et de tolérance aux pannes :
- **O-MD §1, §2, §12 et §13** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : L'idempotence, les quatre mouvements fondamentaux, les files de messages et la résilience opérationnelle.
- **I-MD §6, §11.2 et §11.3** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : Les limites du modèle synchrone, le Transactional Outbox Pattern, les clés d'idempotence strictes et les stratégies de réessais avec Full Jitter.

Pour explorer l'implémentation formelle du Transactional Outbox Pattern, les algorithmes de backoff exponentiel et la manipulation des files de rebut en Python 3.11, poursuis vers le chapitre miroir : **[B07 — Gérer l'asynchronisme et les reprises](/ingenieure/07-asynchronisme-et-reprises)**.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/projet/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A07](/redaction/a07-asynchronisme-et-reprises).
