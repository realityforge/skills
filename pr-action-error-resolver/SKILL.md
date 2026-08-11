---
name: pr-action-error-resolver
description: Resolve the latest failed GitHub Actions run on the current pull request, commit, push, and verify it passes.
metadata:
  short-description: Resolve the latest PR Actions failure
---

Use `github:gh-fix-ci` for diagnosis and `$commit` before committing. Treat invocation as authorization to implement the focused fix, rerun when appropriate, commit, push, and perform the required GitHub writes without pausing for approval.

Invoke `$grill-me` only when repository and Actions evidence cannot settle a required user decision.

Verify the relevant local checks pass, the targeted PR check is green, the remote branch matches `HEAD`, and the worktree is clean.
