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

- The learner has explained, applied, distinguished, or corrected it through retrieval practice.
- It supports the mission beyond the current lesson or demonstration.
- It is likely to remain useful long enough for spaced repetition to help.
- Its terminology agrees with the owning glossary.
- One prompt can test one retrieval target.

Strong candidates include durable mental models, easily confused distinctions, corrected misconceptions, reusable decision rules, and procedures that must be recalled without a reference.

Leave lesson choreography, demo names, arbitrary sample values, material that was merely presented, and transient commands out of the collection. Include tool- or version-specific knowledge only when the mission requires it, and make that scope visible in the prompt or note metadata.

## Compose the card

- Write a prompt that is unambiguous without remembering the lesson.
- Give the shortest answer that fully establishes the target knowledge.
- Put clarification, contrast, and boundary conditions in supporting context rather than adding more retrieval targets.
- Preserve the owning glossary's canonical spelling.
- Cite a primary or official source when one exists.
- Keep lesson provenance in metadata rather than visible question text.
- Use the `humanize` skill on the final prompt, answer, and context.

## Change the collection

1. Read `docs/anki.md` and verify that the integration can inspect the live collection. Completion requires the configured deck, note type, fields, templates, cards, and counts to be observable.
2. Before a bulk rewrite, schema change, or deck reorganization, export a backup that includes scheduling data. Completion requires a readable backup at the reported path.
3. Prefer rewriting or moving an existing note when the retrieval target remains substantially the same. Completion requires its note and card identity to remain stable.
4. Reset scheduling only when the retrieval target materially changes. Completion requires the reset decision to be recorded in the result.
5. If the integration is unavailable, leave the collection pending and report the missing capability. Completion requires an explicit pending result rather than a substitute side file.

## Verify

After every collection change, verify against Anki itself:

- Required fields are present and non-empty.
- Every note is in the destination owned by its scope.
- Tags and templates match the workspace contract.
- Prompts are unique within the course collection.
- Rewritten or moved notes retained identity where required.
- Collection counts match the intended change.

Report the resulting counts, backup path for bulk work, identity preservation, scheduling resets, and whether synchronization ran. A successful local update does not imply synchronization.
