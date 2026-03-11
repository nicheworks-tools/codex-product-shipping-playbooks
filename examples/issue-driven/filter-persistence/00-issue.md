# Issue

## Title

Filters are sometimes cleared after navigation

## Report

When I apply filters on the listing page, the selected values do not always remain after I navigate to another page and then return.

This is especially noticeable when I:

1. open the listing page
2. select one or more filters
3. open an item detail page
4. go back to the listing page

Sometimes the filters still appear correctly, but sometimes they are cleared and I have to set them again.

## Expected behavior

Selected filters should remain active when returning to the listing page during normal in-app navigation.

## Notes

- This issue is about normal in-app navigation, not a full browser reload.
- It is not yet clear whether the problem is caused by route behavior, local state, or another part of the repository.
- No repository-specific details are included in the original report.
