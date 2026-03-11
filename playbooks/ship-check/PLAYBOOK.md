# ship-check

## Purpose

Review whether a change is actually ready to move toward shipping.

This playbook exists to turn readiness into an explicit review step instead of a vague judgment.

---

## When to use this playbook

Use this playbook when:

- acceptance has been defined
- implementation work is close enough to review for shipping readiness
- blockers, risks, docs impact, and release concerns need a structured checkpoint
- the team needs a final recommendation before proceeding

---

## When not to use this playbook

Do not use this playbook when:

- the work is still too early and basic acceptance has not been defined
- repository intake and spec work were skipped
- the task is only about planning future work
- the task is a post-implementation retrospective after release

---

## Required inputs

Typical inputs include:

- acceptance definition
- current implementation status
- known blockers
- known risks
- documentation impact notes
- release-facing concerns

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/pre-ship-review-template.md`

Typical outputs include:

- readiness checks
- blockers list
- risks list
- documentation and communication review
- rollback or recovery notes
- final recommendation
- follow-up items

---

## Gates to pass

This playbook should pass:

- `pre-ship-gate.md`

This is the final MVP gate before the repository moves into release-facing work.

---

## Procedure

1. Review the current scope and make sure it is still understood.
2. Review the acceptance definition and any verification status.
3. List unresolved blockers.
4. List known risks.
5. Review documentation and release-facing impact.
6. Consider rollback or recovery concerns where relevant.
7. Produce a final recommendation:
   - ready to ship
   - ready with caution
   - not ready to ship

---

## Notes and cautions

- Do not treat this as a ceremonial last step.
- Do not skip docs and communication impact.
- Do not hide unresolved blockers under optimistic language.
- If recovery thinking matters, write it down even if the rollback plan is still simple.

---

## Next playbook

In the completed version of the repository, the next step may be:

- `write-release-artifacts`

In the MVP stage, this playbook may be the last formal step in the workflow.

---

## Example

A feature is implemented and appears to work locally.

A weak `ship-check` outcome would say “looks good.”

A strong `ship-check` outcome would state:
- whether acceptance has actually been met
- whether blockers remain
- whether docs need updates
- what release risk is known
- whether the final recommendation is truly “ready to ship”
