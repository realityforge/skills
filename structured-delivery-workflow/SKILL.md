---
name: structured-delivery-workflow
description: Plan, implement, review, and close risky engineering work through a temporary committed plan tree.
disable-model-invocation: true
---

# Structured Delivery Workflow

Deliver authorized scope through a temporary, auditable plan tree.

## Entry gate

Establish the accepted outcome, constraints, and execution authority from the
user's request or a recoverable prior agreement, including sources referenced
by a handoff. A new Task, chat, or handoff does not require reconfirmation.
Acceptance of a design alone does not authorize implementation.

Apply the [decision policy](../AGENTS.md#scope-and-design) to missing authority
and unresolved choices. Recover available sources first, then ask only for the
missing direction. When the user explicitly requests `$grill-me`, wait for its
final shared-understanding confirmation before acting on the interview.

Create a new plan tree for every invocation. Modify an existing tree only when
the user explicitly asks to resume that paused plan. Resolve the exact active
tree before every plan edit, commit, or deletion.

## Plan tree

Unless applicable repository instructions require another location, use:

```text
plans/<initiative>/
  SPEC.md
  tasks/
    TASKMAP.md
    T01-<slug>.md
    T02-<slug>.md
```

Other files inside the active tree are temporary evidence or orchestration
artifacts. The whole tree is removed at closeout.

## Stage router

- Creating a plan, revising a draft plan, or materially replanning:
  read `instructions/planning.md`.
- Implementing a committed plan or continuing implementation review: read
  `instructions/implementation.md`.
- Closing work whose implementation review passed: read
  `instructions/closeout.md`.

When explicitly resuming, read `tasks/TASKMAP.md` first and route from its
status.

## Reviewer identities

Use one read-only planning reviewer for all planning rounds and one fresh
read-only implementation reviewer for all implementation rounds. Continue a
phase's rounds with its existing reviewer. If that reviewer cannot continue,
report the incomplete gate; another reviewer does not substitute for it.

## Output

Link to plan artifacts while they exist. State significant decisions and their
impacts plainly at any requested plan checkpoint and at closeout.
