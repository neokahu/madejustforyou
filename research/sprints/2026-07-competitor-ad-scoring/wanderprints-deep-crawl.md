# Wander Prints — Deep Ad Crawl + Evergreen Candidates (2026-08-04)

**Why this exists:** the July clone-shortlist deep-crawled only Macorner + PFG and *skimmed* Wander Prints (18 ads). This is the proper deep crawl. **Reads only — 0 credits used** (WinningHunter `search_facebook_ads`, US, `searchkeyword=landingurl`). Method matches `research/method/new-ad-potential-scorecard.md`. Raw per-product data: `_recount/wanderprints-raw.tsv` (85 rows).

---

## 0. The "2,000 ads" reconciliation (the thing that prompted this)
WinningHunter's brand view shows Wander Prints at **~2,000+ active ads**. That is `total_active_ads_on_page` — an **account-level** number, product-blind, and per the scorecard it is **never used for scoring**. Here is where the number actually goes:

| Layer | Count | What it is |
|---|---|---|
| `total_active_ads_on_page` (brand view) | **~2,000+** | all live creatives across all their FB pages — **mostly collection-level dynamic/catalog ads (DPA retargeting)** |
| Distinct landing-URL ad records (unfiltered) | **166** | ads pointing at a specific wanderprints.com URL |
| Product-page ad records (`page_type=products`) | **94** | the clean product-prospecting creatives |
| **Distinct evergreen products (≥140d)** | **85** | after dedup by product URL — the real catalogable set |
| July shallow grab (obsolete) | 18 | one non-paginated page; ignore |

So the ~1,800-ad gap between 2,000 and 166 is their **dynamic/collection catalog engine** (competitor-intel already flagged "always-on collection-level dynamic ads"). The "18" was just an un-paginated skim. **Verified** (spot-check, exact-URL unfiltered): `page_type=products` does NOT undercount — per-product counts match (9/9) or come in lower (5), never higher.

---

## 1. The strategic finding — Wander Prints is a DIFFERENT archetype
This is the real takeaway, and it changes how to read them vs Macorner/PFG.

| | Macorner / PFG | **Wander Prints** |
|---|---|---|
| Play | **concentrate** 8–25 creatives on a few HERO products | **breadth** — 85+ products each kept alive for years |
| Per-product creatives (A4/B2) | high (memorial=18, our-moon=25) | **low — median 2, only 4 products ≥8** |
| Longevity (A1) | strong (many 200–468d) | **extreme — median 816d, up to 1,042d (top ~1%)** |
| Extra engine | modest | **massive DPA/catalog retargeting (~1,800 dynamic ads)** |
| How to clone | copy the hero concept | mine the **long-tail catalog** for proven evergreen angles |

**Read:** a Wander Prints product alive **1,000 days on 2 creatives** is still a revealed winner — it quietly converts profitably year-round without needing creative scale. Their edge is **catalog breadth + retention + DPA**, not per-product spend. So for our shortlist, weight their products on **A1 longevity (extreme)**, not A4 scaling (structurally low for them).

**Signals snapshot (85 evergreen products):** longevity min 140d / median 816d / max 1,042d · price min $16.95 / median $25.95 / max $45.95 (low-AOV tier, like PFG) · 18 products ≥4 creatives, 4 products ≥8 · **53 of 85 overlap our Teeinblue angles.**

**By recipient (all 85 evergreen products; recipient tag in `_recount/wanderprints-raw.tsv`):**

| Recipient | # products | Read |
|---|---|---|
| Parents | 13 | mom/dad keepsakes, apparel, mugs |
| Grandparents | 13 | grandma/grandpa — direct overlap with our GPD focus |
| Couples | 11 | anniversary/bestie-couple, "reasons" mechanic |
| Memorial | 9 | their core always-on lane (extreme longevity) |
| Friends | 6 | bestie blankets/pillows |
| Pets | 6 | dog/cat lovers, funny photo |
| Kids/Grandkids | 6 | huggable pillows/blankets for kids |
| Occupation/Other | 2 | nurse, retirement |
| Other/unlabeled | 19 | shortcode/blank-caption URLs — recipient not inferable |

→ **Parents + Grandparents + Couples + Memorial = 46 of 85 (54%)** — the same emotional lanes we target. Grandparents (13) directly reinforces the GPD pipeline.

---

## 2. Top candidate adds (overlap our multi-name/photo core) — for review, NOT yet merged
Ranked by creative count then longevity. A1 = longevity band (all =3, top-decile+). A4 = creative-scaling band. AOV shown. These are the Wander Prints products worth considering for the clone shortlist.

| Concept | Recipient | Creatives (A4) | Days (A1) | AOV | Read |
|---|---|---|---|---|---|
| **"Beautiful gift for Mom & Grandma"** (multi-name) | Parents/Grandparents | **10** | 861 | $22.95 | Their hardest-pushed our-fit product; maps 1:1 to Teeinblue multi-name |
| **"10 reasons you're my bestie" fleece blanket** | Friends | 9 | 1020 | **$39.95** | Premium AOV + 1,000d; "reasons list" mechanic |
| **"Best dog mom ever" ugly sweater** | Pets | 9 | 1019 | $32.95 | Xmas apparel, premium-ish; cat version ("meowy catmas") = 7 |
| **"Granddaughter unicorn hug this" pillow** | Kids/Grandkids | 7 | 1012 | $25.95 | Grandkid keepsake, huggable-object mechanic |
| **"Besties sitting on the moon"** | Friends | 7 | 749 | $26.95 | Friendship, photo/character |
| **"Grandma hugged this" soft blanket** | Grandparents | 5 | 1012 | **$37.95** | Premium AOV, grandma huggable |
| **"Moms grandmas sweethearts"** (3-gen names) | Parents/Grandparents | 3 | 909 | $24.99 | Our exact multi-generation-name strength; premium variant exists at $45.95 |
| **Memorial cluster** — "I'll carry you" (927d) · "if love could have saved you" (861d) · "Memorial gift for pet parents" (881d, 4 creatives) | Memorial | 3–4 | 860–930 | $19–30 | Memorial is their core always-on lane — extreme longevity, year-round, high emotion |
| **"Birth flower — grow an old friend"** | Friends | 2 | 484 | $25.95 | Birth-flower lane (they do journals/dishes; overlaps our birth-flower apparel gap) |

Apparel note: unlike Macorner/PFG, Wander Prints leans into **ugly sweaters, fleece blankets, and soft pillows** at $30–40 — a **higher-AOV format cluster** worth a look given our tier sits ~$24.

---

## 3. What this does NOT yet cover (before anything merges)
1. **Full auto-score not run.** A5 (occasion durability) / A6 (differentiation) are judgment criteria; `scripts/score_concepts.py` should be run on the finalists for shortlist-grade scores.
2. **Prices missing for shortcode products** (`-fbf` redirect URLs had no indexed price).
3. **Backends observed:** `great-family-shop.myshopify.com` (primary, 77/96 rows) + `wdp-us.myshopify.com` (secondary) — treat as one seller.

> **Seller-count / A2 validation is deliberately NOT used** (user directive 2026-08-04): an exact-landing-URL search only catches sellers reusing the identical URL (floors near 1); real copycats run a *similar-not-exact* concept, and judging that similarity is unreliable. Validate on **longevity** (a product alive 800+ days is self-validated) + **lead-seller creative scaling**, not copycat counts.

**Suggested next step:** pick the finalists from §2, run auto-score on them, then merge approved rows into `clone-shortlist-links.csv` (as a new tier or tagged `src=wanderprints`).
