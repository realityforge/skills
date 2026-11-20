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
request. Unless repository instructions specify another location, use a
git-ignored directory:

```text
tmp/plans/<initiative>/
  SPEC.md
  tasks/
    TASKMAP.md
    T01-<slug>.md
    T02-<slug>.md
```

When `tmp/` is not ignored, add it to `.git/info/exclude`. The tree stays out
of commits; the pull request description carries what reviewers need from it.
`SPEC.md` owns the requirements; other files in the tree are working notes.

## Stage router

- Creating a plan, revising a draft plan, or materially replanning:
  read `instructions/planning.md`.
- Implementing a planned tree or continuing implementation review: read
  `instructions/implementation.md`.
- Closing work whose implementation review passed: read
  `instructions/closeout.md`.

When explicitly resuming, read `tasks/TASKMAP.md` first and route from its
status.
