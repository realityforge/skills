# Review And Approval

Use this reference before asking the user to review a persistent plan or before
marking a plan accepted.

## Plan Review Hook

Before asking the user to review a persistent plan tree, invoke
`iterative-plan-review` with focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to that skill's default unless the user set
  one
- known context files the reviewer needs

Pass paths, repository root, and concise scope/context. Do not paste full plan
contents unless the files are unavailable to the reviewer.

Do not run this review hook for lightweight implementation.

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
