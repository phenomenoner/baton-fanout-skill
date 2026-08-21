# Codex App and CLI Adapter

Use this adapter after Baton has selected delegation. The current collaboration tool schema and higher-priority Codex instructions remain authoritative.

## Map plans to Codex collaboration tools

| Intent | Codex primitive |
|---|---|
| Start one bounded subtask | `spawn_agent` |
| Send non-triggering context to a running worker | `send_message` |
| Give a completed or idle worker another bounded task | `followup_task` |
| Wait for the next worker update after useful local work is exhausted | `wait_agent` |
| Stop a drifting or no-longer-useful worker | `interrupt_agent` |
| Inspect current agent state once | `list_agents` |

Do not create, fork, or hand off a user-owned Codex App task to implement an internal subtask. App tasks appear in the user's task list and are for user-owned coordination; collaboration agents are for delegated work inside the current task.

## Context and ownership

- Use `fork_turns="none"` for exact-path, self-contained briefs and a small positive value only when recent conversational context is material. Full history is the exception.
- All native agents share the workspace. Assign exclusive writable paths, list forbidden paths, and serialize unresolved shared contracts.
- A read-only brief is a contract to verify. Capture the relevant baseline and compare it after the worker returns.
- Keep repository-wide checks, synthesis, publication, release decisions, and user-facing truth claims with the main agent.

## Model and effort

Use `references/model-and-effort-routing.md`. Pass `model` and `reasoning_effort` directly to `spawn_agent` when the task-class route should differ from inherited defaults. Official Codex settings also expose `[agents]` defaults, but explicit spawn values take precedence; treat defaults as omission fallbacks rather than task classifiers.

In the current collaboration schema, model overrides require `fork_turns="none"` or a bounded positive recent-turn fork. A full-history fork inherits the parent model and effort and does not accept overrides. Keep the worker brief self-contained, use the smallest fork that supplies needed context, and never request a model or effort the live schema does not expose.

## Waiting

While workers run, continue useful integration or verification work. When no useful work remains, use one long `wait_agent` mailbox wait. Do not wrap native agents in process supervisors or manufacture short polling loops.
