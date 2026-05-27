---
name: iterative-plan-review
description: Run Plan Review in a subagent, assess findings, fix valid plan issues, and repeat review/fix rounds until no actionable findings remain or a configured round limit is reached.
---

# Iterative Plan Review

Use this skill when the user wants a plan reviewed in a subagent with an
explicit feedback assessment and fix loop.

This skill coordinates review work. The subagent performs `plan-review`
judgment; the main agent assesses feedback, updates plan artifacts when
appropriate, and controls the loop.

## Default Parameters

- Default max rounds: `3`.
- If the user specifies a different limit, use that limit.
- If the user does not identify a plan path, infer the active plan from context.
  If no active plan can be inferred, ask the user for the plan path.

## Required Inputs

Before starting, identify:

- the plan artifact paths to review;
- the repository or workspace root;
- the maximum review rounds;
- any known context files the subagent should inspect.

If any required input cannot be inferred safely, ask the user before spawning
the subagent.

## Subagent Rules

Run the review phase in a clean subagent.

The subagent prompt must:

- tell the subagent to use `plan-review`;
- pass the plan artifact paths;
- pass relevant repo/context paths;
- instruct the subagent not to edit files;
- request output starting with `Findings`, then `Scorecard`;
- request `Findings: none` when no actionable findings remain;
- ask the subagent to state any missing user context precisely.

Prefer reusing the same subagent for subsequent review rounds so it can compare
the revised plan against prior findings. Do not fork full conversation context
unless needed; pass focused context.

## Main-Agent Review Loop

For each round:

1. Ask the subagent to review the latest plan.
2. Wait for the subagent response.
3. If the subagent asks for additional user context:
   - assess whether the answer can be inferred from existing plan/repo context;
   - if not, ask the user the specific question before continuing.
4. Restate the subagent feedback to the user-facing transcript:
   - concise finding title;
   - whether the finding is valid, partially valid, or rejected;
   - brief reason for that assessment.
5. Fix valid or partially valid findings in the plan artifacts.
6. Do not fix rejected findings; explain why they were rejected.
7. Validate edited artifacts where practical, such as YAML parse checks for task
   boards.
8. Continue to the next round unless:
   - the subagent reports `Findings: none`;
   - no actionable findings remain after assessment;
   - the max round count has been reached.

Always close the subagent when the loop ends.

## Feedback Assessment Guidance

Treat findings as valid when they expose:

- missing or ambiguous requirements;
- unsafe sequencing;
- unverified validation claims;
- task-board/task-status inconsistency;
- plan/code mismatch discovered during repo inspection;
- missing decision records or unresolved questions.

Reject findings only when there is concrete evidence that:

- the plan already addresses the issue clearly;
- the finding conflicts with explicit user decisions;
- the proposed fix would expand scope beyond the requested plan;
- the finding depends on incorrect repo facts.

If a finding is directionally right but the proposed fix is too broad, mark it
partially valid and apply the narrower correction.

## Editing Rules

- Keep plan updates scoped to the reviewed plan tree unless the user approves
  broader changes.
- Preserve stable task IDs and question IDs.
- If plan status is `accepted`, do not silently mark it back to draft unless the
  change meaningfully reopens decisions or scope.
- Record material review-loop changes in the task board or plan history when
  the plan has such a convention.
- Keep artifacts parseable and concise.

## Final Report

When the loop ends, report:

- how many rounds ran;
- whether the final subagent review had findings;
- which findings were fixed, rejected, or left for user decision;
- validation checks run on edited artifacts;
- confirmation that the subagent was closed.

If the max round count is reached with remaining actionable findings, state that
clearly and list the remaining issues.
