# 🤔 Why this tool, per pillar

Short, honest rationale for each primary tool choice — the kind of write-up a reviewer can click into instead
of taking the choice on faith.

## 🌐 Web & API — Playwright (Python) + pytest

Playwright is cross-browser (Chromium, Firefox, WebKit) from one API, has first-class Python support, and its
`APIRequestContext` covers API testing without a second library. pytest is the de facto Python test runner —
fixtures and parametrization do most of the heavy lifting the Page Object Model needs.

## 🧠 LLM-app testing — Playwright MCP + DeepEval / Ragas / Promptfoo

The UI layer and the "is the output actually correct" layer are two different problems. Playwright MCP
exercises the chat UI like a user would; DeepEval/Ragas/Promptfoo score what the model said, with
deterministic assertions first and LLM-as-judge metrics as a clearly-labeled second layer (LLM-judge scoring
has known run-to-run variance — see `docs/ai_qa_philosophy.md`).

## 🖥️ Windows desktop — pywinauto

Pure Python, no .NET toolchain required, actively used since 2015, and it speaks both the legacy Win32 API and
modern UI Automation — covering more real-world Windows apps than either backend alone.

## 🔷 Power Platform — Power Apps Test Engine

Microsoft's own tool, built on Playwright, specifically because canvas apps' virtualized runtime breaks
hand-rolled selectors. Using the vendor's sanctioned tool here is the engineering-judgment call, not a
shortcut.

## 🔗 Agent orchestration — n8n (for the bug-reporting agent only)

Rebuilding Jira/Gmail/Sheets glue code in Python would be more code for no real benefit. n8n is good at
exactly this kind of reactive, multi-system orchestration, and showing both a code-first suite and a low-code
agent in one repo demonstrates range — not a dependency on it for anything in the critical test-execution
path.

## ⚡ Groq, for inference in the bug-reporting agent

Fast, cost-efficient inference for a workflow that needs to extract structured fields (summary, steps to
reproduce, severity) from a short plain-English description — a latency-sensitive, not accuracy-sensitive,
job, which is exactly Groq's strength.
