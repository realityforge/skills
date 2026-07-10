# Implementation Review

Use this reference after implementation is complete and before final success
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

After implementation is complete and before final success reporting, invoke
`iterative-plan-implementation-review` when there is an active plan artifact to
compare against the implementation.

This normally applies to persistent plan tree work. For lightweight
implementation, run it only when the work was explicitly driven by an existing
plan artifact; otherwise rely on the normal closeout validation because there
is no plan artifact to review against.

Invoke `iterative-plan-implementation-review` with focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to that skill's default unless the user set
  one
- current implementation scope, such as uncommitted changes, recent commits, or
  specific files
- required validation gates from the plan, when available

Apply valid or partially valid findings, reject invalid findings with evidence,
run the required validation for fixes, and update plan/task-board/evidence
artifacts when findings affect task status, validation evidence, or scope.
