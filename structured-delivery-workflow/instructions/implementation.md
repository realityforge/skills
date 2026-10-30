# Implementation

Implement the committed frontier sequentially and pass implementation review.

## Entry

Read the exact active tree's `SPEC.md`, `tasks/TASKMAP.md`, and active task;
load other tasks as dependencies or replanning require. The current plan must
be committed, with status `planned`, `implementing`, or `implementation-review`.

## Task loop

The primary agent implements one task at a time: the lowest-numbered pending
task whose blockers are complete. Keep only that task `in_progress`; delegate
implementation only on explicit user request.

Run every task validation before marking it complete. Record concise evidence,
update task status and frontier, and commit implementation and task/map state
together, excluding unrelated work.

If evidence invalidates a significant decision or materially changes scope,
stop the loop and reconcile the spec and affected tasks through
[planning](planning.md), its review, selected checkpoint, and revised-plan
commit before resuming. Local details preserving planned outcomes and impacts
do not reopen planning.

Before the final task commit, run the owning project's validation gate for the
changed behavior and delivery boundary. Without project policy, select checks
from dependencies and behavioral risk. Record the gate and evidence in
`TASKMAP.md`; enter `implementation-review` only after all tasks and the gate
pass.

## Promote durable knowledge

When the repository has any of `docs/adr/`, `docs/glossary/`, `docs/specs/`, or
`docs/deferred/`, use `$domain-modeling` to classify and promote accepted
durable requirements, decisions, language, and deferred questions. Validate
qualifying artifacts, link them from `TASKMAP.md`, and commit them before
review. Failed required promotion or validation blocks review.

Apply this step again to conclusions changed or omitted during review or
closeout, reusing prior classifications for unaffected conclusions. When none
of those directories exists, promotion is not required.

## Implementation review

Use the [implementation-review brief](../review/implementation-review.md) and
shared [review policy](../SKILL.md#review-policy). Validate and commit fixes
with affected task evidence and plan state before the next round; material
replanning and required promotion follow the rules above. Proceed to
[closeout](closeout.md) only after review passes.
