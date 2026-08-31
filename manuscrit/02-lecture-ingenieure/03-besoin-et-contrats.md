# B03 - Transformer le besoin en contrat vérifiable

> Lecture ingénieure · Amorce de synthèse, chapitre à développer et à relire.

[Sommaire](../SOMMAIRE.md) · [Lire la version accessible](../01-lecture-accessible/03-besoin-et-contrats.md) · [Fiche de rédaction](../../tranches/B03-besoin-et-contrats.md)

## Ce que tu sauras faire

Relier invariants, schémas, validation à l'exécution et compatibilité des contrats.

## Première synthèse

Le schéma d'une requête ne remplace pas la règle métier. Une taille entière positive peut être syntaxiquement valide tout en dépassant le quota de l'organisation. Le contrat doit donc distinguer validation de structure, autorisation et invariants dépendant de l'état courant.

Définir les schémas avant l'implémentation rend les hypothèses inspectables. Cela n'impose pas de figer définitivement le contrat : une évolution justifiée passe par une décision explicite et des tests de compatibilité. Le compilateur vérifie une partie des usages internes ; les données externes doivent toujours être contrôlées à l'exécution.

Pour l'upload, documenter les unités, les identifiants, les erreurs, l'expiration et la finalisation. La limite pédagogique de 500 Mo doit devenir une quantité précise d'octets avant tout test. Un test qui vérifie seulement la forme du JSON ne prouve ni l'appartenance du fichier ni son intégrité.

## Déroulé prévu

1. SPEC, invariants et ADR.
2. Schémas d'entrée, sortie et erreurs.
3. Typage statique versus parsing à l'exécution.
4. Évolution additive et compatibilité des consommateurs.

## Mise en pratique

Produire les contrats de création et de finalisation de session, avec erreurs et règles d'évolution.

## Critère de réussite

Structure, droits et invariants sont testables séparément ; aucune assertion de type ne sert de validation réseau.

## Sources et limites

[O-MD §3, §12](../../sources/originaux/manuel_orchestration_logicielle.md) ; [I-MD §3, §9.3, §10.2](../../sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md).

Cette amorce est une synthèse éditoriale, pas la preuve d'une implémentation exécutée. Les rectifications et vérifications externes sont consignées dans le [registre critique](../../analyse/03-registre-critique.md). Les exemples techniques restent à développer et à tester dans la tranche.
