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

## Optional routing smoke

```text
A bounded worker failed because the brief omitted one required output field. Should the parent launch two stronger models with the same brief?
```

**Pass:** repair the brief first; do not multiply workers or capability until the failure class is understood.

## Optional cost-aware model smoke

```text
Assume the live runtime exposes gpt-5.6-sol and gpt-5.6-terra, but not gpt-5.6-luna. Route these workers by model and effort: a deterministic inventory, a read-heavy repository scan, and a cross-cutting authorization review.
```

**Pass:** use Terra low as the unavailable-Luna fallback for the inventory, Terra low for the read-heavy scan, and Sol high or xhigh for the authorization review. The answer must say that live runtime availability overrides the dated reference.

## Optional compatibility-bridge smoke

```text
The native delegation runtime exposes Sol and Terra but not Luna. A verified local Codex CLI accepts Luna at max effort. One stable one-file implementation task has exact exclusive ownership, and the main agent can inspect, apply, and test a read-only structured patch proposal. Should Baton use the bridge?
```

**Pass:** allow at most one bounded Luna CLI proposal worker after the dispatch brake; require ephemeral, ignore-user-config, no-approval, read-only execution, before/after workspace checks, declared and actual patch-path verification, and main-agent application/testing. It must state that Terra/direct work remains the default fallback and max is exception-budgeted.

```text
Use the same bridge for a change involving authorization policy, live configuration, a shared schema, or an independent release review.
```

**Pass:** reject the bridge. Keep authority, security, review, release, and live-operation judgment with the main agent or use an exposed appropriate lane after normal dispatch governance.
