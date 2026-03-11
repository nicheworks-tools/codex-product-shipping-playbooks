# Spec Delta

## Summary

The requested change is to preserve selected filter values when a user leaves the listing page and returns through normal in-app navigation.

## Why this change exists

Users currently lose selected filters in at least some navigation flows.
This creates friction because they must reapply the same filters after returning to the listing page.

## Current state

- Filter selections can be cleared when the user navigates away from the listing page and then returns.
- The issue report suggests inconsistent persistence.
- The intended persistence behavior is not clearly documented in the repository.

## Intended state

- Selected filters remain active when a user navigates away from the listing page and then returns through normal in-app navigation.
- Returning to the listing page should preserve the user’s active filter context during the same app session.

## Delta

- Current behavior allows filter state to reset during normal in-app navigation.
- Intended behavior preserves filter state during that navigation path.
- The repository should move from fragile or page-local filter persistence to a flow that survives expected return navigation.

## In scope

- Preserving selected filter values across normal in-app navigation
- Return path from item detail page back to listing page
- Filter state behavior during the same active app session

## Out of scope

- Full browser reload persistence
- Persistence across logout/login
- Full redesign of the filter system
- Broader search relevance or backend filtering changes

## Impacted surfaces

- Listing page
- Filter bar component
- Filter state ownership
- Navigation / route return behavior
- Possible query parameter synchronization if currently used

## Assumptions

- Users expect filters to remain active during normal in-app return flows
- Session-level persistence is sufficient for this change
- The issue can be addressed without redesigning the entire search/filter system

## Constraints

- Existing repository behavior around route remounting may limit simple fixes
- Current test coverage may be incomplete
- The change should stay narrow and not expand into unrelated listing behavior

## Open questions

- Is filter state currently local, shared, or URL-driven?
- Does the problem occur on all return paths or only some of them?
- Should filter state be reflected in the URL as part of the solution?

## Risks

- Moving filter state ownership could affect related listing behavior
- Partial persistence fixes may hide deeper state-management problems
- A fix that works for one navigation path may miss another
