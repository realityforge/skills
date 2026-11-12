# Audit, Garden, and Mine

Three modes share one audit; they differ only in scope.

| Mode | Scope |
| --- | --- |
| **Audit** | Artifacts changed on the current branch or PR (diff against its merge base), the artifacts that link to them, and the code the branch changes. When a delivery plan is supplied, it is the source of conclusions: check that each durable conclusion has an owner. |
| **Garden** | Every artifact in every context. Work one context at a time, then check cross-context links. |
| **Mine** | A named code target, process, or concept. Extract candidates first, then audit every artifact the extraction touched or should have touched. |

Read every format file before auditing; each check applies its qualification rules. Judge artifacts as a fresh reader:
by what they say to someone who never saw the work that produced them.

## Mine: extract candidates

1. Read the target, its tests, and its callers. List every candidate: domain terms (types, states, roles, events, the
   words its callers and tests use), enforced invariants and observable behavior, architectural choices (boundaries,
   ownership, deliberate deviations), user goals it serves, and open questions it encodes.
2. Route each candidate through [Route knowledge](./SKILL.md#route-knowledge) and apply its owner's qualification.
   Code shows current behavior, not acceptance: treat behavior as accepted when an existing artifact, a test, or the
   user confirms it, and ask the user about the rest.
3. Record qualifying candidates in their existing owners, creating artifacts only when no owner exists. Surface
   disagreements between code and existing artifacts as bugs or artifact corrections.

Extraction is complete when every candidate is recorded, rejected with a reason, or listed as a question for the user.

## Checks

Apply every check to every artifact in scope.

1. **Durable.** Every sentence passes its format's qualification. Route process sediment—status, task tracking,
   history, before/after narration, PR or ticket references, delivery evidence, mutable configuration—to its owner or
   delete it.
2. **Load-bearing language.** Add a glossary term for each qualifying term that durable artifacts or code in scope use
   without a glossary owner. Remove terms that fail qualification and unlink them. Replace `_Avoid_` words in
   artifacts with the canonical term.
3. **Shape.** Each glossary topic is a coherent, navigable subject: move misplaced terms, merge thin topics, split
   crowded ones. Each specification owns one contract: split independently changeable requirements, merge overlapping
   specifications. Each ADR is one adopted decision passing all three criteria: split, merge, rewrite, or delete
   accordingly. Each use case and deferred issue still qualifies.
4. **Linked.** First-use glossary links and canonical spelling hold. Specifications link the ADRs that constrain them,
   use cases link their governing specifications, and plans in scope link the specifications and ADRs they expand.
   Durable artifacts link no temporary plan or task. Each artifact directory holding two or more artifacts has a
   [catalog](./CATALOG-FORMAT.md) whose entries list every artifact once and match it.
5. **True.** Artifacts agree with each other and with the code. Fix the artifact when it is wrong; surface a bug when the
   code is wrong. Surface deferred issues whose trigger has occurred.

Make reversible corrections directly. Ask before removing or rewriting an accepted requirement or decision whose
acceptance is unclear, and before creating a deferred issue.

## Finish

Run [`scripts/validate_doc_links.py`](./scripts/validate_doc_links.py) against the repository root.

The audit is complete when every check has been applied to every artifact in scope, each finding is fixed or reported
with its reason, and the validator passes. Report fixes, open questions, and surfaced bugs.
