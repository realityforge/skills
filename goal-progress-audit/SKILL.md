---
name: goal-progress-audit
description: Audit a long-running Codex worker thread against its original goal and recommend the highest-value course correction.
disable-model-invocation: true
---

Review one pinned worker thread per invocation. A scheduled replay is one audit, not a new schedule. Keep the monitor in a separate thread so its analysis does not consume the worker's context.

1. Resolve the worker from an explicit thread link or ID. If the target is ambiguous, ask for it. On the first audit, use `read_thread` and its older-turn cursors to establish the original user request, active Goal if visible, later user corrections, and completion criteria. On later audits, reuse that baseline and read only new turns unless the goal changed. Inspect relevant tool results, checkout, or artifacts when the thread summary cannot establish actual progress.
2. Compare the current work with the goal's unfinished major outcomes. Look for repeated attempts against unchanged evidence, detours into tooling or process, polishing a minor detail while a major outcome remains open, and claims of completion unsupported by the agreed evidence. Distinguish a genuine blocker from a slow but productive step; elapsed time alone is not a loop.
3. Review new tests, validation tools, and process documents for a continuing purpose. A regression test or required operational document may be part of the finished product. A one-off proof or migration aid with no remaining consumer is a cleanup candidate. Recommend removal only after checking its current use and the project's requirements.
4. If there is a material issue, choose **one** highest-value correction. State the observed evidence, the likely cause (labeled as inference when necessary), the goal impact, and the next concrete action for the worker. If the same correction was already given, repeat it only when new evidence changes the recommendation; otherwise report that it remains unresolved. If the evidence is insufficient, say exactly what to inspect next. Stay quiet when progress is aligned and no action is needed.

Default to read-only review. A report in the monitor thread should contain a short, ready-to-send worker instruction when intervention would help. Send that instruction to the pinned worker thread only when the user has explicitly authorized cross-thread messages. Never edit the worker's files or change its Goal as part of this audit.
