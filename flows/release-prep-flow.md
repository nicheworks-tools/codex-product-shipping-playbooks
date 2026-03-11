# Release Prep Flow

## Purpose of this flow

This flow describes how work moves from shipping readiness into release-facing communication.

It begins after `ship-check` and focuses on what should be written down for users, maintainers, or release history.

---

## When to use this flow

Use this flow when:

- a change has already passed pre-ship review
- release-facing communication needs to be prepared
- the team wants a structured way to produce changelog and release-note material

Do not use this flow when:

- the change is still blocked
- the work has not passed through `ship-check`
- the task is purely retrospective

---

## Flow sequence

1. `ship-check`
2. `write-release-artifacts`

This is the first release-facing extension of the MVP workflow.

---

## Step 1: `ship-check`

### Goal
Confirm that the change is ready to move toward shipping.

### Typical outputs
- pre-ship review
- blockers and risks list
- readiness recommendation

### Handoff to next step
This step gives `write-release-artifacts` the decision basis for release-facing communication.

---

## Step 2: `write-release-artifacts`

### Goal
Produce the release-facing record of the change.

### Typical outputs
- release note draft
- changelog entry draft
- documentation update summary

### Gate
- `release-artifacts-gate.md`

### End state
At the end of this step, the change should have the release-facing materials appropriate to its scope and audience.

---

## Artifact flow

The expected artifact chain is:

1. `pre-ship-review-template.md`
2. `release-note-template.md`
3. `changelog-entry-template.md`

These outputs should reflect the actual scope of the completed change rather than marketing language.

---

## Example reference

A concrete example of this flow exists inside:

- `examples/issue-driven/filter-persistence/06-release-note.md`
- `examples/issue-driven/filter-persistence/07-changelog-entry.md`

These files show how a completed pre-ship result becomes:

- a scoped release note
- a concise changelog entry
