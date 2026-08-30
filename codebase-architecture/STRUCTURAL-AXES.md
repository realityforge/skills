# Structural Axes

Use this reference when logical architecture may be confused with source,
build, packaging, deployment, or runtime structure.

## Glossary

**Artifact**: A build or packaging output treated as one identified object for
storage, distribution, loading, or execution. An Artifact may contain several
Modules, and a Module's Implementation may span Artifacts.

**Deployment**: The exact set of Artifacts, configuration, and data managed as
one operational release or activation. A project may specialize this around
installation, promotion, admission, rollout, or rollback.

## Classification

Classify each relevant structure before reasoning across it:

- **Logical architecture**: Modules, Interfaces, responsibilities, and Seams.
- **Source structure**: files, directories, packages, crates, and repositories.
- **Build structure**: targets, dependency graph nodes, generated outputs, and
  compilation units.
- **Packaging structure**: Artifacts distributed, loaded, or executed as a
  whole.
- **Deployment structure**: Artifacts, configuration, and data released,
  admitted, activated, or rolled back together.
- **Runtime structure**: processes, sandboxes, address spaces, threads, and
  live instances.

Classify provenance, trust, containment, packaging, loading, visibility,
execution location, and versioning independently when they bear on the design.

These structures may align, but alignment is a design choice rather than a
default. Complete the classification only when every relevant claim belongs to
an explicit axis and no recommendation relies on an unstated equivalence.
