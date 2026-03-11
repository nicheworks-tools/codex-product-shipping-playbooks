# Repo Intake Gate

Use this gate to decide whether repository intake is complete enough to move into `spec-delta`.

## Pass conditions

- [ ] The repository structure has been reviewed at a basic level
- [ ] The main entry points or likely starting points are identified
- [ ] The most relevant files or directories are listed
- [ ] Known repository conventions or constraints are noted
- [ ] Unknowns or missing context are explicitly listed
- [ ] There is enough context to describe the requested change in repository terms

## Questions to ask

- Do we understand where the change is likely to live?
- Do we understand what parts of the repository might be affected?
- Do we know what we still do not know?
- Are we about to guess instead of reading the repository?

## Fail conditions

Do **not** pass this gate if:

- the repository was only skimmed superficially
- likely touch points are still unclear
- key unknowns were not written down
- the next step would rely mainly on assumptions

## Output expected before passing

The following should exist in some usable form:

- repository context memo
- key file or touch point list
- constraints list
- missing context notes
