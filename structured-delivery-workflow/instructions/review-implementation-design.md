# Implementation Design Review Rubric

Judge whether the design is the simplest evidence-backed way to satisfy the
reviewed requirements baseline.

Check:

- every requirement has a concrete design response
- the approach is feasible in the actual repository and system
- simpler direct approaches were assessed before adding indirection,
  compatibility paths, or abstractions
- load-bearing assumptions and capability limits have supporting evidence
- interfaces, contracts, data and state changes, migrations, dependencies,
  failure behavior, rollback, rollout, and operations are addressed where
  relevant
- validation will demonstrate the requirements and acceptance criteria
- material alternatives and trade-offs explain the chosen design where needed

Challenge unsupported claims that a direct approach cannot work. Keep task
granularity and bookkeeping out of this review unless they expose a design gap.
