---
name: refine-agents-md
description: Refactor AGENTS.md to improve clarity, conciseness, and organization.
disable-model-invocation: true
---

First load $writing-for-agents skill.

Then refactor the AGENTS.md file to follow progressive disclosure principles. 

Follow these steps:

1. **Find contradictions**: Identify any instructions that conflict with each other. For each contradiction, ask me which version I want to keep.

2. **Identify the essentials**: Extract only what belongs in the root AGENTS.md:
    - One-sentence project description
    - Build and verification commands if they are non-standard
    - Anything truly relevant to every single task

3. **Group the rest**: Organize remaining instructions into logical categories (e.g., Language conventions, testing patterns, API design, Git workflow). For each group, create a separate markdown file.

4. **Create the file structure**: Output:
    - A minimal root AGENTS.md with markdown links to the separate files
    - Each separate file with its relevant instructions
    - A suggested docs/agents folder structure

5. **Flag for deletion**: Identify any instructions that are:
    - Redundant (the agent already knows this)
    - Too vague to be actionable
    - Overly obvious (like "write clean code")
