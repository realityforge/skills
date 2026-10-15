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

## Review policy

### Continuity

Use read-only reviewers independent of the work they review. Start planning
with a clean reviewer and implementation with a fresh reviewer. Prefer the
same reviewer within each phase.

If a reviewer is unavailable, use a clean replacement without requesting an
exception. Supply the full review inputs: scope, accepted constraints,
execution authority, checkpoints, user corrections, prior coverage, findings,
dispositions and supporting evidence, and consumed and remaining budget. The
replacement verifies those dispositions and inspects any scope whose prior
coverage cannot be established before continuing confirmation. Record the
handoff in `TASKMAP.md`. Replacement is recovery from unavailability, never a
way to evade valid findings; unresolved findings remain open.

### Budget and escalation

Each stage sets its default round limit. Count every reviewer attempt,
including failed attempts, across replacements and replans within that phase;
these events do not reset the budget.

The default budget also includes one final confirmation attempt after the
round limit for fixes to existing findings within authorized scope. Check the
findings, fixes, and affected surfaces; this allowance is used once per phase,
not renewed by further fixes or replans. Explicit user round limits, resource
budgets, checkpoints, and stopping conditions take precedence.

A gate passes only on `Findings: none`. If permitted attempts are exhausted
without a pass, stop dependent work and present one consolidated escalation:
evidence, unresolved findings and tradeoffs, why review has not converged, and
a recommendation with bounded recovery work and budget including confirmation.
Ask for the substantive decision or authority needed under the
[decision policy](../AGENTS.md#scope-and-design), rather than permission for
one more round. Record the decision and its bounds in `TASKMAP.md`. If that
recovery exhausts its budget with the same blocker, report the gate incomplete;
seek another decision only when new material evidence changes the risk,
tradeoff, or required authority. Budget exhaustion never waives unresolved
findings.

## Output

Link to plan artifacts while they exist. State significant decisions and their
impacts plainly at any requested plan checkpoint and at closeout.
