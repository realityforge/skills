# Planning

Create and review the plan, then continue to implementation when authorized.
Planning-only work stops after the plan commit.

## 1. Create the tree

Use the [plan-tree policy](../SKILL.md#plan-tree) and load templates as needed:

- `../templates/SPEC.md`
- `../templates/TASKMAP.md`
- `../templates/TASK.md`

In `TASKMAP.md`, select `human-review (pending)` only when the user explicitly
requested a plan checkpoint; otherwise use `automatic (pending planning
review)`.

## 2. Write `SPEC.md`

Complete the spec with sources for accepted scope, constraints, execution
authority, checkpoints, and verified repository facts. Define
solution-independent requirements, checkable acceptance criteria, and the
technical and testing decisions needed for delivery. Significant decisions
include rationale, impact, and what the user should verify. Resolve choices
requiring user direction under the shared decision policy before review.

## 3. Derive tasks directly from the spec

Use independently verifiable end-to-end slices sized for a fresh context.
Mechanical refactors may use expand-migrate-contract when vertical slices
cannot remain green. Number tasks in dependency order with necessary, acyclic
blockers. Every requirement and acceptance criterion, including cross-cutting
migration, rollout, tests, documentation, and cleanup, has task ownership.

`TASKMAP.md` owns the index, dependencies, unblocked pending frontier, and
status. Each task owns its delivered behavior, spec coverage, blockers,
acceptance criteria, validation, and evidence.

## 4. Run planning review

Use the [planning-review brief](../review/planning-review.md) and shared
[review policy](../SKILL.md#review-policy). Reconcile material spec changes
across the task map and affected tasks. Finalize only after review passes.

## 5. Finalize the plan

Link `SPEC.md` and `TASKMAP.md`; summarize the task sequence, significant
decisions and impacts, what the user should verify, and review result.
For `human-review`, obtain explicit approval; for `automatic`, the update is
non-blocking. Re-review requested changes that materially affect requirements,
decisions, coverage, sequencing, or validation.

Record the completed checkpoint (`automatic` or `human-review`), its basis,
and `planned` status in `TASKMAP.md`. Validate links and the task graph, then
commit the exact active tree without unrelated changes. Implementation requires
this current committed version and execution authority; a failed plan commit
leaves planning incomplete.
