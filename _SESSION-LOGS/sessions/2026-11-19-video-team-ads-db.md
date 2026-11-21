# 2026-11-18/19 — Video team, frameworks, ads database, Hook Lab

## Built (all committed on product-research)
- **Video team** (`research/reference/video-team/README.md`): 00A concept ideator · 00B concept critic · 00C concept selector · GATE 0 (user) ·
  01 hook ideator · 02 hook critic · 03 hook selector · 04 script editor · 05 visual director · 06 editor · 07 QA. Agents `.claude/agents/vt-*`,
  run `/video:new`. Tool-agnostic; tool prompt craft lives in `research/reference/video-team/adapters/`.
- **Frameworks**: `hook-framework.md` (format F1–F15 × trigger T1–T10, fake-reality rules) and `concept-framework.md` (core AN/BY/RC×OC,
  execution ST/PV/PF/PX/RV/EM, hook elements, testing ladder R0–R4). All codes in `marketing/facebook-ads/_ledgers/codebook.csv` (137).
- **Naming convention** (README §4a): ad key `MJ4U-003_R0_K01X1-H07_E0_v01` in the Meta ad name; files add `_916`/`_45` before the version.
- **Ads database**: Supabase `mj4u-ads` (`marketing/facebook-ads/db/README.md`). Daily 15:00 (=00:00 PST) launchd sync stores all 84 Meta
  insight fields raw + typed columns; `db_sync.py rebuild` re-derives from raw; `sync_runs` heartbeat. Only registered (framework) ads are stored.
- **Hook Lab**: https://mj4u-hook-lab.vercel.app (email OTP; viewers in `dashboard_viewers`). Groups results by any code, aliasing warning,
  real-vs-noise check, ad previews from Meta.
- **Fixed**: Meta action aliases were summed (ATC over-counted 3–5×) in db_sync and the engine's `rules.py`.
- **User rulings**: no AI-performer disclosure; relationship hooks ("Your granddaughter…") allowed; music = AI-generated (confirm paid plan);
  old MJ4U-111 ads and the hand-made suncatcher Phase 1 records removed (archived: `_ledgers/archive/2026-11-suncatcher-pre-pipeline/`).

## RESUME: rerun the suncatcher through the full pipeline (fresh session)
Run `/video:new MJ4U-003` starting at **0b Concepts (00A)**. Product = MJ4U-003 (pet memorial suncatcher).
- Inputs ready: product photos/lettering + 4K panel stills, approved AI music, brand kit (see archived README + `marketing/facebook-ads/suncatcher-phase1/`).
  Old renders/shots on Drive may be **reused as references**, but concepts/hooks/scripts must come from the roles.
- **Plan-page conflict to raise at GATE 0**: the plan page (test authority) still locks concepts 01/02/06 × hooks H1/H2. The new slate is
  approved by the user at Gate 0, then the plan page is updated. Do not restructure silently.
- Budget numbers: hook-rate read ≈ $11 (big diff) – $44 (small diff) per arm at CPM $13 (ad-science §5b).

## Later 2026-11-19/20 — test plan, impact research
- **Test plan deck**: Claude https://claude.ai/artifact/DnSw4H317gkQqnZHGHqhet · Cloudflare (public, noindex) https://mj4u-test-plan.namvu47.workers.dev
  (+ `/codes`, strong-for-gifts codes highlighted). Source: `marketing/facebook-ads/test-plan-deck/` (source slides + public/index.html).
  Deck currently shows the "focused plan" (R0 5×2, R1 hook grid, R2 reason, R3 storyline, ~$965/product, ~$4.8k for 5) — SUPERSEDED by the impact ranking below.
- **Impact ranking (final)**: `research/reference/video-team/impact-ranking.md` (20 docs read in full, 24 searches, 21 primary sources).
  Test first: concept/angle → hook (first 1–3s) → person/relationship in frame 1 → personalization timing. Fix: product visible from 0s,
  length 15–25s, 9:16 + 4:5, captions, sound, CTA/end card, **offer (identical in every cell)**. Late-reveal house style contradicts evidence.
- User directives (2026-11-19, strongly stated): test only what has the most impact; caption length/timing, sound, music are minor → FIXED,
  never tested. Concepts get breadth (R0 = 5 concepts × 2 hooks). Read ALL research before changing the plan.

## RESUME HERE (in order)
1. **Rebuild the test plan + deck from impact-ranking.md**: rounds R0 concepts 5×2 ($200) · R1 opening 2×2 (person in frame 1 × personalization
   timing, $170) · R2 reason-to-buy 4 proof types ($170) · R3 break-even check top-2 ads (~$425; stop at 3× break-even CPA with 0 purchases).
   **Check R3 costs: the ranking shows $317 at $30 < $425 at $25 ("capped") — inconsistent, recompute.** Update both deck copies
   (claude.ai artifact via its url + Cloudflare `npx wrangler@4 deploy` in test-plan-deck/).
2. **Align the system**: concept-framework.md §6 ladder + README; DB `cells.round_type` check (currently R0–R4; new rounds must fit);
   codebook/house standards for FIX items; `/video:new` + vt-00c selector (R0 size 5×2, axes); coverage tracker in Hook Lab (tested dims only).
3. **Run `/video:new MJ4U-003`** from 00A (concepts) → Gate 0 (user; plan page then updated). Naming: `MJ4U-003_R0_K01X1-H07_E0_v01`.

## DECIDED 2026-11-21 — DEEP PLAN (replaces the 4-round impact plan as the plan to build)
User: "I need more detail test, with more elements in hooks and concepts, since those are 2 most influential factors."
Everything except hooks + concepts stays FIXED (captions, sound/music, length, VO, CTA/end card, offer identical in every cell).
| Round | Breaks down | Design | Ads | Max @$25 |
|---|---|---|---|---|
| C0 Concept discovery | whole concepts | 6 concepts × 2 hooks, ~800 imp/ad (large gaps) | 12 | $240 |
| C1 Concept core | angle × buyer role × occasion | 8-ad grid, 2 levels each, ~1,700 imp/ad | 8 | $340 |
| C2 Concept execution | structure, POV, tone, reveal timing | 8-ad fractional grid | 8 | $340 |
| H1 Hook opening | person in frame 1, personalization timing, frame-1 subject, onset | 8-ad fractional grid | 8 | $340 |
| H2 Hook type | hook format × trigger (best 2 of each from C0) | 4-ad grid | 4 | $170 |
| B Break-even check | top 2 ads vs break-even CPA (not a creative test) | stop at 3× break-even CPA with 0 purchases | 2 | ~$425 |
Per product: 42 ads, 13 hook+concept elements, ≈ $1,855 max @$25 ($1,485 @$20, $2,225 @$30); typical ≈ 80%. 5 products ≈ $9,300 max (~$7,500 typical).
**Run order**: C0 alone → (H1 ∥ C1) → (C2 ∥ H2) → B. Rounds in parallel only if they change different parts of the ad (H1 and H2 never together);
own ad sets, equal budgets, same launch day. ~3–5 days/round (~$14/ad/day) → ~3–4 weeks/product; products overlap → 5 products in ~2–3 months.
Production: C0 builds 6 concepts; H1/H2 are hook swaps on existing footage; C1/C2 need new scenes (start once C0 decides).
Grids measure main effects only (follow-up test if an interaction is suspected); keep ~1,700 imp per grid ad; sales = guardrail only.

**RESUME step 1 now means**: rebuild the deck + testing plan around THIS deep plan (keep impact-ranking.md as the evidence base);
step 2: framework §6 ladder, DB round codes (C0/C1/C2/H1/H2/B instead of R0–R4), vt-00c selector, `/video:new`, coverage tracker; step 3: `/video:new MJ4U-003`.
