{
  "title": "Catalogue des 37 skills",
  "source_path": "manuscrit/03-annexes/04-catalogue-des-skills.md",
  "weight": 4,
  "description": "Inventaire complet des compétences en fiches dépliables avec permaliens directs."
}

Ce catalogue constitue l'inventaire de référence des 37 compétences d'ingénierie de Matt Pocock. Pour supprimer la charge cognitive et faciliter la navigation, les compétences sont organisées en **six familles thématiques**, présentées sous forme de **fiches compactes dépliables**.

Chaque fiche dispose d'une ancre d'URL directe (ex: `#grill-with-docs`) : vous pouvez copier le permalien pour le partager par email, sur Slack ou dans vos supports de cours.

---
## 1. Gouvernance du Dépôt & Cadrage Amont
<p class="family-lead">Pose le cadre méthodologique, aligne le modèle métier vivant et interroge les zones d'ombre avant d'écrire la moindre ligne de code.</p>
<div class="skills-accordion-group">
<details id="setup-matt-pocock-skills" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/setup-matt-pocock-skills</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Configuration initiale du dépôt pour l'ensemble des compétences.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="setup-matt-pocock-skills">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Configure le dépôt pour l'ensemble des compétences d'ingénierie. À exécuter une seule fois lors de la prise en main d'un projet.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : À l'initialisation d'un nouveau dépôt ou avant d'utiliser les compétences d'ingénierie sur une base existante.</li>
        <li><strong>Entrées / Sorties</strong> : Explore le gestionnaire de tickets (GitHub, GitLab, ou Markdown local sous `.scratch/`), configure les étiquettes de triage canoniques (`needs-triage`, `ready-for-agent`, etc.) et pose l'arborescence documentaire (`CONTEXT.md`, `docs/adr/`, `docs/agents/`).</li>
        <li><strong>Règle d'or</strong> : Les compétences aval dépendent de cette convention pour savoir où lire et publier leurs artefacts. Ne la sautez jamais.</li>
    </ul>
  </div>
</details>
<details id="grill-with-docs" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/grill-with-docs</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Interview contradictoire amont et tenue continue de CONTEXT.md et des ADRs.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="grill-with-docs">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Le point d'entrée par excellence pour toute nouvelle fonctionnalité dans une base de code existante. Combine une interview contradictoire sans complaisance avec la tenue continue du modèle de domaine.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/grill-with-docs [votre intention]`).</li>
        <li><strong>Quand l'invoquer</strong> : Dès qu'une idée émerge et que vous disposez d'un dépôt Git.</li>
        <li><strong>Entrées / Sorties</strong> : Lit le code existant et `CONTEXT.md`. Met à jour `CONTEXT.md` au fil des clarifications. Rédige un ADR dans `docs/adr/` lorsqu'une décision lourde et difficilement réversible est actée.</li>
        <li><strong>Règle d'or</strong> : L'agent pose ses questions **une par une**, avec sa réponse recommandée, après avoir fouillé le code. Aucun code de production n'est écrit durant cette phase.</li>
    </ul>
  </div>
</details>
<details id="grill-me" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/grill-me</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Interview de cadrage stateless pour challenger une idée sans base de code.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="grill-me">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Interview de cadrage sans état (*stateless*).</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/grill-me`).</li>
        <li><strong>Quand l'invoquer</strong> : Lorsque vous voulez challenger un concept, une idée de startup ou un plan abstrait **sans base de code**.</li>
        <li><strong>Entrées / Sorties</strong> : Aucun fichier local n'est modifié ; l'exploration se déroule intégralement dans le fil de conversation.</li>
        <li><strong>Règle d'or</strong> : Si un dépôt existe, utilisez toujours `grill-with-docs`. Réservez `grill-me` aux réflexions préliminaires hors dépôt.</li>
    </ul>
  </div>
</details>
<details id="grilling" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/grilling</code>
      <span class="badge-mode">model-invoked</span>
    </div>
    <span class="skill-short-title">Moteur unitaire d'interview contradictoire animant les compétences de cadrage.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="grilling">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Le moteur unitaire d'interview contradictoire qui anime les compétences de cadrage.</li>
        <li><strong>Invocation</strong> : `model-invoked` (appelé par `grill-with-docs`, `decision-mapping`, `triage`).</li>
        <li><strong>Quand l'invoquer</strong> : Invoqué par d'autres compétences pour traquer les ambiguïtés et lever les non-dits.</li>
        <li><strong>Règle d'or</strong> : Interdiction de soumettre une liste de cinq questions simultanées (effet de sidération). Une seule question à la fois, avec réponse recommandée, en attendant la réponse avant d'enchaîner.</li>
    </ul>
  </div>
</details>
<details id="domain-modeling" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/domain-modeling</code>
      <span class="badge-mode">model-invoked</span>
    </div>
    <span class="skill-short-title">Discipline active de Domain-Driven Design (DDD) entretenant CONTEXT.md et les ADRs.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="domain-modeling">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Discipline active de Domain-Driven Design (DDD). Aligne le vocabulaire du code sur les concepts métier réels.</li>
        <li><strong>Invocation</strong> : `model-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : Dès qu'un terme imprécis ou surchargé apparaît, ou qu'une décision architecturale est arrêtée.</li>
        <li><strong>Entrées / Sorties</strong> : Entretient `CONTEXT.md` (glossaire strict sans code ni spec) et `docs/adr/`.</li>
        <li><strong>Règle d'or</strong> : Un ADR n'est rédigé que s'il réunit trois critères stricts : difficile à inverser, surprenant sans contexte, et issu d'un compromis réel.</li>
    </ul>
  </div>
</details>
<details id="decision-mapping" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/decision-mapping</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Cartographie du brouillard de guerre pour les chantiers massifs (alias /wayfinder).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="decision-mapping">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/decision-mapping" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Exploration méthodique du « brouillard de guerre » pour les chantiers complexes dépassant le cadre d'une seule session de cadrage.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : Face à une initiative vaste, incertaine ou comportant de multiples inconnues architecturales.</li>
        <li><strong>Entrées / Sorties</strong> : Crée et maintient `DECISION_MAP.md` découpé en tickets d'investigation typés (`Research`, `Prototype`, `Grilling`).</li>
        <li><strong>Règle d'or</strong> : Une session = un seul ticket résolu. Chaque session se clôture obligatoirement par `/handoff` pour repartir sur une session neuve.</li>
    </ul>
  </div>
</details>
<details id="loop-me" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/loop-me</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Cadrage et spécification de boucles d'automatisation récurrentes.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="loop-me">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/loop-me" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Cadrage et spécification de boucles d'automatisation récurrentes.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : Pour automatiser une tâche périodique ou récurrente dans votre quotidien de développeur.</li>
        <li><strong>Entrées / Sorties</strong> : Produit une spécification dans `workflows/*.md` avec déclencheur (*trigger*), brief et points de contrôle (*checkpoints*).</li>
        <li><strong>Règle d'or</strong> : Principe du « Push right » : différer l'intervention humaine le plus loin possible pour ne lui soumettre qu'une décision finale synthétique.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## 2. Étude & Spécification
<p class="family-lead">Convertit les arbitrages issus du cadrage en artefacts techniques formels sans relancer de questions.</p>
<div class="skills-accordion-group">
<details id="prototype" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/prototype</code>
      <span class="badge-mode">model / user</span>
    </div>
    <span class="skill-short-title">Fabrication de code jetable destiné exclusivement à répondre à un doute UI ou d'état.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="prototype">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Fabrication de code jetable destiné exclusivement à répondre à une question de conception précise.</li>
        <li><strong>Invocation</strong> : `model-invoked` ou `user-invoked` (`/prototype`).</li>
        <li><strong>Quand l'invoquer</strong> : Doute sur l'ergonomie d'une interface (branche *UI*) ou incertitude sur la viabilité d'une machine d'états (branche *Logic*).</li>
        <li><strong>Entrées / Sorties</strong> : Produit un mini-programme jetable lancé en une seule commande, sans persistance réelle ni suite de tests.</li>
        <li><strong>Règle d'or</strong> : Seule la réponse apprise est conservée (dans un ADR ou une note). Le code du prototype est immédiatement détruit ou absorbé, jamais conservé tel quel.</li>
    </ul>
  </div>
</details>
<details id="to-prd" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/to-prd</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Synthèse formelle sans ré-interview des acquis en Document de Spécification (PRD).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="to-prd">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Synthétise le fil de discussion issu du grilling en document formel de spécification (PRD).</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/to-prd`).</li>
        <li><strong>Quand l'invoquer</strong> : Dès que l'interview `/grill-with-docs` a épuisé toutes les zones d'ombre.</li>
        <li><strong>Entrées / Sorties</strong> : Rédige et publie le PRD : problème, solution, User Stories numérotées, décisions d'implémentation, frontières de tests et hors périmètre (*out of scope*).</li>
        <li><strong>Règle d'or</strong> : **Pas de ré-interview**. L'agent synthétise les acquis sans relancer de questions.</li>
    </ul>
  </div>
</details>
<details id="to-issues" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/to-issues</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Découpage du PRD en tranches verticales indépendantes avec graphe de blocage.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="to-issues">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Découpe un PRD ou une spécification en tickets unitaires indépendants.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/to-issues`).</li>
        <li><strong>Quand l'invoquer</strong> : Immédiatement après `/to-prd`.</li>
        <li><strong>Entrées / Sorties</strong> : Publie les tickets sur l'issue tracker configuré (GitHub, GitLab, ou Markdown local).</li>
        <li><strong>Règle d'or</strong> : Chaque ticket est une **tranche verticale** (*tracer bullet* : traverse schéma, logique, API, UI et test de bout en bout), jamais une tranche horizontale par couche. Ordonnancement strict par dépendances bloquantes.</li>
    </ul>
  </div>
</details>
<details id="to-questionnaire" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/to-questionnaire</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Génération d'un questionnaire ciblé quand le bloqueur est chez un tiers ou client.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="to-questionnaire">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/to-questionnaire" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Lève les blocages d'exigences lorsque l'information n'est ni dans le code ni dans la tête du développeur, mais chez un tiers extérieur (client, expert métier, collègue).</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/to-questionnaire`).</li>
        <li><strong>Quand l'invoquer</strong> : Dès qu'une question du grilling fait apparaître une zone d'ombre commerciale, juridique ou organisationnelle insoluble en interne.</li>
        <li><strong>Entrées / Sorties</strong> : L'agent vous interroge brièvement sur le destinataire et le besoin d'arbitrage, puis génère un questionnaire Markdown prêt à être transmis.</li>
        <li><strong>Règle d'or</strong> : Ne supposez jamais la réponse d'un tiers dans le code. Envoyez le questionnaire et attendez le retour pour réinjecter les faits dans `/grill-with-docs`.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## 3. Fabrication & Preuves d'Ingénierie
<p class="family-lead">Gouverne la production du code sous la contrainte stricte de tests observables et d'une architecture modulaire profonde.</p>
<div class="skills-accordion-group">
<details id="implement" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/implement</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Réalisation bornée et étanche d'un ticket spécifique dans un worktree dédié.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="implement">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/implement" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Réalisation bornée et étanche d'un ticket spécifique.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/implement`).</li>
        <li><strong>Quand l'invoquer</strong> : À l'ouverture d'une session neuve dédiée à un ticket unitaire issu de `/to-issues`.</li>
        <li><strong>Entrées / Sorties</strong> : Travaille dans un arbre de travail Git dédié (*worktree*). Lit le ticket et le PRD.</li>
        <li><strong>Règle d'or</strong> : Chaque ligne modifiée doit tracer directement à la spécification. Ne pousse jamais sur le dépôt distant et n'ouvre pas de PR sans autorisation explicite.</li>
    </ul>
  </div>
</details>
<details id="tdd" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/tdd</code>
      <span class="badge-mode">model-invoked</span>
    </div>
    <span class="skill-short-title">Développement piloté par les tests à la frontière publique (Rouge → Vert → Refactor).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="tdd">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Développement piloté par les tests, un comportement vertical à la fois.</li>
        <li><strong>Invocation</strong> : `model-invoked` (appelé par `implement`) ou `user-invoked` (`/tdd`).</li>
        <li><strong>Quand l'invoquer</strong> : Pour chaque comportement métier observable à implémenter.</li>
        <li><strong>Entrées / Sorties</strong> : Cycle Rouge (test échouant pour la bonne raison à la frontière publique) $	o$ Vert (code minimal pour passer) $	o$ Refactor (nettoyage sous protection du test).</li>
        <li><strong>Règle d'or</strong> : L'assertion doit porter sur l'interface publique stable, jamais sur les détails privés d'implémentation ou des mocks artificiels.</li>
    </ul>
  </div>
</details>
<details id="codebase-design" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/codebase-design</code>
      <span class="badge-mode">model-invoked</span>
    </div>
    <span class="skill-short-title">Vocabulaire et principes de conception de modules profonds aux interfaces étroites.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="codebase-design">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Référentiel de conception des **modules profonds** (*deep modules*).</li>
        <li><strong>Invocation</strong> : `model-invoked`.</li>
        <li><strong>Notions clés</strong> : Module, Interface, Profondeur (*depth*), Couture (*seam*), Adaptateur, Levier (*leverage*), Localité.</li>
        <li><strong>Règle d'or</strong> : Appliquer le **test de suppression** : si supprimer le module fait disparaître la complexité, c'était un passe-plat superficiel. Si la complexité réapparaît chez $N$ appelants, le module est légitime.</li>
    </ul>
  </div>
</details>
<details id="migrate-to-shoehorn" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/migrate-to-shoehorn</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Sécurisation des suites de tests en remplaçant les assertions arbitraires par shoehorn.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="migrate-to-shoehorn">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Assainissement des suites de tests TypeScript.</li>
        <li><strong>Invocation</strong> : `user-invoked` ou `model-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : Détection d'assertions de type risquées (`as MyType`) dans les fixtures de test.</li>
        <li><strong>Règle d'or</strong> : Remplace les castings aveugles par des données partielles sûres via `@total-typescript/shoehorn`.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## 4. Contrôle, Diagnostic & Santé du Code
<p class="family-lead">Garantit la barrière de péage avant merge, résout les incidents complexes et audite la dette architecturale.</p>
<div class="skills-accordion-group">
<details id="review" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/review</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Audit contradictoire automatisé sur 2 axes : Axe Standards et Axe Spécification.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="review">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/review" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : La barrière de péage avant toute intégration ou ouverture de PR.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/review`).</li>
        <li><strong>Quand l'invoquer</strong> : À la fin de l'implémentation d'un ticket, avant de committer ou de fusionner.</li>
        <li><strong>Entrées / Sorties</strong> : Lance deux sous-agents indépendants en parallèle :</li>
        <li>*Axe Standards* : conformité aux règles `AGENTS.md` du dépôt, style et modularité.</li>
        <li>*Axe Spec* : stricte réponse au besoin sans aucun ajout superflu.</li>
        <li><strong>Règle d'or</strong> : Les sous-agents sont strictement en lecture seule. Ils ne corrigent pas le code, ils fournissent un rapport précis avec références de lignes.</li>
    </ul>
  </div>
</details>
<details id="diagnosing-bugs" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/diagnosing-bugs</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Diagnostic déterministe avec boucle rouge obligatoire, sondes et test de non-régression.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="diagnosing-bugs">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Protocole d'investigation scientifique en 6 phases pour les bogues ardus et régressions de performance.</li>
        <li><strong>Invocation</strong> : `model-invoked` ou `user-invoked` (`/diagnosing-bugs`).</li>
        <li><strong>Quand l'invoquer</strong> : « Ça plante », « Comportement anormal », « Régression de vitesse ».</li>
        <li><strong>Les 6 phases</strong> : </li>
        <p>1. *Boucle de rétroaction rouge déterministe* (test, curl, trace rejouée).</p>
        <p>2. *Minimisation* du scénario à la charge utile minimale.</p>
        <p>3. *3 à 5 hypothèses falsifiables* classées avant toute retouche.</p>
        <p>4. *Sondes ciblées* taguées `[DEBUG-xxxx]`.</p>
        <p>5. *Test de non-régression* à la bonne couture, puis correction.</p>
        <p>6. *Nettoyage* des sondes et bilan d'architecture.</p>
        <li><strong>Règle d'or absolue</strong> : **Interdiction de lire le code pour formuler des hypothèses tant qu'une commande ne reproduit pas le bogue en rouge de façon nette.**</li>
    </ul>
  </div>
</details>
<details id="improve-codebase-architecture" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/improve-codebase-architecture</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Audit automatique des modules superficiels et génération d'un rapport HTML visuel.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="improve-codebase-architecture">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Audit proactif de la dette technique et recherche d'opportunités d'épaississement de modules.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/improve-codebase-architecture`).</li>
        <li><strong>Quand l'invoquer</strong> : Lors des temps calmes ou quand l'ajout de fonctionnalités devient fastidieux.</li>
        <li><strong>Entrées / Sorties</strong> : Génère un rapport HTML interactif autonome dans `/tmp/` (Mermaid + Tailwind) illustrant les refactorings recommandés avant/après, puis lance un grilling sur le candidat choisi.</li>
        <li><strong>Règle d'or</strong> : Regroupe la logique éparpillée pour maximiser la localité et rendre le code naturellement navigable pour les agents.</li>
    </ul>
  </div>
</details>
<details id="resolving-merge-conflicts" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/resolving-merge-conflicts</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Résolution d'un conflit de fusion Git par l'analyse d'intention des deux branches.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="resolving-merge-conflicts">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Résolution causale des conflits de fusion et de rebase Git.</li>
        <li><strong>Invocation</strong> : `model-invoked` lors d'un conflit Git en cours.</li>
        <li><strong>Quand l'invoquer</strong> : Dès qu'un rebase ou un merge s'arrête sur un conflit.</li>
        <li><strong>Règle d'or</strong> : Remonter aux sources primaires (commits, PRs d'origine) pour comprendre l'intention des deux branches. Ne jamais résoudre en aveugle ; valider par la suite de tests complète avant de clore.</li>
    </ul>
  </div>
</details>
<details id="triage" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/triage</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Qualification et triage des tickets et PRs externes entrants (jamais de to-issues).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="triage">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/engineering/triage" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Qualification des signalements et PRs externes via une machine à états stricte.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/triage`).</li>
        <li><strong>Quand l'invoquer</strong> : Pour traiter le flux d'issues et de contributions extérieures.</li>
        <li><strong>Entrées / Sorties</strong> : Vérifie la non-redondance dans `.out-of-scope/`, reproduit l'anomalie ou exécute la PR, et attribue le rôle (`needs-info`, `ready-for-agent`, `wontfix`).</li>
        <li><strong>Règle d'or</strong> : Ne pas trier les issues issues de `/to-issues` (elles sont déjà prêtes pour l'agent). Réserver le triage aux flux non filtrés arrivant de l'extérieur.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## 5. Outillage Opérationnel & Sécurité
<p class="family-lead">Garde-fous d'intégrité, recadrage anti-jargon et guidage des actions humaines sensibles.</p>
<div class="skills-accordion-group">
<details id="wait-what" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/wait-what</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Bouton d'arrêt d'urgence et recadrage sans complaisance en langage simple avec CONTEXT.md.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="wait-what">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/wait-what" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Arrêt d'urgence et recadrage immédiat lorsque l'agent part dans du jargon, dérive ou produit une réponse incompréhensible.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/wait-what`).</li>
        <li><strong>Quand l'invoquer</strong> : En cours de session, à l'intérieur de n'importe quel autre skill, dès que vous perdez le fil de l'explication de l'agent.</li>
        <li><strong>Entrées / Sorties</strong> : L'agent s'arrête instantanément, examine ce qui a causé l'incompréhension, et ré-explique sa position en français simple et direct, en s'appuyant uniquement sur le vocabulaire validé dans `CONTEXT.md`.</li>
        <li><strong>Règle d'or</strong> : Ne débattez jamais avec un agent qui a commencé à halluciner ou à jargonner. Invoquez `/wait-what` pour rétablir une base saine avant de continuer.</li>
    </ul>
  </div>
</details>
<details id="wizard" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/wizard</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Script Bash interactif guidant un opérateur humain dans des étapes sensibles (clés, Cloud).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="wizard">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/wizard" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Générateur de scripts bash interactifs guidant un opérateur humain dans des procédures manuelles fastidieuses.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Quand l'invoquer</strong> : Configurations de services tiers (Stripe, Cloudflare, secrets GitHub), migrations sensibles de données, bascules d'état irréversibles.</li>
        <li><strong>Entrées / Sorties</strong> : Génère un script bash soigné (barre de progression, saisie masquée des clés secrètes, ouverture automatique des URLs, écriture dans `.env`).</li>
        <li><strong>Règle d'or</strong> : Éphémère par défaut, détruit une fois la procédure validée, sauf demande explicite d'archivage dans `scripts/`.</li>
    </ul>
  </div>
</details>
<details id="git-guardrails-claude-code" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/git-guardrails-claude-code</code>
      <span class="badge-mode">hook</span>
    </div>
    <span class="skill-short-title">Crochets de sécurité bloquant les commandes Git destructrices d'un agent.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="git-guardrails-claude-code">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Crochets de sécurité interceptant les commandes Git destructrices d'un agent autonome.</li>
        <li><strong>Invocation</strong> : Installation de hooks.</li>
        <li><strong>Règle d'or</strong> : Bloque impitoyablement `push --force`, `reset --hard`, `clean -fd` et suppressions brutales de branches.</li>
    </ul>
  </div>
</details>
<details id="setup-pre-commit" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/setup-pre-commit</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Configuration des contrôles rapides avant commit (Husky, lint-staged, tests ciblés).</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="setup-pre-commit">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/misc/setup-pre-commit" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Mise en place de contrôles automatisés rapides avant chaque commit Git.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Entrées / Sorties</strong> : Configure Husky, lint-staged, le formatage Prettier, le typage et les tests ciblés.</li>
        <li><strong>Règle d'or</strong> : Empêche l'introduction de code mal formaté ou cassé dans l'historique local.</li>
    </ul>
  </div>
</details>
<details id="handoff" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/handoff</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Passerelle portative inter-sessions pour vider le contexte sans perdre les acquis.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="handoff">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Passerelle inter-sessions pour vider le contexte conversationnel sans perdre les acquis.</li>
        <li><strong>Invocation</strong> : `user-invoked` (`/handoff`).</li>
        <li><strong>Quand l'invoquer</strong> : Dès qu'une session approche des 100k tokens ou lors d'une bifurcation vers un prototype.</li>
        <li><strong>Entrées / Sorties</strong> : Compacte la conversation dans un fichier Markdown temporaire dans `/tmp/` (hors dépôt), avec liste des compétences recommandées pour la session suivante.</li>
        <li><strong>Règle d'or</strong> : Ne stockez jamais de handoff dans le dépôt Git ; utilisez `/tmp/`.</li>
    </ul>
  </div>
</details>
<details id="writing-great-skills" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/writing-great-skills</code>
      <span class="badge-mode">référence</span>
    </div>
    <span class="skill-short-title">Le traité d'ingénierie pour concevoir des compétences d'agents prévisibles.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="writing-great-skills">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Le traité d'ingénierie des compétences d'agents.</li>
        <li><strong>Invocation</strong> : Document de référence.</li>
        <li><strong>Principes clés</strong> : Hiérarchie d'information (étapes directes vs références externalisées), divulgation progressive, élimination sans pitié des phrases creuses (*no-ops*), mots directeurs (*leading words*).</li>
        <li><strong>Règle d'or</strong> : Une compétence sert à arracher du déterminisme à un système stochastique. Sa prévisibilité prime sur tout.</li>
    </ul>
  </div>
</details>
<details id="find-skills" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/find-skills</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Découverte et installation de compétences communautaires.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="find-skills">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/vercel-labs/skills/tree/main/skills/find-skills" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Outil de découverte et d'installation de compétences d'agents issues de la communauté.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## 6. Pédagogie, Rédaction & Gestion des Savoirs
<p class="family-lead">Outille l'enseignement technique, la conception d'exercices et la chaîne de publication éditoriale du manuel.</p>
<div class="skills-accordion-group">
<details id="teach" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/teach</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Enseignement interactif d'un concept où le workspace sert d'atelier d'expérimentation.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="teach">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/productivity/teach" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Enseignement interactif d'un concept technique où le workspace sert d'atelier d'expérimentation.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
    </ul>
  </div>
</details>
<details id="scaffold-exercises" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/scaffold-exercises</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Génération de structures complètes d'exercices de cours avec tests de validation.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="scaffold-exercises">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/misc/scaffold-exercises" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Générateur de structures d'exercices de cours (énoncé, indices, solution, suite de tests de validation).</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
    </ul>
  </div>
</details>
<details id="writing-fragments" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/writing-fragments</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Capture et organisation des matériaux bruts et pensées non structurées.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="writing-fragments">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-fragments" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Première phase de la chaîne de rédaction : collecte brute d'intuitions, de faits et d'exemples sans souci de plan ni de style.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
    </ul>
  </div>
</details>
<details id="writing-beats" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/writing-beats</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Structuration du rythme narratif et de la progression logique d'un texte.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="writing-beats">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-beats" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Deuxième phase : assemblage du matériau brut en pulsations logiques (*beats*).</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <li><strong>Règle d'or</strong> : Chaque notion doit être posée et définie avant qu'une pulsation suivante ne s'appuie dessus.</li>
    </ul>
  </div>
</details>
<details id="writing-shape" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/writing-shape</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Façonnage et ciselage des paragraphes et transitions thématiques.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="writing-shape">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/in-progress/writing-shape" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Troisième phase : façonnage rédigé, paragraphe par paragraphe, à partir des pulsations validées.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
    </ul>
  </div>
</details>
<details id="edit-article" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/edit-article</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Relecture éditoriale impitoyable éliminant le verbiage et les fausses évidences.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="edit-article">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/personal/edit-article" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Quatrième phase : ciselage éditorial, resserrement de la prose et élimination des tournures passives.</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
    </ul>
  </div>
</details>
<details id="obsidian-vault" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/obsidian-vault</code>
      <span class="badge-mode">user-invoked</span>
    </div>
    <span class="skill-short-title">Exploration et mise à jour raisonnée de notes personnelles dans un coffre Obsidian.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="obsidian-vault">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/personal/obsidian-vault" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Organisation et maillage de la base de connaissances personnelle en Markdown (liens wiki, notes d'index).</li>
        <li><strong>Invocation</strong> : `user-invoked`.</li>
        <p>---</p>
    </ul>
  </div>
</details>
</div>

---
## Compétences Absorbées ou Dépréciées
<p class="family-lead">Compétences des premières versions de Matt Pocock, aujourd'hui intégrées dans les briques canoniques.</p>
<div class="skills-accordion-group">
<details id="design-an-interface" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/design-an-interface</code>
      <span class="badge-mode">déprécié</span>
    </div>
    <span class="skill-short-title">Absorbé par /codebase-design et /tdd.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="design-an-interface">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/deprecated/design-an-interface" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Absorbé par /codebase-design et /tdd.</li>
        <li><strong>Invocation</strong> : `déprécié`</li>
    </ul>
  </div>
</details>
<details id="request-refactor-plan" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/request-refactor-plan</code>
      <span class="badge-mode">déprécié</span>
    </div>
    <span class="skill-short-title">Absorbé par /improve-codebase-architecture.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="request-refactor-plan">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/deprecated/request-refactor-plan" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Absorbé par /improve-codebase-architecture.</li>
        <li><strong>Invocation</strong> : `déprécié`</li>
    </ul>
  </div>
</details>
<details id="ubiquitous-language" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/ubiquitous-language</code>
      <span class="badge-mode">déprécié</span>
    </div>
    <span class="skill-short-title">Absorbé par /domain-modeling et CONTEXT.md.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="ubiquitous-language">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/deprecated/ubiquitous-language" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Absorbé par /domain-modeling et CONTEXT.md.</li>
        <li><strong>Invocation</strong> : `déprécié`</li>
    </ul>
  </div>
</details>
<details id="qa" class="skill-card">
  <summary class="skill-summary">
    <div class="skill-meta-badges">
      <code class="badge-cmd">/qa</code>
      <span class="badge-mode">déprécié</span>
    </div>
    <span class="skill-short-title">Absorbé par le double péage de /review.</span>
  </summary>
  <div class="skill-expanded-body">
    <div class="skill-actions-bar">
      <button type="button" class="btn-copy-link" data-anchor="qa">
        <span class="copy-icon">🔗</span> <span class="copy-text">Copier le lien direct</span>
      </button>
      <a href="https://github.com/mattpocock/skills/tree/main/skills/deprecated/qa" target="_blank" rel="external noopener noreferrer" class="link-github">
        Code source sur GitHub ↗
      </a>
    </div>
    <ul class="skill-fields-list">
      <li><strong>Rôle & Intention</strong> : Absorbé par le double péage de /review.</li>
        <li><strong>Invocation</strong> : `déprécié`</li>
    </ul>
  </div>
</details>
</div>

---

<style>
.family-lead {
  font-size: .95rem;
  color: var(--muted);
  margin-bottom: 1.2rem;
}
.skills-accordion-group {
  display: flex;
  flex-direction: column;
  gap: .6rem;
  margin-bottom: 2rem;
}
.skill-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 4px;
  overflow: hidden;
  transition: border-color .15s ease, box-shadow .15s ease;
}
.skill-card:hover {
  border-color: var(--accent);
}
.skill-card[open] {
  background: var(--paper);
  border-color: var(--accent);
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.skill-card.highlight-skill {
  outline: 2px solid var(--accent);
  box-shadow: 0 0 12px rgba(35, 98, 82, 0.35);
  animation: pulse-border 1.5s ease-in-out;
}
@keyframes pulse-border {
  0% { transform: scale(1); }
  50% { transform: scale(1.01); }
  100% { transform: scale(1); }
}
.skill-summary {
  padding: .85rem 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: baseline;
  gap: 1rem;
  user-select: none;
  font-family: var(--sans);
}
.skill-summary:focus-visible {
  outline: 2px solid var(--rust);
}
.skill-meta-badges {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-shrink: 0;
}
.badge-cmd {
  font-family: ui-monospace, Consolas, monospace;
  font-size: .84rem;
  font-weight: 600;
  color: var(--ink);
  background: var(--paper);
  padding: .15rem .45rem;
  border-radius: 3px;
  border: 1px solid var(--line);
}
.skill-card[open] .badge-cmd {
  background: var(--surface);
  color: var(--accent);
  border-color: var(--accent);
}
.badge-mode {
  text-transform: uppercase;
  letter-spacing: .08em;
  font-size: .62rem;
  font-weight: 650;
  color: var(--muted);
}
.skill-short-title {
  font-size: .88rem;
  color: var(--ink);
  line-height: 1.35;
}
.skill-expanded-body {
  padding: 1.1rem 1.3rem 1.3rem;
  border-top: 1px solid var(--line);
  background: var(--paper);
}
.skill-actions-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: .8rem;
  padding-bottom: .85rem;
  margin-bottom: 1rem;
  border-bottom: 1px dashed var(--line);
}
.btn-copy-link {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 3px;
  padding: .35rem .7rem;
  font-size: .75rem;
  font-family: var(--sans);
  color: var(--ink);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  transition: all .15s ease;
}
.btn-copy-link:hover {
  background: var(--paper);
  border-color: var(--accent);
  color: var(--accent);
}
.btn-copy-link.copied {
  background: var(--accent);
  color: #ffffff;
  border-color: var(--accent);
}
.link-github {
  font-size: .78rem;
  color: var(--muted);
  text-decoration: none;
}
.link-github:hover {
  color: var(--accent);
  text-decoration: underline;
}
.skill-fields-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: .65rem;
  font-family: var(--sans);
  font-size: .86rem;
  line-height: 1.55;
}
.skill-fields-list li {
  margin: 0;
}
.skill-fields-list strong {
  color: var(--ink);
  font-weight: 650;
}
@media(max-width: 680px) {
  .skill-summary {
    flex-direction: column;
    gap: .4rem;
  }
}
</style>

<script>
(function() {
  function openAnchorSkill() {
    const hash = window.location.hash.slice(1);
    if (!hash) return;
    const target = document.getElementById(hash);
    if (target && target.tagName === 'DETAILS') {
      target.open = true;
      target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      target.classList.add('highlight-skill');
      setTimeout(() => {
        target.classList.remove('highlight-skill');
      }, 2500);
    }
  }

  window.addEventListener('load', openAnchorSkill);
  window.addEventListener('hashchange', openAnchorSkill);

  document.querySelectorAll('.btn-copy-link').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const anchor = btn.getAttribute('data-anchor');
      const url = window.location.origin + window.location.pathname + '#' + anchor;
      navigator.clipboard.writeText(url).then(() => {
        const textSpan = btn.querySelector('.copy-text');
        const origText = textSpan.textContent;
        btn.classList.add('copied');
        textSpan.textContent = 'Lien copié !';
        setTimeout(() => {
          btn.classList.remove('copied');
          textSpan.textContent = origText;
        }, 2000);
      });
    });
  });
})();
</script>
