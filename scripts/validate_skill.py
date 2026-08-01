#!/usr/bin/env python3
"""Validate the portable Baton Fanout skill bundle."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    ROOT / "README.md",
    ROOT / "ABOUT.md",
    ROOT / "LICENSE",
    ROOT / "NOTICE.md",
    ROOT / "scripts" / "run_checks.py",
    ROOT / "tests" / "test_public_bundle.py",
    ROOT / "references" / "dispatch-planning.md",
    ROOT / "references" / "context-and-briefs.md",
    ROOT / "references" / "execution-and-verification.md",
    ROOT / "references" / "smoke-tests.md",
]


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise SystemExit("SKILL.md must start with YAML frontmatter at byte 0")
    match = re.search(r"\n---\s*\n", content[4:])
    if match is None:
        raise SystemExit("SKILL.md frontmatter closing delimiter not found")
    end = match.start() + 4
    frontmatter = yaml.safe_load(content[4:end])
    body = content[match.end() + 4 :].strip()

    if not isinstance(frontmatter, dict):
        raise SystemExit("frontmatter must parse as a YAML mapping")
    if frontmatter.get("name") != "baton-fanout-skill":
        raise SystemExit("frontmatter name must be baton-fanout-skill")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.startswith("Use before"):
        raise SystemExit("description must be a routing trigger beginning with 'Use before'")
    if len(description) > 1024:
        raise SystemExit("description exceeds 1024 characters")
    if frontmatter.get("license") != "MIT":
        raise SystemExit("frontmatter license must be MIT")
    if not body:
        raise SystemExit("SKILL.md body must not be empty")
    if len(content) > 100_000:
        raise SystemExit("SKILL.md exceeds 100,000 characters")

    notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
    for required in (
        "https://github.com/cablate/baton",
        "77f12e600406065a6e62a22a66347355e278a9d7",
        "Copyright (c) 2026 CabLate",
        "MIT License",
    ):
        if required not in notice:
            raise SystemExit(f"NOTICE.md missing attribution: {required}")

    print("VALIDATION_OK")
    print(f"skill_chars={len(content)} required_files={len(REQUIRED)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
