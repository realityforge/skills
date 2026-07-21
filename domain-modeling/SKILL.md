---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when resolving domain language, recording an architectural decision, deliberately deferring or reconsidering a consequential question, or when another skill needs to maintain these artifacts.
---

# Domain Modeling

Actively sharpen the project's language, decisions, and deferred questions as they emerge during design and implementation. Ground changes in the existing model, relevant design documents, ADRs, and code.

## Locate domain language

- Use `docs/glossary/` as the sole home for domain language. When it exists, read `README.md` and the relevant topic files before changing terminology.
- Use the project's documented domain and design terminology. Surface conflicts between those sources, the user's statements, and the code before writing.

## Sharpen language

When resolving or adding a term, read [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md) before editing.

- Challenge terminology that conflicts with the glossary.
- Replace vague or overloaded language with a proposed canonical term.
- Probe relationships with concrete edge-case scenarios.
- Check stated behavior against the code and surface contradictions.
- Update the owning glossary topic as soon as a term is resolved.

## Record decisions

When a choice could be a durable architectural or technology decision, read [ADR-FORMAT.md](./ADR-FORMAT.md) before offering or writing an ADR and before a plan expands the choice. Apply all qualification, separation, and plan-linking rules in that reference.

## Defer questions

When a consequential question is deliberately deferred, or current work may satisfy a recorded reconsideration trigger, read [DEFERRED-FORMAT.md](./DEFERRED-FORMAT.md) before creating, updating, reconsidering, or deleting a deferred issue.
