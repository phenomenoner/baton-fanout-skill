from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "__pycache__", ".venv"}


def public_text_bundle() -> str:
    """Read every UTF-8 text-like public file, including dotfiles and extensionless files."""
    texts: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        data = path.read_bytes()
        if b"\x00" in data:
            continue
        try:
            texts.append(data.decode("utf-8"))
        except UnicodeDecodeError:
            continue
    return "\n".join(texts)


class PublicBundleTests(unittest.TestCase):
    def test_required_public_files_exist(self) -> None:
        for rel in (
            "README.md",
            "ABOUT.md",
            "SKILL.md",
            "LICENSE",
            "NOTICE.md",
            "CHANGELOG.md",
            "CONTRIBUTING.md",
            "SECURITY.md",
            "scripts/validate_skill.py",
            "scripts/run_checks.py",
            "tests/test_public_bundle.py",
            "references/dispatch-planning.md",
            "references/context-and-briefs.md",
            "references/execution-and-verification.md",
            "references/model-and-effort-routing.md",
            "references/smoke-tests.md",
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_model_routing_reference_is_dated_and_refreshable(self) -> None:
        routing = (ROOT / "references" / "model-and-effort-routing.md").read_text(
            encoding="utf-8"
        )
        for required in (
            "gpt-5.6-sol",
            "gpt-5.6-terra",
            "gpt-5.6-luna",
            "2026-08-01",
            "relative cost proxy",
            "https://developers.openai.com/api/docs/pricing",
            "https://developers.openai.com/api/docs/changelog",
        ):
            self.assertIn(required, routing)

    def test_no_machine_specific_home_paths(self) -> None:
        text = public_text_bundle()
        unix_home = "/" + "(?:home|Users)" + "/"
        wsl_users = "/mnt/" + "[A-Za-z]/" + "Users/"
        windows_users = "[A-Za-z]:" + r"\\Users\\"
        patterns = (
            rf"(?<![\w.-]){unix_home}[^/\s]+/",
            rf"(?<![\w.-]){wsl_users}[^/\s]+/",
            windows_users + r"[^\\\s]+\\",
        )
        for pattern in patterns:
            self.assertIsNone(re.search(pattern, text), pattern)

    def test_no_common_secret_shapes(self) -> None:
        text = public_text_bundle()
        patterns = (
            r"\bsk-[A-Za-z0-9_-]{20,}",
            r"\b(?:ghp|gho|github_pat)_[A-Za-z0-9_]{20,}",
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
            r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b",
            r"(?i)authorization:\s*bearer\s+[A-Za-z0-9._-]{16,}",
        )
        for pattern in patterns:
            self.assertIsNone(re.search(pattern, text), pattern)

    def test_upstream_attribution_is_consistent(self) -> None:
        notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("https://github.com/cablate/baton", notice)
        self.assertIn("77f12e600406065a6e62a22a66347355e278a9d7", notice)
        self.assertIn("Copyright (c) 2026 CabLate", notice)
        self.assertIn("Copyright (c) 2026 CabLate", license_text)

    def test_portable_install_preserves_license_and_notice(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        portable = readme.split("### Other agent systems", 1)[1].split("## Core decision", 1)[0]
        self.assertIn("LICENSE", portable)
        self.assertIn("NOTICE.md", portable)

    def test_readme_does_not_use_social_hashtag_block(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("## Tags", readme)
        self.assertNotRegex(readme, r"(?m)^#AIAgents\b")


if __name__ == "__main__":
    unittest.main()
