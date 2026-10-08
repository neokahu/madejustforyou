# Topic — Phase-1 testing-plan page (Vietnamese, for supervisor approval)

**Status:** live, approval pending.

- **Live:** https://testing-plan-phase-1.namvu47.workers.dev (Cloudflare Worker `testing-plan-phase-1`)
- **Source:** `marketing/facebook-ads/testing-plan-page/index.html` — deploy with `npx wrangler deploy` from that folder.

## Current decisions
- Phase 1 = 3 concepts × 2 hooks × 3 products = **18 ads**, built from the 12-field brief (section 05).
- Section 04 advance/fix/park table read across a concept's 6 ads; **Phase 1 kills nothing**.
- Naming: `Phase` (budget tier) · `Vòng` (one test) · `Cổng` (pass/fail). "Phase 1.5" = `Cổng Ý định`.
- Run order: Vòng Hook before Vòng Craft. The 9 in section 06 are *cách mở* (tactics), not hooks.
- CTA: **"Make one that's only theirs"** (recipient-neutral).
- Hook must qualify — first 3s reveal what gift is sold (the MJ4U-111 fix). Log LPV→ATC from day one.
- Page audience = supervisor: no meta-commentary (memory `page-audience-is-supervisor`). VI language rules in sessions/2026-09-23.

## Open items
- Get the page approved; redeploy with corrected blanket row.
- Two stale Workers still live: `testing-plan`, `mj4u-test-protocol` — delete? (asked twice, unanswered).
- Phase 2 needs its own plan page.

## Detail
- `marketing/facebook-ads/PHASE1-TOURNAMENT-3-products.md` (+ `-vi.md`)
- Session: [2026-09-23](../../sessions/2026-09-23-phase1-testing-plan-page.md)
