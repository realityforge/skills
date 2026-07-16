---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model.
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline — challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* `CONTEXT.md` for vocabulary is not this skill — that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

## File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Separate decision kinds and implementation

An ADR records a durable architectural choice: ownership, boundaries, constraints, trust relationships, selected
patterns, and why alternatives were rejected. An implementation or requirements document records how that choice is
realised: classes, interfaces, routes, algorithms, version pins, configuration keys, timeout values, file layout,
rollout sequencing, and similar mechanics.

Library and technology selections can also qualify as ADRs. Record them in their own ADR when they have distinct
alternatives, rationale, or lock-in rather than bundling them into the structural architecture ADR they implement. A
library-selection ADR may include the concrete library, evaluated version or major line, required dependencies, and
material runtime or operational implications. Mutable pins and setup mechanics remain in the linked plan unless the pin
itself is the durable decision.

Do not combine independently changeable decisions in one ADR merely because they belong to the same feature. Split
them when each has its own alternatives and rationale. Conversely, do not promote an implementation detail into an ADR
unless that detail itself meets the ADR criteria and carries architectural or technology lock-in. Consequences may
describe unavoidable downstream effects, but should not become an implementation plan.

### Link plans to ADRs

When creating or updating a plan, requirements document, or technical handoff:

1. Identify and record every qualifying architectural or technology decision as an ADR first.
2. Link the relevant ADR at the point where the plan expands that decision, not only in a detached ADR index.
3. Let the ADR own the decision and its rationale, including material technology-selection details; let the plan own
   realisation detail, evidence, sequencing, and verification.
4. Do not let a plan silently redefine or contradict an ADR. Update or supersede the ADR when the architecture changes.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).
