---
name: structured-delivery-workflow
description: Structure high-risk or multi-phase engineering delivery through separate requirements, design, task, review, and knowledge-promotion gates. Use when work needs a reviewable plan, spans threads or agents, carries migration, data, architecture, compliance, or parity risk, or requires durable traceability.
disable-model-invocation: true
license: Apache-2.0
compatibility: Works best in repositories that allow markdown/yaml planning artifacts and test/build execution.
metadata:
  author: realityforge
  version: "4.0"
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
- Do not bulk-load this skill's instruction or template files. Read the stage
  instruction only when the current stage requires it. Read templates only when
  creating the corresponding artifacts.

## Modes

Use the persistent plan tree path only:

- **Persistent plan tree** preserves reviewed requirements, implementation
  design, and task state across risk, delegation, or multiple threads.

Read `instructions/planning.md` as the first planning instruction.

## Stage Router

- Creating or revising a persistent plan: read `instructions/planning.md`.
- Implementing from an accepted persistent plan: read
  `instructions/existing-plan-implementation.md`.
- Updating persistent task state: read `instructions/task-tracking.md`.
- Reviewing a persistent planning stage, asking for user review, or accepting a
  plan: read `instructions/review-and-approval.md`.
- Review requirements gate before progressing: read
  `instructions/review-requirements.md`.
- Reviewing implementation design: read
  `instructions/review-implementation-design.md`.
- Reviewing task breakdown before execution: read
  `instructions/review-task-breakdown.md`.
- Handling post-implementation issues or reviewing implementation outcomes:
  read `instructions/implementation-review.md`.
- A domain term, qualifying adopted decision, or user-deferred question settles,
  or durable knowledge must be promoted before plan cleanup: read
  `instructions/knowledge-promotion.md`.
- Removing completed plan artifacts: read `instructions/plan-cleanup.md`.
- Preparing the final response: read `instructions/closeout.md`.

## Required Flow

1. Read stage-specific local instructions and check worktree state.
2. Locate or initialize the active persistent plan tree and plan node.
3. Gather local context needed for stage artifacts and the active plan node.
4. Resolve evidence-answerable questions yourself.
5. Ask one user question at a time only for true blockers.
6. Follow the stage instruction for the current step.
7. Validate structured artifacts when edited.
8. Run required validation before marking work complete.
9. Inspect the diff or changed files before reporting completion.

For the persistent plan tree:

- run the built-in iterative stage review after completing each
  requirements, implementation-design, and task-breakdown gate by reading the
  matching `instructions/review-*.md` file, and only progress after acceptance.
- run the built-in requirements-first implementation review loop after
  implementation when active plan artifacts exist, using
  `instructions/implementation-review.md`.
- promote durable requirements, decisions, terminology, and deferred questions
  and prepare the closeout record before plan cleanup
- after implementation-review issues are fixed and knowledge is promoted,
  remove the temporary active plan tree unless retention is explicitly required

## Output Style

- Keep chat updates short and evidence-based.
- Prefer links to planning files over pasted artifacts.
- Summarize decisions and validation results; avoid narrating every
  bookkeeping step.
