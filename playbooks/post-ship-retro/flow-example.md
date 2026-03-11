# Flow Example: post-ship-retro

## Scenario

A filter persistence bug fix has already been shipped, documented, and reviewed internally.

Now the team wants to capture what it learned from the full path from issue to shipped change.

---

## Why this playbook is used here

By this point, the workflow already has:

- a release-facing record
- an internal diff review
- follow-up observations

The remaining task is to turn those observations into useful learning rather than letting them disappear.

This is the role of `post-ship-retro`.

---

## Example inputs

- diff review
- changelog entry
- release note draft
- pre-ship review
- follow-up items

---

## Example work performed

The playbook is used to produce:

- a short retro summary
- notes about what worked in the workflow
- notes about where ambiguity or delay still appeared
- concrete improvement actions for the next similar change

---

## Example outputs

- retro summary
- lessons learned
- improvement actions

Example summary:

- The issue-to-ship flow helped clarify scope early
- Acceptance criteria reduced ambiguity before shipping
- Secondary return paths should have been checked earlier
- A future similar change should define navigation-path coverage sooner

---

## Gate used

- `gates/retro-gate.md`

---

## What this enables next

This output gives the repository a reusable learning record that can improve later planning, acceptance, and review quality.
