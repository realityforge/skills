# Review And Approval

Use this instruction before asking the user to review a persistent plan or before
marking a plan accepted.

## Plan Review Loop

Before asking the user to review a persistent plan tree, run a clean read-only
review subagent with the review rubric below, then assess and fix valid
findings. Default max rounds: `5`, unless the user says otherwise. Infer the
active plan path; ask only when it cannot be inferred.

Do not run this review loop for lightweight implementation.

For each round:

1. Spawn or reuse one clean read-only review subagent.
2. Pass only plan artifact paths, repository root, and focused context paths.
   Do not fork full conversation context unless necessary.
3. Include the review rubric below and ask for `Findings` and `Scorecard`;
   `Findings: none` means stop.
4. Assess findings against repository, plan, and user evidence. Accept unless
   contradicted; narrow over-broad fixes.
5. Patch accepted or partially accepted plan issues. Do not patch rejected
   findings.
6. Validate edited structured artifacts where practical.
7. Re-review only after material plan edits and only until no actionable
   findings remain or max rounds is reached.

Use focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to `5` unless the user set one
- known context files the reviewer needs

Pass paths, repository root, and concise scope/context. Do not paste full plan
contents unless the files are unavailable to the reviewer.

Keep plan updates scoped to the reviewed plan tree unless the user approves
broader changes. Preserve stable task IDs and question IDs. If plan status is
`accepted`, do not mark it back to draft unless the change reopens decisions or
scope.

User-facing output should be one terse digest per round. Detail only rejected
findings, unresolved user decisions, blockers, and validation failures. Final
report should include rounds run, final status, material fixes, validations,
and remaining issues, if any.

## Review Rubric

Stress-test whether the plan is specific enough to implement safely.

Read the plan first. Inspect referenced repository or system context only when
needed to verify a material assumption, contract, dependency, or validation
claim. Do not bulk-load context or restate the plan.

Find issues that would block implementation, create avoidable risk, or leave a
critical decision to the implementer. Ignore cosmetic gaps and ordinary
implementation discretion.

Check the relevant risk surface: scope, success criteria, interfaces and
contracts, data and state changes, migrations, sequencing, failure and rollback
behavior, validation, rollout and operations, and external dependencies.

Start with `Findings`.

For each finding, include:

- the risk or ambiguity
- why it matters
- the concrete plan change needed

Use evidence when repository or context inspection affected the finding. Order
findings by implementation risk. Keep wording dense and skip praise.

If there are no material issues, write `Findings: none` and mention only
residual risk or unchecked context that matters.

Do not rewrite the plan unless asked.

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
the review passes, treat that as conditional approval once the review loop has
no remaining actionable findings.
