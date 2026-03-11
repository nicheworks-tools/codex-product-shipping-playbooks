# Architecture

## Overview

This repository is structured as a layered system.

The goal is to keep these responsibilities separate:

- workflow units
- reusable output templates
- review checkpoints
- end-to-end sequences
- compatibility or export logic

This separation prevents the repository from collapsing into a vague mix of notes, templates, and half-defined instructions.

---

## Top-level architecture

```text
codex-product-shipping-playbooks/
├─ AGENTS.md
├─ README.md
├─ spec/
├─ docs/
├─ playbooks/
├─ artifacts/
├─ gates/
├─ flows/
├─ examples/
├─ scripts/
├─ adapters/
└─ archive/
```

Each top-level area has a distinct role.

---

## Layer responsibilities

### `AGENTS.md`

Repository-wide rules and constraints.

This file defines:

* what this repository is trying to be
* what it must avoid becoming
* naming rules
* quality expectations
* separation rules between layers

This is the highest-level operational rule file inside the repository.

---

### `spec/`

Formal project specifications.

This layer stores the main project specification documents, including language-specific versions where needed.

It exists to preserve the source-of-truth model of the project.

This layer should answer:

* what the repository is supposed to become
* what its boundaries are
* what “complete” means

---

### `docs/`

Supporting design and operating documents.

This layer explains:

* vision
* architecture
* workflows
* naming
* roadmap
* quality standards

`docs/` supports understanding.
It does not replace `spec/`.

---

### `playbooks/`

Concrete workflow units.

This is the operational core of the repository.

Each playbook represents one clear workflow responsibility, such as:

* understanding a repository
* defining a spec delta
* planning a change
* defining acceptance
* checking readiness before shipping

A playbook is not a theme or department.
It is a concrete step in work.

---

### `artifacts/`

Reusable templates for outputs.

Artifacts are the forms of output that playbooks create or update.

Examples:

* spec delta templates
* change plan templates
* acceptance templates
* pre-ship review templates
* release note templates

Artifacts are shared resources.
They should not be buried inside random prose.

---

### `gates/`

Review and completion checkpoints.

A gate defines what must be true before a workflow step is considered complete.

Examples:

* repository intake gate
* spec delta gate
* acceptance gate
* pre-ship gate

Gates are practical review tools, not aspirational lists.

---

### `flows/`

Multi-step workflow chains.

A flow explains how multiple playbooks connect in sequence.

Examples:

* issue to ship
* repo change flow
* diff to retrospective
* release preparation flow

A flow should make handoffs visible.
It shows how outputs from one step become inputs to the next.

---

### `examples/`

Illustrative usage scenarios.

Examples show how the system can be used in realistic contexts.

They are not the main architecture, but they are important for proving that the structure works in practice.

---

### `scripts/`

Local maintenance and validation scripts.

This layer exists to support repository hygiene.

Typical scripts include:

* structure validation
* required file checks
* markdown checks
* index generation

Scripts are support tools, not the core product.

---

### `adapters/`

Compatibility or export layer.

Adapters exist for optional export into external formats.

The main rule of this layer is simple:

**the native structure comes first**

Adapters should export from the project’s own structure.
The project must not be redesigned around adapter needs.

---

### `archive/`

Deprecated or superseded materials.

This layer stores old playbooks, old artifacts, or retired materials that should not remain in active use.

Archive content should be clearly separated from active content.

---

## Why the architecture is layered this way

The repository uses this layered structure for three reasons.

### 1. Clarity

A user should be able to tell the difference between:

* a workflow step
* a template
* a review gate
* a multi-step sequence
* an optional compatibility layer

If those are mixed together, the project becomes harder to understand and harder to maintain.

### 2. Maintainability

A clean separation makes updates easier.

Examples:

* a template can change without rewriting the entire playbook
* a gate can become stricter without changing the flow definition
* a flow can be expanded without changing the core playbook purpose

### 3. Originality

This structure helps the repository remain distinct from skills-based public repositories.

The architecture is designed around workflow execution, not around a skills catalog format.

---

## Playbook model

Each playbook folder has this minimum structure:

```text
playbooks/<playbook-name>/
├─ PLAYBOOK.md
└─ flow-example.md
```

### `PLAYBOOK.md`

The central definition of the playbook.

It must define:

* purpose
* use cases
* non-use cases
* required inputs
* output artifacts
* required gates
* procedure
* next playbook in the workflow

### `flow-example.md`

A concrete example of how the playbook appears in a real sequence.

### Optional local directories

A playbook may also include local support directories such as:

* `artifacts/`
* `gates/`
* `scripts/`

These are optional.
They should only be added when a playbook actually needs local material that should not live in the shared top-level layers.

---

## Core workflow model

The first working loop of the repository is built around five playbooks:

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

This loop represents the minimum viable shipping path.

It moves from understanding the repository to checking whether a change is ready to ship.

Later expansion adds:

* `write-release-artifacts`
* `review-diff`
* `post-ship-retro`

These extend the system from pre-ship work into release and post-change learning.

---

## Relationship between layers

The intended relationship is:

* **playbooks** define what to do
* **artifacts** define what gets produced
* **gates** define what must be true
* **flows** define how steps connect
* **examples** demonstrate real use
* **adapters** export the system when needed

That relationship should remain stable as the repository grows.

---

## Structural rules

The following structural rules must be preserved.

### Rule 1

Do not treat a playbook as a generic topic bucket.

### Rule 2

Do not bury reusable templates inside long prose files.

### Rule 3

Do not hide review criteria inside unrelated documents.

### Rule 4

Do not blur the line between the native structure and compatibility layers.

### Rule 5

Do not add new top-level layers casually.

Any new structural layer must solve a real architecture problem, not just a naming preference.

---

## Evolution path

The structure is designed to expand gradually without losing clarity.

### Foundation phase

* establish the top-level layers
* define the first five playbooks
* create the first artifacts, gates, and flows

### MVP phase

* make the first issue-to-pre-ship loop usable
* test the structure against real work
* improve boundaries and naming

### Expansion phase

* add release artifacts
* add diff review
* add post-ship retrospective
* expand examples and validation scripts

### Public release phase

* improve public clarity
* improve adapter support if needed
* formalize quality standards
* prepare the repository for publication

---

## Architecture success criteria

The architecture is working if:

* readers can understand the top-level layers quickly
* playbooks do not overlap heavily
* artifacts are reusable
* gates are practical
* flows show realistic handoffs
* the repository feels workflow-native rather than skills-clone-like
* the structure still makes sense as content grows

If these are no longer true, the structure needs to be revisited.
