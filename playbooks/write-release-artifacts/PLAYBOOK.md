# write-release-artifacts

## Purpose

Produce the release-facing materials that should exist after a change is considered ready to ship.

This playbook exists to connect shipping readiness to clear outward-facing communication.

---

## When to use this playbook

Use this playbook when:

- `ship-check` has produced a clear readiness recommendation
- the change is ready to move toward release-facing communication
- the team needs release notes, changelog entries, or documentation updates
- the work should leave behind a clear public or internal summary

---

## When not to use this playbook

Do not use this playbook when:

- the change is still blocked
- acceptance is not yet clear
- `ship-check` has not been done
- the task is only about planning future implementation
- the task is a post-release retrospective

---

## Required inputs

Typical inputs include:

- pre-ship review
- acceptance definition
- spec delta
- change plan
- notes about documentation impact
- any release or communication constraints

---

## Artifacts created or updated

This playbook should usually create or update:

- `artifacts/release-note-template.md`
- `artifacts/changelog-entry-template.md`

Typical outputs include:

- release note draft
- changelog entry draft
- documentation update summary
- short user-facing explanation of the change

---

## Gates to pass

This playbook should pass:

- `gates/release-artifacts-gate.md`

Do not treat release-facing communication as complete until the essential outputs are present and understandable.

---

## Procedure

1. Review the pre-ship recommendation and confirm the change is ready for release-facing work.
2. Review the acceptance definition and spec delta to understand what should be communicated.
3. Draft a concise changelog entry.
4. Draft a release note at the level of detail appropriate for the audience.
5. Capture any documentation updates that should accompany the change.
6. Make sure the wording matches the actual scope of the change.
7. Review the outputs against the release artifacts gate.

---

## Notes and cautions

- Do not overstate what changed.
- Do not silently expand scope in release-facing language.
- Do not describe speculative improvements as completed work.
- If the change is narrow, the release note should stay narrow.
- If the change is mostly internal, the changelog may matter more than a long release note.

---

## Next playbook

A later workflow may continue into:

- `review-diff`
- `post-ship-retro`

This playbook is the bridge between shipping readiness and release-facing communication.

---

## Example

A filter persistence bug fix has passed `ship-check`.

A good `write-release-artifacts` output would produce:

- a short changelog entry describing preserved filters during return navigation
- a release note draft explaining the user-visible behavior change
- a note about whether any docs or help text need updating
