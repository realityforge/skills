# Plan Artifact Cleanup

Use this instruction when persistent plan tree work is complete and committed.

Remove the active persistent plan artifacts after:

- implementation is complete
- requirements-first implementation review has no remaining actionable
  findings
- valid implementation-review findings have been fixed and validated
- implementation, evidence, and review-fix changes have been committed

The cleanup must be a separate commit that contains only removal of the active
plan artifacts. Do not combine plan-artifact deletion with implementation,
review-fix, evidence, or unrelated cleanup changes.

## Ordering

1. Update and validate required plan/task/evidence state before cleanup.
2. Commit implementation, evidence, and review-fix changes first.
3. Delete only the active plan tree for the completed scope.
4. Create a deletion-only cleanup commit.
5. Verify the cleanup commit contains only active plan artifact removal.

## Rules

- Delete only the active plan tree for the completed scope.
- Do not remove unrelated plan trees, even if they appear stale.
- Use the repository's normal commit workflow and hooks.
- If the user explicitly prohibited commits, leave the plan cleanup pending and
  report that the final cleanup commit was not created.
- If implementation was intentionally left uncommitted, do not remove the plan
  artifacts yet; report that cleanup is blocked until implementation is
  committed or the user explicitly changes the workflow.
