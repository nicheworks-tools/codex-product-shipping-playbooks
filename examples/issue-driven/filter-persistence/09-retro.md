# Retro

## Summary

This retrospective covers the synthetic filter-persistence example from issue intake through release-facing communication, diff review, and post-ship learning.

## Source inputs

- Diff review:
  `08-diff-review.md`

- Release note or changelog:
  `06-release-note.md`
  `07-changelog-entry.md`

- Pre-ship review:
  `05-pre-ship-review.md`

- Other observations:
  synthetic workflow demonstration context

## What went well

- The issue-to-ship flow clarified scope early.
- Acceptance criteria reduced ambiguity before shipping review.
- Release-facing wording stayed aligned with the actual delivered scope.

## What went poorly

- Secondary navigation paths were left as later follow-up instead of being resolved earlier.
- The example still depends on synthetic assumptions rather than a live repository.
- Some scope confidence was deferred until later review rather than tested sooner.

## Surprises

- The distinction between release-facing notes and implementation-facing review became more useful once both were written separately.
- A narrow bug fix still benefited from explicit acceptance and pre-ship structure.
- The later retrospective remained concise because the earlier workflow records were already clear.

## Improvement actions

- Define covered navigation paths earlier in similar future changes.
- Check for scope drift before implementation review begins.
- Reuse the same example pattern for at least one more scenario later.

## Notes

This example suggests that the repository structure is most valuable when each step leaves behind a usable record for the next one.
