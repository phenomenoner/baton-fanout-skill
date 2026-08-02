# Changelog

All notable changes to Baton Fanout Skill are documented here.

## [Unreleased]

### Added

- Dated GPT-5.6 model and reasoning-effort routing reference with current Sol, Terra, and Luna cost ratios, live-capability fallbacks, and escalation rules.
- Validation coverage that requires the routing reference, official pricing sources, and refresh metadata.
- Optional, runtime-specific Codex CLI compatibility-bridge guidance for a verified Luna implementation lane when native delegation cannot expose it; the bridge stays read-only, proposal-only, and under main-agent integration and verification.
- Adaptive compatibility-bridge budget and observable-progress guidance: host-rendered task WALs remain outside the read-only workspace and evidence-only, while stalled work, scope drift, or exhausted budgets trigger intervention.
- Expected-budget versus hard-timeout guidance for compatibility bridges, including latest-WAL-progress intervention, parseable checkpoint emission before late polish, completion buffers, timeout evidence retention, and narrower retry boundaries.

## [1.0.0] - 2026-08-01

### Added

- Portable `baton-fanout-skill` agent skill.
- Context-affinity grouping and compact ref-backed context packs.
- Explicit per-task routing guidance without hard-coded model prices.
- Failure-class escalation and no-blind-retry rules.
- Ownership, centralized verification, and synthesis templates.
- Three fresh-session decision smokes plus an optional routing smoke.
- Public validation script, CI workflow, attribution notice, and MIT license.

### Attribution

Derived from CabLate's MIT-licensed Baton `v0.1.1`, pinned at commit `77f12e600406065a6e62a22a66347355e278a9d7`.
