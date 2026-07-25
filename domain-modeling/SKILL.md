---
name: domain-modeling
description: Model a project's domain. Use when resolving domain language, recording accepted durable requirements in specifications, recording architectural decisions, deliberately deferring or reconsidering consequential questions, or when another skill needs these artifacts.
---

# Domain Modeling

Ground changes in existing domain artifacts, relevant design documents, and code.

## Link language

Link the first body use of every glossary-owned term in each specification, ADR, and deferred issue to its canonical
heading, using the canonical spelling as link text; apply the same rule to references between glossary definitions. Use
unlinked canonical spelling thereafter. For example:
`[Interactive Authentication](../glossary/authentication.md#interactive-authentication)`.

Language use is complete when every glossary-owned term in every affected artifact uses canonical spelling and each
required first-use link resolves to its owning heading.

After changing a specification, ADR, deferred issue, or glossary file, run
[`scripts/validate_doc_links.py`](./scripts/validate_doc_links.py) against the repository root. It validates every local
file and heading-fragment target in those artifact directories.

## Route knowledge

Route each conclusion to one owner before writing:

| Matter | Owner |
| --- | --- |
| Meaning of a domain term | `docs/glossary/` |
| Accepted durable behavior, constraint, or invariant | Specification when it meets specification qualification |
| Adopted architectural or technology choice and why | ADR when it meets the ADR threshold |
| Consequential unresolved question intentionally postponed | Deferred issue when it meets deferred qualification and the user agrees |
| Proposed requirement or unresolved current design | Owning design, plan, or backlog |
| Implementation and mutable configuration | Code |
| Delivery sequence, temporary evidence, or migration detail | Plan or task |
| Incorrect current behavior | Bug |

## Sharpen language

Before resolving, adding, or changing domain language, read
[GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md). Apply every structure, rule, and update requirement.

## Record decisions

Before offering, creating, updating, replacing, or deleting an ADR—and whenever a plan expands an architectural or
technology choice—read [ADR-FORMAT.md](./ADR-FORMAT.md). Apply every qualification, capture, lifecycle, separation, and
plan-linking rule.

## Record specifications

Before offering, creating, updating, replacing, or deleting a specification—and whenever work accepts or changes a
durable requirement—read [SPEC-FORMAT.md](./SPEC-FORMAT.md) and run its gates in order. Drafting begins only after the
candidate-classification gate is complete, and specification work ends only after the specification-only diff audit is
complete.

## Defer questions

Before creating, updating, reconsidering, or deleting a deferred issue—and whenever a consequential question is
deliberately deferred or a recorded trigger may have occurred—read
[DEFERRED-FORMAT.md](./DEFERRED-FORMAT.md). Apply every qualification, authority, capture, and lifecycle rule.
