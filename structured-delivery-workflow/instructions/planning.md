# Planning

Create the complete plan from the confirmed conversation context and pass
planning review. Continue directly to implementation unless the user explicitly
requested to review the plan first.

## 1. Create the tree

Record `Plan checkpoint: human-review (pending)` in `TASKMAP.md` only when the
user explicitly asked to review the plan before implementation; otherwise use
`Plan checkpoint: automatic (pending planning review)`. Their `$grill-me`
confirmation supplies the plan's authority but does not by itself request
another review pause.

Read applicable repository instructions and inspect the worktree. Choose an
unused `plans/<initiative>/` path. An existing path is never a merge target;
use it only when the user explicitly named or requested resumption of that
paused plan.

Load these templates only while creating their artifact:

- `../templates/SPEC.md`
- `../templates/TASKMAP.md`
- `../templates/TASK.md`

## 2. Write `SPEC.md`

Synthesize the completed `$grill-me` conversation and verified repository
facts. Do not interview the user again. Reopen a settled point only when
current evidence contradicts it.

The spec is complete when it has:

- the problem, required outcome, scope boundaries, and constraints
- solution-independent requirements and checkable acceptance criteria
- the technical and testing decisions needed to preserve shared understanding
- every significant decision with its rationale, impact, and what the user
  should verify
- no unresolved choice that could materially change delivered behavior

Use user stories only when actors or distinct observable journeys are clearer
that way. Prefer stable modules and contracts over file paths or code snippets.
Include a decision-rich prototype fragment only when prose would lose the
decision it encodes.

If repository evidence materially conflicts with the confirmed understanding,
surface the evidence and required user decision before continuing.

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

Perform one author preflight against the completion criteria above. Then create
one clean, read-only planning reviewer and read
`../review/planning-review.md`. The first round reviews `SPEC.md`, `TASKMAP.md`,
and every task file together. Continue later rounds with that same reviewer and
only the prior findings, resulting edits, and affected surfaces.

The planning limit is three total reviewer rounds unless the user sets or
extends another limit. Each reviewer attempt consumes one round. Assess every
finding against the conversation, repository, and plan; make the narrowest
evidence-backed correction. A material spec change requires reconciliation of
the task map and affected task files.

The review passes only on `Findings: none`. If blocking findings remain at the
limit, ask whether to extend it. Do not substitute another reviewer or proceed
with a plan that has not passed.

Record reviewer identity, round count, and result in `TASKMAP.md`.

## 5. Finalize the plan

After planning review passes, follow the selected plan checkpoint.

For `automatic`, record `Plan checkpoint: automatic` and its basis—the
confirmed `$grill-me` understanding and passing planning review—in
`TASKMAP.md`, set its status to `planned`, send a non-blocking progress update
with links to `SPEC.md` and `TASKMAP.md`, and continue without asking for
approval.

For `human-review`, give the user:

- links to `SPEC.md` and `TASKMAP.md`
- a concise task sequence
- every significant decision, its impact, and what the user should verify
- planning-review rounds and result

Ask for explicit approval. Apply requested changes and re-review with the same
reviewer when they materially affect requirements, decisions, coverage,
sequencing, or validation.

After approval, record `Plan checkpoint: human-review` and the approval basis
in `TASKMAP.md`, and set its status to `planned`.

For either checkpoint, validate the plan links and task graph, then commit the
exact active plan tree without staging unrelated changes. Stop before
implementation if the plan commit fails.

Planning is complete when the current plan exists in git history and the
worktree contains that committed version.
