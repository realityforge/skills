# Review Policy

## Reviewer continuity

Start each phase with a clean, read-only subagent independent of the work;
reuse it within the phase. Reviewers create no other agents.

Supply the repository root, the plan tree, applicable user corrections, and the
attempt count and limit. The phase brief names its additional inputs.

If the reviewer becomes unavailable, use a clean replacement with the same
inputs plus prior findings and their dispositions. Replacement keeps unresolved
findings and the consumed budget.

## Review loop

Review the complete scope first. The confirmation round checks finding
dispositions, fixes, and affected surfaces, while reporting any newly
discovered material defect. Verify findings against the code; fix valid issues
and explain rejections. A pass requires no unresolved material findings. Report
findings with evidence, impact, and a specific correction; otherwise report
`Findings: none`, coverage, and residual risk.

## Pass validity

Substantive changes invalidate affected validation and review passes. Rerun
affected checks and any project gate whose result could change, then reopen
affected reviews before dependent work or closeout.

## Budget and escalation

Each phase allows two attempts: one review and one confirmation. Replacement
and replanning do not reset the budget. A passed review reopened by a later
change gets one more confirmation. Explicit user budgets take precedence.

If confirmation does not pass, stop dependent work and present one escalation:
unresolved findings, tradeoffs, and a recommended recovery. Ask the user for
the decision under the
[shared decision policy](../../AGENTS.md#scope-and-design).

Track each phase's attempts and result in `TASKMAP.md`.
