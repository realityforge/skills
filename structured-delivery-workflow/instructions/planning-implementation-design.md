# Stage 2: Implementation Design

Use this instruction after the requirements baseline passes review and the
implementation design is absent or affected.

In the default plan tree, use `10-implementation-plan.md` to define how the
requirements baseline will be satisfied. Record the chosen approach, affected
components and contracts, risks, dependencies, sequencing, and validation
strategy.

## Derive the Design

Derive the implementation design from the requirements baseline rather than
restating the requirements as tasks:

- map each requirement, or coherent group of requirements, to the design
  response that satisfies it
- start with the simplest direct design that could satisfy the baseline; add
  indirection, compatibility paths, or new abstractions only when their need is
  supported by evidence
- identify load-bearing assumptions whose failure would materially change the
  architecture, scope, sequencing, or validation strategy
- verify each load-bearing assumption through code, authoritative
  documentation, or a focused experiment before relying on it
- test consequential capability claims, especially that a direct approach
  cannot work, against the actual system rather than inference alone
- record credible alternatives and trade-offs only when they explain why the
  chosen design is preferable or prevent likely rediscovery

Keep requirement outcomes authoritative. If design investigation contradicts
the requirements baseline, return to Stage 1 and resolve the conflict before
continuing.

The implementation design is complete when:

- every requirement maps to a design response
- the simplest direct approach has been assessed and any added indirection or
  abstraction is justified
- every load-bearing assumption has supporting evidence
- material assumptions, risks, dependencies, and compatibility concerns are
  explicit
- material alternatives and trade-offs are recorded when their rationale will
  matter during implementation or future reconsideration
- the intended validation demonstrates the requirements and acceptance
  criteria
- no unresolved design question blocks task breakdown

After the completion gate, read `review-and-approval.md` and run the built-in
design review before creating the detailed task breakdown.
