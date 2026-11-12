# Artifact Catalogs

A catalog is the `README.md` in an `adr/`, `deferred/`, `specs/`, or `use-cases/` directory. It lets a fresh reader find
the artifact that owns a question without opening every file. The glossary's `README.md` follows
[GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md) instead.

## Placement

Create the catalog when its directory gains a second artifact. The catalog is navigation, not an artifact: it owns no
requirement, decision, rationale, or status.

## Entries

List every artifact in the directory exactly once as an entry: a relative link titled with the artifact's title,
followed by one line stating what it owns. Add per kind:

| Directory | Entry also states |
| --- | --- |
| `specs/` | The requirement-ID prefix. When specifications form a pipeline, what each consumes and produces and which specifications it depends on. |
| `deferred/` | The neutral question and a condensed `Reconsider when` trigger, so triggers can be checked from the catalog alone. |
| `adr/` | The ADR number and the adopted choice in one line. |
| `use-cases/` | The role and goal. |

Group entries by subject or stage once a flat list stops being scannable. A specification catalog may add reading
orders that link specifications again outside the entries.

## Update

Update the catalog in the same change that creates, renames, splits, merges, or deletes an artifact, or changes what an
artifact owns, its requirement prefix, or a deferred trigger.

The catalog is current when every artifact in its directory appears exactly once as an entry and every entry's summary
matches its artifact. [`scripts/validate_doc_links.py`](./scripts/validate_doc_links.py) reports artifacts a catalog
does not link and catalog links to missing files.
