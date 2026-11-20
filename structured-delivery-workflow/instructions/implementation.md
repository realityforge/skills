# Implementation

Implement the planned frontier sequentially and pass implementation review.

## Entry

Read the active tree's `tasks/TASKMAP.md` and `SPEC.md`. During
implementation, load the selected task and others as dependencies or replanning
require. The tree's status must be `planned`, `implementing`, or
`implementation-review`.

## Task loop

The primary agent implements one task at a time: the lowest-numbered pending
task whose blockers are complete. Mark only that task `in_progress` in
`TASKMAP.md`; delegate implementation only on explicit user request.

Run every task validation before marking it complete in `TASKMAP.md`. Update the
map's status and frontier, then commit the task's implementation, excluding
unrelated work.

If implementation invalidates a significant decision or materially changes
scope, stop the loop and reconcile the spec and affected tasks through
[planning](planning.md), including its review when required, before resuming.
Local details preserving planned outcomes and impacts do not reopen planning.

Before the final task commit, run [`$simplify`](../../simplify/SKILL.md) on the
delivered code. Then run the owning project's validation gate for the changed
behavior. Without project policy, select checks from dependencies and
behavioral risk. Enter `implementation-review` only after all tasks and the
gate pass.

## Promote durable knowledge

Promotion is required when the work creates or changes a durable conclusion
(behavior consumers rely on, a decision costly to reverse, domain language, or
a deliberate deferral) and the repository has any of `docs/adr/`,
`docs/glossary/`, `docs/specs/`, or `docs/deferred/`. Then use
`$domain-modeling` to promote it, validate the artifacts, and commit them
before review. Apply this step again to conclusions that review changes.

## Implementation review

Before starting or resuming implementation review, read the
[review policy](../review/policy.md) and
[implementation-review brief](../review/implementation-review.md). Validate and
commit fixes before the next round; material replanning and required promotion
follow the rules above. Proceed to [closeout](closeout.md) only after review
passes.
