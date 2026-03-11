# define-acceptance

## Purpose

Define what must be true before a change can be considered complete and acceptable.

This playbook exists to prevent “implemented” from being treated as automatically equal to “done.”

---

## When to use this playbook

Use this playbook when:

- the change has been defined
- the implementation plan exists in some usable form
- the team needs explicit completion criteria
- edge cases and manual verification need to be clarified before shipping review

---

## When not to use this playbook

Do not use this playbook when:

- the change itself is still vague
- no implementation shape has been proposed yet
- the task is only release-note writing or post-change review
- the team already has a strong acceptance definition that remains current

---

## Required inputs

Typical inputs include:

- spec delta draft
- change plan
- repository context notes
- known risks
- issue or request context

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/acceptance-template.md`

Typical outputs include:

- expected outcome
- acceptance criteria
- edge cases
- manual verification checks
- failure conditions
- done checklist
- notes for ship review

---

## Gates to pass

This playbook should pass:

- `acceptance-gate.md`

Do not move to ship review until the team can explain what “done” means in clear terms.

---

## Procedure

1. Review the spec delta and implementation plan together.
2. Define the expected outcome in concrete terms.
3. Write explicit acceptance criteria.
4. Identify edge cases that should not be ignored.
5. Define manual verification expectations.
6. Write down failure conditions and non-goals where useful.
7. Produce a done checklist that can support ship review.

---

## Notes and cautions

- Do not let acceptance become a vague feeling.
- Do not skip manual verification where it matters.
- Do not confuse “we wrote the code” with “the work is acceptable.”
- Good acceptance work reduces ambiguity during shipping review.

---

## Next playbook

- `ship-check`

This playbook provides the completion criteria that ship review should use when deciding readiness.

---

## Example

A planned UI change adds a new warning state.

A good `define-acceptance` output would clarify:
- when the warning should appear
- when it should not appear
- what must be verified manually
- what failure cases would make the change unacceptable
