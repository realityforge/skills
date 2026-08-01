# Planning

Use this instruction when creating or revising persistent planning artifacts.

Persistent planning has three ordered stages. Begin at the earliest stage
affected by the work and complete its gate and review before loading the next
stage. Reconcile every affected later stage when revising an existing plan.
Apply the same stage boundaries when repository convention uses different
files or sections than the default plan tree.

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

## Stage Router

Read only the instruction for the active stage:

- requirements are absent, changed, or contradicted by evidence: read
  `planning-requirements.md`
- reviewed requirements exist and implementation design is absent or affected:
  read `planning-implementation-design.md`
- reviewed implementation design exists and task ownership, execution order,
  or task-level validation is absent or affected: read
  `planning-task-breakdown.md`

## Procedure

1. Read local instructions and active planning conventions.
2. Check worktree state before editing.
3. Identify the active planning stage, read its routed instruction, and gather
   only enough code and repository context to complete it.
4. Resolve evidence-answerable questions yourself.
5. Ask one user question at a time only for true blockers.
6. Complete the active stage gate and its review transition.
7. Load the next stage instruction only after the current stage passes and
   another stage is required.
8. When a finding changes an earlier stage, reconcile every later artifact and
   re-review only stages whose obligations or validation risk materially
   changed.
9. After all required stage reviews pass, complete the plan-acceptance step in
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
