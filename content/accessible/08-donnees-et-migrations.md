{
  "title": "Protéger les données et faire évoluer leur structure",
  "description": "Comprendre pourquoi les données demandent une prudence différente de celle du code.",
  "weight": 8,
  "chapter_id": "A08",
  "theme": "08",
  "status": "redaction",
  "source_path": "manuscrit/01-lecture-accessible/08-donnees-et-migrations.md",
  "mirror": "/ingenieure/08-donnees-et-migrations",
  "related": [
    "/accessible/07-asynchronisme-et-reprises",
    "/accessible/09-livraison-et-production"
  ],
  "notions": [
    {
      "label": "Migration",
      "anchor": "migration"
    },
    {
      "label": "RPO",
      "anchor": "rpo"
    },
    {
      "label": "RTO",
      "anchor": "rto"
    }
  ],
  "previous": "/accessible/07-asynchronisme-et-reprises",
  "next": "/accessible/09-livraison-et-production"
}

## Ce que tu sauras faire

Comprendre pourquoi les données demandent une prudence différente de celle du code.

---

## Première synthèse

### 1. Le déménagement de la bibliothèque : pourquoi le code se remplace, mais pas les données

Dans le monde du logiciel, il existe une différence fondamentale que tout pilote doit graver dans son esprit :
- **Le code est remplaçable à volonté** : Si une nouvelle version de ton programme ne fonctionne pas, une seule commande Git (`git revert`) permet de revenir à la version d'hier en trois secondes. Le code est léger, jetable et sans mémoire.
- **Les données sont irremplaçables et vivantes** : Les factures de tes clients, les devis déposés, les comptes utilisateurs et l'historique bancaire ne peuvent pas être « réinitialisés ». Si une mauvaise commande efface ou mélange ces données, aucune commande magique ne viendra les ressusciter sans dégâts considérables.

Imagine la rénovation d'une grande bibliothèque publique contenant cent mille ouvrages rares.

Si l'architecte veut repeindre les murs du hall d'accueil, il peut le faire dans la nuit : au pire, si la couleur déplaît, on applique une autre couche le lendemain. C'est l'équivalent d'une modification de code.

Mais s'il décide de changer tout le système de classement des livres pour passer de l'ordre alphabétique à l'ordre thématique, il ne peut pas jeter tous les rayonnages par la fenêtre un vendredi soir en espérant que tout sera rangé le lundi matin. Pendant les travaux, les lecteurs continuent d'entrer, d'emprunter des livres et d'en rapporter. Si un livre est mal étiqueté pendant la transition, il est perdu à jamais dans les réserves.

Faire évoluer une base de données en production (ce que l'on appelle une **[Migration](/annexes/glossaire#migration)**) exige cette infinie délicatesse : **changer le mobilier sans jamais empêcher les clients d'accéder à leurs dossiers**.

---

### 2. Le mystère de la dernière place de concert : la contrainte d'unicité

Prenons une situation classique : il reste exactement **un seul billet** pour un festival très prisé.

À 10 h 00 min 00 s, Sophie et Thomas cliquent exactement à la même milliseconde sur le bouton *« Acheter la dernière place »*.

Si ton application est conçue avec naïveté, voici ce qui se passe :
1. L'écran de Sophie demande au système : *« Reste-t-il une place ? »*. Le système répond : *« Oui, il en reste 1 »*.
2. L'écran de Thomas demande au même instant : *« Reste-t-il une place ? »*. Le système répond : *« Oui, il en reste 1 »*.
3. L'écran de Sophie enregistre l'achat.
4. L'écran de Thomas enregistre l'achat.
5. **Catastrophe** : Tu as vendu deux fois le même fauteuil. Deux spectateurs vont se battre à l'entrée de la salle.

Pourquoi cette catastrophe s'est-elle produite ? Parce que l'agent d'IA a placé la vérification au niveau de l'écran ou d'un simple calcul temporaire.

Pour empêcher les doublons, la règle ne doit pas vivre dans l'écran : elle doit être **gravée au fer rouge dans le coffre-fort de la base de données sous la forme d'une Contrainte d'Unicité ([Invariant](/annexes/glossaire#invariant))**.

La base de données agit comme un tourniquet mécanique impitoyable : quand deux personnes se présentent en même temps, le tourniquet ne laisse passer qu'un seul corps. Le premier achat est validé, et la tentative concurrente est instantanément refoulée avec un message courtois : *« Désolé, ce billet vient d'être attribué à un autre acheteur »*.

---

### 3. La méthode du pont suspendu : le pattern Élargir - Transiter - Contracter

Quand une entreprise souhaite modifier le rangement de ses données (par exemple, séparer un champ `nom_complet` en deux champs distincts `prenom` et `nom_de_famille`), un agent inexpérimenté propose souvent une commande brutale :
> *« C'est facile, je vais renommer la colonne dans la base de données dès ce soir ! »*

C'est l'assurance d'un crash généralisé. Pourquoi ? Parce que pendant les quelques minutes où le nouveau code est en cours de déploiement sur les serveurs, les anciennes versions de l'application continuent de chercher l'ancienne colonne et tombent en panne immédiate.

L'ingénierie moderne applique la technique du **pont suspendu**, connue sous le nom de pattern **Élargir - Transiter - Contracter (*Expand-Contract*)**[^1] :

```text
LES TROIS PHASES D'UNE MIGRATION SANS COUPURE (EXPAND-CONTRACT) :

  PHASE 1 : ÉLARGIR (EXPAND)
  On ajoute les nouvelles colonnes ("prenom", "nom") à côté de l'ancienne.
  ► L'application actuelle continue de tourner sans s'apercevoir de rien.
            │
            ▼
  PHASE 2 : TRANSITER (DOUBLE ÉCRITURE & REMPLISSAGE)
  La nouvelle version du code est déployée :
  • Tout nouveau client est écrit dans l'ANCIEN ET le NOUVEAU format.
  • Un petit robot d'arrière-plan recopie tranquillement les 50 000 anciens dossiers.
            │
            ▼
  PHASE 3 : CONTRACTER (CONTRACT)
  Une fois que 100 % des données sont vérifiées dans le nouveau format :
  • L'application bascule exclusivement sur le nouveau rangement.
  • On supprime proprement l'ancienne colonne devenue inutile.
```

Grâce à cette discipline en trois temps, ton site ne subit **aucune seconde d'interruption de service** (*Zero-Downtime Migration*), et aucun client ne se retrouve face à un écran blanc.

[^1]: Formalisé par Pramod Sadalage et Martin Fowler dans *Refactoring Databases: Evolutionary Database Design*, Addison-Wesley, 2006.

---

### 4. Sauvegardes, RPO et RTO : l'art de mesurer le pire

Dans la vie d'une entreprise numérique, la question n'est pas de savoir *si* un serveur va tomber en panne un jour, mais *quand* cela va arriver.

Pour piloter la sécurité de tes données, tu n'as pas besoin de connaître le langage SQL. Tu dois maîtriser deux sigles universels :

```text
LES DEUX CADRANS DE LA SÉCURITÉ DES DONNÉES :

     RPO (Recovery Point Objective)            RTO (Recovery Time Objective)
       « Combien de données puis-je               « Combien de temps puis-je
            me permettre de perdre ? »                rester en panne ? »
  ┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
  │ Exemple : Sauvegarde 1 fois par jour │  │ Exemple : Panne survenue à 14h00     │
  │ Si le serveur brûle à 23h59, tu perds│  │ Combien de minutes pour réinstaller  │
  │ 23 heures et 59 minutes d'achats !   │  │ le système et réouvrir la boutique ? │
  │ ► Trop risqué pour un commerce.      │  │ ► Objectif : moins de 30 minutes.    │
  └──────────────────────────────────────┘  └──────────────────────────────────────┘
```

- **Le RPO (Perte maximale tolérée)** : Si ton activité génère des ventes à chaque minute, une simple sauvegarde quotidienne est insuffisante. Tu dois exiger une sauvegarde continue des journaux de transactions (ce que les techniciens appellent les logs WAL), permettant de remonter le temps jusqu'à la seconde précédant le crash.
- **Le RTO (Délai de réouverture)** : C'est le temps nécessaire pour brancher une nouvelle machine et recharger les données.

> [!IMPORTANT]
> **La règle d'or du pilote : Le théorème du parachute**  
> Un fichier de sauvegarde qui n'a **jamais été testé en restauration réelle** n'a aucune valeur. C'est un parachute que l'on n'a jamais ouvert.  
> Exige régulièrement de ton équipe ou de tes agents qu'ils fassent l'exercice de restaurer la base sur une machine de test vierge pour prouver que les données reviennent réellement à la vie.

---

## Mise en pratique

### Exemple fil rouge : Faire évoluer le statut du devis sans casser le service

Reprenons notre fil rouge. Au départ, le statut d'un devis était un simple mot binaire : `"EN_ATTENTE"` ou `"VALIDE"`. L'entreprise grandit et l'atelier a désormais besoin de distinguer deux étapes : `"VALIDE_CONFORME"` et `"VALIDE_EN_FABRICATION"`, avec la date exacte de validation.

Voici comment le pilote découpe la migration pour son agent sans risque d'interruption :

```text
================================================================================
PLAN DE MIGRATION EXPAND-CONTRACT POUR LE STATUT DU DEVIS
================================================================================

[ÉTAPE 1 : ÉLARGIR (LIVRAISON DU LUNDI)]
- Créer la nouvelle colonne 'statut_detaille' et 'date_validation'.
- Laisser ces colonnes facultatives (nullable).
- L'application existante continue de lire et d'écrire sur 'statut'.

[ÉTAPE 2 : DOUBLE ÉCRITURE ET SYNCHRONISATION (LIVRAISON DU MARDI)]
- Déployer la nouvelle version du code applicatif :
  * Dès qu'un devis passe à l'état validé, le code écrit :
    statut = 'VALIDE' ET statut_detaille = 'VALIDE_CONFORME'.
  * Le code sait lire 'statut_detaille' s'il existe, ou se rabattre sur 'statut'.
- Lancer un script de fond qui met à jour les 2 000 anciens devis de l'année.

[ÉTAPE 3 : CONTRÔLE DE CONVERGENCE (MERCREDI)]
- Vérifier qu'il ne reste aucun devis avec 'statut_detaille' vide.
- Vérifier que l'atelier voit les nouvelles mentions sans aucune anomalie.

[ÉTAPE 4 : CONTRACTER (LIVRAISON DU JEUDI)]
- Déployer la version finale du code qui ne lit plus que 'statut_detaille'.
- Supprimer proprement l'ancienne colonne 'statut' devenue obsolète.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Un agent autonome travaille sur l'ajout d'un champ obligatoire `numero_tva` pour tous les clients du site. Il t'envoie ce message :

> *« J'ai préparé la migration de la base de données. J'ai ajouté l'instruction suivante :  
> `ALTER TABLE clients ADD COLUMN numero_tva VARCHAR(20) NOT NULL;`  
> Je prévois d'exécuter cette commande directement sur la base de production ce midi, cela prendra moins de dix secondes ! »*

### Les questions du pilote

Face à cette proposition d'une dangerosité extrême, le pilote analyse immédiatement le problème :

1. **Que signifie `NOT NULL` ?** : Cette contrainte ordonne à la base de données : *« Chaque ligne de cette table DOIT OBLIGATOIREMENT avoir un numéro de TVA valide, sans exception possible »*.
2. **Que se passe-t-il pour les 15 000 clients déjà enregistrés ?** : Les clients existants n'ont évidemment pas encore de numéro de TVA dans la base ! La commande SQL va tenter d'insérer une valeur vide dans une colonne qui l'interdit.
3. **Le résultat immédiat** : Soit la commande échoue brutalement en bloquant toute la base de données, soit elle bloque l'inscription de tous les clients existants dès la seconde suivante.

### Le corrigé commenté

**La décision du pilote** : Rejet immédiat et instruction de correction.

Tu ordonnes à l'agent :  
*« Interdiction absolue d'exécuter cette commande. Tu ne peux pas ajouter une colonne obligatoire (`NOT NULL`) sur une table contenant déjà des données historiques sans valeur par défaut.  
Applique la procédure en trois temps :  
1. Ajoute d'abord la colonne comme facultative (`NULLABLE`), ou avec une valeur par défaut temporaire (`DEFAULT 'NON_RENSEIGNE'`).  
2. Permets aux clients de remplir leur numéro de TVA dans leur espace profil.  
3. Ce n'est que lorsque les données existantes seront assainies que nous pourrons envisager de rendre le champ obligatoire pour les nouvelles créations. »*

Cette décision évite un blocage destructeur de ta base commerciale.

---

## Checklist réflexe du pilote

Avant d'autoriser la moindre modification touchant à la structure des données, vérifie ces cinq règles de prudence :

- [ ] **L'expansion précède la contraction** : Aucune colonne n'est renommée ou supprimée brutalement ; la nouvelle structure cohabite avec l'ancienne le temps de la transition.
- [ ] **Les contraintes sont dans la base** : L'unicité des comptes, l'intégrité des montants et les liaisons sont protégées par le moteur de base de données, pas seulement par l'écran.
- [ ] **Pas de `NOT NULL` sauvage** : Toute nouvelle colonne ajoutée sur des données existantes est facultative ou dispose d'une valeur par défaut sensée.
- [ ] **Le RPO et le RTO sont fixés** : L'équipe sait combien d'heures de données sont au maximum exposées et en combien de minutes le service peut être restauré.
- [ ] **Le test de restauration est prouvé** : La sauvegarde a déjà été restaurée avec succès sur une machine de test isolée pour prouver sa validité.

---

## Sources et limites

Ce chapitre approfondit les méthodologies de persistance et de protection des données :
- **O-MD §2, §3, §8, §10 et §13** ([Manuel d'Orchestration Logicielle](/references/sources/o-md)) : L'intégrité transactionnelle, le modèle relationnel, les migrations versionnées et la reprise après incident.
- **I-MD §7** ([Manuel d'Ingénierie Logicielle](/references/sources/i-md)) : Les niveaux d'isolation SQL, les verrous optimistes et pessimistes, le pattern Expand-Contract et la réplication continue par WAL.

Pour explorer la gestion des transactions concurrentes, l'implémentation d'un verrou optimiste et le script d'un backfill en Python 3.11, poursuis vers le chapitre miroir : **[B08 — Structurer les données et réussir les migrations](/ingenieure/08-donnees-et-migrations)**.

## Références pour approfondir

- [PostgreSQL — NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html) — Notifications de sessions ; à distinguer d'une file durable de travaux. [Notice et chapitres associés](/references#ref-notify).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A08](/redaction/a08-donnees-et-migrations).
