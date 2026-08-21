# Changelog

All notable changes to Baton Fanout Skill are documented here.

## [Unreleased]

### Added

- Codex-first distribution surface with a dedicated collaboration-tool adapter and `agents/openai.yaml` metadata, so Codex users reach the runtime-specific primitives before portable guidance.
- Baton-approved Luna/max as the first candidate for stable, exact-path, mechanically verifiable code generation, with direct or exposed native lanes retained when Luna is unavailable, ineligible, or fails calibration.
- Independent-review routing floor of Sol/high plus a relative-strength rule: use a clearly stronger exposed lane than the working session when possible, or the same runtime-ceiling lane with fresh adversarial context.
- Dated GPT-5.6 model and reasoning-effort routing reference with current Sol, Terra, and Luna cost ratios, live-capability fallbacks, and escalation rules.
- Validation coverage that requires the routing reference, official pricing sources, and refresh metadata.
- Native per-spawn model and reasoning-effort routing, including the explicit-override versus full-history inheritance boundary.
- Luna/max routing for stable exact-target code generation and bounded low-judgment scouts whose expected judgment need is no greater than Terra/high.

### Removed

- The Codex CLI Luna compatibility bridge and its wrapper-specific timeout/WAL rules, superseded by native subagent model and effort overrides.

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
