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

## Folder map

Stable **playbook** (rarely changes) is separated from **living sprint work** (changes constantly).

```
research/
├── method/        the playbook, numbered to the pipeline stages
├── reference/     stable tool docs (Teeinblue mechanics + verdict)
├── templates/     reusable schemas (idea-db, brief, experiment card)
├── scripts/       all code (scorers, calendar builder)
├── calendar/      the gifting-occasion calendar (generated)
└── sprints/       living work — one self-contained folder per sprint
```

**`method/`** — the methodology, filenames = pipeline stage numbers:

| File | Stage | What it is |
|------|-------|-----------|
| [`method/0-foundation.md`](method/0-foundation.md) | 0 | controlled vocabularies (products, recipients, occasions, personalization, angles) |
| [`method/1-discover.md`](method/1-discover.md) | 1 | every demand-signal source + the exact tool/query to pull it |
| [`method/2-generate.md`](method/2-generate.md) | 2 | the **idea engine** — *craft* a design from a validated slot (mechanic+angle+hook+aesthetic) |
| [`method/3-score.md`](method/3-score.md) | 3 | the weighted scoring model + worked example |
| [`method/4-validate.md`](method/4-validate.md) | 5 | test tiers, metrics, benchmark thresholds, decision rules |
| [`method/new-ad-potential-scorecard.md`](method/new-ad-potential-scorecard.md) | 3 | the competitor-ad opportunity scorecard (PART 0 thresholds) |

**`reference/` · `templates/` · `scripts/` · `calendar/`**

| Path | What it is |
|------|-----------|
| [`reference/teeinblue-assets-guide.md`](reference/teeinblue-assets-guide.md) | **VERIFIED** Teeinblue mechanics — source of truth, don't re-guess |
| [`reference/teeinblue.md`](reference/teeinblue.md) | Teeinblue tool fit / verdict / pricing |
| [`templates/idea-database.csv`](templates/idea-database.csv) | the backlog / knowledge-base schema (Stages 2 & 6) |
| [`templates/design-brief.md`](templates/design-brief.md) | Stage 4 — one-page brief handed to the designer/AI |
| [`templates/experiment-card.md`](templates/experiment-card.md) | Stage 5 — one card per test, thresholds declared *before* launch |
| `scripts/` | `score_concepts.py` · `score_ads.jq` · `score_gpd.py` · `build_calendar.py` |
| [`calendar/occasions-calendar.md`](calendar/occasions-calendar.md) | gifting-occasion calendar (+ `.csv` master, `.ics` import) |

**`sprints/`** — living work; see [`sprints/README.md`](sprints/README.md) for the index. One folder
per sprint; each greenlit concept is a **self-contained sub-folder** (brief + specs + experiment +
`_assets/`). Finished reusable component libraries **graduate** to the repo-root `teeinblue-assets/`.

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
date (see the occasion calendar in `method/0-foundation.md`).

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
7. **Every idea and concept carries its sources — no claim without a link.** Each backlog row
   records the source URL(s) it came from; every crafted concept links the live listings / posts /
   ads it was built from (the standard **"Reference examples"** section in sprint concept docs).
   This keeps findings auditable, lets anyone eyeball the real designs, and — as the macorner
   "4.2M Hawaiian shirt" correction showed — stops a keyhole sample from becoming a false claim.
