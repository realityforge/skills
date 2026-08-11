# Implementation Review

Review delivered behavior against the approved spec before examining task
alignment. Remain read-only and do not create other agents.

## Inputs

The main agent supplies:

- repository root and exact active plan path
- approved plan commit and current implementation commit or diff range
- `SPEC.md`, `TASKMAP.md`, every task file, and canonical artifacts promoted
  from the plan
- required task-local and full-scope validation
- round number, round limit, and prior findings for confirmation rounds

## Review order

1. **Outcomes:** map every requirement and acceptance criterion to observable
   implementation, tests, and validation evidence. Find contradictions,
   omissions, disconnected code, weak tests, and unplanned behavior.
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

In the first round, inspect the complete delivered scope. In later rounds,
verify prior findings and the surfaces changed to resolve them; report a new
finding only when those edits introduced or exposed it.

## Output

Start with `Findings` and order actionable findings by delivery risk.

Use compact bullets:

`- [P1|P2] <title>. Evidence: <file/line, behavior, or command result>. Impact:
<requirement or delivery risk>. Fix: <specific next step>.`

When no actionable issue remains, output:

`Findings: none. Checked: <concise evidence>. Residual risk: <none or specific
unverified gate>.`
