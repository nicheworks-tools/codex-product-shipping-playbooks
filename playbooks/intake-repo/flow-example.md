# Flow Example: intake-repo

## Scenario

A repository has an issue that says:

> The settings page sometimes loses selected values after navigation.

The issue describes a symptom, but it does not identify where the problem lives in the repository.

---

## Why this playbook is used here

Before defining the change, the team needs a basic repository-aware understanding of:

- where the settings page lives
- what state management is involved
- whether routing affects the problem
- what documentation or tests may already exist
- what is still unknown

This is the role of `intake-repo`.

---

## Example inputs

- repository tree
- issue text
- likely UI entry points
- any existing docs for settings behavior

---

## Example work performed

The playbook is used to identify:

- the settings UI component directory
- the route handling the settings page
- the state layer that stores selected values
- any persistence or caching layer that may affect navigation behavior
- missing context, such as whether the problem occurs only under certain routes

---

## Example outputs

- repository context memo
- key file list
- constraints list
- missing context notes

Example summary:

- Settings UI lives under `app/settings/...`
- Selection state appears to be managed in a shared store
- Navigation behavior may involve route-level reset logic
- No clear test coverage for value persistence was found
- It is still unclear whether persistence is expected across full reloads or only route changes

---

## Gate used

- `repo-intake-gate.md`

---

## What this enables next

This output gives `spec-delta` enough context to define the requested change in repository terms instead of guessing from issue wording alone.
