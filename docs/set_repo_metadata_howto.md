# 🏷️ How to set the repo's About, description & hashtags (topics)

This runs **`scripts/set_repo_metadata.sh`**, which sets the GitHub "About" box (description + homepage link)
and the repo's topics — GitHub's equivalent of hashtags, shown on the repo card and used in search.

You run this **yourself, from your own terminal**, after the repo exists on GitHub (it edits a repo that's
already there — it doesn't create one).

> ⚠️ **Windows note:** `set_repo_metadata.sh` is a Bash script. PowerShell and Command Prompt **cannot run
> `.sh` files directly** — you need **Git Bash** (installed automatically with [Git for Windows](https://git-scm.com/download/win))
> or **WSL**. Every command below that says "Git Bash" goes in that terminal, not plain PowerShell.

## ✅ Before you start — checklist

- [ ] The repo `suryakulshreshtha/Forkable-Agentic-QA-Lab` already exists on GitHub and has at least one push.
- [ ] You have **admin/write access** to that repo (you're the owner, so this should already be true).
- [ ] (Windows only) Git Bash is installed.

## 🪜 Steps

### Step 1 — Install the GitHub CLI (`gh`), if you don't have it

| Platform | Command |
|---|---|
| 🪟 **Windows** (PowerShell, as Administrator) | `winget install --id GitHub.cli` |
| 🍎 **macOS** (Terminal, with [Homebrew](https://brew.sh/)) | `brew install gh` |

Check it installed, on either platform:
```bash
gh --version
```

### Step 2 — Log in to GitHub as `suryakulshreshtha`

Same command on both platforms — run it in PowerShell/Terminal (login itself doesn't need Git Bash):
```bash
gh auth login
```
It will ask:
1. `GitHub.com` or `GitHub Enterprise Server` → choose **GitHub.com**
2. Preferred protocol → **HTTPS** is the simplest choice
3. Authenticate with a browser or a token → choose **Login with a web browser**, press Enter, and it gives you
   a one-time code — paste it into the browser tab that opens and approve it.

### Step 3 — Confirm you're logged in as the right account

```bash
gh auth status
```
Look for `Logged in to github.com account suryakulshreshtha` in the output. If it shows a different account,
run `gh auth logout` first, then repeat Step 2.

### Step 4 — Open a terminal in the repo folder

| Platform | Command |
|---|---|
| 🪟 **Windows** (open **Git Bash**, not PowerShell, from here on) | `cd /c/path/to/Forkable-Agentic-QA-Lab` |
| 🍎 **macOS** (Terminal) | `cd ~/path/to/Forkable-Agentic-QA-Lab` |

(Replace `/c/path/to/...` or `~/path/to/...` with wherever you cloned the repo.)

### Step 5 — Make the script executable (first time only)

| Platform | Command |
|---|---|
| 🪟 **Windows** (Git Bash) | `chmod +x scripts/set_repo_metadata.sh` |
| 🍎 **macOS** (Terminal) | `chmod +x scripts/set_repo_metadata.sh` |

### Step 6 — Run it

Same command, both platforms (Windows: in **Git Bash**):
```bash
./scripts/set_repo_metadata.sh
```

It will print each step as it runs, then show the repo's live description, homepage, and topic list at the
end so you can confirm it worked.

### Step 7 — Verify on GitHub

Open `https://github.com/suryakulshreshtha/Forkable-Agentic-QA-Lab` in a browser — the About box (top-right
of the repo page) should now show the description and the topic tags (hashtags) underneath it.

## 🛠️ If something goes wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| `gh: command not found` | `gh` isn't installed, or isn't on PATH yet | Re-run Step 1, then open a **new** terminal window |
| `HTTP 403` / `HTTP 404` on the repo | Not logged in as an account with write access, or the repo name doesn't match yet | Re-check Step 3's output; re-check the repo exists at that exact URL |
| `zsh: permission denied` / `bash: permission denied` | Script isn't executable yet | Re-run Step 5 |
| Topics don't show up on the page right away | Browser cache | Hard-refresh (`Ctrl+Shift+R` / `Cmd+Shift+R`) |

📚 Official docs: [GitHub CLI manual — `gh repo edit`](https://cli.github.com/manual/gh_repo_edit) ·
[GitHub CLI manual — `gh auth login`](https://cli.github.com/manual/gh_auth_login) ·
[About topics — GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
