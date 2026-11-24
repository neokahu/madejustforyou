# Customer support: Freshdesk tickets + Shopify order check

Ticket volume is low, so this runs **inside a Claude Code chat session**, not as a server. Claude pulls the
tickets, checks each customer's order on Shopify, drafts a reply, and you approve or correct it in chat.
Nothing reaches a customer until you say so.

## How a session runs

```
you: "check support"
  1. python3 -m cs.run inbox           -> open/pending tickets, each with its order stage
  2. python3 -m cs.run ticket <id>     -> thread + orders + stage + KB hits + draft + flags
  3. you: approve / "change X" / give the answer      (Claude rewrites; loop until you OK it)
  4. python3 -m cs.run send <id> --file <draft> --yes  -> posts the reply, logs it to log/
  5. new answer worth keeping -> added to kb/faq.json as approved
```

Run commands from `ops/customer-support/`. `python3 -m cs.run demo` shows the whole flow offline on fixtures.
Stdlib only, no installs.

## Order stages (`cs/stages.py`, thresholds in `config/support.json`)

Checked in this order; the first match wins. Days are calendar days by default (`day_count: "business"` switches).

| Stage | Rule | Reply | Escalate? |
|---|---|---|---|
| CANCELLED / REFUNDED / PAYMENT_PENDING | order cancelled / refunded / payment not complete | factual | yes |
| DELIVERED | carrier says delivered | ask what's wrong, ask for a photo | yes |
| DELIVERY_ISSUE | carrier failure / attempted delivery | "looking into it" | yes |
| PARTIALLY_SHIPPED | some items shipped | tracking + "rest ships separately" | no |
| SHIPPED_DELAYED | shipped ≥ 14 days, not delivered | "checking with carrier" | yes |
| SHIPPED | shipped, in transit | tracking link | no |
| ON_HOLD | fulfillment on hold | "checking a detail" | yes |
| JUST_PLACED | unshipped, ≤ 2 days | "just placed, being processed" | no |
| IN_PRODUCTION | unshipped, 3–4 days | "in production now" | no |
| SHIPPING_SOON | unshipped, 5–9 days | "in production, ships soon" | no |
| OVERDUE | unshipped, ≥ 10 days | "checking with production team" | yes: check the POD supplier first |
| NO_ORDER_FOUND / MULTIPLE_ORDERS | no match / can't tell which | ask for the order number | no |

The order is found by an order number in the ticket text (`#1234`), else by the requester's email.
Reply wording is in `config/stage-replies.json`. Edit it there, not in code.

**Store facts** (`config/support.json → facts`): production time, shipping time, edit window and support hours are
**placeholders (`confirmed: false`)** until you confirm them. Every draft that uses one is flagged.

## Knowledge base (`kb/faq.json`)

33 standard e-commerce and personalized-gift questions in 9 categories. Each entry has:
`question`, `keywords` (for matching), `answer_raw` (your answer, as you gave it), `answer` (the customer-facing
rewrite), and `status`: `needs_answer` → `draft` (rewritten, awaiting your OK) → `approved`.

- `python3 -m cs.run kb` lists the questions still needing an answer; `kb list` lists all; `kb show <id>` shows one.
- Workflow: you give a rough answer in chat → Claude stores it in `answer_raw`, writes the polished `answer`, and sets
  `draft` → you OK it → `approved`. Only approved answers go into drafts without a flag.
- `order-status` is special: its answer is the stage reply above.

Matching is keyword-based (`cs/kb.py`). The `match(text) -> [Hit(entry, score, matched)]` interface stays the
same if the KB later moves to Supabase with embeddings.

## Access needed

| What | Secret names in `~/.global-keys.env` | State |
|---|---|---|
| Freshdesk | `FRESHDESK_DOMAIN`, `FRESHDESK_API_KEY` (Profile settings → API key) | **not set up yet** |
| Shopify | `SHOPIFY_STORE_DOMAIN`, `SHOPIFY_ORDERS_CLIENT_ID`, `SHOPIFY_ORDERS_CLIENT_SECRET` (app `mj4u-orders`, read_orders + read_customers) | keys present; **app not installed on the store yet** (token request returns 400) |

Shopify notes: the code asks only for order, fulfillment and tracking fields, not customer name, email or
address, so it doesn't depend on Protected Customer Data approval. The email is used only as a search filter.
If Shopify refuses that filter without approval, request Protected customer data in the Dev Dashboard. Without
the `read_all_orders` scope, only orders from the last 60 days are visible.

## Future (designed, not built): confidence score + Slack approval loop

The seam already exists: every draft carries `signals` (`cs/draft.py`), and every send is logged to
`log/sent.jsonl` with whether the draft was edited. That log is the training data.

**1. Score (0–100), a pure function of `Draft.signals`.** Start rule-based, tune on the log:

| Signal | Effect |
|---|---|
| order found, single order, stage not escalate | + |
| KB top hit `approved` and score ≥ 0.75 | + |
| uses an unconfirmed fact | − |
| escalate stage (OVERDUE, DELIVERY_ISSUE, refund…) | cap at "needs human" |
| two intents tie / no KB match / no first name | − |
| history: share of past drafts for this (intent, stage) sent unedited | + (once the log has volume) |

Bands: **≥ 85** could auto-send later (only after the log shows it's safe) · **50–84** send to Slack for approval ·
**< 50** send to Slack marked "needs your answer".

**2. Slack approval loop (threads).** A small worker (cron or Freshdesk webhook) posts one Slack message per
ticket: customer message, order stage, draft, score, flags, with **Approve** / **Edit** buttons.

- You reply **in the thread** with what to fix ("mention the Dec 11 cutoff", "offer a free remake").
- The worker redrafts with Claude, using the thread as instructions, and posts the new version in the same thread.
- This repeats until you press **Approve**. Then it posts the reply to Freshdesk and logs the final text, the
  number of rounds and your edits.
- Edits that recur become KB updates (proposed in the thread; you approve).

Slack over Telegram because threads keep each ticket's back-and-forth together, and Block Kit buttons give
one-click approval. Build order when the time comes: Slack app (bot token, interactivity URL) → worker (Supabase
edge function or a small server) → reuse `cs/` for the logic.

## Files

```
cs/config.py       paths, config, secrets          cs/freshdesk.py   Freshdesk v2 client (reply/note = writes)
cs/shopify.py      read-only order lookup           cs/stages.py      order -> stage (pure, tested)
cs/kb.py           FAQ load/match                    cs/draft.py       ticket + orders -> Draft (text, flags, signals)
cs/run.py          CLI                                config/           thresholds, facts, stage replies
kb/faq.json        knowledge base                    tests/            offline tests + fixtures (run by scripts/verify.sh)
log/               sent replies (gitignored: holds customer text)
```
