# Planning

Use this instruction when creating or revising persistent planning artifacts.

Persistent planning has three ordered stages. Complete each stage before
progressing to the next. When revising an existing plan, begin at the earliest
stage affected by the change and reconcile every affected later stage. Apply
the same stage boundaries when repository convention uses different files or
sections than the default plan tree.

## Stage 1: Requirements Baseline

In the default plan tree, use `00-requirements.md` to define what the work must
accomplish independently of the implementation design. Record the intended
outcomes, scope boundaries, constraints, acceptance criteria, and unresolved
questions.

The requirements baseline is complete when:

- intended outcomes, in-scope work, and out-of-scope boundaries are explicit
- material constraints and acceptance criteria are checkable
- evidence-answerable questions have been resolved
- no blocking requirements question remains open
- user decisions and material assumptions are recorded

## Stage 2: Implementation Design

In the default plan tree, use `10-implementation-plan.md` to define how the
requirements baseline will be satisfied. Record the chosen approach, affected
components and contracts, risks, dependencies, sequencing, and validation
strategy.

The implementation design is complete when:

- every requirement is addressed by the design
- material assumptions, risks, dependencies, and compatibility concerns are
  explicit
- the intended validation demonstrates the requirements and acceptance
  criteria
- no unresolved design question blocks task breakdown

## Stage 3: Detailed Task Breakdown

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

## Procedure

1. Read local instructions and active planning conventions.
2. Check worktree state before editing.
3. Identify the active planning stage and gather only enough code and
   repository context to complete it.
4. Resolve evidence-answerable questions yourself.
5. Ask one user question at a time only for true blockers.
6. Complete the requirements baseline gate.
7. Complete the implementation design gate.
8. Complete the detailed task breakdown gate.
9. Validate planning artifacts when they are structured files.
10. Run the built-in iterative plan review loop after all three stage gates are
    complete and before asking the user to review the plan.
11. Apply valid or partially valid review findings to the earliest affected
    stage, reconcile later stages, and revalidate edited artifacts. Reject
    invalid findings with evidence.
12. If the user requested review, pause after the review loop and ask for
    review before implementation.

## Open Questions

Track open questions only when real uncertainty remains after repository
inspection.

For persistent plan trees, use stable `Q-*` IDs and record:

- status (`open` or `resolved`)
- question
- context
- options and tradeoffs
- recommended default
- user decision when resolved
- artifacts updated

Do not finalize a reviewable plan while a blocking question is still open.
Non-blocking assumptions may remain if they are labeled and have a recommended
default.

## Plan Changes

When scope, sequencing, risk, or validation expectations change:

- update the active planning state in the same iteration if one exists
- keep the old decision visible only when it matters for audit or future review
- avoid long decision logs for routine implementation discoveries
