# Adapters

## Purpose of this directory

This directory contains optional compatibility and export helpers.

The native structure of this repository is built around:

- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`

Adapters exist only to export or translate that native structure when needed.

They are **not** the core identity of the project.

---

## Core rule

The native repository structure comes first.

If an adapter is added later, it must work **from** the native structure.
The repository must not be redesigned just to mimic an outside format.

---

## What belongs here

Examples of things that may belong in this directory:

- export tools for Codex-oriented formats
- mapping notes between native playbooks and external formats
- compatibility helpers for generated output
- documentation explaining the limits of a given export path

---

## What does not belong here

This directory should not contain:

- the main playbook definitions
- primary templates
- core review gates
- the main workflow logic
- any restructuring of the repository around external conventions

If something is central to how this repository works, it belongs outside `adapters/`.

---

## Current status

At the foundation stage, this directory exists as a placeholder.

It signals that compatibility may be added later, while making clear that compatibility is secondary to the native model.

---

## Future direction

A likely first adapter is:

- `export_codex_skill_format.py`

If that is added later, it should:

- read from the native repository structure
- generate an export format without changing the source structure
- remain clearly documented as an adapter, not as the main system

---

## Rule for future contributors

Before adding an adapter, ask:

1. Does this solve a real compatibility problem?
2. Can it be implemented without reshaping the native structure?
3. Is the adapter clearly secondary to the repository’s core model?

If the answer to any of these is no, do not add the adapter yet.
