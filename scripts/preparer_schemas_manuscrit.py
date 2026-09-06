"""Transposition graphique de tous les schémas ASCII du manuscrit.

Génère data/diagrams/manuscrit.json pour les chapitres de lecture
accessible et ingénieure, ainsi que les annexes.
"""
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slug(text):
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def clean(line):
    line = line.strip().strip("|│").strip()
    line = re.sub(r"^[├└┌]──\s*", "", line).strip()
    return line.removeprefix("• ").strip()


def node(title, lines=(), **extra):
    return dict(kind="node", title=title, lines=list(lines), **extra)


def arrow(label="", direction="down"):
    return dict(kind="arrow", label=label, direction=direction)


def grid(items, **extra):
    return dict(kind="grid", items=items, **extra)


def sequence(nodes):
    result = []
    for n in nodes:
        if result:
            result.append(arrow())
        result.append(n)
    return result


def parse_boxes(lines):
    result, current = [], None
    for line in lines:
        s = line.strip()
        if s.startswith("┌"):
            if current:
                result.append(node(current[0], current[1:]))
            current = []
        elif (s.startswith("├") or s.startswith("┼")) and current:
            result.append(node(current[0], current[1:]))
            current = []
        elif s.startswith("└") and current is not None:
            if current:
                result.append(node(current[0], current[1:]))
            current = None
        elif current is not None and ("│" in line or "|" in line):
            val = clean(line)
            if val:
                current.append(val)
    if current:
        result.append(node(current[0], current[1:]))
    return result


def parse_phases(lines):
    result = []
    current = None
    for line in lines:
        s = line.strip()
        m = re.match(r"^(\d+[\.\)]|PHASE \d+|ÉTAPE \d+)\s*(.*)", s, re.I)
        if m:
            if current:
                result.append(node(current[0], current[1:]))
            current = [clean(s)]
        elif current and (s.startswith("►") or s.startswith("•") or s.startswith("(") or s.startswith("«") or "──►" in s or re.search(r"\w", s)):
            v = clean(s)
            if v and not v.startswith("│") and not v.startswith("▼"):
                current.append(v)
    if current:
        result.append(node(current[0], current[1:]))
    return sequence(result)


def parse_bracket_flow(lines):
    nodes = []
    for line in lines:
        s = line.strip()
        brackets = re.findall(r"\[\s*([^\]]+?)\s*\]", s)
        for b in brackets:
            nodes.append(node(b.strip()))
    return sequence(nodes)


def parse_custom(h, lines, title):
    # 1. B01 : Boucle fermée de rétroaction déterministe
    if h.startswith("5dab7eac"):
        steps = [
            node("1. CADRAGE & MISSION", ["Contexte, SPEC, Invariants", "Périmètre strict et critères de terminaison"]),
            node("2. ACTION STOCHASTIQUE", ["L'agent inspecte le dépôt et produit le code"]),
            node("3. ORACLE INDÉPENDANT", ["Tests, Typage AST, Linter", "(Exécuté hors du modèle, dans l'environnement hôte)"]),
        ]
        branches = grid([
            dict(kind="branch", parts=[
                node("Erreur détectée"),
                arrow(),
                node("Réinjection de la trace pure", ["Trace d'erreur sans bavardage ──► Boucle suivante"]),
            ]),
            dict(kind="branch", parts=[
                node("Succès déterministe"),
                arrow(),
                node("Gel de l'artefact", ["Revue humaine & signature de commit"]),
            ]),
        ])
        return sequence(steps) + [arrow(), branches]

    # 2. B01 : Barrière d'interception matérielle
    if h.startswith("b0fad7e8"):
        nodes = [
            node("Agent (LLM)", ["Propose une commande : git push -f"]),
            node("BARRIÈRE D'INTERCEPTION (PreToolUse Hook)", [
                "Script : .claude/hooks/block-dangerous-git.sh (ADR-0004)",
                "Action : Analyse syntaxique de la commande AVANT transmission au shell.",
            ]),
            node("Évaluation du filtre de sécurité", [
                "Correspondance 'git push' ou '--force' ?\n"
                "• OUI ──► Interception immédiate (Exit Code 2). Message : 'BLOCKED: Opération interdite.'\n"
                "• NON ──► Autorisation d'exécution dans le bac à sable isolé.",
            ]),
        ]
        return sequence(nodes)

    # 2b. Avant-propos : Jauge de faisabilité en solo vs équipe
    if h.startswith("1b531e47"):
        nodes = [
            node("FAISABILITÉ IMMÉDIATE EN SOLO", [
                "Outils internes d'automatisation",
                "Portails de gestion de dossiers clients",
                "Moteurs de génération documentaire (PDF)",
                "Tableaux de bord métier & métriques",
                "Petits commerces & catalogues locaux",
            ]),
            node("EXIGE UNE ÉQUIPE SPÉCIALISÉE", [
                "Systèmes bancaires directs (cœur de banque)",
                "Moteurs de jeux vidéo 3D temps réel",
                "Applications à haute fréquence boursière",
                "Algorithmes de cryptographie sur mesure",
                "Systèmes médicaux à pilotage d'organes",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 3. A01 : Quatre mouvements fondamentaux
    if h.startswith("5eee210a"):
        nodes = [
            node("1. RECEVOIR", ["Une intention qui entre"]),
            node("2. VALIDER", ["Le contrôle de légitimité"]),
            node("3. TRANSFORMER", ["Le calcul ou la recette"]),
            node("4. PERSISTER / RÉPONDRE", ["L'armoire forte ou la trace durable"]),
        ]
        return [grid(nodes, style="comparison")]

    # 4. B02 : Comparaison de profondeur architecturale
    if h.startswith("ae472019"):
        nodes = [
            dict(kind="module", title="MODULE PROFOND (Idéal pour l'IA)", parts=[
                node("INTERFACE MINIMALE : 2 FONCTIONS", ["read(id), write(id, payload)"]),
                node("COMPLEXITÉ INTERNE FORTE (MASQUÉE)", [
                    "Gestion des pools de connexion DB",
                    "Mise en cache LRU mémoire",
                    "Détection des collisions & Locks",
                    "Retry exponentiel sur panne",
                    "Chiffrement AES-256 au vol",
                ]),
            ]),
            dict(kind="module", title="MODULE SUPERFICIEL (Anti-pattern)", parts=[
                node("INTERFACE LARGE : 12 MÉTHODES", ["init(), config(), setBuff(), auth(), lock(), flush(), verify(), clear()..."]),
                node("COMPLEXITÉ INTERNE MINIME", ["(Ne fait que relayer les paramètres vers un autre composant sans véritable transformation)"]),
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 5. B02 : Topologie hexagonale du système
    if h.startswith("55526c84"):
        entry_points = grid([node("REQUÊTE HTTP"), node("APPEL CLI"), node("WEBHOOK TIERS")])
        adapters_in = node("ADAPTATEURS PRIMAIRES (DRIVING)", ["(Fastify Controller, CLI Command, Message Consumer)"])
        domain_core = node("DOMAINE MÉTIER PUR (HEXAGONE CENTRAL)", [
            "Entités, Invariants, Règles métier immuables",
            "(ZÉRO dépendance vers Fastify, SQL, Réseau ou Disque)",
        ])
        adapters_out = node("ADAPTATEURS SECONDAIRES (DRIVEN)", ["(PostgresRepository, S3BlobStorage, SendgridMailer)"])
        return [entry_points, arrow(), adapters_in, arrow(), domain_core, arrow(), adapters_out]

    # 6. B03 : Effacement de type aux frontières
    if h.startswith("db50b2e2"):
        nodes = [
            node("Client Web / Tiers non maîtrisé", ["Envoie un payload brut non vérifié : { \"taille\": \"500Mo\" }"]),
            node("Contrôleur applicatif (interface Document)", [
                "TypeScript compile sans erreur : interface Document { taille_octets: number; }",
                "Illusion de sécurité : le compilateur croit au type mais le runtime contient une String.",
            ]),
            node("Domaine Métier (Calcul arithmétique)", [
                "Crash à l'exécution : NaN ou TypeError.",
                "Garantie violée : la donnée corrompue a traversé la frontière.",
            ]),
        ]
        return sequence(nodes)

    # 7. B03 : Cycle Schema-First
    if h.startswith("b9d18a31"):
        schema = node("SCHÉMA RUNTIME UNIQUE", ["(JSON Schema, OpenAPI, TypeBox, Pydantic)"])
        branches = grid([
            dict(kind="branch", parts=[
                node("Génération statique"),
                arrow(),
                node("Types TypeScript / Python", ["Compilation, Intellisense & vérification AST"]),
            ]),
            dict(kind="branch", parts=[
                node("Exécution dynamique"),
                arrow(),
                node("Validation aux frontières", ["Parse, Don't Validate & RFC 9457"]),
            ]),
        ])
        domain = node("Code Métier Inviolable", ["Invariants mathématiquement garantis sans code défensif parasite."])
        return [schema, arrow(), branches, arrow(), domain]

    # 8. B04 : Comparaison d'inspection de code
    if h.startswith("6dcfce42"):
        nodes = [
            node("LECTURE NAÏVE (Textuelle brute)", [
                "650 lignes de code injectées",
                "Détails d'implémentation parasites",
                "Variables temporaires et bruit syntaxique",
                "Gaspillage massif de la fenêtre de contexte",
            ]),
            node("EXTRACTION PAR AST (Chirurgicale)", [
                "18 lignes d'index structurel",
                "Signatures de fonctions et types exportés",
                "Zéro corps de méthode superflu",
                "Économie de 97 % de tokens de contexte",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 9. B04 : Dégradation cognitive hors smart zone
    if h.startswith("01f67575"):
        nodes = [
            node("SMART ZONE (0 - 120k tokens)", [
                "Raisonnement logique optimal",
                "Rigueur de typage et respect des invariants",
                "Précision maximale : 80 % à 100 %",
            ]),
            node("DÉGRADATION HORS ZONE (> 120k tokens)", [
                "Zone d'hallucinations statistiques",
                "Oubli des consignes initiales et régressions silencieuses",
                "Chute brutale de la précision vers 0 %",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 10. B05 : Le graphe d'objets Git (DAG)
    if h.startswith("6680e9fd"):
        c = node("Commit: feat(upload)", ["Pointe vers Parent Commit"])
        root = node("Root Tree (Arborescence racine)")
        blobs = grid([
            node("Tree: /app", ["Blob: parseur.py (SHA: e89f02...)"]),
            node("Blob: CONTEXT.md", ["Documentation contractuelle (SHA: 4a2b1c...)"]),
        ])
        return [c, arrow(), root, arrow(), blobs]

    # 11. B05 : Topologie Git Worktrees
    if h.startswith("b10e92b4"):
        repo = node("DÉPÔT CENTRAL (.git)", ["Base d'objets immuable, Refs, Index partagé"])
        trees = grid([
            node("WORKTREE MAIN", ["~/src/projet-main", "(Branche main, Staging stable)"]),
            node("WORKTREE AGENT-01", ["~/src/worktrees/feat-upload", "(Branche feat/upload, tâche 1)"]),
            node("WORKTREE AGENT-02", ["~/src/worktrees/fix-auth", "(Branche fix/auth, tâche 2)"]),
        ])
        return [repo, arrow(), trees]

    # 12. B05 : Stacked Pull Requests
    if h.startswith("cdef4815"):
        top = node("main (Production stable)")
        prs = [
            node("PR 1 : feat(schema)", ["Contrats et objets-valeurs purs (60 lignes)"]),
            node("PR 2 : feat(parseur)", ["Parseur aux frontières et erreurs RFC 9457 (85 lignes)"]),
            node("PR 3 : feat(metier)", ["Machine à états et règles d'invariants (110 lignes)"]),
            node("PR 4 : feat(api)", ["Route HTTP et adaptateur Fastify (75 lignes)"]),
        ]
        return [top, arrow()] + sequence(prs)

    # 13. B05 : Contrat oracle bisect
    if h.startswith("5e1dab2a"):
        nodes = [
            node("Code retour = 0", ["Le commit est SAIN (Good / Old)."]),
            node("Code retour = 1", ["Le commit est DÉFAILLANT (Bad / New). La régression est présente."]),
            node("Code retour = 125", ["Le commit est INÉVALUABLE (Skip). Dépendance cassée, code non compilable."]),
        ]
        return [grid(nodes)]

    # 14. B06 : Pyramide de vérification déterministe
    if h.startswith("aa7a2b8a"):
        levels = [
            node("NIVEAU 3 : TESTS E2E SYSTÈME (Playwright / Cypress)",
                 ["Volume : < 5 % | Durée : 1 à 3 min | Coût : Élevé", "Parcours complets des flux nominaux critiques."],
                 badge="E2E"),
            node("NIVEAU 2 : TESTS DE CONTRAT & INTÉGRATION (Seams)",
                 ["Volume : ~20 % | Durée : 2 à 10 s | Coût : Moyen", "Validation de la coopération entre Domaine et Infrastructure."],
                 badge="INTÉG."),
            node("NIVEAU 1 : TESTS UNITAIRES BOÎTE NOIRE (Mypy / Pytest)",
                 ["Volume : > 75 % | Durée : < 500 ms | Coût : Négligeable", "Vérification exhaustive des règles d'invariants métier."],
                 badge="UNITAIRES"),
            node("NIVEAU 0 : ANALYSE STATIQUE, TYPES STRICTS & LINTER",
                 ["Volume : 100 % du code | Durée : Instantanée", "Preuve syntaxique, AST, absence d'effets de bord occultes."],
                 badge="ANALYSE STATIQUE"),
        ]
        return [dict(kind="pyramid", items=levels)]

    # 15. B07 : Full Jitter vs Sans Jitter
    if h.startswith("41f3366e"):
        nodes = [
            node("Sans Jitter (Pulsations synchrones destructrices)", [
                "Pics brutaux à 1000 req/s synchronisés à t=5s, t=10s, t=15s",
                "Thundering Herd : le service s'effondre à chaque réessai collectif",
            ]),
            node("Avec Full Jitter (Dispersion uniforme de Poisson)", [
                "Charge lissée à ~200 req/s sur l'intervalle",
                "Le service absorbe la charge et retrouve son équilibre sans saturer",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 16. B07 : Verrou d'idempotence
    if h.startswith("81f9b485"):
        req = node("Requête entrante avec clé d'idempotence", ["Clé UUIDv4 transmise par le client"])
        test = node("Vérification dans le registre (Redis / DB)", ["La clé existe-t-elle déjà ?"])
        branches = grid([
            dict(kind="branch", parts=[
                node("Clé absente (Nouveau traitement)"),
                arrow(),
                node("Acquisition du verrou (LOCK)", [
                    "1. INSERT INTO locks (key, status='IN_PROGRESS', ttl=60s)",
                    "2. Exécution du traitement de paiement",
                    "3. Stockage de la réponse scellée (status='SUCCESS')",
                    "4. Libération du verrou",
                ]),
            ]),
            dict(kind="branch", parts=[
                node("Clé présente (Doublon détecté)"),
                arrow(),
                node("Vérification du statut", [
                    "• Si statut 'IN_PROGRESS' : 409 Conflict ou 425 Too Early",
                    "• Si statut 'SUCCESS' : Renvoi immédiat de la réponse en cache sans réexécuter",
                ]),
            ]),
        ])
        return [req, arrow(), test, arrow(), branches]

    # 17. B08 : Stratégies de verrouillage
    if h.startswith("b76c1a23"):
        nodes = [
            node("VERROUILLAGE OPTIMISTE (OCC)", [
                "Contrôle par numéro de version (colonne version_id)",
                "Zéro lock pendant la phase de lecture",
                "Rejet avec 409 Conflict si la version a changé au moment du commit",
                "Idéal pour fort trafic en lecture et faible taux de collision",
            ]),
            node("VERROUILLAGE PESSIMISTE (Pessimistic Locking)", [
                "SELECT ... FOR UPDATE",
                "Verrou exclusif posé sur la ligne en base de données",
                "Les autres transactions attendent la fin de la transaction",
                "Indispensable pour décrémenter un quota ou un solde critique",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 18. B08 : RPO vs RTO
    if h.startswith("ceb3e065"):
        nodes = [
            node("RPO (Recovery Point Objective)", [
                "« Combien de données puis-je me permettre de perdre ? »",
                "Sauvegarde continue WAL : perte maximale = 0 à 1 seconde.",
            ]),
            node("RTO (Recovery Time Objective)", [
                "« Combien de temps puis-je rester en panne ? »",
                "Restauration automatique PITR : retour en ligne en < 15 minutes.",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 19. B09 : Reverse proxy et sondes de santé
    if h.startswith("d5effaed"):
        proxy = node("REVERSE PROXY (Caddy / Envoy)", ["Terminaison TLS, Let's Encrypt, Rate Limiting, Port 443"])
        instances = grid([
            node("INSTANCE ACTIVE (Conteneur A)", ["Sonde /healthz : HTTP 200 (OK)", "Trafic de production acheminé"]),
            node("INSTANCE CANDIDATE (Conteneur B)", ["Sonde /readyz : Attente réchauffement cache", "Zéro trafic tant que le statut n'est pas prêt"]),
        ])
        return [proxy, arrow(), instances]

    # 20. B10 : Transitions circuit breaker
    if h.startswith("ab021123"):
        states = [
            node("FERMÉ", ["(Nominal) : Requêtes transmises au service distant, mesure du taux d'échec"], key="closed"),
            node("OUVERT", ["(Protection) : Appels coupés net (Fail-fast), temporisation cooldown"], key="open"),
            node("SEMI-OUVERT", ["(Sondage) : Sonde d'essai, 1 requête de test autorisée"], key="half"),
        ]
        return [dict(kind="states", items=states, transitions=[
            dict(source="closed", target="open", label="Taux d'échec > Seuil critique"),
            dict(source="open", target="half", label="Délai de cooldown expiré"),
            dict(source="half", target="closed", label="Succès de la sonde d'essai"),
            dict(source="half", target="open", label="Échec de la sonde d'essai"),
        ])]

    # 21. B11 : Découpage horizontal vs tranche verticale
    if h.startswith("5ab61b05"):
        nodes = [
            node("DÉCOUPAGE HORIZONTAL (DANGEREUX)", [
                "Couche 1 : Tous les DTOs",
                "Couche 2 : Tous les contrôleurs",
                "Couche 3 : Tous les repositories",
                "Intégration tardive, effet tunnel, risque d'incohérence élevé",
            ]),
            node("TRANCHE VERTICALE (ROBUSTE)", [
                "Tranche 1 : Upload de document complet (UI + Métier + DB)",
                "Tranche 2 : Consultation de document",
                "Chaque tranche traverse toutes les couches",
                "Prouvée par tests end-to-end dès le premier jour",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 22. A03 : Conception horizontale vs tranche verticale
    if h.startswith("ee71b225"):
        nodes = [
            node("CONCEPTION HORIZONTALE (À PROSCRIRE)", [
                "Tous les écrans du site (Mois 1)",
                "Tous les formulaires (Mois 2)",
                "Toutes les tables SQL (Mois 3)",
                "Effet tunnel : rien n'est testable ni démontrable avant la fin",
            ]),
            node("TRANCHE VERTICALE (MÉTHODE DU PILOTE)", [
                "Un seul écran + sa validation + sa table",
                "Livré et prouvé en 2 jours",
                "Valeur immédiate et testable de bout en bout",
            ]),
        ]
        return [grid(nodes, style="comparison")]

    # 23. B11 : Upload direct multipart
    if h.startswith("7a4f125f"):
        steps = [
            node("1. Déclaration initiale", [
                "Client ──► Serveur API : POST /uploads/sessions (taille: 450 Mo, checksum)",
                "Serveur API vérifie droits et quota",
            ]),
            node("2. Réservation & URLs signées", [
                "Serveur API ──► S3/R2 : InitiateMultipartUpload",
                "Retour au client des URLs pré-signées par chunk",
            ]),
            node("3. Transfert direct parallèle", [
                "Client ──► S3/R2 : PUT direct des chunks 1..45",
                "La mémoire vive du serveur API n'est jamais sollicitée",
            ]),
            node("4. Finalisation & Scellement", [
                "Client ──► Serveur API : POST /uploads/complete",
                "Calcul et vérification de l'empreinte SHA-256 finale",
            ]),
        ]
        return sequence(steps)

    # 24. B11 : Interleaving temporel doublon
    if h.startswith("7ae1f55e"):
        cols = [
            node("Thread A (Requête 1)", [
                "SELECT id FROM commandes WHERE panier_id = 42; (NULL)",
                "INSERT INTO commandes; (Commit réussi : Commande #1042 créée)",
            ]),
            node("Thread B (Requête 2)", [
                "SELECT id FROM commandes WHERE panier_id = 42; (NULL)",
                "INSERT INTO commandes; (Commit réussi : Commande #1043 créée !)",
            ]),
        ]
        return [grid(cols, style="comparison")]

    # 25. B11 : Matrice alignement protocoles
    if h.startswith("128c022b"):
        steps = [
            node("1. SPÉCIFICATION (O & R)", ["ORCHESTRE : Observer & Résultat", "Outils : /grill-with-docs, /to-prd", "Contrôle : Audit de l'existant, User Stories et critères"]),
            node("2. CONTRATS (C & H)", ["ORCHESTRE : Cartographier & Hypothèse", "Outils : /to-issues, ADR formel (docs/adr)", "Contrôle : Tranches verticales, architecture minimale"]),
            node("POINT D'ARRÊT DÉCISIONNEL", ["Gel mémoire (/clear), purge du contexte et handoff humain"]),
            node("3. TESTS & 4. IMPLÉMENTATION (E, S, T)", ["ORCHESTRE : Expérimenter, Sécuriser, Tracer", "Outils : /tdd (Preuve rouge), /implement (Code vert), Commits atomiques", "Contrôle : Test frontière, code minimal sans parasite"]),
            node("5. INTÉGRATION & 6. LIVRAISON (R & E)", ["ORCHESTRE : Relire & Exposer", "Outils : /review (Double audit), Staging / Blue-Green", "Contrôle : Standards & Spécification, surveillance SLO"]),
        ]
        return sequence(steps)

    # 26. B12 : Architecture de routage agnostique
    if h.startswith("d42f946b"):
        top = node("HARNAIS AGENTIQUE SOUVERAIN", ["Aider / Claude Code / Roo Code / OpenHands"])
        router = node("COUCHE DE ROUTAGE UNIFIÉE", ["LiteLLM Proxy / Ollama / Local Gateway"])
        backends = grid([
            node("Moteurs Propriétaires", ["Claude (Anthropic API)", "OpenAI (o-series / GPT-4o)", "Gemini (Google AI)"]),
            node("Inférence Dédiée / VPS", ["vLLM / SGLang (GPU Nvidia)", "Modèles Open Weights hébergés"]),
            node("Inférence Locale", ["Ollama / llama.cpp (Apple Silicon / CPU)", "Qwen2.5, DeepSeek, Codestral"]),
        ])
        return [top, arrow("(Standard OpenAI / OpenTelemetry)"), router, arrow(), backends]

    # 27. Annexes : Ruban principal
    if h.startswith("a6f3f955"):
        main_flow = [
            node("Cadrage & Spécification", ["Idée brute ──► /grill-with-docs ──► /to-prd ──► /to-issues", "En cas de doute UI : /prototype"]),
            node("Purge de Contexte", ["Commande /clear : réinitialisation de la fenêtre"]),
            node("Développement sous Preuve", ["/implement + /tdd (cycle TDD inversé)"]),
            node("Contrôle Qualité", ["/review (Double audit : Standards + Spécification)"]),
        ]
        on_ramps = node("Voies d'Insertion (On-Ramps)", [
            "Bugs & retours externes ──► /triage ──► Ticket prêt",
            "Bug dur ou régression ──► /diagnosing-bugs ──► Fix + Test rouge",
            "Brouillard complet ──► /wayfinder ──► Décisions ──► /to-prd"
        ])
        return sequence(main_flow) + [arrow(), on_ramps]

    # 28. Annexes : Décision session
    if h.startswith("89fc56cf"):
        items = [
            node("Idée nouvelle ou fonctionnalité", ["/grill-with-docs (avec dépôt Git) ou /grill-me (sans dépôt)"]),
            node("Incertitude sur le point de départ", ["/ask-matt (l'aiguilleur universel de session)"]),
            node("Jargon ou confusion de l'agent", ["/wait-what (arrêt d'urgence et recadrage)"]),
            node("Action humaine requise (secrets, OAuth)", ["/wizard (script interactif) ou /to-questionnaire"]),
            node("Chantier immense (brouillard)", ["/wayfinder (carte de tickets de décision)"]),
            node("Panne, régression ou lenteur", ["/diagnosing-bugs (boucle rouge déterministe)"]),
            node("Dette technique ou code rigide", ["/improve-codebase-architecture (modules profonds)"]),
            node("Signalements externes ou conflits Git", ["/triage ou /resolving-merge-conflicts"]),
        ]
        return [grid(items, style="pillars")]

    # 29. Annexes : Jalon 1
    if h.startswith("424ff6aa"):
        steps = [
            node("1. Aiguillage initial", ["/ask-matt (Constat : besoin de cadre formel)"]),
            node("2. Modélisation de domaine", ["CONTEXT.md (Glossaire strict & _Avoid_)"]),
            node("3. Arbitrage engageant", ["docs/adr/0001-harnais-en-trois-couches.md"]),
            node("4. Outillage opérationnel", [".agents/skills/ (37 skills déployés)"]),
            node("5. Preuves observables", ["26 tests unitaires OK + Build Hugo"]),
            node("6. Publication & Traçabilité", ["Git commit, push, Cloudflare Pages HTTP 200"]),
        ]
        return sequence(steps)

    return None


def parse_diagram(body, file_path):
    lines = [l.rstrip() for l in body.strip().splitlines() if l.strip()]
    if not lines:
        return None

    h = hashlib.sha256(body.encode()).hexdigest()
    title = ""
    start_idx = 0
    first = lines[0].strip()
    if not any(c in first for c in "┌┬└┼─│═╔╚") and not first.startswith("["):
        title = first.rstrip(" :")
        start_idx = 1
    elif first.startswith("┌") and len(lines) > 2 and any(kw in lines[1] for kw in ["RUBAN", "JALON"]):
        title = clean(lines[1])
        start_idx = 2

    # Check custom handlers first
    custom_parts = parse_custom(h, lines, title)
    if custom_parts:
        diag_id = slug(title or Path(file_path).stem + "-" + h[:8])
        return dict(id=diag_id, title=title or "SCHÉMA DU SYSTÈME", source_sha256=h, parts=custom_parts)

    content_lines = lines[start_idx:]

    # Box parsing
    b = parse_boxes(content_lines)
    if b:
        if not title:
            title = b[0]["title"]
        diag_id = slug(title or Path(file_path).stem + "-" + h[:8])
        return dict(id=diag_id, title=title, source_sha256=h, parts=sequence(b))

    # Phases parsing
    p = parse_phases(content_lines)
    if p:
        diag_id = slug(title or Path(file_path).stem + "-" + h[:8])
        return dict(id=diag_id, title=title or "SÉQUENCE DU PROTOCOLE", source_sha256=h, parts=p)

    # Bracket flow parsing
    bf = parse_bracket_flow(content_lines)
    if bf:
        diag_id = slug(title or Path(file_path).stem + "-" + h[:8])
        return dict(id=diag_id, title=title or "TOPOLOGIE DU SYSTÈME", source_sha256=h, parts=bf)

    return None


def build_manuscrit_registry(root=ROOT):
    seen = set()
    registry = {}
    for folder in ["manuscrit/01-lecture-accessible", "manuscrit/02-lecture-ingenieure", "manuscrit/03-annexes"]:
        for r, dirs, files in os.walk(root / folder):
            for f in sorted(files):
                if f.endswith(".md"):
                    p = Path(r) / f
                    text = p.read_text(encoding="utf-8")
                    for m in re.finditer(r"```text\n(.*?)```", text, re.DOTALL):
                        body = m.group(1)
                        if any(c in body for c in "┌┬└┼─│"):
                            h = hashlib.sha256(body.encode()).hexdigest()
                            if h not in seen:
                                seen.add(h)
                                rel = str(p.relative_to(root))
                                diag = parse_diagram(body, rel)
                                if diag:
                                    registry[h] = diag
                                else:
                                    print(f"ATTENTION : diagramme non transposé dans {rel} ({h[:8]})")
    return registry


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Vérifie sans écrire.")
    args = parser.parse_args()
    registry = build_manuscrit_registry()
    out_path = ROOT / "data/diagrams/manuscrit.json"
    if args.check:
        if not out_path.exists():
            raise ValueError(f"Fichier manquant : {out_path}")
        saved = json.loads(out_path.read_text(encoding="utf-8"))
        if registry != saved:
            raise ValueError("Schémas du manuscrit non synchronisés.")
        print(f"OK : {len(registry)} schémas du manuscrit vérifiés.")
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"OK : {len(registry)} schémas du manuscrit transposés avec succès dans {out_path.name}.")


if __name__ == "__main__":
    main()
