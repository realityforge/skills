# Implementation Review

Use this instruction after implementation is complete and before final success
reporting when active plan artifacts exist.

## Post-Implementation Issues

Do not open an issue register for every follow-up.

Use a persistent issue register only when:

- a persistent plan tree is active
- the issue changes accepted scope or sequencing
- the issue needs user approval before implementation
- multiple related follow-ups must be tracked across turns

Otherwise, fix the issue within the current scope, validate it, and summarize
the evidence.

For tracked issues, include:

- stable issue ID
- status (`open`, `planned`, `resolved`, or `deferred`)
- context and evidence
- proposed response
- validation expectation
- linked task IDs, if any

Ask for explicit approval before editing implementation files only when the
response changes accepted scope, has meaningful product/design tradeoffs, or
the user requested approval-first handling.

## Requirements-First Implementation Review

After implementation is complete and before final success reporting, run the
built-in iterative requirements-first implementation review when there are
active plan artifacts to compare against the implementation.

Review in this order:

1. requirements outcomes: the implementation satisfies the reviewed
   requirements and acceptance criteria
2. design validity: implementation discoveries have not invalidated the chosen
   design or exposed a materially simpler approach
3. delivery alignment: implementation, tasks, and validation evidence agree
   with the current reviewed design

Failure at an earlier level cannot be compensated for by alignment at a later
level. Requirements remain authoritative for accepted scope; implementation
design and task state explain how the requirements are being delivered and may
need revision when implementation produces better evidence.

This normally applies to persistent plan tree work. For lightweight
implementation, run it only when the work was explicitly driven by an existing
plan artifact; otherwise rely on the normal closeout validation because there
is no plan artifact to review against.

Defaults:

- max rounds: `5`, unless the user gives another limit
- reviewer: clean read-only subagent using the review rubric below
- main agent owns fixes, validation, evidence updates, and final reporting

Before spawning, resolve the repository root, plan artifacts, implementation
scope, review mode, required gates, and round limit. Infer these from context
when safe; ask only if the review target is genuinely ambiguous.

Use `delta` mode when the request is a follow-up round, names prior findings,
or says only specific fixes changed. Use `full` mode otherwise.

Use focused inputs:

- requirements baseline, implementation design, and task-board paths
- repository or workspace root
- review mode: `full` or `delta`
- maximum review rounds, defaulting to `5` unless the user set one
- current implementation scope, such as uncommitted changes, recent commits, or
  specific files
- relevant prior findings for delta rounds
- required validation gates from the plan, when available

For each round:

1. Send the subagent a focused read-only prompt: repository root, requirements,
   design and task paths, implementation scope, relevant prior findings,
   required gates, review order, and the rubric below. Ask for `Findings` and a
   `Scorecard` only when full mode or merge/release gating needs it. Do not pass
   full conversation context unless necessary.
2. Assess each finding against repository evidence.
3. Fix valid or partially valid findings with the narrowest requirements,
   design, task, implementation, test, or evidence change at the earliest
   affected level. Reject only with concrete evidence.
4. Run targeted validation for changed behavior. Run the plan's full gate
   before final success, or explain why it could not be run.
5. Update requirements, design, task-board, or evidence artifacts only when
   accepted scope, actual design, task state, or validation evidence changed.
6. Re-review unless the subagent reports `Findings: none`, no actionable
   findings remain after assessment, or max rounds is reached.

When implementation evidence invalidates the recorded design or exposes a
simpler path that still satisfies the requirements, revise the design and task
state rather than preserving obsolete alignment. Obtain user approval before
changing accepted scope or choosing a materially different product or design
trade-off.

Do not weaken requirements to match incomplete implementation. Preserve
unrelated user changes. Do not commit unless asked.

Final report should include rounds run, final review result,
fixes/rejections/leftovers, validation results, evidence updates, and subagent
closure.

## Review Rubric

Judge the implementation in three passes: requirements outcomes, design
validity, then delivery alignment. Be strict, evidence-backed, and concise.

Identify the review scope first: plan paths, repository root, diff or commit
range, implementation scope, and whether the round is `full` or `delta`.

Evidence order:

1. Inspect `git status` and changed-file shape first.
2. Read the requirements needed to extract accepted outcomes, constraints, and
   acceptance criteria.
3. Map requirements to current behavior, changed files, tests, and recorded
   evidence.
4. Read the implementation design and test its load-bearing assumptions against
   what implementation revealed.
5. Compare the resulting design to task state and delivery evidence.
6. Read implementation files only where they prove or disprove a requirement,
   design claim, or task claim.
7. Inspect recent commits only when named, the working tree is clean, or
   history is needed to explain the delivered state.
8. Treat plan entries and summaries as claims. Verify the underlying code,
   tests, or command evidence before relying on them.

In full mode, complete all three review passes against current repository
state.

In delta mode, verify the named prior findings, changed files, and any new
drift introduced by the fix. Do not re-review the whole plan unless the diff
changed broadly.

### Pass 1: Requirements Outcomes

Report:

- accepted behavior, constraints, or scope missing or only partially delivered
- implementation behavior that contradicts a requirement
- unplanned behavior or API changes that alter accepted scope
- acceptance criteria without convincing implementation or validation evidence
- code that exists but is disconnected, dead, stubbed, or superficially tested

### Pass 2: Design Validity

Report:

- implementation evidence that disproves a load-bearing design assumption
- a materially simpler direct approach exposed by implementation discoveries
- indirection, compatibility paths, or abstractions whose justification no
  longer holds
- new interface, data, migration, operational, failure, or rollback concerns
  absent from the design
- implementation choices that satisfy requirements but represent an unrecorded
  material trade-off

### Pass 3: Delivery Alignment

Report:

- required design work missing or partial
- implementation that deviates from the still-valid reviewed design without
  evidence that the deviation is preferable
- tasks, dependencies, status, or evidence that no longer describe delivered
  work
- tests or validation promised but absent, weak, stale, or not wired into gates
- evidence claims that overstate what was checked
- prior-review fixes that do not actually close the prior finding

A requirements-satisfying improvement over the recorded design requires design
and task reconciliation, not a finding that the implementation must regress to
the old plan.

Do not report harmless wording drift, accepted plan changes, or minor style
issues unless they affect alignment or safety.

Prefer decisive evidence over exhaustive reading. For large reviews, stop after
the highest-risk actionable findings unless exhaustive coverage was requested.
Do not rerun heavy validation in a read-only review unless current evidence is
missing or suspicious. Cheap non-mutating checks are fine.

Start with `Findings`.

Use compact bullets:

- `[P1] Short title. Evidence: file/line or command result. Why it matters.
  Fix: concrete next step.`

If there are no findings:

`Findings: none. Checked: <short evidence list>. Residual risk: <none or
specific unverified gate>.`

Include a scorecard only when requested, the review is full mode, or the result
will gate merge or release.
