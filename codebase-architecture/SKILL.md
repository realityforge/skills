---
name: codebase-architecture
description: Architecture vocabulary for deep Modules. Use for architecture design or review, physical-structure classification, deepening shallow Modules, alternative-Interface exploration, or when another skill needs the shared language.
---

# Codebase Architecture

Read the repository instructions and project design language first. Project
terms specialize this shared language and remain valid when they name different
concepts. Continue when every local term and durable decision bearing on the
design has been accounted for.

## Glossary

**Module**: Anything with an Interface and an Implementation. Scale-agnostic: a
function, class, package, process, or larger slice may be a Module.

**Interface**: Everything a caller must know to use a Module correctly,
including types, invariants, ordering, errors, effects, configuration, and
performance. It is the complete caller contract, not merely an API or
signature.

**Implementation**: Everything hidden behind a Module's Interface. Use Adapter
when discussing the role an Implementation fills at a Seam.

**Depth**: The Leverage a Module provides through its Interface. A deep Module
hides substantial behavior behind a small Interface; a shallow Module exposes
nearly as much complexity as it implements.

**Seam**: A place where behavior can change without editing at that place; the
location where a Module's Interface lives. A boundary may instead name a trust,
protocol, transaction, failure, or scope limit.

**Adapter**: An Implementation that satisfies an Interface at a Seam. Adapter
names the role filled, not its technology, size, or internal structure.

**Internal Module**: A Module whose Interface is private to its containing
Implementation. Internal describes Interface visibility, not physical
placement.

**Leverage**: The capability callers gain for the amount of Interface they must
learn.

**Locality**: The concentration of change, knowledge, bugs, and verification
inside one Module rather than across its callers.

## Design discipline

- Prefer deep Modules with small Interfaces and substantial hidden behavior.
- Judge Depth by caller Leverage, not lines of Interface and Implementation.
- Apply the deletion test: removing a valuable Module makes its hidden
  complexity reappear across callers; removing a pass-through removes only
  indirection.
- A Module presents one conceptual external Interface, which may use several
  language-level types, protocols, or caller views.
- Place a Seam only where behavior varies. Two independently useful Adapters
  are strong evidence; a test Adapter counts only when it exercises the same
  undistorted Interface.
- Make dependency ownership explicit. Accept a dependency when the caller owns
  its selection or lifecycle; construct it internally when the Module owns it.
- Make effects and failure modes part of the Interface. Behavioral tests use
  that Interface; focused internal tests may cover hazardous algorithms without
  becoming caller contracts.

Finish only when the Module's responsibility and complete Interface are clear,
its hidden complexity earns Leverage and Locality, every Seam has demonstrated
variation, and representative callers, tests, dependencies, and repository
decisions support the design.

## Further analysis

- **Physical structure**: when source, build, packaging, deployment, loading,
  process, or versioning structure matters, read
  [STRUCTURAL-AXES.md](STRUCTURAL-AXES.md).
- **Deepening**: when a cluster of shallow Modules may become one deep Module,
  read [DEEPENING.md](DEEPENING.md).
- **Alternative Interfaces**: when a consequential Interface warrants
  materially different designs, read [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md).
