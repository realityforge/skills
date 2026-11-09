---
name: babysit-pr
description: Monitor the current pull request until it merges.
disable-model-invocation: true
---

Treat invocation as authorization to watch the pull request and perform the focused commits, pushes, and GitHub writes required below. It does not authorize merging the pull request, approving it, enabling auto-merge, entering a merge queue, force-pushing, or changing unrelated code.

Accept an optional pull request URL or number. Otherwise resolve the open pull request for the current repository and checked-out branch, and pin `owner/repository#number`. Run one wake on the current PR state first — pre-existing threads and failures are yours to handle before anything new arrives — then keep exactly one watcher running. A reinvocation while watching runs one wake and leaves the existing watcher in place.

## Watch

Never write your own polling or `sleep` loop, and never run two watchers on one PR: every watcher on a GitHub account shares one rate limit.

- **In T3 Code:** call `watch_pull_request` and end your turn. It wakes this thread when a check fails, required checks pass, someone comments or reviews, or the branch conflicts. Only the thread that owns the PR watches it; a delegated child never does. The watch persists across turns: call `unwatch_pull_request` when you stop — merged, paused, or handing off — and re-watch to resume. A merge or close ends the watch on its own. "Stopped watching, could not read it" means the GraphQL rate limit is spent: check `gh api rate_limit --jq .resources.graphql`, wait for `reset` with one background command, then watch again.
- **Everywhere else:** run `scripts/pr-wait` from this skill's directory as one long command (in Claude Code, with the Monitor tool so each line wakes you):

  ```bash
  pr-wait <pr> [--repo owner/name] --until any-change
  ```

  One line per real event; exit 0 on an event or merge, 1 when it needs you (a required check failed, the branch conflicts, the PR closed, GitHub stayed unreachable), 2 on bad input or when another pid already watches the PR — kill that one only if its events do not reach you. After each handled event, start it again; stop only on a merged line. It remembers what it already reported, so a restart loses nothing.

When GraphQL is exhausted, REST still works: read the PR with `gh api repos/<owner>/<repo>/pulls/<n>` and its checks with `gh api repos/<owner>/<repo>/commits/<sha>/check-runs`.

## A wake

A wake is news, not a merge decision. Bind every action to the current head: findings and failures from earlier heads are noise, and a diagnostic comment counts only through its linked build, status, or commit — age alone is insufficient.

1. **Merged:** report the verified merge and the impact of actions taken while babysitting; archive this task when nothing in the report needs the user. This is the only successful terminal state.
2. **Needs you:** the PR is closed unmerged, draft, from a fork, or missing verified push access, or an actionable human comment outside a review thread → pause (below).
3. **Unresolved review threads:** invoke `$pr-review-resolver`, following its [bot re-review policy](../pr-review-resolver/SKILL.md#bot-re-review). Re-fetch the head afterward; validation triggered by its push belongs to the next wake.
4. **Conflicts:** run the conflict procedure.
5. **Failed checks:** run the failure procedure.
6. **Waiting:** pending, queued, in-progress, missing, neutral, and skipped checks are waiting unless repository evidence makes them blocking.
7. **Green and unmerged:** report the PR ready and keep watching — approval, queue, or human merge is someone else's move — unless the user explicitly requested a merge; then run the merge procedure.

Before modifying files, require a clean worktree and a verified route to the source branch. Fetch and fast-forward a clean source branch that advanced remotely; pause on a dirty or divergent worktree, a wrong branch, or a detached checkout without a safe push target. After any push, verify the remote source branch matches `HEAD`.

When an event needs no action, end your turn without a message.

## Conflict procedure

Act when GitHub reports conflicts, or branch protection blocks progress until the head is current.

1. Follow explicit repository guidance; otherwise merge the current base into the source branch, preserving two-parent history. A newer base alone is not a reason to update the branch.
2. Resolve when repository evidence, tests, and both sides establish one behavior-preserving result; use documented regeneration for generated files.
3. If the source advances concurrently, abort, fetch both refs, and retry once from the new head. A second race pauses.
4. If competing behaviors remain plausible, capture the paths and the ambiguity, abort back to the verified clean head, and pause for the decision.
5. Run focused tests, invoke `$commit`, create the merge commit, and push. Repository-required rebasing or history rewriting pauses.
6. Leave validation of the pushed head to the next wake.

## Failure procedure

- For current-head GitHub Actions conclusions `failure`, `error`, `timed_out`, `cancelled`, or `action_required`, invoke `$pr-action-error-resolver`.
- For another current-head required status with a recognized machine diagnostic, inspect its linked logs and comment, fix the root cause, run focused checks, invoke `$commit`, and push.
- A current-head passing status plus a machine failure diagnostic may be a later delivery failure; establish that link from build evidence before acting.
- Never repeat an attempted repair against unchanged evidence. If a resolver cannot progress, or the same head fails identically after its focused fix, pause and report the blocker.

## Merge procedure

An explicit user request to merge is separate authorization; without one, report the PR ready and keep watching. Right before merging, `git fetch` and re-check the PR on the latest head: merge only when the merge gate passes and the branch is current with its base. When commits that landed on the base after the last green run touch this PR's files, update the branch first (conflict procedure) and wait for a fresh green run. After merging, report per step 1.

## Pause

When required user direction blocks safe progress, stop the watcher — `unwatch_pull_request` in T3 Code; elsewhere leave `pr-wait` stopped — and ask a focused question under the [decision policy](../AGENTS.md#scope-and-design). Resume the same watch after the blocker is resolved and the blocked action is complete, unless the user cancels monitoring.
