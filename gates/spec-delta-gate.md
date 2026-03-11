# Spec Delta Gate

Use this gate to decide whether the change has been defined clearly enough to move into `plan-change`.

## Pass conditions

- [ ] The current state is described clearly
- [ ] The intended state is described clearly
- [ ] The delta between them is explicit
- [ ] In-scope and out-of-scope boundaries are written down
- [ ] Likely impacted surfaces are listed
- [ ] Important assumptions are listed
- [ ] Important risks or open questions are listed

## Questions to ask

- Is the change actually defined, or only implied?
- Would another person understand what is changing and what is not?
- Are scope boundaries clear enough to plan implementation?
- Are we hiding uncertainty instead of naming it?

## Fail conditions

Do **not** pass this gate if:

- the requested change is still vague
- scope boundaries are missing
- impacted surfaces are not identified at all
- the next step would have to invent the change definition

## Output expected before passing

The following should exist in some usable form:

- spec delta draft
- in-scope / out-of-scope section
- impacted surfaces list
- assumptions and open questions
