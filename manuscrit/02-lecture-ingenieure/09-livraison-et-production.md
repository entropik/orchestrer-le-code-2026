# B09 - Passer du poste local à un service réel

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/09-livraison-et-production.md) · [Fiche de rédaction](../../tranches/B09-livraison-et-production.md)

## Ce que tu sauras faire

Définir une chaîne de livraison traçable avec compatibilité, santé et limites d'infrastructure.

## Première synthèse

Le pipeline construit et vérifie un artefact, puis le promeut avec une configuration maîtrisée. Un tag contenant un SHA reste une convention de nommage : l'identité de l'image se contrôle par son digest. Les migrations et les paramètres nécessaires font partie de la traçabilité de la livraison.

Une bascule sans coupure dépend de la capacité disponible, de la compatibilité du schéma, de la disponibilité réelle de la nouvelle instance et du drainage de l'ancienne. Un rechargement du reverse proxy ne prouve pas à lui seul la continuité du service. Les sondes doivent distinguer processus vivant et aptitude à servir le trafic.

Les exemples de configuration doivent annoncer leurs prérequis. Le module de limitation de débit Caddy cité dans les sources n'est pas livré avec la distribution standard. Les permissions des secrets doivent être testées avec l'identité effective du processus qui les lit, et non déduites de la seule présence d'un fichier d'environnement.

## Déroulé prévu

1. CI, dépendances verrouillées et artefact identifié par digest.
2. VPS, reverse proxy, réseau et persistance.
3. Configuration, secrets et privilèges minimaux.
4. Staging, bascule, drainage et rollback compatible.

## Mise en pratique

Spécifier les étapes de livraison et un scénario d'échec au moment de la bascule.

## Critère de réussite

La version, la migration et l'image réellement servies sont retrouvables ; les prérequis de configuration sont explicites.

## Sources et limites

[O-MD §8](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §8, §10.2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
