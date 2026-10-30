---
name: structured-delivery-workflow
description: Plan, implement, review, and close risky engineering work through a temporary committed plan tree.
disable-model-invocation: true
---

# Structured Delivery Workflow

Deliver authorized scope through a temporary, auditable plan tree.

## Plan tree

Apply the [shared scope and decision policy](../AGENTS.md#scope-and-design).
Create a new tree for each invocation; resume an existing tree only on explicit
request. Verify the exact active tree before editing, committing, or deleting
it. Unless repository instructions specify another location, use:

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
- Implementing a committed plan or continuing implementation review: read
  `instructions/implementation.md`.
- Closing work whose implementation review passed: read
  `instructions/closeout.md`.

When explicitly resuming, read `tasks/TASKMAP.md` first and route from its
status.

## Review policy

Start each phase with a clean, read-only subagent independent of the work;
reuse it within the phase. Reviewers create no other agents.

Supply the repository root, active plan, accepted scope and constraints,
authority and checkpoints, user corrections with their sources and scope,
relevant evidence, and attempt count and limit. The phase brief names its
additional inputs.

Review the complete scope first. Later rounds focus on finding dispositions,
fixes, corrections, and affected surfaces, while reporting any newly discovered
material defect. Verify findings against evidence; fix valid issues and explain
rejections. A pass requires no unresolved material findings. Report findings
with evidence, impact, and a specific correction; otherwise report
`Findings: none`, coverage, and missing evidence or residual risk. Required
unverified gates remain incomplete.

If the reviewer becomes unavailable, use a clean replacement with the same
inputs, prior coverage, findings, dispositions, and supporting evidence. It
verifies dispositions and any scope whose coverage cannot be established.
Replacement preserves unresolved findings and the consumed budget.

Default limits are three planning attempts and five implementation attempts,
including confirmation. Count failed attempts; replacement and replanning do
not reset the phase budget. Explicit user budgets and stopping conditions
take precedence.

If the budget ends without a pass, stop dependent work and present one
consolidated escalation: unresolved findings, evidence, tradeoffs, why review
has not converged, and a recommended recovery with a bounded budget including
confirmation. Request the substantive decision or authority under the shared
decision policy. If recovery exhausts its budget on the same blocker, leave the
gate incomplete; seek another decision only when new material evidence changes
the risk, tradeoff, or authority needed.

Record reviewer history, coverage, attempts, dispositions, results, and any
recovery decision and its bounds in `TASKMAP.md`.
