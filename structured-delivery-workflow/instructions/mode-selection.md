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

Keep scope, any useful checklist, validation commands, and final evidence in
conversation. Create no persistent planning artifacts.

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

After selecting this mode, read `planning.md` for the ordered stages, default
artifacts, optional artifacts, and templates.
