# New Pixel / New Page Cold-Start Methodology (e-com, personalized product)

**Why this doc exists:** MJ4U-111's first purchase-optimized ad sets drew **$130–250 CPM with ~0 clicks** on a brand-new pixel/page. That is the textbook cold-start failure, not bad creative. This is the researched methodology to launch a new pixel/store correctly. (Prior research covered kill-rules + page CRO but missed this — gap now closed.)

## The core mistake we made
Optimizing for **Purchase** on a pixel with **zero purchase history**. Meta is told "find people who'll buy," has no signal, so it delivers to a tiny, ultra-expensive sliver → CPM explodes and you buy almost no impressions. At $250 CPM, $25 = ~100 impressions, so "no clicks" is **no sample size**, not a creative verdict.

## The consensus fix: the Optimization-Event Ladder
Optimize for the **lowest-funnel event you can feed with volume**, then climb as data accumulates. Meta wants **~50 optimization events per ad set per week** to learn well; a new pixel can't hit that on Purchase, but *can* on clicks/views.

Ladder (climb only when the lower rung has volume):
1. **Link Clicks / Landing Page Views** (Traffic objective) — cheap CPM, real delivery; seasons the pixel + builds warm audiences
2. **ViewContent**
3. **Add to Cart**
4. **Initiate Checkout**
5. **Purchase** (Sales objective) — only once purchase volume can approach ~50/ad-set/week

## Cold-start phase plan for MJ4U-111
- **Phase 1 (now):** **Traffic** campaign, optimize **Landing Page Views**. Broad US, modest budget. Goals: (a) cheap traffic to *read the creative test* on cost-per-LPV/CTR, (b) fire ViewContent/ATC to season the pixel, (c) feed GA4/Clarity on-site behavior. Add **Conversions API** for stronger signal.
- **Phase 2:** once **Add-to-Cart volume builds** (enough weekly ATC), move to **Sales objective optimizing Add to Cart** (mid-funnel has far more volume than Purchase).
- **Phase 3:** once purchases can approach ~50/ad-set/week, optimize **Purchase**.
- Throughout: keep audiences **broad**, minimize edits (each reset restarts learning), be patient through the learning phase, and don't run many identical ad sets that self-compete in the auction.

## Sources
- **Modern Marketing Institute** — "How to Exit the Meta Ads Learning Phase Fast (2026)": the *Optimization Event Ladder* — choose the event your conversion volume can sustain; climb over time. modernmarketinginstitute.com
- **Shopify Community** — "New Meta pixel with no purchase data — best optimization strategy for a new store?": *"With ~25 visits you don't have a conversion problem yet, you have no sample size"*; the 50-conv/wk figure is a *learning-phase benchmark, not a prerequisite to select Purchase.* community.shopify.com
- **Influee** — Meta Campaign Objectives: *"Best objective for ecommerce is Sales — as long as your Pixel is firing purchase events. If it isn't, run **Traffic** for a while."* influee.co
- **Stackmatix** — Meta Ads Funnel Strategy (2026): new launches — *"use traffic and video-view campaigns to build a warm audience of product-aware visitors"*; pixel event priority **ViewContent → AddToCart → InitiateCheckout → Purchase**. stackmatix.com
- **Meta Business Help** — About the Learning Phase (official; ~50 optimization events/ad-set/week; edits restart learning). facebook.com/business/help/112167992830700

## How this maps to our earlier findings
Confirms the "store/pixel too new = structural early tax" note from the CRO diagnosis ([[pod-page-speed-not-the-bottleneck]]): you cannot brute-force a new pixel into Purchase optimization with budget. Climb the ladder instead. Also validates the sensitivity model's realistic-CPM range — Purchase optimization on a cold pixel blows far past it.
