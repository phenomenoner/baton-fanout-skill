# Model and Effort Routing

Use this reference only after the dispatch brake selects delegation and before launching workers. The live runtime's model and effort schema overrides every recommendation below.

## Cost snapshot

As of 2026-08-01, official OpenAI Standard API prices for short-context text are:

| Model | Input / 1M tokens | Output / 1M tokens | Relative to Sol | Practical role |
|---|---:|---:|---:|---|
| `gpt-5.6-sol` | $5.00 | $30.00 | 1.00x | Frontier judgment and demanding agent work |
| `gpt-5.6-terra` | $2.00 | $12.00 | 0.40x | Balanced everyday work and read-heavy scans |
| `gpt-5.6-luna` | $0.20 | $1.20 | 0.04x | Clear, repeatable, high-volume work |

The OpenAI changelog reports that Luna pricing fell 80% and Terra pricing fell 20% on 2026-07-30. Treat API prices as a relative cost proxy, not as a Codex, ChatGPT, or other agent-runtime bill: subscriptions, credits, service tiers, cached tokens, long context, and product policy may differ.

In this snapshot, Batch and Flex API rates are normally half the Standard rates, while Fast mode is twice Standard. Do not infer that an agent runtime uses any API service tier unless its live configuration says so.

## Quick routing matrix

| Workstream | Default model | Effort | Escalate when | Fallback |
|---|---|---|---|---|
| Deterministic extraction, classification, formatting, inventory, or repetitive transforms | `gpt-5.6-luna` | low | Instructions require interpretation or results conflict | `gpt-5.6-terra` low |
| Repository search, documentation scan, log triage, large-file reading, or evidence collection | `gpt-5.6-terra` | low | Cross-source synthesis or subtle semantics appear | Terra medium, then Sol medium |
| Clear bounded implementation with stable contracts and focused tests | `gpt-5.6-terra` | medium | Multiple modules, unclear behavior, or repeated test failure | Sol medium or high; optional verified Luna CLI bridge |
| Conventional debugging with a known symptom and bounded evidence | `gpt-5.6-terra` | medium | Root cause crosses state, concurrency, identity, or security boundaries | Sol high |
| Independent checklist review with objective acceptance criteria | `gpt-5.6-terra` | medium or high | Review requires ambiguity resolution or adversarial edge cases | Sol high |
| Architecture, migration design, ambiguous diagnosis, or cross-cutting contract reasoning | `gpt-5.6-sol` | high | Contradictions remain after evidence review | Sol xhigh |
| Security, authorization, destructive change, release judgment, or high-cost error analysis | `gpt-5.6-sol` | high or xhigh | Deeper reasoning is demonstrably useful | Sol max or ultra when exposed |
| Final integration, contradiction resolution, and user-facing truth claims | Main agent | Current task setting | Do not outsource final judgment | One independent Sol review only when justified |

If Luna is not exposed by the current runtime, use Terra low for its lane or direct work by default. Never invent or request an unavailable model slug.

## Optional CLI compatibility bridge

A runtime-specific, verified wrapper may expose `gpt-5.6-luna` through Codex CLI when the native delegation schema does not. This is a compatibility bridge for one bounded implementation proposal, not a replacement for the runtime's delegation controls or an authority/capability escalation.

Use it only after the dispatch brake selects one delegated worker and all of these are true:

- the contract is stable, the owned target paths are exact, and no other worker may write them;
- the local CLI has been verified to accept the requested model and effort; for example, Codex CLI 0.146 accepted `gpt-5.6-luna` with `model_reasoning_effort="max"`;
- the worker is ephemeral, ignores user configuration, requires no approval, runs read-only, and returns a structured `apply_patch` proposal;
- the main agent compares workspace state before and after, mechanically verifies both declared and actual patch paths, applies any accepted patch itself, and independently tests it.

Do not send credentials, private receipts, connection profiles, or live configuration to the bridge. Do not use it for architecture, security, authorization, independent review, release or cutover judgment, live operations, or overlapping writes. Preserve an exposed native lane or direct work as the default fallback. `max` is exception-budgeted for a demonstrably clear bounded implementation; it is not the default Luna effort.

Choose an expected bridge budget by task shape - about five minutes for one file or 15 minutes for a bounded cross-file proposal - and separately predeclare an outer hard timeout of up to 30 minutes. Judge continuation from the latest meaningful host-rendered task-WAL progress, not total elapsed time alone. The host may stream progress into a task WAL outside the read-only workspace for the main agent to inspect. That WAL is evidence only and grants the worker no new filesystem authority.

Require a parseable checkpoint or final proposal before late format-polish and reserve a small completion buffer before the hard deadline. Intervene on about five minutes without meaningful progress, repeated failed reads or hypotheses, scope drift, or budget exhaustion. Prolonged work may continue only within the predeclared bounded maximum while progress advances. At the outer timeout preserve only emitted partial evidence; never adopt an in-memory or unemitted patch. If no proposal arrives, split the task narrower rather than replaying the unchanged brief.

## Effort modifiers

| Effort | Use when | Avoid when |
|---|---|---|
| `low` | Work is mechanical, scoped, and easy to verify | Ambiguity, edge cases, or cross-cutting reasoning dominate |
| `medium` | Ordinary exploration, implementation, and synthesis | A lower-effort lane already meets the contract |
| `high` | Complex logic, competing hypotheses, reviewer work, or risky edge cases | The brief is incomplete or evidence is missing |
| `xhigh` | Frontier work with real ambiguity or high-cost mistakes | Routine workers or broad fan-out |
| `max` / `ultra` | Exceptional blocking judgment when supported and budgeted | Default routing or compensation for a defective brief |

Higher effort increases latency and token use. First reduce unnecessary context, output volume, and duplicated reads; these often save more than a model downgrade alone.

## Escalation order

1. Repair missing scope, output fields, evidence requirements, or stop conditions in the brief.
2. Add only the missing sources or a compact context pack.
3. Increase effort one step when the model is capable but reasoning was shallow.
4. Move Luna to Terra or Terra to Sol when complexity exceeds the current model lane.
5. Stop after repeated same-cause failure and change the work boundary or primitive.

Do not launch duplicate stronger workers with the same defective brief. Sample a small slice before committing a high-volume lane.

## Refresh sources

- Model selection guidance: https://developers.openai.com/tracks/building-agents#how-to-choose
- Current prices: https://developers.openai.com/api/docs/pricing
- Price-change date and percentages: https://developers.openai.com/api/docs/changelog
