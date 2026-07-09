---
name: commit
description: "Read this skill before making git commits"
---

Create one Conventional Commit for intended local changes. Commit only; do not push.

## Message

- Subject: `<type>(<scope>): <summary>`; type required, scope optional, summary imperative, <=72 chars, no period. Types: `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `perf`.
- Body: include unless trivial; explain what changed and why.
- No breaking-change markers/footers, sign-offs, or `Signed-off-by`.

## Inputs

- Treat caller args as guidance.
- Paths/globs limit staging; freeform text guides subject/body.
- If changed files are ambiguous, ask before staging.

## Workflow

1. Review `git status` and relevant `git diff`.
2. If style/scope is unclear, inspect `git log -n 50 --pretty=format:%s`.
3. Stage only intended files; stage all changes only when no paths/globs were specified.
4. Inspect `git diff --cached`.
5. Run normal commit hooks; do not bypass them.
6. Run `git commit -m "<subject>"` and add `-m "<body>"` when needed.
