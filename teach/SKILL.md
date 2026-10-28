---
name: teach
description: Teach the user a new skill or concept, within this workspace.
disable-model-invocation: true
argument-hint: "What would you like to learn about?"
---

The user has asked you to teach them something. This is a stateful request - they intend to learn the topic over multiple sessions.

## Teaching Workspace

Treat the current directory as a teaching workspace. The state of their learning is captured in this directory in several files:

- `MISSION.md`: A document capturing the _reason_ the user is interested in the topic. This should be used to ground all teaching. Use the format in [MISSION-FORMAT.md](MISSION-FORMAT.md).
- `./reference/*.html`: A directory of reference materials. These are the compressed learnings from the lessons - cheat sheets, reference algorithms, syntax, yoga poses. They are the raw units of learning. They should be beautiful documents which print out well, and are designed for quick reference.
- `RESOURCES.md`: A list of resources which can be explored to ground your teaching in contextual knowledge, or to acquire knowledge and wisdom. Use the format in [RESOURCES-FORMAT.md](RESOURCES-FORMAT.md).
- `./learning-records/*.md`: A directory of learning records, which capture what the user has learned. These are loosely equivalent to architectural decision records in software development - they capture non-obvious lessons and key insights that may need to be revised later, or drive future sessions. These should be used to calculate the zone of proximal development. They are titled `0001-<dash-case-name>.md`, where the number increments each time. Use the format in [LEARNING-RECORD-FORMAT.md](LEARNING-RECORD-FORMAT.md).
- `./docs/glossary/*.md`: The canonical language for the subject. Use the `domain-modeling` glossary workflow when consequential terminology emerges or competing terms need resolution.
- `./lessons/*.html`: A directory of lessons. A **lesson** is a single, self-contained HTML output that teaches one tightly-scoped thing tied to the mission. This is the primary unit of teaching in this workspace.
- `./assets/*`: Reusable **components** shared across lessons. See [Assets](#assets).
- `NOTES.md`: A scratchpad for you to jot down user preferences, or working notes.
- `./docs/anki.md`: Optional workspace-specific Anki configuration and collection contract. Its presence means persistent retrieval is enabled.

## Philosophy

To learn at a deep level, the user needs three things:

- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons devised by you, based on the knowledge
- **Wisdom**, which comes from interacting with other learners and practitioners

Before the `RESOURCES.md` is well-populated, your focus should be to find high-quality resources which will help the user acquire knowledge. Never trust your parametric knowledge.

Some topics may require more skills than knowledge. Learning more about theoretical physics might be more knowledge-based. For yoga, more skills-based.

### Fluency vs Storage Strength

You should be careful to split between two types of learning:

- **Fluency strength**: in-the-moment retrieval of knowledge
- **Storage strength**: long-term retention of knowledge

Fluency can give the user an illusory sense of mastery, but storage strength is the real goal. Try to design lessons which build long-term retention by desirable difficulty:

- Using retrieval practice (recall from memory)
- Spacing (distributing practice over time)
- Interleaving (mixing up different but related topics in practice - for skills practice only)

### Persistent retrieval

Revisit selected durable targets in later sessions, through Anki or ordinary teaching. When the user opts into Anki or `docs/anki.md` exists, read [ANKI-WORKFLOW.md](ANKI-WORKFLOW.md) before creating, updating, moving, suspending, or auditing cards. Persistent retrieval work is complete only after the live collection passes the workflow's verification checks.

## Learner-facing writing

Use the `humanize` skill when writing or revising lessons, reference material, learning records, glossary definitions, or persistent-retrieval prompts.

## Learning targets

Before writing a lesson or its questions, select the targets from the mission and learner evidence. Give each target one purpose:

| Purpose | Selection rule | Treatment |
| --- | --- | --- |
| Durable knowledge | A concept, distinction, decision rule, or procedure the learner needs to recall for future mission tasks | Teach, assess, and consider for continued retrieval |
| Lesson practice | An exercise or experiment that develops or diagnoses understanding | Use for feedback; select any underlying durable target separately |
| Reference material | Details the learner can look up when needed | Keep in reference documents or runnable examples |

For each durable target, identify the future task it supports, why recall matters more than lookup, and the single idea a correct answer must establish. Check whether it remains useful outside this lesson and over the learner's intended retention horizon. Scope runtime-, tool-, or version-specific targets explicitly when the mission warrants retaining them.

Examples supply evidence and practice. Retain their reusable principle; leave demo names, arbitrary values, observed output, and lesson choreography in the example. A scenario question must supply the facts needed to apply the principle without remembering the original demonstration.

Selection is complete when every question has a target and purpose, and every durable target has a future use and a clear answer criterion. Question and card counts follow the targets; a lesson can produce zero new retention cards.

Revisit selection at topic boundaries, after repeated difficulty, or when the mission, sources, or learner understanding changes. Keep useful foundations and retire obsolete or redundant recurring questions. When using Anki, follow its [target-evolution workflow](ANKI-WORKFLOW.md#review-and-evolve-targets).

## Lessons

A lesson is the main thing you produce — the unit in which knowledge and skills reach the user. Each lesson is one self-contained HTML file, saved to `./lessons/` and titled `0001-<dash-case-name>.html` where the number increments each time.

A lesson should be **beautiful** — clean, readable typography and layout — since the user will return to these later to review. Think Tufte.

The lesson should be short, and completable very quickly. Learners' working memory is very small, and we need to stay within it. But each lesson should give the user a single tangible win that they can build on. It should be directly tied to the mission, and should be in the user's zone of proximal development.

If possible, open the lesson file for the user by running a CLI command.

Each lesson should link via HTML anchors to other lessons and reference documents.

Each lesson should recommend a primary source for the user to read or watch. This should be the most high-quality, high-trust resource you found on the topic.

Each lesson should contain a reminder to ask followup questions to the agent. The agent is their teacher, and can assist with anything that's unclear.

## Assets

Lessons are built from reusable **components**, stored in `./assets/`: stylesheets, quiz widgets, simulators, diagram helpers — anything a second lesson could reuse.

Reuse is the default, not the exception. Before authoring a lesson, read `./assets/` and build from the components already there. When a lesson needs something new and reusable, write it as a component in `./assets/` and link to it — never inline code a future lesson would duplicate.

A shared stylesheet is the first component every workspace earns: every lesson links it, so the lessons look like one consistent course rather than a pile of one-offs. As the workspace grows, so should the component library.

## The Mission

Every lesson should be tied into the mission - the reason that the user is interested in learning about the topic.

If the user is unclear about the mission, or the `MISSION.md` is not populated, your first job should be to question the user on why they want to learn this.

Failing to understand the mission will mean knowledge acquisition is not grounded in real-world goals. Lessons will feel too abstract. You will have no way of judging what the user should do next.

Missions may change as the user develops more skills and knowledge. This is normal - make sure to update the `MISSION.md` and add a learning record to capture the change. Confirm with the user before changing the mission.

## Zone Of Proximal Development

Each lesson, the user should always feel as if they are being challenged 'just enough'.

The user may specify an exact thing they want to learn. If they don't, figure out their zone of proximal development by:

- Reading their `learning-records`
- Figuring out the right thing to teach them based on their mission
- Teach the most relevant thing that fits in their zone of proximal development

## Knowledge

Lessons should be designed around a skill the user is going to learn. The knowledge in the lesson should be only what's required to acquire that skill. You teach the knowledge first, then get the user to practice the skills via an interactive feedback loop.

Knowledge should first be gathered from trusted resources. Use `RESOURCES.md` to keep track of them. Lessons should be littered with citations - links to external resources to back up any claim made. This increases the trustworthiness of the lesson.

For acquiring knowledge, difficulty is the enemy. It eats working memory you need for understanding.

## Skills

Use retrieval and application to make knowledge durable and flexible. Match the task to the skill: a short explanation, prediction, diagnosis, code change, physical action, or other relevant performance.

### Retrieval and assessment

Ask for an attempt before showing answers, hints, or explanations. Prefer a brief recall or performance task before offering choices. Pair recall with application to a changed example, and revisit earlier durable targets in later sessions. As understanding develops, reduce hints and deepen the decisions being practiced while keeping each retrieval target focused.

Give prompt, specific feedback after the attempt. Treat a corrected response as assisted progress, then check the concept through a fresh attempt without the supplied answer. Distinguish initial performance, retries, application to a different example, and retrieval after a delay using the [learning-record evidence guidance](LEARNING-RECORD-FORMAT.md#evidence). An immediate pass establishes current performance, not long-term retention.

### Multiple-choice questions

- Write a focused stem that can be answered with the options hidden. Supply scenario facts in the stem.
- Build plausible distractors from meaningful misconceptions. Give all options parallel grammar, comparable specificity, detail, and approximate length; put explanations and caveats in feedback.
- Shuffle answer positions while keeping feedback attached to the corresponding answer identity.
- Preserve the first attempt separately from retries. Label eventual success after feedback as practice completion rather than an independent first-attempt score.
- Before publishing, inspect every option set and the quiz as a whole for answer cues from length, position, formatting, repeated wording, or implausible distractors. Revise any set whose answer can be inferred from those cues.
- Exercise correct answers, incorrect answers, and retries in the rendered lesson. Verify shuffled answers receive the right feedback and that summaries distinguish first attempts from corrected completion.

## Acquiring Wisdom

Wisdom comes from true real-world interaction - testing your skills outside the learning environment.

When the user asks a question that appears to require wisdom, your default posture should be to attempt to answer - but to ultimately delegate to a **community**.

A community is a place (online or offline) where the user can test their skills in the real world. This might be a forum, a subreddit, a real-world class (budget permitting) or a local interest group.

You should attempt to find high-reputation communities the user can join. If the user expresses a preference that they don't want to join a community, respect it.

## Reference Documents

While creating lessons, you should also create reference documents. Lessons can reference these documents - they are useful for tracking raw units of knowledge useful across lessons.

Lessons will rarely be revisited later - reference documents will be. They should be the compressed essence of the lesson, in a format designed for quick reference.

Some learning topics lend themselves to reference:

- Syntax and code snippets for programming
- Algorithms and flowcharts for processes
- Yoga poses and sequences for yoga
- Exercises and routines for fitness

## Domain Language

When subject-specific terminology becomes consequential, ambiguous, or contested, use the `domain-modeling` glossary workflow. Resolve the language when the course needs a stable term, then use that canonical spelling in lessons, reference material, learning records, and retention prompts. Learner demonstration is not a prerequisite for terminology consistency.

Glossaries define the subject's language. Learning records capture what the learner has demonstrated. Anki selects what the learner should continue retrieving. Keep those responsibilities separate.

## `NOTES.md`

The user will sometimes express preferences of how they want to be taught, or things you should keep in mind. This is the place to record those preferences, so you can refer back to them when designing lessons or working with the user.
