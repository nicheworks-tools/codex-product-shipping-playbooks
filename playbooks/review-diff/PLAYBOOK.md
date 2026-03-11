# review-diff

## Purpose

Review a completed diff or change set and turn it into a clear record of what changed, what matters, and what should happen next.

This playbook exists to connect completed implementation work to structured review and follow-up.

---

## When to use this playbook

Use this playbook when:

- implementation work already exists in diff, PR, or patch form
- the team needs a concise summary of what changed
- review notes or follow-up items should be captured explicitly
- later retrospective work will benefit from a clean review record

---

## When not to use this playbook

Do not use this playbook when:

- the change has not yet been implemented
- the task is still in planning or acceptance definition
- the work is only about release-note writing
- the task is a broad retrospective across many unrelated changes

---

## Required inputs

Typical inputs include:

- diff, PR, or patch summary
- spec delta
- change plan
- acceptance definition
- pre-ship review
- release-facing notes if they already exist

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/diff-review-template.md`

Typical outputs include:

- concise change summary
- notable implementation observations
- review notes
- follow-up items
- scope confirmation or mismatch notes

---

## Gates to pass

This playbook should pass:

- `gates/diff-review-gate.md`

Do not treat review output as complete until the actual change is summarized clearly and any important follow-up is visible.

---

## Procedure

1. Review the diff or patch at a practical level.
2. Compare the implemented change against the spec delta and change plan.
3. Summarize what actually changed.
4. Note anything surprising, incomplete, or especially important.
5. Record follow-up items if the implementation creates future work.
6. Confirm whether the delivered scope matches the intended scope.
7. Review the output against the diff review gate.

---

## Notes and cautions

- Do not restate the entire diff line by line.
- Do not confuse release-facing language with implementation review language.
- Do not hide mismatches between intended and delivered scope.
- Keep the output useful for later retrospective work.

---

## Next playbook

A later workflow may continue into:

- `post-ship-retro`

This playbook creates the review record that retrospective work can build on.

---

## Example

A filter persistence fix has already shipped.

A good `review-diff` output would produce:

- a concise summary of where state handling changed
- notes about the actual touch points
- any mismatch between planned and delivered scope
- follow-up items for less common navigation paths
