---
name: babysit-pr
description: Monitor the current pull request until it merges.
disable-model-invocation: true
---

Treat invocation as authorization to maintain a same-thread heartbeat and perform the focused commits, pushes, and GitHub writes required below. It does not authorize merging the pull request, approving it, enabling auto-merge, entering a merge queue, force-pushing, or changing unrelated code.

Accept an optional pull request URL or number and cadence. Otherwise resolve the open pull request for the current repository and checked-out branch. Default to 30 minutes.

## Start or resume

1. Resolve and pin `owner/repository#number`. Prefer an explicit target; ask which pull request only when accepted instructions and repository evidence cannot select one.
2. Run one monitoring tick immediately.
3. While the pull request remains unmerged, create or update exactly one heartbeat in this task named `Babysit owner/repository#number`. Its prompt must explicitly name `$babysit-pr`, `$pr-review-resolver`, `$pr-action-error-resolver`, and `$commit`, plus the pinned identity, cadence, accepted authority and scope, live exceptions, checkpoints, and stopping conditions. Give temporary restrictions their purpose and accepted expiry condition. Link current instructions and state owners; retain only a compact checkpoint needed to prevent repeated actions. A replay invokes `$babysit-pr` for one tick; it does not create another monitor.
4. A manual reinvocation runs an immediate tick, updates a supplied cadence, and resumes the existing heartbeat.

## Monitoring tick

1. Recover later user direction from this conversation and reconcile the existing heartbeat under the [correction policy](../AGENTS.md#scope-and-design). Read current repository and skill instructions. Fetch the pull request state, current head SHA, source and base refs, mergeability, unresolved review threads, check runs, classic commit statuses, and relevant diagnostic comments. Bind every action to the current head. Correlate a diagnostic comment through its linked build, status, or commit; age alone is insufficient.
2. If merged, pause the heartbeat. Report the verified merge and the impact of actions taken while babysitting. Archive this task when no work remains in it and nothing in the report requires the user's attention. This is the only successful terminal state.
3. Pause for required user direction when the pull request is closed unmerged, draft, from a fork, lacks verified push access, or has an actionable human conversation comment outside a review thread. Apply the pause procedure below.
4. Before modifying files, require a clean worktree and a verified route to the source branch. Fetch and fast-forward a clean source branch that advanced remotely. Pause for a dirty or divergent worktree, a wrong branch, or a detached checkout without a safe push target.
5. Invoke `$pr-review-resolver` when unresolved review threads exist; follow its [bot re-review policy](../pr-review-resolver/SKILL.md#bot-re-review) for additional requests. Re-fetch the pull request and head afterward. If the resolver pushed a new head, leave its newly triggered validation to the next tick.
6. Resolve a merge conflict using the conflict procedure below.
7. Resolve current-head failures using the failure procedure below.
8. Treat pending, queued, in-progress, missing, neutral, and skipped checks as waiting unless repository evidence makes them blocking. Continue monitoring long queues; pause when evidence shows progress requires user action.
9. When the pull request is green but awaiting approval, a merge queue, or a human merge, keep monitoring without approving, enqueueing, enabling auto-merge, or merging.

## Conflict procedure

Act when GitHub reports conflicting changes or branch protection blocks progress because the head must be current.

1. Follow explicit repository guidance. Otherwise merge the current base into the source branch, preserving two-parent history. A merely newer base is not itself a reason to update the branch.
2. Resolve conflicts when repository evidence, tests, and both sides establish one behavior-preserving result. Use documented regeneration for generated files.
3. If the source advances concurrently, abort, fetch both refs, and retry once from the new exact head. A second race requires a pause for user direction.
4. If competing behaviors remain plausible, capture the conflicting paths and ambiguity, abort back to the verified clean head, and pause for the unresolved decision.
5. Run focused tests selected from the affected files and repository guidance. Invoke `$commit` before creating the merge commit, then push normally to the verified source branch. Repository requirements for rebasing or rewritten history require a pause for user direction.
6. Require fresh validation for the pushed exact head.

## Failure procedure

- For current-head GitHub Actions conclusions `failure`, `error`, `timed_out`, `cancelled`, or `action_required`, invoke `$pr-action-error-resolver`.
- For another current-head required status with a recognized machine diagnostic, inspect its linked logs and comment, fix the root cause, run focused checks, invoke `$commit`, commit, and push. Verify the remote branch matches `HEAD` and the worktree is clean.
- Ignore stale failures from earlier heads. A current-head passing status plus a machine failure diagnostic may represent a later delivery failure; establish that link from build evidence before acting.
- Never repeat an attempted repair against unchanged evidence. If a resolver cannot progress or the same head fails identically after its focused fix, pause and report the blocker.

## Pause and completion

Pause the heartbeat when required user action or direction blocks safe progress. Recover accepted instructions before asking a focused question under the [decision policy](../AGENTS.md#scope-and-design). Resume the same heartbeat after the blocker is resolved and the blocked action is complete, unless the user cancels monitoring.

When the user explicitly requests a full `$grill-me` interview, pause the heartbeat and wait for its final shared-understanding confirmation before acting on it.

After every mutation, verify the remote source matches local `HEAD` and the worktree is clean. At the end of every tick, re-check merge state. Stay quiet when nothing changed and no user action is needed; report actions, blockers, and failures.
