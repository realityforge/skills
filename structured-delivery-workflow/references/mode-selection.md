# Mode Selection

Choose the lightest mode that preserves decisions, sequencing, and validation
evidence. Start lighter when uncertain, then escalate if evidence shows durable
planning state is needed.

## Lightweight Implementation

Use for bounded implementation work where:

- the user did not ask for plan artifacts
- the work can finish in the current thread
- no durable handoff, audit trail, or delegated implementation state is needed
- validation can be summarized in chat

Keep state in conversation:

- scope in one or two sentences
- short task checklist, if useful
- targeted and final validation commands
- final summary with files changed and verification results

Do not create `plans/` files for lightweight implementation.

## Persistent Plan Tree

Use when at least one is true:

- the user asks to create a plan, emit planning artifacts, or pause for review
- the user explicitly asks for persistent requirements, task board,
  traceability, or audit evidence
- work is multi-phase or expected to span multiple threads or days
- another agent will implement from the plan and needs machine-readable task
  state
- migration, data safety, architecture, compliance, or parity risk is high
- repository convention already requires a persistent plan tree

Default persistent plan tree:

```
plans/<initiative>/
  00-requirements.md
  10-implementation-plan.md
  20-task-board.yaml
```

Create optional files only when they add useful durable state:

- `40-test-strategy.md` for complex or multi-environment validation
- `30-compatibility-matrix.md` for parity or migration work
- `30-output-contract.md` for CLI/API output contracts
- `01-*-deep-dive.md` for focused decisions that would overload requirements
- `50-implementation-issues.md` only after real follow-up issues exist

Use the reference templates only when creating the corresponding files:

- Requirements deep dive template: `requirements-deep-dive-template.md`
- Implementation plan template: `implementation-plan-template.md`
- Task board template: `task-board-template.yaml`
