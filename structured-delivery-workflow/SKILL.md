---
name: structured-delivery-workflow
description: Plan, implement, review, and close risky engineering work through a temporary local plan tree.
disable-model-invocation: true
---

# Structured Delivery Workflow

Deliver risky work through a temporary plan tree kept out of version control.

## Plan tree

Apply the [shared scope and decision policy](../AGENTS.md#scope-and-design).
Create a new tree for each invocation; resume an existing tree only on explicit
request. Unless repository instructions specify another location, use:

```text
plans/<initiative>/
  SPEC.md
  tasks/
    TASKMAP.md
    T01-<slug>.md
    T02-<slug>.md
```

Other files in the tree are supporting evidence, not requirements sources.
The whole tree is temporary and removed at closeout.

## Stage router

- Creating a plan, revising a draft plan, or materially replanning:
  read `instructions/planning.md`.
- Implementing a plan or continuing implementation review: read
  `instructions/implementation.md`.
- Closing work whose implementation review passed: read
  `instructions/closeout.md`.

When explicitly resuming, read `tasks/TASKMAP.md` first and route from its
status.
