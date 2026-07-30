# Session Handoff — 2026-07-31 · Theme: home page → design handoff

**This log = the Shopify theme thread only** (research work is in a separate log same date). **Rule: theme code lives in the SEPARATE repo; all logs/docs stay here in the main repo — never write to the theme repo.** See `THEME-REPO.md` + memory `repo-split-theme-vs-docs`.

## Repo split established
- Removed the stale `theme_export__…16JUL2026` snapshot (482 files) from this main repo. **Shopify theme code now lives only in** `~/Desktop/projects/madejustforyou-theme/shopify-theme-1/` — GitHub `Minh-Quy-K/shopify-theme-1`, branch `main`, synced from Shopify. Pointer: `THEME-REPO.md`.
- Installed **Shopify CLI 4.5.2**. Local dev: `cd` theme repo → `shopify theme dev --store=madejustforyou-store.myshopify.com`. Added `.gitignore` (`.shopify/`) to the theme repo. **`shopify theme pull --live`** syncs live composition into git before editing (git's index.json/settings can be behind live).

## Achieved — home page reworked to `design_handoff_home/` (Horizon 4.1.1, `mc-*` sections)
Built + verified via `theme dev`, then **merged to `main` and deployed to the live theme; branch `design-handoff-home` deleted.**
- **Type fixes** (`mc-homepage.css`): eyebrows → clay `#C15F3C`, 26px/**700** (fixed Caveat weight-synthesis "blur"), hero eyebrow 30px; hero H1 → **italic/800/70px**; section headings → 36px/700/-0.015em; body → stone.
- **"Recipient" clay accent** — added a highlight-word setting in `mc-image-link-grid` that wraps the word in a clay span.
- **Product cards** (`mc-product-showcase.css` + `mc-homepage.css`): price → **Playfair bold 17px clay** (was Caveat italic hot-pink); badges (Sold out/Sale/Bestseller) → **DM Sans upright**, clay/stone (was Caveat italic hot-pink); button radius 14 + clay.
- **New `mc-email-signup` section** (rose `#F7DCD3` panel, Caveat eyebrow, Playfair heading, white pill input + dark Save button, shipping-policy link) — placed at the **end** of the home. Native Shopify `{% form 'customer' %}` → captures subscribers to Admin→Customers, **no app needed**.
- **Uniform white section backgrounds** (killed the cream/white alternation).
- **Tighter section spacing** (`.mc-home-section` padding → ~30–46px).
- **Country/currency picker**: replaced the globe dropdown with a **circular flag button → modal** (country select + Save & Continue + shipping link), matching the provided screenshots. Flag via flagcdn by `localization.country`. Dropped the ">1 country" guard so the flag always shows.

## Learnt / decided
- **"Sold out" on every product = data, not code.** The card correctly reads `product.available == false`. Fix in admin (see below).
- **Country/currency = Shopify Markets, not theme.** New Markets UI has no "primary market" toggle; unmatched visitors (e.g. Singapore→Austria) fall to the **Store default**. Theme can't override server-side geo.
- **Section composition (`index.json`) is admin-managed** — was edited on-branch only for preview; kept edits to `mc-*.css`/`.liquid`.

## Open — ADMIN steps (not code) needed for full effect
1. **Settings → Markets:** set **Store default = United States / USD** (fixes non-US visitors defaulting to Austria).
2. **Products → Inventory:** check **"Continue selling when out of stock"** (or untrack qty) → clears the "Sold out" badges (POD standard).
3. **Fonts:** confirm hero **Playfair 800** renders true (not faux) — theme loads `Playfair:…800`. If faux, add the weight in theme settings.

## Deploy state
- Live theme `shopify-theme-1/main` HEAD **993e8f8** (pushed; Shopify syncing). Branch deleted (local+remote). Verify on live store after sync.
- Commits: **no Claude co-author** (user preference, saved to memory).
