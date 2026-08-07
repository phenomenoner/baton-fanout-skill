# Baton Fanout Decision Smokes

Run these in a fresh agent session after installing or materially changing the skill. They test decisions, not keyword matching.

## 1. Reject wasteful delegation

```text
Use baton-fanout-skill to evaluate this plan:

A known formatting bug is in one known file with one focused test. Spawn an investigator, a builder, and a verifier.

Return the minimum execution primitive, why it is sufficient, and the coordination costs avoided.
```

**Pass:** direct main-agent execution plus the focused check; no three-worker fan-out.

## 2. Preserve justified parallel research

```text
Use baton-fanout-skill to design execution for three independent, read-only sources: official documentation, repository usage, and operational case studies. A main agent must synthesize the decision.

Return the primitive, worker boundaries, result format, synthesis owner, and stop conditions.
```

**Pass:** bounded parallel read-only workers with distinct source boundaries and main-agent synthesis.

## 3. Stop unsafe parallel writes

```text
Use baton-fanout-skill to review a proposed parallel refactor where three builders all need to edit the same shared type and registry before changing separate feature folders.
```

**Pass:** shared type and registry converge under one owner before any feature fan-out; no overlapping writers.

## 4. Brief-repair routing smoke

```text
A bounded worker failed because the brief omitted one required output field. Should the parent launch two stronger models with the same brief?
```

**Pass:** repair the brief first; do not multiply workers or capability until the failure class is understood.

## 5. Native-lane and scout routing smoke

```text
Assume the live runtime exposes gpt-5.6-sol and gpt-5.6-terra, but not gpt-5.6-luna. Route these workers by model and effort: a deterministic inventory, a read-heavy repository scan, and a cross-cutting authorization review.
```

**Pass:** use Terra low or direct work for the inventory because the codegen-only CLI bridge does not cover scouting, Terra low for the read-heavy scan, and at least Sol high for the authorization review. The answer must say that live runtime availability overrides the dated reference and must not invent Luna exposure.

```text
The live runtime exposes native Luna. Compare a deterministic exact-path inventory with an exploratory repository scout whose source locations and hypotheses are unknown. May either use Luna/max, and may either use the CLI bridge?
```

**Pass:** native Luna/max may be the first candidate for the deterministic, cheaply falsifiable inventory after Baton. The exploratory scout should use direct work or one bounded native Terra/Sol lane; the codegen-only CLI bridge is ineligible for both scouting and search.

## 6. Compatibility-bridge smokes

```text
The native delegation runtime exposes Sol and Terra but not Luna. A verified local Codex CLI accepts Luna at max effort. One stable one-file implementation task has exact exclusive ownership, and the main agent can inspect, apply, and test a read-only structured patch proposal. Should Baton use the bridge?
```

**Pass:** select at most one Luna/max CLI proposal as the first candidate after the dispatch brake; require ephemeral, ignore-user-config, no-approval, read-only execution, before/after workspace checks, declared and actual patch-path verification, and main-agent application/testing. It must state that Terra/Sol or direct work remains the fallback when Luna is unavailable, ineligible, or fails calibration.

```text
Use the same bridge for a change involving authorization policy, live configuration, a shared schema, or an independent release review.
```

**Pass:** reject the bridge. Keep authority, security, review, release, and live-operation judgment with the main agent or use an exposed appropriate lane after normal dispatch governance.

```text
The same verified bridge has one exact file and emits streamed progress to a task WAL outside its read-only workspace. It has made meaningful source-reading progress at minute 6. At minute 11, it repeatedly rereads the same files without a new hypothesis. How should Baton set and use its outer timeout?
```

**Pass:** distinguish the expected five-minute one-file budget from a predeclared bounded hard timeout. Permit continuation at minute 6 because the latest WAL progress is meaningful, then intervene after the stalled window rather than treating elapsed time alone as failure. Require the host-owned WAL to remain outside the workspace and evidence-only; it must not grant worker write authority. Mention 15 minutes for bounded cross-file work and up to 30 minutes only while progress continues.

```text
At the hard deadline the read-only bridge has an in-memory patch but has not emitted a parseable proposal. Its WAL shows recent format-polish after earlier useful work. What may the main agent retain or adopt, and how should the next attempt be shaped?
```

**Pass:** preserve only emitted partial evidence, never adopt the in-memory or unemitted patch, and require a parseable checkpoint/final proposal before late format-polish with a small completion buffer. If no proposal arrives, split the task narrower rather than replaying the unchanged brief.

## 7. Independent-review relative-strength smoke

```text
The working session uses an exposed Sol/high lane. Route one genuinely independent code reviewer. Then answer the same question when the working session already uses the strongest lane exposed by the runtime.
```

**Pass:** the first case chooses a clearly stronger exposed reviewer route above Sol/high, without assuming Sol/max is always the answer. At the runtime ceiling it uses the same top lane with fresh independent or adversarial context. It never drops below Sol/high, never uses Luna for review, and does not invent an unavailable model or effort.
