# Diff Review Gate

Use this gate to decide whether the diff review is complete enough to support later retrospective work.

## Pass conditions

- [ ] The implemented change is summarized clearly
- [ ] Main touch points are identified
- [ ] Delivered scope is compared with intended scope
- [ ] Important review notes are recorded
- [ ] Follow-up items are listed if needed
- [ ] The output is concise enough to be useful later

## Questions to ask

- Does this review explain what actually changed?
- Is the implementation summary clearer than reading release-facing notes alone?
- Did we note any mismatch between intended and delivered scope?
- Would a later retrospective benefit from this record?

## Fail conditions

Do not pass this gate if:

- the summary is too vague
- touch points are missing completely
- scope comparison is absent
- follow-up work is implied but not recorded

## Output expected before passing

The following should exist in some usable form:

- diff review summary
- touch point list
- scope comparison notes
- follow-up items if needed
