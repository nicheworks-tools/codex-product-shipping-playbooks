# intake-repo

## Purpose

Understand the repository well enough to describe a requested change in repository terms rather than in vague product language.

This playbook is the entry point for repository-aware workflow.

---

## When to use this playbook

Use this playbook when:

- work starts from an existing repository
- a change request, issue, or idea needs repository context
- the likely touch points are not fully known yet
- the team needs a shared understanding of the current structure before planning change

---

## When not to use this playbook

Do not use this playbook when:

- the repository context is already well documented and recently reviewed
- the task is purely about release notes after implementation
- the task begins from a finished diff that only needs review
- there is no repository yet

---

## Required inputs

Typical inputs include:

- repository tree
- key files or likely entry points
- current docs
- issue or request text
- known constraints
- known uncertainty

---

## Artifacts created or updated

This playbook usually produces or supports:

- repository context memo
- key file list
- constraints list
- missing context notes

During the MVP stage, these may exist as structured notes rather than formal templates.

---

## Gates to pass

This playbook should pass:

- `repo-intake-gate.md`

Do not move forward until the team has enough repository understanding to describe the requested change realistically.

---

## Procedure

1. Review the repository structure at a practical level.
2. Identify likely entry points, touch points, and related areas.
3. Note repository conventions, constraints, or obvious patterns.
4. Record what is still unclear.
5. Summarize the repository context in a form that the next playbook can use.

---

## Notes and cautions

- Do not confuse a quick skim with real intake.
- Do not jump into implementation planning too early.
- If important unknowns remain, name them explicitly.
- The purpose is not full repository mastery. The purpose is enough context for reliable next-step work.

---

## Next playbook

- `spec-delta`

This playbook feeds repository context into the definition of what is actually changing.

---

## Example

A repository has a bug report about a settings screen behaving incorrectly.

Use `intake-repo` to identify:
- where the settings UI lives
- what state or API layers are involved
- what docs or tests may matter
- what repository conventions may affect the change

That output becomes the starting point for `spec-delta`.
