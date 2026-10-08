# Topic — Ad-testing framework + video-ad decomposition

**Status:** method complete — "stop deepening it, start using it".

## Current decisions
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
