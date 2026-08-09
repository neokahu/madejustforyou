# Step 1 — Meta Ads API + MCP Setup Guide

**Goal:** stand up legitimate, first-party API automation for our Meta ads and wire the **official Meta Ads MCP** into Claude Code, so the automation engine (built next) can read Insights and — later — create/kill/scale campaigns unattended.

**Who does this:** you (it's account/console work in Meta's UI + a few terminal commands). Budget **~½ day**. When done, send me the 4 things in [§10](#10-what-to-hand-back-to-me).

> ⚠️ **Meta renames things constantly.** Product names, menu labels, and button positions drift (e.g. "Ads Management Standard Access" was renamed to "Marketing API Access Tier" in May 2026). Where a label may have moved, I describe *what you're looking for* and link the official doc — trust the doc over the exact wording here. Marketing API is at **v26.0** as of writing (Aug 2026).

> ✅ **Why this is safe for us:** the Business Manager is ours; only the ad account is rented and shared into our BM with admin. We authenticate with **our own app + our own system-user token** — legitimate server-to-server. This is *not* the "unofficial third-party tool with shared keys" pattern that gets accounts banned.

---

## 0. Prerequisites — confirm before you start

- [ ] You can log into **business.facebook.com** and see **our Business Manager** (we own it).
- [ ] Inside it, **Business Settings → Accounts → Ad Accounts** lists the **rented ad account**, and your role on it is **Admin** (or at least "Manage campaigns"). If it says *Analyst/read-only*, stop — get it upgraded first; nothing below will be able to write.
- [ ] You're an **Admin of the Business Manager itself** (Business Settings → Users → People → your name → should show "Admin"). System users can only be created by a BM admin.
- [ ] Note two IDs you'll need throughout:
  - **Business ID** — Business Settings → Business Info (a long number).
  - **Ad Account ID** — Business Settings → Ad Accounts → the rented one (looks like `act_1234567890`; the number after `act_` is the raw ID).
- [ ] Also note the ad account's **currency** and **timezone** (Business Settings → Ad Accounts → the account → details). The automation math needs these — spend thresholds and "day" boundaries depend on them.

---

## 1. Create the Meta developer app

1. Go to **developers.facebook.com** → log in with the same personal account that's a BM admin → **My Apps → Create App**.
2. **App type:** choose **Business** (this is the type that unlocks Marketing API + business assets).
3. Give it a name (e.g. `MJ4U Ads Automation`) and, when asked, **link it to our Business** (our Business Manager). If it doesn't ask during creation, you'll attach it in §3.
4. In the app dashboard, **Add Product → Marketing API → Set up**.
5. **App Settings → Basic:** add a **Privacy Policy URL** (any working URL on our domain, e.g. `https://<ourstore>.com/policies/privacy-policy` — Shopify stores have one by default) and a **Category**. Save. (Meta blocks token generation for apps with no privacy URL.)
6. Leave the app in **Development / not public** — for our own/shared assets we do **not** need to make it Live or pass App Review (see [§8](#8-access-tier--rate-limits-fyi)).

Note the **App ID** and **App Secret** (App Settings → Basic). Keep the secret private.

---

## 2. Attach the app to our Business (if not already)

Business Settings → **Accounts → Apps → Add → Add an App → paste the App ID**. This makes the app a business asset so a system user can use it. (Skip if step 1.3 already linked it.)

---

## 3. Create a System User + generate a NON-EXPIRING token

A **System User** is a headless "service account" whose token doesn't expire — this is what unattended automation must use (personal tokens expire every ~60 days and would break the agent).

1. Business Settings → **Users → System Users → Add**.
   - Name: `mjp-ads-bot`
   - Role: **Admin** (needed to manage campaigns/budgets). If you prefer least-privilege, "Employee" can work *only if* you then grant it full task access on the ad account in the next step — Admin is simpler and we own the BM.
2. With the system user selected → **Add Assets**:
   - **Apps** → select `MJ4U Ads Automation` → grant **Full control (Manage app)**.
   - **Ad Accounts** → select the **rented ad account** → toggle **Manage campaigns** (and **Manage ad account** if shown). This is the step that grants API write on that account.
3. Still on the system user → **Generate New Token**:
   - **App:** `MJ4U Ads Automation`
   - **Token expiration:** **Never**.
   - **Scopes (check these):** `ads_read`, `ads_management`, `business_management`.
     - **If you'll use the official Meta MCP** (you will), also add: `ads_mcp_management`. Optionally `catalog_management`, `pages_show_list`, `instagram_basic` if we later manage catalogs/IG placements.
   - Click **Generate** → **copy the token immediately** (it's shown once). This is a long string starting with something like `EAAG...`.

> This token = full ads control on that account, forever, until revoked. Treat it exactly like a password.

---

## 4. Store the token securely

From the repo:

```bash
cd marketing/facebook-ads
cp .env.example .env
```

Open `.env` and fill in the real values (App ID, App Secret, System-User token, Business ID, `act_` Ad Account ID, currency, timezone). **`.env` is already gitignored** (root `.gitignore` excludes `.env`) — never commit it, never paste the token into chat or a doc.

To revoke/rotate later: Business Settings → System Users → `mjp-ads-bot` → the token list → revoke, then regenerate.

---

## 5. Validate READ access (proves auth works)

Replace `<TOKEN>` and `<ACT_ID>` (the number only, no `act_` for `$ACCOUNT`, or use full `act_...` in the path). Easiest: `source .env` first if you named the vars accordingly, else paste inline.

```bash
# 5a. Who am I? (should return the system user's id/name)
curl -s "https://graph.facebook.com/v26.0/me?access_token=<TOKEN>"

# 5b. Can I see the ad account? (name, status, currency, timezone)
curl -s "https://graph.facebook.com/v26.0/act_<ACT_ID>?fields=name,account_status,currency,timezone_name&access_token=<TOKEN>"

# 5c. Can I read Insights? (spend/impressions/ctr for last 7 days)
curl -s "https://graph.facebook.com/v26.0/act_<ACT_ID>/insights?date_preset=last_7d&fields=spend,impressions,ctr,cpm&access_token=<TOKEN>"
```

**Expected:** JSON with real data. `account_status: 1` = active. If 5b/5c error, jump to [§9 Troubleshooting](#9-troubleshooting).

---

## 6. Validate WRITE access (the 15-minute test that de-risks everything)

This confirms the system user can actually mutate the rented account — the one thing that's uncertain with a shared-in account. We create a **paused** campaign (spends nothing) and then delete it.

```bash
# 6a. Create a PAUSED campaign (no budget, no delivery — safe)
curl -s -X POST "https://graph.facebook.com/v26.0/act_<ACT_ID>/campaigns" \
  -F "name=API_WRITE_TEST_delete_me" \
  -F "objective=OUTCOME_SALES" \
  -F "status=PAUSED" \
  -F "special_ad_categories=[]" \
  -F "is_adset_budget_sharing_enabled=false" \
  -F "access_token=<TOKEN>"
# → returns {"id":"<CAMPAIGN_ID>"}  ✅ write works
# NOTE: v26 requires is_adset_budget_sharing_enabled (true/false) on any campaign
# not using campaign budget (CBO). Omitting it → error 4834011.

# 6b. Clean up — delete the test campaign
curl -s -X DELETE "https://graph.facebook.com/v26.0/<CAMPAIGN_ID>?access_token=<TOKEN>"
# → {"success":true}
```

**If 6a returns a campaign ID, write access is confirmed** and we are NOT blocked by the "Full Access / App Review" wall — the shared-in ad account behaves like an in-BM asset. 🎉
**If 6a fails** with `(#274)` or a permissions error, see [§9](#9-troubleshooting) — usually a missing task on the system user or a missing scope.

---

## 7. Wire the official Meta Ads MCP into Claude Code

Meta ships a first-party MCP server at **`https://mcp.facebook.com/ads`** (launched Apr 2026) — this is what lets Claude read/act on ads directly, the sanctioned way. Official get-started doc: <https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-get-started>

Add it to Claude Code with your system-user token as a bearer header:

```bash
claude mcp add --transport http meta-ads https://mcp.facebook.com/ads \
  --header "Authorization: Bearer <TOKEN>"
```

Then in a Claude Code session:
```bash
/mcp        # should list "meta-ads" as connected
```

Notes:
- The MCP also supports an interactive **Facebook Login for Business (OAuth)** flow instead of a bearer token. For **unattended** use, the **system-user bearer token is the right choice** (OAuth sessions expire). If the exact header name differs, follow the get-started doc above — it's authoritative.
- Once connected, Claude can call the MCP's tools (reporting, campaign/ad create+edit, A/B tests, activity logs). We'll drive those from the engine in phase 2+.
- **Scope guard:** as BM owner you can set **per-account rules** on what the MCP is allowed to do (e.g. allow reporting + budget edits, block campaign deletion). Do this once we go live — for now read + the paused-campaign test is enough.

Quick MCP sanity check inside Claude: ask it to *"use the meta-ads MCP to pull last-7-day spend and ROAS for our ad account."* If it returns numbers, the loop is closed.

---

## 8. Access tier + rate limits (FYI, no action)

- **Marketing API Access Tier** (formerly "Ads Management Standard Access"): new apps start at **Limited Access**, which works **without App Review** on assets **in your own Business** — including assets shared into it, like our rented account. That's why §6 should just work.
- **Full Access** (higher limits, needed only to operate across other businesses) is granted automatically after **500+ successful API calls in a trailing 15 days with <15% error rate** — we'll cross that naturally; no application needed for our use.
- **Rate limits** at our budget ($30–100/day) are a non-issue. One hard cap to know for the engine: **budget edits are limited to ≤4 per hour per ad set** (we scale on a multi-day cadence, so fine).
- Ref: <https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/rate-limiting>

---

## 9. Troubleshooting

| Symptom | Cause | Fix |
| :-- | :-- | :-- |
| `(#274) ... not enabled for usage in Ads API` or *"owner has not granted ads_management"* | System user missing a **task** on the ad account, or token missing `ads_management` | §3.2 — assign the ad account to the system user with **Manage campaigns**; regenerate token with `ads_management` scope |
| `(#200) Permissions error` on write | Missing scope or role too low | Ensure token has `ads_management`; system user role is Admin (or has full ad-account tasks) |
| `Invalid OAuth access token` | Token typo / truncated / revoked | Re-copy from Business Settings; tokens are long — ensure no line breaks |
| Read works, write (§6) fails | Cross-BM boundary forcing Full Access (rare for shared-in assets) | Send me the exact error — we may need the ad-account *owner* (the renter) to confirm the share includes management, or pursue App Review as a fallback |
| MCP shows "failed"/not connected | Wrong header/token, or org policy | Verify the bearer token works via §5 curl first; re-check the header name against Meta's get-started doc |

Useful tool: **Access Token Debugger** — <https://developers.facebook.com/tools/debug/accesstoken/> — paste the token to see its scopes, expiry (should say "Never"), and associated app.

---

## 10. What to hand back to me

Once §5 and §6 pass, send me:
1. ✅/❌ **Read test** (§5) and **Write test** (§6) results — for write, just "got a campaign ID, deleted it, success."
2. **Ad account:** the `act_<ID>`, its **currency**, and **timezone**.
3. **`/mcp` shows `meta-ads` connected?** (§7) ✅/❌
4. Any errors you hit (paste the JSON).

Do **not** send me the token itself — keep it in `.env`.

With that confirmed, I'll build **phase 2: the read-only decision engine** — it pulls Insights via the MCP, computes each product's break-even CPA/ROAS, applies the kill/keep/scale methodology, and produces a daily call sheet. We prove the *decisions* are right before it ever moves real budget.

---

### Security checklist
- [ ] `.env` holds the token; confirmed gitignored (`git status` should NOT list it).
- [ ] Token never pasted into chat, docs, or commits.
- [ ] Token expiration = **Never** (system user) — treat as a password; rotate if ever exposed.
- [ ] Per-account MCP rules set before enabling unattended **write** (phase 4), not now.
