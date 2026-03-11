# Quality Gates

## Purpose of this document

This document defines the quality thresholds that repository content must meet.

The goal is to prevent the project from drifting into:

- vague theory
- clone-like structure
- weak template sprawl
- unclear workflow boundaries
- publication without operational proof

This document is about **pass / fail standards**, not about the broader vision of the project.

---

## What quality means here

Quality in this repository does **not** mean “longer” or “more detailed.”

Quality means:

- the purpose of each file is clear
- workflow handoffs are practical
- outputs are reusable
- review checkpoints are concrete
- the repository still feels like a shipping workflow system

A file can be short and still be high quality.
A file can be long and still fail.

---

## Repository-level gates

### Gate R1: Identity clarity
A reader should still understand that this repository is:

- a shipping workflow system
- repository-aware
- implementation-aware
- ship-aware

It must not read like:

- a generic PM toolkit
- a prompt collection
- a skills clone
- a loose template dump

### Gate R2: Structural clarity
The distinction between these layers must remain clear:

- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`
- `adapters/`

If content starts to blur those responsibilities, the structure is failing.

### Gate R3: Native-first structure
The native structure must remain primary.

Adapters may be added, but the repository must not be reshaped around external compatibility.

### Gate R4: Workflow continuity
The core path must remain understandable from:

- repository intake
- spec delta
- change planning
- acceptance definition
- ship check

If that chain becomes unclear, the repository is not healthy.

### Gate R5: Public-value clarity
The reason to use this with Codex must still be explainable in one sentence.

If that sentence becomes hard to defend, the repository has drifted too far.

---

## Playbook-level gates

Every playbook must pass the following.

### Gate P1: One clear responsibility
A playbook must represent one workflow responsibility.

If it tries to cover multiple roles at once, it should be split or narrowed.

### Gate P2: Clear use and non-use cases
A playbook must clearly state:

- when to use it
- when not to use it

If those boundaries are missing, the playbook is too vague.

### Gate P3: Concrete inputs and outputs
A playbook must define:

- what inputs it expects
- what artifacts it creates or updates

If those are not concrete, the playbook is incomplete.

### Gate P4: Handoff clarity
A playbook must clearly connect to the next step.

If it produces output that does not help the next workflow step, it has failed the gate.

### Gate P5: Repository relevance
A playbook must stay tied to real repository work.

If it drifts into abstract PM language without operational value, it fails.

### Gate P6: Distinctiveness
A playbook must not feel like a renamed generic PM topic.

It should feel like a concrete step in repository-based shipping work.

### Gate P7: Testability
A playbook must be usable in at least one realistic repository scenario.

If it cannot be tested in practice, it is not ready.

---

## Artifact-level gates

Every artifact must pass the following.

### Gate A1: Operational usefulness
An artifact must be usable in real work with minimal rewriting.

If it is too generic to be useful, it fails.

### Gate A2: Clear purpose
The filename and structure of the artifact must make its purpose obvious.

A user should not have to guess what the template is for.

### Gate A3: Workflow alignment
An artifact must clearly support one or more playbooks.

If it floats independently without a workflow role, revise or remove it.

### Gate A4: Low filler
Artifacts should avoid:

- generic boilerplate
- motivational filler
- abstract framing with no operational consequence

### Gate A5: Reusability
An artifact should be reusable across multiple change scenarios.

If it is too narrow, it may belong inside an example instead.

---

## Gate-level gates

Every gate file must pass the following.

### Gate G1: Practicality
A gate must be short enough to use in actual work.

### Gate G2: Decision usefulness
A gate must help someone decide whether a step is actually complete.

If it reads like a vague reminder list, it fails.

### Gate G3: Concrete checks
A gate should include checks tied to:

- implementation
- docs
- risks
- shipping readiness

as appropriate for the workflow step.

### Gate G4: Workflow fit
A gate must match the playbook it belongs to.

A gate that is too generic weakens the system.

---

## Flow-level gates

Every flow file must pass the following.

### Gate F1: Sequence clarity
The order of steps must be obvious.

### Gate F2: Handoff visibility
The flow must show what output from one step becomes input to the next.

### Gate F3: Realism
The flow must feel usable in real work, not like a theoretical chain.

### Gate F4: Scope discipline
A flow should not try to describe every possible variation at once.

Core flows should stay readable and practical.

---

## Documentation-level gates

Supporting docs must pass the following.

### Gate D1: Clear role
Each document in `docs/` must have a clear role.

If a document overlaps heavily with another file, revise the structure.

### Gate D2: Non-redundancy
Documents should support the system without repeating the same explanation unnecessarily.

### Gate D3: Structural support
Docs should strengthen understanding of the repository model.

They should not drift into unrelated general theory.

---

## Example-level gates

Examples must pass the following.

### Gate E1: Realistic context
An example should describe a believable repository situation.

### Gate E2: Clear mapping
It should be clear which playbooks, artifacts, and gates are involved.

### Gate E3: Workflow value
The example should show why the repository structure helps.

If the example could be replaced by generic prose, it is too weak.

### Gate E4: Synthetic honesty
If an example is synthetic, it should say so clearly.

---

## Adapter-level gates

Adapters must pass the following.

### Gate X1: Secondary role
An adapter must remain a support layer, not the product core.

### Gate X2: Native structure preservation
The native repository structure must not be bent to satisfy adapter needs.

### Gate X3: Explicit boundary
It should be clear what the adapter exports and what it does not.

---

## Review questions before adding content

Before adding a new file, ask:

1. What layer does this belong to?
2. What concrete job does it do?
3. What workflow step does it support?
4. Does it duplicate something that already exists?
5. Would this make the repository feel more like a clone or a dump?
6. Does it strengthen the shipping workflow identity?

If these questions do not have good answers, do not add the file yet.

---

## Review questions before publishing

Before publication, the repository should pass these questions:

1. Does the structure feel original?
2. Is the Codex-related value obvious?
3. Do the workflow layers make sense?
4. Are the core playbooks usable in real work?
5. Are the artifacts practical?
6. Are the gates concrete?
7. Do the examples prove that the model works?
8. Does the repository still feel like a shipping workflow system?

If the answer to several of these is no, publication should wait.

---

## Minimum pass condition

A part of the repository is good enough only if:

- its role is clear
- its boundary is clear
- its practical use is clear
- its next connection is clear
- it strengthens the repository’s identity

Anything less should be treated as draft material, not completed work.
