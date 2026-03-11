# Flow Example: define-acceptance

## Scenario

A concrete change plan now exists for preserving selected settings values across route navigation.

The next step is to define what counts as acceptable completion.

---

## Why this playbook is used here

Implementation planning is not enough to determine whether the work is done.

The workflow now needs to clarify:

- what must be true when the change is finished
- what edge cases matter
- what must be checked manually
- what failure would still count as unacceptable

This is the role of `define-acceptance`.

---

## Example inputs

- spec delta draft
- change plan
- repository context notes
- known risks

---

## Example work performed

The playbook is used to define:

- expected outcome:
  selected values remain intact when navigating away and back during the same in-app session
- acceptance criteria:
  values do not reset on normal route changes
- edge cases:
  browser reload is out of scope, but rapid back-and-forth navigation should still behave correctly
- manual verification:
  choose values, navigate away, return, confirm the same values remain
- failure conditions:
  values reset under normal route transitions, or unrelated settings behavior breaks

---

## Example outputs

- acceptance definition
- edge-case notes
- manual verification notes
- done checklist

Example checklist:

- [ ] Selected values persist across in-app route navigation
- [ ] No obvious regression appears in the settings page
- [ ] Edge-case behavior was reviewed
- [ ] Manual verification was completed

---

## Gate used

- `acceptance-gate.md`

---

## What this enables next

This output gives `ship-check` a concrete standard for deciding whether the work is actually ready to move toward shipping.
