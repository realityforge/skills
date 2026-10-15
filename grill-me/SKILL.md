---
name: grill-me
description: A relentless interview that asks every frontier question at once, round by round.
disable-model-invocation: true
---

Run a full interview when the user explicitly requests it. Recover accepted decisions from their sources and use them as settled branches. Reopen them only under the [decision policy](../AGENTS.md#scope-and-design).

Interview the unresolved design relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled — the questions you can ask *now* without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each round the user answers reshapes the tree — settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a *later* round, not this one.

Finding *facts* is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it — don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report — ask the rest of the frontier now. The *decisions* are the user's — put each to them and wait.

The frontier is empty when every design branch is settled by an accepted decision or an interview answer. Summarize the resulting understanding and obtain the user's explicit confirmation before acting on it, even when the interview reused all decisions. Recover execution authority under the decision policy and ask only if it is missing.

If any of the `docs/(adr|glossary|specs|deferred)` dirs exists or the file `.domain-modeling.toml` exists then use the $domain-modeling skill.
