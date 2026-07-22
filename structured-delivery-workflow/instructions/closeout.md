# Closeout

Use this instruction before the final response.

## All Work

- Run the strongest practical validation for the changed scope.
- Inspect the diff or changed files.
- Verify structured planning files parse before cleanup when applicable.
- Run the requirements-first implementation review when active plan artifacts
  exist.
- Run the knowledge-promotion sweep and prepare its closeout record before
  removing active plan artifacts.
- Create the separate plan-artifact cleanup commit when required.
- Deliver the prepared closeout record in the pull request, issue, repository
  report, or final response selected during knowledge promotion.
- Report validation commands and outcomes.
- Report uncommitted work or skipped verification, if any.

## Persistent Plan Tree

Also verify:

- no in-scope task remains pending unexpectedly
- completed tasks do not have stale `commit.hash: pending`
- review/approval state matches what actually happened
- durable knowledge has been promoted or classified as temporary plan state
- the active plan tree was removed in a separate cleanup commit, or the blocker
  is reported explicitly

## Output Style

- Keep chat updates short and evidence-based.
- Prefer links to planning files over pasted artifacts.
- Do not repeat template text in chat unless asked.
- Do not load templates until the selected mode needs them.
- Summarize decisions and validation results; avoid narrating every
  bookkeeping step.
