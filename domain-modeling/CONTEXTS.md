# Documentation Contexts

A context is one canonical artifact root and its permitted outward references. Use contexts when a repository has
multiple domain-documentation roots or includes an independently owned project.

## Configuration

Place `.domain-modeling.toml` at the repository root:

```toml
version = 1

[[contexts]]
name = "repository"
root = "docs"
imports = ["codec"]

[[contexts]]
name = "codec"
root = "codec/docs"
imports = ["repository"]
```

Each context requires a unique `name` and a repository-relative `root`. `imports` is optional and names the contexts
that this context may reference. Imports are outward, direct, and non-transitive; explicit cycles are valid.

Roots must exist, remain inside the repository, and neither overlap nor contain one another. Each root may contain
`adr/`, `deferred/`, `specs/`, and `glossary/`; create those directories lazily. The validator treats Markdown below
those directories as artifact sources. Other files are link targets, not additional artifact sources.

Without this file, the repository is one legacy context: artifacts live below `docs/` and may link anywhere inside the
repository.

## Ownership

Configuration records locations and permitted links, not semantic ownership. Follow repository ownership rules first.
When none exist, put specialized knowledge in the context that owns the subject and reserve a repository context for
knowledge that genuinely spans contexts. Ask the user when the choice remains consequentially ambiguous.

Each conclusion has one canonical owner. Artifact identities are context-local: ADR numbers, specification and deferred
issue filenames, and glossary terms may repeat in independent contexts. Within one context, ADR numbers and glossary
terms are unique; specification and deferred issue filenames are case-insensitively unique.

An imported glossary remains a separate vocabulary. Link deliberately to an imported canonical term when using that
context's concept; an import does not make matching words part of the importing context's glossary.

## Links and changes

Use relative Markdown paths. A local target must resolve inside the source context or one of its direct imports;
absolute paths and symlink escapes are invalid.

When a root or import changes, update `.domain-modeling.toml` and every affected inbound link in the same change. Run
`scripts/validate_doc_links.py` once against the repository root to validate every configured context. The validator
requires Python 3.11 or newer and rejects unknown configuration versions.
