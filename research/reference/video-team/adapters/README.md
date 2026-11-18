# Tool adapters

Role 05 writes **tool-agnostic generation briefs** (`../role-research/05-visual-director.md` §4.1). An adapter
turns a brief into a prompt for one specific tool. When a tool changes, write a new adapter; the roles stay the same.

Each adapter must define:
- field order and syntax the tool prefers
- how it takes references (count limit, indexing, roles)
- camera-move vocabulary and how reliably the tool follows it
- word cap and negative-prompt support
- structured parameters vs prose (aspect, duration, resolution, seed)
- minimum and billable duration, and cost
- known failure modes with tested fixes

Every adapter must keep the principles in §4.2 of the role-05 research: positive framing, one move per shot, never re-describing what a reference carries, limbs located in space, no generated text, the product never drawn, draft low and select from N.

## Current adapters (tool-specific docs written before this team existed)
| Tool / class | Adapter |
|---|---|
| Seedance 2.x video (text/image/reference-to-video) | `../../seedance-prompt-method.md` |
| Image-to-video, any model (cheat sheet) | `../../image-to-video-prompt-method.md` |
| Image models: GPT Image, Nano Banana, Seedream | `../../image-prompt-method.md` |
| Camera / transition move names | Motion Prompt skill (`~/.claude/skills/motion-prompt`), see seedance-prompt-method § "Naming the move" |

Enforcement: `../../generation-prompt-guard.md` (a PreToolUse hook). Extend it whenever a new adapter is added.
