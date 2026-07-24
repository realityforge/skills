# Knowledge Promotion

Use this instruction after the requirements-first implementation review and
before removing persistent planning artifacts.

Requirements, implementation design, task state, and validation evidence are
working delivery state. Promote only the parts that remain useful after the
delivery is complete, then allow the working plan to be removed.

## Promote As Knowledge Resolves

Promote durable knowledge when it becomes settled during design or
implementation. Use the closeout sweep to catch remaining candidates, not to
reconstruct rationale that was already available earlier.

When language, an accepted durable requirement, an adopted decision, or a
deliberately deferred question may be durable, use `domain-modeling` and follow
its relevant glossary, specification, ADR, or deferred-issue rules.

## Closeout Sweep

Review the accepted requirements, final implementation design, material plan
deviations, implementation discoveries, and unresolved questions. Classify
each potentially durable item:

| Knowledge | Canonical destination |
| --- | --- |
| Resolved domain language | Project glossary through `domain-modeling` |
| Qualifying accepted durable requirement | Specification through `domain-modeling` |
| Qualifying adopted architecture or technology decision | ADR through `domain-modeling` |
| Consequential question deliberately postponed by the user | Deferred issue through `domain-modeling` |
| Current architectural structure needed to understand the system | Existing architecture or design documentation |
| Task sequencing, file lists, intermediate status, and command bookkeeping | Temporary plan state; no promotion |

Use the repository's existing canonical locations and conventions. Update one
authoritative home for each conclusion and link to it elsewhere. Treat code,
tests, or existing documentation as sufficient only when `domain-modeling`
qualification does not require a specification.

Validate every canonical artifact changed during promotion. Preserve a
deferred question only after the user has explicitly deferred it or accepted
the proposed deferral.

## Closeout Record

Prepare a concise historical record in the delivery's existing channel: pull
request, issue, or final response. Create a repository report only when project
convention, audit needs, or the absence of another durable delivery record
justifies one.

The closeout record should contain:

- accepted outcome and delivered result
- material deviations from the implementation design and why
- links to promoted canonical artifacts
- validation performed and its outcome
- residual risk, skipped validation, and unresolved or deferred questions
- plan-cleanup status

Link canonical artifacts rather than restating their contents. The closeout
record owns delivery history; canonical artifacts own current project truth.

## Completion Gate

Knowledge promotion is complete when:

- every potentially durable requirement, decision, term, discovery, and
  unresolved question has been classified
- qualifying knowledge has one updated and validated canonical home
- deferred issues have user agreement and an observable reconsideration trigger
- the closeout record is prepared with links to promoted artifacts
- everything remaining only in the plan tree is temporary delivery state
