# 2026-11-21→24 — Deep plan system, Shopify IDs + apps, MJ4U-133 C0 run (to Gate A)

## Done
- **Step 1 — deck** rebuilt on the deep plan (Cloudflare only; claude.ai artifact deleted by user) + run-order + 2 glossary slides. User ruling: RV only in H1, proof type in C2.
- **Step 2 — system aligned** (commit 4474156): framework §6 rounds C0/H1/C1/C2/H2/B(+S), grid layouts; DB migration 013 (applied); ad-key parser + tests;
  agent round modes; `/video:new` round table; Hook Lab coverage panel **built but NOT deployed** (Vercel deploy blocked → user runs
  `cd marketing/facebook-ads/hook-lab-web && vercel deploy --prod`).
- **Shopify IDs:** app `mj4u-catalog` (read/write products, project `~/Desktop/projects/mj4u-catalog`, creds in `~/.global-keys.env`, client-credentials token).
  All 43 store products tagged `MJ4U-NNN` (user-approved map `products/_registry/product-ids.json`; raw pull `shopify-products.json`;
  script `scripts/shopify_catalog.py pull|tag [--apply]`). Tracker CSV + Sheet updated (+ `shopify_product_id` column). New numbers MJ4U-113…139.
- **Orders app** `mj4u-orders` (read_orders, read_customers; project `~/Desktop/projects/mj4u-orders`; creds `SHOPIFY_ORDERS_*`) created + deployed.
  **Open (user):** install link `https://admin.shopify.com/store/madejustforyou-store/oauth/install?client_id=bddb3bd7c4a1d86938998fb929ef1839`,
  request Protected customer data (Dev Dashboard → API access), give Freshdesk domain + `FRESHDESK_API_KEY`. Build the ticket flow in the `customer-support` worktree, drafts only.
- **MJ4U-133 (3D Family Wood Ornament, Shopify 9776740696421)** — `/video:new` C0 run, folder `marketing/facebook-ads/MJ4U-133-C0/`:
  - BRIEF (user): C0 only this season then scale to the Dec 11 cutoff · 20s · no offer · $240 media + $300 production · launch ≈ Nov 30.
  - CRITERIA.md locked (72 criteria). Concepts: 00A 13 cards → 00B 3-judge panel (`00B-scores.md`) → 00C → **GATE 0 approved** (`concepts/GATE0.md`):
    K10 · K13 · K04 · K06 (rebuilt "First Christmas as four", re-scored 75) · K02 · K01 (control).
  - **Renders** from the live personalizer → SVG download → transparent PNG 3185×3000 (`RENDERS.md`; media `products/MJ4U-133-family-wood-ornament/ads/renders/`).
    Method: page JS helper (`__mj`) sets the family; `__mj.save()` downloads the SVG; scratchpad script renders it with headless Chrome + Google fonts (Chewy).
  - Hooks: 01 (60 kept) → 02 three blind judges (`hooks/02-scores.md`; judge B re-run after an output-limit crash; packets still leaked ideators' self-verdicts — strip next time)
    → **03 selection** `hooks/03-selection.md` (12 hooks + reserves; 8 fixes for 04/05).
  - **04 scripts done 2026-11-24**: `MJ4U-133-C0/{K10,K13,K04,K06,K02,K01}/script.md` (20s; hook 0–2.0s, hook caption to 3.2s; end card 17.5–20.0s; one ad copy per concept). Open for the user before Gate A: shared end-card plate; K13 H17 10-word caption vs 2.5 words/s; K13 ending reuses the bed; K01 seven-person shot must read.

## RESUME HERE
1. Collect the 6 scripts; `/llm-council` per script (craft only); then **GATE A** (user approves hooks + scripts).
2. 05 visual director per concept (shot list + reference sheet) → GATE B (07 shot mode + user) → generation within the $300 cap → GATE C → 06 edit → 07 → GATE D → upload by ~Nov 30.
3. User items: Hook Lab deploy; orders-app install + data access + Freshdesk key; music paid-plan evidence (CRITERIA E65 is S1 without it).
