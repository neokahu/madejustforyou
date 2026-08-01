# Stage 3 — Scoring & Prioritization

You will always have more ideas than you can test. This rubric turns a messy backlog into a
ranked shortlist so testing budget goes to the highest-expected-value ideas. Score each idea
**0–5** on six criteria, multiply by the weight, sum to a composite **0–5**.

---

## The rubric

| # | Criterion | Weight | What a **5** looks like | What a **1** looks like |
|---|-----------|:------:|-------------------------|-------------------------|
| 1 | **Demand** | **30%** | High/rising search volume *and* strong marketplace velocity | Flat, thin, or no measurable demand |
| 2 | **Competition gap** | **20%** | Clear demand but weak/low-quality/expensive competitor coverage | Saturated; many rivals running ads on it |
| 3 | **Giftability** | **15%** | Obvious, emotionally strong gift for a clear recipient/occasion | Generic; no clear gifting trigger |
| 4 | **Margin & producibility** | **15%** | Cheap base, light ship, low breakage, simple print | Costly/heavy/fragile/complex, thin margin |
| 5 | **Seasonality fit** | **10%** | Evergreen, or enough lead time before the window | Season already peaking; no runway |
| 6 | **Brand fit** | **10%** | On-brand: warm, heartfelt, personalized | Off-brand tone or category |

**Composite = Σ(score × weight).** Range 0–5.

### Advance thresholds

| Composite | Action |
|-----------|--------|
| **≥ 4.0** | Fast-track — brief immediately |
| **3.0 – 3.9** | Queue for the next test batch |
| **2.0 – 2.9** | Park — revisit if a new signal lifts demand or a season approaches |
| **< 2.0** | Drop |

> **Veto rules** (auto-drop regardless of composite): margin/producibility scores **1**
> (you can't make money on it) OR a seasonal idea with **no remaining lead time**.

---

## Scoring the Demand criterion (the 30% that matters most)

Blend the three demand signals so no single source dominates:

```
demand_score = round( 0.5 × search + 0.3 × marketplace + 0.2 × social )   # each sub-score 0–5
```

| Sub-signal | 0–5 anchor |
|-----------|-----------|
| **search** | 5 = high volume & rising; 3 = moderate & steady; 1 = negligible/declining |
| **marketplace** | 5 = bestsellers with fast review growth; 3 = present, steady; 1 = absent |
| **social** | 5 = clearly trending (rising saves/engagement); 3 = some traction; 1 = none |

This is the first sub-score to automate: a script pulls Ahrefs volume+slope (`search`) and
Apify marketplace velocity (`marketplace`) and writes them into the Idea Database.

---

## Worked example

**Idea:** *Custom pet-photo ornament, "First Christmas as a family of [n]", sentimental, for new
pet parents.* Signals: rising "pet ornament" searches into Q4; Etsy bestsellers with fast
review growth; strong on Pinterest.

| Criterion | Score | Weight | Weighted |
|-----------|:-----:|:------:|:--------:|
| Demand (search 5, mktpl 5, social 4 → 4.8) | 4.8 | 0.30 | 1.44 |
| Competition gap (present but generic) | 3 | 0.20 | 0.60 |
| Giftability (very high, clear occasion) | 5 | 0.15 | 0.75 |
| Margin & producibility (ornament: cheap, light) | 5 | 0.15 | 0.75 |
| Seasonality fit (found in Aug → full runway) | 5 | 0.10 | 0.50 |
| Brand fit (warm, personal) | 5 | 0.10 | 0.50 |
| **Composite** | | | **4.54** |

→ **≥ 4.0 → fast-track to brief.** Contrast: the same idea discovered in **December** scores
Seasonality **1** and triggers the lead-time **veto** → drop, revisit next August.

---

## Notes on using the rubric

- **Calibrate quarterly.** After ~20 tested ideas, check whether high-composite ideas actually
  won. If not, adjust weights (usually: trust Demand and Competition-gap more).
- **Score in batches**, comparatively — it's easier and more consistent to rank 15 ideas
  against each other than to score one in isolation.
- **Keep the scores in the row.** The knowledge base (Stage 6) later correlates scores with
  test outcomes — that's how the rubric earns its weights.
