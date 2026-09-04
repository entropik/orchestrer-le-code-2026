#!/usr/bin/env python3
"""
scripts/ask_matt.py — Aiguilleur d'ingénierie agentique en ligne de commande.

Usage:
    python3 scripts/ask_matt.py
    python3 scripts/ask_matt.py --situation bug
    python3 scripts/ask_matt.py --list
"""

import sys
import argparse

SCENARIOS = {
    "1": {
        "id": "feature",
        "title": "Nouvelle fonctionnalité ou idée en tête",
        "skill": "/grill-with-docs",
        "cmd": '/grill-with-docs "Votre intention de fonctionnalité"',
        "pipeline": [
            "/grill-with-docs",
            "Doute UI/Automate ? (/handoff -> /prototype -> /handoff)",
            "/to-prd",
            "/to-issues (tranches verticales)",
            "/clear (vidage contexte)",
            "/implement (avec /tdd)",
            "/review (Standards + Spécification)"
        ],
        "action": (
            "Pose des questions une par une avec sa réponse recommandée après avoir inspecté le code. "
            "Aligne le glossaire dans CONTEXT.md et acte les décisions structurantes dans docs/adr/."
        ),
        "pitfall": (
            "Ne commencez JAMAIS à coder avant d'avoir traversé /to-prd et /to-issues. "
            "Un agent lancé sans ticket vertical dérive rapidement dans l'architecture horizontale."
        )
    },
    "2": {
        "id": "bug",
        "title": "Bug dur, intermittent ou régression en production",
        "skill": "/diagnosing-bugs",
        "cmd": "/diagnosing-bugs",
        "pipeline": [
            "1. Commande rouge déterministe (reproduction à 100%)",
            "2. Minimiser le cas de test",
            "3. 3 à 5 hypothèses falsifiables",
            "4. Sondes étiquetées [DEBUG-xxxx]",
            "5. Fix minimal + Test de non-régression à la frontière publique",
            "6. Si couture absente : /improve-codebase-architecture"
        ],
        "action": (
            "Refuse toute spéculation tant qu'une boucle de rétroaction courte et déterministe "
            "(une commande unique qui échoue) n'est pas acquise. Corrige à la frontière publique."
        ),
        "pitfall": (
            "Ne laissez jamais l'agent modifier du code au hasard pour 'voir si ça passe'. "
            "Exigez d'abord la preuve de la reproduction rouge."
        )
    },
    "3": {
        "id": "triage",
        "title": "Tickets & retours utilisateurs en vrac",
        "skill": "/triage",
        "cmd": "/triage",
        "pipeline": [
            "Ticket entrant brut",
            "Contrôle antériorité (.out-of-scope/)",
            "Reproduction minimale",
            "Attribution rôle (ready-for-agent / wontfix / needs-info)",
            "/implement"
        ],
        "action": (
            "Passe au crible les tickets ou PRs soumis par des tiers. Contrôle la cohérence avec le périmètre exclu, "
            "reproduit la panne et formate le ticket pour qu'il soit directement traitable par l'agent."
        ),
        "pitfall": (
            "Ne passez JAMAIS par /triage les tickets générés par /to-issues ! Les vôtres sont déjà agent-ready. "
            "/triage est exclusivement réservé aux tickets arrivant de l'extérieur."
        )
    },
    "4": {
        "id": "fog",
        "title": "Brouillard complet / Chantier massif aux multiples inconnues",
        "skill": "/wayfinder (decision-mapping)",
        "cmd": "/decision-mapping",
        "pipeline": [
            "DECISION_MAP.md",
            "Tickets typés (Research / Prototype / Grilling)",
            "1 session = 1 ticket résolu (décisions, pas livrables)",
            "Clôture impérative par /handoff",
            "Brouillard dissipé -> /to-prd -> /to-issues"
        ],
        "action": (
            "Établit une carte de tickets de décision ('decisions, not deliverables') sur l'issue tracker. "
            "Pousse le brouillard pas à pas, sans chercher à coder l'application finale en une fois."
        ),
        "pitfall": (
            "Ne cherchez pas à implémenter durant la cartographie. Ne résolvez qu'une seule décision par session, "
            "et clôturez obligatoirement par /handoff."
        )
    },
    "5": {
        "id": "panic",
        "title": "L'agent s'égare / Réponse en jargon ou hors sujet",
        "skill": "/wait-what",
        "cmd": "/wait-what",
        "pipeline": [
            "Arrêt d'urgence immédiat",
            "Recadrage en français limpide",
            "Alignement strict sur le glossaire CONTEXT.md",
            "Reprise de la session sur base saine"
        ],
        "action": (
            "Stoppe la dérive cognitive de l'agent. Celui-ci s'arrête, analyse ce qui n'a pas été compris et "
            "ré-explique sa position sans jargon, en utilisant uniquement les termes validés dans CONTEXT.md."
        ),
        "pitfall": (
            "Ne tentez pas d'argumenter au milieu d'une explication confuse : le contexte continue de se polluer. "
            "Déclenchez immédiatement /wait-what pour réinitialiser la communication."
        )
    },
    "6": {
        "id": "thirdparty",
        "title": "Bloqué par un tiers (la réponse est chez le client / collègue)",
        "skill": "/to-questionnaire",
        "cmd": "/to-questionnaire",
        "pipeline": [
            "Identification du gap de savoir",
            "Interview sur le destinataire et l'attendu",
            "Génération d'un questionnaire ciblé et structuré",
            "Réponses reçues réinjectées dans /grill-with-docs ou /to-prd"
        ],
        "action": (
            "S'active quand l'inconnue se trouve dans la tête d'un client, d'un collègue ou d'un expert métier. "
            "Génère un questionnaire précis et percutant pour lever l'ambiguïté sans réunion inutile."
        ),
        "pitfall": (
            "Ne présumez pas de la réponse du client dans votre code. Quand un choix commercial ou métier est inconnu, "
            "produisez le questionnaire avant d'écrire la moindre ligne."
        )
    },
    "7": {
        "id": "manual",
        "title": "Action humaine & Secrets (OAuth, Stripe, Cloud, console web)",
        "skill": "/wizard",
        "cmd": "/wizard",
        "pipeline": [
            "Étape manuelle identifiée",
            "Génération d'un script Bash interactif",
            "Ouverture guidée des URLs dans le navigateur",
            "Saisie masquée des secrets",
            "Stockage automatique dans .env / GitHub Secrets"
        ],
        "action": (
            "Prend le relais lorsque l'agent atteint une limite d'autonomie (cliquer dans une console AWS/Stripe, "
            "générer une clé API, basculer un DNS). Génère un script interactif qui vous guide pas à pas."
        ),
        "pitfall": (
            "Ne fournissez jamais vos identifiants administrateurs maîtres dans le chat. "
            "Utilisez /wizard pour que l'opération humaine reste cloisonnée et vos secrets sécurisés."
        )
    },
    "8": {
        "id": "gitconflict",
        "title": "Conflits Git lors d'un rebase ou d'un merge",
        "skill": "/resolving-merge-conflicts",
        "cmd": "/resolving-merge-conflicts",
        "pipeline": [
            "Arrêt de tout git merge --abort",
            "Analyse de l'intention des deux branches (sources primaires)",
            "Résolution hunk par hunk",
            "Validation obligatoire par la suite de tests",
            "Commit de fusion propre"
        ],
        "action": (
            "Résout le conflit en remontant aux sources primaires (l'intention de chaque commit) plutôt qu'en arbitrant "
            "ligne par ligne. Ne valide la résolution qu'après passage au vert de la suite de tests."
        ),
        "pitfall": (
            "Ne faites jamais un git merge --abort par panique. "
            "Laissez le skill inspecter l'historique et valider la réconciliation par les tests unitaires."
        )
    }
}

def print_result(s):
    print("\n" + "=" * 68)
    print(f"  SKILL RECOMMANDÉ : {s['skill']}")
    print("=" * 68)
    print(f"\n👉 COMMANDE À COPIER :\n   \033[1;32m{s['cmd']}\033[0m\n")
    print("📍 PIPELINE D'INGÉNIERIE :")
    for idx, step in enumerate(s['pipeline'], 1):
        print(f"   {idx}. {step}")
    print("\n💡 ACTION DE L'AGENT :")
    print(f"   {s['action']}")
    print("\n⚠️  PIÈGE MORTEL À ÉVITER :")
    print(f"   \033[1;31m{s['pitfall']}\033[0m")
    print("=" * 68 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Aiguilleur d'ingénierie agentique (ask-matt)")
    parser.add_argument("--situation", "-s", help="Identifiant direct (ex: feature, bug, triage, fog, panic, thirdparty, manual, gitconflict)")
    parser.add_argument("--list", "-l", action="store_true", help="Lister les situations disponibles")
    args = parser.parse_args()

    if args.list:
        for k, s in SCENARIOS.items():
            print(f"[{k}] {s['id']:<12} : {s['title']}")
        return

    if args.situation:
        match = next((s for s in SCENARIOS.values() if s['id'] == args.situation), None)
        if match:
            print_result(match)
            return
        print(f"Erreur : situation '{args.situation}' inconnue. Utilisez --list.")
        sys.exit(1)

    print("\n┌────────────────────────────────────────────────────────┐")
    print("│         ASK-MATT — ROUTEUR D'INGÉNIERIE AGENTIQUE      │")
    print("└────────────────────────────────────────────────────────┘")
    print("Quelle est votre situation actuelle ?\n")
    for k, s in SCENARIOS.items():
        print(f"  [{k}] {s['title']}")
    print("  [q] Quitter\n")

    try:
        choice = input("Votre choix (1-8) : ").strip().lower()
        if choice in ('q', 'quit', 'exit'):
            print("Au revoir.")
            return
        if choice in SCENARIOS:
            print_result(SCENARIOS[choice])
        else:
            print("Choix invalide.")
    except (KeyboardInterrupt, EOFError):
        print("\nSession interrompue.")

if __name__ == "__main__":
    main()
