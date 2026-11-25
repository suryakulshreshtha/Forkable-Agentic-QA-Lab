#!/usr/bin/env bash
# 🏷️ Sets this repo's GitHub "About" section (description + homepage) and topics (hashtags).
#
# Run this ONCE, after the repo has been created and pushed, and after you've run
# `gh auth login` (or have GITHUB_TOKEN set) with write access to the repo.
#
# Usage:
#   ./scripts/set_repo_metadata.sh
#   ./scripts/set_repo_metadata.sh suryakulshreshtha/Forkable-Agentic-QA-Lab   # override the repo slug

set -euo pipefail

REPO="${1:-suryakulshreshtha/Forkable-Agentic-QA-Lab}"

DESCRIPTION="🤖 AI-powered, Python + Playwright QA automation showcase — Web, API, Desktop, Power Platform & LLM-app testing, with an AI-agent layer on top."
HOMEPAGE="https://github.com/${REPO}"

# GitHub topics act as this repo's "hashtags" — they show on the repo card and are searchable.
# Keep this list to GitHub's rules: lowercase, hyphens only, no spaces, 20 topics max.
TOPICS=(
  "qa-automation"
  "test-automation"
  "playwright"
  "playwright-python"
  "python"
  "pytest"
  "ai-testing"
  "llm-testing"
  "prompt-engineering"
  "power-platform"
  "power-apps"
  "mcp"
  "model-context-protocol"
  "n8n"
  "ai-agents"
  "qa-engineering"
  "test-case-generation"
  "allure-report"
  "github-actions"
  "showcase"
)

echo "🔧 Setting description and homepage on ${REPO}..."
gh repo edit "${REPO}" \
  --description "${DESCRIPTION}" \
  --homepage "${HOMEPAGE}"

echo "🏷️  Setting topics (hashtags) on ${REPO}..."
# gh repo edit --add-topic can be repeated; build the flag list dynamically.
topic_flags=()
for t in "${TOPICS[@]}"; do
  topic_flags+=(--add-topic "${t}")
done
gh repo edit "${REPO}" "${topic_flags[@]}"

echo "✅ Done. Current repo metadata:"
gh repo view "${REPO}" --json description,homepageUrl,repositoryTopics \
  --jq '{description, homepage: .homepageUrl, topics: [.repositoryTopics[].name]}'
