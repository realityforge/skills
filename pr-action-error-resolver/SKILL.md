---
name: pr-action-error-resolver
description: Resolve the latest failed GitHub Actions run on the current pull request, commit, push, and verify it passes.
metadata:
  short-description: Resolve the latest PR Actions failure
---

Use available GitHub MCP tools to inspect failed Actions runs, read job logs, and rerun jobs when appropriate; use `gh` for operations those tools do not expose. Use `$commit` before committing. Treat invocation as authorization to implement the focused fix, rerun when appropriate, commit, push, and perform the required GitHub writes without pausing for approval.

Recover accepted direction and resolve missing choices under the [decision policy](../AGENTS.md#scope-and-design). Investigate repository and Actions evidence before asking a focused decision question; use a full `$grill-me` interview when explicitly requested.

Verify the relevant local checks pass, the targeted PR check is green, the remote branch matches `HEAD`, and the worktree is clean.
