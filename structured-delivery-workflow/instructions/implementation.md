# Implementation

Implement the committed frontier sequentially, promote durable knowledge when
the repository uses it, and pass one iterative implementation review.

## Entry

Read the active tree's `tasks/TASKMAP.md`. Verify that:

- status is `planned`, `implementing`, or `implementation-review`
- the current plan snapshot exists in git history
- the active tree is the exact plan for the authorized outcome, or the plan
  explicitly requested for resumption

Load `SPEC.md`, the task map, and only the active task before implementation.
Load other task files when dependencies, cross-task contracts, or replanning
requires them.

## Task loop

The primary agent implements one task at a time. Select the lowest-numbered
pending task whose blockers are complete and keep only that task
`in_progress`.

For each task:

1. Confirm its delivered behavior, spec coverage, acceptance criteria, and
   validation.
2. Inspect the relevant implementation and repository conventions.
3. Make the smallest coherent end-to-end change.
4. Run focused checks while iterating and every task validation before marking
   it complete.
5. Record concise command or observable evidence in the task file, mark the
   task complete, and advance the task map's frontier.
6. Commit the implementation and its task/map state together without staging
   unrelated work.

Delegate implementation only when the user explicitly requests it. Reviewer
agents remain read-only.

When implementation evidence invalidates a committed significant decision or
materially changes scope, stop the task loop. Update `SPEC.md` and every
affected task artifact, return to `planning.md` for review by the same planning
reviewer, follow the selected plan checkpoint, and commit the revised plan
before resuming. Local details that preserve planned outcomes and impacts do
not reopen planning.

For the final task, run the strongest practical full-scope gate after its
task-local validation. Record the full-gate evidence in `TASKMAP.md` before
committing that task. Set status to `implementation-review` only when every
task and the full gate pass.

## Promote durable knowledge

After implementation and before activating the implementation reviewer, check
for any of:

- `docs/adr/`
- `docs/glossary/`
- `docs/specs/`
- `docs/deferred/`

If any exists, use `$domain-modeling` to classify the plan's accepted durable
requirements, decisions, resolved language, and deliberately deferred
questions. Promote every qualifying item to its canonical owner and validate
the changed artifacts as that skill requires. Record canonical links in
`TASKMAP.md` and commit promoted artifacts before review. A failed required
promotion or validation blocks implementation review.

When none of those directories exists, proceed without promotion; the delivery
workflow does not require a domain-documentation system.

## Implementation review

Create one fresh, clean, read-only implementation reviewer and read
`../review/implementation-review.md`. Use that same reviewer for every round.

The first round reviews the committed spec against delivered behavior, plan
history, implementation scope, tests, validation evidence, and promoted
knowledge. Later rounds receive prior findings, their disposition, resulting
changes, and affected surfaces.

The implementation limit is five total reviewer rounds unless the user sets or
extends another limit. Each reviewer attempt consumes one round. Verify every
finding against repository evidence. Fix valid findings at the earliest
affected level and run focused validation.

If a fix changes planned scope or a significant decision, return to planning,
review, the selected plan checkpoint, and a revised-plan commit before
continuing. Otherwise update the affected task evidence and commit the fix with
its plan-state update.

When domain directories are present and a fix changes durable knowledge, run
`$domain-modeling` promotion and validation before the next review round.

The review passes only on `Findings: none`. If blocking findings remain at the
limit, ask whether to extend it. Do not substitute another reviewer or claim
success.

Record reviewer identity, round count, and result in `TASKMAP.md`, then route to
`closeout.md`.
