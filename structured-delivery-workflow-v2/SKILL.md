---
name: structured-delivery-workflow-v2
description: Plan, approve, implement, review, and close risky engineering work through a temporary committed plan tree.
disable-model-invocation: true
---

# Structured Delivery Workflow V2

Deliver from a completed `$grill-me` session through a temporary, auditable plan
tree.

## Entry gate

Confirm that the current conversation contains the user's explicit confirmation
of shared understanding from `$grill-me`. If it does not, stop and direct the
user to `$grill-me`; this skill does not run its own interview.

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

- Creating a plan, revising an unapproved plan, or materially replanning:
  read `instructions/planning.md`.
- Implementing an approved plan or continuing implementation review: read
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
impacts plainly at human review and closeout.
