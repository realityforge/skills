# Planning

Use this instruction when creating or revising persistent planning artifacts.

Persistent planning has three ordered stages. Complete each stage before
progressing to the next. When revising an existing plan, begin at the earliest
stage affected by the change and reconcile every affected later stage. Apply
the same stage boundaries when repository convention uses different files or
sections than the default plan tree.

## Default Plan Artifacts

Use existing repository conventions when present. Otherwise use:

```
plans/<initiative>/
  00-requirements.md
  10-implementation-plan.md
  20-task-board.yaml
```

Create optional artifacts only when their branch applies:

- `01-*-deep-dive.md` for focused requirements that would overload the baseline
- `30-compatibility-matrix.md` for parity or migration work
- `30-output-contract.md` for CLI or API output contracts
- `40-test-strategy.md` for complex or multi-environment validation
- `50-implementation-issues.md` after follow-up issues require persistent state

Load a template only when creating its corresponding artifact:

- `templates/requirements.md`
- `templates/requirements-deep-dive.md`
- `templates/implementation-plan.md`
- `templates/task-board.yaml`

## Stage 1: Requirements Baseline

In the default plan tree, use `00-requirements.md` to define what the work must
accomplish independently of the implementation design. Record the intended
outcomes, scope boundaries, constraints, acceptance criteria, and unresolved
questions.

### Requirements Entry Path

Start from the strongest available requirements baseline.

Use the **pre-aligned path** when the user has already confirmed shared
understanding, including through `grill-me`, or has directed the work from an
accepted specification or requirements artifact:

- record the source and basis of acceptance
- preserve settled outcomes, constraints, and decisions
- check them against current repository evidence
- reopen a settled point only when evidence contradicts it, scope has changed,
  or its acceptance criteria cannot be evaluated

Use the **evidence-led path** when no accepted baseline exists:

- derive candidate requirements from the request, repository instructions,
  referenced issues or specifications, current behavior, code, and tests
- resolve factual questions from evidence before asking the user
- treat a clear original request as acceptance when it leaves no material
  requirements choice open
- when a material choice remains, present the evidence, recommendation, and
  decision needed before completing the baseline

If evidence contradicts a pre-aligned requirement, surface the conflict and
resolve it before progressing to implementation design.

The requirements baseline is complete when:

- its source and basis of acceptance are recorded
- intended outcomes, in-scope work, and out-of-scope boundaries are explicit
- material constraints and acceptance criteria are checkable
- evidence-answerable questions have been resolved
- no blocking requirements question remains open
- user decisions and material assumptions are recorded
- it states required outcomes rather than implementation choices, except where
  the implementation itself is a requirement or constraint

## Stage 2: Implementation Design

In the default plan tree, use `10-implementation-plan.md` to define how the
requirements baseline will be satisfied. Record the chosen approach, affected
components and contracts, risks, dependencies, sequencing, and validation
strategy.

### Derive the Design

Derive the implementation design from the requirements baseline rather than
restating the requirements as tasks:

- map each requirement, or coherent group of requirements, to the design
  response that satisfies it
- start with the simplest direct design that could satisfy the baseline; add
  indirection, compatibility paths, or new abstractions only when their need is
  supported by evidence
- identify load-bearing assumptions whose failure would materially change the
  architecture, scope, sequencing, or validation strategy
- verify each load-bearing assumption through code, authoritative
  documentation, or a focused experiment before relying on it
- test consequential capability claims, especially that a direct approach
  cannot work, against the actual system rather than inference alone
- record credible alternatives and trade-offs only when they explain why the
  chosen design is preferable or prevent likely rediscovery

Keep requirement outcomes authoritative. If design investigation contradicts
the requirements baseline, return to Stage 1 and resolve the conflict before
continuing.

The implementation design is complete when:

- every requirement maps to a design response
- the simplest direct approach has been assessed and any added indirection or
  abstraction is justified
- every load-bearing assumption has supporting evidence
- material assumptions, risks, dependencies, and compatibility concerns are
  explicit
- material alternatives and trade-offs are recorded when their rationale will
  matter during implementation or future reconsideration
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
4. When requirements are affected, select the pre-aligned or evidence-led
   requirements path.
5. Resolve evidence-answerable questions yourself.
6. Ask one user question at a time only for true blockers.
7. Complete the requirements baseline gate, then run the built-in requirements
   review before starting implementation design.
8. Complete the implementation design gate, then run the built-in design
   review before creating the detailed task breakdown.
9. Complete the detailed task breakdown gate, validate structured artifacts,
   then run the built-in task review.
10. When a finding changes an earlier stage, reconcile every later artifact and
    re-review only stages whose obligations or validation risk materially
    changed.
11. After all stage reviews pass, complete the plan-acceptance step in
    `review-and-approval.md` before implementation.

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
