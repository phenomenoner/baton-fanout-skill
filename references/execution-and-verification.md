# Execution and Verification

Use this reference while delegated work runs and when integrating its results.

## Monitor without over-dispatching

While workers run:

1. Prepare the integration checklist and final commands.
2. Incorporate verified conclusions into the shared context pack.
3. Check returned partial results for scope violations, contradictions, and invalid assumptions.
4. Do only independent work outside active ownership boundaries.
5. Monitor failure rate, elapsed time, resource use, and integration backlog.

Never add workers just because concurrency is available. Do not modify artifacts owned by active workers.

## Read-only write-surface verification

A read-only brief is a declared boundary, not proof that no write occurred. For audits involving skills, configuration, registries, generated catalogs, or other routing surfaces:

1. Capture a pre-dispatch inventory or snapshot of the exact write surface.
2. Explicitly forbid configuration, memory, policy, skill, or generated-governance writes unless one is intentionally owned.
3. Keep final archive, delete, index, and catalog mutations serialized under the main agent.
4. After every worker returns, compare the live surface with the baseline.
5. If a worker violated scope, preserve evidence, revert or quarantine the artifact, and repeat active-catalog and index verification.

## Failure signals

| Signal | Main-agent response |
|---|---|
| Unclear or incomplete brief | Repair the brief before changing models or adding workers |
| Repeated same-cause failure | Stop; change brief, boundary, primitive, or validation |
| Scope or ownership violation | Pause affected work; reconcile artifacts before resuming |
| Conflicting conclusions | Recheck primary evidence; adjudicate centrally |
| Integration backlog growing | Stop fan-out; synthesize what exists |
| Worker stuck in expensive verification | Recover partial work; centralize the gate |
| Delegation unavailable or unsafe | Fall back to direct execution |
| Rate-limit or retry cascade | Reduce concurrency; use bounded sequential batches |

## Verification economics

- Run fast focused checks near a change when they do not contend for shared resources.
- Run repository-wide builds, type checks, integration tests, and shared-environment tests once after integration.
- Centralize live or visual verification unless a worker needs it to establish root cause.
- Worker self-reports are inputs, never completion evidence; review changed artifacts and sample material evidence.

## Synthesis checklist

The main agent must:

1. confirm coverage and list failed, partial, skipped, or blocked work;
2. compare artifacts with ownership;
3. deduplicate repeat findings;
4. adjudicate contradictions from primary evidence;
5. preserve credible minority concerns;
6. run final integration gates; and
7. label each conclusion as verified, consistent but not independently rechecked, reasoned but unverified, or needing human testing.

```markdown
## Inputs and coverage
## Integrated changes or findings
## Conflicts and adjudication
## Remaining minority concerns
## Verification evidence
## Gaps and human checks
```
