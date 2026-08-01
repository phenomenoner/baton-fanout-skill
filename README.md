# Baton Fanout Skill

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Upstream Baton](https://img.shields.io/badge/upstream-cablate%2Fbaton-6f42c1)](https://github.com/cablate/baton)
[![Skill](https://img.shields.io/badge/agent-skill-ready-2f855a)](SKILL.md)

A portable agent skill for deciding **when fan-out earns its context, ownership, and verification cost**.

> This is an independent, MIT-licensed derivative of [CabLate's Baton](https://github.com/cablate/baton), not an official CabLate release. Upstream attribution and the pinned source revision are recorded in [NOTICE.md](NOTICE.md).

## The 30-second story

Spawning more agents is easy. Getting a trustworthy result can be harder: workers reread the same sources, collide on shared files, repeat expensive checks, and hand the parent a larger synthesis problem.

Baton Fanout Skill adds a small decision gate before delegation:

- **Dispatch less.** Keep small or tightly coupled work with the main agent.
- **Group by context.** Split by source, artifact, dependency, and verification surface—not by bullet count.
- **Own every write.** Give each writable artifact one owner and serialize shared contracts.
- **Route intentionally.** Treat runtime defaults as fallbacks; select per-task model and reasoning effort when the platform supports it.
- **Stop blind retries.** Repair unclear briefs first and escalate by failure class instead of relaunching identical workers.
- **Verify centrally.** Worker self-reports are inputs, not completion evidence.

## What is included

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Portable dispatch and fan-out governance skill |
| [`references/dispatch-planning.md`](references/dispatch-planning.md) | Primitive selection, context grouping, ownership map |
| [`references/context-and-briefs.md`](references/context-and-briefs.md) | Compact context-pack and worker-brief templates |
| [`references/execution-and-verification.md`](references/execution-and-verification.md) | Monitoring, escalation, synthesis, and evidence rules |
| [`references/model-and-effort-routing.md`](references/model-and-effort-routing.md) | Dated GPT-5.6 cost snapshot and quick model/effort routing matrix |
| [`references/smoke-tests.md`](references/smoke-tests.md) | Three decision smokes for fresh-session validation |
| [`NOTICE.md`](NOTICE.md) | Upstream source, pinned revision, and MIT attribution |

## Quick start

### Hermes Agent

```bash
git clone https://github.com/phenomenoner/baton-fanout-skill.git \
  ~/.hermes/skills/autonomous-ai-agents/baton-fanout-skill
```

Start a fresh Hermes session, then load `baton-fanout-skill` before meaningful delegation or multi-surface fan-out. Run the three prompts in [`references/smoke-tests.md`](references/smoke-tests.md) after installation.

### Other agent systems

Keep `SKILL.md`, `references/`, `LICENSE`, and `NOTICE.md` together when copying this bundle into another system's skill or instruction directory. Map generic primitives—main-agent work, one scout, bounded parallel workers, batches, worktrees, and centralized verification—to capabilities that actually exist in that runtime.

This repository contains guidance, templates, and validation checks. It does not install an orchestrator or grant agents new permissions.

## Core decision

Before fan-out, answer five questions:

1. **Outcome:** What exact deliverable and acceptance conditions are required?
2. **Direct alternative:** Would the main agent finish faster, safer, or cheaper?
3. **Independence:** Can workers progress without rereading the same large context or waiting on each other?
4. **Ownership:** Does every write—including secondary writes—have one owner?
5. **Closure:** Who synthesizes, resolves conflicts, verifies, and reports gaps?

If any answer is unclear, do not fan out yet. Clarify, use one bounded scout, or converge the shared contract first.

## Design principles

- Normal parallelism should be small and bounded.
- A large task is not automatically a parallel task.
- The same full-context brief should not be sent to multiple workers unless the purpose is explicit A/B testing, independent verification, or adversarial review.
- Fast-changing model prices and runtime limits belong in live configuration or a dated, source-linked reference—not in the core skill instructions.
- Final judgment and side-effect decisions remain with the main agent.

## Validate the bundle

With [`uv`](https://docs.astral.sh/uv/), run all checks in an ephemeral dependency environment without modifying the system Python:

```bash
uv run --with 'PyYAML>=6,<7' python scripts/run_checks.py
```

Without `uv`, create an isolated virtual environment and install `PyYAML>=6,<7` there before running `python scripts/run_checks.py`.

## Upstream and license

Baton Fanout Skill adapts ideas from:

- **Baton** by CabLate
- Source: https://github.com/cablate/baton
- Upstream release: `v0.1.1`
- Pinned upstream commit: `77f12e600406065a6e62a22a66347355e278a9d7`
- Upstream license: MIT

See [NOTICE.md](NOTICE.md) for the retained upstream copyright and permission notice.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
