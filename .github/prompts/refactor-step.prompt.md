---
name: refactor-step
description: "Help perform a small, safe refactor step: produce a concise plan, required code edits, and minimal tests. Use when working on focused refactors across language examples."
applyTo: "**"
---

When to use
-----------
Use this prompt when you have a focused refactor task (small scope change, rename, extract method, simplify logic) and want a reproducible step-by-step edit + tests.

Inputs (provide these in your message)
------------------------------------
- `language`: The programming language or folder (e.g., `python`, `java`, `csharp`).
- `target_files`: One or more file paths or a single code selection to change.
- `goal`: Short description of the refactor goal (one sentence).
- `constraints` (optional): Backwards-compatibility, performance, API stability, or style rules.
- `tests` (optional): Whether to add/update minimal tests (`yes`/`no`).

Task
----
1. Summarize the refactor goal in one sentence.
2. List a short plan of 3–6 atomic steps to complete the refactor.
3. For each step produce the exact code edits (unified diff or file patch) and the minimal rationale.
4. If `tests=yes`, provide one or two focused unit tests and where to place them.
5. Provide commands to run the tests (point to relevant README lines when available).

Output style
------------
- Keep changes minimal and reversible.
- Use precise file paths and small patches.
- When suggesting tests, prefer existing test frameworks in the repo for that language.

Example invocation
------------------
Refactor the `update_quality()` function in `python/gilded_rose.py` to extract a helper for `aged brie` logic and add a unit test.

Notes for the agent
-------------------
- When a language-specific README exists, include a link to the line with the recommended test command.
- If multiple `target_files` are provided, prefer the smallest scope that satisfies the `goal`.
- Ask a clarifying question if the `goal` is ambiguous or the change could break public APIs.
