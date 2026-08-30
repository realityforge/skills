# Design It Twice

Use this process when an Interface choice is consequential enough to justify
materially different designs. Apply the vocabulary and discipline in
[SKILL.md](SKILL.md) throughout.

## 1. Frame the decision

Record the callers, required outcomes, invariants, ordering, errors, effects,
dependencies, and repository decisions every design must satisfy. Use
[STRUCTURAL-AXES.md](STRUCTURAL-AXES.md) when physical structure constrains the
choice.

Continue when every alternative can be judged against the same evidence and
constraints.

## 2. Produce alternatives

Develop at least three materially different Interface shapes. Useful pressures
include minimum surface area, maximum extensibility, and the simplest common
caller. Parallel agents are optional; different names over the same call shape
do not count as different designs.

For each alternative provide:

- the complete Interface, including behavioral contract;
- one representative caller;
- the complexity hidden by the Implementation;
- dependency ownership, Seams, and Adapters;
- the main gain and cost in Depth, Leverage, and Locality.

Continue when the alternatives make genuinely different responsibility or Seam
placement choices.

## 3. Compare and recommend

Compare the alternatives against the shared constraints, then recommend one or
a specific hybrid. Prefer the design with the strongest caller Leverage and
maintainer Locality that does not buy speculative flexibility.

Finish when the recommendation explains why its Interface and Seam placement
are stronger than each rejected alternative.
