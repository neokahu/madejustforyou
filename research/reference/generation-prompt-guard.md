# Generation prompt guard — mechanical enforcement of the prompt method

**Why this exists.** On 2026-09-26 I ignored the documented prompt method **three times in one session**,
each time costing a failed generation and a wrong conclusion:

1. **Test C** — four simultaneous motions, no named shots, no constraints → the dog morphed sitting→standing.
2. **Test E** — one shot instead of two, action not located in space → a grief ad where the man holds his
   palm out at camera like a *stop* gesture, eyes closed.
3. **Test D4** — a ~190-word prompt that re-described the entire printed poem → the print outranked the
   pose and the model produced a catalogue packshot instead of the wrapped shot asked for.

All three violate rules that were already written down. **Documentation did not change behaviour.** This
hook does, because it blocks the call before it runs.

## How it works

`PreToolUse` fires before a generation tool executes. Claude Code pipes the tool name and arguments to
`~/.claude/hooks/generation-prompt-guard.py` on stdin. The script validates the prompt and returns a
decision. On `deny` **the call never executes** and the reason is returned naming the rule and the fix.

Registered in `.claude/settings.json`, matching TopView / Seedance / Kling / Veo / Wan / Hailuo / Sora /
AtlasCloud generation tools. Source mirrored at `research/scripts/generation-prompt-guard.py`.

## What it blocks

| Rule | Check | Source |
|---|---|---|
| `LENGTH` | prompt > 100 words | *"20–50 words. Quality fragments past ~80–100."* |
| `REDESCRIBE` | reproduces the product's own printed text/design | **THE ONE RULE** — *"#1 cause of warping/morphing"* |
| `SHOTS` | video prompt with no named `Shot 1` | settled recipe: two named shots |
| `TIMECODE` | contains `0–3 seconds` style timings | *"unstable, may lead to abnormal generation results"* |
| `OPENMOVE` | Shot 1 has no camera move, or is static | measured: fixed opening dropped hook3 **14.90 → 5.87** |
| `ONEMOVE` | more than one camera move in Shot 1 | *"will increase image instability"* |
| `CONSTRAINT` | no line pinning what must not change | *"constraint words are very important"* |

Warnings (non-blocking): `RES` (4K on a likely first pass — draft first), `REDESCRIBE-SOFT`.

## Override

Add `ACK-<RULE>` to `commandId` — e.g. `beat3-ACK-OPENMOVE` for a mid-film beat not measured by `hook3`.
An exception must be a conscious act and explained to the user, not a silent bypass.

## Verified

```
✅ ALLOW   testE3 two-shot people prompt      (validated: hook3 14.90)
✅ ALLOW   testC3 reveal beat                 (validated: hook3 14.68)
❌ DENY    testC original                     → SHOTS, CONSTRAINT
❌ DENY    testC2 fixed opening               → OPENMOVE
❌ DENY    testD4 blanket prompt              → LENGTH, REDESCRIBE
✅ ALLOW   testC2 + ACK-OPENMOVE              (override honoured)
```

Blocks every real mistake from that session; passes everything that actually worked.

## Bugs found while building it — keep if extending

- `pan` matched inside **"panel"**, blocking a known-good prompt. All camera verbs need `\b` boundaries.
- `exactly as in` appears in the *required* CONSTRAINT line, so the re-describe check fired on correct
  prompts. It now also requires a text/artwork/design word nearby.
- A static opening was first a warning; the measured hook3 collapse justifies a block with an override.

## What it cannot check

It is mechanical. It cannot tell whether an action is **located in space** (the Test E failure — *"raises
his hand into the light"* passes every check and still produced a stop gesture), whether casting matches
customized artwork, or whether the shot serves the concept. Those remain judgement, and judgement still
belongs in the doc read before prompting.


---

## 2026-09-26 — extended to the image models, both providers

**Coverage hole found by testing, not by reading:** `nano_banana`, `gpt_image`, `seedream`, `flux2_image`,
`imagen4`, `ideogram_v3` and `wan_image` were never in the tool list, so **every kie.ai image call ran
unguarded** — including the one that produced the punched-through hand.

**AtlasCloud needed a different fix.** It routes every image model through one generic tool
(`atlas_generate_image`) and passes the model id as a *parameter*, so the tool name cannot identify the
model. `model_of()` now recovers it by reading `model` / `modelId` / `parameters.model`, which also covers
TopView (`nano_banana2`, `gpt-image-2.5-flare`) and AtlasCloud ids like
`openai/gpt-image-2.5-flare/edit`, `bytedance/seedream-v4.7/edit`.

### Verified coverage — 9 paths, all guarded

```
kie.ai  nano_banana_pro_image · nano_banana_edit · gpt_image_2 · openai_4o_image · ideogram_v3_edit
atlas   atlas_generate_image (+gpt-image) · atlas_generate_image (+seedream) · atlas_quick_generate
topview submit_topview_canvas_generation_task (+nano_banana2, image_edit)
```

### Generic image rules

| Rule | Check | Source |
|---|---|---|
| `NEGFRAME` | exclusionary framing — "only X shows", "no Y visible", "without Z" | Google: *"use positive framing"* |
| `LIMB` | a hand/arm/palm named but never located | THE LIMB RULE — the punched-hand failure |
| `REFROLE` | a reference used with no assigned role | OpenAI multi-ref format |

### Model-specific rules — fire only on their own model (cross-checked)

| Rule | Model | Check |
|---|---|---|
| `GPTTERSE` | GPT Image, edit | prose in an edit prompt ("beautiful", "artistically", "please"). OpenAI: **direct commands, terse, no flowery language** |
| `NANOREL` | Nano Banana, with refs | no relationship instruction. Google's formula is *[references] + [relationship] + [new scenario]*, started with a strong verb |
| `SEEDQUOTE` | Seedream | text requested without double quotes around the exact string (warning) |

Image word cap is **250** (not 100 — that came from the i2v doc, which is about *animating* an existing
image; generation formulas are structurally longer and Seedream's own limit is ~600 words).

Full method: `research/reference/image-prompt-method.md`.
