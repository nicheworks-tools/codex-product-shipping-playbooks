# spec-delta

## Purpose

Define the difference between the current repository behavior and the intended change.

This playbook exists to separate change definition from implementation planning.

---

## When to use this playbook

Use this playbook when:

- repository intake is complete enough to describe the current state
- a request, issue, or problem statement needs sharper definition
- the team needs explicit scope before planning implementation
- assumptions and unknowns need to be surfaced

---

## When not to use this playbook

Do not use this playbook when:

- repository intake has not been done at all
- the change has already been defined clearly and recently
- the task is only to review a finished implementation
- the work is purely release-facing and no new change definition is needed

---

## Required inputs

Typical inputs include:

- repository context memo
- key file list
- issue or request text
- notes about current behavior
- known constraints
- missing context notes

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/spec-delta-template.md`

Typical outputs include:

- current state
- intended state
- explicit delta
- in-scope / out-of-scope
- impacted surfaces
- assumptions
- risks
- open questions

---

## Gates to pass

This playbook should pass:

- `spec-delta-gate.md`

Do not move into planning if the requested change is still mostly implied rather than defined.

---

## Procedure

1. Describe the current state relevant to the request.
2. Describe the intended state.
3. Write the specific delta between the two.
4. Clarify what is in scope and what is out of scope.
5. Identify likely impacted surfaces.
6. Record assumptions, open questions, and risks.
7. Produce a spec delta draft that the next playbook can use for planning.

---

## Notes and cautions

- Do not let the implementation approach replace the change definition.
- Do not hide uncertainty. Write it down.
- Do not leave scope boundaries unstated.
- A good spec delta makes planning easier because the actual change is visible.

---

## Next playbook

- `plan-change`

This playbook turns the defined delta into an implementation-oriented plan.

---

## Example

A request says: “Make the settings page faster.”

A weak output would jump straight to caching or refactoring ideas.

A good `spec-delta` output would first define:
- what “faster” means in this context
- what current behavior is unsatisfactory
- what surfaces are likely involved
- what is not included in this change
