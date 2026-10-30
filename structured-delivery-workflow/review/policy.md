# Review Policy

## Reviewer continuity

Start each phase with a clean, read-only subagent independent of the work;
reuse it within the phase. Reviewers create no other agents.

Supply the repository root, active plan, accepted scope and constraints,
authority and checkpoints, user corrections with their sources and scope,
relevant evidence, and attempt count and limit. The phase brief names its
additional inputs.

If the reviewer becomes unavailable, use a clean replacement with the same
inputs, prior coverage, findings, dispositions, and supporting evidence. It
verifies dispositions and any scope whose coverage cannot be established.
Replacement preserves unresolved findings and the consumed budget.

## Review loop

Review the complete scope first. Later rounds focus on finding dispositions,
fixes, corrections, and affected surfaces, while reporting any newly discovered
material defect. Verify findings against evidence; fix valid issues and explain
rejections. A pass requires no unresolved material findings. Report findings
with evidence, impact, and a specific correction; otherwise report
`Findings: none`, coverage, and missing evidence or residual risk. Required
unverified gates remain incomplete.

## Pass validity

Substantive changes invalidate affected validation and review passes. Rerun
affected checks and any project gate whose result could change, then reopen
affected reviews before dependent work or closeout. Record refreshed evidence
in the existing task files or `TASKMAP.md`.

## Budget and escalation

Default limits are three planning attempts and five implementation attempts,
including confirmation. Count failed attempts; replacement and replanning do
not reset the phase budget, nor does reopening a passed review. Explicit user
budgets and stopping conditions take precedence.

If the budget ends without a pass, stop dependent work and present one
consolidated escalation: unresolved findings, evidence, tradeoffs, why review
has not converged, and a recommended recovery with a bounded budget including
confirmation. Request the substantive decision or authority under the
[shared decision policy](../../AGENTS.md#scope-and-design). If recovery exhausts
its budget on the same blocker, leave the gate incomplete; seek another
decision only when new material evidence changes the risk, tradeoff, or
authority needed.

Record reviewer history, coverage, attempts, dispositions, results, and any
recovery decision and its bounds in `TASKMAP.md`.
