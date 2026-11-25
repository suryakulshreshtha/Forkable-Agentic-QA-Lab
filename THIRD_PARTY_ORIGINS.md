# 🔒 Third-party dependency origins

This repo follows a **non-Chinese dependency policy**: every third-party tool is checked for its *controlling
publisher* — not just its license — before it's added. A permissive license says nothing about who controls a
project's roadmap, telemetry, or update channel, so license alone isn't the bar here.

> ⚠️ **Scope note:** this is an engineering screening process, not a legal or export-control determination.
> "Non-Chinese" here means *the controlling company or foundation is not headquartered in or governed from
> mainland China*, checked by publisher research (GitHub org, PyPI/npm maintainer metadata, the project's own
> "About" page). If this repo is ever used inside an organization with a formal compliance requirement, have
> that requirement reviewed against this document before relying on it as a control.

## ✅ Screening method

1. **Identify the controlling entity** — the GitHub org, the PyPI/npm maintainer, the company's own "About" page.
2. **Prefer foundation-governed projects** (Apache Software Foundation, OpenJS Foundation, Python Software
   Foundation) over single-company projects when an equivalent exists.
3. **Check for phone-home behaviour** to a mainland-China domain (`*.aliyun.com`, `*.qq.com`,
   `*.bytedance.com`, `*.alibaba.com`, `*.modelscope.cn`) — grep the source, don't assume.
4. **Record it here** — every dependency's origin is logged below so no one has to re-research it.
5. **Enforce it in CI** — [`ci/origin_check.py`](./ci/origin_check.py) runs on every pull request and fails the
   build if a new dependency resolves to a denylisted publisher.

## 📋 Approved dependencies (verified)

| Dependency | Publisher | Country | License | Role in this repo |
|---|---|---|---|---|
| Python | Python Software Foundation | US | PSF | Language runtime |
| pytest | pytest-dev / community | — (OSS community) | MIT | Test runner |
| Playwright (Python) | Microsoft | US | Apache-2.0 | Browser automation |
| Playwright MCP | Microsoft | US | Apache-2.0 | Agentic browser control |
| pywinauto | Open community | — (OSS community, BSD-3) | BSD-3-Clause | Windows desktop automation |
| FlaUI | Open community | — (OSS community, .NET) | MIT | Windows desktop automation (alternative) |
| Power Apps Test Engine | Microsoft | US | MIT | Power Apps / Power Automate testing |
| DeepEval | Confident AI | US | Apache-2.0 | LLM output evaluation |
| Ragas | Exploding Gradients, Inc. | US | Apache-2.0 | RAG-specific LLM evaluation |
| Promptfoo | Promptfoo Inc. | US | MIT | Prompt regression & red-teaming |
| Allure Report | Qameta Software | US (with an Estonia entity) | Apache-2.0 | Test reporting |
| GitHub Actions | Microsoft/GitHub | US | — | CI/CD |
| pip-audit | Python Packaging Authority | US (OSS community) | Apache-2.0 | Vulnerability scanning |
| cyclonedx-python | CycloneDX / OWASP-adjacent | — (OSS community) | Apache-2.0 | SBOM generation |
| n8n | n8n GmbH | 🇩🇪 Germany (Berlin) | Sustainable Use License ("fair-code") — **not** OSI open-source | Agent orchestration (bug-reporting workflow) |
| Groq (GroqCloud API) | Groq, Inc. | US (Mountain View) | — (commercial API) | Fast LLM inference for the bug-reporting agent |
| Jira | Atlassian | Australia / US (dual-listed) | — (commercial) | Defect tracker |
| Gmail / Google Sheets | Google | US | — (commercial) | Notifications / execution-sheet updates |

## 🚫 Considered and rejected (Chinese-origin — do not add)

| Tool | What it does | Why it's out | Non-Chinese replacement used instead |
|---|---|---|---|
| HttpRunner | API/load testing framework | Chinese-origin (creator `debugtalk`); installer hosted on Alibaba Cloud OSS, support via WeChat | `httpx` + pytest / Playwright `APIRequestContext` |
| Midscene.js | AI-vision UI testing | Built and governed by ByteDance's Web Infra team | Playwright MCP + Claude/GPT-family reasoning |
| WeTest / PerfDog | Cloud device-farm & performance testing | Tencent product line | BrowserStack / Sauce Labs (US) if a device farm is ever needed |
| UI-TARS / UI-TARS-desktop | Vision-grounded GUI agent model | ByteDance Seed research team | Playwright MCP's own accessibility-tree approach |
| Qwen-family models, if used as a vision-grounding model | LLM backbone for a GUI agent | Alibaba | Any US-origin model (Claude, GPT, Groq-hosted open models) |

Add a row to the appropriate table above **before** adding any new dependency to `pyproject.toml`,
`package.json`, or an n8n workflow's node list.
