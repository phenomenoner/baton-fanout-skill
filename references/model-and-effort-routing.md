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
| Deterministic extraction, classification, formatting, inventory, or repetitive transforms | `gpt-5.6-luna` | max when the lane is verified and the result is cheap to falsify | Instructions require interpretation or results conflict | `gpt-5.6-terra` low or direct work |
| Bounded low-judgment scout, repository inventory, documentation scan, log triage, or evidence collection with an exact output contract | `gpt-5.6-luna` | max | Source locations, hypotheses, or semantics require material interpretation | Terra low/high as needed, then Sol medium |
| Stable, bounded code generation with exact target paths and mechanically verifiable acceptance | `gpt-5.6-luna` | max | The contract is incomplete, paths overlap, or judgment dominates | Direct work or an exposed Terra/Sol lane selected from evidence |
| Conventional debugging with a known symptom and bounded evidence | `gpt-5.6-terra` | medium | Root cause crosses state, concurrency, identity, or security boundaries | Sol high |
| Independent code, release, migration, or cutover review | At least `gpt-5.6-sol` | At least `high` | A clearly stronger reviewer lane is exposed above the working session | Use that stronger lane; at the runtime ceiling use the same top lane with fresh context |
| Architecture, migration design, ambiguous diagnosis, or cross-cutting contract reasoning | `gpt-5.6-sol` | high | Contradictions remain after evidence review | Sol xhigh |
| Security, authorization, destructive change, release judgment, or high-cost error analysis | `gpt-5.6-sol` | high or xhigh | Deeper reasoning is demonstrably useful | Sol max or ultra when exposed |
| Final integration, contradiction resolution, and user-facing truth claims | Main agent | Current task setting | Do not outsource final judgment | One independent Sol review only when justified |

Luna/max is the first native candidate only after Baton selects delegation for a stable, bounded task whose result is cheap to falsify and whose expected judgment need is no greater than Terra/high. This includes exact-target code generation and low-judgment scouts with an explicit evidence/output contract. Exploratory scouting with unknown source locations or hypotheses, ambiguous diagnosis, architecture, security or authority decisions, independent review, release or cutover judgment, live operations, credentials, overlapping ownership, and incomplete contracts stay with direct work or an appropriate native Terra/Sol lane.

If Luna is unavailable or ineligible, choose direct work or an exposed Terra/Sol lane from task evidence; do not invent an unavailable lane and do not treat Luna failure as an automatic Terra fallback.

## Independent-review floor and relative strength

Route an independent reviewer at no less than `gpt-5.6-sol` at `high` effort. When the live runtime exposes a reviewer lane that it clearly orders above the user session's working lane, use that stronger lane. Prefer a higher model tier, then higher effort within the same tier; do not pretend incomparable or unavailable routes form a reliable total order.

If the working session is already at the runtime's strongest exposed lane, use the same top lane with fresh independent or adversarial context. This preserves genuine independence without making Sol/max a fixed default. If the current session's model or effort is not exposed, apply the Sol/high floor and state that relative-strength comparison could not be proven. Always keep the main agent's final judgment and never use Luna for independent review.

## Native spawn override contract

Codex supports global `[agents]` defaults and explicit per-spawn model and reasoning-effort values. Use `spawn_agent` with `model: "gpt-5.6-luna"` and `reasoning_effort: "max"` for an eligible Luna task. Explicit spawn values take precedence over global defaults, so keep install-wide defaults neutral unless most omitted routes genuinely share one class.

The live collaboration schema controls context-fork compatibility. In the current Codex App schema, explicit model/effort overrides require `fork_turns="none"` or a bounded positive recent-turn fork; a full-history fork inherits the parent route and does not accept overrides. Prefer a self-contained brief and the smallest useful fork. Never shell out to `codex exec` merely to obtain a worker route already exposed by native subagents.

## Effort modifiers

| Effort | Use when | Avoid when |
|---|---|---|
| `low` | Work is mechanical, scoped, and easy to verify | Ambiguity, edge cases, or cross-cutting reasoning dominate |
| `medium` | Ordinary exploration, implementation, and synthesis | A lower-effort lane already meets the contract |
| `high` | Complex logic, competing hypotheses, reviewer work, or risky edge cases | The brief is incomplete or evidence is missing |
| `xhigh` | Frontier work with real ambiguity or high-cost mistakes | Routine workers or broad fan-out |
| `max` / `ultra` | Eligible Luna code generation at max, or exceptional blocking judgment when supported and budgeted | Compensation for a defective brief or an automatic review default |

Higher effort increases latency and token use. First reduce unnecessary context, output volume, and duplicated reads; these often save more than a model downgrade alone.

## Escalation order

1. Repair missing scope, output fields, evidence requirements, or stop conditions in the brief.
2. Add only the missing sources or a compact context pack.
3. Increase effort one step when the model is capable but reasoning was shallow.
4. Move Luna to Terra or Terra to Sol when complexity exceeds the current model lane.
5. Stop after repeated same-cause failure and change the work boundary or primitive.

Do not launch duplicate stronger workers with the same defective brief. Sample a small slice before committing a high-volume lane.

## Refresh sources

- Codex subagent configuration and precedence: https://learn.chatgpt.com/docs/agent-configuration/subagents
- Codex `[agents]` configuration keys: https://learn.chatgpt.com/docs/config-file/config-reference
- Model selection guidance: https://developers.openai.com/tracks/building-agents#how-to-choose
- Current prices: https://developers.openai.com/api/docs/pricing
- Price-change date and percentages: https://developers.openai.com/api/docs/changelog
