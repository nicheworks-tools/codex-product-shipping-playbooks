# Flow Example: ship-check

## Scenario

The settings-page persistence change has been implemented and reviewed informally.

Now the team needs a structured pre-ship decision.

---

## Why this playbook is used here

At this point, the workflow needs to answer:

- has acceptance actually been met?
- are blockers still open?
- are there known risks?
- do docs or release-facing notes need attention?
- is the correct recommendation “ready to ship” or not?

This is the role of `ship-check`.

---

## Example inputs

- acceptance definition
- current implementation status
- known blockers
- known risks
- docs impact notes

---

## Example work performed

The playbook is used to review:

- whether manual verification was completed
- whether the route-navigation case behaves correctly
- whether any blocker remains unresolved
- whether changing state ownership introduced side effects
- whether the behavior change needs documentation or release-note mention

---

## Example outputs

- pre-ship review
- blockers and risks list
- readiness recommendation
- follow-up items

Example conclusion:

- Acceptance was reviewed and mostly satisfied
- No release-blocking issue remains
- One moderate risk exists around another settings-related path
- No major user-facing docs change is required
- Final recommendation: **Ready with caution**

---

## Gate used

- `pre-ship-gate.md`

---

## What this enables next

In the MVP stage, this may be the final structured decision point.

In the expanded version of the repository, this output may feed into:
- `write-release-artifacts`
- `review-diff`
- `post-ship-retro`
