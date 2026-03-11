# Naming

## Purpose of this document

This document defines the naming rules for the repository.

Naming matters because this project must remain:

- understandable
- practical
- structurally clean
- distinct from clone-like patterns

Good naming should make the system easier to use and easier to explain.

---

## General naming principles

### 1. Prefer action over category
Names should describe what the file or folder does, not a broad abstract topic.

Prefer:
- `spec-delta`
- `plan-change`
- `ship-check`

Avoid:
- `strategy`
- `research`
- `execution`
- `product-thinking`

The repository is workflow-first, so names should reflect work steps.

### 2. Prefer concrete language
Names should feel tied to actual repository work.

Prefer words like:
- repo
- spec
- change
- acceptance
- ship
- release
- diff
- retro

Avoid language that feels:
- vague
- aspirational
- overly corporate
- generic PM flavored

### 3. Keep names short but meaningful
A name should be easy to scan in a repository tree.

Short names are good, but only if the purpose remains clear.

### 4. Keep naming patterns consistent
Once a naming pattern is chosen for a layer, follow it consistently.

Examples:
- playbooks use kebab-case action names
- artifacts use `<purpose>-template.md`
- gates use `<purpose>-gate.md`

### 5. Preserve originality
Names should not be chosen in a way that makes the repository feel like a direct descendant of an existing public system.

Even when solving similar problems, the naming should remain recognizably its own.

---

## Top-level naming rules

### Repository name
Current working repository name:

`codex-product-shipping-playbooks`

This may be revised later, but the name should continue to signal:

- Codex context
- shipping focus
- playbooks structure

### Top-level directories
Approved top-level layer names:

- `docs/`
- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`
- `examples/`
- `scripts/`
- `adapters/`
- `archive/`
- `spec/`

These names are intentionally distinct from a skills-first structure.

---

## Playbook naming rules

### Pattern
Use **kebab-case** action-oriented names.

### Preferred form
Use a verb or action-plus-object structure.

Examples:
- `intake-repo`
- `spec-delta`
- `plan-change`
- `define-acceptance`
- `ship-check`
- `write-release-artifacts`
- `review-diff`
- `post-ship-retro`

### What playbook names should communicate
A playbook name should suggest:
- what step of work it belongs to
- what it produces
- where it fits in the sequence

### Avoid
Do not use:
- broad department-like names
- generic PM categories
- abstract nouns with unclear workflow meaning

Avoid examples such as:
- `product-strategy`
- `market-research`
- `roadmapping`
- `operations`
- `execution`

Those names weaken the workflow identity.

---

## `PLAYBOOK.md` naming rule

Each playbook folder should contain:

`PLAYBOOK.md`

The uppercase filename is intentional.
It makes the defining file inside each playbook easy to spot.

No alternative names should be introduced for the defining playbook file.

---

## Artifact naming rules

### Pattern
Use:

`<purpose>-template.md`

### Examples
- `spec-delta-template.md`
- `change-plan-template.md`
- `acceptance-template.md`
- `pre-ship-review-template.md`
- `release-note-template.md`
- `changelog-entry-template.md`
- `rollback-note-template.md`

### Rule
Artifact names should make their operational purpose obvious.

Do not use filenames like:
- `template.md`
- `general-template.md`
- `notes-template.md`

---

## Gate naming rules

### Pattern
Use:

`<purpose>-gate.md`

### Examples
- `repo-intake-gate.md`
- `spec-delta-gate.md`
- `acceptance-gate.md`
- `pre-ship-gate.md`
- `release-artifacts-gate.md`
- `retro-gate.md`

### Rule
A gate name should make it clear what checkpoint it represents.

Do not use vague names like:
- `quality-gate.md`
- `review-gate.md`
- `final-gate.md`

unless the scope is truly repository-wide.

---

## Flow naming rules

### Pattern
Use either:

- `<context>-flow.md`
- `<from>-to-<to>.md`

### Examples
- `repo-change-flow.md`
- `release-prep-flow.md`
- `issue-to-ship.md`
- `diff-to-retro.md`

### Rule
A flow name should communicate either:
- the context of the sequence, or
- the start and end points of the sequence

---

## Example naming rules

### Directory names
Example directories should describe the scenario clearly.

Examples:
- `small-repo/`
- `issue-driven/`
- `release-cycle/`

### File names
Example filenames should be easy to scan and tied to the scenario.

Prefer:
- `README.md`
- `sample-flow.md`
- `example-01.md`

Avoid opaque names like:
- `notes.md`
- `test.md`
- `misc.md`

---

## Script naming rules

### Pattern
Use **snake_case** for scripts.

Examples:
- `validate_structure.py`
- `check_required_files.py`
- `lint_markdown.py`
- `build_index.py`

### Rule
Script names should communicate what the script checks or builds.

Avoid vague names like:
- `run.py`
- `tool.py`
- `check.py`

---

## Adapter naming rules

### Pattern
Adapters should describe the export or compatibility target.

Examples:
- `export_codex_skill_format.py`

### Rule
Adapter names should make it obvious:
- what they export to
- whether they are import or export tools
- whether they are one-way or bidirectional

If more adapters are added later, keep the naming explicit.

---

## Document naming rules inside `docs/`

Files in `docs/` should use lowercase kebab-case or clear lowercase names, depending on readability.

Current approved names include:
- `vision.md`
- `architecture.md`
- `workflows.md`
- `roadmap.md`
- `quality-gates.md`
- `naming.md`
- `release-model.md`
- `artifacts-model.md`

### Rule
A docs filename should reflect one clear concept.

Avoid unnecessary fragmentation into too many tiny files unless there is a real structural reason.

---

## Naming review checklist

Before finalizing a name, check the following:

1. Does the name reflect a concrete role?
2. Does it fit the layer it belongs to?
3. Is it consistent with nearby names?
4. Does it sound too much like a clone?
5. Would a new reader understand it without extra explanation?
6. Does it strengthen the workflow-first identity?

If the answer to several of these is no, rename it before proceeding.

---

## Naming success condition

Naming is good enough when:

- the repository tree is easy to scan
- the role of each file or folder is easy to infer
- the structure feels original
- the names reinforce workflow and shipping work
- the system does not read like a generic PM library

That is the standard this repository should follow.
