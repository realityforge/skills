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

## Implementation Alignment Review

After implementation is complete and before final success reporting, run the
built-in iterative `plan-implementation-review` loop when there is an active
plan artifact to compare against the implementation.

This normally applies to persistent plan tree work. For lightweight
implementation, run it only when the work was explicitly driven by an existing
plan artifact; otherwise rely on the normal closeout validation because there
is no plan artifact to review against.

Defaults:

- max rounds: `5`, unless the user gives another limit
- reviewer: clean subagent using `plan-implementation-review`
- main agent owns fixes, validation, evidence updates, and final reporting

Before spawning, resolve the repository root, plan artifacts, implementation
scope, required gates, and round limit. Infer these from context when safe; ask
only if the review target is genuinely ambiguous.

Use focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to `5` unless the user set one
- current implementation scope, such as uncommitted changes, recent commits, or
  specific files
- required validation gates from the plan, when available

For each round:

1. Send the subagent a focused read-only prompt: repository root, plan paths,
   implementation scope, relevant prior findings, required gates, and
   `Findings`/`Scorecard` output. Do not pass full conversation context unless
   necessary.
2. Assess each finding against repository evidence.
3. Fix valid or partially valid findings with the narrowest implementation,
   test, or evidence change. Reject only with concrete evidence.
4. Run targeted validation for changed behavior. Run the plan's full gate
   before final success, or explain why it could not be run.
5. Update plan/task-board/evidence artifacts only when status, scope, or
   validation evidence changed.
6. Re-review unless the subagent reports `Findings: none`, no actionable
   findings remain after assessment, or max rounds is reached.

Do not weaken the plan to match incomplete implementation. Preserve unrelated
user changes. Do not commit unless asked.

Final report should include rounds run, final review result,
fixes/rejections/leftovers, validation results, evidence updates, and subagent
closure.
