# Existing Plan Implementation

Use this instruction when implementing from an already accepted persistent plan.

Inspect local instructions and worktree state before loading or editing the
active plan.

## Context Loading

Use `20-task-board.yaml` as the index into the plan before loading every
artifact.

Read first:

- current plan status, `current_focus`, active tasks, and blocked tasks
- the target task's acceptance criteria, dependencies, touched files or
  patterns, and validation expectations
- linked or directly relevant sections of `00-requirements.md`,
  `10-implementation-plan.md`, and optional artifacts

Read all plan artifacts only when:

- performing planning-stage review or requirements-first implementation review
- active task scope, sequencing, dependencies, or validation gates are unclear
- task-board state conflicts with requirements, implementation plan, or repo
  state
- the task board does not point to enough requirement or validation detail
- cross-cutting migration, safety, parity, or architecture constraints could be
  missed by reading only task-local context

If task-board indexing is weak, fix the active planning state or read the
missing plan context before editing implementation files.

## Implementation Loop

For each implementation slice:

1. Confirm current scope and relevant files.
2. Make the smallest coherent change.
3. Run targeted checks while iterating.
4. Run the required validation gate before marking the slice done.
5. Update persistent planning state only if the selected mode uses it or the
   plan changed.
6. Commit only when the user asked for commits or repository instructions
   require them.

Before a command mutates external state such as a database, deployment,
service, or remote resource, resolve the exact target and environment from
evidence and identify the recovery or cleanup path. Use that same explicit
target for validation and cleanup.

Task sizing:

- Good: one behavior slice with its tests/docs/process updates.
- Too broad: a whole subsystem rewrite.
- Too narrow: isolated trivial edits that cannot be validated independently.
