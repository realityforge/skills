---
name: iterative-plan-implementation-review
description: Run Plan Implementation Review in a subagent, assess findings, fix valid implementation or evidence gaps, and repeat review/fix rounds until no actionable findings remain or a configured round limit is reached.
---

# Iterative Plan Implementation Review

Use this skill when the user wants implementation alignment reviewed in a
subagent with an explicit feedback assessment, fix, and re-review loop.

This skill coordinates alignment review work. The subagent performs
`plan-implementation-review` judgment; the main agent assesses feedback,
implements valid fixes, updates evidence artifacts when appropriate, validates
the result, and controls the loop.

## Default Parameters

- Default max rounds: `5`.
- If the user specifies a different limit, use that limit.
- If the user does not identify a plan path, infer the active plan from context.
  If no active plan can be inferred, ask the user for the plan path.

## Required Inputs

Before starting, identify:

- the plan artifact paths to compare against implementation;
- the repository or workspace root;
- the maximum review rounds;
- the current implementation scope, such as uncommitted changes, recent commits,
  or specific files;
- required validation gates from the plan, when available.

If any required input cannot be inferred safely, ask the user before spawning
the subagent.

## Subagent Rules

Run the review phase in a clean subagent.

The subagent prompt must:

- tell the subagent to use `plan-implementation-review`;
- pass the plan artifact paths;
- pass the repository root and relevant implementation paths;
- instruct the subagent to inspect git status and relevant diffs first;
- instruct the subagent not to edit files;
- request output starting with `Findings`, then `Scorecard`;
- request `Findings: none` when no actionable findings remain;
- ask the subagent to state any missing user context precisely.

Prefer reusing the same subagent for subsequent review rounds so it can compare
new repository state against earlier findings. Do not fork full conversation
context unless needed; pass focused context.

## Main-Agent Review Loop

For each round:

1. Ask the subagent to review current implementation alignment against the
   latest plan.
2. Wait for the subagent response.
3. If the subagent asks for additional user context:
   - assess whether the answer can be inferred from plan/repo context;
   - if not, ask the user the specific question before continuing.
4. Restate the subagent feedback to the user-facing transcript:
   - concise finding title;
   - whether the finding is valid, partially valid, or rejected;
   - brief reason for that assessment.
5. Fix valid or partially valid findings.
6. Do not fix rejected findings; explain why they were rejected.
7. Run targeted validation for changed behavior.
8. Run the plan's required gate before claiming a round's implementation fixes
   are complete, unless the user explicitly asks to defer it.
9. Update plan/task-board/evidence artifacts when fixes affect task status,
   validation evidence, or implementation scope.
10. Continue to the next round unless:
    - the subagent reports `Findings: none`;
    - no actionable findings remain after assessment;
    - the max round count has been reached.

Always close the subagent when the loop ends.

## Feedback Assessment Guidance

Treat findings as valid when they expose:

- planned implementation that is absent or partial;
- implementation behavior that contradicts the plan;
- missing or weak tests for promised behavior;
- validation evidence that is absent, stale, or overstated;
- task-board or plan status that does not match repository state;
- extra implementation scope not justified by the plan;
- dead, disconnected, or unverified code paths.

Reject findings only when there is concrete evidence that:

- the implementation already satisfies the plan;
- the plan explicitly excludes the requested behavior;
- the finding depends on incorrect repo facts;
- the proposed fix would expand scope beyond the accepted plan or user request.

If a finding is directionally right but the proposed fix is too broad, mark it
partially valid and apply the narrower correction.

## Editing Rules

- Keep implementation fixes scoped to the reviewed plan unless the user approves
  broader changes.
- Do not silently weaken the plan to match incomplete implementation.
- If the implementation is correct but evidence is missing, prefer adding or
  correcting validation evidence over changing code.
- If task-board entries are marked complete, make sure completed tasks have
  non-pending commit metadata or an explicit `not_required` marker according to
  the plan convention.
- Preserve user changes and unrelated worktree changes.
- Do not commit unless the user asks for a commit.

## Validation Rules

- Run targeted tests after behavior fixes.
- Run the plan's required full gate before final success reporting when
  practical.
- If a full gate cannot be run, state the blocker and keep any affected task or
  finding open unless the user explicitly accepts deferral.
- Re-parse edited YAML or structured artifacts when practical.

## Final Report

When the loop ends, report:

- how many rounds ran;
- whether the final subagent review had findings;
- which findings were fixed, rejected, or left for user decision;
- validation checks run and their results;
- whether the plan/task-board evidence was updated;
- confirmation that the subagent was closed.

If the max round count is reached with remaining actionable findings, state that
clearly and list the remaining issues.
