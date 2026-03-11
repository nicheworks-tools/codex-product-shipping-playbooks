# Issue to Ship

## Purpose of this flow

This flow describes the standard path from a reported issue or requested change to a pre-ship decision.

It is the main workflow for the MVP stage of this repository.

---

## When to use this flow

Use this flow when:

- a repository already exists
- a change request, bug report, or issue is available
- the work needs to move from clarification into shipping preparation
- the team wants a structured path instead of ad hoc discussion

Do not use this flow for:
- pure idea exploration with no repository
- general market or product strategy work
- release-only work after implementation is already complete

---

## Flow sequence

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`

---

## Step 1: `intake-repo`

### Goal
Understand enough of the repository to describe the requested change in repository terms.

### Typical inputs
- issue or request
- repository tree
- key files
- existing docs
- known constraints

### Typical outputs
- repository context memo
- key file list
- constraints list
- missing context notes

### Gate
- `repo-intake-gate.md`

### Handoff to next step
This step gives `spec-delta` the repository context needed to define the requested change realistically.

---

## Step 2: `spec-delta`

### Goal
Define the actual difference between the current state and the intended state.

### Typical inputs
- repository context memo
- issue or request
- known constraints
- current behavior notes

### Typical outputs
- spec delta draft
- in-scope / out-of-scope section
- impacted surfaces
- assumptions
- risks and open questions

### Gate
- `spec-delta-gate.md`

### Handoff to next step
This step gives `plan-change` a concrete definition of what should change and what should not.

---

## Step 3: `plan-change`

### Goal
Turn the spec delta into a practical implementation plan.

### Typical inputs
- spec delta draft
- impacted surfaces
- assumptions
- repository constraints

### Typical outputs
- change plan
- touch point list
- implementation steps
- docs impact notes
- risks and tradeoffs

### Gate
Use the playbook’s own review judgment during MVP.
A dedicated planning gate may be added later if needed.

### Handoff to next step
This step gives `define-acceptance` the planned shape of the work so acceptance can be defined against something concrete.

---

## Step 4: `define-acceptance`

### Goal
Define what has to be true before the change can be considered complete.

### Typical inputs
- spec delta draft
- change plan
- known risks
- issue context

### Typical outputs
- acceptance definition
- done checklist
- edge-case notes
- manual verification notes

### Gate
- `acceptance-gate.md`

### Handoff to next step
This step gives `ship-check` a concrete basis for deciding whether the change is actually ready.

---

## Step 5: `ship-check`

### Goal
Decide whether the change is ready to move toward shipping.

### Typical inputs
- acceptance definition
- current implementation status
- open blockers
- known risks
- docs / communication impact

### Typical outputs
- pre-ship review
- blockers and risks list
- readiness recommendation
- follow-up items

### Gate
- `pre-ship-gate.md`

### End state
At the end of this step, the work should be in one of these states:

- ready to ship
- ready with caution
- not ready to ship

---

## Artifact flow

The expected artifact chain is:

1. `spec-delta-template.md`
2. `change-plan-template.md`
3. `acceptance-template.md`
4. `pre-ship-review-template.md`

These outputs should support each other in sequence rather than being written independently.

---

## Common failure modes

### Failure mode 1: skipping repository intake
The workflow jumps into planning before understanding the codebase.

### Failure mode 2: vague change definition
The workflow moves forward without a real spec delta.

### Failure mode 3: planning without scope boundaries
Implementation steps are proposed before the actual change is clearly defined.

### Failure mode 4: acceptance as an afterthought
The team assumes “implemented” means “done.”

### Failure mode 5: ship check as a formality
The final review happens emotionally instead of structurally.

---

## Signs that the flow is working

This flow is working when:

- repository context is captured early
- the requested change becomes more precise over time
- implementation plans become easier to review
- acceptance criteria reduce ambiguity
- pre-ship review produces a clear decision

If those outcomes are not happening, the flow should be revised.

---

## Example reference

A concrete example of this flow exists at:

- `examples/issue-driven/filter-persistence/`

That example shows how one issue can move through:

1. issue report
2. repository intake
3. spec delta
4. change plan
5. acceptance definition
6. pre-ship review

It is intended to serve as the first end-to-end proof that the MVP workflow can be used in practice.
