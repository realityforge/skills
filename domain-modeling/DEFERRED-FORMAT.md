# Deferred Issues

A deferred issue preserves a consequential unresolved question until named evidence, conditions, prerequisites, or development stages make reconsideration timely. Current work can proceed without answering it.

## Qualification

Create a deferred issue only when all of these hold:

1. The question could affect a future product, domain, design, architecture, or implementation decision.
2. Answering it now would be premature because evidence, prerequisites, scope, or requirements are missing.
3. The current work is not blocked by leaving it open.
4. At least one observable condition should cause reconsideration.
5. Preserving the context will prevent meaningful rediscovery or accidental foreclosure later.

Route other matters to their canonical artifact:

| Matter | Artifact |
| --- | --- |
| Shared term | `docs/glossary/` |
| Adopted architectural choice | ADR when it meets the ADR threshold |
| Understood work awaiting execution | Plan or task |
| Defect | Bug |
| Question blocking current work | Current design or plan |
| Consequential question intentionally postponed | Deferred issue |

The user owns deferral. Record an explicit user deferral immediately; when the agent identifies a candidate, propose it and wait for agreement. A deferred issue preserves a question—it does not remove required work or silently change current scope.

## Placement and naming

Use:

```text
docs/deferred/neutral-subject.md
```

Create the directory lazily. Use a short kebab-case subject that remains neutral about the answer:

```text
plugin-process-isolation.md
event-schema-compatibility.md
```

Each file owns one independently reconsiderable question. Split questions that can reach different decisions or triggers; keep subquestions together when they must be reconsidered as one decision.

## Format

```md
# <Unresolved question stated neutrally>

<Optional one-paragraph framing when the title alone is insufficient.>

## Why it matters

<Consequences that make the question worth preserving.>

## Why deferred

<Missing evidence, prerequisite, scope boundary, or other reason.>

## Reconsider when

- <Observable trigger>

## Context

<Optional context already learned: evidence, constraints, alternatives, affected areas, terminology, or related artifacts.>
```

`Context` is optional; omit the heading when it adds no value. Use the project's existing domain and design terminology and link related ADRs when they materially locate or constrain the question.

State triggers as observable events, prerequisites, thresholds, changed assumptions, or named development stages. Examples include “before stabilizing the public API,” “when a second backend is introduced,” and “after the scheduler ownership decision is recorded.”

Record only context already learned. Preserve visible options or possible impacts when useful without performing the deferred analysis.

A deferred issue may identify options that delay could close. Any present work or constraint intended to preserve those options belongs in an explicit current decision or plan.

## Capture and update

1. Check the relevant glossary, design language, ADRs, plans, and code needed to confirm that the question remains unresolved and does not contradict an adopted decision.
2. Search the applicable `docs/deferred/` directory for the same question.
3. Update an existing issue with genuinely new context instead of duplicating it. Preserve its question; split a new issue when the concern can be reconsidered independently.
4. Create the file only after the user has explicitly deferred the question or accepted the agent's proposal.
5. Link from the originating plan or design document only when the link explains a scope boundary, omitted decision, or future dependency.
6. Continue the current work.

Capture is complete when the record is unique, neutral, non-blocking, uses established terminology, states a specific reason for deferral, contains an observable trigger, and imposes no unapproved constraint on current work.

## Reconsider and resolve

Before making a consequential decision, search deferred issues for the same subject. Surface a relevant issue when a recorded trigger has occurred; reconsideration and resolution remain the user's decisions.

- If the question remains premature, update `Why deferred` and `Reconsider when` with the new evidence and next trigger.
- If new evidence arises before a trigger, update the existing record only when that evidence changes useful context, the deferral reason, or the trigger.
- If the question is resolved, transfer every durable conclusion and rationale to the appropriate canonical artifact, replace or remove backlinks, then delete the deferred issue.

File existence means the issue is active. Deferred issues have no status field, lifecycle, or resolved archive; repository history provides recovery when needed.
