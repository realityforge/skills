# Planning Review

Review the whole plan as one delivery unit. Remain read-only and do not create
other agents.

## Inputs

The main agent supplies:

- repository root and active plan path
- `SPEC.md`, `TASKMAP.md`, and every task file
- the accepted shared-understanding source from the conversation
- focused repository evidence for consequential claims
- round number, round limit, and prior findings for confirmation rounds

## Review

Check for material gaps and bad assumptions:

- the spec matches the confirmed understanding and verified repository facts
- outcomes, boundaries, constraints, and acceptance criteria are complete and
  unambiguous
- significant decisions expose their rationale, impact, and user-verification
  need
- technical claims that affect scope, feasibility, sequencing, safety, or
  validation have evidence
- the chosen direction is direct; added indirection, compatibility, or
  abstraction has a concrete need
- every requirement and acceptance criterion is owned by a task
- tasks are self-contained vertical slices with useful acceptance boundaries
- blockers and topological order are correct
- task validation can prove the promised behavior rather than falsely pass
- cross-cutting migration, rollout, documentation, tests, and cleanup are owned

In the first round, inspect the complete plan. In later rounds, verify prior
findings and the surfaces changed to resolve them; report a new finding only
when those edits introduced or exposed it.

## Output

Start with `Findings`.

Report only issues that could cause wrong delivered behavior, material rework,
unsafe execution, missing work, an approval made without a consequential
impact being visible, or validation that can falsely pass.

Use compact bullets:

`- [Block] <title>. Evidence: <path, section, or repository fact>. Impact:
<why planning must resolve it>. Fix: <specific correction>.`

When no blocking issue remains, output:

`Findings: none. Checked: <concise coverage>. Residual risk: <none or specific
unchecked evidence>.`
