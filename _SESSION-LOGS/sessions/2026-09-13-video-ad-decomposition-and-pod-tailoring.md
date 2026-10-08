# Handoff — Video-Ad Decomposition + Personalized-Gift POD Tailoring (2026-09-13)

## Where we are
The ad-testing **method** is now complete down to the creative level. Previous sessions built the factor
matrix + staged elimination funnel + 5-tier benchmarks (see `2026-09-07-ads-testing-framework.md`). This
session answered the remaining question the framework couldn't: **what exactly is inside a video ad, which
part do I test first, and how many videos do I need per product** — then re-rated every generic answer for a
*personalized-gift* store instead of generic DTC.

## ✅ DONE (2026-09-13) — 3 commits, all pushed
New file `research/reference/video-ad-decomposition-2026.md` (191 lines) + a new 🎬 block in Group A of
`marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md`. Both synced to Google Docs.

**1. Decomposition (commit `2d29af8`)** — derived from sources, not invented:
- A video ad = **Hook · Concept/Angle · Body (Story+Proof) · Offer · CTA · Format · cross-cutting craft
  (captions / pacing / sound)**. Timeline spine = Hook→Body→CTA; the *test knobs* = the 7 parts.
  (Two lenses reconcile: structural people — Sovran, Barry Hott, Meta — vs analytics taggers — Motion,
  creads.io.) Per-component table: what each drives, sub-types, benchmark, how to test, source URL.
- **Phase-1 test order: Hook ▸ Concept/Angle ▸ Body/hold ▸ CTA.**
- **Hook dominance [DATA]:** Meta/Nielsen — up to **47% of a video campaign's value lands in the first 3s**
  (65% of 3s-watchers reach 10s, 45% reach 30s). Same body cut 3 ways swings hook rate **18%→38%** (AdLibrary).
- **Hook × Hold 2×2 routing:** low/low → replace the concept · high hook/low hold → fix the body only ·
  **low hook/high hold → rebuild just the first ~1.5s (jumps 10–15pt)** · high/high → scale.
- **ANSWER — how many videos for ONE product:** first Phase-1 batch ≈ **9–12 ads = 3–4 distinct concepts
  × 3 hooks each**; 3–5 creatives per ad set (so each exits learning); **~$20–40 per concept** before judging;
  settled days only. **After a winner:** velocity mode = **10–20 hook swaps** on the winning body + repurpose
  the message into **2–3 new formats**; refresh every **~2–3 weeks** (Andromeda fatigue is faster).
- Pure micro-OFAT as a *discovery* method is outdated — Andromeda rewards diversity + volume; OFAT is for
  iterating a proven winner.

**2. + 3. POD tailoring (commits `8ac5525`, `614ddf4`)** — every generic-DTC recommendation re-rated for a
personalized-gift store using a **fallback ladder: EXACT (personalized POD) → WIDER (general POD/merch) →
LAST-RESORT (generic DTC, flagged)**. Every claim carries its rung.
- **Format fit:** personalization-reveal · gift-reaction · occasion/deadline · POV-giving · testimonial · UGC ·
  hyper-personalization (handwriting / kid's drawing / paw print / recipe) = **HIGH**.
  ⚠️ **Founder-story down-rated to LOW, podcast format = SKIP** — both are generic-DTC advice that does not
  transfer; a gift buyer cares about the *recipient's* emotion, not your origin story.
- **Angle library (12)** tailored by recipient + emotion, each rung-labeled (incl. memorial/keepsake = highest
  emotional intensity; "feel truly seen" = the Etsy thesis).
- **Hook library** — concrete first-3s (on-screen text + opening shot) for every angle.
- **Body/Retention:** a gift ad is **NOT** a problem→solution ad. PAS/AIDA fire System-2 (active shoppers only);
  the gift engine is an **emotion arc: anticipation → escalation → payoff (reveal + reaction)**. Proof ranked
  (recipient's genuine reaction = #1). 3 beat-by-beat 15–30s skeletons (reaction-led cold / Thai-ad warm /
  personalization-demo retargeting). **Put the reveal at the MID-point, not the end** — you need runtime after
  it for the reaction + CTA while retention is highest.
- **Offer ranked (gift-native):** order-by-date ▸ free remake guarantee ▸ free personalization (framed as a free
  *gift*, not a discount) ▸ bundles ▸ gift-wrap ▸ **discount last**. Strongest stack =
  order-by-date + free remake + free personalization.
- **CTA:** Meta's *button* is limited to ~17 presets ("Order Now" for deadline, else "Shop Now"); say the gift
  CTA in the on-screen text / VO / end-card — "Make it for them", "See it with your names". Avoid bare
  "Buy Now" for cold gift traffic.
- **Hook tactics tiered for gifts:** Tier 1 = reaction cold-open · personalization-reveal cold-open ·
  occasion/deadline. Tier 3 (down-rank) = stat · contrarian · problem-callout — they fight the emotion arc.

**Honesty (kept explicit in the doc):** there is **no public ad-performance dataset for personalized-gift video
ads.** The EXACT rung is qualitative (Etsy Seller Handbook, live brand positioning, TikTok gift-reaction culture,
creator briefs); every hard number is POD-wide or all-category, i.e. directional. The four tailorings are
**evidence-informed hypotheses, not proven lifts.** Test, don't assume.

## ⭐ NEXT ACTION (next session) — run Phase 1 on NEW products
The method is done and documented. **Stop deepening it, start using it.**
- **Not MJ4U-111 / Grandma's Garden** — that one is already ads-live and has its own separate diagnosis
  (cart→checkout cliff, see `mj4u-111-test-state` memory + GA4/Clarity). We are testing **new products.**
- **Pick the new test product(s) from the Tier-1 backlog** in `products/_registry/product-tracker.csv`
  (111 rows: 36 Tier-1, 109 still `backlog`, only MJ4U-052 live and MJ4U-111 ads-live). Top-scored Tier-1
  candidates: MJ4U-001 pet-portrait phone case (91%) · MJ4U-002 "Legend: Husband-Dad-Grandpa" shirt (91%) ·
  MJ4U-003 pet-memorial suncatcher (91%) · MJ4U-004 "Once a brother" tumbler (91%) ·
  MJ4U-005 bestie trinket dish (91%). Pick by recipient spread + design feasibility, then confirm with user.
- **Then, per chosen product, execute the Phase-1 batch exactly as specced:** 3–4 concepts from the angle
  library × 3 hooks from the hook library ≈ **9–12 videos**, 3–5 per ad set, ~$20–40/concept, LPV objective,
  judge on settled days against the Part-D tiers (hook 25–35%+ · hold 40–50% · link CTR), route via the
  hook×hold 2×2.
- Fill the **Campaign Planner** rows + log outcomes in **Results Log** (Matrix Sheet), and update
  `product-tracker.csv` **and** the mirrored Google Sheet together (Claude is sole writer).
- Production: use the AI film studio pipeline (`/film:new`, `research/reference/ai-film-studio.md`) —
  Skeleton B (Thai-ad) maps to it; Skeletons A/C are cheaper UGC-style cuts.

## Files (source of truth — all in repo, English)
- `research/reference/video-ad-decomposition-2026.md` — **new this session**; decomposition, volume numbers, POD tailoring, honesty notes, source URLs
- `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md` — framework (Group A now carries the 🎬 video block)
- `research/reference/fb-ads-benchmarks-2026-sources.md` — every tier number + citation
- `marketing/facebook-ads/FB-ADS-PLAYBOOK.md` · `AD-KILL-RULES.md`
- `products/_registry/product-tracker.csv` — 111 products, tier + stage + ad_status

## Live artifacts (Drive)
- **Video Decomposition Doc:** https://docs.google.com/document/d/1obX8brgMHnwmV1c4rpeZLkmC-ww7NXA-NC99hO84kaQ/edit
- Framework Doc: https://docs.google.com/document/d/1zND10THgf_VohvNRgRl4hGhsOwPaXVt15eNhNaOdh-I/edit
- Matrix Sheet: https://docs.google.com/spreadsheets/d/1ZNZijKm5PJRkOj91A4DUGhAb-orvDOidyMNP627-k1w/edit
- Benchmarks & Tier Sources: https://docs.google.com/document/d/1peKFvur7Wt05a765WnYV2qlDKYxGJZMnwesVxoExsMQ/edit
- Playbook Doc: https://docs.google.com/document/d/1_5MddywFb-MM5KLrpmMoMSKXh6Qzx_RDdKHOZjCmuxw/edit

## Repo state
Branch `product-research`, working tree clean, `origin/product-research` = `614ddf4` — nothing unpushed.

## Open decisions for user
- **Which new product(s) to run Phase 1 on** (see Tier-1 shortlist above) — needs the user's pick.
- How many products in parallel vs one at a time (budget: ~$20–40/concept × 3–4 concepts ≈ $60–160 per product per Phase-1 round).
- Interactive DB + dashboard (Supabase + Cloudflare) — still deferred until the method is proven on the Sheet.
