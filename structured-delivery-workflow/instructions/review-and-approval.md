# Review And Approval

Use this instruction after completing each persistent planning stage, before
asking the user to review a persistent plan, or before marking a plan accepted.

## Stage Review Loops

Review each persistent planning stage after its completion gate and before the
next stage begins, subject to the task-review branch below:

1. requirements baseline against its accepted source and repository evidence
2. implementation design against the reviewed requirements baseline
3. detailed task breakdown against the reviewed implementation design

Requirements and implementation-design reviews are required. Run the detailed
task review only when one or more apply:

- the plan guides another thread, agent, or parallel work
- migration, rollout, destructive, or irreversible sequencing is involved
- incorrect dependency or ownership boundaries could create expensive rework
- the task validation cannot be exercised cheaply during implementation

Otherwise validate the structured artifact and locally confirm that every
reviewed design obligation has an owner and an independently verifiable
implementation boundary. The task stage can pass without a review subagent.

Default max rounds: `5` for each stage. A user-supplied limit applies to each
stage unless the user scopes it to a specific stage. Each initial review and
re-review consumes one round from the current stage; unused rounds do not
transfer. If an upstream change reopens a passed stage, resume that stage's
existing round count. Infer the active plan path; ask only when it cannot be
inferred.

For each stage:

1. Run one author preflight against the stage completion criteria and matching
   rubric. Patch evident omissions, contradictions, and unsupported claims;
   stop after this pass rather than searching for refinements. This preflight
   is not a review round.
2. Spawn one clean read-only review subagent; reuse it only for additional
   rounds of the same stage.
3. Pass the current stage artifact, its reviewed upstream artifacts, repository
   root, focused evidence paths, the current stage's remaining round limit, and
   the matching rubric below. Do not pass downstream artifacts or full
   conversation context unless needed.
4. Ask for findings classified as `Block` or `Carry`; `Findings: none` means
   the stage review passes.
5. Assess each finding against repository, plan, and user evidence and the
   materiality gate below. Accept a blocking finding only when evidence supports
   its pre-implementation risk; otherwise carry or reject it. Narrow over-broad
   fixes.
6. Patch accepted or partially accepted blocking issues in the earliest
   affected stage. Carry implementation-local findings into the relevant later
   stage or task without failing the current stage or triggering re-review. Do
   not patch rejected findings.
7. Reconcile downstream artifacts already present and validate edited
   structured files where practical.
8. Re-review after material stage edits until no blocking findings remain or
   the current stage's round limit is reached.

Treat every additional round for the same stage as a focused confirmation, not
a new broad review. Pass the prior blocking findings, their dispositions, the
resulting edits, and directly affected context. Verify that each block is
resolved and that the edits introduced no contradiction on the affected risk
surface. Do not reopen unaffected parts of the stage. A newly observed issue in
a confirmation round blocks only when the edits introduced or exposed it and it
meets the materiality gate; otherwise carry or reject it.

If a blocking finding invalidates an upstream stage, return to that stage and
apply its rubric. Reconcile every downstream artifact, but re-review only a
stage whose requirement coverage, design obligations, sequencing, or validation
risk changed. Evidence citations, wording clarifications, and bookkeeping edits
do not by themselves reopen downstream reviews. Charge each review to the stage
whose rubric it applies.

A stage passes when its review has no blocking findings. A stage pass permits
progress to the next planning stage; it does not by itself mark the complete
plan as accepted.

A stalled or unusable reviewer attempt consumes one round from the current
stage. Replace it once with a narrower prompt and focused evidence paths. If no
usable review completes within that stage's limit, the stage has not passed;
report the missing review evidence instead of claiming success.

If a stage reaches its limit with blocking findings or required re-review
remaining, report the unresolved evidence and ask whether to extend that
stage's limit. Later stages retain their full budgets.

Use focused inputs:

- current stage artifact path
- reviewed upstream artifact paths
- requirements source or accepted shared-understanding summary when reviewing
  requirements
- repository or workspace root
- known evidence and context paths needed for the matching rubric
- current-stage round count and limit

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

Apply this materiality gate:

- `Block`: leaving the issue unresolved before implementation could cause
  incorrect requirements or delivered behavior, architectural or irreversible
  rework, unsafe migration or rollout, cross-task coordination failure, or
  validation that can falsely pass.
- `Carry`: a local, reversible implementation detail that required
  implementation checks can expose cheaply. Assign it to the relevant later
  stage or task; it does not fail the reviewed stage.
- Reject cosmetic, speculative, unsupported, or out-of-scope suggestions.

For each finding, include:

- its `Block` or `Carry` classification
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
remaining blocking findings and no material scope or design choice was
reopened.
