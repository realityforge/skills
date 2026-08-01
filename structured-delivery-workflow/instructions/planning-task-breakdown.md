# Stage 3: Detailed Task Breakdown

Use this instruction after the implementation design passes review and task
ownership, execution order, or task-level validation is absent or affected.

In the default plan tree, use `20-task-board.yaml` to turn the implementation
design into ordered, executable work. Each task should identify its
dependencies, acceptance criteria, touched files or patterns, and validation
expectations.

The task breakdown is complete when:

- every implementation-design obligation belongs to a task
- dependencies and execution order are coherent
- every task is independently verifiable at a useful implementation boundary
- no required work is unowned or represented only in prose outside the task
  board

After the completion gate, validate structured artifacts, then read
`review-and-approval.md`. Run the built-in task review when its branch applies;
otherwise perform its local coverage check.
