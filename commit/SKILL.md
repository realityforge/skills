---
name: commit
description: "Use before creating git commits"
---

Create intentional local commits for intended changes. This skill does not authorize pushing; push only when explicitly requested.

- Treat args as intent: paths/globs limit staging, free text guides the message.
- Inspect status and relevant diffs. Stage only intended changes, inspect the staged diff before each commit, and ask only when file ownership is ambiguous.
- Default to one commit; split when requested or when changes are clearly independent.
- Match user guidance and repo history. Check recent log only if style is unclear. If no stronger style exists, use Conventional Commit: `<type>(<scope>): <summary>`.
- Keep subjects imperative, <=72 chars, and without a period. Add a body only when it explains useful what/why context.
- Run normal hooks. Do not bypass hooks or add sign-offs, footers, or breaking-change markers unless explicitly required.
