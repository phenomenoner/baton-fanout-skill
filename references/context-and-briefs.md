# Context Packs and Worker Briefs

Use this reference when multiple workers need common conclusions or when preparing a delegation brief.

## Shared context pack

Create one only when at least two workers need the same verified findings or when the main agent has already completed expensive discovery that should not be repeated. Keep it factual, compact, dated, and reference-backed.

```markdown
# Shared Context Pack — <task>

## Outcome and non-goals
## Acceptance conditions
## Current state and constraints
## Relevant architecture or source map
## Verified conclusions and primary evidence
## Rejected directions and reasons
## Shared contracts and invariants
## Ownership boundaries
## Minimum reading set per workstream
## Risks, unknowns, and confidence
## Verification and synthesis plan
```

Mark each conclusion as verified or inferred. Update the pack at phase boundaries; do not turn it into a source dump or transcript mirror.

Prefer:

- source paths and URLs;
- artifact or query IDs;
- evidence references;
- content hashes;
- short verified conclusions.

Avoid copying the full parent conversation into every worker.

## Dispatch-ready worker brief

Assume a worker has no access to the main conversation. Finalize a brief only after dependencies, ownership, verification, and stop conditions are stable.

```markdown
# Brief — <workstream>

## Objective and acceptance conditions
## Why this boundary is independent
## Shared context and required sources
## Exact in-scope and out-of-scope work
## Minimum files or sources to read
## Allowed writes
## Forbidden writes and high-risk shared artifacts
## Allowed commands and local verification
## Required output format
## Time, token, retry, and scope stop conditions
## What to do when an assumption fails
```

For independent review, provide the artifact and acceptance criteria without the implementer's preferred conclusion or reasoning trail.

## Default boundaries

Unless the task states otherwise:

- allow focused, local checks only;
- reserve repository-wide, live, and shared-environment gates for integration;
- forbid dependency installation and lockfile changes;
- stop before touching unowned paths;
- report changed artifacts, evidence, deviations, and unresolved assumptions.

## Worker result format

```markdown
## Summary
## Changed artifacts or source findings
## Verified evidence
## Reasoned but unverified conclusions
## Risks and assumptions
## Deviations from brief
## Needs main-agent decision
## Large artifact paths or evidence references
```

Prefer bounded artifacts and references over large inline dumps.
