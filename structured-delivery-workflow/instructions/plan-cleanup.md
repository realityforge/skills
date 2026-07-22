# Plan Artifact Cleanup

Use this instruction when persistent plan tree work is complete.

Remove the active persistent plan artifacts after:

- implementation is complete
- requirements-first implementation review has no remaining actionable
  findings
- valid implementation-review findings have been fixed and validated
- knowledge promotion is complete and the closeout record is prepared
- temporary plan retention is not required by repository policy or user
  decision

## Ordering

1. Update and validate required plan/task/evidence state before cleanup.
2. Complete knowledge promotion and validate changed canonical artifacts.
3. Prepare the closeout record with links to promoted artifacts.
4. Delete only the active plan tree for the completed scope.
5. Inspect the resulting change set.
6. When commits are requested, include plan removal in the final delivery or
   closeout commit. Use a separate deletion-only commit only when the user or
   repository convention requires one.

## Rules

- Delete only the active plan tree for the completed scope.
- Do not remove unrelated plan trees, even if they appear stale.
- Use the repository's normal commit workflow and hooks.
- If retention is required, leave the active plan tree in its reviewed final
  state and report the policy or user decision.
- If no commit was requested, remove temporary plan artifacts and report the
  remaining uncommitted implementation and documentation changes normally.
