# MJ4U-133 C0 — generation cost & timing (as of 2026-11-25 16:30 +07)

Source of truth per asset: `marketing/facebook-ads/media-cost-ledger.csv` (charged price, model, timing, size, file). Job counts cross-checked with AtlasCloud's daily usage report.

| Day (UTC) | Model | Jobs (Atlas) | In ledger | Charged in ledger | Est. not in ledger |
|---|---|---|---|---|---|
| 11-24 | Seedream v5 Pro Edit | 21 | 21 | $1.51 | — |
| 11-24 | Nano Banana Pro Edit | 2 | 2 | $0.28 | — |
| 11-24 | Seedance 2.0 Fast ref-to-video | 1 | 1 | $0.78 | — |
| 11-25 | Seedream v5 Pro Edit | 29 | 20 | $1.01 | 9 × ~$0.055 ≈ $0.50 |
| 11-25 | Nano Banana Pro Edit | 81 | 50 | $6.86 | 31 × $0.14 ≈ $4.34 |
| **Total** | | **134** | **94** | **$10.44** | **≈ $4.84 → round total ≈ $15.30** |

The 40 unlogged 11-25 jobs are early Gate B images downloaded before the ledger hook existed. AtlasCloud's history API ignores paging, so they can't be pulled automatically; their cost is estimated at list price above.

**Unit prices seen (charged):** Nano Banana Pro Edit 2k $0.14 · Seedream v5 Pro Edit $0.036 (≤2.61 MP) / $0.072–0.077 (2048² / 1776×2368) · Seedance 2.0 Fast ref-to-video 5 s 720p, 3 refs $0.78.
**Time per job (submit → done):** Nano Banana Pro avg 108 s (max 606 s) · Seedream avg 141 s (max 186 s) · Seedance 5 s clip 273 s.
