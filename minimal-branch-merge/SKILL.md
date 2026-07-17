---
name: minimal-branch-merge
description: Merge a fetched source branch into the current branch, defaulting to the remote default branch, and retain only the delta required by the current branch's mission.
---

On the current branch, merge the requested source or the remote default. The result must be the smallest mission-required diff from that source.

1. Read repository instructions and status. Never discard uncommitted work without explicit authorization.
2. `git fetch --prune origin`. Resolve the source argument or `refs/remotes/origin/HEAD`; inspect refs, graph, merge base, and tracking state.
3. Establish the mission from the request, PR/issue, branch name, and focused commits. Ask only when evidence cannot resolve a material ambiguity.
4. Fast-forward if the current branch is the source's ancestor; otherwise merge the fetched ref without committing and preserve a merge parent.
5. Audit the source-relative diff. Source wins unless evidence proves a difference is required. Delete upstreamed duplication, unused/out-of-closure targets, stale scaffolding, and unrelated edits. Use queries, history, generators, builds, and tests as evidence.
6. Resolve conflicts by mission, update sources of truth, regenerate outputs, and format.
7. Validate narrowly, then broadly as warranted. Inspect `git diff --check`, final source-relative and staged diffs, status, and merge parents.
8. Use the `commit` skill. Push only when explicitly requested; verify the remote ref and clean tracking state.

Report the retained source-relative delta, removed scope, validation results, commit, push state, and any known failing checks.
