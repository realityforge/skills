---
name: improve-codebase-architecture
description: Find and examine architecture improvements in a codebase.
disable-model-invocation: true
---

# Improve Codebase Architecture

Use `$codebase-architecture` for the shared vocabulary and design discipline.
Read repository instructions and project design language before judging the
architecture; project terms specialize the shared language.

If any of the `docs/(adr|glossary|specs|deferred)` dirs exists or the file `.domain-modeling.toml` exists then use the $domain-modeling skill.

This skill diagnoses opportunities. Keep the scan and report read-only.
Implementation or durable artifact changes require execution authority under
the [decision policy](../AGENTS.md#scope-and-design); an explicitly requested
full `$grill-me` interview retains its confirmation gate.

## 1. Set the scope

Use an area, pain point, or Module named by the user. Otherwise inspect enough
recent history to find code that changes repeatedly, then use those paths as
leads rather than proof. Widen the scan when history has no clear concentration.

Read the instructions, design language, domain artifacts, and durable decisions
that govern the chosen area.

Continue when the scope and every authority bearing on it are explicit.

## 2. Trace the architecture

Follow representative behavior through callers, Modules, tests, dependencies,
configuration, build definitions, and failure paths. Inspect enough examples to
distinguish recurring friction from an awkward isolated case.

Look for evidence that:

- an Interface exposes nearly as much complexity as its Implementation;
- callers repeat policy, ordering, failure handling, or dependency coordination;
- understanding one responsibility requires crossing several shallow Modules;
- tests preserve internal call shapes while caller-visible behavior remains hard
  to verify;
- a Seam lacks real variation, or variation exists without a clear Seam;
- logical and physical structure are being treated as equivalent without an
  explicit reason.

Apply the deletion test to each suspected shallow Module. Use the deepening and
structural-axis branches of `$codebase-architecture` when they apply.

Continue when each candidate is supported by current code, representative
callers and tests, and the governing project decisions.

If no candidate clears that bar, report what was inspected and why no change is
justified, then stop.

## 3. Present the candidates

Read [HTML-REPORT.md](HTML-REPORT.md), then write a fresh report to a repository
local temp directory, or if no such directory exists the OS temp directory, as
`architecture-review-<timestamp>.html`. Open it with an available viewer and
give the user its absolute path.

For each candidate include:

- affected files and representative callers;
- the current responsibility and Interface friction;
- the evidence that makes it more than a file-shape preference;
- the responsibility change worth exploring, without designing its Interface;
- expected changes in Depth, Leverage, Locality, and behavioral test surface;
- relevant dependencies and physical-structure constraints;
- a before-and-after diagram;
- `Strong`, `Worth exploring`, or `Speculative` confidence;
- a conflicting ADR or specification only when the evidence justifies reopening
  it.

End with one top recommendation. Do not turn the report into a refactoring plan
or propose exact Interfaces.

Continue when the report lets the user compare every supported candidate and
choose one without reading the code first.

## 4. Hand off the decision

When the user has delegated candidate selection and implementation within an
authorized outcome, choose the best supported candidate and proceed. Otherwise
present the recommendation and ask for selection or execution authority only
where it is missing.

Reuse accepted constraints, dependency ownership, Seam placement, and surviving
tests. Investigate remaining facts and resolve choices under the decision
policy. A full interview is available when the user explicitly requests it.

For authorized follow-up:

- use `$domain-modeling` to route accepted durable knowledge when its artifacts
  are present or the conclusion warrants one;
- use the Design It Twice branch of `$codebase-architecture` when a consequential
  Interface needs materially different alternatives;
- implement only when the user has authorized implementation.

Finish when the candidate is rejected with a recorded rationale where warranted,
or its accepted conclusions have been routed to their proper owners and any
authorized follow-up is clear.
