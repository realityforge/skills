# Specification Format

Specifications live at `docs/specs/<kebab-case-subject>.md`. Create `docs/specs/` lazily. Each file owns one coherent
contract; split requirements that can change independently.

A specification records current, durable, verifiable requirements that survive implementation changes and the deletion
of delivery plans.

## Qualification

A requirement belongs in a specification when all of these hold:

1. The requirement is accepted now, not proposed or deferred.
2. It expresses behavior, a constraint, or an invariant that future implementations must preserve.
3. It can be stated independently of the current code structure.
4. Without a specification, it would have no durable owner beyond implementation artifacts or temporary delivery
   state.

## Minimal format

```md
# <Subject> Specification

## Purpose

<One short paragraph defining scope and linking relevant glossary topics when they exist.>

## Requirements

1. <Durable requirement stated directly.>
2. <Another independently verifiable requirement.>

## Architectural basis

<Optional compact links to ADRs that constrain the requirements.>
```

Omit `Architectural basis` when no ADR materially constrains the specification. Add another section only when it makes
the requirements substantially easier to navigate.

## Rules

- Record what must remain true; decision rationale and realisation details stay in their owning artifacts.
- Use established glossary terms.
- State one independently verifiable obligation per requirement. Use invariants for cross-scenario behavior and
  scenarios for verifiable edge cases.
- Keep requirements implementation-independent; include a technical detail only when it is part of the durable
  contract.
- Link ADRs rather than copying their context, alternatives, or rationale. A specification may state a verifiable
  consequence of an ADR.
- Use the smallest set of sections needed to navigate the requirements.

## Capture and update

1. Read the relevant glossary, ADRs, existing specifications, plans, tests, and code needed to establish current intent.
2. Search `docs/specs/` for an existing owner and update it instead of creating overlapping specifications.
3. Extract durable requirements from a temporary plan before that plan is deleted; leave sequencing, evidence, and
   implementation detail behind.
4. Check every requirement against current behavior. When behavior differs from the accepted contract, record the
   requirement in the specification and surface the mismatch as a bug or implementation work.
5. When a plan expands or implements a requirement, link the specification at that point. The specification owns what
   must remain true; the plan owns how and when.

Capture or update is complete when every in-scope requirement has one specification owner and an independently
verifiable statement of the accepted contract, implementation detail and decision rationale remain in their owning
artifacts, and every implementation mismatch and relevant plan link is surfaced.

Specifications describe the currently accepted contract; repository history owns chronology. When the contract
changes, update or remove obsolete requirements. When replacing, renaming, or deleting a specification, update every
inbound reference.
