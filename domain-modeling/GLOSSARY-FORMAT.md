# Domain Glossary Format

Domain terminology lives under `<context-root>/glossary/`. The directory is the context's canonical location; create it
lazily when the first term is resolved.

## Structure

`README.md` is the glossary entry point. A small glossary may keep every term there:

```md
# Domain Glossary

## Language

### Order

A request by a [Customer](#customer) to obtain goods.
_Avoid_: Purchase, transaction

### Invoice

A request for payment sent to a [Customer](#customer) after delivery.
_Avoid_: Bill, payment request

### Customer

A person or organization that places an [Order](#order).
_Avoid_: Client, buyer, account
```

When independently navigable subject areas emerge, move their terms into topic files:

```text
<context-root>/glossary/
├── README.md
├── ordering.md
├── billing.md
└── fulfillment.md
```

`README.md` then links the topics and records only relationships needed to navigate or interpret the language:

```md
# Domain Glossary

## Topics

- [Ordering](./ordering.md) — receives and tracks customer orders
- [Billing](./billing.md) — generates invoices and processes payments
- [Fulfillment](./fulfillment.md) — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

A topic file names the subject area, briefly establishes its scope, then defines its terms:

```md
# <Topic>

<One sentence establishing scope.>

## Language

### <Term>

<One- or two-sentence definition.>
_Avoid_: <Competing terms>
```

A term heading supplies its GitHub-style Markdown fragment: `### Interactive Authentication` becomes
`#interactive-authentication`.

## Rules

- **Keep it a glossary.** Define domain terms and route other conclusions to their owning artifacts.
- **Give every term one owner.** Define it once under a level-three heading whose text is the canonical term, and link to
  that heading from dependent topics.
- **Be opinionated.** Pick one canonical term and list competing words under `_Avoid_`.
- **Keep definitions tight.** Use one or two sentences that define what the concept is.
- **Keep terms domain-specific.** General programming and engineering vocabulary belongs elsewhere.
- **Split by navigable subject.** Topic files organize navigable language only; bounded contexts, ownership boundaries, and source layout require their own evidence.
- **Use relationships sparingly.** Keep a relationship in `README.md` only when it helps readers locate or interpret terminology.

## Updating the glossary

1. Search the applicable context's `glossary/` for the term, its synonyms, and related concepts.
2. Select the existing topic that owns its core meaning.
3. Resolve contradictions with documented language or code before editing.
4. Probe relationships with concrete edge-case scenarios.
5. Update the owning file immediately after the term is resolved.
6. Create a topic only when a coherent, independently navigable group has emerged; add it to `README.md` in the same change.
7. After renaming or moving a term, update every inbound term link.

The update is complete when the term has one canonical level-three heading, competing language is identified where
useful, every required first-use link resolves to that heading, affected glossary topics and durable artifacts use the
canonical spelling, and requirements and decisions remain in their owning artifacts.
