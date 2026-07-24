# Domain Glossary Format

Domain terminology lives under `docs/glossary/`. The directory is the single canonical location; create it lazily when the first term is resolved.

## Structure

`README.md` is the glossary entry point. A small glossary may keep every term there:

```md
# Domain Glossary

**Order**:
A request by a Customer to obtain goods.
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a Customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places Orders.
_Avoid_: Client, buyer, account
```

When independently navigable subject areas emerge, move their terms into topic files:

```text
docs/glossary/
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

**<Term>**:
<One- or two-sentence definition.>
_Avoid_: <Competing terms>
```

## Rules

- **Keep it a glossary.** Define domain terms and route other conclusions to their owning artifacts.
- **Give every term one owner.** Define a shared term in the topic that owns its core meaning and link to it from dependent topics.
- **Be opinionated.** Pick one canonical term and list competing words under `_Avoid_`.
- **Keep definitions tight.** Use one or two sentences that define what the concept is.
- **Keep terms domain-specific.** General programming and engineering vocabulary belongs elsewhere.
- **Split by navigable subject.** Topic files organize navigable language only; bounded contexts, ownership boundaries, and source layout require their own evidence.
- **Use relationships sparingly.** Keep a relationship in `README.md` only when it helps readers locate or interpret terminology.

## Updating the glossary

1. Search `docs/glossary/` for the term, its synonyms, and related concepts.
2. Select the existing topic that owns its core meaning.
3. Resolve contradictions with documented language or code before editing.
4. Probe relationships with concrete edge-case scenarios.
5. Update the owning file immediately after the term is resolved.
6. Create a topic only when a coherent, independently navigable group has emerged; add it to `README.md` in the same change.

The update is complete when the term has one canonical definition, competing language is identified where useful,
every affected glossary topic and durable artifact remains consistent, and requirements and decisions remain in their
owning artifacts.
