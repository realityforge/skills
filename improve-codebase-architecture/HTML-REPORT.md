# HTML Report

Use this reference only while producing the architecture review in step 3 of
[SKILL.md](SKILL.md).

## Shape

Produce one static HTML file. Tailwind may load from its CDN and Mermaid 11 may
load as an ES module from its CDN. Use Mermaid for dependency, call-flow, and
sequence diagrams; use HTML, CSS, or inline SVG when a mass diagram,
cross-section, or collapsed call graph communicates the change better.

Keep the page editorial rather than dashboard-like: a narrow reading width,
generous space, restrained color, and diagrams that carry more of the argument
than the prose. Use one accent color, red for leakage, and amber for conflicts.

The page contains:

1. a header with repository name, date, and a compact diagram legend;
2. one card per candidate;
3. one top-recommendation card linking to the preferred candidate.

## Candidate card

Each card contains:

- a short title naming the responsibility change;
- a confidence badge and relevant dependency or structural-axis labels;
- affected files and representative callers in monospace;
- equally weighted before-and-after diagrams;
- one sentence describing the evidenced friction;
- one sentence describing the responsibility change worth examining;
- short gains tied to Depth, Leverage, Locality, or behavioral tests;
- one concise ADR or specification warning when applicable.

The diagrams should show the architectural claim directly. Useful patterns
include:

- **Dependency or call flow:** show repeated coordination or knowledge leaking
  across current Seams, then the proposed concentration behind one Interface.
- **Mass diagram:** compare Interface surface with hidden Implementation before
  and after deepening.
- **Cross-section:** show several thin pass-through Modules becoming one deep
  Module with internal structure.
- **Call-graph collapse:** retain internal calls as faded detail inside the new
  Module while reducing what callers must know.
- **Sequence:** compare repeated caller-managed steps with one outcome-oriented
  interaction.

Vary the pattern when the candidates make different claims. Keep each diagram
compact enough for the before-and-after pair to remain visible together on a
desktop screen, and stack them on narrow screens.

## Vocabulary and prose

Use the glossary from `$codebase-architecture` and the repository's
specializations precisely. Terms such as component, service, API, boundary, or
Artifact remain valid when the repository uses them for a distinct concept; do
not substitute them for Module, Interface, Seam, or another architectural term.

Name the mechanism and evidence. Prefer “three callers repeat retry ordering”
over “the code is hard to maintain.” Keep every sentence or bullet necessary to
choose between candidates. Exact Interface proposals belong after the user has
selected a candidate.

## Minimal scaffold

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Architecture review for {{repository}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true, theme: "neutral", securityLevel: "loose" });
    </script>
    <style>
      .seam { stroke-dasharray: 4 4; }
      .leak { stroke: #b91c1c; }
      .deep { background: #172033; color: white; }
    </style>
  </head>
  <body class="bg-stone-50 text-slate-900">
    <main class="mx-auto max-w-5xl space-y-12 px-6 py-12">
      <header>...</header>
      <section id="candidates" class="space-y-10">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

No repository files, application code, or interactive controls are required.
