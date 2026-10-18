---
name: handoff
description: Distill the current task into minimal, high-value context for another agent. Use when the user asks to hand off, transfer, continue, or preserve work for a new thread, session, or subagent.
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

Create a requested new thread or subagent with the handoff as initial context. Otherwise write it to the user-specified path, project local `tmp/` dir or `mktemp -t handoff-XXXXXX.md` in that order of priority; report the path.

Suggest the skills to be used, if any, by the next session.

## Core Principles

1. **Current authority and state.** Carry the accepted outcome, authority sources, scope, live exceptions, checkpoints, and stopping conditions. Include temporary restrictions' purpose and accepted expiry condition. Link the controlling goal, relevant saved schedule, and current state owners so the recipient can recover later corrections and execution state. Describe progress as observations to verify; the recipient chooses actions within that authority.
2. **Reference, don't duplicate.** Do not paste content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs, design docs). Point to them by path or URL.
3. **Capture the "why".** Decisions and rejected approaches are the most valuable and least recoverable information. Code shows *what*; only you remember *why* and *what failed*. Include applicable user corrections, their source, meaning and scope, and any affected peers still unchecked.
4. **Trust nothing blindly.** Frame all claims as context to verify against the actual code, not facts to accept.
5. **Redact secrets.** Strip API keys, tokens, passwords, and personally identifiable information. Reference where credentials live (e.g. ".env.local, not committed") — never their values.
6. **Be ruthless.** Every line must be something the next agent cannot trivially get by reading the code or project config. Cut anything obvious, redundant, or explanatory.
7. **Omit Project Rules**: DO NOT duplicate content present in AGENTS.md in the target project. The handoff is session-specific only.
