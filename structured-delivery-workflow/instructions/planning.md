# Planning

Create the plan, review it when required, then continue to implementation
unless the user asked for a plan only.

## 1. Create the tree

Use the [plan-tree policy](../SKILL.md#plan-tree) and load templates as needed:

- `../templates/SPEC.md`
- `../templates/TASKMAP.md`
- `../templates/TASK.md`

## 2. Write `SPEC.md`

State the problem, accepted scope and constraints, and the repository facts the
plan relies on. Define solution-independent requirements, checkable acceptance
criteria, and the technical and testing decisions needed for delivery.
Significant decisions include rationale, impact, and what the user should
verify. Resolve choices requiring user direction under the shared decision
policy before review.

## 3. Derive tasks directly from the spec

Use independently verifiable end-to-end slices sized for a fresh context.
Mechanical refactors may use expand-migrate-contract when vertical slices
cannot remain green. Number tasks in dependency order with necessary, acyclic
blockers. Every requirement and acceptance criterion, including cross-cutting
migration, rollout, tests, documentation, and cleanup, has task ownership.

`TASKMAP.md` alone owns the task index, status, dependencies, and unblocked
pending frontier. Task files own delivered behavior, spec coverage, acceptance
criteria, and validation.

## 4. Run planning review when required

Planning review is required when the plan has more than three tasks, a
significant decision that is costly to reverse, or the user asks for it;
otherwise mark it `not required` in `TASKMAP.md` and finalize.

Before starting or resuming planning review, read the
[review policy](../review/policy.md) and
[planning-review brief](../review/planning-review.md). Reconcile material spec
changes across the task map and affected tasks. Finalize only after review
passes.

## 5. Finalize the plan

Validate links and the task graph, then set status `planned` in `TASKMAP.md`.
Summarize the task sequence, significant decisions and impacts, what the user
should verify, and the review result.

When the user asked to see the plan before implementation, wait for their
approval and re-review changes that materially affect requirements, decisions,
coverage, sequencing, or validation. Otherwise continue to implementation.
