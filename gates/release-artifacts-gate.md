# Release Artifacts Gate

Use this gate to decide whether release-facing communication is complete enough for the current change.

## Pass conditions

- [ ] A changelog entry exists if one is warranted
- [ ] A release note exists if one is warranted
- [ ] The wording matches the actual scope of the change
- [ ] Documentation impact was considered
- [ ] The communication does not overstate what was delivered
- [ ] The outputs are understandable to the intended audience

## Questions to ask

- Does this describe what actually changed?
- Is the wording too broad for the real scope?
- Did we forget a release-facing artifact that should exist?
- Are we claiming more certainty or coverage than the work supports?

## Fail conditions

Do not pass this gate if:

- release-facing wording is still vague
- the communication exaggerates the change
- a needed changelog or release note is missing
- documentation impact was ignored completely

## Output expected before passing

The following should exist in some usable form:

- release note draft if needed
- changelog entry draft if needed
- documentation update summary or explicit no-update note
