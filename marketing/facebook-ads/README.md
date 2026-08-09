# Facebook / Meta Ads — FB-Advertiser Domain

This is the FB-advertiser (media-buyer) domain: it owns **break-even economics, test→scale execution, and kill/scale automation** for the store's Meta ads. It is deliberately **separate from the AI Film Studio** — the studio delivers finished creative, then hands off here.

> **👉 To operate the agent day to day, read [`HOW-TO-USE.md`](HOW-TO-USE.md).** For one-time setup, see `setup/`. This README is the architecture overview.

- **Methodology source of truth:** sop-docs → `Internal-Guidelines/Kien-thuc-chuyen-mon/Marketing/Facebook-Testing-Scaling-Research.md` (4 Meta-official base laws + consensus playbook: break-even math, leading/lagging metrics, kill/keep rules, ABO-test → CBO-scale pipeline).
- **Goal:** automate test→scale as **full unattended execution**, Claude-driven, via the official Meta Ads MCP + Marketing API, with a native-rules safety floor.

## Architecture (hybrid)
1. **Layer 1 — native Automated Rules (free, 24/7 floor):** emergency runaway-spend kill + per-ad-set budget caps + hard ROAS-floor pause. Runs under our own BM; can't be revoked.
2. **Layer 2 — Claude judgment engine (scheduled agent + official Meta MCP):** per-product break-even, leading indicators vs accumulated spend, kill/keep/scale calls, executed via the MCP with hard guardrails (daily ceiling, per-run max budget increase, dry-run→live, full action log, kill-switch, digest).

## Account context (why this is viable)
The **Business Manager is ours**; only the **ad account is rented** and shared into our BM with **admin access**. So we run legitimate first-party automation through **our own app + system-user token** — not the unofficial-shared-key pattern that gets accounts banned. Residual risk: the rented ad account can be revoked / carries its own ban risk → keep the native-rules floor + alerting independent of the agent.

## Build phases
1. ✅ **Setup + validate access** → `setup/01-meta-api-setup.md` (app + system-user token, read+write validated)
2. ✅ **Read-only decision engine** → `engine/` (encodes the methodology; proven on sample data, awaiting live campaigns)
3. ✅ **Native-rule safety floor** → `setup/02-native-rules-safety-floor.md` (24/7 defensive backstop in Ads Manager)
4. ✅ **Unattended write executor** → `setup/03-unattended-execution.md` + `engine/execute.py` (dry-run default; guardrailed --live; built, validated on sample — awaiting a live test campaign + go-live soak)

## Layout
```
marketing/facebook-ads/
├── README.md                          # this file
├── setup/
│   ├── 01-meta-api-setup.md           # app, system-user token, MCP, read/write validation
│   └── 02-native-rules-safety-floor.md# the 24/7 native Automated-Rules floor (per-product)
├── .env.example                       # secrets template (real .env is gitignored)
├── .gitignore                         # ignores .env + reports/
└── engine/                            # decision engine (P2) + floor spec (P3) + executor (P4)
    ├── run.py  meta.py  economics.py  rules.py  report.py   # read-only decision engine
    ├── floor_spec.py                                        # native-rule numbers per product (P3)
    ├── execute.py  meta_write.py                            # guardrailed write executor (P4)
    ├── sample_data.json  README.md
    └── config/products.json  thresholds.json  floor_thresholds.json  execution.json
```

## Run
```bash
cd engine
python3 run.py --sample       # decision engine on synthetic data (every verdict)
python3 run.py                # live, read-only, last 7d → call sheet
python3 floor_spec.py         # print the Ads-Manager safety-floor numbers per product
python3 execute.py --sample   # executor dry-run on synthetic data (WOULD-DO)
python3 execute.py            # executor dry-run on live account (default; no writes)
python3 execute.py --live     # executor LIVE (guardrailed) — only after the go-live soak
```
