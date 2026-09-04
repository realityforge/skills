---
name: explain-diff-html
description: Use when the user asks for a rich explanation of a code change, diff, branch, or PR. Produces HTML output.
disable-model-invocation: true
---

# Explain Diff

Please make me a rich, interactive explanation of the specified code change.

It should have these sections:

- Executive overview: Overview that is understandable without reading the rest of the report and short enough to read in about one minute. Explains essential project-specific terms, impacts and risks
- Background: Explain the existing system relevant to this change. (You should broadly explore surrounding code for this.) We don't know how much the reader already knows, so include a deep background for beginners (note that it can be skipped if the reader is already familiar), and then a more narrow background directly relevant to the change.
- Intuition: Explain the core intuition for the code change. The focus here is to explain the essence, not the full details. Use concrete examples with toy data. Use figures and diagrams liberally.
- Code: Do a high-level walkthrough of the changes to the code. Group/order the changes in an understandable way.
- Quiz: Come up with five questions that test the reader's knowledge of this PR. This should be medium difficulty, difficult enough that you actually need to understand the substance of the PR to answer them, but not gotchas. The goal is to help the reader make sure that they've actually understood. These should be presented as interactive multiple-choice questions, and when the user clicks, it tells them whether they were correct and gives feedback.

Format:

- Output a single self-contained HTML file which includes CSS and JavaScript. Make the whole thing one long page with section headers and a table of contents. Don't use tabs for the top-level structure. Basic responsive styling so you can view it on a phone is nice too. Put the file inside a repository local temp directory or if no such dir exists in a global place on my computer outside of the code repo, and make sure the filename always starts with today's date in `YYYY-MM-DD-` format, because it helps keep the files time-sorted and out of version control. For example: 2026-01-12-explanation-<slug>.html
- Please write with the clarity and flow of Martin Kleppmann, making it engaging and written in classic style. Transitions between sections should be smooth.
- Some tips on diagrams. Ideally, you should pick a small number of diagram families that can be reused throughout the explanation to explain various cases. Some useful kinds of diagrams:
    - A very simplified version of the UI that the user sees in the app, to explain UI changes.
    - A system diagram showing data flow or communication between components. Make sure to include example data here!
- Don't use ASCII diagrams. Use simple HTML designs for your diagrams, HTML lists for lists of things, etc. For complex diagrams feel free to use SVG or $mermaid-diagrams skill.
- Use callouts for key concepts or definitions, important edge cases, etc.

If any of the `docs/(adr|glossary|specs|deferred)` dirs exists or the file `.domain-modeling.toml` exists then use the $domain-modeling skill. Add a glossary at the end for any domain or project specific terms.
