---
name: pr-review-resolver
description: Address all unresolved review threads on the current pull request, react and reply, resolve them, commit, and push.
metadata:
  short-description: Address and resolve PR review threads
---

Use available GitHub MCP tools to inspect and address review threads; use `gh` for operations those tools do not expose. Use `$commit` before committing. Treat invocation as authorization to handle every unresolved thread and perform the requested GitHub writes.

Recover accepted direction and resolve missing choices under the [decision policy](../AGENTS.md#scope-and-design). Ask a focused question only when user direction is required; use a full `$grill-me` interview when explicitly requested.

Verify each bot finding against the current source before changing code.

- Addressed: commit and push the change, react 👍 to the initial comment, reply with the commit SHA and a concise description, then resolve.
- Not addressed: react 👎 to the initial comment, reply with the reason, then resolve.

Verify all reviewed threads are resolved, the remote branch matches `HEAD`, and the worktree is clean.

## Bot re-review

Handle incoming bot findings normally. Request another external bot review only under explicit user authority or the accepted repository review policy. Follow that policy's criteria for material changes or unresolved risk; a new commit alone does not authorize another request. Carry a user's stop instruction into the controlling monitor under the [correction policy](../AGENTS.md#scope-and-design).
