---
name: structured-delivery-workflow
description: Run a context-efficient engineering workflow with right-sized planning, task tracking, validation evidence, and optional review/commit traceability. Use when work spans multiple files, has process risk, needs a reviewable plan, or must preserve progress across threads.
license: Apache-2.0
compatibility: Works best in repositories that allow markdown/yaml planning artifacts and test/build execution.
metadata:
  author: realityforge
  version: "3.2"
---

# Structured Delivery Workflow

Use this skill to keep engineering work explicit without turning process state
into the work. Start with the smallest durable state that preserves decisions,
sequencing, and validation evidence. Escalate only when the request or risk
justifies the extra artifacts.

## Hard Rules

- Inspect local instructions, repository state, and relevant code before
  planning or editing.
- Prefer existing repository planning conventions. Do not invent a new layout
  when one exists.
- Ask the user only for decisions that cannot be answered from evidence and
  materially affect scope, behavior, risk, or review.
- Keep one active implementation focus at a time.
- Record validation evidence before claiming completion.
- Do not modify unrelated `plans/` trees. Identify the active plan before
  editing any file under `plans/`.
- Do not create persistent artifacts just to satisfy process. Create them when
  they will be reviewed, resumed, delegated, audited, or used during
  implementation.
- Do not bulk-load this skill's reference files. Read the stage reference only
  when the current stage requires it.

## Modes

Choose the lightest mode that fits the request. If mode choice is unclear, read
`references/mode-selection.md`.

### Lightweight Implementation

Use for bounded implementation work where the user did not ask for plan
artifacts and the work can finish in the current thread.

Keep state in conversation:

- scope in one or two sentences
- short task checklist, if useful
- targeted and final validation commands
- final summary with files changed and verification results

Do not create `plans/` files for lightweight implementation.

### Persistent Plan Tree

Use when the user asks for plans or traceability, work spans phases or threads,
another agent will implement from the plan, risk is high, or repository
convention requires persistent plans.

Default persistent plan tree:

```
plans/<initiative>/
  00-requirements.md
  10-implementation-plan.md
  20-task-board.yaml
```

Create optional files only when they add useful durable state:

- `40-test-strategy.md` for complex or multi-environment validation
- `30-compatibility-matrix.md` for parity or migration work
- `30-output-contract.md` for CLI/API output contracts
- `01-*-deep-dive.md` for focused decisions that would overload requirements
- `50-implementation-issues.md` only after real follow-up issues exist

Use templates only when creating corresponding files:

- `references/requirements-deep-dive-template.md`
- `references/implementation-plan-template.md`
- `references/task-board-template.yaml`

## Stage Router

- Unclear mode choice or escalation: read `references/mode-selection.md`.
- Creating or revising a persistent plan: read `references/planning.md`.
- Implementing from an accepted persistent plan: read
  `references/existing-plan-implementation.md`.
- Updating persistent task state: read `references/task-tracking.md`.
- Asking for user review or accepting a plan: read
  `references/review-and-approval.md`.
- Handling post-implementation issues or checking implementation alignment:
  read `references/implementation-review.md`.
- Removing completed plan artifacts: read `references/plan-cleanup.md`.
- Preparing the final response: read `references/closeout.md`.

## Required Flow

1. Read local instructions and check worktree state.
2. Select lightweight implementation or persistent plan tree.
3. Gather only enough local context for the current stage.
4. Resolve evidence-answerable questions yourself.
5. Ask one user question at a time only for true blockers.
6. Follow the stage reference for the current step.
7. Validate structured artifacts when edited.
8. Run required validation before marking work complete.
9. Inspect the diff or changed files before reporting completion.

For persistent plan trees:

- run the built-in iterative `plan-review` loop after drafting the plan and
  before asking the user to review
- run the built-in iterative `plan-implementation-review` loop after
  implementation when active plan artifacts exist
- after implementation-review issues are fixed and committed, remove the active
  plan tree in a separate deletion-only cleanup commit when commits are allowed

## Output Style

- Keep chat updates short and evidence-based.
- Prefer links to planning files over pasted artifacts.
- Do not repeat template text in chat unless asked.
- Do not load reference templates until the selected mode needs them.
- Summarize decisions and validation results; avoid narrating every
  bookkeeping step.
