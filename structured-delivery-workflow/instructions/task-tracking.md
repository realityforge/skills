# Task Tracking

Use this instruction when updating implementation state or task boards.

- Use `20-task-board.yaml`.
- Include `id`, `title`, `status`, `priority`, `depends_on`, acceptance
  criteria, requirement links, touched files or patterns, validation
  expectations, and evidence.
- Keep one task `in_progress` at a time.
- Mark tasks complete immediately after required checks pass.
- Add commit metadata only when the user requested commit traceability or the
  repository convention requires it.
- Record real hashes only after commits exist; do not leave stale
  `commit.hash: pending` values.
- Use `not_required` only when commit metadata is required for the task and no
  commit is expected.

If task state changes because implementation discovers a scope, sequencing, or
validation issue, update the active planning state in the same iteration.
