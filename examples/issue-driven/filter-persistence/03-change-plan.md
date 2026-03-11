# Change Plan

## Summary

Adjust the filter-state handling so selected values survive normal in-app navigation away from the listing page and back.

## Source inputs

- Repository context memo
- Spec delta
- Original issue report

## Proposed implementation shape

The likely solution is to move filter state ownership to a level that survives expected route transitions, or to restore the state from an existing navigation-safe source when the listing page is revisited.

## Likely touch points

- Listing page component
- Filter bar component
- Filter state hook, store, or context
- Route transition or page initialization logic
- Any query parameter synchronization logic

## Planned steps

1. Inspect where filter values are currently stored and how they are initialized.
2. Confirm whether the listing page is remounted on return navigation.
3. Identify whether filter state should be:
   - lifted to a longer-lived state layer, or
   - restored from URL / route state if that pattern already exists.
4. Update the filter-state flow so expected return navigation restores the prior selection.
5. Verify that the change does not break default filter initialization.
6. Review whether any user-facing docs or internal notes need updates.

## Dependencies

- Clear understanding of current state ownership
- Confirmation of how return navigation is handled in the app

## Sequencing notes

State ownership should be understood before changing UI behavior.
Acceptance should be defined before the team treats the implementation as ready.

## Documentation impact

Potential updates:
- Internal behavior notes for listing/filter state
- Testing notes if filter persistence behavior is documented
- Release summary if this is a user-visible bug fix

## Testing implications

The team should verify:

- filters remain selected after navigating to detail and back
- default filter state still works for a fresh visit
- unrelated listing interactions are not broken
- behavior remains stable across expected navigation paths

## Risks and tradeoffs

- Lifting state may increase coupling
- URL-based persistence may introduce its own complexity
- A narrow fix may miss another return path if routing behavior differs elsewhere

## Unresolved questions

- Should filter persistence live in shared state or URL state?
- Are there existing conventions in this repository that make one approach preferable?

## Handoff notes

Acceptance must explicitly define:
- which navigation paths are covered
- what counts as success
- what is out of scope
- what must be checked manually before shipping
