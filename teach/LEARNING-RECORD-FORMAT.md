# Learning Record Format

Learning records live in `./learning-records/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc. Create the directory lazily — only when the first record is written.

They are the teaching equivalent of ADRs: they capture non-obvious lessons, key insights, and stated prior knowledge that will steer future sessions. They are used to calculate the zone of proximal development.

## Template

```md
# {Short title of what was learned or established}

{1-3 sentences: what was learned (or what prior knowledge was claimed), the evidence and assistance involved, and why it matters for future sessions.}
```

That is the whole format. A learning record can be a single paragraph. The value is recording _that_ this is now known and _why_ it changes what to teach next — not in filling out sections.

## Optional sections

Only include these when they add genuine value. Most records won't need them.

- **Status** frontmatter (`active | superseded by LR-NNNN`) — useful when an earlier understanding turns out to be wrong and is replaced.
- **Evidence** — expand the summary's evidence when its conditions or limitations will steer future teaching. Use the distinctions below.
- **Implications** — what this unlocks or rules out for future sessions. Worth recording when non-obvious.

## Evidence

Record the target, what the learner actually did, and the support available. Distinguish:

- **Independent retrieval:** an explanation or performance before choices, hints, or supplied answers.
- **Recognition or assisted correction:** a response selected from alternatives or produced after guidance.
- **Transfer:** application to a different example or context; state whether it was independent or assisted.
- **Delayed retrieval:** successful recall in a later session; identify the earlier evidence so the delay is clear.

An immediate restatement of a supplied correction is assisted progress. Record any remaining uncertainty and use a fresh unaided attempt to establish independent understanding. A quiz's final score after retries does not establish first-attempt accuracy or long-term retention. Keep claimed prior knowledge distinguishable from observed performance.

Update the owning record when later evidence changes what to teach next. Routine reviews belong to the review system, not new learning records.

## Numbering

Scan `./learning-records/` for the highest existing number and increment by one.

## When to write a learning record

Write one when any of these is true:

1. **The user demonstrated genuine understanding of something non-trivial** — not just exposure, but evidence they can use the concept correctly. This sets a new floor for what to teach next.
2. **The user disclosed prior knowledge** — "I already know X." Record it so future sessions don't re-teach it. Also record the _depth_ claimed.
3. **A misconception was corrected** — the user previously believed something wrong and now sees why. These are high-value: they predict future stumbling blocks for related topics.
4. **The mission shifted in response to learning** — the user discovered they cared about something different than they thought. Cross-link to [[MISSION.md]] and update it.

### What does _not_ qualify

- Material that was merely covered. Coverage is not learning. Wait for evidence.
- A term definition already owned by `docs/glossary/`. Record only the demonstrated understanding and why it changes future teaching.
- Session-by-session activity logs. Learning records are not a journal — they are decision-grade insights.

## Supersession

When a later record corrects or replaces an earlier understanding, mark the old record `Status: superseded by LR-NNNN` rather than deleting it. Deeper understanding can extend a still-valid foundation; keep both records active when both remain useful. Card retirement follows the Anki workflow and does not by itself invalidate a learning record.
