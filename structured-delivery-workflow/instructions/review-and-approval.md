# Review And Approval

Use this instruction after completing each persistent planning stage, before
asking the user to review a persistent plan, or before marking a plan accepted.

## Stage Review Loops

Review each persistent planning stage after its completion gate and before the
next stage begins:

1. requirements baseline against its accepted source and repository evidence
2. implementation design against the reviewed requirements baseline
3. detailed task breakdown against the reviewed implementation design

Do not run these reviews for lightweight implementation. Default max rounds:
`5` across the full planning sequence, unless the user gives another limit.
Each stage's initial review consumes one round. Infer the active plan path; ask
only when it cannot be inferred.

For each stage:

1. Spawn one clean read-only review subagent; reuse it only for additional
   rounds of the same stage.
2. Pass the current stage artifact, its reviewed upstream artifacts, repository
   root, focused evidence paths, remaining round limit, and the matching rubric
   below. Do not pass downstream artifacts or full conversation context unless
   needed.
3. Ask for `Findings` and a compact `Scorecard`; `Findings: none` means the
   stage review passes.
4. Assess each finding against repository, plan, and user evidence. Accept
   unless contradicted; narrow over-broad fixes.
5. Patch accepted or partially accepted issues in the earliest affected stage.
   Reject findings only with concrete evidence.
6. Reconcile downstream artifacts already present and validate edited
   structured files where practical.
7. Re-review after material stage edits until no actionable findings remain or
   the planning-sequence round limit is reached.

If a finding invalidates an upstream stage, return to that stage, apply its
rubric, and rerun every affected downstream review before progressing.

Use focused inputs:

- current stage artifact path
- reviewed upstream artifact paths
- requirements source or accepted shared-understanding summary when reviewing
  requirements
- repository or workspace root
- known evidence and context paths needed for the matching rubric
- maximum review rounds for the planning sequence, defaulting to `5` unless the
  user set one

Pass paths and concise context. Paste artifact contents only when files are
unavailable to the reviewer. Keep updates scoped to the active plan tree unless
the user approves broader changes. Preserve stable task IDs and question IDs.
If plan status is `accepted`, preserve it unless an earlier-stage change
reopens scope or a user decision.

User-facing output should be one terse digest per round. Detail only rejected
findings, unresolved user decisions, blockers, and validation failures. Final
report should include each stage's rounds, status, material fixes,
validations, and remaining issues, if any.

## Requirements Review Rubric

Judge whether the requirements baseline accurately captures what must be true.

Check:

- alignment with the accepted request, shared understanding, issue, or
  specification
- complete outcomes, scope boundaries, constraints, and checkable acceptance
  criteria
- ambiguity, contradiction, or an unstated product or design decision that
  would change delivered behavior
- factual claims that conflict with repository evidence
- implementation choices presented as requirements without being mandated

Inspect repository context only where it can confirm or contradict a material
requirement. Report the requirement change or user decision needed; do not
invent missing product choices.

## Implementation Design Review Rubric

Judge whether the design is the simplest evidence-backed way to satisfy the
reviewed requirements baseline.

Check:

- every requirement has a concrete design response
- the approach is feasible in the actual repository and system
- simpler direct approaches were assessed before adding indirection,
  compatibility paths, or abstractions
- load-bearing assumptions and capability limits have supporting evidence
- interfaces, contracts, data and state changes, migrations, dependencies,
  failure behavior, rollback, rollout, and operations are addressed where
  relevant
- validation will demonstrate the requirements and acceptance criteria
- material alternatives and trade-offs explain the chosen design where needed

Challenge unsupported claims that a direct approach cannot work. Keep task
granularity and bookkeeping out of this review unless they expose a design gap.

## Detailed Task Review Rubric

Judge whether the task breakdown completely and safely executes the reviewed
implementation design.

Check:

- every design obligation belongs to a task
- dependencies and execution order are coherent
- tasks use independently verifiable implementation boundaries
- acceptance criteria and validation expectations prove each task's obligation
- touched files or patterns are sufficient to locate the work
- cross-cutting tests, documentation, migration, rollout, and cleanup work are
  owned rather than left in plan prose

Treat the reviewed design as the baseline. Report an upstream finding only
when task decomposition exposes a real requirements or design contradiction.

## Review Output

Start with `Findings`.

For each finding, include:

- the risk or ambiguity
- why it matters
- the concrete change needed in the affected stage

Use evidence when repository or context inspection affected the finding. Order
findings by implementation risk. Keep wording dense and skip praise.

If there are no material issues, write `Findings: none` and mention only
residual risk or unchecked context that matters. Do not rewrite artifacts
unless asked.

## User Approval

Require explicit user review before marking a plan `accepted` only when:

- the user asked to pause for review
- the plan will guide another thread/agent
- a persistent plan tree is being used
- implementation must not begin without user approval

Capture approval either in `20-task-board.yaml` or the planning document.

If the user says to proceed, treat that as approval for the current scope and
record it if persistent planning state exists.

If the user requested a plan review and also instructed you to implement after
the review passes, treat that as conditional approval once all required stage
reviews have no remaining actionable findings.
