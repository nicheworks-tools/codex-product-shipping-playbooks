# Diff Review Flow

## Purpose of this flow

This flow describes how work moves from implemented change into structured internal review.

It exists to capture what actually changed in implementation terms after shipping readiness and release-facing communication are already in place.

---

## When to use this flow

Use this flow when:

- the implementation already exists
- the team wants a clean internal record of the diff
- later retrospective work would benefit from a structured review artifact

Do not use this flow when:

- the change has not yet been implemented
- the task is still pre-ship
- the work is only about release-facing communication

---

## Flow sequence

1. `write-release-artifacts`
2. `review-diff`

This is the next extension after release-facing documentation.

---

## Step 1: `write-release-artifacts`

### Goal
Produce release-facing communication for a change that is ready to ship.

### Typical outputs
- release note draft
- changelog entry draft
- documentation update summary

### Handoff to next step
This step leaves a release-facing record, but not a focused implementation review.

---

## Step 2: `review-diff`

### Goal
Produce a structured internal review record of what actually changed.

### Typical outputs
- diff review summary
- touch point list
- scope comparison notes
- follow-up items

### Gate
- `diff-review-gate.md`

### End state
At the end of this step, the repository should have a concise implementation review that can support later retrospective work.

---

## Artifact flow

The expected artifact chain is:

1. `release-note-template.md`
2. `changelog-entry-template.md`
3. `diff-review-template.md`

These outputs should move from release-facing wording toward implementation-facing review.

---

## Example reference

A concrete example of this flow exists at:

- `examples/issue-driven/filter-persistence/08-diff-review.md`

That file shows how a shipped change becomes:

- a concise implementation summary
- an explicit scope comparison
- a short follow-up list
