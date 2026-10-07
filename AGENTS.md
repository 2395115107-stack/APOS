# Repository Guidelines

## Project Structure & Module Organization

APOS is a documentation-first operating system for AI product development. The repository is organized by numbered layers so contributors and agents read it in a stable order:

- `01-core/`: manifesto, global AI rules, and core operating principles.
- `02-product/`: product definition, roadmap, requirements, and active tasks.
- `03-design/`: design system and visual direction.
- `04-development/`: technical stack and engineering constraints.
- `05-memory/`: decisions, lessons, patterns, runs, evaluations, and evolution notes.
- `06-references/`: external research and benchmark notes.
- `07-workflows/`: repeatable workflows such as initialize, feature work, redesign, review, hotfix, release, loop, evaluation, and memory review.
- `08-agents/`: role definitions for planner, architect, designer, frontend, backend, reviewer, and testers.

There is no application source tree yet; this repository currently manages product, workflow, and agent documentation.

## Build, Test, and Development Commands

This project has no build pipeline or package manager commands at the moment. Use Git and Markdown review as the primary workflow:

- `git status`: inspect local changes.
- `git diff`: review documentation edits before committing.
- `git log --oneline -5`: check recent history.

When code or tooling is added later, document commands in `04-development/TECH_STACK.md` and update this file.

## Coding Style & Naming Conventions

Write Markdown in clear, direct language. Prefer short sections, actionable bullets, and stable labels such as `Owner`, `Next`, `Inputs`, `Outputs`, `Skills`, and `Writeback`.

Use uppercase filenames for major product records, for example `PRODUCT.md`, `TASKS.md`, and `EVALS.md`. Use lowercase hyphenated filenames for workflow documents, for example `new-feature.md` and `memory-review.md`.

## Testing Guidelines

Testing is currently documentation-based. Run `python 09-tools/check_docs.py` before closing documentation tasks: it verifies required files exist, internal path references resolve, and task entries carry all required fields.

Before closing a task, verify that:

- Requirements, tasks, workflows, agents, and memory records stay consistent.
- Any workflow change updates related files in `02-product/`, `05-memory/`, and `07-workflows/`.
- Completed work is recorded in `05-memory/RUNS.md` and evaluated in `05-memory/EVALS.md`.

## Commit & Pull Request Guidelines

Recent commits use concise imperative summaries, such as `Add beginner quickstart` and `Initialize APOS system`. Keep using short, outcome-focused commit messages.

Pull requests should include the purpose of the change, affected APOS layers, updated documents, and any follow-up tasks. Add screenshots only when visual assets or rendered documentation are changed.

## Agent-Specific Instructions

Root `AGENTS.md` is the contributor guide. The operating rules for AI agents live in `01-core/AGENTS.md`. When in doubt, follow the numbered APOS flow: read core rules, clarify product intent, choose a workflow, execute with agents, then write back to memory.
