# New-Ad Potential Scorecard (competitor-tracking strategy)

> ⚠️ **STATUS: thresholds are PROVISIONAL — NOT yet data-validated.** The *logic* (two tracks,
> template-level saturation, the criteria themselves) is sound. But every **number** below
> (day-ranges like 8–21d / 6mo+, score cutoffs ≥18 / ≥15, "≥3 brands", the 70/30 split) is a
> placeholder from general domain judgment — **not** derived from data. Team rule: everything
> based off data. Do not rely on the cutoffs until calibrated.
>
> **Calibration plan — do this before trusting the bands:**
> 1. **Back-test on our 10 tracked brands** (native WinningHunter, next session): pull each
>    brand's ad history; for their *known* scaled winners, record the ACTUAL days-running and
>    1w/1m active-ads growth *at the point they took off*, plus template-copycat counts.
>    Derive the real "rising" (Track B) and "durable" (Track A) thresholds from THEIR data.
> 2. **Deep-research (cited):** does days-running / active-ad-growth actually predict
>    profitability? real POD saturation heuristics? typical evergreen:trending revenue mix?
> 3. **Replace every number** below with the data-derived value + its source, then re-score a
>    sample of known winners vs duds to confirm the bands separate them. Log the evidence.

**Strategy:** don't build blind. Ride proven operators' ads across **two revenue engines —
run both**:

- **Track A · EVERGREEN** = products/ads they've run **for a long time**. Still running after
  months = still profitable = durable demand. Lower risk, steady baseline revenue. Saturation
  is *fine* here — the market is big enough for many operators. This is the **foundation catalog**.
- **Track B · TRENDING** = **newly-launched** ads caught **early** (rising, few copycats).
  Higher upside, perishable, act fast. This is **opportunistic growth** on top of the base.

Both beat building with no niche experience (the operators already validated demand, audience,
price band, fulfillment). Aim for a **portfolio**: evergreen SKUs fund stability, trending tests
capture spikes. (Rough split to start: ~70% evergreen catalog / ~30% trending bets.)

**Watchlist (proven operators, exclude from "new opportunity" but mine for angles):**
Macorner · Pawsionate · Wander Prints · Suzitee · OrnamentallyYou · Alma Gems ·
Personalized Family Gifts · Faith & Love · A Gift Customized · OrnamentallyYou.
(WinningHunter `list_tracked_brands`.)

---

> **Unit of competition = the concept / angle / personalization template, not the exact SKU.**
> In custom gifts, exact overlap is rare — everyone re-skins winning templates with small tweaks.
> So (a) measure saturation at the **template level**, and (b) our edge is never a "unique
> product" — it's a **better personalization mechanic + design + offer** on a proven concept.
> Copying done right = take the concept, upgrade the execution.

## Track A · EVERGREEN scorecard (long-runners) — score 0–3

Pick a product/ad a tracked brand has run **a long time**. Here longevity + many operators = GOOD.

| # | Criterion | 0 | 3 (strong) | WH signal |
|---|---|---|---|---|
| A1 | **Longevity** (continuous run) | <2mo | **6mo+ still active** | `scan_ad` days-running / brand history |
| A2 | **Persistence** (stable, reappears seasonally) | spiked then died | consistently on / returns yearly | `analyze_tracked_brand` history |
| A3 | **Durable demand** (evergreen relationship/occasion) | date-locked fad | Mom/Dad/Grandparent/pet/memorial/wedding — always-on | judgment |
| A4 | **Market depth** (multiple operators sustain it) | only 1 brand | **several proven brands run it** (proves size) | watchlist / `find_similar_shops` |
| A5 | **Offer we can match or beat** | can't match | same personalization, better price/quality | product page |
| A6 | **We-can-make-it** (Teeinblue/POD fit) | exotic sourcing | trivially POD-able | judgment |
| A7 | **Margin viability** | thin | strong perceived value, $30–60 AOV | judgment |

**Max 21. Bands:** ≥15 → **BUILD as evergreen SKU** · 10–14 → maybe (differentiate) · <10 → skip.
*Note: A1 long run and A4 many operators are POSITIVES here — the opposite of Track B.*

---

## Track B · TRENDING scorecard — score each NEW ad 0–3 per criterion

| # | Criterion | 0 (skip) | 1 | 2 | 3 (strong) | WH signal source |
|---|---|---|---|---|---|---|
| 1 | **Traction velocity** — is the brand *scaling* it? | flat | slight ↑ | clear 1w ↑ | steep 1w & 1m active-ads ↑ | `analyze_tracked_brand` / `find_winning_products` active-ads growth 1w·1m |
| 2 | **Survival window** — passed their kill-gate but still early | <3d (unproven) or >60d (late) | 30–60d | 4–7d | **8–21d & still active** | `scan_ad` days-running |
| 3 | **Creative conviction** — multiple variants pushed | 1 static | 2 | 3–4 | 5+ variants/iterations | brand ad count for that product |
| 4 | **Low template-saturation** — few brands run the same **concept/angle**, not exact SKU (measure at template level — exact copies are rare in custom gifts) | concept on many stores | some | few | concept still fresh | scan ads for the same angle/template across watchlist |
| 5 | **Demand tailwind** — rising need/occasion | declining | flat evergreen | seasonal peak coming | on an **exploding topic** ↑ | `search_exploding_topics` |
| 6 | **Angle strength** — hook + emotional gift angle | weak/unclear | ok | good | scroll-stopping, emotional, giftable | `scan_ad` hook/angle + `get_ad_transcript` |
| 7 | **We-can-make-it** — POD/personalization fit | needs exotic sourcing | hard | doable | trivially POD-able (Teeinblue) | judgment |
| 8 | **Margin viability** — giftable AOV vs COGS/ship | thin | ok | good | strong perceived value, $30–60 AOV | judgment + product page |

**Max 24. Decision bands:**
- **≥18 → TEST** — reverse-engineer (scan_ad + transcript), design brief, build & test.
- **12–17 → WATCH** — add to watch list, re-score weekly; test if velocity keeps rising.
- **<12 → SKIP.**

**Hard vetoes (auto-skip regardless of score):** can't fulfill/personalize it; trademark/IP on
the product; already saturated across ≥3 of our tracked brands (we're late); ad already
running >60d (peak likely passed).

---

## Tracking workflow — two cadences
- **Track A · Evergreen (monthly/quarterly):** scan each tracked brand's **long-running** ads
  (`analyze_tracked_brand` full history; `scan_ad` days-running) → score with Track A → BUILD
  the ≥15s into the foundation catalog. Slow-moving, high-certainty.
- **Track B · Trending (weekly):** the fast loop below.
1. **Pull new ads** from each tracked brand → `analyze_tracked_brand` (view = newest) or
   `daily_radar` for fresh signals. Filter to ads **launched in the last ~21 days**.
2. **Pre-filter:** drop anything already run by ≥3 watchlist brands (saturated), or >60d old.
3. **Score** each survivor with the scorecard above.
4. **Shortlist TEST** (≥18) → `scan_ad` + `get_ad_transcript` to capture hook/angle/offer →
   write a design brief (`research/sprints/briefs/`).
5. **Log** everything (product · brand · launch date · 1w growth · score · decision) into
   `research/sprints/competitor-intel-<month>.md` so trends compound over time.

## Why this beats the alternatives
- **vs build-new:** the operators already proved demand + audience; we skip the riskiest unknowns.
- **vs copy-saturated:** we catch the ad on the way *up* (low days-running, few copycats), not after every store runs it.
- **Compounding:** weekly scoring builds a proprietary dataset of what "rising" looks like in
  *our* niche — the scorecard gets sharper each cycle.

> Run the WinningHunter pulls with native `mcp__winninghunter__*` tools after a session restart.
> Ties to: `research/tools/winninghunter-*`, `research/sprints/competitor-intel-*`.
