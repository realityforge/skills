---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

Output the handoff as:
- a single fenced code block in the chat so the user can copy it in one click.
- to a path specified by the user or produced by `mktemp -t handoff-XXXXXX.md`.

Suggest the skills to be used, if any, by the next session.

Do not duplicate content already captured in other artifacts. Reference them by path or URL instead.

DO NOT duplicate content present in AGENTS.md in the target project. The handoff is session-specific only.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
