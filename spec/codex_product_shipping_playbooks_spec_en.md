# Codex Product Shipping Playbooks Specification

## 1. Purpose of This Document

This specification defines the standards for designing, building, and publishing **Codex-ready product shipping playbooks** using a structure that is intentionally original.

This project may draw inspiration from the **idea** behind existing Claude-oriented skills repositories, but its structure, naming, responsibilities, and public-facing shape must be designed as a separate system.

This document does **not** define only the MVP. The MVP is treated as a milestone, not the destination. The real goal is a **fully developed public release** with clear value.

---

## 2. Core Direction of the Project

### 2.1 What This Project Is
This project is **not** a generic collection of PM skills.

It is a set of **playbooks and workflows** designed to help teams repeatedly handle specification work, implementation planning, shipping checks, and post-change review in the context of a real repository.

### 2.2 What This Project Aims to Enable
The system should make it possible to repeat the following flow with a consistent level of quality:

1. Understand the current repository
2. Clarify the change request
3. Define the specification delta
4. Build an implementation plan
5. Define acceptance criteria
6. Run pre-ship checks
7. Produce docs and release artifacts
8. Review the resulting diff and capture lessons learned

### 2.3 What This Project Does Not Aim to Be
The project is not intended to become any of the following:

- A generic PM framework library
- A market research template pack
- A top-of-funnel toolkit centered on GTM, OKRs, or personas
- A Claude skills clone
- A recreation of a skills catalog format

---

## 3. Differentiation Requirements

### 3.1 Why the Project Does Not Use a Skills-First Structure
A public structure centered on `skills/` and `SKILL.md` is too easily perceived as an extension of existing Claude- or Codex-style skills repositories.

For that reason, this project uses **playbooks and workflows as the primary public structure**.

### 3.2 What Counts as the Core Public Product
The core public product consists of the following layers:

- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`
- `adapters/`

If needed, the project may later provide an **adapter that exports into a Codex-compatible format**, but the native format of the project must not be a skills clone.

### 3.3 Definition of Public Value
The public value of the project must be explainable in one sentence.

**“A shipping workflow kit that helps Codex operate more effectively inside a real repository, from specification work through pre-release checks.”**

---

## 4. Target Users

### 4.1 Primary Audience
- Solo developers working with an existing repository
- Small engineering teams
- Developers who want a cleaner handoff between specification work and implementation
- Developers who want to make docs updates, changelog work, and pre-ship review less ad hoc

### 4.2 Secondary Audience
- OSS maintainers
- Developers who work from issues
- Teams whose release checks are still highly dependent on individual habits

### 4.3 Users Who Are Not the Primary Focus
- People who only have an idea and no codebase yet
- Users who mainly want general PM materials
- Users whose main goal is market research or GTM planning

---

## 5. Design Principles

### 5.1 Clean-Room Principle
- The project may borrow ideas, concerns, and design intent from existing OSS projects
- Direct reuse of wording, headings, names, or template text is prohibited
- The README, naming, structure, and responsibilities must be rewritten from scratch

### 5.2 Workflow-First Principle
- The unit of design is not a thought category but a **real workflow step inside a repository**
- Every playbook must make clear when to use it, what it produces, and what it connects to next

### 5.3 Shipping-First Principle
- Priority goes to spec work, planning, acceptance, shipping, and review
- Docs, release artifacts, rollback considerations, and monitoring must be included in scope

### 5.4 Adapter Principle
- The native system remains in its own original structure
- Compatibility with Codex can be added later through adapters
- The internal design must not be distorted just to mimic an external format

### 5.5 Local-First Principle
- The repository is designed for local Git-based management
- The system should remain portable through markdown, text files, and lightweight scripts
- Dependency on external services should stay minimal

---

## 6. Definition of the Finished Product

The completed version of the project should satisfy the following conditions.

### 6.1 Structural Requirements
- Responsibilities are clearly separated across playbooks, artifacts, gates, flows, and adapters
- Repository-wide rules are centralized in `AGENTS.md`
- The docs are sufficient for a reader to understand the whole structure

### 6.2 Functional Requirements
- The project includes 7 to 9 core playbooks
- Each playbook has the artifacts, gates, and examples it needs
- The system can support a full issue-to-ship loop in a real repository
- Release artifacts and retrospective work are included in the overall workflow

### 6.3 Quality Requirements
- Boundaries between playbooks are clear
- Artifact names and gate names are easy to understand
- The README alone communicates what the project is for
- The value of using it with Codex can be explained in one sentence

### 6.4 Public-Value Requirements
- The project must not look like a Claude-style skills clone
- It must not look like a generic PM template pack
- Its repo-aware, implementation-aware, and ship-aware value must be obvious

---

## 7. Finished-State Directory Structure

```text
codex-product-shipping-playbooks/
├─ AGENTS.md
├─ README.md
├─ LICENSE
├─ .gitignore
├─ docs/
│  ├─ vision.md
│  ├─ architecture.md
│  ├─ workflows.md
│  ├─ artifacts-model.md
│  ├─ release-model.md
│  ├─ roadmap.md
│  ├─ quality-gates.md
│  ├─ naming.md
│  └─ changelog.md
├─ playbooks/
│  ├─ intake-repo/
│  │  ├─ PLAYBOOK.md
│  │  ├─ artifacts/
│  │  ├─ gates/
│  │  ├─ scripts/
│  │  └─ flow-example.md
│  ├─ spec-delta/
│  ├─ plan-change/
│  ├─ define-acceptance/
│  ├─ ship-check/
│  ├─ write-release-artifacts/
│  ├─ review-diff/
│  └─ post-ship-retro/
├─ artifacts/
│  ├─ spec-delta-template.md
│  ├─ change-plan-template.md
│  ├─ acceptance-template.md
│  ├─ pre-ship-review-template.md
│  ├─ release-note-template.md
│  ├─ changelog-entry-template.md
│  └─ rollback-note-template.md
├─ gates/
│  ├─ repo-intake-gate.md
│  ├─ spec-delta-gate.md
│  ├─ acceptance-gate.md
│  ├─ pre-ship-gate.md
│  ├─ release-artifacts-gate.md
│  └─ retro-gate.md
├─ flows/
│  ├─ issue-to-ship.md
│  ├─ repo-change-flow.md
│  ├─ diff-to-retro.md
│  └─ release-prep-flow.md
├─ examples/
│  ├─ small-repo/
│  ├─ issue-driven/
│  └─ release-cycle/
├─ scripts/
│  ├─ validate_structure.py
│  ├─ check_required_files.py
│  ├─ lint_markdown.py
│  └─ build_index.py
├─ adapters/
│  ├─ README.md
│  └─ export_codex_skill_format.py
└─ archive/
   ├─ deprecated-playbooks/
   └─ old-artifacts/
```

---

## 8. Responsibilities of Each Top-Level Layer

### 8.1 `AGENTS.md`
The repository-wide rules layer.

#### Required Contents
- A statement that this repository is a shipping playbooks system
- A statement that the goal is not to clone a skills system
- Naming rules
- Rules for adding new playbooks
- Clear separation of playbooks, artifacts, gates, and flows
- A rule that repository context must be understood before decisions are made
- A rule that docs, tests, and release implications must always be considered
- Explicit prohibitions

### 8.2 `docs/`
The documentation layer that fixes the project’s vision, structure, naming, and quality standards.

### 8.3 `playbooks/`
The core layer that defines concrete units of work.

### 8.4 `artifacts/`
The layer that stores templates for the outputs each playbook creates or updates.

### 8.5 `gates/`
The layer that defines review and completion criteria.

### 8.6 `flows/`
The layer that explains how multiple playbooks connect into end-to-end workflows.

### 8.7 `adapters/`
The support layer for exporting the project into external formats if needed.

---

## 9. Specification for `playbooks/`

### 9.1 Core Rule
- One folder equals one clear operational responsibility
- Playbooks are divided by workflow role, not by abstract thought category
- Each playbook must make clear what comes next in the chain

### 9.2 Required Structure for Each Playbook Folder

```text
playbooks/<playbook-name>/
├─ PLAYBOOK.md
├─ artifacts/
├─ gates/
├─ scripts/
└─ flow-example.md
```

### 9.3 Required Sections in `PLAYBOOK.md`
1. Playbook name
2. Purpose
3. When to use it
4. When not to use it
5. Required inputs
6. Artifacts it creates or updates
7. Gates it must pass
8. Procedure
9. Notes and cautions
10. The next playbook in the chain
11. Example

---

## 10. Core Playbook Set

The finished version should include the following 7 core playbooks.

### 10.1 `intake-repo`
#### Purpose
Understand the repository’s structure, key files, constraints, entry points, and working conventions.

#### Main Outputs
- Repository context memo
- List of key files
- List of constraints
- Notes on missing context

### 10.2 `spec-delta`
#### Purpose
Define the difference between the current system and the requested change.

#### Main Outputs
- Specification delta draft
- In-scope / out-of-scope section
- Impacted surfaces
- Assumption list

### 10.3 `plan-change`
#### Purpose
Turn the specification delta into a workable implementation plan.

#### Main Outputs
- Change plan
- Touch points
- Implementation steps
- Docs impact notes

### 10.4 `define-acceptance`
#### Purpose
Define acceptance criteria, edge cases, and manual verification coverage.

#### Main Outputs
- Acceptance definition
- Edge-case list
- Done checklist
- Manual verification notes

### 10.5 `ship-check`
#### Purpose
Run the checks required before shipping and reduce the chance of missed items.

#### Main Outputs
- Pre-ship review
- Blockers and risks
- Release-readiness notes

### 10.6 `write-release-artifacts`
#### Purpose
Prepare release notes, changelog entries, and required documentation updates.

#### Main Outputs
- Release-note draft
- Changelog entry
- Docs update memo
- User-facing summary

### 10.7 `review-diff`
#### Purpose
Review a diff, PR, or implementation result and extract a concise summary plus follow-up needs.

#### Main Outputs
- Change summary
- Review notes
- Follow-up items

### 10.8 `post-ship-retro` (Expanded Core)
#### Purpose
Capture lessons after shipping and define improvements for the next cycle.

#### Main Outputs
- Retrospective memo
- Lessons learned
- Next improvements

This playbook is part of the finished product, but it may be deferred during the earliest foundation phase.

---

## 11. Specification for `artifacts/`

### 11.1 Role
The `artifacts/` layer stores reusable templates for the outputs produced by the playbooks.

### 11.2 Initial Artifact Set
- `spec-delta-template.md`
- `change-plan-template.md`
- `acceptance-template.md`
- `pre-ship-review-template.md`
- `release-note-template.md`
- `changelog-entry-template.md`
- `rollback-note-template.md`

### 11.3 Requirements for Artifacts
- They must be usable in real work with minimal rewriting
- They must not collapse into vague abstraction
- Their filenames must clearly communicate what they are for

---

## 12. Specification for `gates/`

### 12.1 Role
The `gates/` layer defines the criteria used to decide whether a step is truly complete.

### 12.2 Initial Gate Set
- `repo-intake-gate.md`
- `spec-delta-gate.md`
- `acceptance-gate.md`
- `pre-ship-gate.md`
- `release-artifacts-gate.md`
- `retro-gate.md`

### 12.3 Requirements for Gates
- The checks must be concrete
- They must not become overly long
- They must cover implementation, documentation, and shipping concerns

---

## 13. Specification for `flows/`

### 13.1 Role
The `flows/` layer explains how to connect multiple playbooks into complete workflows.

### 13.2 Initial Flow Set
- `issue-to-ship.md`
- `repo-change-flow.md`
- `diff-to-retro.md`
- `release-prep-flow.md`

### 13.3 Requirements for Flows
- The order of playbooks must be clear
- Input and output handoffs must be clear
- The document must show the overall workflow, not just isolated playbooks

---

## 14. Specification for `adapters/`

### 14.1 Role
The `adapters/` layer allows the native structure to be exported into other formats when needed.

### 14.2 Initial Adapter
- `export_codex_skill_format.py`

### 14.3 Adapter Policy
- Adapters are a support layer, not the core product
- The native structure must not be distorted to satisfy adapter needs
- Export support comes first; import support can be deferred

---

## 15. Naming Rules

### 15.1 Playbook Names
- Use kebab-case with names that describe an action
- Examples: `spec-delta`, `ship-check`

### 15.2 Artifact Names
- Format: `<purpose>-template.md`
- Example: `change-plan-template.md`

### 15.3 Gate Names
- Format: `<purpose>-gate.md`
- Example: `pre-ship-gate.md`

### 15.4 Flow Names
- Use either `<context>-flow.md` or `<from>-to-<to>.md`

### 15.5 Script Names
- Use snake_case as the default

---

## 16. Writing Style Requirements

### Required Style
- The writing must remain understandable even to beginners
- It must not hide behind abstract vocabulary
- Concrete terms such as repo, files, tests, docs, and release should be preferred
- The writing must lead naturally to the next action

### Prohibited Style
- Exaggerated claims such as “ultimate,” “perfect,” or “guaranteed”
- Slipping back into generic PM theory
- Reproducing the language pattern of existing skills repositories
- Creating playbooks with blurry or overlapping responsibilities

---

## 17. Quality Standards

Each playbook must satisfy the following.

1. Its role can be explained in one sentence
2. Its use cases and non-use cases are clear
3. Its inputs and outputs are concrete
4. It is tied to corresponding artifacts and gates
5. The next playbook in the chain is defined
6. It clearly contributes to repo-aware, implementation-aware, or ship-aware work
7. The reason to use it with Codex can be explained
8. There is at least one workflow example that can be tested on a real project

---

## 18. Relationship Between the MVP and the Finished Product

### 18.1 Definition of the MVP
The MVP is the smallest version that can support a full loop through these five playbooks:

- `intake-repo`
- `spec-delta`
- `plan-change`
- `define-acceptance`
- `ship-check`

The MVP is complete when the project includes the minimum artifacts, gates, and flows needed to run a real issue-to-pre-ship workflow.

### 18.2 What the Finished Product Adds
The finished product must also include:

- `write-release-artifacts`
- `review-diff`
- `post-ship-retro`
- Adapter support
- Expanded docs, flows, and examples
- Improved scripts

### 18.3 Structural Policy
This specification does not simplify the repository structure for the sake of the MVP alone. The finished-state structure is defined first, and the project is built up gradually inside that structure.

---

## 19. Initial Milestones

### Phase 1: Foundation
- Create the repository
- Create `AGENTS.md`
- Create `README.md`
- Write `docs/vision.md`
- Write `docs/architecture.md`
- Create the core `playbooks/` folders

### Phase 2: Core Flow MVP
- Write `PLAYBOOK.md` for the 5 MVP playbooks
- Create the initial artifacts, gates, and flows

### Phase 3: Practical MVP
- Test the system on real project work
- Add examples
- Adjust boundaries and remove weak or unnecessary parts

### Phase 4: Shipping Expansion
- Add `write-release-artifacts`
- Add `review-diff`
- Add `post-ship-retro`
- Expand docs, flows, and examples

### Phase 5: Public Release Candidate
- Bring the README, docs, and examples up to public-release quality
- Create the first adapter
- Formalize quality gates
- Make the final publication decision

---

## 20. Acceptance Criteria for the Finished Product

The project can be treated as complete only if it satisfies at least the following.

- The core playbook set exists
- Every playbook has a `PLAYBOOK.md`
- Required artifacts and gates exist
- The `flows/` layer is in place
- The `docs/` layer is in place
- The `README.md` alone communicates the value of the project
- There are real repository usage examples
- The structure itself makes it clear that this is not a skills clone
- The reason to use it with Codex can be explained in one sentence

---

## 21. Deferred Topics

The following topics are explicitly deferred for future consideration.

- A separate GPT version
- Support for multiple adapter targets
- A dedicated CLI
- HTML index generation
- Stronger automation for issue and PR integration

---

## 22. Conclusion

This project is not a renamed version of a skills repository. It is an **original shipping playbooks system** designed to make it easier to repeat the flow from specification work to pre-release review inside a real repository.

For that reason, the project is designed from the beginning around the following ideas:

- An original structure built around playbooks, artifacts, gates, flows, and adapters
- Workflow-first responsibility boundaries
- A shipping-first definition of value
- Adapters as a support layer rather than the core structure

This specification is the baseline document for building that finished product.
