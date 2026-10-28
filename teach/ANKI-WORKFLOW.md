# Anki workflow

Use Anki to retain knowledge the learner already understands. The workspace's `docs/anki.md` owns the collection-specific deck, note type, field, scope, tag, and template rules.

## Route knowledge

Route each conclusion before writing:

| Matter | Owner |
| --- | --- |
| Meaning of a subject term | `docs/glossary/` |
| Evidence of learner understanding | `learning-records/` |
| Durable knowledge worth future retrieval | Anki |
| Teaching preference or temporary course context | `NOTES.md` |

An Anki card is derived retention material. It does not become the canonical definition of a term or the evidence that the learner understands it.

## Workspace contract

If the user opts into Anki and `docs/anki.md` does not exist, establish the collection contract before changing Anki. Record the deck structure, note type and fields, visible template content, scope and tag mappings, source and provenance fields, and collection checks. This step is complete when the workspace document contains every choice needed to create and verify a note without guessing.

## Capture gate

A concept is eligible only when all of these are true:

- It passes the skill's [durable-target selection](SKILL.md#learning-targets).
- The learner has independently explained, applied, or distinguished it through retrieval practice.
- Its terminology agrees with the owning glossary.
- One prompt can test one retrieval target.

Strong candidates include durable mental models, easily confused distinctions, corrected misconceptions, reusable decision rules, and procedures that must be recalled without a reference.

After correction or hints, use a fresh unaided attempt before promotion. Keep an important target that is not yet understood in the teaching work, with the outstanding gap in an existing learning record or `NOTES.md`. Eligibility for Anki establishes readiness for spaced practice, not proof of long-term retention.

Before adding a note, compare its meaning with existing retrieval targets. Prefer improving an existing prompt when it tests the same knowledge; different wording alone does not justify another card.

## Compose the card

- Write a prompt that is unambiguous without remembering the lesson.
- Give the shortest answer that fully establishes the target knowledge.
- Put clarification, contrast, and boundary conditions in supporting context rather than adding more retrieval targets.
- Preserve the owning glossary's canonical spelling.
- Cite a primary or official source when one exists.
- Keep lesson provenance in metadata rather than visible question text.
- Use the `humanize` skill on the final prompt, answer, and context.

## Review and evolve targets

During a target audit, inspect usefulness, scope, redundancy, and demonstrated depth. Inspect actual review history when available and state when it is unavailable. Choose an action for each affected target:

| Condition | Action |
| --- | --- |
| Still useful and reliably recalled | Keep active and let the scheduler extend intervals; one correct answer is not a retirement criterion |
| Same target, unclear wording or unnecessary cues | Rewrite in place, preserving note/card identity and scheduling |
| Repeated failure | Diagnose ambiguity, missing prerequisites, or interference; reteach, clarify, or split the target before resuming review |
| A new distinction or application deserves retention | Add a focused target with fresh scheduling; retain the foundation while it remains useful |
| A replacement covers the old target | Check coverage and independent application in a later session before suspending the redundant card |
| Obsolete, outside the mission, or merely lesson-specific | Suspend the card and keep useful reference material with its owner |

Archive through suspension, preserving content and review history. Record affected note/card IDs, the reason, and any replacement in `NOTES.md`; record changes in demonstrated understanding in the owning learning record. Greater detail alone does not establish replacement coverage, and an active card still needs one focused retrieval target.

## Change the collection

1. Read `docs/anki.md` and verify that the integration can inspect the live collection. Completion requires the configured deck, note type, fields, templates, cards, and counts to be observable.
2. Before a bulk rewrite, suspension batch, schema change, or deck reorganization, export a backup that includes scheduling data. Completion requires a readable backup at the reported path.
3. Prefer rewriting or moving an existing note when the retrieval target remains substantially the same. Completion requires its note and card identity to remain stable.
4. Give a materially changed retrieval target fresh scheduling, through a new card or an explicit reset; its predecessor's long interval does not establish readiness for the new target. Completion requires the identity and scheduling decision to be recorded in the result.
5. If the integration is unavailable, leave the collection pending and report the missing capability. Completion requires an explicit pending result rather than a substitute side file.

## Verify

After every collection change, verify against Anki itself:

- Required fields are present and non-empty.
- Every note is in the destination owned by its scope.
- Tags and templates match the workspace contract.
- Prompts are unique within the course collection, stand alone, match their intended scope, and pass durable-target selection. Inspect overlap by meaning as well as duplicate wording; retain multiple prompts for one concept only when they exercise distinct retrieval needs.
- Rewritten or moved notes retained identity where required.
- New or materially changed targets have fresh scheduling; archived cards are suspended and their reasons and replacements are recorded.
- Total and active/suspended collection counts match the intended change.

Report the resulting total and active/suspended counts, backup path for bulk work, identity preservation, scheduling resets, retirement reasons and replacements, and whether synchronization ran. A successful local update does not imply synchronization.
