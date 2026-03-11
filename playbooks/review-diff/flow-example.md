# Flow Example: review-diff

## Scenario

A filter persistence bug fix has already been implemented and documented for release.

Now the team wants a concise internal review record of what the implementation actually changed.

---

## Why this playbook is used here

Release-facing materials explain the change at a user or release-history level.

That is not the same as a structured implementation review.

The workflow now needs to capture:

- what actually changed in the implementation
- what was more or less than expected
- what follow-up work may still exist
- what later retrospective work should know

This is the role of `review-diff`.

---

## Example inputs

- diff or patch
- spec delta
- change plan
- pre-ship review
- release note draft

---

## Example work performed

The playbook is used to produce:

- a concise implementation summary
- notes about touched state handling and navigation logic
- confirmation that the main intended scope was delivered
- follow-up items for additional navigation-path checks

---

## Example outputs

- diff review summary
- review notes
- follow-up items

Example summary:

- The implementation moved filter persistence to a longer-lived state layer
- The listing page now restores selected filters during the covered return flow
- The delivered scope matches the intended primary navigation path
- Additional verification may still be useful for secondary return paths

---

## Gate used

- `gates/diff-review-gate.md`

---

## What this enables next

This output gives later retrospective work a cleaner record of the implementation than release-facing notes alone.
