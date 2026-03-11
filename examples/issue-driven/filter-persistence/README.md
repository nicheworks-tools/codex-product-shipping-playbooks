# Filter Persistence Example

## Purpose of this example

This example shows how the repository’s MVP workflow can turn an issue report into a structured pre-ship decision.

The scenario is intentionally simple:
a user reports that selected filters are sometimes cleared after navigation.

The goal is to show how the playbooks help transform that issue into:

- repository-aware understanding
- a defined change delta
- a practical change plan
- explicit acceptance criteria
- a structured pre-ship review

---

## Scenario summary

A web application includes a filter bar on a listing page.

Users expect selected filters to remain active when they navigate to another page and then return.

Instead, the filters sometimes reset.

The issue report describes the symptom, but not the repository structure, implementation shape, or acceptance conditions.

---

## Important note

This is a **synthetic example** created to demonstrate the workflow model.

It is not a record copied from a live production repository.
Its purpose is to show how one issue can move through the repository’s playbooks in a realistic but controlled way.

---

## Workflow used

This example follows the MVP workflow:

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

---

## Files in this example

- `00-issue.md`
  The starting issue report

- `01-repo-context-memo.md`
  Repository-aware context collected through `intake-repo`

- `02-spec-delta.md`
  Change definition produced through `spec-delta`

- `03-change-plan.md`
  Implementation-oriented plan produced through `plan-change`

- `04-acceptance-definition.md`
  Completion criteria produced through `define-acceptance`

- `05-pre-ship-review.md`
  Sample pre-ship decision produced through `ship-check`

---

## Why this example matters

This is a small issue, but it is still enough to demonstrate the value of the system.

Without structure, the team might jump straight into code changes.
With the workflow, the team instead produces:

- a clearer understanding of what is actually wrong
- explicit scope boundaries
- a more reviewable implementation plan
- a defined idea of what “done” means
- a reasoned shipping decision

That is exactly the kind of value this repository is meant to provide.
