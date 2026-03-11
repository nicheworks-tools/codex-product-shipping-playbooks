# plan-change

## Purpose

Turn a defined specification delta into a practical implementation plan.

This playbook exists to connect change definition to concrete repository work.

---

## When to use this playbook

Use this playbook when:

* the requested change has already been defined clearly enough
* scope boundaries exist
* likely impacted surfaces are known
* the team needs a structured path from change definition to execution

---

## When not to use this playbook

Do not use this playbook when:

* the change is still vague
* repository intake is incomplete
* the task is only to define acceptance or review shipping readiness
* the task is post-implementation diff review

---

## Required inputs

Typical inputs include:

* spec delta draft
* impacted surfaces
* assumptions
* repository constraints
* issue or request context
* notes from repository intake

---

## Artifacts created or updated

This playbook should usually create or update:

* `artifacts/change-plan-template.md`

Typical outputs include:

* overall implementation shape
* likely touch points
* step-by-step work sequence
* docs impact notes
* testing implications
* risks and tradeoffs
* unresolved questions

---

## Review checkpoint

This playbook does not yet have a dedicated repository-wide gate.

Even so, do not treat the output as complete until these questions can be answered clearly:

* Is the implementation shape plausible for this repository?
* Are likely touch points concrete enough to review?
* Is the order of work practical?
* Were docs and testing implications considered?
* Are the main risks and unknowns visible?

If the answer to several of these is no, revise the plan before moving to `define-acceptance`.

---

## Procedure

1. Review the spec delta and repository context together.
2. Identify likely files, components, routes, services, or data structures involved.
3. Decide on an implementation shape that fits the repository.
4. Break the change into concrete ordered steps.
5. Note documentation impact.
6. Note testing implications.
7. Write down risks, tradeoffs, and unresolved questions.
8. Review the plan against the checkpoint above.
9. Produce a change plan that can support acceptance work.

---

## Notes and cautions

* Do not invent a plan for a change that has not been defined well enough.
* Do not pretend all touch points are certain if they are not.
* Do not ignore docs and verification just because coding is the visible part.
* The plan should make the work easier to review, not just longer.

---

## Next playbook

* `define-acceptance`

This playbook provides the implementation shape that acceptance should be measured against.

---

## Example

A spec delta says a filter component must preserve selected values across navigation.

A good `plan-change` output would identify:

* likely state ownership
* relevant UI touch points
* possible route or storage interactions
* docs and testing impact
* a realistic step sequence for the change
