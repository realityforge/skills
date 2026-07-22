# Review And Approval

Use this instruction after completing each persistent planning stage, before
asking the user to review a persistent plan, or before marking a plan accepted.

## Stage Review Loops

Review each persistent planning stage after its completion gate and before the
next stage begins:

1. requirements baseline against its accepted source and repository evidence
2. implementation design against the reviewed requirements baseline
3. detailed task breakdown against the reviewed implementation design

Default max rounds: `5` across the full planning sequence, unless the user gives
another limit. Each stage's initial review consumes one round. Infer the active
plan path; ask only when it cannot be inferred.

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

A stage passes when its review has no actionable findings. A stage pass permits
progress to the next planning stage; it does not by itself mark the complete
plan as accepted.

A stalled or unusable reviewer attempt consumes one review round. Replace it
once with a narrower prompt and focused evidence paths. If no usable review
completes within the round limit, the stage has not passed; report the missing
review evidence instead of claiming success.

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

## Stage Rubric Router

Load only the rubric for the current stage:

- requirements baseline: `review-requirements.md`
- implementation design: `review-implementation-design.md`
- detailed task breakdown: `review-task-breakdown.md`

Include the selected rubric and the common output contract below in the review
prompt.

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

## Plan Acceptance

Require explicit user review before marking a plan `accepted` only when:

- the user asked to pause for review
- the plan will guide another thread/agent
- implementation must not begin without user approval
- a stage review exposes a material scope or design choice that evidence cannot
  resolve

Capture approval either in `20-task-board.yaml` or the planning document.

If the user says to proceed, treat that as approval for the current scope and
record it if persistent planning state exists.

If the user already instructed implementation to follow planning or review,
treat that as conditional approval once all required stage reviews have no
remaining actionable findings and no material scope or design choice was
reopened.
