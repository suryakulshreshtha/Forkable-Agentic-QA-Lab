# Publishing this repository to GitHub

This takes the folder on your computer to a repository on GitHub, with an About box, topics and badges —
written in the same shape as `docs/publishing-to-github.md` in your other Forkable\* repos.

> **Nothing here runs by itself.** Every step is a command or a click that you perform.
> Throughout, the account name is `suryakulshreshtha`. The credit name used below is **Anti Errorist** —
> that's what your other repos' `LICENSE` and git config use, so it's used here for consistency. Say the word
> if this one should be different, and I'll update `LICENSE`, this doc and the README's credit line.

> **Status of this guide.** The repo's local scaffold (33 files) was built and `git add`-ed in a sandbox —
> nothing has been committed, pushed, or created on GitHub yet. The `gh` commands below were checked against
> GitHub CLI's own documentation (links at the end), not run against a live repo.

## 0. Before you publish: a checklist

| Check | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| The origin-policy gate passes | `python3 ci/origin_check.py` | `python ci\origin_check.py` |
| No secrets: `.env` is ignored, only `.env.example` is tracked | `git check-ignore -v .env` (after step 2) | `git check-ignore -v .env` |
| No generated files: reports, SBOMs, caches | `git status --short` after step 2 shows none of them | the same |
| Your name, not a placeholder, in `LICENSE` | `grep -n Copyright LICENSE` | `Select-String Copyright LICENSE` |

## 1. Install git, and tell it who you are

```text
git config --global user.name
git config --global user.email
```

If either prints nothing, set them:

```text
git config --global user.name  "Anti Errorist"
git config --global user.email "YOUR-CHOSEN-EMAIL"
```

GitHub offers a private "noreply" address (**Settings → Emails**) if you don't want your real one shown.

## 2. Make the first commit

From the repository folder (same on both systems):

```text
git add .
git status
```

You should see source and config files. You should **not** see `.env`, `.venv/`, `__pycache__/`, `ci/sbom/*.json`
or anything under `reports/`; `.gitignore` excludes them. If you do, stop and fix `.gitignore` first.

```text
git commit -m "Scaffold the Forkable Agentic QA Lab"
```

## 3. Create the repository on GitHub

**A. In the browser.** Sign in, **New repository**, name it `Forkable-Agentic-QA-Lab`, choose Public or
Private, and **do not** tick "Add a README", ".gitignore" or "license" (the folder already has them).

**B. With the GitHub CLI** (after `gh auth login`):

```text
gh repo create Forkable-Agentic-QA-Lab --public --source=. --remote=origin --description "🤖 AI-powered, Python + Playwright QA automation showcase — Web, API, Desktop, Power Platform & LLM-app testing, with an AI-agent layer on top."
```

Use `--private` to keep it to yourself. This creates the repo and adds the remote, but doesn't push unless
you add `--push`.

## 4. Connect and push

After route A:

```text
git remote add origin https://github.com/suryakulshreshtha/Forkable-Agentic-QA-Lab.git
git push -u origin main
```

After route B, only `git push -u origin main` is needed. **This is the moment your work becomes visible**
(if the repo is public).

## 5. The About box, topics and bio — the automated way

`scripts/set_repo_metadata.sh` does steps 5–7 below in one go, once `gh auth login` is done — see
[`docs/set_repo_metadata_howto.md`](set_repo_metadata_howto.md) for the exact terminal steps.

## 6. The About box — by hand, if you'd rather

**Description**

```text
🤖 AI-powered, Python + Playwright QA automation showcase — Web, API, Desktop, Power Platform & LLM-app testing, with an AI-agent layer on top.
```

```text
gh repo edit --description "🤖 AI-powered, Python + Playwright QA automation showcase — Web, API, Desktop, Power Platform & LLM-app testing, with an AI-agent layer on top."
```

## 7. Topics (hashtags)

Lowercase letters, numbers and hyphens only; up to 20 per repo:

```text
qa-automation test-automation playwright playwright-python python pytest ai-testing llm-testing
prompt-engineering power-platform power-apps mcp model-context-protocol n8n ai-agents qa-engineering
test-case-generation allure-report github-actions showcase
```

```text
gh repo edit --add-topic qa-automation --add-topic test-automation --add-topic playwright --add-topic playwright-python --add-topic python --add-topic pytest --add-topic ai-testing --add-topic llm-testing --add-topic prompt-engineering --add-topic power-platform --add-topic power-apps --add-topic mcp --add-topic model-context-protocol --add-topic n8n --add-topic ai-agents --add-topic qa-engineering --add-topic test-case-generation --add-topic allure-report --add-topic github-actions --add-topic showcase
```

For a social post (no character rules, just text):

```text
#AgenticQA #Playwright #Python #AITesting #TestAutomation #SDET #MCP #n8n #QAEngineering
```

## 8. Short bio text

```text
Test automation: Python, Playwright, pytest, CI/CD, and an AI-agent layer on top (LLM test-case generation, MCP, n8n). Forkable, public-by-design QA showcase. Credit: Anti Errorist.
```

## 9. Badges

Already in the README:

```text
[![CI](https://github.com/suryakulshreshtha/Forkable-Agentic-QA-Lab/actions/workflows/origin_and_sbom_check.yml/badge.svg)](https://github.com/suryakulshreshtha/Forkable-Agentic-QA-Lab/actions/workflows/origin_and_sbom_check.yml)
[![License: MIT](https://img.shields.io/github/license/suryakulshreshtha/Forkable-Agentic-QA-Lab)](LICENSE)
![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)
![Playwright](https://img.shields.io/badge/tested%20with-Playwright-45ba4b)
```

The CI badge stays grey until the workflow has run once.

## 10. The repo card (social preview + README banner)

A card was rendered for this repo using your own `~/Desktop/SKgitIO/tools/card-kit` pipeline and is already
committed into this scaffold at `docs/assets/forkable-card.png`, with the matching `<!-- forkable-card:start -->`
banner at the top of the README — the same markers `apply_cards.py` looks for, so once this repo is pushed and
cloned into `~/Desktop/GitHubPushes/Forkable-Agentic-QA-Lab`, re-running `apply_cards.py` will recognise and
manage it like your other repos (an entry for it is already in `apply_cards.py`'s `REPOS` dict). The same PNG
is also saved to `~/Desktop/SKgitIO/cards/Forkable-Agentic-QA-Lab.png`, and the entry is in
`~/Desktop/SKgitIO/tools/card-kit/cards.json` (index matches the other 13 cards already there).

To use it as the GitHub **social preview** too: repo **Settings → Social preview → Edit → Upload** →
`docs/assets/forkable-card.png` (1280×640, already the ideal size).

## 11. After publishing

1. Open the **Actions** tab and confirm the first run of `origin_and_sbom_check.yml` starts.
2. Enable **Issues** if you want forks/contributors to report things (`gh repo edit --enable-issues`).
3. `suryakulshreshtha/.github` already supplies `CODE_OF_CONDUCT.md`, `SECURITY.md` and `SUPPORT.md` as
   repo-wide defaults — no need to duplicate them here unless you want repo-specific versions.

## 12. If you pushed something you shouldn't have

Revoke or rotate the secret at the provider first, then clean the history (GitHub's docs: "Removing sensitive
data from a repository"). Rotation is the step that actually protects you.

## Credit

Created by **Anti Errorist**. MIT-licensed: use it, teach with it, adapt it, keep the copyright notice.

## References

* Topics: <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics>
* `gh repo create`: <https://cli.github.com/manual/gh_repo_create>
* `gh repo edit`: <https://cli.github.com/manual/gh_repo_edit>
* Git: <https://git-scm.com/doc>
