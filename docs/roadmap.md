# Roadmap

## Purpose of this document

This document describes the staged development path for the repository.

The roadmap is not just a list of tasks.
It defines how the project should grow without losing its structure, originality, or public value.

---

## Overall direction

The project should grow in a controlled way.

It should move through these stages:

1. establish the structure
2. make the first workflow usable
3. validate the workflow on real work
4. expand into release and review flows
5. prepare for public release

The repository should not try to become “big” too quickly.
Clarity matters more than speed.

---

## Phase 1: Foundation

### Goal
Create the base structure of the project and lock in the design direction.

### Main targets
- establish the top-level layers
- create `AGENTS.md`
- create `README.md`
- write the foundational docs
- create the core playbook folders
- define the first artifact, gate, and flow placeholders

### Expected result
By the end of this phase, the repository should have:
- a stable structure
- clear naming
- a non-clone identity
- a clear path into MVP work

### Things that matter most here
- structure
- responsibility boundaries
- naming clarity
- design direction

### Things that do **not** matter most here
- content volume
- completeness of every template
- polished examples
- public-facing polish

---

## Phase 2: Core Flow MVP

### Goal
Make the first issue-to-pre-ship workflow actually usable.

### Core playbooks in this phase
- `intake-repo`
- `spec-delta`
- `plan-change`
- `define-acceptance`
- `ship-check`

### Main targets
- write the first `PLAYBOOK.md` files
- create the first working artifacts
- create the first working gates
- create the first working flows
- make the system usable in a real repository context

### Expected result
A user should be able to:
- understand a repository
- define a change
- build an implementation plan
- define what counts as done
- run a pre-ship review

This is the minimum viable operational loop.

---

## Phase 3: Practical MVP Validation

### Goal
Test the structure against real work and tighten weak areas.

### Main targets
- run the system against real repository tasks
- identify where playbooks overlap
- identify weak or vague artifacts
- strengthen gates that are too soft
- improve flow clarity
- remove unnecessary complexity

### Expected result
The repository should become more practical and less theoretical.

This phase is about proving that the model works in use, not just in outline.

### Key questions for this phase
- Do the playbooks actually reduce ambiguity?
- Are the artifacts reusable?
- Are the gates concrete enough to matter?
- Is the handoff between steps clean?
- Does the repository feel workflow-native?

---

## Phase 4: Shipping Expansion

### Goal
Expand the system beyond pre-ship work into release-facing and post-change workflows.

### Main targets
- add `write-release-artifacts`
- add `review-diff`
- add `post-ship-retro`
- extend the artifact set
- extend the flow set
- improve examples
- improve supporting docs

### Expected result
The repository should support a broader shipping lifecycle:

- before implementation
- during change planning
- before shipping
- around release communication
- after implementation and shipping

This is the phase where the system begins to feel complete.

---

## Phase 5: Public Release Candidate

### Goal
Bring the repository up to a level that is suitable for publication.

### Main targets
- improve README clarity
- improve docs quality
- strengthen examples
- formalize quality standards
- refine naming where necessary
- add the first adapter support
- make publication decisions

### Expected result
A public visitor should be able to understand:
- what the project is
- what it is not
- why it exists
- why it is useful with Codex
- how the structure works
- how to try it on real work

This phase is where internal structure becomes public product quality.

---

## Phase 6: Post-release development

### Goal
Improve the system after publication without losing its core identity.

### Possible directions
- refine adapters
- improve validation scripts
- add more realistic examples
- add stronger release and review flows
- improve index and discoverability
- expand documentation for contributors

### Warning
Expansion should be selective.
The repository should not drift into:
- a generic PM toolkit
- a template dump
- a compatibility-first clone

---

## What should not happen

The roadmap should not be allowed to drift into these failure modes:

### Failure mode 1: clone drift
The project starts to resemble a skills clone in naming, structure, or public presentation.

### Failure mode 2: PM drift
The project expands into generic PM topics and loses its repository-aware shipping focus.

### Failure mode 3: template sprawl
The repository adds too many templates without improving workflow quality.

### Failure mode 4: structure erosion
The boundaries between playbooks, artifacts, gates, and flows become blurry.

### Failure mode 5: publication before proof
The project gets polished for release before the workflow model has been validated on real work.

---

## Release readiness for each phase

### Foundation phase is complete when:
- the base structure exists
- the core docs exist
- the naming direction is stable
- the identity of the repository is clear

### Core Flow MVP phase is complete when:
- the five core playbooks exist
- the first artifacts exist
- the first gates exist
- the first flows exist
- the issue-to-pre-ship loop can be run

### Practical MVP Validation phase is complete when:
- the system has been tested on real work
- weak or overlapping parts have been revised
- the workflow feels usable in practice

### Shipping Expansion phase is complete when:
- release-facing work is supported
- diff review is supported
- post-ship learning is supported
- the repository feels like a broader shipping system

### Public Release Candidate phase is complete when:
- the public-facing explanation is strong
- examples are convincing
- quality standards are formalized
- publication can be justified clearly

---

## Long-term success condition

The roadmap is successful if the repository reaches a state where it can honestly be described as:

**an original shipping workflow system for real repositories**

If it becomes merely:
- a renamed clone
- a generic PM library
- a loose collection of prompts and templates

then the roadmap has failed, even if many files were added.
