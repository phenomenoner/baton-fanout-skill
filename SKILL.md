---
name: baton-fanout-skill
description: Use before meaningful subagent delegation, parallel fan-out, batch execution, worktrees, migrations, multi-surface changes, or broad audits. Choose the smallest reliable execution structure; prevent duplicated context, overlapping writes, blind retries, and unsynthesized results.
version: 1.0.0
author: CabLate upstream; fan-out adaptation by phenomenoner
license: MIT
metadata:
  hermes:
    tags: [delegation, fanout, orchestration, subagents, context-economy, ownership, verification]
    related_skills: []
    homepage: https://github.com/phenomenoner/baton-fanout-skill
---

# Baton Fanout Governance

> **Dispatch less. Deliver more.**
>
> Independent fan-out/context-economy adaptation of [CabLate's Baton v0.1.1](https://github.com/cablate/baton), pinned at `77f12e600406065a6e62a22a66347355e278a9d7` under the MIT License. See `NOTICE.md`.

## Overview

Apply this skill before spawning subagents, opening worktrees, scaling a workflow, or splitting a task across multiple sources or artifacts. It decides whether delegation earns its coordination cost and, if so, chooses the smallest reliable execution shape.

It is advisory. The current user request, live runtime/tool schema, security and approval boundaries, and repository-local contracts take precedence. This skill does not change models, permissions, files, or schedules by itself.

## When to use

Use this skill for:

- meaningful subagent delegation or parallel fan-out;
- broad research split across independent source classes;
- multi-file or multi-surface implementation;
- homogeneous audits, migrations, or batch work;
- worktree/branch proposals;
- independent review or adversarial verification;
- repeated worker failures, context duplication, or synthesis backlog.

Do not load it for a single obvious tool call, a tiny edit with one focused check, or a request that must stay tightly coupled to the main conversation.

## Dispatch brake

Before delegation, establish all five answers:

1. **Outcome:** What exact deliverable and observable acceptance conditions are required?
2. **Direct-work alternative:** Would the main agent finish faster, more safely, or more cheaply?
3. **Independence:** Can workstreams progress without repeated shared-source reading or waiting on each other?
4. **Ownership:** Can every writable artifact—including configs, schemas, registries, generated outputs, and lockfiles—have one clear owner?
5. **Closure:** Who integrates, resolves contradictions, verifies final state, and reports coverage gaps?

If any answer is unclear, do not fan out. Clarify, use one bounded scout, converge a shared contract, or design ownership first. A large-looking task is not automatically a parallel task.

## Choose the smallest useful primitive

| Task shape | Default execution |
|---|---|
| Small edit, tightly coupled reasoning, final judgment, synthesis | Main agent directly |
| Bounded scout, one source, independent read-only review | One leaf worker |
| A few genuinely independent source or artifact surfaces | Bounded parallel leaf workers |
| Many homogeneous items with deterministic mapping | Small sampled slice, then bounded batches |
| Overlapping writes or competing implementation options | Serialize under one owner, or use an explicitly approved isolated branch/worktree |
| Shared workspace with disjoint paths | Parallel only with exclusive ownership and centralized final gates |
| Workers needing open-ended debate | Gather bounded independent evidence; let the main agent synthesize |

Normal worker waves should be small—often one to three. The runtime's configured hard cap remains authoritative. Never increase worker count merely because capacity is idle.

## Context-economy gate

Group raw request items by:

- shared source or source class;
- artifact ownership;
- dependencies and shared contracts;
- verification surface;
- expected reads and secondary writes.

Do not map one request bullet to one worker.

If two workers must reread the same large context, prefer one worker or one bounded scout that produces a compact, ref-backed context pack. Never clone the full parent transcript into every worker brief.

Create a shared context pack only when at least two workers need the same verified conclusions. Pass minimum reading sets, paths, artifact IDs, or evidence references rather than raw source dumps.

See `references/context-and-briefs.md`.

## Runtime and model routing

Read model routing, concurrency, role limits, safety, and tool capabilities from the live runtime configuration and current tool schema. Keep fast-changing prices out of the core instructions. When the runtime exposes the OpenAI GPT-5.6 family, use the dated cost snapshot and quick selection matrix in `references/model-and-effort-routing.md`, then refresh it from the linked official sources when exact prices matter.

When per-task model or reasoning-effort overrides exist:

- assign an intentional route to meaningful workers;
- treat install-wide delegation defaults as fallbacks for omissions, not as task classifiers;
- start with the lowest capability that has evidence of meeting the acceptance contract;
- reserve frontier models or maximum effort for ambiguity, contradiction, high-cost errors, or blocking final gates.

When a lower-cost model is unavailable from the native delegation schema, keep an exposed native lane or direct work as the default. A verified runtime-specific CLI compatibility bridge may be considered only after this skill selects one bounded delegation with stable contracts, exact exclusive target paths, and a main-agent integration owner. It must be ephemeral, ignore user configuration, require no approval, run read-only, and return a structured `apply_patch` proposal. The main agent verifies declared and actual patch paths, applies an accepted proposal itself, and runs the checks.

This bridge is not a new authority or capability. Do not use it for architecture, security, authorization, independent review, release or cutover judgment, live operations, credentials, or overlapping writes. Treat maximum effort as exception-budgeted for a demonstrably clear bounded implementation, never as the default for a low-cost lane.

Escalate by failure class:

- unclear output or missing fields → repair the brief first;
- bounded quality deficit → increase effort or move to a stronger operational lane;
- ambiguity, conflicting evidence, or high-risk judgment → use a frontier reasoning lane;
- repeated same-cause failure → stop or change task boundary, primitive, or validation.

## Standard execution flow

1. State outcome, non-goals, constraints, evidence required, budget, and direct-work fallback.
2. Group by shared context, artifacts, dependencies, and verification surface.
3. Converge shared schemas, registries, architecture choices, and high-risk contracts before fan-out.
4. Build one compact shared context pack only when it prevents meaningful rereading.
5. Assign exclusive artifact ownership and explicit forbidden writes.
6. Finalize self-contained worker briefs with output shape and stop conditions.
7. Select the lowest-cost model and effort lane with evidence of meeting the acceptance contract; repair unclear briefs before buying more capability.
8. Dispatch the minimum number of workers.
9. While they run, prepare integration and final verification instead of adding idle workers.
10. Main agent checks coverage, ownership, evidence, contradictions, and gaps.
11. Run centralized integration gates and report verified facts separately from unverified reasoning.

Read `references/dispatch-planning.md` and `references/execution-and-verification.md` for templates.

## Non-negotiable invariants

- Final judgment, side-effect decisions, synthesis, and truth claims stay with the main agent.
- Never parallelize unresolved shared contracts or overlapping writes.
- Every worker gets minimum sufficient context, exact scope, allowed/forbidden writes, output shape, evidence requirements, and a stop condition.
- Workers do not self-certify completion; independently verify material claims.
- Centralize expensive repository-wide, live, or shared-environment gates unless local diagnosis requires them.
- Keep failed, partial, skipped, or contradictory work visible as a coverage gap.
- If delegation is unavailable, unsafe, or repeatedly fails, fall back to direct execution.

## No blind duplicate workers

Identical full-context workers are allowed only for explicit A/B testing, independent verification, or adversarial review. Otherwise they multiply context and synthesis cost without creating a distinct evidence surface.

After the same cause fails again, do not launch a third unchanged attempt. Change the brief, context, model/effort lane, task boundary, primitive, or validation strategy.

## Write-surface discipline

For every write task, name:

- paths the worker owns;
- paths it may read but must not modify;
- shared artifacts that require serialization;
- secondary writes to watch, such as lockfiles, generated manifests, caches, or indexes;
- the integration owner.

Treat `read-only` as a contract to verify, not proof. For audits of skills, configs, catalogs, registries, or generated governance surfaces, capture a baseline and compare the write surface after every worker completes.

## Global stop conditions

Stop a delegated phase when any applies:

- acceptance criteria are met;
- time, token, retry, or worker budget is reached;
- repeated rounds make no material progress;
- the same cause fails again;
- ownership or dependency boundaries become invalid;
- integration and verification cost exceeds likely remaining benefit.

## Quick decision output

For non-trivial dispatch, return:

```markdown
## Outcome and success conditions
## Why delegation beats direct work
## Primitive and scale
## Shared context strategy
## Ownership and sequencing
## Worker briefs and evidence contract
## Verification and synthesis owner
## Budgets and stop conditions
## Direct-work fallback
```

## Verification

Run the three decision cases in `references/smoke-tests.md` in a fresh session after installation or a material update. A passing result should reject wasteful fan-out, preserve justified read-only parallelism, and stop unsafe overlapping writes.

## Attribution

This adaptation is derived from CabLate's MIT-licensed Baton project. Retain `LICENSE` and `NOTICE.md` when redistributing substantial portions.
