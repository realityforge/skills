# Planning

Create the complete plan from the authorized scope and verified facts and pass
planning review. Continue directly to implementation unless an explicit user
checkpoint or stopping condition applies.

For planning-only authority, report the reviewed plan and stop at that boundary.
Implementation awaits the user's next instruction.

## 1. Create the tree

Record `Plan checkpoint: human-review (pending)` in `TASKMAP.md` only when the
user explicitly asked to review the plan before implementation; otherwise use
`Plan checkpoint: automatic (pending planning review)`. Record the accepted
scope and execution-authority sources established at the entry gate. Scope
acceptance or interview confirmation does not itself request a plan-review
pause.

Read applicable repository instructions and inspect the worktree. Choose an
unused `plans/<initiative>/` path. An existing path is never a merge target;
use it only when the user explicitly named or requested resumption of that
paused plan.

Load these templates only while creating their artifact:

- `../templates/SPEC.md`
- `../templates/TASKMAP.md`
- `../templates/TASK.md`

## 2. Write `SPEC.md`

Synthesize the accepted scope, constraints, execution authority, and verified
repository facts. Reuse prior decisions and resolve remaining choices under
the [decision policy](../../AGENTS.md#scope-and-design).

The spec is complete when it has:

- the problem, required outcome, scope boundaries, and constraints
- solution-independent requirements and checkable acceptance criteria
- the technical and testing decisions needed to preserve shared understanding
- every significant decision with its rationale, impact, and what the user
  should verify
- no unresolved choice requiring user direction under the decision policy

Use user stories only when actors or distinct observable journeys are clearer
that way. Prefer stable modules and contracts over file paths or code snippets.
Include a decision-rich prototype fragment only when prose would lose the
decision it encodes.

If verified evidence invalidates an accepted assumption, reopen the affected
decision under that policy. Pause dependent work only when user direction is
required; continue independent work.

## 3. Derive tasks directly from the spec

Create one task file per tracer-bullet vertical slice. Each task delivers and
validates a narrow end-to-end behavior and fits one fresh context window.
Number tasks in topological order, with blockers before dependants.

Use expand-migrate-contract tasks for a wide mechanical refactor only when a
vertical slice cannot remain green. Prefactoring that makes the change easy is
an earlier task with its own observable acceptance boundary.

`tasks/TASKMAP.md` is the implementation plan. It owns the task index,
dependency edges, execution frontier of all unblocked pending tasks, status,
and cross-task sequencing notes.
Each task file owns its delivered behavior, spec coverage, blockers, acceptance
criteria, validation, and evidence. Supporting files are not additional
requirements sources.

The task tree is complete when:

- every requirement and acceptance criterion has task ownership
- every task is independently demonstrable or verifiable
- dependencies are necessary and acyclic
- the lowest-numbered unblocked pending task can be selected mechanically
- cross-cutting tests, documentation, migration, rollout, and cleanup work has
  an owner

## 4. Run planning review

Perform one author preflight against the completion criteria above. Read
`../review/planning-review.md` and start or resume review under the shared
[review policy](../SKILL.md#review-policy) for continuity, replacement, budget,
and escalation. The first round reviews `SPEC.md`, `TASKMAP.md`, and every task
file together. Later rounds check prior findings, their dispositions,
intervening user corrections, resulting edits, and affected surfaces.

The default planning limit is three rounds plus the shared policy's final
confirmation allowance, unless the user sets another budget. Assess every
finding against the conversation, repository, and plan; make the narrowest
evidence-backed correction. A material spec change requires reconciliation of
the task map and affected task files.

Record reviewer history, consumed rounds and final confirmation, finding
dispositions, and result in `TASKMAP.md`. Finalize only after review passes.

## 5. Finalize the plan

After planning review passes, follow the selected plan checkpoint.

For `automatic`, record `Plan checkpoint: automatic` and its basis—the
accepted scope, execution authority, and passing planning review—in
`TASKMAP.md`, set its status to `planned`, send a non-blocking progress update
with links to `SPEC.md` and `TASKMAP.md`, and continue without asking for
approval.

For `human-review`, give the user:

- links to `SPEC.md` and `TASKMAP.md`
- a concise task sequence
- every significant decision, its impact, and what the user should verify
- planning-review rounds and result

Ask for explicit approval. Apply requested changes and return to planning
review when they materially affect requirements, decisions, coverage,
sequencing, or validation; the existing review budget still applies.

After approval, record `Plan checkpoint: human-review` and the approval basis
in `TASKMAP.md`, and set its status to `planned`.

For either checkpoint, validate the plan links and task graph, then commit the
exact active plan tree without staging unrelated changes. Stop before
implementation if the plan commit fails.

Planning is complete when the current plan exists in git history and the
worktree contains that committed version.
