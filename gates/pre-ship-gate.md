# Pre-Ship Gate

Use this gate to decide whether a change is ready to move past review and toward shipping.

## Pass conditions

- [ ] Scope is still understood and unchanged in a risky way
- [ ] Acceptance has been reviewed
- [ ] Known blockers are listed
- [ ] Known risks are listed
- [ ] Documentation impact was checked
- [ ] Release-facing communication impact was considered
- [ ] Rollback or recovery concerns were considered if relevant
- [ ] A final recommendation can be stated clearly

## Questions to ask

- Is this actually ready, or does it only feel close?
- Are there unresolved blockers that should stop shipping?
- Are the risks understood well enough?
- Did we remember docs and release-facing impact?
- If something goes wrong, do we at least know how to think about recovery?

## Fail conditions

Do **not** pass this gate if:

- blockers are still unresolved
- risks are not understood at all
- acceptance has not really been reviewed
- documentation impact was ignored
- no one can clearly say whether this is ready to ship

## Output expected before passing

The following should exist in some usable form:

- pre-ship review
- blockers and risks list
- documentation / communication check
- final recommendation
