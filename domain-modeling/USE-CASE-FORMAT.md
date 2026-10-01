# Essential Use Case Format

Essential use cases live at `<context-root>/use-cases/<kebab-case-goal>.md`. Create `use-cases/` only when the first case
qualifies. A case describes how a person and the system cooperate to achieve a meaningful goal across possible
interfaces. It composes requirements; it does not own their exact rules.

## Qualification

Create a case when all of these hold:

1. The user role, goal, and successful outcome are accepted rather than speculative.
2. The goal is meaningful to the user independently of a screen, control, route, or delivery increment.
3. The intention and responsibility structure connects multiple requirements or clarifies a task that one
   specification's Purpose cannot express concisely.

Otherwise, use the existing specification's Purpose, or keep a proposed goal in its design or backlog. One case may
connect several specifications; one specification may support several cases. Do not create a case for each user story.

## Format

```md
# <User goal>

**Role:** <Who pursues this goal.>
**Success:** <What the person can accomplish or know when the task succeeds.>

## Intentions and responsibilities

| User intention | System responsibility |
| --- | --- |
| <Goal-level intention> | <Observable responsibility at the same level> |

## Material alternatives

<Only outcomes that change how the user can complete or recover the task. Omit when none exist.>

## Governing contracts

<Links to the specifications that own exact behavior. Add an ADR only when its choice materially constrains the task.>
```

Keep the dialogue at the level of intentions and responsibilities. Describe a necessary order only when the task
requires it. Use domain language; avoid interface gestures, endpoint names, data layouts, and test procedure. Link the
first body use of every glossary-owned term to its canonical heading. Link the governing specifications rather than
copying their requirements or acceptance examples. A specification may link back when the goal adds useful context;
reciprocal links are not required.

## Capture and update

1. Read the relevant glossary, specifications, ADRs, existing use cases, and plans. Identify the current owner of each
   accepted obligation before drafting.
2. Apply the qualification test and search the context's `use-cases/` for an existing goal or an overlapping case.
3. Draft the role, success outcome, and intention-responsibility dialogue. Route any newly discovered accepted
   obligation through [SPEC-FORMAT.md](./SPEC-FORMAT.md); keep unresolved design in its existing owner.
4. Check each responsibility against its governing specification. Resolve contradictions, replace duplicated rules
   with links, and update inbound links when renaming or removing a case.

Capture is complete when the case qualifies, has one goal and one owner, every accepted obligation has a specification
owner, the case adds task understanding without duplicating exact rules, and its glossary and contract links resolve.
Run [`scripts/validate_doc_links.py`](./scripts/validate_doc_links.py) against the repository root after a change.
