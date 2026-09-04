---
name: simplify
description: Use to simplify working, verified code prior before user review or on request.
---

Review changes in the current branch, or in the scope the user specifies. Only touch code in scope, and run the validation checks after changes.

Code must stand on its own. If a change only makes sense to someone who watched it happen (this conversation, this PR), it is overfitted. Write for the reader who arrives with no history.

- Read AGENTS.md / nearby code. Match existing conventions.
- Apply YAGNI. Remove abstractions when they have one caller.
- Preserve behavior exactly.
- Remove stale comments and stale code.
- Don't expose things that don't need to be exposed, default should be private.
- Use DRY when it makes sense, even if it means touch code that was already there
- **No backwards compatibility with unshipped code.** Supporting an old signature, alias, or data shape that only existed earlier in the same branch is compatibility with something that was never deployed. Delete the old path and update its callers.
- Variable names, function names, and comments are all prose.
  - Never use a long word where a short one will do.
  - If it is possible to cut a word out, always cut it out.
  - Never use the passive where you can use the active.
  - Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
  - The exception is if any of the `docs/(adr|glossary|specs|deferred)` dirs exists or the file `.domain-modeling.toml` exists, then use the $domain-modeling skill and associated glossary.

### Comments

State, in plain English, the constraint the code cannot show: why the **non-obvious** exists.

- ✅ If code is complex and the implementation is non-obvious, add a comment.
- ✅ If a function contains complex behaviors or side effects, add a doc comment.
- 🗑️ If a comment narrates change history from the conversation, delete it.
- 🗑️ If a comment restates code whose behavior is self-evident, delete it.
