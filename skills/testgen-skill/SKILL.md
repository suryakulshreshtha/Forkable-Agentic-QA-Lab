---
name: testgen-skill
description: Use when asked to turn a requirement, user story, or spec document into pytest test cases for this repo's suites.
---

# Test-case generator skill

**Status:** 🚧 Planned for Phase 3 — this SKILL.md describes the intended behaviour; `src/testgen/generate.py`
is the implementation it calls.

## When to use this

When someone hands you a requirement, a user story, or a short spec and asks for test cases — for the
`web_api`, `llm_app`, `windows_desktop`, or `power_platform` suites in this repo.

## Steps

1. Read the requirement/user-story text in full.
2. Identify which suite it belongs to (`tests/web_api/`, `tests/llm_app/`, `tests/windows_desktop/`, or
   `tests/power_platform/`) from the feature area it describes.
3. Run `uv run python -m src.testgen.generate --input <path-or-text> --suite <suite-name>` (see
   `src/testgen/README.md` once built) — this applies the versioned prompt template in
   `src/testgen/prompts/` and returns pytest-ready code.
4. Write the output to `tests/generated/<suite-name>/test_<slug>.py`.
5. Run `uv run pytest tests/generated/<suite-name>/test_<slug>.py` to confirm it at least collects and runs
   (not that it passes — a generated test failing against real code is itself a useful signal, not a bug in
   the generator).
6. Tell the person what suite the case was added to and what it checks, in one or two sentences — not the
   full generated code, unless they ask to see it.

## Notes

- The generation prompt itself is evaluated (not just the tests it produces) — see
  `docs/ai_qa_philosophy.md` for why, and `tests/llm_app/test_prompt_eval.py` for how.
- This same capability is also exposed as an MCP tool (`src/testgen/mcp_server.py`) for agents that prefer a
  structured tool call over this file-based skill — use whichever your runtime supports.
