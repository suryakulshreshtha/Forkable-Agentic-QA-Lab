# 🧠 Sample LLM app

**Status:** 🚧 Planned for Phase 3.

A small chat/assistant endpoint that `tests/llm_app/` drives through Playwright MCP (UI layer) and
DeepEval/Ragas/Promptfoo (output evaluation).

**Open decision (flagged in the feasibility study, Section 9):** should this wrap a real third-party LLM API,
or run against a small self-hosted/mock model so the whole repo runs offline and free for any reviewer? This
should be decided before this folder is built out — see `docs/ai_qa_philosophy.md` for the evaluation
approach either way.
