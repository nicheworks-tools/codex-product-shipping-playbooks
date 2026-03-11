# post-ship-retro

## Purpose

Capture what was learned after shipping and turn that learning into explicit follow-up improvement.

This playbook exists to connect shipped work to future process, product, and implementation improvement.

---

## When to use this playbook

Use this playbook when:

- a change has already shipped
- review notes or follow-up items already exist
- the team wants to record what went well, what did not, and what should improve next time
- the work is important enough to justify structured reflection

---

## When not to use this playbook

Do not use this playbook when:

- the change has not yet shipped
- implementation review has not been captured
- the task is still pre-ship
- the work is too small to justify a formal retrospective

---

## Required inputs

Typical inputs include:

- diff review
- release note or changelog context
- pre-ship review
- acceptance definition
- follow-up items already identified
- any post-release observations that matter

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/retro-template.md`

Typical outputs include:

- retro summary
- what went well
- what went poorly
- what was surprising
- concrete improvement actions
- owners or next-step notes if relevant

---

## Gates to pass

This playbook should pass:

- `gates/retro-gate.md`

Do not treat retrospective work as complete until the learning is clear enough to influence future work.

---

## Procedure

1. Review the diff review and release-facing record of the shipped change.
2. Summarize the outcome of the work at a high level.
3. Capture what went well.
4. Capture what went poorly or created friction.
5. Note surprises, mismatches, or unexpected complexity.
6. Turn the learning into concrete improvement actions.
7. Review the retro against the retro gate.

---

## Notes and cautions

- Do not turn the retro into blame language.
- Do not write vague lessons with no practical consequence.
- Do not pretend every shipped change needs a long retrospective.
- Prefer a short useful retro over a long empty one.

---

## Next playbook

This is currently the last planned workflow step in the shipping expansion path.

Its outputs should inform future:
- repository intake
- planning quality
- acceptance quality
- release communication
- implementation review

---

## Example

A filter persistence fix has already been reviewed after implementation.

A good `post-ship-retro` output would produce:

- a short summary of what worked in the workflow
- a note that acceptance helped reduce ambiguity
- a note that secondary navigation paths should be tested earlier next time
- one or two concrete improvement actions for future changes
