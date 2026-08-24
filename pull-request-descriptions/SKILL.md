---
name: pull-request-descriptions
description: Write or revise pull request and merge request description.
---

# Pull Request Descriptions

A pull request description is a guide for human review. Add the purpose, context, and judgment the diff cannot provide,
then direct attention to the places where review is most valuable.

## Establish the review context

Inspect the diff against its base, the issue or request it serves, committed design and domain artifacts, the repository's
pull request template, and its continuous integration workflow. Establish:

- the problem and intended outcome;
- who or what is affected, including breaking behavior, migration, and rollout concerns;
- the choices and tradeoffs that are not obvious from the code;
- the risky, uncertain, incomplete, or consequential areas that deserve close review; and
- any useful evidence gathered beyond the repository's normal automation.

Support every claim with the inspected change or repository context. Make the description self-contained and link only
to resources available to reviewers, never agent conversations or uncommitted local files.

When the change relies on artifacts governed by
[`domain-modeling`](../domain-modeling/SKILL.md), invoke that skill to recover canonical language and the owning artifact.
Preserve those terms in the technical part of the description and link to committed artifacts when that helps the
reviewer.

## Write for two reading depths

Open with a short executive summary in plain language. State the problem, the outcome, and the affected behavior. Keep
implementation vocabulary out of this opening where ordinary language carries the meaning. Put breaking changes or
unusual rollout requirements here when they change the reader's decision about the pull request.

Follow with only the technical context needed for a useful review. Explain the approach and its tradeoffs where the diff
cannot, using precise code and domain terms when they reduce ambiguity. Point reviewers to specific risks, assumptions,
open questions, or known incomplete work. Say what is safe to skim when mechanical changes would otherwise hide the
important work. Expand uncommon acronyms on first use.

Use prose by default. Use bullets for genuine peer lists such as review targets, and headings only when they make a
description easier to scan. Omit empty sections and generic statements.

## Spend words on hidden information

Treat the diff, commit list, and continuous integration results as reviewer-visible context rather than material to
repeat. Leave out file-by-file inventories, commit-log summaries, and routine test or lint reports that duplicate the
repository's automation.

Include validation only when it adds evidence reviewers would not otherwise see: a manual scenario, an environment or
production check, a one-off analysis, or another step beyond continuous integration. State a meaningful unverified case
when it changes the risk assessment. Include screenshots, migration or deploy ordering, deliberate follow-ups, and
rollback constraints only when applicable.

## Finalize

Apply [`humanize`](../humanize/SKILL.md) to the complete draft. Then cut anything that merely narrates the diff, proves
that normal automation ran, or does not help the reviewer decide, understand, or focus.

Finish when the opening is understandable without implementation jargon, the remainder directs review toward the
non-obvious work, every retained claim is supported, and no routine inventory or continuous integration report remains.
Return only the finished description unless the user asks for commentary.
