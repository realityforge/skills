---
name: structured-delivery-workflow
description: Run a context-efficient engineering workflow with right-sized planning, task tracking, validation evidence, and optional review/commit traceability. Use when work spans multiple files, has process risk, needs a reviewable plan, or must preserve progress across threads.
license: Apache-2.0
compatibility: Works best in repositories that allow markdown/yaml planning artifacts and test/build execution.
metadata:
  author: realityforge
  version: "2.3"
---

# Structured Delivery Workflow

Use this skill to keep engineering work explicit without turning process state into the work.
Start with the smallest durable state that preserves decisions, sequencing, and validation
evidence. Escalate only when the request or risk justifies the extra artifacts.

## Core Rules

- Inspect local instructions, repository state, and relevant code before planning or editing.
- Prefer existing repository planning conventions. Do not invent a new layout when one exists.
- Ask the user only for decisions that cannot be answered from evidence and materially affect scope, behavior, risk, or review.
- Keep one active implementation focus at a time.
- Record validation evidence before claiming completion.
- Do not modify unrelated `plans/` trees. Identify the active plan before editing any file under `plans/`.
- Do not create persistent artifacts just to satisfy process. Create them when they will be reviewed, resumed, delegated, audited, or used during implementation.

## Workflow Modes

Choose the lightest mode that fits the request. If unsure, start lighter and
escalate when evidence shows the work needs durable planning state.

### Tier 0: Lightweight Implementation

Use for bounded implementation work where the user did not ask for plan artifacts and the work can finish in the current thread.

State to keep in conversation:

- scope in one or two sentences
- short task checklist, if useful
- targeted and final validation commands
- final summary with files changed and verification results

Do not create `plans/` files for Tier 0.

### Full Plan Tree

Use when at least one is true:

- the user asks to create a plan, emit planning artifacts, or pause for review
- the user explicitly asks for full requirements, task board, traceability, or audit evidence
- work is multi-phase or expected to span multiple threads/days
- another agent will implement from the plan and needs machine-readable task state
- migration, data safety, architecture, compliance, or parity risk is high
- repository convention already requires the full tree

Default full tree:

```
plans/<initiative>/
  00-requirements.md
  10-implementation-plan.md
  20-task-board.yaml
  30-compatibility-matrix.md   # only for parity/migration work
  40-test-strategy.md          # only for complex validation
  50-implementation-issues.md  # only after real follow-up issues exist
```

Use the reference templates only when creating the corresponding files:

- Requirements deep dive template: `references/requirements-deep-dive-template.md`
- Implementation plan template: `references/implementation-plan-template.md`
- Task board template: `references/task-board-template.yaml`

## Planning Procedure

1. Read local instructions and active planning conventions.
2. Check worktree state before editing.
3. Select the workflow mode and say which mode you are using.
4. Gather only enough code/context to make the plan concrete.
5. Resolve evidence-answerable questions yourself.
6. Ask one user question at a time only for true blockers.
7. Write or update the selected planning state.
8. Validate planning artifacts when they are structured files.
9. For full plan trees, run `iterative-plan-review` after the plan is drafted
   and local context has been gathered, but before asking the user to review it.
10. Apply valid or partially valid review findings to the plan, reject invalid
    findings with evidence, and revalidate edited artifacts.
11. If the user requested review, pause after the review loop and ask for review
    before implementation.

## Open Questions

Track open questions only when real uncertainty remains after repository inspection.

For full plan trees, use stable `Q-*` IDs and record:

- status (`open` or `resolved`)
- question
- context
- options and tradeoffs
- recommended default
- user decision when resolved
- artifacts updated

Do not finalize a reviewable plan while a blocking question is still open. Non-blocking assumptions may remain if they are labeled and have a recommended default.

## Implementation Loop

For each implementation slice:

1. Confirm current scope and relevant files.
2. Make the smallest coherent change.
3. Run targeted checks while iterating.
4. Run the required validation gate before marking the slice done.
5. Update persistent planning state only if the selected mode uses it or the plan changed.
6. Commit only when the user asked for commits or repository instructions require them.

Task sizing:

- Good: one behavior slice with its tests/docs/process updates.
- Too broad: a whole subsystem rewrite.
- Too narrow: isolated trivial edits that cannot be validated independently.

## Task Tracking

Tier 0:

- Use conversation checklist or `update_plan` when useful.
- No persistent task board.

Full plan tree:

- Use `20-task-board.yaml`.
- Include `id`, `title`, `status`, `priority`, `depends_on`, acceptance criteria, touched files or patterns, and validation evidence.
- Keep one task `in_progress` at a time.
- Mark tasks complete immediately after required checks pass.
- Record commit metadata only when a commit was created or explicitly expected.
- Use `not_required` only when the task is complete and no commit is expected.

## Review and Approval

Before asking the user to review a full plan tree, invoke
`iterative-plan-review` with focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to that skill's default unless the user set one
- known context files the reviewer needs

Do not run this review hook for Tier 0.

Require explicit user review before marking a plan `accepted` only when:

- the user asked to pause for review
- the plan will guide another thread/agent
- a full plan tree is being used
- implementation must not begin without user approval

Capture approval either in `20-task-board.yaml` or the planning document.

If the user says to proceed, treat that as approval for the current scope and record it if persistent planning state exists.

## Plan Changes

When scope, sequencing, risk, or validation expectations change:

- update the active planning state in the same iteration if one exists
- keep the old decision visible only when it matters for audit or future review
- avoid long decision logs for routine implementation discoveries

## Post-Implementation Issues

Do not open an issue register for every follow-up.

Use a persistent issue register only when:

- a full plan tree is active
- the issue changes accepted scope or sequencing
- the issue needs user approval before implementation
- multiple related follow-ups must be tracked across turns

Otherwise, fix the issue within the current scope, validate it, and summarize the evidence.

For tracked issues, include:

- stable issue ID
- status (`open`, `planned`, `resolved`, or `deferred`)
- context and evidence
- proposed response
- validation expectation
- linked task IDs, if any

Ask for explicit approval before editing implementation files only when the response changes accepted scope, has meaningful product/design tradeoffs, or the user requested approval-first handling.

## Implementation Alignment Review

After implementation is complete and before final success reporting, invoke
`iterative-plan-implementation-review` when there is an active plan artifact to
compare against the implementation.

This normally applies to full plan tree work. For Tier 0, run it only when the
work was explicitly driven by an existing plan artifact; otherwise rely on the
normal closeout validation because there is no plan artifact to review against.

Invoke `iterative-plan-implementation-review` with focused inputs:

- plan artifact paths
- repository or workspace root
- maximum review rounds, defaulting to that skill's default unless the user set one
- current implementation scope, such as uncommitted changes, recent commits, or specific files
- required validation gates from the plan, when available

Apply valid or partially valid findings, reject invalid findings with evidence,
run the required validation for fixes, and update plan/task-board/evidence
artifacts when findings affect task status, validation evidence, or scope.

## Closeout

Before final response:

- run the strongest practical validation for the changed scope
- inspect the diff or changed files
- verify structured planning files parse when applicable
- run the implementation alignment review when an active plan artifact exists
- report validation commands and outcomes
- report uncommitted work or skipped verification, if any

For full plan tree closeout, also verify:

- no in-scope task remains pending unexpectedly
- completed tasks do not have stale `commit.hash: pending`
- review/approval state matches what actually happened

## Output Style

- Keep chat updates short and evidence-based.
- Prefer links to planning files over pasted artifacts.
- Do not repeat template text in chat unless asked.
- Do not load reference templates until the selected mode needs them.
- Summarize decisions and validation results; avoid narrating every bookkeeping step.
