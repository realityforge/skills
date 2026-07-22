# Detailed Task Review Rubric

Judge whether the task breakdown completely and safely executes the reviewed
implementation design.

Check:

- every design obligation belongs to a task
- dependencies and execution order are coherent
- tasks use independently verifiable implementation boundaries
- acceptance criteria and validation expectations prove each task's obligation
- touched files or patterns are sufficient to locate the work
- cross-cutting tests, documentation, migration, rollout, and cleanup work are
  owned rather than left in plan prose

Treat the reviewed design as the baseline. Report an upstream finding only
when task decomposition exposes a real requirements or design contradiction.
