---
name: structured-delivery-workflow
description: Structure high-risk or multi-phase engineering delivery through separate requirements, design, task, review, and knowledge-promotion gates. Use when work needs a reviewable plan, spans threads or agents, carries migration, data, architecture, compliance, or parity risk, or requires durable traceability.
disable-model-invocation: true
license: Apache-2.0
compatibility: Works best in repositories that allow markdown/yaml planning artifacts and test/build execution.
metadata:
  author: realityforge
  version: "4.0"
---

# Structured Delivery Workflow

Use a persistent plan tree to preserve reviewed requirements, implementation
design, task state, and validation evidence across risky or multi-threaded
delivery.

## Guardrails

- Identify the active plan tree before editing files under `plans/`, and scope
  every plan edit to that tree.
- Read only the routed instruction for the current stage and the context it
  points to. Load a template only when creating its corresponding artifact.

## Entry

Use the persistent plan tree path only. Read
`instructions/existing-plan-implementation.md` first when implementing from an
accepted plan. Otherwise read `instructions/planning.md` to create or revise
the plan.

## Stage Router

- Updating persistent task state: read `instructions/task-tracking.md`.
- Reviewing a persistent planning stage, asking for user review, or accepting a
  plan: read `instructions/review-and-approval.md`.
- Handling post-implementation issues or reviewing implementation outcomes:
  read `instructions/implementation-review.md`.
- A domain term, qualifying adopted decision, or user-deferred question settles,
  or durable knowledge must be promoted before plan cleanup: read
  `instructions/knowledge-promotion.md`.
- Removing completed plan artifacts: read `instructions/plan-cleanup.md`.
- Preparing the final response: read `instructions/closeout.md`.

## Output Style

- Prefer links to planning files over pasted artifacts.
