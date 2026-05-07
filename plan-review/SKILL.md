---
name: plan-review
description: Use when the user asks to review a plan, implementation plan, execution plan, task breakdown, rollout plan, or migration plan for gaps, ambiguity, unsafe sequencing, missing details, hidden assumptions, or unconsidered work. This skill stress-tests whether the plan is specified well enough to implement safely.
---

# Plan Review

Review plans aggressively but concisely. The goal is to find what would make implementation unsafe, vague, brittle, or incomplete.

Prefer surfacing unconsidered items over praising what is already present.

## Workflow

1. Read the full plan before judging any part of it.
2. If the plan references real files, systems, APIs, migrations, or repo context, inspect that context before reviewing.
3. Review both:
   - plan intent: what outcome is being promised
   - plan execution: how the work is broken down and validated
4. Look for omissions, not just contradictions. Assume missing details matter unless they are genuinely trivial.
5. Order findings by implementation risk and safety impact.
6. For every finding, include the missing decision, constraint, or correction needed to make the plan safer.
7. Keep the review dense. No long intro, no padded summary, no generic encouragement.

## Coverage

Check the plan against this list and call out any weak or missing area that matters:

- goal clarity and success criteria
- scope boundaries, exclusions, and non-goals
- assumptions, prerequisites, and external dependencies
- interfaces, APIs, schemas, or contract changes
- data flow, state changes, persistence, and migration impact
- edge cases, failure modes, and rollback behavior
- task sequencing, dependency ordering, and decomposition quality
- validation strategy, tests, observability, and acceptance criteria
- rollout, compatibility, operational safety, and cutover concerns when relevant
- repo or system checks the plan assumes but does not explicitly require

Also check whether the plan leaves critical design choices to the implementer. If so, treat that as a finding.

## Output Contract

Start with `Findings`.

Each finding should be short and complete:

- title: short label
- problem: why this matters
- gap: what is missing, ambiguous, unsafe, or unvalidated
- fix: the missing decision, constraint, or task needed to close it

Prefer findings like:

- "Missing success criteria for phase completion"
- "Migration step lacks rollback boundary"
- "Task breakdown assumes API shape without confirming existing callers"
- "Validation omits failure-path coverage"
- "Scope boundary between refactor and behavior change is unresolved"

Then include `Scorecard` with terse ratings for:

- completeness
- clarity
- implementation safety

Use either `1-5` or `low/medium/high`, but stay brief and consistent within a review.

## Review Stance

- Default to critique-plus-fix, not plan rewrite.
- Do not spend words on obvious strengths unless they affect risk triage.
- If the plan is severely underspecified, say that directly and focus on the highest-leverage missing decisions.
- If repo inspection changes the review materially, mention the concrete mismatch between the plan and the actual code or files.
- If a risk is conditional, state the condition instead of speculating broadly.

When the user asks to "review a plan" or "identify gaps," this skill should bias toward thorough issue discovery with compressed wording.
