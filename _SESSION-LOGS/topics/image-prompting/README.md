# Topic — Image prompting

**Status:** method documented; per-model rules enforced by the prompt-guard hook.

## Current decisions
- **THE ONE RULE:** when a product reference image is supplied, **don't re-describe the product**. D4 (~190 words re-describing the poem) → catalogue packshot; D5 (~50 words, product not described) → pose landed, print correct.
- **Stills model:** `nano_banana2` (Nano Banana Pro) — best text fidelity. `gpt-image-2.5-flare` spells right in the **wrong typeface** — avoid where font matters.
- **Draft at 720p/2K, batch 3–4, re-run the keeper at full res.** Ignoring this burned ~66 TopView credits in one day.
- **Casting must match customized artwork:** never describe the on-camera person generically — name skin tone, hair texture, colour and style to match the printed figure.
- Word caps (hook): image prompts 250.

## Key evidence
- D4 vs D5 (blanket) — sessions/2026-09-26 §8.
- "Young woman" → white woman against Black cartoon figures — sessions/2026-09-26 §11.

## Open items
- Character reference sets — see [character-references](../character-references/README.md).

## Detail
- `research/reference/image-prompt-method.md` (incl. character reference-set template + QA 2026-09-29)
- `research/reference/image-to-video-prompt-method.md`
- `research/reference/RESEARCH-REPORT-2026-10-ad-production.md`
- Sessions: [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md) · [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
