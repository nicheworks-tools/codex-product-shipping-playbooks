# Flow Example: spec-delta

## Scenario

The repository intake step identified the likely files and state flow for a settings page issue.

Now the team needs to define exactly what is changing.

---

## Why this playbook is used here

The original issue only says that selected values are lost after navigation.

That is not yet a good change definition.

The workflow now needs to answer:

- what the current behavior is
- what the intended behavior is
- what is included in this change
- what is not included
- what parts of the repository are likely affected

This is the role of `spec-delta`.

---

## Example inputs

- repository context memo
- key file list
- issue text
- notes about current state handling
- known unknowns from intake

---

## Example work performed

The playbook is used to define:

- current state:
  selected values reset when the user navigates away and back
- intended state:
  selected values should remain during normal in-app navigation
- in scope:
  preserving selected values across route changes inside the app
- out of scope:
  preserving values across full browser reload or logout
- impacted surfaces:
  settings UI, shared state store, route transition logic

---

## Example outputs

- spec delta draft
- in-scope / out-of-scope section
- impacted surfaces
- assumptions and open questions

Example summary:

- Current behavior resets selected values during route transitions
- Intended behavior preserves the values during in-app navigation
- Full reload persistence is not part of this change
- Likely impacted areas include settings UI state binding and route-level reset logic
- Assumption: preserving values only within a session is acceptable

---

## Gate used

- `spec-delta-gate.md`

---

## What this enables next

This output gives `plan-change` a concrete change definition so that implementation planning can be based on scope and repository reality rather than guesses.
