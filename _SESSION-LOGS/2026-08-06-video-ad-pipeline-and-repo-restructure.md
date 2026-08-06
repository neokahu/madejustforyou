# Session Handoff — 2026-08-06 · Video-ad pipeline, Kie.ai MCP, repo restructure

Big session. Read this before resuming.

## What was achieved
1. **Clone-shortlist finalized** (`products/_registry/` ← was the July sprint work):
   - Fixed corrupted row 1; recomputed `active_creatives_US` per-landing-URL.
   - **Removed `distinct_sellers`** (user directive: seller-count is meaningless — copycats run *similar-not-exact* concepts; validate on **longevity**, not seller count).
   - **Deep-crawled Wander Prints** → 85 evergreen products; scored + tiered all into one shortlist (**110 rows**). Finding: WP is a *broad long-tail catalog* archetype (median 816d longevity, low creatives/product) — see `research/sprints/2026-07-competitor-ad-scoring/wanderprints-deep-crawl.md`.
   - Added **recipient** category to every product.
2. **Product ops tracker** built: `products/_registry/product-tracker.csv` + **Google Sheet mirror** (ID `1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE`). Claude is sole writer; re-push via `update_drive_file` from the attachments staging copy. See [[product-tracker-and-sheet-sync]] memory.
3. **First live product tracked: MJP-111** — Grandma's Garden candle warmer. Real live URL = `.../grandmas-garden-love-grows-here-personalized-candle-warmer-49` (the one first given 404s). Clone of Macorner, scored 80% Evergreen T2, $49.95. Competitor ad is LIVE (copy "love growing at home").
4. **AI video-ad research → 2 playbooks** in `research/reference/`: `ai-emotional-video-ad-playbook.md` (strategy) + `image-to-video-prompt-method.md` (prompt craft). Pipeline = product image → i2v clips (Kling) → HyperFrames assemble → MP4. No CapCut (no MCP; manual only). Per-product, product-direct; character-build only if a recurring person.
5. **Fixed + extended the Kie.ai MCP** (`~/Desktop/projects/kie-ai-mcp`, pushed to its own GitHub): Kling 2.6 fix (was missing `image_urls[]`+`sound`), added **Kling 3.0 Turbo** (`kling_v3_turbo_video`), **Seedance 2.0** (`seedance_2_video`), **Veo 3.1** (`veo31_video`, flat body /veo/generate). Default model = **Kling 3.0 Turbo**.
6. **Proof clip generated** via AtlasCloud (Kie.ai MCP was broken at the time) from the store image — confirms pipeline works. Atlas Kling = ~$0.30/clip (pricey at scale → use Kie.ai).
7. **Repo restructured** into scalable domains: `research/ · products/ · library/ · marketing/` (+ `_SESSION-LOGS/`). Merged `handoffs/`→`_SESSION-LOGS/`; removed obsolete `design_handoff_*`. Future slots documented: `suppliers/ ops/ data/`.

## ⚠️ BLOCKER for next session
**The fixed Kie.ai MCP tools (Kling 3.0 Turbo etc.) need a SESSION RESTART to load.** The running MCP had the old code all session. After restart, the new tools go live.

## Next steps
1. **Restart the session** (loads the fixed Kie.ai MCP tools).
2. Drop the product image **with the personalized names** into `products/MJP-111-grandmas-garden-candle-warmer/ads/source-images/`.
3. Generate real clips: `kling_v3_turbo_video` (image → i2v; jpg/png only — use weserv proxy for webp). Save to `ads/clips/`. Ad copy ready in `ads/ad-copy.md`.
4. Assemble in **HyperFrames** (name-reveal title card + clips + captions + ElevenLabs VO + music) → `ads/final/`.
5. Update tracker: MJP-111 `ad_status` when ads go live.

## Key facts / gotchas
- Video-gen models need **jpg/png**, not webp → `https://images.weserv.nl/?url=ssl:<cdn-url>&output=jpg&w=1080`.
- Meta Ad Library search matches **ad text**, not product words (that's why product-keyword ad links returned nothing).
- Binaries (img/video) are **Drive-synced, gitignored**; only text committed.
- This is the **docs repo** — merging product-research→main is safe, **NOT** a store deploy (that's the separate theme repo). [[repo-split-theme-vs-docs]]
