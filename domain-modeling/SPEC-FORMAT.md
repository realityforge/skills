# Specification Format

Specifications live in `docs/specs/`. Create the directory lazily when the first specification is needed.

A specification records current, durable, verifiable requirements that should survive implementation changes and the
deletion of delivery plans.

## Qualification and routing

Create or update a specification when all of these hold:

1. The requirement is accepted now, not proposed or deferred.
2. It expresses behavior, a constraint, or an invariant that future implementations must preserve.
3. It can be stated independently of the current code structure.
4. Recovering it from code later could confuse deliberate behavior with an implementation accident.

Route other information to its canonical artifact:

| Matter | Artifact |
| --- | --- |
| Meaning of a domain term | `docs/glossary/` |
| Architectural or technology choice and why | ADR |
| Durable required behavior or constraint | Specification |
| Implementation and mutable configuration | Code |
| Consequential unresolved question | Deferred issue |
| Delivery sequence, temporary evidence, or migration detail | Plan |
| Incorrect current behavior | Bug |

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

- Record what must remain true, not why a choice was made or how it is implemented.
- Use established glossary terms without redefining them.
- State one observable or verifiable obligation per requirement. Prefer invariants over scenarios and exhaustive wire
  descriptions.
- Exclude provider brands, libraries, classes, routes, configuration keys, version pins, timeout values, storage
  choices, and rollout details unless the detail is itself a durable external contract.
- Link ADRs rather than copying their context, alternatives, or rationale. A specification may state a verifiable
  consequence of an ADR.
- Keep proposed requirements in their owning design, plan, or backlog. Create a deferred issue only when an unresolved
  question meets the qualification rules in [DEFERRED-FORMAT.md](./DEFERRED-FORMAT.md).
- Keep the document as short as the subject allows. Do not turn it into a system overview or implementation inventory.

## Capture and update

1. Read the relevant glossary, ADRs, existing specifications, plans, tests, and code needed to establish current intent.
2. Search `docs/specs/` for an existing owner and update it instead of creating overlapping specifications.
3. Extract durable requirements from a temporary plan before that plan is deleted; leave sequencing, evidence, and
   implementation detail behind.
4. Check every requirement against current behavior. When behavior differs from the accepted contract, record the
   requirement in the specification and surface the mismatch as a bug or implementation work.
5. When a plan expands or implements a requirement, link the specification at that point. The specification owns what
   must remain true; the plan owns how and when.

Capture or update is complete when every in-scope requirement has one specification owner, is independently
verifiable, reflects the accepted contract, keeps implementation detail and decision rationale in their owning
artifacts, and surfaces every contradiction and relevant plan link.

Specifications describe the currently accepted contract. Update or remove obsolete requirements when that contract
changes; repository history owns chronology.
