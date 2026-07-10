---
name: plan-review
description: Review a plan, implementation plan, task breakdown, rollout, or migration plan for blocking gaps, unsafe assumptions, unclear decisions, weak sequencing, or missing validation before implementation.
---

# Plan Review

Stress-test whether the plan is specific enough to implement safely.

Read the plan first. Inspect referenced repo or system context only when needed to verify a material assumption, contract, dependency, or validation claim. Do not bulk-load context or restate the plan.

Find issues that would block implementation, create avoidable risk, or leave a critical decision to the implementer. Ignore cosmetic gaps and ordinary implementation discretion.

Check the relevant risk surface: scope, success criteria, interfaces and contracts, data and state changes, migrations, sequencing, failure and rollback behavior, validation, rollout and operations, and external dependencies.

Start with `Findings`.

For each finding, include:

- the risk or ambiguity
- why it matters
- the concrete plan change needed

Use evidence when repo or context inspection affected the finding. Order findings by implementation risk. Keep wording dense and skip praise.

If there are no material issues, write `Findings: none` and mention only residual risk or unchecked context that matters.

Do not rewrite the plan unless the user asks.
