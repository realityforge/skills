# Implementation Review

Use this instruction after implementation is complete and before final success
reporting when active plan artifacts exist.

## Post-Implementation Issues

Do not open an issue register for every follow-up.

Use a persistent issue register only when:

- a persistent plan tree is active
- the issue changes accepted scope or sequencing
- the issue needs user approval before implementation
- multiple related follow-ups must be tracked across turns

Otherwise, fix the issue within the current scope, validate it, and summarize
the evidence.

For tracked issues, include:

- stable issue ID
- status (`open`, `planned`, `resolved`, or `deferred`)
- context and evidence
- proposed response
- validation expectation
- linked task IDs, if any

Ask for explicit approval before editing implementation files only when the
response changes accepted scope, has meaningful product/design tradeoffs, or
the user requested approval-first handling.

## Implementation Alignment Review

After implementation is complete and before final success reporting, run the
built-in iterative implementation alignment review loop when there is an active
plan artifact to compare against the implementation.

This normally applies to persistent plan tree work. For lightweight
implementation, run it only when the work was explicitly driven by an existing
plan artifact; otherwise rely on the normal closeout validation because there
is no plan artifact to review against.

Defaults:

- max rounds: `5`, unless the user gives another limit
- reviewer: clean read-only subagent using the review rubric below
- main agent owns fixes, validation, evidence updates, and final reporting

Before spawning, resolve the repository root, plan artifacts, implementation
scope, review mode, required gates, and round limit. Infer these from context
when safe; ask only if the review target is genuinely ambiguous.

Use `delta` mode when the request is a follow-up round, names prior findings,
or says only specific fixes changed. Use `full` mode otherwise.

Use focused inputs:

- plan artifact paths
- repository or workspace root
- review mode: `full` or `delta`
- maximum review rounds, defaulting to `5` unless the user set one
- current implementation scope, such as uncommitted changes, recent commits, or
  specific files
- relevant prior findings for delta rounds
- required validation gates from the plan, when available

For each round:

1. Send the subagent a focused read-only prompt: repository root, plan paths,
   implementation scope, relevant prior findings, required gates, and
   the review rubric below. Ask for `Findings` and a `Scorecard` only when full
   mode or merge/release gating needs it. Do not pass full conversation context
   unless necessary.
2. Assess each finding against repository evidence.
3. Fix valid or partially valid findings with the narrowest implementation,
   test, or evidence change. Reject only with concrete evidence.
4. Run targeted validation for changed behavior. Run the plan's full gate
   before final success, or explain why it could not be run.
5. Update plan/task-board/evidence artifacts only when status, scope, or
   validation evidence changed.
6. Re-review unless the subagent reports `Findings: none`, no actionable
   findings remain after assessment, or max rounds is reached.

Do not weaken the plan to match incomplete implementation. Preserve unrelated
user changes. Do not commit unless asked.

Final report should include rounds run, final review result,
fixes/rejections/leftovers, validation results, evidence updates, and subagent
closure.

## Review Rubric

Judge repository-to-plan alignment. Be strict, evidence-backed, and concise.

Identify the review scope first: plan paths, repository root, diff or commit
range, implementation scope, and whether the round is `full` or `delta`.

Evidence order:

1. Inspect `git status` and changed-file shape first.
2. Read only the plan sections needed to extract concrete promises: behavior,
   APIs, files, tests, validation, rollout, and constraints.
3. Map promises to changed files, tests, and recorded evidence.
4. Read implementation files only where they prove or disprove a promise.
5. Inspect recent commits only when named, the working tree is clean, or
   history is needed to explain alignment.
6. Treat task-board entries and summaries as claims. Verify the underlying
   code, tests, or command evidence before relying on them.

In full mode, check the plan promises against current repository state.

In delta mode, verify the named prior findings, changed files, and any new
drift introduced by the fix. Do not re-review the whole plan unless the diff
changed broadly.

Report mismatches that matter:

- promised work missing or partial
- implementation contradicts the plan
- unplanned scope that changes behavior, API, architecture, or risk
- tests or validation promised but absent, weak, stale, or not wired into gates
- evidence claims that overstate what was checked
- code that exists but is disconnected, dead, stubbed, or superficially tested
- prior-review fixes that do not actually close the prior finding

Do not report harmless wording drift, accepted plan changes, or minor style
issues unless they affect alignment or safety.

Prefer decisive evidence over exhaustive reading. For large reviews, stop after
the highest-risk actionable findings unless exhaustive coverage was requested.
Do not rerun heavy validation in a read-only review unless current evidence is
missing or suspicious. Cheap non-mutating checks are fine.

Start with `Findings`.

Use compact bullets:

- `[P1] Short title. Evidence: file/line or command result. Why it matters.
  Fix: concrete next step.`

If there are no findings:

`Findings: none. Checked: <short evidence list>. Residual risk: <none or
specific unverified gate>.`

Include a scorecard only when requested, the review is full mode, or the result
will gate merge or release.
