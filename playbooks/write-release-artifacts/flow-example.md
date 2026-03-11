# Flow Example: write-release-artifacts

## Scenario

A filter persistence bug fix has passed pre-ship review with the recommendation:

**Ready with caution**

The next step is to prepare the release-facing materials that should accompany the change.

---

## Why this playbook is used here

The workflow already determined that the change is ready to move toward shipping.

Now the team needs to decide:

- what should appear in the changelog
- whether a release note is warranted
- whether any documentation update should be recorded
- how to describe the change without overstating it

This is the role of `write-release-artifacts`.

---

## Example inputs

- pre-ship review
- acceptance definition
- spec delta
- notes about docs impact

---

## Example work performed

The playbook is used to produce:

- a changelog entry describing the bug fix
- a release note draft explaining the user-visible improvement
- a short note that no major README update is needed
- language that keeps the scope narrow to the covered return flow

---

## Example outputs

- release note draft
- changelog entry draft
- documentation update summary

Example summary:

- Changelog: fixed a bug where selected filters could be lost after returning to the listing page during normal in-app navigation
- Release note: users returning from item detail pages should now see their active filters preserved more reliably
- Docs update: no major public documentation update required

---

## Gate used

- `gates/release-artifacts-gate.md`

---

## What this enables next

This output gives later workflows a clean release-facing record of the shipped change and creates a clearer handoff into later review and retrospective work.
