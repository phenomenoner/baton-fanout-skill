# Dispatch Planning

Use this reference when choosing whether to delegate, selecting an execution primitive, sizing a worker wave, or assigning write ownership.

## Decision sequence

Evaluate blockers before benefits:

1. Confirm the deliverable and acceptance conditions are stable enough to brief once.
2. Estimate direct work, including main-context, coordination, and review cost.
3. Group request items by shared context, artifacts, dependencies, and verification surface.
4. Identify workstreams by source, artifact, or responsibility—not vague role names.
5. Estimate shared-context overlap; make one compact context pack only when it prevents meaningful rereading.
6. Map expected reads, writes, and secondary writes.
7. Name the synthesis owner and final verification surface.

## Primitive selection

- **Main agent:** small work, tightly coupled reasoning, final decisions, or synthesis.
- **One worker:** bounded scouting, isolated source research, independent review; read-only by default.
- **CLI proposal worker:** one bounded implementation proposal only when a verified runtime-specific compatibility bridge is needed; keep the workspace read-only and let the main agent apply and verify the patch.
- **Parallel workers:** only a small number of mutually exclusive source or artifact surfaces.
- **Batch/workflow:** homogeneous items with deterministic mapping, retries, and a stop rule; begin with a sample.
- **Worktree/branch:** competing approaches or overlapping writes that need isolation; require explicit scope and a verified base.
- **Shared workspace:** only disjoint owned paths; forbid unplanned dependency, lockfile, schema, config, registry, and generated-manifest writes.

## Context-tax test

Before fan-out, compare:

```text
expected parallel benefit
versus
repeated context + coordination + duplicate verification + synthesis debt
```

If the workers need nearly identical reading sets and produce overlapping conclusions, fan-out usually loses. Use one worker or a scout-produced compact evidence pack instead.

## Ownership map

For every write dispatch, fill this before launch:

| Workstream | Must read | May write | Must not write | Secondary writes to watch | Integration owner |
|---|---|---|---|---|---|

Shared schemas, registries, indexes, generated outputs, configuration, and lockfiles are high-risk. Converge them first or assign one integration owner.

## Compatibility-bridge proposal contract

Treat a CLI proposal worker as delegated work, not a way around the dispatch brake. Before launch, record exact allowed target paths, the baseline workspace snapshot, permitted read-only checks, structured result fields, an outer budget, and the main-agent integration owner. Require an ephemeral, no-approval, read-only worker that ignores user configuration. Verify its post-run workspace snapshot and parse the actual patch paths as well as declared target paths before the main agent applies any proposal.

Choose about five minutes for one file, 15 minutes for a bounded cross-file proposal, and up to 30 minutes only while observable progress advances. Have the host render streamed progress to a task WAL outside the read-only workspace; the main agent may inspect it, but the WAL is not a worker write capability or new filesystem authority. Intervene on about five minutes without meaningful progress, repeated failed reads or hypotheses, scope drift, or budget exhaustion—not simply because a complex bounded task is still progressing past five minutes.

Do not route unresolved contracts, shared schemas or lockfiles, security or authority work, independent review, releases, cutovers, live operations, or credentials through a compatibility bridge. If its runtime support is absent or the brief fails twice for the same cause, use an exposed lane or direct work instead.

## Dispatch plan template

```markdown
## Outcome and success conditions
## Why delegation beats direct work
## Primitive and scale
## Shared context strategy
## Ownership and sequencing
## Verification and synthesis owner
## Budgets and stop conditions
## Direct-work fallback
```

## Scale conservatively

- Unclear direction → one scout.
- A few independent perspectives → a few read-only workers.
- Many homogeneous items → sampled slice, then bounded batches.
- Multi-phase work → discovery, convergence, implementation, and verification phases with gates between them.

Reduce parallelism when judgment-heavy integration, rapidly changing shared state, rate limits, or repeated failures dominate.
