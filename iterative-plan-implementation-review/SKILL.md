---
name: iterative-plan-implementation-review
description: Run plan implementation review in a subagent, fix valid gaps, and repeat until clean or the round limit is reached.
---

# Iterative Plan Implementation Review

Use when implementation must be checked against an accepted plan with an
independent review/fix loop.

Defaults:

- max rounds: `5`, unless the user gives another limit
- reviewer: clean subagent using `plan-implementation-review`
- main agent owns fixes, validation, evidence updates, and final reporting

Before spawning, resolve the repo root, plan artifacts, implementation scope,
required gates, and round limit. Infer these from context when safe; ask only if
the review target is genuinely ambiguous.

For each round:

1. Send the subagent a focused read-only prompt: repo root, plan paths,
   implementation scope, relevant prior findings, required gates, and
   `Findings`/`Scorecard` output. Do not pass full conversation context unless
   necessary.
2. Assess each finding against repo evidence.
3. Fix valid or partially valid findings with the narrowest implementation,
   test, or evidence change. Reject only with concrete evidence.
4. Run targeted validation for changed behavior. Run the plan's full gate before
   final success, or explain why it could not be run.
5. Update plan/task-board/evidence artifacts only when status, scope, or
   validation evidence changed.
6. Re-review unless the subagent reports `Findings: none`, no actionable
   findings remain after assessment, or max rounds is reached.

Do not weaken the plan to match incomplete implementation. Preserve unrelated
user changes. Do not commit unless asked.

Final report: rounds run, final review result, fixes/rejections/leftovers,
validation results, evidence updates, and subagent closure.
