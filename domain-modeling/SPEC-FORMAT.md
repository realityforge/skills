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

## Replacement test

Use the replacement test to apply qualification criteria 2 and 3: imagine deleting every delivery plan and replacing
the current implementation with a different conforming implementation.

A candidate conclusion passes when every conforming replacement must preserve it and compliance remains independently
verifiable without reference to the current code structure. An exact technical detail passes only when its value itself
constrains conformance, such as through interoperability, content identity, persisted compatibility, or observable
behavior.

Apply the replacement test separately from acceptance. An accepted delivery decision is not automatically a
specification requirement.

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

Complete each gate before advancing to the next.

### Gate 1: Establish the current contract

1. Read the relevant glossary, ADRs, existing specifications, plans, tests, and code needed to establish current intent
   and behavior.
2. Search `docs/specs/` for an existing owner and update it instead of creating an overlapping specification.
3. When updating an existing specification, inspect its relevant history for material deliberately removed, relocated,
   or superseded.

This gate is complete when the current specification owner is identified, the accepted intent and behavior are
established, and relevant prior removals, relocations, and replacements are accounted for.

### Gate 2: Classify every candidate conclusion

1. Enumerate every conclusion introduced, accepted, changed, or preserved by the work.
2. Route each candidate to exactly one owner before drafting.
3. Apply all four qualification criteria and the replacement test separately to every candidate routed to a
   specification.

This gate is complete when every candidate is classified exactly once and every specification candidate passes every
qualification criterion and the replacement test.

### Gate 3: Draft and verify the contract

1. Draft the invariant each conforming implementation must preserve.
2. State one independently verifiable obligation per requirement.
3. Check every requirement against current behavior. When behavior differs from the accepted contract, record the
   requirement and surface the mismatch as a bug or implementation work.
4. When a plan expands or implements a requirement, link the specification at that point.

This gate is complete when every qualifying candidate has one independently verifiable statement in its specification,
every implementation mismatch is surfaced, and every relevant plan link is present.

### Gate 4: Audit the specification-only diff

1. Apply the replacement test to every changed sentence, including the Purpose and every requirement.
2. Check the changed prose against the specification's Purpose, existing requirements, and relevant history.
3. Review every exact technical detail, numeric bound, tool or file reference, delivery-scope statement, and future
   possibility. Keep it only when it passes the replacement test; otherwise route it to its owner.

Capture or update is complete when every changed sentence passes the replacement test, every exact technical detail has
an identified durable contract consequence, the specification remains internally coherent, delivery sequencing,
temporary evidence, implementation detail, decision rationale, and future possibilities remain in their owning
artifacts, and every implementation mismatch and relevant plan link is surfaced.

Specifications describe the currently accepted contract; repository history owns chronology. When the contract
changes, update or remove obsolete requirements. When replacing, renaming, or deleting a specification, update every
inbound reference.
