---
name: root-cause-analysis
description: Root-cause analysis for recurring failures, failed fixes, incident reviews, decision postmortems, and suspected workarounds.
---

# Root cause analysis

Trace an observed failure through evidence to the causes that explain it and can prevent recurrence. Five Whys is a prompt for continuing the investigation, not a required count or output format.

## Process

1. Define the failure as observable facts: actual behavior, expected behavior, conditions, timing, and impact. Separate evidence from assumptions.

2. Reproduce the failure when practical. Inspect the original errors, logs, traces, code, configuration, history, and environment before choosing an explanation.

3. Build a causal graph. Distinguish:

   - **Trigger:** the event that exposed the failure.
   - **Mechanism:** how the failure occurred.
   - **Enabling condition:** what allowed the mechanism to operate.
   - **Escape:** why existing checks or detection did not catch it.
   - **Contributing cause:** an independent factor that changed likelihood or impact.

   Ask why each evidenced condition existed. Branch when causes are independent. Distinguish recurrence of the original failure from a new downstream failure.

4. Validate every accepted causal edge:

   - Evidence supports the connection.
   - The cause explains the observed scope and timing.
   - Removing the cause should prevent the failure within that scope.
   - Reintroducing it reproduces the failure when a safe focused test is practical.

   Test competing explanations. Reject them with evidence or report the remaining uncertainty and its effect on confidence.

5. Stop when the causes are specific, evidenced, actionable, and sufficient to explain the failure. Treat labels such as human error, bad luck, missing tests, and misconfiguration as prompts to identify the mechanism or changeable condition they describe.

6. Report the smallest useful causal narrative. Include the observed failure, causal graph, evidence, root and contributing causes, confidence, rejected hypotheses, and unresolved uncertainty. When corrective action is in scope, distinguish immediate recovery, recurrence prevention, and detection, then verify the original failure against the change.

## Completion criterion

Every accepted causal edge has evidence. Plausible competing explanations are rejected or marked uncertain. Each proposed action maps to an identified cause, and its verification tests the original failure.
