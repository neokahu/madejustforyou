# GPD02 — Grandma's Garden / Little Birds · Build Status Checklist

Concept: Roster mechanic (one motif per grandchild), two metaphors A/B'd:
**2A Garden** (birth flower) · **2B Little Birds** (bird on a branch). Products: sweatshirt (AOV) +
**lamp** (Garden, continuous wrap 31×5 cm). Last updated **2026-07-31**.

Legend: ✅ done · 🟡 in progress / partial · ⬜ not started · ❓ open question

---

## Concept & specs
- ✅ Concept locked + scored (composite 4.15) — [`brief.md`](brief.md)
- ✅ **2B bird layout spec** (per-count 1–10, center-balanced, ~110 layers) — [`2B-bird-layout-spec.md`](2B-bird-layout-spec.md)
- ✅ **2B bird-library asset brief** + **validated (v3) Nano-Banana prompts** — [`2B-bird-library.md`](2B-bird-library.md)
- ✅ **2A flower-library asset brief** (12 birth flowers, mirrors 2B) — [`2A-flower-library.md`](2A-flower-library.md)
- ✅ **Lamp print spec recorded** — continuous wrap 31×5 cm → 3661×591 px @ 300 DPI (2A brief §0)
- ✅ Design decisions locked: 3/4 front-facing birds · plump owl-on-nest grandma bird (no props) · full 1–10 · names on

## Asset generation
- ✅ **8 birds + small owl + grandma owl + branch generated & prompt-validated** (10 raw, 2048 px) — [`bird-gen/`](bird-gen/)
  - keepers: robin/small-owl/grandma-owl/branch = v1; bluebird/cardinal/chickadee/sparrow/dove/goldfinch = v3
- 🟡 **Sparrow v3 = JPEG (no alpha)** → re-run once for a transparent PNG
- ⬜ Background-remove all 10 keepers (`recraft_remove_background`)
- ⬜ Trim + place each on 520×520 (720 grandma owl) with feet/nest on bottom-center anchor
- ⬜ Normalize optical scale across the flock
- ⬜ **12 flower assets** — not yet generated (brief + prompts ready)
- ⬜ Grandma-bloom anchor + soil/garden-bed line (2A) — not generated

## Teeinblue build
- ⬜ Upload birds as Clipart Category "Birds" (set reposition on first → all inherit)
- ⬜ Upload flowers as Clipart Category "Birth Flowers" (labeled by month)
- ⬜ Additional Option "Number of grandkids" 1–10 (drives conditional layouts)
- ⬜ Build N=1–5 layouts (single row) → validate → N=6–10 (two branches) [2B]
- ⬜ Build single-row garden-border layout for the **lamp** (2A, continuous wrap)
- ⬜ Nickname → title conditional + name text layers (Caveat, auto-scale)

## Test / validation
- ⬜ Mock N=3 (Ava, Liam, Noah) for both 2A + 2B — Tier-1 post
- ⬜ **Lamp name-legibility test** — worst case 10 flowers across 31 cm (~3 cm each); may cap grandkid count
- ⬜ Tier-1 organic A/B: 2A vs 2B, watch saves/comments 48–72h
- ⬜ A/B parity check (same product/fonts/palette/positions — 2A brief §7)

## Open questions ❓
- ❓ Lamp max grandkid count (pending legibility test) — does it match the sweatshirt's 1–10 or cap lower?
- ❓ Supplier base cost / target retail / margin for lamp + sweatshirt (blocks the ≥3× margin gate)
- ❓ Lamp color profile (sRGB vs CMYK) + bleed requirement — confirm with supplier

---

## Broader research thread (from session handoff — not GPD02 assets)
- ⬜ **Google Trends pull** (5yr+90d) on Tier-1 mechanics + "grandparents day gifts" (A3/B3) — handoff Next #1
- ⬜ **Margin ≥3× GATE + decision-band cut-scores** from real supplier costs + sales — handoff Next #3
- ✅ Bird-library asset brief + prompts (handoff Next #2) — **this session**

> Full research context: [`../../../_SESSION-LOGS/2026-07-31-research-competitor-ad-scoring-gpd.md`](../../../../_SESSION-LOGS/2026-07-31-research-competitor-ad-scoring-gpd.md)
