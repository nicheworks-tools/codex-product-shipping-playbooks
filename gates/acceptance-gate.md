# Acceptance Gate

Use this gate to decide whether acceptance has been defined clearly enough to support `ship-check`.

## Pass conditions

- [ ] Expected outcome is clearly stated
- [ ] Acceptance criteria are explicit
- [ ] Relevant edge cases are listed
- [ ] Manual verification expectations are listed
- [ ] Failure conditions are named
- [ ] Non-goals are identified where useful
- [ ] The done checklist is practical and understandable

## Questions to ask

- Do we know what “done” means for this change?
- Would a reviewer know how to check whether the work is acceptable?
- Are important edge cases being ignored?
- Are we treating “implemented” as the same thing as “accepted”?

## Fail conditions

Do **not** pass this gate if:

- acceptance is still based on vague judgment
- edge cases are missing entirely
- manual verification is undefined where it should exist
- the next step would still need to invent completion criteria

## Output expected before passing

The following should exist in some usable form:

- acceptance definition
- edge-case notes
- manual verification notes
- done checklist
