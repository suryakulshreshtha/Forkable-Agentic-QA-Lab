# ✨ Test-case generator

**Status:** 🚧 Planned for Phase 3.

Turns a requirement/user-story document into pytest-ready test cases using a versioned prompt template
(`prompts/test_case_prompt.v1.md`). Exposed two ways once built:

- as a plain Python function (`generate.py`) called from the CLI or from `skills/testgen-skill/`
- as an MCP tool (`mcp_server.py`) so Claude Code, Copilot, or any MCP-aware agent can call it mid-session

See [`docs/ai_qa_philosophy.md`](../../docs/ai_qa_philosophy.md) for why the prompt itself gets evaluated, not
just its output.
