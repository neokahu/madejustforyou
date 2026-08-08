---
name: film:new
description: Produce a MadeJustForYou emotional short-film ad, step-gated, via the film studio crew
argument-hint: "[product id or name]"
---

<objective>
Produce a ~35s emotional short-film ad (Thai-ad style) for a product, plus a 15s FB cut,
by running the phased studio pipeline step-gated. Delegates to the film crew and keeps a
live credit/time budget. Product appears only as the emotional payoff.
</objective>

<context>
Target product: $ARGUMENTS
Source of truth: @research/reference/ai-film-studio.md
Kit + standard folder layout: products/_templates/film-studio/
</context>

<process>
1. Launch the **film-producer** agent to own the run. It must:
   - P0: confirm product, core emotion, recipient, scope, **budget cap** with the user.
   - Copy the kit: `cp -r products/_templates/film-studio products/<ID>/ads/film`; init `production.md`.
   - P1: run **film-screenwriter** → `ads/film/script.md`. **GATE: user approves the script.**
   - P2: run **film-art-continuity** to build+host the character turntable AND scale-anchored product turntable; **film-qa** verifies. **HARD GATE: user approves refs before any scene.**
   - P3: run **film-director** to batch-generate scenes from the locked refs (parallel); **film-qa** verifies each; reshoot only failures.
   - P4: run **film-editor** to assemble (grade, captions, crossfades, music, logo end card) → `out/`.
   - P5: cut the 15s version + variants; update the product tracker `ad_status`; report spend vs budget.
2. Enforce: turntables gated BEFORE shooting; verify every shot; ~$0.70–1.00/clip; STANDARD folders (refs→shots→build→out); never a lonely giftee.
3. Pause at each GATE for user sign-off. Do not burn credits speculatively.
</process>
