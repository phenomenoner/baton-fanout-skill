## Summary

_Describe the change._

## Why this improves dispatch or fan-out decisions

_Explain the decision-quality improvement._

## Decision cases affected

- [ ] Direct-work brake
- [ ] Context-affinity grouping
- [ ] Ownership / write boundaries
- [ ] Model or effort routing guidance
- [ ] Retry / stop conditions
- [ ] Verification / synthesis

## Validation

- [ ] `uv run --with 'PyYAML>=6,<7' python scripts/run_checks.py`
- [ ] `git diff --check`
- [ ] `git diff --cached --check`
- [ ] Fresh-session decision smoke added or updated when routing language changed

## Public and license hygiene

- [ ] No private identities, paths, logs, data, or credentials
- [ ] Upstream attribution remains intact
