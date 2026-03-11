# Workflows

## Purpose of this document

This document explains how the playbooks connect into actual working sequences.

A playbook on its own is only one step.
The value of this repository comes from how those steps connect through artifacts, gates, and handoffs.

This document exists to make those connections explicit.

---

## Core workflow model

The repository is built around a shipping-oriented flow.

The base workflow is:

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

This is the minimum working loop.

It moves from repository understanding to change definition, then to execution planning, completion criteria, and pre-ship review.

---

## Workflow philosophy

### 1. Repository context comes first
The system should not jump into planning before understanding the codebase.

That is why `intake-repo` comes first.

### 2. A change must be defined before it is planned
The workflow separates “what is changing” from “how to implement it.”

That is why `spec-delta` comes before `plan-change`.

### 3. Acceptance should be defined before shipping
Implementation work is not enough.
The system needs an explicit idea of what “done” means.

That is why `define-acceptance` comes before `ship-check`.

### 4. Shipping is a review step, not just a feeling
“Looks ready” is not enough.
A real pre-ship checkpoint is required.

That is the role of `ship-check`.

---

## Workflow 1: Repository intake to pre-ship

### Summary
This is the baseline workflow for a requested change inside an existing repository.

### Sequence

#### Step 1: `intake-repo`
Use this step to understand:
- repository structure
- key files
- entry points
- conventions
- obvious constraints
- unclear areas that need follow-up

#### Output
- repository context memo
- key file list
- constraints list
- missing context notes

#### Step 2: `spec-delta`
Use the repository context plus the requested change to define:
- what is changing
- what is not changing
- what surfaces are likely affected
- what assumptions are being made

#### Output
- spec delta draft
- in-scope / out-of-scope section
- impacted surfaces
- assumptions

#### Step 3: `plan-change`
Turn the spec delta into a practical implementation plan.

This step should define:
- likely touch points
- implementation steps
- sequencing
- documentation impact
- notable risks

#### Output
- change plan
- touch point list
- implementation steps
- docs impact notes

#### Step 4: `define-acceptance`
Define what has to be true before the change can be considered complete.

This step should clarify:
- acceptance criteria
- manual checks
- edge cases
- done conditions

#### Output
- acceptance definition
- done checklist
- edge-case notes
- manual verification notes

#### Step 5: `ship-check`
Review whether the change is actually ready to ship.

This step should check:
- unresolved blockers
- unverified assumptions
- release risks
- docs and communication readiness

#### Output
- pre-ship review
- blockers and risks
- final readiness notes

---

## Workflow 2: Issue-driven change flow

### Summary
This workflow starts from an issue, ticket, or problem report rather than a vague request.

### Sequence
1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

### Special emphasis
In issue-driven cases, the system should pay extra attention to:
- what the issue claims
- whether the issue describes symptoms or root cause
- whether the requested solution should be challenged
- whether repository reality matches the issue description

### Useful outputs
This workflow is especially useful for producing:
- clearer scope boundaries
- implementation-ready change plans
- explicit done criteria

---

## Workflow 3: Release-preparation extension

### Summary
This workflow extends the core loop after `ship-check`.

It belongs to the completed version of the repository, not the earliest foundation phase.

### Sequence
1. `ship-check`
2. `write-release-artifacts`
3. `review-diff`
4. `post-ship-retro`

### Purpose
This extension supports:
- release note preparation
- changelog writing
- change summarization
- post-change learning

---

## Workflow 4: Diff-to-review flow

### Summary
This workflow begins after implementation work already exists.

It is useful when the repository already contains a diff, PR, or change set that needs to be reviewed and learned from.

### Sequence
1. `review-diff`
2. `post-ship-retro`

### Purpose
This workflow helps the repository produce:
- concise change summaries
- review notes
- follow-up items
- lessons learned

---

## Hand-off model

Each step in the workflow should pass something concrete to the next step.

### `intake-repo` -> `spec-delta`
Pass:
- repository context
- key files
- constraints
- unresolved unknowns

### `spec-delta` -> `plan-change`
Pass:
- the defined change
- scope boundaries
- assumptions
- impacted surfaces

### `plan-change` -> `define-acceptance`
Pass:
- proposed implementation shape
- likely risks
- areas needing verification

### `define-acceptance` -> `ship-check`
Pass:
- explicit done conditions
- edge cases
- verification expectations

### `ship-check` -> release-facing work
Pass:
- final readiness status
- blockers
- release concerns
- documentation concerns

---

## Workflow boundaries

These workflows are designed for repositories that already exist.

They are not intended to cover:
- pure ideation with no codebase
- broad market planning
- strategy-only work disconnected from implementation
- abstract PM theory

The workflows should stay close to real repository operations.

---

## What makes a workflow healthy

A workflow in this repository is healthy when:

- each step has a clear purpose
- each step produces concrete output
- the handoff to the next step is obvious
- artifacts are reused instead of rewritten from scratch
- gates are practical enough to actually use
- the flow stays tied to a real repository

If these conditions are missing, the workflow needs revision.

---

## Future workflow extensions

The structure is designed to support additional workflow variants later, such as:

- issue to release flow
- bug report to rollback decision flow
- release prep to post-ship monitoring flow
- diff review to improvement backlog flow

These should only be added if they solve a real operational need and do not weaken the clarity of the core flow.
