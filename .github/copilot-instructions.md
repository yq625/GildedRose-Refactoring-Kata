---
name: copilot-instructions
description: "Workspace instructions for GitHub Copilot Chat: guidance for running tests, editing language examples, and making contributions. Use when: working on language folders, running TextTest fixtures, or updating examples."
applyTo: "**"
---

Purpose
-------
Keep agent guidance concise and link to authoritative docs in this repo. Don't duplicate per-language README content; link instead.

Quick Start
-----------
- Build & test: consult the language-specific README under each top-level folder (for example, `c99/`, `go/`, `TypeScript-deno/`).
- Common test runner: use [start_texttest.sh](start_texttest.sh) to run TextTest-based fixtures used across language implementations.

Where to look
-------------
- Main README: [README.md](README.md#L1)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md#L1)
- CI/workflows: [.github/workflows/](.github/workflows/)
- Language examples: top-level language folders (e.g., `c99/`, `java/`, `python/`) — each contains its own README with exact commands.

Conventions
-----------
- Small, focused commits per language example.
- Preserve existing language folder structure when adding tests.
- When proposing changes to many language folders, open a single tracking issue and link PRs.

How the agent should help
------------------------
- Prefer linking to files over embedding long commands or docs.
- When asked to run or suggest commands, reference the exact language README and include line links.
- For multi-step changes (create/update many files), ask for confirmation and create a short TODO plan first.

Example prompts
---------------
- "Create a small unit test for the Java implementation and run its test suite."
- "Add a README snippet under `go/` with the exact `go test` command and expected output." 
- "Add a new TextTest fixture and run `start_texttest.sh` to validate." 

Next suggestions
----------------
- Add short, focused prompts in `.github/prompts/` for common tasks (create test, run TextTest, add language example).
- Consider an agent `create-pr.agent.md` to encapsulate PR checklist and formatting hooks.

If you want, I can now create `.github/prompts/` and a small example prompt file, or add a `create-pr.agent.md` template.
