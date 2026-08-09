# Step 3 — Native Automated Rules: the Safety Floor

**Goal:** a small set of **defensive** rules set inside **Meta Ads Manager** that run 24/7 and pause obvious money-losers even if the decision engine (or its token) is down. This is the seatbelt — not the driver.

**Who does this:** you, in Ads Manager UI (~15 min). No code, no token, nothing the ad-account owner can revoke — the rules run under your own BM login.

> **Why native (UI) and not the API?** A safety floor must survive *our* stack failing. Native rules live in Meta, independent of our app/token, so if the engine breaks, the API access is pulled, or a script hangs, these still fire. That independence is the whole point.

---

## The one principle: the floor is LOOSER than the engine

Two systems will eventually watch the same ads (the engine + these rules). To keep them from fighting:

- **The engine acts first** — it kills at ~1× break-even CPA (no ATC) and ~2.5× (ATC, no sale), and makes the nuanced calls.
- **The floor only catches what the engine missed** — it triggers at **~3× break-even CPA** and on **catastrophic ROAS**, i.e. runaways, or any day the engine didn't run.

So the floor should almost never fire when things are healthy. If it fires often, either the engine isn't running or thresholds need a look.

> **Attribution caveat:** these rules read **Meta's own** numbers, which undercount conversions post-iOS-14.5. That's exactly why the ROAS-kill threshold is set well *below* break-even (catastrophic only) — so a delivered-but-underreported winner doesn't get killed by a pessimistic ROAS. Emergencies only.

---

## The rules — MJ4U-111 (break-even CPA **$38.19**, break-even ROAS **1.57×**)

Regenerate these numbers for any product with `python3 engine/floor_spec.py` (reads the same economics).

| Rule | Scope | Condition | Action | Check |
|---|---|---|---|---|
| **A · Runaway kill (no sales)** | Ad set | Purchases = 0 **AND** Amount spent ≥ **$115** | **Turn off ad set** | Daily |
| **B · ROAS emergency** | Ad set | Purchase ROAS < **1.10** **AND** Amount spent ≥ **$115** **AND** Time since created ≥ **3 days** | **Turn off ad set** | Daily |
| **C · Fatigue notify** | Ad | Frequency > **3** (last 7 days) | **Send notification only** | Daily |
| **D · Scale (optional, interim)** | Ad set / Campaign | Purchase ROAS > **2.36** (last 3 days) | **Increase daily budget 20%** | Max once / 48h |

- **A** catches the classic "spending, zero conversions" runaway (covers 0-ATC too, since 0 ATC ⇒ 0 purchases — native rules can't read ATC cleanly, so we gate on purchases).
- **B** is the "clearly losing money" backstop (ROAS 1.10 ≈ 0.7× break-even = bleeding), only after 3 days so learning-phase noise can't trip it.
- **C** never changes anything — it just emails/notifies you to queue a creative refresh (fatigue kills POD winners; the film studio feeds the refresh pipeline).
- **D** is the *only* offense rule, and it's **interim**: it gives you automated scaling in the window before the Phase-4 engine takes over. **Disable D the moment the engine drives budgets**, or two systems will both bump budget and you'll blow past learning-reset limits.

Set a **maximum budget cap** on any ad set that has Rule D, so a scale rule can't run away.

---

## How to create a rule in Ads Manager

1. **Ads Manager** → top-right **Rules** (or **More tools → Automated Rules**) → **Create rule → Custom rule**.
2. **Apply to:** pick the scope — for A/B choose **"All active ad sets"** (or select specific ones); for C choose **"All active ads."** You can also scope a rule to a single campaign.
3. **Action:** choose **Turn off** (A, B), **Send notification** (C), or **Increase daily budget → By percentage → 20%** (D).
4. **Conditions:** add each condition from the table (Amount spent, Purchases / Results, Purchase ROAS, Frequency, Time since created). Use **AND** between them.
5. **Time range:** set to match the rule (A/B: **Today** or **Maximum**; C: **Last 7 days**; D: **Last 3 days**).
6. **Schedule / frequency:** **Daily** is plenty for a $30–100/day account (you don't need "continuously"). For D set **Action frequency** so it can only fire **once every 48 hours**.
7. **Notifications:** turn on email (and Slack/mobile if you use it) so every automatic pause reaches you.
8. **Save.** Repeat for each rule.

> **Learning phase is safe:** pausing an ad set and budget changes ≤20% do **not** reset learning (Meta-official). Rules A/B/D respect this.

---

## Coordinating with the engine (now and at Phase 4)

- **Now (engine is read-only):** the floor is your only automation. Keep A, B, C on; D optional if you want interim auto-scaling.
- **At Phase 4 (engine writes):** the engine becomes the primary actor. **Disable D.** Keep A, B, C — they stay as the independent backstop, and because they're looser, they won't pre-empt the engine's finer decisions. If both ever pause the same ad set, that's fine (idempotent — it just ends up off).

---

## Checklist
- [ ] Rule A (runaway kill, $115 / 0 purchases) — created, notifications on
- [ ] Rule B (ROAS emergency < 1.10 @ $115, ≥3d) — created
- [ ] Rule C (frequency > 3 → notify only) — created
- [ ] Rule D (interim +20% scale) — created **only if** you want interim auto-scaling; note to disable at Phase 4
- [ ] Max budget cap set on any ad set carrying Rule D
- [ ] Email/Slack notifications enabled so every auto-action reaches you
- [ ] Re-run `engine/floor_spec.py` whenever you add a product, and add its rules

Once these are live, the account has a 24/7 floor under it — safe to move to **Phase 4** (guardrailed engine writes, dry-run → live).
