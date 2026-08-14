# THEME HANDOFF #01 — Mobile page speed (Grandma's Garden candle warmer)

**For:** whoever works the theme repo (`shopify-theme-1`). Self-contained — no prior chat context needed.
**Goal:** cut mobile load time on the product page so cold ad traffic stops bouncing before it renders.
**Page:** https://madejustforyou.net/products/grandmas-garden-love-grows-here-personalized-candle-warmer-49

---

## Why this matters (the business case)
- Facebook ad traffic to this page is **~100% mobile**, and it **bounces 83–100% within <10 seconds** (GA4, Aug 9–12): ~1 page/session, **1 add-to-cart in 33 sessions, 0 purchases.**
- We need on-site conversion rate to climb from ~0% toward ~4% for the ads to be viable. **Load speed is the first blocker.**

## Measured baseline — Lighthouse MOBILE, 2026-08-13 (Browserless)
**Performance score: 30/100.**

| Metric | Measured | Target |
|---|--:|--:|
| Largest Contentful Paint (LCP) | **17.1 s** | < 2.5 s |
| Time to Interactive | **25.8 s** | < 5 s |
| Total Blocking Time (TBT) | **4,470 ms** | < 500 ms |
| Speed Index | 9.0 s | < 3.4 s |
| First Contentful Paint | 3.0 s | < 1.8 s |
| Cumulative Layout Shift | 0.077 | < 0.1 (already OK) |
| Total page weight | **~4.4 MB** | < 1.8 MB |
| Main-thread work | 24.9 s | — |
| JS bootup time | 10.8 s | — |
| **Server response (TTFB)** | **10 ms** | — |

**Key insight: TTFB is 10 ms — hosting/server is fine. The entire problem is front-end weight (JavaScript + images loaded eagerly).** LCP of 17.1 s alone means most visitors leave before the main content paints.

## Named culprits (heaviest / most-unused resources on mobile)
| Resource | Size | Unused | Notes |
|---|--:|--:|---|
| Teeinblue SDK `sdk.teeinblue.com/shopify/app-v1.js` | 353 KB | 212 KB | Personalizer. Loads eagerly. **Biggest single offender.** |
| Teeinblue preview images (image-layers / mockup-layers `.webp`) | 121/82/80 KB… | — | Personalizer preview art, loaded up front |
| Google tag `G-FY63Q735GJ` (GA4) | 165 KB | 67 KB | |
| Google tag `AW-18336945415` (Google Ads) | 153 KB | 51 KB | |
| Google tag `GT-MK5QW83V` | 144 KB | 66 KB | 3rd Google container — **3 loading eagerly** |
| `adsagentclientafd-*.azurefd.net` ("adsagent" app) | 114 KB + chunks | ~150 KB | Identify — remove if unused |
| Facebook pixel `fbevents.js` | 104 KB | — | |
| Shopify checkout-web hydrate + hooks | 198 + 91 KB | — | Shopify's own; lower priority |

---

## ⚠️ ROOT CAUSE UPDATE (2026-08-14, after theme investigation)
**The theme is NOT the bottleneck — it's Teeinblue, injected via `content_for_header` (an app embed, not theme code).** On a personalized product, **Teeinblue replaces the theme gallery**, so its preview **canvas is the LCP element**, and it can't paint until the **353 KB SDK boots (~10.8 s JS)** → that chain IS the 17 s LCP. The theme's own product images are already responsive/optimized (main image `fetchpriority:high`+eager, rest lazy); the "3840 px hero" was Teeinblue's canvas, not a theme `<img>`. The Google tags + FB pixel + adsagent are also app embeds / web pixels, outside theme code.

**Consequence:** the big wins are **app/admin settings, not theme edits.** And items ① (speed) and ③ (personalizer friction) are the **same fix**: stop Teeinblue from being the on-load, above-the-fold LCP. Make the theme's static product image the hero (fast paint); defer Teeinblue's canvas/form to interaction ("Personalize" tap) or below the fold. The only real *theme* lever is resource hints (below).

## What to fix (in impact order)

### 1. Lazy-load the Teeinblue personalizer  ← biggest win
Don't load the Teeinblue SDK **or** its preview images until the user actually engages personalization (e.g. taps a "Personalize" button) or the personalizer block scrolls into view (IntersectionObserver).
- Check Teeinblue app settings first for a built-in lazy/defer option.
- Otherwise, in the theme: find the Teeinblue snippet/section, and gate its `<script>`/init on click or intersection instead of on page load.
- Dovetails with the planned UX change of moving the personalizer **below** the hero (separate brief item ③) — so it's off the critical path anyway.
- **Removes ~470 KB + a large chunk of the 24.9 s main-thread work from initial load.**

### 2. Defer / consolidate tracking scripts
Three Google containers + FB pixel + the "adsagent" app all load eagerly and block the main thread (~4.5 s TBT).
- Consolidate the 3 Google tags into **one GTM container**, or load them via Shopify **Customer Events (web pixels)** which run off the main document.
- Defer non-essential tags to an interaction/idle trigger; keep only what's needed for attribution.
- Defer/async the **FB pixel**.
- Identify the **`adsagentclientafd` (azurefd) app** in Shopify admin → **uninstall if not in use** (user/admin action, not theme code).

### 3. Images
- Serve a **mobile-width hero** (not 3840 px). Use Shopify `image_url: width` + responsive `srcset`.
- `preload` the LCP hero image; add `loading="lazy"` to everything below the fold.

### 4. Reduce unused JS/CSS
- Trim unused theme JS/CSS; ensure app scripts only load on templates that need them (e.g. review widget only where reviews render).

---

## Acceptance criteria (re-test to confirm)
Re-run **Lighthouse mobile** on the same URL and hit:
- **LCP < 2.5 s** (from 17.1 s)
- **TBT < 500 ms** (from 4,470 ms)
- **Total weight < 1.8 MB** (from 4.4 MB)
- Performance score **≥ 70** (from 30)

Re-test options: Google PageSpeed Insights (mobile strategy), or ping me to re-run the same Browserless Lighthouse audit for an apples-to-apples comparison.

## Ownership notes
- **Theme code:** Teeinblue lazy-load gating, image tags, script defer/async, unused CSS/JS.
- **App settings / Shopify admin:** Teeinblue lazy option, GTM/Customer-Events setup, uninstalling the "adsagent" app.
- Theme auto-publishes on merge to the theme repo's `main` — stage/test before merging.
