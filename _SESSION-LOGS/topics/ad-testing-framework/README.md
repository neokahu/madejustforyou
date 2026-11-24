# Topic — Ad-testing framework + video-ad decomposition

**Status:** method complete — "stop deepening it, start using it".

## Current decisions
- **2026-11-21 deep plan supersedes the Phase-1 test order below:** only hooks + concepts are tested, in rounds
  C0 → (H1 ∥ C1) → (C2 ∥ H2) → B, 42 ads ≈ $1,855/product max at CPM $25. Rules: `research/reference/video-team/concept-framework.md` §6.
  Live: deck https://mj4u-test-plan.namvu47.workers.dev · DB migration `013_deep_plan_rounds` on Supabase mj4u-ads (round codes) ·
  Hook Lab https://mj4u-hook-lab.vercel.app (coverage panel live 2026-11-24).
- **Design = the test unit.** Matrix 1 Design Profile (fixed) + Matrix 2 test axes M/AUD/A/O/R/D/F.
- Video ad = Hook · Concept/Angle · Body · Offer · CTA · Format · craft. **Phase-1 test order: Hook ▸ Concept ▸ Body ▸ CTA.**
- Hook × Hold 2×2 routing; up to 47% of value in first 3s (Meta/Nielsen).
- Per product, first batch ≈ 9–12 ads (3–4 concepts × 3 hooks), ~$20–40/concept, settled days only.
- POD tailoring via fallback ladder EXACT → WIDER → LAST-RESORT; founder-story LOW, podcast SKIP; offer stack = order-by-date + free remake + free personalization; discount last.
- No public ad-performance dataset exists for personalized-gift video — tailorings are hypotheses.

## Key thresholds (Part D)
Stage 1 hook <18% kill / >28% advance; link CTR >4% (Gifts). Stage 2 ATC <2% kill / >7.5% advance. Stage 3 click→purchase <0.65% kill / >3.2% advance.

## Detail
- `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md` · `MATRIX-CORRECTION-design-unit.md` · `FB-ADS-PLAYBOOK.md` · `AD-KILL-RULES.md`
- `research/reference/video-ad-decomposition-2026.md` (+ `-vi.md`) · `fb-ads-benchmarks-2026-sources.md`
- Matrix Sheet `1ZNZijKm5PJRkOj91A4DUGhAb-orvDOidyMNP627-k1w` · Framework Doc `1zND10THgf_VohvNRgRl4hGhsOwPaXVt15eNhNaOdh-I` · Decomposition Doc `1obX8brgMHnwmV1c4rpeZLkmC-ww7NXA-NC99hO84kaQ`
- Sessions: [2026-09-07](../../sessions/2026-09-07-ads-testing-framework.md) · [2026-09-13](../../sessions/2026-09-13-video-ad-decomposition-and-pod-tailoring.md)
