# 🤝 Contributing

Thanks for considering a contribution — this repo is being built in public, so issues and PRs are genuinely
welcome, not just a formality.

## 🧰 Before you start

1. Read [`README.md`](./README.md) for the architecture and the [Roadmap](./README.md#️-roadmap) so your
   change lands in the right phase.
2. Check [`THIRD_PARTY_ORIGINS.md`](./THIRD_PARTY_ORIGINS.md) **before** adding any new dependency — PRs that
   add a dependency without an origin entry will be asked to add one.
3. Run the local setup in the [Environment setup](./README.md#-environment-setup-beginner-friendly) section.

## ✅ Pull request checklist

- [ ] Tests pass locally: `uv run pytest`
- [ ] New dependencies are logged in `THIRD_PARTY_ORIGINS.md`
- [ ] `ci/origin_check.py` passes: `uv run python ci/origin_check.py`
- [ ] Commit messages are clear and in the imperative mood ("Add...", "Fix...", not "Added...")

## 🐛 Reporting a bug

Open an issue with: what you ran, what you expected, what happened instead, and your OS (Windows/macOS/Linux)
— several of this repo's suites behave differently per OS by design (see the desktop-testing note in the
README).

## 💬 Questions

Open a [Discussion](../../discussions) or an issue tagged `question`.
