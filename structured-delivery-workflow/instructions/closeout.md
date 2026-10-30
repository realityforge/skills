# Closeout

Close only after implementation review passes. Complete any remaining
[required knowledge promotion](implementation.md#promote-durable-knowledge)
and validation before deleting the plan.

## Cleanup gate

Verify that all tasks, task-local and full-scope validation, implementation
review, and required knowledge promotion are complete. Review history and
evidence must be recorded, with the plan and implementation updates in git
history.

Apply the [global cleanup rules](../../AGENTS.md#test-and-clean-up) to documents
completed by this work, including those outside the plan tree.

Inspect the exact active tree, including temporary files, then delete only
that tree. Commit the deletion with any final canonical changes, excluding
unrelated work. Earlier commits preserve the audit trail. If deletion or its
commit fails, report the remaining worktree state and leave closeout incomplete.

## Handoff

Report:

- Delivered outcome, significant decisions, and impacts.
- Validation commands and results, review attempts and results, and residual
  risk or skipped checks.
- Canonical artifact links, plan and closeout commits, confirmation of tree
  removal, and unrelated uncommitted work.
- When published, the pull request URL, check status, and pending human Merge.

Closeout is complete when the published pull request is ready for a human to
merge. Passing checks do not extend closeout into merging the pull request.
