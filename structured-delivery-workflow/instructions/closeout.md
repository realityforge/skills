# Closeout

Close only after implementation review passes. Complete any remaining
[required knowledge promotion](implementation.md#promote-durable-knowledge)
and validation before deleting the plan.

## Domain audit

When promotion was required, after it is complete, run the `$domain-modeling` audit in a clean subagent independent of
the work, supplying the repository root, diff range, and active plan tree. It corrects artifacts directly and reports
open questions. Validate and commit its corrections; resolve its questions with the user before the cleanup gate.

## Cleanup gate

Verify that all tasks, simplification, task-local and full-scope validation,
implementation review, required knowledge promotion, and domain audit are
complete, with
[passes valid for the final substantive changes](../review/policy.md#pass-validity).
Review history and evidence must be recorded, with the plan and implementation
updates in git history.

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
- Publication results when required by the delivery boundary; for pull request
  delivery, the URL, check status, and pending human Merge.

Closeout completes at the authorized delivery boundary recorded in `SPEC.md`.
For pull request delivery, leave it ready for human merge; passing checks do
not authorize merging.
