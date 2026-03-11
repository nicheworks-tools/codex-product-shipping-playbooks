# AGENTS.md

## Purpose of this repository

This repository is an original **product shipping playbooks system** for repository-based Codex workflows.

It is not:

- a generic PM toolkit
- a clone of a skills repository
- a loose collection of templates
- a prompt dump

Its job is to help work move more consistently from:

- repository intake
- spec delta definition
- implementation planning
- acceptance definition
- pre-ship review
- release-facing follow-up
- post-change review

The native structure of the repository is built around:

- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`
- `adapters/`

If compatibility with another format is needed later, handle it through adapters.
Do not reshape the core repository just to imitate another ecosystem.

---

## Core rules

### 1. Workflow first
Each playbook must represent one concrete workflow step.

Good examples:
- understanding the repository
- defining a spec delta
- planning a change
- defining acceptance
- checking readiness before shipping

Bad examples:
- vague strategy buckets
- broad research categories
- generic product-thinking labels

### 2. Shipping first
Favor outputs that support real repository work.

Priority goes to:
- repository context
- scope definition
- spec deltas
- implementation plans
- acceptance criteria
- pre-ship review
- release-facing artifacts
- post-change review notes

Do not let the repository drift into a general PM library.

### 3. Repository-aware thinking
Before proposing changes, understand the repository context as much as possible.

Prefer concrete references to:
- files
- directories
- entry points
- constraints
- conventions
- likely touch points
- documentation impact
- shipping impact

Avoid outputs that ignore the codebase.

### 4. Clear handoffs
Every playbook should feed the next step cleanly.

A playbook is incomplete if its output does not help the next workflow step move forward.

---

## Clean-room rules

This repository may learn from public ideas, but it must remain original in wording, naming, structure, and framing.

### Allowed
- learning from public design ideas
- learning from general workflow concepts
- solving similar operational problems
- building equivalent functionality from scratch

### Not allowed
- copying README wording
- copying section structure line by line
- copying template text
- copying naming too closely
- reproducing another project’s public identity

When in doubt, rewrite from first principles.

---

## Structural rules

### Layer responsibilities

- `playbooks/`
  Concrete workflow units

- `artifacts/`
  Reusable output templates

- `gates/`
  Review and completion checkpoints

- `flows/`
  Multi-step workflow chains

- `docs/`
  Supporting design and operating documents

- `adapters/`
  Optional export or compatibility tools

### Required separation
Do not blur these layers.

Examples:
- reusable templates belong in `artifacts/`
- completion checks belong in `gates/`
- multi-step sequences belong in `flows/`

---

## Rules for playbooks

### One folder, one responsibility
Each playbook folder must represent one clear workflow role.

### Required file
Each playbook must include:
- `PLAYBOOK.md`

It may also include:
- `artifacts/`
- `gates/`
- `scripts/`
- `flow-example.md`

### Every `PLAYBOOK.md` must make these points clear
- what the playbook is for
- when to use it
- when not to use it
- what inputs it expects
- what artifacts it creates or updates
- what gates it should pass
- what comes next

### Naming rule
Use action-oriented kebab-case names.

Prefer:
- `intake-repo`
- `spec-delta`
- `plan-change`
- `define-acceptance`
- `ship-check`

Avoid broad category names.

---

## Rules for artifacts

Artifacts are reusable output templates.

Each artifact should:
- have a clear operational purpose
- be usable in real work with minimal rewriting
- avoid generic filler language
- connect naturally to one or more playbooks

Use explicit filenames such as:
- `spec-delta-template.md`
- `change-plan-template.md`
- `acceptance-template.md`

Avoid vague names such as:
- `template.md`
- `general-template.md`
- `notes.md`

---

## Rules for gates

Gates are explicit review or completion checkpoints.

A gate should:
- be concrete
- be short enough to use in real work
- include implementation, docs, and shipping concerns where relevant

A gate is a decision point, not a motivational checklist.

---

## Rules for flows

Flows describe how multiple playbooks connect.

Each flow should:
- show the order of steps
- show what output feeds the next step
- explain what triggers the flow
- stay practical

Flows are how this repository proves that its playbooks work together as a system.

---

## Writing rules

### Prefer
- clear language
- direct wording
- concrete operational terms
- repository-aware examples

Use real work terms such as:
- repo
- file
- test
- docs
- release
- diff
- scope
- risk
- acceptance

### Avoid
- exaggerated claims
- buzzword-heavy prose
- generic product-management language
- vague theory without operational consequence

Do not write like marketing copy.
Write like someone building a practical working system.

---

## Quality bar

A new or updated playbook is not good enough unless:

1. its role can be explained in one sentence
2. its use cases and non-use cases are clear
3. its inputs and outputs are concrete
4. it maps to at least one artifact or gate
5. it connects to the next workflow step
6. it supports repo-aware, implementation-aware, or ship-aware work
7. the reason to use it with Codex can be explained clearly
8. it can be tested in a real repository workflow

If these are not true, revise the design before expanding the content.

---

## Expansion rules

### Add a new playbook only when:
- an existing workflow step is overloaded
- a clear boundary exists
- the new playbook creates real operational value
- it is not just a renamed version of something already present

### Prefer strengthening before expanding
Before adding more playbooks, improve:
- artifacts
- gates
- flows
- examples
- naming clarity
- cross-references

---

## Adapter policy

Adapters are optional support tools.
They are not the core identity of the project.

If a Codex export format is added later:
- keep it inside `adapters/`
- export from the native structure
- do not redesign the repository around the adapter

Native first, compatibility second.

---

## Final rule

This repository should always feel like:

**a practical shipping workflow system for real repositories**

and never like:

- a clone of someone else’s skills repo
- a generic PM template dump
- a loose collection of disconnected notes
