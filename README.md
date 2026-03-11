# Codex Product Shipping Playbooks

A repository-first workflow kit for turning change requests into concrete shipping work.

This project is designed to help repository-based Codex workflows move more reliably through:

- repository intake
- spec delta definition
- implementation planning
- acceptance definition
- pre-ship review
- release-facing communication
- implementation review
- post-ship retrospective

It is **not** a generic PM toolkit.
It is **not** a clone of a skills repository.
Its native structure is built around playbooks, artifacts, gates, flows, and adapters.

---

## What this repository is for

This repository exists to make shipping-oriented workflow steps easier to repeat inside a real codebase.

It is for cases where you already have a repository and want better support for work such as:

- understanding the repository before proposing a change
- defining the delta between current behavior and intended behavior
- turning requested changes into implementation plans
- defining what counts as done
- checking whether something is actually ready to ship
- producing release-facing notes after shipping decisions are made
- reviewing the implementation that was actually delivered
- capturing useful post-ship learning

The goal is to support **real repository work**, not just planning language.

---

## Core model

The native structure of this repository is:

- **playbooks** for concrete workflow steps
- **artifacts** for reusable output templates
- **gates** for review and completion checkpoints
- **flows** for multi-step workflow chains
- **adapters** for optional export or compatibility support

If compatibility with another format is needed later, it should be handled through adapters.
The native structure should remain primary.

---

## Current workflow path

The repository currently supports this end-to-end path:

1. `intake-repo`
2. `spec-delta`
3. `plan-change`
4. `define-acceptance`
5. `ship-check`
6. `write-release-artifacts`
7. `review-diff`
8. `post-ship-retro`

This means the system now covers work from repository understanding through post-ship learning.

---

## Why use this with Codex

The value of this project is not abstract PM theory.

The value is that it helps structure repository work around practical questions such as:

- What is changing in this repository?
- What files, routes, or state surfaces are likely involved?
- What should the implementation plan look like before coding starts?
- What counts as done for this change?
- What must be checked before shipping?
- What should be written in release-facing communication?
- What did the implementation actually deliver?
- What should improve next time?

In other words, this repository is meant to help Codex work more effectively **inside a real repo**, not just generate nice planning prose.

---

## Start here

If you are new to the repository, use this order:

1. `AGENTS.md`
2. `spec/`
3. `examples/issue-driven/filter-persistence/`
4. `playbooks/`
5. `artifacts/`, `gates/`, and `flows/`

This gives you the rules, the source-of-truth intent, one full example, and then the reusable workflow system.

---

## Example proof

The main end-to-end example lives here:

- `examples/issue-driven/filter-persistence/`

It currently covers:

1. issue report
2. repository intake
3. spec delta
4. change plan
5. acceptance definition
6. pre-ship review
7. release note
8. changelog entry
9. diff review
10. retro

This is the first full proof that the repository’s workflow can run end to end.

---

## Useful entry points

- `spec/`
  Source-of-truth project specification

- `docs/vision.md`
  Why the project exists

- `docs/architecture.md`
  How the repository is structured

- `docs/workflows.md`
  How the layers connect

- `examples/issue-driven/filter-persistence/`
  Full synthetic end-to-end example

- `scripts/validate_structure.py`
  Structure validation

- `scripts/check_required_files.py`
  Required file validation

- `scripts/lint_markdown.py`
  Markdown hygiene check

---

## Repository structure

```text
codex-product-shipping-playbooks/
├─ AGENTS.md
├─ README.md
├─ DISCLAIMER.md
├─ .github/
├─ spec/
├─ docs/
├─ playbooks/
├─ artifacts/
├─ gates/
├─ flows/
├─ examples/
├─ scripts/
├─ adapters/
└─ archive/
```

---

## Publisher

Published by **NicheWorks**.

Website:

* `https://nicheworks.app/`

---

## Support

If this project is useful, you can support NicheWorks here:

* Ko-fi: `https://ko-fi.com/nicheworks`
* OFUSE: `https://ofuse.me/nicheworks`

GitHub funding metadata is also included through `.github/FUNDING.yml`.

---

## Disclaimer

This repository is provided as a workflow resource.

Examples may be synthetic, and nothing here should be treated as a guarantee of correctness, completeness, shipping quality, legal compliance, or release approval.

For the full disclaimer, see:

* `DISCLAIMER.md`

Users remain responsible for implementation, testing, security review, compliance review, documentation accuracy, and release decisions.

---

## What this repository is not

This project is not intended to become:

* a generic PM framework library
* a prompt dump
* a clone of a public skills repository
* a loose collection of templates with no workflow logic

It only makes sense if it stays focused on repository-aware shipping work.

---

## Current status

The repository has passed:

* foundation setup
* core-flow MVP
* practical tightening
* shipping expansion
* end-to-end example extension

The immediate goal now is public-release preparation.

---

## License

MIT
