# Session Logs — INDEX (read this first)

**How to use:** read only this file at session start. Then follow a path below — a topic README for the
current state of an area, a session log for full detail. Never load every log.

```
_SESSION-LOGS/
  INDEX.md                      ← you are here (resume block + map, pointers only)
  topics/<topic>/README.md      ← per-topic summary: decisions, evidence pointers, open items
  sessions/<YYYY-MM-DD-slug>.md ← full detailed per-session logs
```

## ⏸ IN PROGRESS — RESUME HERE  (as of 2026-11-24)

1. **MJ4U-133 ornament C0** (`marketing/facebook-ads/MJ4U-133-C0/`): Gate 0 approved, renders done, 12 hooks selected; scripts (04) in progress →
   council → **GATE A (user)** → 05 visuals → build → QA → launch ≈ Nov 30 (Christmas cutoff Dec 11).
2. Support-ticket tooling ready (2026-11-24): `mj4u-orders` installed with customer-data access (orders, fulfillment, email readable) + Freshdesk API verified (key name in keys file is `FRESKDESK_API_KEYS`, typo). Next: build ticket → order-status draft flow in the `customer-support` worktree.
Full detail: `sessions/2026-11-23-mj4u-133-c0-shopify-ids.md` (RESUME HERE). Deep-plan background: `sessions/2026-11-19-video-team-ads-db.md`.

## Current state by area

| Area | State (1–2 lines) |
|---|---|
| Suncatcher "Alex" | ✅ 6 plan ads built + gated; awaiting review + upload |
| Blanket MJ4U-012 | D1–D5 passed; no scripts, no character sets; child/adult casting open |
| MJ4U-111 candle warmer | Ads live since 2026-08-09; checkout verified working + real orders (2026-10-08) |
| Platforms | ⚠️ **kie.ai out of credits** (2026-10-08) → images via AtlasCloud `google/nano-banana-pro/edit` ($0.14). Video AtlasCloud. TopView dropped. AtlasCloud ~$41 |
| Prompt method | Seedance 2.0 two-shot recipe settled; prompt-guard hook enforces it |
| Testing plan page | Live, approval pending; blanket row fix not redeployed |
| Ad-testing method | Deep plan (C0→H1+C1→C2+H2→B) built into the system 2026-11-23; first run = MJ4U-133 C0 |
| Shopify catalog | All 43 products tagged MJ4U-NNN (2026-11-23); apps mj4u-catalog + mj4u-orders |
| Teeinblue / pajama | Base PSD done; campaign build + anchors + Route A/B open |
| Theme | Home rework live; 3 admin items open |

## Pending user decisions
- Suncatcher: watch 6 ads · approve upload
- Child vs adult granddaughter · Approve testing-plan page
- Delete stale Workers `testing-plan`, `mj4u-test-protocol`? · Cancel TopView monthly plan?
- Teeinblue title render Route A vs B · Which new Tier-1 products for Phase 1

## Topic map

| Topic | README |
|---|---|
| Video prompting (Seedance) | [topics/video-prompting](topics/video-prompting/README.md) |
| Image prompting | [topics/image-prompting](topics/image-prompting/README.md) |
| Product text fidelity | [topics/product-text-fidelity](topics/product-text-fidelity/README.md) |
| Platforms & cost | [topics/platforms-and-cost](topics/platforms-and-cost/README.md) |
| Script method | [topics/script-method](topics/script-method/README.md) |
| Character references | [topics/character-references](topics/character-references/README.md) |
| Prompt-guard hook | [topics/prompt-guard-hook](topics/prompt-guard-hook/README.md) |
| Suncatcher build | [topics/suncatcher-build](topics/suncatcher-build/README.md) |
| Blanket build | [topics/blanket-build](topics/blanket-build/README.md) |
| Testing-plan page | [topics/testing-plan-page](topics/testing-plan-page/README.md) |
| Translation tooling | [topics/translation-tooling](topics/translation-tooling/README.md) |
| Ad-testing framework | [topics/ad-testing-framework](topics/ad-testing-framework/README.md) |
| FB-ads automation + MJ4U-111 | [topics/fb-ads-mj4u-111](topics/fb-ads-mj4u-111/README.md) |
| AI film studio (demoted) | [topics/ai-film-studio](topics/ai-film-studio/README.md) |
| Competitor research | [topics/competitor-research](topics/competitor-research/README.md) |
| Idea research + GPD | [topics/idea-research-gpd](topics/idea-research-gpd/README.md) |
| Teeinblue + pajama | [topics/teeinblue-and-pajama](topics/teeinblue-and-pajama/README.md) |
| Shopify theme | [topics/shopify-theme](topics/shopify-theme/README.md) |

## Session map (newest first)

| Date | Log | Topics |
|---|---|---|
| 2026-10-08 | [suncatcher-ads-built](sessions/2026-10-08b-suncatcher-ads-built.md) | suncatcher, character-refs, script-method |
| 2026-10-08 | [research-consolidated-handoff](sessions/2026-10-08-research-consolidated-handoff.md) | platforms, character-refs, script-method |
| 2026-09-26 | [testing-complete-both-products](sessions/2026-09-26-testing-complete-both-products.md) | suncatcher, blanket, text-fidelity, prompt-guard |
| 2026-09-25 | [topview-evaluated-seedance-method](sessions/2026-09-25-topview-evaluated-seedance-method.md) | video-prompting, platforms |
| 2026-09-23 | [phase1-testing-plan-page](sessions/2026-09-23-phase1-testing-plan-page.md) | testing-plan-page, translation |
| 2026-09-13 | [video-ad-decomposition-and-pod-tailoring](sessions/2026-09-13-video-ad-decomposition-and-pod-tailoring.md) | ad-testing-framework |
| 2026-09-07 | [ads-testing-framework](sessions/2026-09-07-ads-testing-framework.md) | ad-testing-framework |
| 2026-08-14 | [cro-diagnosis-speed-ruled-out-efficiency-kill](sessions/2026-08-14-cro-diagnosis-speed-ruled-out-efficiency-kill.md) | fb-ads-mj4u-111 |
| 2026-08-09 | [fb-ads-automation-and-mj4u111-launch](sessions/2026-08-09-fb-ads-automation-and-mj4u111-launch.md) | fb-ads-mj4u-111 |
| 2026-08-08 | [ai-film-studio-and-mjp111](sessions/2026-08-08-ai-film-studio-and-mjp111.md) | ai-film-studio |
| 2026-08-06 | [video-ad-pipeline-and-repo-restructure](sessions/2026-08-06-video-ad-pipeline-and-repo-restructure.md) | competitor-research, platforms |
| 2026-08-02 | [competitor-ad-links-csv-PROBLEMS-and-data](sessions/2026-08-02-competitor-ad-links-csv-PROBLEMS-and-data.md) | competitor-research |
| 2026-07-31 | [research-competitor-ad-scoring-gpd](sessions/2026-07-31-research-competitor-ad-scoring-gpd.md) | competitor-research, idea-research-gpd |
| 2026-07-31 | [theme-home-design-handoff](sessions/2026-07-31-theme-home-design-handoff.md) | shopify-theme |
| 2026-07-28 | [winninghunter-ad-scoring-handoff](sessions/2026-07-28-winninghunter-ad-scoring-handoff.md) | competitor-research, teeinblue |
| 2026-07-26 | [teeinblue-asset-system-handoff](sessions/2026-07-26-teeinblue-asset-system-handoff.md) | teeinblue-and-pajama |
| 2026-07-20 | [pajama-clone-handoff](sessions/2026-07-20-pajama-clone-handoff.md) | teeinblue-and-pajama |
| 2026-07-10 | [session-01-handoff](sessions/2026-07-10-session-01-handoff.md) | idea-research-gpd |

## Handoff rule (every session)
1. Write the full detailed log to `sessions/<YYYY-MM-DD-slug>.md`.
2. Update/create the touched `topics/<topic>/README.md` (≤ ~60 lines, pointers to detail).
3. Update this INDEX: resume block, state table, decisions, both maps. **Never pile detail in here.**
