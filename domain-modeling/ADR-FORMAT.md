# ADR Format

ADRs live in `docs/adr/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create the `docs/adr/` directory lazily — only when the first ADR is needed.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

Keep the ADR to the shortest text that records the decision and its rationale.

## Lifecycle

Create an ADR when the decision is adopted. Files in `docs/adr/` are the currently adopted architectural decisions;
repository history owns chronology.

When a later decision replaces an ADR, record the replacement and its rationale, update every reference to describe the
current decision, then delete the obsolete ADR. Replacement is complete when the current rationale remains discoverable,
every inbound reference names the current decision, and the obsolete ADR is removed.

## Separate decisions, not implementation plans

Keep the ADR at the architectural level: ownership, boundaries, constraints, trust relationships, selected patterns,
and rationale. Put durable requirements in linked specifications and realisation details in linked plans unless a
detail is itself the hard-to-reverse architectural decision.

Library and technology selections may have their own ADRs when they meet the ADR criteria. Keep these separate from the
structural architecture ADR they implement. A selection ADR may record the concrete technology, evaluated version or
major line, required dependencies, and material runtime or operational consequences; mutable setup and rollout details
remain in the linked plan.

Split independently changeable decisions when they have different alternatives or reasons. A `Consequences` section
identifies only unavoidable implementation obligations; plans own their realisation.

When a plan expands an ADR, link the ADR at that point and retain the implementation detail locally. The ADR owns the
decision and why; the plan owns how, sequencing, evidence, and verification.

## Optional sections

- **Considered Options** — only when the rejected alternatives are worth remembering
- **Consequences** — only when non-obvious downstream effects need to be called out

## Numbering

Scan `docs/adr/` for the highest existing number and increment by one.

## When to offer an ADR

All three of these must be true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will look at the code and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If a decision is easy to reverse, skip it — you'll just reverse it. If it's not surprising, nobody will wonder why. If there was no real alternative, there's nothing to record beyond "we did the obvious thing."

### What qualifies

- **Architectural shape.** "We're using a monorepo." "The write model is event-sourced, the read model is projected into Postgres."
- **Integration patterns between subsystems or domain boundaries.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library — just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer Management owns Customer data; other subsystems reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Architectural choices forced by external constraints.** Link the constraint's canonical owner; record the
  hard-to-reverse architectural choice and its rationale in the ADR.
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it — otherwise someone will suggest GraphQL again in six months.

## Capture

1. Read the relevant glossary, specifications, ADRs, design documents, plans, and code needed to establish the current
   choice and rationale.
2. Search `docs/adr/` for an existing owner or a decision this choice replaces.
3. Apply all three qualification criteria and separate independently changeable decisions.
4. Use the next sequential number when creating an ADR.
5. Link every plan that expands the decision.

Capture is complete when the decision satisfies all three qualification criteria, has one current ADR, records the
choice and rationale, keeps delivery detail in its owning plan, and every plan that expands it links it. A new ADR uses
the next sequential number.
