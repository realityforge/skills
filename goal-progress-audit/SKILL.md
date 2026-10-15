---
name: goal-progress-audit
description: Audit a long-running agent job against the user's agreed outcome and directly correct material drift.
disable-model-invocation: true
---

Keep a worker focused on the user's agreed outcome. Direct invocation authorizes a concise corrective message to the named worker conversation. A saved schedule must name the worker and explicitly carry that authorization. Each scheduled run performs one audit; it does not create another schedule. Resolve and retain the worker's exact identity before reviewing it.

1. Establish the goal from the original request, later user corrections, and evidence required for completion. Reuse the previous audit's baseline when available, updating it for new instructions. If the worker cannot be identified unambiguously, ask for its identity.
2. Check actual progress in the worker's conversation, tool results, and artifacts available to the monitor. Identify the major unfinished outcome and what changed since the last audit. Look for repeated attempts without new evidence, detours into process or tooling, minor polish ahead of major work, and unsupported completion claims. Time spent alone is not evidence of a loop.
3. Check whether new tests, validation tools, and documents serve the finished work. A durable regression test or required document may belong in the result. A one-off proof or transition aid with no remaining consumer is a cleanup candidate once its purpose is complete.
4. When a material issue exists, send the worker **one** highest-value correction through the available messaging channel. State the evidence, its effect on the goal, the next concrete action, and when to reassess. Label inferred causes as inferences. Record what was sent in the monitor conversation. If the same advice was already sent and nothing changed, report the unresolved issue to the user instead of repeating it to the worker.

Stay quiet when progress is aligned. If the worker or its messaging channel is inaccessible, report the specific barrier and the correction that would have been sent. The worker owns implementation; the monitor steers through messages.
