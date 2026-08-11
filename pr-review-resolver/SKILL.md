---
name: pr-review-resolver
description: Address all unresolved review threads on the current pull request, react and reply, resolve them, commit, and push.
metadata:
  short-description: Address and resolve PR review threads
---

Use `github:gh-address-comments` for review work and `$commit` before committing. Treat invocation as authorization to handle every unresolved thread and perform the requested GitHub writes.

Invoke `$grill-me` if further user context is needed.

- Addressed: commit and push the change, react 👍 to the initial comment, reply with the commit SHA and a concise description, then resolve.
- Not addressed: react 👎 to the initial comment, reply with the reason when useful, then resolve.

Verify all reviewed threads are resolved, the remote branch matches `HEAD`, and the worktree is clean.
