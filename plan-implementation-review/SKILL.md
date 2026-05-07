---
name: plan-implementation-review
description: Use when the user asks to check whether code, repository state, uncommitted changes, or recent commits align with a plan, implementation plan, rollout plan, migration plan, or task breakdown. This skill compares the intended work against the actual repository state and identifies gaps, fumbles, divergence, extra work, and unverified implementation.
---

# Plan Implementation Review

Review implementation against the plan aggressively but concisely. The goal is to determine whether the repository actually matches what the plan said would be built.

Prefer concrete repo evidence over inference, and prefer finding misalignment over describing what already looks fine.

## Workflow

1. Read the full plan first and extract the concrete promised work.
2. Inspect the current repository state and the files most relevant to those promised changes.
3. If the repo is in git, inspect uncommitted changes first.
4. Inspect recent commits when they materially affect current alignment or help explain divergence.
5. Compare plan promises against actual implementation, tests, and repo evidence.
6. Produce flat findings ordered by alignment risk and implementation safety.
7. For every finding, include the mismatch and the missing fix, check, or implementation step needed.
8. Keep the review dense. No long intro, no padded summary, no generic praise.

If the user gives no plan text, ask for the plan or inspect the referenced plan document/path before reviewing alignment.

If git history is unavailable, fall back to current repo/file state and say that commit-based evidence was not available.

## Coverage

Check for these forms of misalignment:

- planned work that is absent
- planned work that is only partially implemented
- implementation that contradicts the plan
- extra work not justified by the plan
- incorrect sequencing or incomplete task closure
- missing tests, validation, rollout steps, or operational checks promised by the plan
- code that appears implemented but is stubbed, disconnected, dead, or unverified
- local diffs or recent commits that materially weaken alignment
- plan items that seem complete in code but do not match the intended behavior or interface

Treat missing or partial implementation as findings by default, not only explicit contradictions.

## Output Contract

Start with `Findings`.

Each finding should be short and complete:

- title: short label
- problem: why the mismatch matters
- evidence: what the repo, diff, test surface, or commit history does or does not show
- fix: what implementation step, validation step, or decision is needed to restore alignment

Prefer findings like:

- "Planned validation step has no repo evidence"
- "Implementation covers only part of the promised behavior"
- "Recent commit changed interface beyond plan scope"
- "Uncommitted diff bypasses the rollout step described in the plan"
- "Task marked complete but failure-path tests are absent"

Then include `Scorecard` with terse ratings for:

- plan alignment
- implementation completeness
- implementation safety

Use either `1-5` or `low/medium/high`, but stay brief and consistent within a review.

## Review Stance

- Default to strict alignment review, not benefit-of-the-doubt interpretation.
- Do not restate the whole plan. Focus on mismatch, absence, extra scope, and weak evidence.
- If a mismatch is only likely rather than proven, say what evidence is missing and what check would resolve it.
- If recent commits materially explain the current state, mention that linkage directly.
- If the implementation appears ahead of the plan, treat that as potential scope drift unless the plan or context justifies it.

When the user asks whether the repo "matches the plan" or asks for "alignment," this skill should bias toward evidence-backed findings with compressed wording.
