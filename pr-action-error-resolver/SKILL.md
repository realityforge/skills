---
name: pr-action-error-resolver
description: Resolve the latest failed GitHub Actions run on the current pull request, commit, push, and verify it passes.
metadata:
  short-description: Resolve the latest PR Actions failure
---

Use available GitHub MCP tools to inspect failed Actions runs, read job logs, and rerun jobs when appropriate; use `gh` for operations those tools do not expose. Use `$commit` before committing. Treat invocation as authorization to implement the focused fix, rerun when appropriate, commit, push, and perform the required GitHub writes without pausing for approval.

Recover accepted direction and resolve missing choices under the [decision policy](../AGENTS.md#scope-and-design). Investigate repository and Actions evidence before asking a focused decision question; use a full `$grill-me` interview when explicitly requested.

When resolving a detected failure requires a rebuild or rerun, inspect the original run's full job logs and annotations for warnings, including successful jobs. Determine each distinct warning's cause and impact from the relevant code, configuration, and tool documentation. Fix warnings that reveal real problems within the focused repair scope. For confirmed non-issues, prefer correcting their source; otherwise use narrowly scoped suppression only when it preserves behavior and visibility of actionable diagnostics. Leave warnings visible when their impact is uncertain or no safe remedy is available, and report the evidence and remaining limitation.

After rebuilding or rerunning, inspect the completed run's logs and annotations again to verify warning fixes or suppressions and assess any newly exposed warnings under the same criteria. A green check alone does not complete this review. Report which warnings were fixed, safely suppressed, or left visible and why; identify any logs that could not be inspected.

Verify the relevant local checks pass, the targeted PR check is green, the remote branch matches `HEAD`, and the worktree is clean.
