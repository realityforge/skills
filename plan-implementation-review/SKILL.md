---
name: plan-implementation-review
description: Use when checking whether repository state, diffs, or recent commits actually satisfy an accepted plan, task board, rollout plan, or implementation checklist.
---

# Plan Implementation Review

Judge repo-to-plan alignment. Be strict, evidence-backed, and concise.

## Mode

Use `delta` mode when the request is a follow-up round, names prior findings, or says only specific fixes changed.
Use `full` mode otherwise.

- Full mode: check the plan promises against current repo state.
- Delta mode: verify the named prior findings, changed files, and any new drift introduced by the fix. Do not re-review the whole plan unless the diff changed broadly.

If no plan text/path is provided, ask for it or inspect the referenced plan path before reviewing.

## Evidence Order

1. Identify review scope: plan paths, repo root, diff/commit range, and whether this is full or delta.
2. Inspect `git status` and changed-file shape first.
3. Read only the plan sections needed to extract concrete promises: behavior, APIs, files, tests, validation, rollout, constraints.
4. Map promises to changed files, tests, and recorded evidence.
5. Read implementation files only where they prove or disprove a promise.
6. Inspect recent commits only when the user names them, the working tree is clean, or history is needed to explain alignment.
7. Treat task-board entries and summaries as claims. Verify the underlying code, tests, or command evidence before relying on them.

## What Counts As A Finding

Report mismatches that matter:

- promised work missing or partial
- implementation contradicts the plan
- unplanned scope that changes behavior, API, architecture, or risk
- tests or validation promised but absent, weak, stale, or not wired into gates
- evidence claims that overstate what was checked
- code that exists but is disconnected, dead, stubbed, or only superficially tested
- prior-review fixes that do not actually close the prior finding

Do not report harmless wording drift, already-accepted plan changes, or minor style issues unless they affect alignment or safety.

## Efficiency Rules

Prefer decisive evidence over exhaustive reading.
For large reviews, stop after the highest-risk actionable findings unless the user asked for exhaustive coverage.
For clean delta rounds, output only the checked fixes, any residual risk, and `Findings: none`.
Do not rerun heavy validation in a read-only review unless current evidence is missing or suspicious. Cheap non-mutating checks are fine.

## Output

Start with `Findings`.

Use compact bullets:

- `[P1] Short title. Evidence: file/line or command result. Why it matters. Fix: concrete next step.`

If there are no findings:

`Findings: none. Checked: <short evidence list>. Residual risk: <none or specific unverified gate>.`

Include a scorecard only when the user asks, the review is full mode, or the result will gate merge/release.
