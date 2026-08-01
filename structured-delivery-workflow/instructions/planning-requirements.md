# Stage 1: Requirements Baseline

Use this instruction when requirements are absent, changed, or contradicted by
evidence.

In the default plan tree, use `00-requirements.md` to define what the work must
accomplish independently of the implementation design. Record the intended
outcomes, scope boundaries, constraints, acceptance criteria, and unresolved
questions.

## Requirements Entry Path

Start from the strongest available requirements baseline.

Use the **pre-aligned path** when the user has already confirmed shared
understanding, including through `grill-me`, or has directed the work from an
accepted specification or requirements artifact:

- record the source and basis of acceptance
- preserve settled outcomes, constraints, and decisions
- check them against current repository evidence
- reopen a settled point only when evidence contradicts it, scope has changed,
  or its acceptance criteria cannot be evaluated

Use the **evidence-led path** when no accepted baseline exists:

- derive candidate requirements from the request, repository instructions,
  referenced issues or specifications, current behavior, code, and tests
- resolve factual questions from evidence before asking the user
- treat a clear original request as acceptance when it leaves no material
  requirements choice open
- when a material choice remains, present the evidence, recommendation, and
  decision needed before completing the baseline

If evidence contradicts a pre-aligned requirement, surface the conflict and
resolve it before progressing to implementation design.

The requirements baseline is complete when:

- its source and basis of acceptance are recorded
- intended outcomes, in-scope work, and out-of-scope boundaries are explicit
- material constraints and acceptance criteria are checkable
- evidence-answerable questions have been resolved
- no blocking requirements question remains open
- user decisions and material assumptions are recorded
- it states required outcomes rather than implementation choices, except where
  the implementation itself is a requirement or constraint

After the completion gate, read `review-and-approval.md` and run the built-in
requirements review before starting implementation design.
