# 🧪 Tests

One `pytest` entry point, five sub-packages — each can run in isolation:

```bash
uv run pytest tests/web_api          # 🌐 Web + API — Phase 2
uv run pytest tests/llm_app          # 🧠 LLM-app testing — Phase 3
uv run pytest tests/windows_desktop  # 🖥️ Windows desktop — Phase 4 (Windows runners only)
uv run pytest tests/power_platform   # 🔷 Power Apps / Power Automate — Phase 5
uv run pytest tests/generated        # ✨ Output of the AI test-case generator
```

`conftest.py` and `fixtures/` hold shared fixtures (browser context, auth, test-data factories) used across
every sub-package, so a new suite only needs to add its own page objects / test files, not its own plumbing.

See the root [README's roadmap](../README.md#️-roadmap) for which folders are active right now.
