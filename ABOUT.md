# About Baton Fanout Skill

## Purpose

Baton Fanout Skill is a portable governance layer for AI-agent delegation. It helps an agent choose the smallest reliable execution structure before spawning workers, then controls shared context, artifact ownership, retries, verification, and synthesis.

## Who it is for

- Agent operators who already have subagents but want better dispatch judgment.
- Teams seeing repeated context reads, overlapping writes, retry cascades, or expensive synthesis.
- Skill-compatible runtimes that support one or more of: leaf workers, parallel tasks, batches, isolated worktrees, model overrides, or centralized verification.

## What this adaptation adds

Relative to the upstream Baton concepts, this bundle emphasizes:

1. **Context-affinity grouping** before worker assignment.
2. **Compact ref-backed context packs** instead of transcript cloning.
3. **Explicit per-task model/effort routing** when the runtime supports it, without hard-coding fast-changing model prices.
4. **Failure-class escalation**: repair the brief before increasing capability.
5. **No blind duplicate retries** after repeated same-cause failure.
6. **Public, portable templates and validation smokes** for skill-based runtimes.

## What it is not

- Not a swarm runtime or scheduler.
- Not a benchmark claim that more agents become faster.
- Not an official CabLate product or release.
- Not a replacement for runtime security, permission controls, repository contracts, or human approval.

## Relationship to Baton

This is an independent derivative of [CabLate's Baton](https://github.com/cablate/baton), based on the MIT-licensed `v0.1.1` source pinned at commit `77f12e600406065a6e62a22a66347355e278a9d7`.

The upstream project introduced the core idea: **dispatch less, deliver more** by judging whether delegation earns its coordination cost. This repository packages a focused fan-out/context-economy adaptation for portable agent-skill use.

See [NOTICE.md](NOTICE.md) for proper attribution and the retained upstream MIT notice.
