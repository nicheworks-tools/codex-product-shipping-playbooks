# Flow Example: plan-change

## Scenario

The specification delta has been defined for a settings-page persistence issue.

Now the team needs to convert that definition into an implementation-oriented plan.

---

## Why this playbook is used here

At this point, the workflow already knows:

- what is changing
- what is not changing
- which repository areas are likely involved

The next step is to turn that into a realistic implementation sequence.

This is the role of `plan-change`.

---

## Example inputs

- spec delta draft
- impacted surfaces
- repository constraints
- key file list from intake
- assumptions recorded during spec work

---

## Example work performed

The playbook is used to define:

- likely touch points:
  settings UI component, shared state store, route transition handling
- implementation shape:
  move the selected-value state into a layer that survives route transitions
- sequencing:
  1. confirm current reset path
  2. update state ownership
  3. adjust UI binding
  4. verify route behavior
  5. review docs impact
- documentation impact:
  update any behavior notes if the settings page behavior is described anywhere

---

## Example outputs

- change plan
- touch point list
- implementation steps
- docs impact notes
- risks and tradeoffs

Example summary:

1. inspect route transition path for state reset
2. refactor selected-value ownership to session-level shared state
3. update settings UI to read from the new state source
4. verify route transitions preserve values
5. confirm whether any user-facing notes need revision

Known risk:
- changing state ownership may affect another settings-related flow

---

## What this enables next

This output gives `define-acceptance` a concrete basis for deciding what must be true before the change can be considered complete.
