# Topic — Generation prompt-guard hook

**Status:** live. A `PreToolUse` hook BLOCKS generation prompts that break the documented method.

## Why
The documented prompt method was ignored three times in one session (Tests C, E, D4), each costing a failed generation and a wrong conclusion. Documentation did not change behaviour → enforce mechanically.

## Current state
- Script: `~/.claude/hooks/generation-prompt-guard.py`, mirrored at `research/scripts/generation-prompt-guard.py`; registered in `.claude/settings.json`.
- Covers kie.ai, AtlasCloud, TopView image + video generation.
- Per-model rules: `GPTTERSE`, `NANOREL`, `SEEDQUOTE`. `motion_control` exempt from shot-structure rules.
- Word caps: image 250 · structured video 220 · freeform 100. Warns on 4K first passes.
- Override: `ACK-<RULE>` in `commandId`.
- Verified: passes testE3/testC3 (worked), denies testC/testC2/testD4 (failed).

## Detail
- `research/reference/generation-prompt-guard.md`
- Sessions: [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md) · [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
