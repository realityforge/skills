# Planning

Use this instruction when creating or revising persistent planning artifacts.

## Procedure

1. Read local instructions and active planning conventions.
2. Check worktree state before editing.
3. Gather only enough code and repository context to make the plan concrete.
4. Resolve evidence-answerable questions yourself.
5. Ask one user question at a time only for true blockers.
6. Write or update the selected planning state.
7. Validate planning artifacts when they are structured files.
8. Run the built-in iterative plan review loop after the plan is drafted and
   local context has been gathered, but before asking the user to review it.
9. Apply valid or partially valid review findings to the plan, reject invalid
   findings with evidence, and revalidate edited artifacts.
10. If the user requested review, pause after the review loop and ask for review
    before implementation.

## Open Questions

Track open questions only when real uncertainty remains after repository
inspection.

For persistent plan trees, use stable `Q-*` IDs and record:

- status (`open` or `resolved`)
- question
- context
- options and tradeoffs
- recommended default
- user decision when resolved
- artifacts updated

Do not finalize a reviewable plan while a blocking question is still open.
Non-blocking assumptions may remain if they are labeled and have a recommended
default.

## Plan Changes

When scope, sequencing, risk, or validation expectations change:

- update the active planning state in the same iteration if one exists
- keep the old decision visible only when it matters for audit or future review
- avoid long decision logs for routine implementation discoveries
