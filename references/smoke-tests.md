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
Assume the live runtime exposes gpt-5.6-sol and gpt-5.6-terra, but not gpt-5.6-luna. Route these workers by model and effort: a deterministic inventory, an exploratory repository scan, and a cross-cutting authorization review.
```

**Pass:** use direct work or an exposed Terra lane for the inventory and exploratory scan, and at least Sol/high for the authorization review. The answer must say that live runtime availability overrides the dated reference, must not invent Luna exposure, and must not shell out to a nested Codex CLI worker.

```text
The live runtime exposes native Luna. Compare a deterministic exact-path inventory with an exploratory repository scout whose source locations and hypotheses are unknown. Which native route should each use?
```

**Pass:** native Luna/max is the first candidate for the deterministic, cheaply falsifiable inventory after Baton. The exploratory scout should use direct work or one bounded native Terra/Sol lane because unknown hypotheses raise the judgment requirement.

## 6. Native override and context-fork smokes

```text
The live collaboration schema exposes Luna and per-spawn model and reasoning-effort fields. One stable one-file implementation task has exact exclusive ownership and mechanically verifiable acceptance. How should Baton dispatch it?
```

**Pass:** select at most one native Luna/max worker after the dispatch brake and pass an explicit native model and effort override to `spawn_agent`. Use a self-contained brief, exact ownership, main-agent review, and focused verification. Do not start `codex exec` or another CLI worker.

```text
The exact-path worker needs Luna/max but also requests a full-history fork. The current schema says full-history forks inherit the parent route and do not accept model overrides. What should Baton do?
```

**Pass:** choose a self-contained `fork_turns="none"` brief or a bounded positive fork so the explicit override is valid. If full history is genuinely required, inherit the parent route and do not claim Luna/max was applied.

```text
Global configuration sets default_subagent_model and default_subagent_reasoning_effort. Should Baton rely on those defaults to route every codegen, scout, architecture, and review worker?
```

**Pass:** treat the globals as omission fallbacks, not task classifiers. Pass explicit native overrides for meaningful task-class routes; retain Luna/max for eligible stable work and Sol/high-or-stronger for independent review.

## 7. Independent-review relative-strength smoke

```text
The working session uses an exposed Sol/high lane. Route one genuinely independent code reviewer. Then answer the same question when the working session already uses the strongest lane exposed by the runtime.
```

**Pass:** the first case chooses a clearly stronger exposed reviewer route above Sol/high, without assuming Sol/max is always the answer. At the runtime ceiling it uses the same top lane with fresh independent or adversarial context. It never drops below Sol/high, never uses Luna for review, and does not invent an unavailable model or effort.
