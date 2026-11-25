# 🐞 Bug-reporting agent (n8n + Groq)

**Status:** 🚧 Planned for Phase 3 (see the root [README's roadmap](../../README.md#️-roadmap)) — this folder
currently holds the setup contract, not a built workflow yet.

## What it will do

Takes a plain-English failure description (e.g. *"Application crashes when clicking the Login button"*) and:

1. 🔎 Extracts the key defect details (summary, steps to reproduce, expected vs. actual result, severity) using
   [Groq](https://console.groq.com/docs) for fast LLM inference.
2. 📌 Creates a complete issue in Jira with those fields filled in, via n8n's Jira node.
3. 📧 Sends an email notification to the relevant team.
4. 📊 Updates a tracking/execution sheet with the bug ID and status.
5. 🔁 Returns the bug ID to whatever triggered it (a CI run, a manual webhook call).

## How it will be triggered

A GitHub Actions job (`.github/workflows/`) calls this workflow's n8n webhook URL on pytest failure, passing
the failure's test name and traceback as the "plain-English description" input.

## Files that will live here

- `workflow.json` — the exported n8n workflow (import via n8n's UI: **Workflows → Import from File**).
- `.env.example` — the credentials this workflow needs (see below).

## 🔧 Setup (once the workflow is built)

| Platform | Command to run n8n locally via Docker |
|---|---|
| 🪟 **Windows** (PowerShell) | `docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n` |
| 🍎 **macOS** (Terminal) | `docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n` |

Then open `http://localhost:5678`, import `workflow.json`, and fill in the credentials it asks for (Jira API
token, Gmail OAuth, Google Sheets, Groq API key — see `.env.example` in this folder).

📚 Official docs: [n8n documentation](https://docs.n8n.io/) · [Groq API reference](https://console.groq.com/docs)
