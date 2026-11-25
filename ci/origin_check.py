#!/usr/bin/env python3
"""
🔒 Dependency-origin CI gate.

Reads this repo's declared Python dependencies (from pyproject.toml), looks each one up on
PyPI, and fails (non-zero exit) if any package name matches the denylist below — the
Chinese-origin tools recorded as "rejected" in THIRD_PARTY_ORIGINS.md.

This is a *name-based* denylist, intentionally simple: it catches the exact tools this repo
already decided to avoid (see THIRD_PARTY_ORIGINS.md for the reasoning on each). It is not a
general-purpose "detect any Chinese-controlled package" scanner — that would require checking
live PyPI maintainer metadata for every dependency, which this script does as a best-effort
second pass (see `check_pypi_maintainer_hint`), but that check is advisory only and should not
be the sole gate for a compliance-grade requirement.

Usage:
    python ci/origin_check.py                  # checks this repo's own pyproject.toml
    python ci/origin_check.py path/to/other.toml
"""

from __future__ import annotations

import json
import pathlib
import sys
import tomllib
import urllib.request

# Package names this repo has explicitly decided not to depend on.
# Keep this in sync with the "Considered and rejected" table in THIRD_PARTY_ORIGINS.md.
DENYLIST: dict[str, str] = {
    "httprunner": "Chinese-origin (debugtalk / Aliyun-hosted installer) — see THIRD_PARTY_ORIGINS.md",
    "midscene": "ByteDance Web Infra team — see THIRD_PARTY_ORIGINS.md",
    "ui-tars": "ByteDance Seed research team — see THIRD_PARTY_ORIGINS.md",
}

# Domain fragments that suggest a mainland-China phone-home endpoint, for the advisory scan.
SUSPICIOUS_DOMAIN_FRAGMENTS = (
    "aliyun.com",
    "qq.com",
    "bytedance.com",
    "alibaba.com",
    "modelscope.cn",
)


def load_declared_dependencies(pyproject_path: pathlib.Path) -> list[str]:
    """Return every dependency name declared under [project.dependencies] and
    [project.optional-dependencies], lower-cased and stripped of version specifiers."""
    data = tomllib.loads(pyproject_path.read_text())
    project = data.get("project", {})
    raw: list[str] = list(project.get("dependencies", []))
    for group in project.get("optional-dependencies", {}).values():
        raw.extend(group)

    names = []
    for spec in raw:
        # Strip version pins/markers: "deepeval>=1.0" -> "deepeval", "pywinauto>=0.6.8; sys_platform==...": "pywinauto"
        name = spec.split(";")[0]
        for sep in ("==", ">=", "<=", "~=", ">", "<", "[", " "):
            name = name.split(sep)[0]
        names.append(name.strip().lower())
    return sorted(set(names))


def check_denylist(names: list[str]) -> list[str]:
    """Return a list of human-readable failure messages for any denylisted package found."""
    failures = []
    for name in names:
        if name in DENYLIST:
            failures.append(f"❌ '{name}' is denylisted: {DENYLIST[name]}")
    return failures


def check_pypi_maintainer_hint(name: str, timeout: float = 5.0) -> str | None:
    """Best-effort, advisory-only: fetch the package's PyPI JSON metadata and flag it if the
    project_urls/home_page contain a suspicious domain fragment. Never raises — a network
    failure here should not break CI for an unrelated reason; it just skips the advisory check.
    """
    try:
        with urllib.request.urlopen(f"https://pypi.org/pypi/{name}/json", timeout=timeout) as resp:
            data = json.loads(resp.read())
    except Exception:
        return None

    info = data.get("info", {})
    urls = list(info.get("project_urls", {}).values()) + [info.get("home_page") or ""]
    for url in urls:
        for fragment in SUSPICIOUS_DOMAIN_FRAGMENTS:
            if fragment in (url or ""):
                return f"⚠️  '{name}' lists a project URL containing '{fragment}' ({url}) — review manually."
    return None


def main() -> int:
    pyproject_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("pyproject.toml")
    if not pyproject_path.exists():
        print(f"❌ Could not find {pyproject_path}")
        return 2

    names = load_declared_dependencies(pyproject_path)
    print(f"🔍 Checking {len(names)} declared dependencies against the non-Chinese origin policy...\n")

    hard_failures = check_denylist(names)
    advisories = [m for n in names if (m := check_pypi_maintainer_hint(n))]

    for msg in advisories:
        print(msg)
    for msg in hard_failures:
        print(msg)

    if hard_failures:
        print(f"\n🚫 {len(hard_failures)} denylisted dependency(ies) found — failing the build.")
        return 1

    print("\n✅ No denylisted dependencies found.")
    if advisories:
        print(f"ℹ️  {len(advisories)} advisory note(s) above — not build-failing, but worth a human look.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
