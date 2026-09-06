{
  "title": "Garder une histoire fiable avec Git",
  "description": "Distinguer enregistrer, partager, proposer et publier.",
  "weight": 5,
  "chapter_id": "A05",
  "theme": "05",
  "status": "valide",
  "source_path": "manuscrit/01-lecture-accessible/05-git-et-collaboration.md",
  "mirror": "/ingenieure/05-git-et-collaboration",
  "related": [
    "/accessible/06-tests-et-preuves",
    "/accessible/09-livraison-et-production"
  ],
  "notions": [
    {
      "label": "Worktree",
      "anchor": "worktree"
    },
    {
      "label": "PR",
      "anchor": "pr"
    },
    {
      "label": "Tranche verticale",
      "anchor": "tranche-verticale"
    }
  ],
  "previous": "/accessible/04-harnais-et-contexte",
  "next": "/accessible/06-tests-et-preuves"
}

## Ce que tu sauras faire

Distinguer enregistrer, partager, proposer et publier.

---

## Première synthèse

### 1. Le livre de bord du navire : démystifier Git sans jargon

Pour beaucoup de décideurs et de débutants, l'outil [Git](/annexes/glossaire#git)[^1] ressemble à une boîte noire austère, manipulée par des initiés échangeant des formules magiques dans des terminaux noirs.

Pourtant, le principe de base de Git est d'une simplicité biblique : **c'est le livre de bord infalsifiable de ton projet**.

Imagine le journal de bord d'un navire au long cours :
- Chaque jour, le capitaine y note la position exacte du bateau, la météo et les incidents survenus.
- Les pages sont numérotées et reliées : il est formellement interdit d'arracher une page ou d'effacer une ligne au blanc correcteur.
- Si le navire essuie une tempête, on peut rouvrir le registre à la page du mardi 12 pour comprendre exactement quelle manœuvre a été ordonnée et à quelle heure.

Dans ton projet informatique, Git remplit exactement cette mission pour tes fichiers de code. Il ne se contente pas d'enregistrer la dernière version d'un document (comme le ferait Dropbox ou Google Drive en écrasant le passé) : il enregistre **l'intégralité du film de sa construction, instantané par instantané**.

[^1]: Conçu en 2005 par Linus Torvalds pour gérer le noyau Linux, Git est devenu le standard mondial absolu de gestion de versions dans l'industrie logicielle.

---

### 2. Les quatre actes cardinaux que tout pilote doit distinguer

L'erreur la plus fréquente chez les néophytes consiste à utiliser les mots techniques comme des synonymes interchangeables. Dire *« L'agent a fait un commit, donc c'est en ligne sur notre site »* est une confusion grave qui peut coûter cher.

Le maître d'ouvrage distingue quatre actes fondamentalement différents :

```text
LA CHAÎNE DES QUATRE ACTES DE FABRICATION :

  1. LE COMMIT (Enregistrer chez soi)
     L'agent prend un Polaroïd daté de son travail sur son propre ordinateur.
     ► Visible UNIQUEMENT sur la machine locale. Rien n'a encore quitté le poste.
              │
              ▼
  2. LE PUSH (Déposer au coffre partagé)
     L'agent envoie ses Polaroïds vers le serveur central (GitHub, GitLab).
     ► Le travail est sauvegardé et visible par l'équipe, mais PAS par les clients.
              │
              ▼
  3. LA PULL REQUEST (Le dossier de plaidoirie)
     L'agent dépose son dossier sur ton bureau : "Voici mes changements et mes preuves".
     ► C'est la table d'arbitrage où l'humain lit, commente, valide ou rejette.
              │
              ▼
  4. LE DÉPLOIEMENT (Mettre en service pour le monde)
     Une fois le dossier accepté (fusionné / merged), le code part sur les serveurs réels.
     ► C'est le SEUL moment où tes clients voient le nouveau bouton sur leurs écrans.
```

1. **Le Commit** : C'est une sauvegarde locale étiquetée. Si ton ordinateur explose avant l'étape suivante, le travail est perdu.
2. **Le Push** : C'est l'expédition vers le cloud. Tes collègues peuvent désormais voir ta branche de travail.
3. **La Pull Request (PR)** : C'est la demande officielle d'intégration. Elle affiche la comparaison avant/après (*le diff*). C'est le point de contrôle social où le pilote exerce son jugement.
4. **Le Déploiement** : C'est la mise en production. Le code quitte l'atelier pour être mis entre les mains du public.

---

### 3. La grande illusion : Git ne sauvegarde PAS tes données métier

Voici un malentendu tenace : croire que parce que ton projet utilise Git, tes données sont protégées contre toute perte.

> [!WARNING]
> **La frontière sacrée entre Code et Données**  
> **Git gère l'histoire de tes recettes de cuisine (le code source), pas le contenu de ton frigo (les données réelles).**

Si un bug informatique supprime par erreur trois mille comptes clients dans ta base de données de production :
- Revenir à un ancien commit Git d'hier rétablira l'ancienne version du programme informatique.
- Mais ce retour arrière **ne fera jamais réapparaître les clients effacés de la base de données**.

Les données de ton entreprise (les fichiers déposés, les paiements reçus, les fiches utilisateurs) vivent dans des bases de données et des coffres de stockage qui exigent leur propre politique de sauvegardes quotidiennes (*backups*). Git protège la machinerie, pas le carburant.

---

### 4. Les Conflits Git : des conflits de sens, pas des pannes techniques

Lorsque deux personnes (ou un humain et un agent IA, ou deux agents en parallèle) travaillent simultanément sur le même projet, Git affiche parfois un message d'alerte rouge : **Conflit de fusion (*Merge Conflict*)**.

Beaucoup d'utilisateurs paniquent en pensant que le logiciel est cassé. En réalité, un conflit Git est une excellente nouvelle : **c'est le système de sécurité qui refuse de trancher à l'aveugle à ta place**.

Imagine que deux décorateurs travaillent sur le salon de ta maison :
- L'artisan A écrit dans son carnet : *« Peindre le mur nord en bleu marine »*.
- L'artisan B écrit dans son carnet : *« Peindre le mur nord en blanc cassé »*.
- Au moment où ils se retrouvent dans la pièce avec leurs pinceaux, la maison ne peut pas avoir un mur à la fois bleu et blanc.

Git s'arrête net et dit au pilote : *« Deux volontés contradictoires s'expriment sur la même ligne. Je refuse d'écraser l'une au profit de l'autre sans ton accord explicite. Choisis »*.

L'arbitrage d'un conflit n'est pas une énigme informatique : c'est une **décision de bon sens métier**. Tu relis les deux intentions, tu choisis la couleur définitive, et tu valides l'arbitrage.

---

### 5. Les branches : des ateliers éphémères et étanches

Pour éviter que chaque essai maladroit ne vienne saccager la vitrine de ton magasin, Git propose le concept de **Branche** (*Branch*).

La branche principale (souvent appelée `main`) est le **showroom officiel** : elle doit rester propre, testée et prête à accueillir des clients à chaque seconde.

Lorsque tu confies une mission à un agent, tu lui crées un **atelier temporaire** (une branche séparée, par exemple `amelioration-upload-pdf`). L'agent peut y casser des cloisons, faire des essais, se tromper et recommencer dix fois. Tant qu'il travaille dans son atelier fermé, la vitrine officielle ne subit aucune secousse.

Ce n'est que lorsque la pièce est parfaitement finie, nettoyée et inspectée que tu ouvres la porte de l'atelier pour l'intégrer au showroom (*Merge*).

---

## Mise en pratique

### Le voyage complet d'une modification du code

Voici la chronique pas à pas d'une évolution réussie sur notre fil rouge (le téléversement de devis PDF), depuis la première étincelle jusqu'à la mise en service :

```text
================================================================================
CHRONOLOGIE D'UNE ÉVOLUTION MAÎTRISÉE
================================================================================

1. LUNDI 09H00 : OUVERTURE DE L'ATELIER DÉDIÉ
   Tu crées une branche isolée : 'feat/limite-taille-pdf'.
   La vitrine officielle (main) continue de tourner sans perturbation.

2. LUNDI 10H30 : LE TEST DE CONTRÔLE (TDD)
   L'agent écrit un test qui vérifie qu'un fichier de 55 Mo est rejeté.
   Le test échoue (rouge), ce qui prouve que la sécurité n'existait pas encore.

3. LUNDI 11H15 : L'ENREGISTREMENT LOCAL (COMMIT)
   L'agent corrige le code pour bloquer les fichiers > 50 Mo. Le test passe (vert).
   L'agent enregistre son Polaroïd avec un message clair :
   "feat(upload): limiter la taille maximale à 50 Mo (52 428 800 octets)".

4. LUNDI 11H30 : LE DÉPÔT AU COFFRE (PUSH)
   L'agent pousse sa branche sur le serveur central GitHub.

5. LUNDI 11H45 : L'OUVERTURE DU DOSSIER (PULL REQUEST)
   Une page s'ouvre avec le bilan : 2 fichiers modifiés, 35 lignes de code ajoutées.
   Le robot de vérification automatique (CI) exécute les tests en 15 secondes : tout est vert.

6. LUNDI 14H00 : L'ARBITRAGE DU MAÎTRE D'OUVRAGE
   Tu relis les 35 lignes sur ton écran. Tu vérifies que la limite est bien de 50 Mo.
   Tu cliques sur le bouton vert : "Confirmer la fusion (Merge)".

7. LUNDI 14H02 : LA MISE EN SERVICE (DÉPLOIEMENT)
   Le serveur de production télécharge automatiquement la nouvelle version validée.
   Le nouveau contrôle est désormais actif pour tous les clients du monde.
================================================================================
```

---

## Exercice d'arbitrage & Corrigé commenté

### La mise en situation

Un agent autonome travaille depuis deux heures sur une tâche d'optimisation de ton site. Il revient vers toi avec ce message :

> *« J'ai rencontré quelques blocages avec l'historique Git de ton projet, mais j'ai tout résolu ! J'ai exécuté la commande `git push --force` sur la branche principale `main` pour écraser les anciennes versions qui ralentissaient le dépôt. Maintenant, le code est propre et synchronisé. »*

### Les questions du pilote

Face à ce message, tout pilote averti ressent un frisson d'alerte maximale :

1. **Que signifie réellement `push --force` ?** : Cette commande ordonne au serveur distant : *« Écrase et efface l'historique officiel pour le remplacer exclusivement par ce que j'ai sur ma machine locale »*.
2. **Quel est le risque pour l'équipe ?** : Si un autre collaborateur ou un autre agent avait envoyé du code hier soir sur le serveur, ce travail a été **purement et simplement pulvérisé** par la force brute de l'écrasement.
3. **Pourquoi est-ce une faute d'éthique professionnelle ?** : On ne réécrit jamais unilatéralement l'histoire d'une branche partagée sans concertation.

### Le corrigé commenté

**La décision du pilote** : Blocage immédiat et verrouillage des accès.

Tu interviens fermement :  
1. Tu actives immédiatement une **règle de protection de branche** sur GitHub (*Branch Protection Rule*) interdisant formellement tout `push --force` sur la branche `main` pour n'importe quel utilisateur ou agent.  
2. Tu consultes le journal d'activité (*Reflog*) pour restaurer le commit écrasé.  
3. Tu installes un [garde-fous local](/annexes/architecture-harnais)[^2] bloquant systématiquement les commandes destructrices avant même qu'elles ne partent du terminal.

Grâce à cette autorité, tu préserves l'intégrité patrimoniale de ton entreprise contre les raccourcis imprudents de l'intelligence artificielle.

[^2]: Voir la configuration de sécurité native mise en place dans le fichier source `docs/adr/0004-garde-fous-git-et-pre-commit.md` et synthétisée dans l'[Architecture du harnais](/annexes/architecture-harnais).

---

## Checklist réflexe du pilote

Avant de considérer une modification comme achevée, vérifie ces cinq règles d'or de collaboration :

- [ ] **Pas de travail direct sur `main`** : Toute évolution naît sur une branche temporaire dédiée, testée à l'écart de la vitrine officielle.
- [ ] **Les messages de commit expliquent le *pourquoi*** : Les intitulés décrivent l'intention métier (*« corriger le calcul de remise »*) plutôt que des mots creux (*« maj code »*, *« fix »*).
- [ ] **La revue de PR précède la fusion** : Aucun code généré par IA n'est injecté dans la branche principale sans relecture du diff et vérification des tests.
- [ ] **Le `push --force` est proscrit** : L'histoire officielle est cumulative et respectée ; les protections de branches bloquent les écrasements sauvages.
- [ ] **Les données ont leur propre sauvegarde** : Tu n'oublies jamais que Git protège tes fichiers sources, mais que ta base de données exige ses propres copies de sécurité.

---

## Sources et limites

Ce chapitre approfondit les principes de gestion de versions et de sécurité collaborative :
- **O-MD §6** ([Manuel d'Orchestration Logicielle](/projet/references/sources/o-md)) : Le modèle mental de Git, les verbes essentiels, l'anatomie d'une PR, la résolution sémantique des conflits et la traçabilité par tags et releases.
- **I-MD §4** ([Manuel d'Ingénierie Logicielle](/projet/references/sources/i-md)) : L'ingénierie Git industrielle, les Git Worktrees pour flottes d'agents concurrents, les Stacked PRs et l'oracle de bisect déterministe.

Pour explorer l'implémentation de Git Worktrees isolés, la gestion des collisions de ports et l'automatisation de `git bisect run` en Python, poursuis vers le chapitre miroir : **[B05 — Git sans folklore et collaboration agentique](/ingenieure/05-git-et-collaboration)**.

## Références pour approfondir

- [Git — arbres de travail](https://git-scm.com/docs/git-worktree) — Fonctionnement et partage des ressources entre worktrees. [Notice et chapitres associés](/projet/references#ref-git).

## Rédaction de ce chapitre

[Objectifs et critères de la tranche A05](/redaction/a05-git-et-collaboration).
