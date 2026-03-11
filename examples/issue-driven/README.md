# Issue-Driven Example

## Purpose of this example

This example set shows how the repository can be used when work begins from an issue, ticket, or bug report rather than from a fully defined change request.

The point is to demonstrate how the workflow helps turn issue language into repository-aware shipping work.

---

## Scenario

A repository has an issue that says:

> Search filters are sometimes cleared after navigating between pages.

The issue reports a visible problem, but it does not clearly define:

- the current repository behavior
- the real scope of the change
- the likely touch points
- what should count as done

This makes it a good issue-driven example.

---

## Why this example matters

Issue-driven work often starts with language like:

- “sometimes broken”
- “should be faster”
- “doesn’t work right”
- “seems to reset”

That language is useful as a signal, but it is not enough to support reliable implementation or shipping decisions.

This example set shows how the repository structure helps convert a raw issue into operational workflow steps.

---

## Core workflow covered

This example now covers the full current path from issue intake through post-ship learning:

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`
6. `write-release-artifacts`
7. `review-diff`
8. `post-ship-retro`

---

## Included example set

### `filter-persistence/`

This synthetic example walks through a concrete issue where selected filters are lost after navigation.

It includes:

- `00-issue.md`
- `01-repo-context-memo.md`
- `02-spec-delta.md`
- `03-change-plan.md`
- `04-acceptance-definition.md`
- `05-pre-ship-review.md`
- `06-release-note.md`
- `07-changelog-entry.md`
- `08-diff-review.md`
- `09-retro.md`

This is the first full end-to-end example in the repository.

---

## Artifacts represented in the example

This example now demonstrates the use of:

- `artifacts/spec-delta-template.md`
- `artifacts/change-plan-template.md`
- `artifacts/acceptance-template.md`
- `artifacts/pre-ship-review-template.md`
- `artifacts/release-note-template.md`
- `artifacts/changelog-entry-template.md`
- `artifacts/diff-review-template.md`
- `artifacts/retro-template.md`

---

## Why this example is useful

This example shows how the system helps when the starting point is weak or incomplete issue language.

Its value is in turning:

- symptoms into repository-aware understanding
- complaints into scope
- requests into plans
- implementation into reviewable acceptance
- shipping readiness into release-facing communication
- completed changes into review and learning

---

## What this example does not try to prove

This example does not try to prove:

- behavior taken from a live production repository
- a multi-team release process
- every possible variation of release workflow

Its purpose is to serve as a synthetic but realistic end-to-end workflow demonstration.
