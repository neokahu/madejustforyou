# MadeJustForYou — Design Idea Research Playbook

A systematic, repeatable pipeline for finding and validating **design ideas** before
competitors do — replacing ad-hoc competitor spying with a process that compounds.

> **Core premise.** In personalized print-on-demand gifting, the product is not the mug —
> it's the *design idea*: a specific combination of
> **Product × Recipient × Occasion × Personalization × Emotional Angle**, expressed as a
> creative *hook* (a phrase, a visual concept). There are effectively infinite combinations.
> The edge is a system that surfaces the high-demand / low-competition ones, tests them
> cheaply, and remembers every result.

Spying on competitors only shows you what *already* won — you always arrive late. This
pipeline adds **leading** signals (search trends, marketplace velocity, social ideation)
and a **testing loop** so you can back winners early and kill losers cheaply.

---

## The pipeline at a glance

```
 0. FOUNDATION      Dimension libraries — the controlled vocabulary of ideas
        │           (products, recipients, occasions, personalization, angles)
        ▼
 1. DISCOVER        Pull demand signals from many sources → raw signals
        │           (search • marketplace • social • competitor • voice-of-customer • internal)
        ▼
 2. GENERATE        Turn signals into candidate ideas (combinatorial / trend-led / gap-led)
        │           → Idea Database backlog
        ▼
 3. SCORE           Rank backlog with the weighted rubric → shortlist
        │           (demand • competition gap • giftability • margin • seasonality • brand fit)
        ▼
 4. BRIEF           Greenlit idea → one-page design brief → mockups
        │
        ▼
 5. VALIDATE        Cheap tiered tests with pre-set kill/scale thresholds
        │           (organic → paid signal → pre-order/live)
        ▼
 6. LEARN           Record every idea + test + outcome in the knowledge base.
        └──────────► Winners → expand. Losers → avoid. Loop back to DISCOVER.
```

Each stage has its own reference doc / template (below).

---

## Files in this folder

| File | What it is |
|------|-----------|
| [`01-dimension-libraries.md`](01-dimension-libraries.md) | Stage 0 — the controlled vocabularies (products, recipients, occasions, personalization, angles) |
| [`02-signal-sources.md`](02-signal-sources.md) | Stage 1 — every demand signal source, what it reveals, and the exact tool/query to pull it |
| [`03-scoring-rubric.md`](03-scoring-rubric.md) | Stage 3 — the weighted scoring model + worked example |
| [`04-validation-testing.md`](04-validation-testing.md) | Stage 5 — test tiers, metrics, benchmark thresholds, decision rules |
| [`templates/idea-database.csv`](templates/idea-database.csv) | The backlog / knowledge base schema (Stages 2 & 6) |
| [`templates/design-brief.md`](templates/design-brief.md) | Stage 4 — one-page brief handed to the designer/AI |
| [`templates/experiment-card.md`](templates/experiment-card.md) | Stage 5 — one card per test, thresholds declared *before* launch |

---

## Operating rhythm (cadence)

| Cadence | Ritual | Time | Output |
|---------|--------|------|--------|
| **Weekly** | Signal scan → add to backlog; launch 2–3 Tier-1 tests; review last week's test results | 60–90 min | Fresh backlog rows, live tests, verdicts |
| **Monthly** | Seasonal look-ahead: lock briefs for the next 1–2 occasions on the calendar (respect lead times) | 2–3 hrs | Greenlit briefs for the upcoming season |
| **Quarterly** | Knowledge-base review: update dimension libraries, recalibrate scoring weights & test benchmarks against your own data | half day | Tuned system |

**Lead-time rule:** a seasonal design must clear validation *and* production setup before the
occasion's buying window opens. Buying windows open earlier than people think — e.g. Christmas
gift research starts spiking in October, Mother's Day in early April. Work backwards from the
date (see the occasion calendar in `01-dimension-libraries.md`).

---

## Automation map (playbook first → automate the heavy steps)

The playbook works run manually today. These are the steps worth wiring to the connected
data tools next, in priority order:

| Stage | Manual today | Automate with |
|-------|-------------|---------------|
| 1 Discover — search demand | Look up volumes by hand | **Ahrefs** Keywords Explorer (overview, matching/related terms, volume history), **Semrush** |
| 1 Discover — marketplace velocity | Browse Etsy/Amazon bestsellers | **Apify** Etsy / Amazon scraper actors (bestsellers, review counts + growth as a sales proxy) |
| 1 Discover — social ideation | Scroll TikTok/Pinterest | **Apify** TikTok / Pinterest / Instagram actors (trending, saves) |
| 1 Discover — competitor new-arrivals & ads | Manually visit sites | **Firecrawl / Tavily** on competitor `/collections/new` + `/best-sellers`; Meta & TikTok ad libraries |
| 3 Score — demand sub-score | Type numbers into rubric | Script: pull Ahrefs volume + Apify velocity → auto-fill the demand columns |
| 4 Brief — concept mockups | Brief a designer | Image-gen tools (nano-banana / imagen / ideogram) for fast concept mockups |
| 6 Learn — knowledge base | CSV in this folder | Graduate to Airtable / Sheets / Notion once volume grows |

> When we automate, each script writes rows straight into the Idea Database schema, so the
> playbook and the tooling never diverge.

---

## Principles (guardrails)

1. **An idea is a combination, not a copy.** Generate from the dimension libraries; use
   competitors as *one* signal, never the only one.
2. **Demand before design.** Never invest in artwork before a signal + score justifies it.
3. **Declare kill/scale thresholds before you test**, not after — otherwise you rationalize.
4. **Cheapest test that can kill the idea, first.** Escalate spend only as an idea survives.
5. **Write down every result.** A losing test is data you paid for — the knowledge base is
   the real asset and the thing competitors can't copy.
6. **Respect lead times.** A great Mother's Day idea found in April is worth little.
