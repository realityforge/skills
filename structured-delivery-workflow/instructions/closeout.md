# Closeout

Close only after implementation review reports `Findings: none`.

## Final knowledge sweep

When any `docs/adr/`, `docs/glossary/`, `docs/specs/`, or `docs/deferred/`
directory exists, use `$domain-modeling` once more. Classify reviewer-driven
changes and any qualifying durable conclusion missed before review. Validate
every changed canonical artifact. A failed required promotion or validation
leaves the plan tree intact and blocks closeout.

## Cleanup gate

Before deletion, verify from repository and plan evidence that:

- every task is complete
- task-local and full-scope validation passed
- implementation review passed and its round count is recorded
- qualifying durable knowledge is promoted and validated when domain
  directories exist
- the committed plan and implementation updates exist in git history

Resolve the exact active plan path again. Inspect its contents, including
arbitrary temporary files, then delete that tree and no other plan tree.

Commit the deletion as the final closeout commit, together with any canonical
artifact changes from the final knowledge sweep. Do not stage unrelated work.
The deleted tree remains auditable through its earlier commits.

If deletion or its commit fails, report the exact remaining worktree state and
do not claim closeout.

## Handoff

Report:

- accepted outcome and delivered result
- significant decisions and their impacts
- implementation and review rounds and final results
- validation commands and outcomes
- promoted canonical artifacts, when any
- plan and closeout commits
- confirmation that the active plan tree was removed
- ready-for-review pull request URL, check status, and the pending human Merge action when the branch is published
- residual risk, skipped checks, or unrelated uncommitted work

Closeout is complete when the published pull request is ready for a human to
merge. Passing checks do not extend closeout into merging the pull request.
