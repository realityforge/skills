# Closeout

Close only after implementation review passes and any
[required knowledge promotion](implementation.md#promote-durable-knowledge) is
complete.

## Cleanup gate

Verify that all tasks, simplification, task and full-scope validation,
implementation review, and required promotion are complete, with
[passes valid for the final substantive changes](../review/policy.md#pass-validity).

Apply the [global cleanup rules](../../AGENTS.md#test-and-clean-up) to documents
completed by this work.

## Deliver

Deliver to the point the user or repository instructions set; without one,
open a pull request and leave the merge to the user. Write the pull request
description with `$pull-request-descriptions`, drawing the problem, outcome,
and significant decisions from `SPEC.md`. Then delete the plan tree.

## Handoff

Report:

- Delivered outcome, significant decisions, and impacts.
- Validation and review results, and residual risk or skipped checks.
- Canonical artifact links and unrelated uncommitted work.
- For pull request delivery, the URL and check status.
