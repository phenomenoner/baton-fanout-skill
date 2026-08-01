#!/usr/bin/env python3
"""Run all local release checks with a non-zero minimum test count."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIN_TESTS = 6


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    run([sys.executable, "scripts/validate_skill.py"])

    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    count = suite.countTestCases()
    if count < MIN_TESTS:
        raise SystemExit(f"expected at least {MIN_TESTS} tests, discovered {count}")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1

    if (ROOT / ".git").exists():
        run(["git", "diff", "--check"])
        run(["git", "diff", "--cached", "--check"])

    print(f"RELEASE_CHECKS_OK tests={count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
