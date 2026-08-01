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
