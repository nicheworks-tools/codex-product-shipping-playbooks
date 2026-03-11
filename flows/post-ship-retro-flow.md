# Post-Ship Retro Flow

## Purpose of this flow

This flow describes how work moves from implementation review into structured learning after shipping.

It exists to make sure important lessons are captured and turned into useful follow-up improvements.

---

## When to use this flow

Use this flow when:

- the change has already shipped
- implementation review already exists
- the work is significant enough to justify structured reflection

Do not use this flow when:

- the change has not shipped yet
- implementation review has not been captured
- the work is too small to benefit from formal retrospective work

---

## Flow sequence

1. `review-diff`
2. `post-ship-retro`

This is the final extension of the current shipping workflow path.

---

## Step 1: `review-diff`

### Goal
Produce a structured internal review record of what actually changed.

### Typical outputs
- diff review summary
- touch point list
- scope comparison notes
- follow-up items

### Handoff to next step
This step provides the implementation record that retrospective work can build on.

---

## Step 2: `post-ship-retro`

### Goal
Capture what was learned and turn it into explicit improvement actions.

### Typical outputs
- retro summary
- what went well
- what went poorly
- improvement actions

### Gate
- `retro-gate.md`

### End state
At the end of this step, the repository should have a reusable learning record for future similar work.

---

## Artifact flow

The expected artifact chain is:

1. `diff-review-template.md`
2. `retro-template.md`

These outputs should move from implementation review into reusable process learning.

---

## Example reference

A concrete example of this flow exists at:

- `examples/issue-driven/filter-persistence/09-retro.md`

That file shows how a shipped change becomes:

- a short learning summary
- a record of workflow strengths and weaknesses
- a small set of concrete improvement actions
