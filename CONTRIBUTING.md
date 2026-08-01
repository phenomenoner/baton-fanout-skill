# Contributing

Contributions that sharpen dispatch boundaries, context economy, ownership, verification, or portable runtime mapping are welcome.

## Before opening a pull request

1. Keep the skill runtime-agnostic unless a platform-specific note is clearly isolated.
2. Do not hard-code fast-changing model prices or private deployment paths.
3. Add or update a positive/negative decision smoke when changing routing language.
4. Preserve upstream attribution in `LICENSE` and `NOTICE.md`.
5. Run the complete release gate without modifying the system Python:

```bash
uv run --with 'PyYAML>=6,<7' python scripts/run_checks.py
git diff --check
git diff --cached --check
```

## Public bundle hygiene

Do not include credentials, private identities, local databases, raw logs, machine-specific absolute paths, private project names, or copied conversation transcripts.

## Commit style

Use concise conventional commits, for example:

- `docs: clarify context-affinity grouping`
- `feat: add fan-out routing smoke`
- `fix: preserve upstream attribution in bundle validator`
