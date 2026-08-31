# Deepening

Use this process when several shallow Modules may become one deep Module. Apply
the vocabulary and discipline in [SKILL.md](SKILL.md) throughout.

## 1. Establish the cluster

Trace representative behavior through callers, Modules, tests, and failures.
Name the knowledge or sequencing that leaks across current Interfaces. Apply
the deletion test to each suspected pass-through.

Continue when the candidate cluster and its architectural friction are
evidenced in current code rather than inferred from file shape or naming.

## 2. Classify dependencies

- **In-process**: pure computation or memory owned within the cluster. Keep it
  inside the new Implementation.
- **Local-substitutable**: a real local stand-in can exercise production
  behavior. Keep the Seam internal unless callers select it.
- **Remote and owned**: define the narrow Interface owned by the deep Module;
  production and in-memory Adapters exercise the same contract.
- **External**: isolate the third-party contract behind the narrowest owned
  Interface and use a faithful test Adapter.

When the dependency crosses Artifacts, deployments, processes, or sandboxes,
also apply [STRUCTURAL-AXES.md](STRUCTURAL-AXES.md).

Continue when every dependency has explicit ownership, lifecycle, execution
location, and Adapter treatment.

## 3. Shape the deep Module

Design the external Interface around caller outcomes. Move policy, sequencing,
failure handling, and dependency coordination behind it. Keep test-only and
algorithmic Seams private.

Continue when deleting the proposed Module would redistribute real complexity
across callers and its Interface provides more Leverage than the cluster it
replaces.

## 4. Replace the test surface

Verify equivalent behavior through the new external Interface, then delete
tests whose only purpose was to preserve obsolete shallow Interfaces. Retain
focused internal tests only for behavior that remains hazardous and private.

Deepening is complete when callers and behavioral tests use the new Interface,
obsolete Interfaces and compatibility layers are gone unless explicitly
required, and the resulting Locality is visible in the diff.
