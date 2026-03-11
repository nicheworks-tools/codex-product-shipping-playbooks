# Repo Change Flow

## Purpose of this flow

This flow describes how to use the core playbooks when the starting point is **not** a formal issue.

It exists to cover repository-driven work such as:

* an internal request
* an observed repository problem
* a refactor need
* a scope adjustment discovered during implementation
* maintenance work where the codebase itself is the clearest source of truth

This is a secondary MVP flow.
Its purpose is to show that the playbooks can support repository-driven work, not only issue-driven work.

---

## How this differs from `issue-to-ship`

`issue-to-ship.md` begins with a reported issue and turns that issue into a pre-ship decision.

`repo-change-flow.md` begins with repository reality.

The difference is not the playbook chain.
The difference is the **starting point**.

Use `issue-to-ship` when the issue text is the main entry.
Use `repo-change-flow` when the repository itself is the main entry.

---

## When to use this flow

Use this flow when:

* there is already enough repository context to begin from codebase reality
* the request is informal, incomplete, or internal
* the team is reacting to something seen in the repository itself
* implementation and shipping impact matter more than issue wording

Do not use this flow when:

* a formal issue is already the clearest starting point
* the work is pure ideation with no repository
* the work is purely strategic and disconnected from implementation
* the work starts after implementation is already finished

---

## Flow sequence

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

This is the same core chain as the issue-driven MVP flow.
The distinction is that the repository is the primary source of truth at the start.

---

## Example starting points

This flow is useful when work begins from observations such as:

* “This state handling is too fragile and should be made more stable.”
* “This route transition causes confusing resets.”
* “This component has grown too coupled and needs a narrow refactor.”
* “This behavior is undocumented but clearly inconsistent with nearby code.”

These are valid starting points even when no formal issue exists yet.

---

## Step emphasis in this flow

### `intake-repo`

This step is especially important here because repository understanding is the main entry point.

Questions include:

* Where does the current behavior live?
* What is the likely source of the problem or change opportunity?
* What constraints are already visible in the codebase?

### `spec-delta`

In this flow, `spec-delta` often turns a repository observation into an explicit change definition.

Questions include:

* What is wrong with the current state?
* What should change?
* What should remain untouched?

### `plan-change`

This step should turn the repository-driven change into a practical implementation sequence.

Questions include:

* What files or surfaces are likely involved?
* What is the safest order of work?
* What documentation impact may exist?

### `define-acceptance`

This step prevents a repository-driven change from staying informal forever.

Questions include:

* What counts as completion?
* What edge cases matter?
* What must be checked manually?

### `ship-check`

This step makes sure the change is not treated as “ready” just because the coding feels finished.

Questions include:

* Are blockers still open?
* Are risks understood?
* Is the final recommendation clear?

---

## Handoff structure

### `intake-repo` -> `spec-delta`

Handoff:

* repository context memo
* key file list
* constraints
* missing context notes

### `spec-delta` -> `plan-change`

Handoff:

* change definition
* scope boundaries
* impacted surfaces
* assumptions and open questions

### `plan-change` -> `define-acceptance`

Handoff:

* implementation steps
* touch points
* documentation impact
* key risks

### `define-acceptance` -> `ship-check`

Handoff:

* acceptance criteria
* done checklist
* edge cases
* manual verification expectations

---

## Expected artifact chain

This flow usually creates or updates:

* `spec-delta-template.md`
* `change-plan-template.md`
* `acceptance-template.md`
* `pre-ship-review-template.md`

These artifacts should still form one connected workflow.

---

## Why this flow exists

This repository should not become useful only when issue wording is already available.

A real shipping workflow system should also help when work begins from repository observation, maintenance needs, or internal change pressure.

That is the reason this flow is kept separate from `issue-to-ship.md`.

---

## Signs that this flow is working

This flow is working when:

* repository understanding leads to a clearer change definition
* informal change requests become easier to review
* implementation planning becomes more concrete
* acceptance is made explicit instead of assumed
* shipping decisions become less ad hoc

If those outcomes are not visible, this flow is too close to `issue-to-ship` and should be simplified or merged later.
