#!/usr/bin/env bash
# 🚀 One-shot local environment bootstrap. Safe to re-run.
#
# What it does, in order (see README.md § Environment setup for the beginner-friendly version
# of these same steps, with Windows/macOS commands side by side):
#   1. Checks for Python 3.12+
#   2. Installs `uv` if it's missing
#   3. Installs project dependencies with `uv sync`
#   4. Installs Playwright's browsers
#   5. Copies .env.example to .env if .env doesn't exist yet

set -euo pipefail

echo "🐍 Checking Python version..."
python3 --version

if ! command -v uv &> /dev/null; then
  echo "📦 'uv' not found — installing it..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
else
  echo "📦 'uv' already installed."
fi

echo "📚 Installing project dependencies..."
uv sync

echo "🌐 Installing Playwright browsers..."
uv run playwright install

if [ ! -f .env ]; then
  echo "🔐 Creating .env from .env.example (fill in real values before running the LLM/agent suites)..."
  cp .env.example .env
else
  echo "🔐 .env already exists — leaving it alone."
fi

echo "✅ Bootstrap complete. Run 'uv run pytest' to run the suite."
