# Implementation Review

Review delivered behavior against the committed spec before examining task
alignment. Remain read-only and do not create other agents.

## Inputs

The main agent supplies:

- repository root and exact active plan path
- plan commit and current implementation commit or diff range
- `SPEC.md`, `TASKMAP.md`, every task file, and canonical artifacts promoted
  from the plan
- required task-local and full-scope validation
- accepted scope, constraints, execution-authority sources, and checkpoints
- applicable user corrections with their source, meaning, and scope
- attempt number, remaining round budget, and final-confirmation status
- prior coverage, findings, dispositions, and supporting evidence for later
  rounds or a replacement reviewer

## Review order

1. **Outcomes:** map every requirement, acceptance criterion, and applicable
   user correction to observable implementation, tests, and validation evidence
   across affected peers. Find contradictions, omissions, disconnected code,
   weak tests, and unplanned behavior.
2. **Decision validity:** test significant decisions and load-bearing technical
   assumptions against what implementation revealed. Identify material
   trade-offs, safety concerns, or simpler direct designs that are now evident.
3. **Delivery alignment:** compare the valid design to task status, dependency
   completion, evidence, and promoted knowledge. Find stale or overstated
   claims.

Treat plan entries and recorded commands as claims. Inspect the underlying
code, tests, git state, and cheap non-mutating checks needed to verify them.
Requirements remain authoritative; do not weaken them to match incomplete
implementation.

Apply the [documentation rules](../../AGENTS.md#documentation) to documentation
created or changed by this work.

Apply the [global verification and cleanup rules](../../AGENTS.md#test-and-clean-up)
to verification artifacts added or materially changed by this work. Trace
claimed consumers beyond their own tests and build wiring. Prefer existing
suites when they preserve the failure trigger; retain separate fixtures when
isolation is necessary.

Follow the [shared review policy](../SKILL.md#review-policy) on replacement.
In the first round, inspect the complete delivered scope. In later rounds,
verify prior findings, resulting edits, and intervening user corrections across
affected peers. New findings must arise from those edits or corrections, or
from previously unverified scope inspected during replacement.

## Output

Start with `Findings` and order actionable findings by delivery risk.

Use compact bullets:

`- [P1|P2] <title>. Evidence: <file/line, behavior, or command result>. Impact:
<requirement or delivery risk>. Fix: <specific next step>.`

When no actionable issue remains, output:

`Findings: none. Checked: <concise evidence>. Residual risk: <none or specific
unverified gate>.`
