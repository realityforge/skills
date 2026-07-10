---
name: iterative-plan-review
description: Run Plan Review in a subagent, assess findings, fix valid plan issues, and repeat review/fix rounds until no actionable findings remain or a configured round limit is reached.
---

# Iterative Plan Review

Use this skill for a subagent `plan-review`/fix loop. Default max rounds: `5`,
unless the user says otherwise. Infer the active plan path; ask only when it
cannot be inferred.

For each round:

1. Spawn or reuse one clean read-only subagent with `plan-review`.
2. Pass only plan artifact paths, repo root, and focused context paths. Do not
   fork full conversation context unless necessary.
3. Ask for `Findings` and `Scorecard`; `Findings: none` means stop.
4. Main agent assesses findings against repo, plan, and user evidence. Accept
   unless contradicted; narrow over-broad fixes.
5. Patch accepted or partially accepted plan issues. Do not patch rejected
   findings.
6. Validate edited structured artifacts where practical.
7. Re-review only after material plan edits and only until no actionable
   findings remain or max rounds is reached.

Keep plan updates scoped to the reviewed plan tree unless the user approves
broader changes. Preserve stable task IDs and question IDs. If plan status is
`accepted`, do not mark it back to draft unless the change reopens decisions or
scope.

User-facing output: one terse digest per round. Detail only rejected findings,
unresolved user decisions, blockers, and validation failures. Final report:
rounds run, final status, material fixes, validations, and remaining issues, if
any.
