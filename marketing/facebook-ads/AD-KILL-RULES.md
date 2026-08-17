# When to Kill (or Keep) a Facebook Ad — Decision Rules

A reusable decision guide for MadeJustForYou FB/Meta ad tests. The core mistake is
applying a **purchase-CPA kill rule** to a campaign where it doesn't belong — killing a
winning ad because of a problem that isn't the ad's fault. Before you pause anything, run
the request through the three questions below.

> Pairs with [`research/reference/new-pixel-coldstart-methodology.md`](../../research/reference/new-pixel-coldstart-methodology.md)
> (the optimization-event ladder) and the memory note *meta-inday-metrics-are-estimates*.

---

## The one principle: match the rule to the campaign

A kill rule is only valid if it matches the campaign's **(1) optimization event, (2) stage,
and (3) the layer where the problem actually is.** Get any of these wrong and you'll kill a
good ad.

### 1. Right METRIC — judge the campaign on what it's optimizing for
- A campaign optimizing **AddToCart** is judged on **cost per ATC**, not cost per purchase.
- A campaign optimizing **Purchase** is judged on **cost per purchase (CPA)**.
- Applying a purchase kill-rule to an ATC-optimized campaign is a category error. On a new
  pixel you deliberately optimize a *higher-funnel* event first (see the coldstart ladder),
  so "no sales" is not yet the campaign's job to deliver.

### 2. Right STAGE — don't judge during the learning phase
- Meta needs **~50 optimization events per ad set per week** to exit the learning phase.
- Edits (budget, creative, targeting, audience) **reset learning** — so "tweak then kill"
  churns you in the most expensive, least stable phase forever.
- **"0 sales" only means something once you've spent ~2–3× your break-even CPA** with zero
  results. Below that, you don't have a conversion problem — you have **no sample size**.

### 3. Right LAYER — is it the ad, or the store?
Diagnose *where* the money dies before you touch the ad:
- **Top funnel weak** (low hook / low CTR / high CPC / expensive ATC) → an **ad** problem.
  Killing/replacing the creative or audience is the right move.
- **Top funnel strong but the funnel leaks downstream** (good ATC, but ATC→checkout or
  checkout→purchase collapses) → an **on-site** problem. Killing the ad fixes nothing; you'll
  relaunch a good ad into the same wall. Fix the store, keep the ad running.

---

## Break-even CPA — how to set the "fair-shot" spend

You cannot judge purchases until you've given it a fair shot in dollars. Compute it:

```
break-even CPA = (product price) − (COGS/print + shipping cost + fees)   ≈ gross margin per order
fair-shot spend (per ad) before judging "no sales" = ~2–3 × break-even CPA
```

Worked example (MJ4U-111, ~$45 candle warmer, POD margins):
- Break-even CPA ≈ **$23–27** (plug in your real COGS/shipping).
- Fair-shot line ≈ **$70–80** of spend with 0 purchases before "no sales" is even evaluable.
- To evaluate the **checkout→purchase** step you also need volume there — treat **~15+
  begin-checkouts with 0 purchases** as the minimum before calling the checkout broken.

---

## Concrete thresholds (tune per test)

| Signal | Kill / act? | Notes |
|---|---|---|
| Hook rate (3s plays/impr) < ~20% | Weak creative — test a new hook | Autoplay inflates this; use as relative signal |
| Link CTR < ~1.5–2% | Ad/audience problem — refresh | Strong = 4%+; MJ4U-111 winner ran 6.7% |
| Cost per **optimization event** > ~3–4× your good runs | Ad-level kill | e.g. cost/ATC ballooning past ~$8–10 when good runs are ~$2.50 |
| Spent < ~2–3× break-even CPA, 0 sales | **Do NOT kill** | No sample size yet — keep running |
| Spent ~2–3× break-even CPA **AND** 15+ checkouts, 0 sales | Act — but on the **leaking layer**, usually on-site, not an ad kill | |
| Mid-learning-phase, downstream metric looks bad | **Do NOT kill / do NOT edit** | Edits reset learning; wait it out |

**In-day caveat:** live ATC/purchase counts inflate during the day then settle *down*. Only
act on **settled** days, never on same-day estimates.

---

## Anti-patterns (what NOT to do)
- Killing an ATC-optimized campaign for "no purchases" while it's still in learning.
- Judging purchase CPA on a handful of checkouts (no statistical power).
- Editing a campaign to "help it" mid-learning → resets the phase, burns money.
- Running many near-identical ad sets that self-compete in the auction.
- Blaming the creative when the diagnosed leak is on-site (cart→checkout).

---

## Worked example — MJ4U-111 phase-2 (as of 2026-08-17)

Campaign `120251963479950556`, optimizing **AddToCart**, ~$63 / 1 day:
- Hook 35%, CTR 6.76%, CPC $0.46, **25 ATC @ $2.53**, 4 checkout, **0 purchase**.
- Micro-funnel (users): view_item 107 → personalizer opened (`form_start`) 40 → ATC 20 →
  begin_checkout 2. **The leak is ATC→checkout (90% drop).**

**Verdict: do NOT kill.**
1. Metric — it optimizes ATC and is crushing it ($2.53 CPATC). 2. Stage — 1 day, still in
learning, ~$63 is just under the ~$70–80 fair-shot line, only ~2–4 checkouts (no purchase
sample). 3. Layer — the diagnosed failure is **cart→checkout on-site**, not the ad. Killing
the ad would throw away a winning creative and fix nothing.
**Action:** keep the ad running to fatten the sample + exit ATC learning; fix the cart→checkout
leak (shipping/total/ETA shock — confirm via Microsoft Clarity). Re-evaluate purchases at
~$150–200 spend with 15+ checkouts.
