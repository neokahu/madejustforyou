# Customer support (Freshdesk + Shopify)

Code and design: `ops/customer-support/README.md`. Branch `customer-support`.

## State (2026-11-24)
- Built: Freshdesk client, read-only Shopify order lookup (app `mj4u-orders`), 15 order stages with reply
  templates, FAQ knowledge base (33 questions, all `needs_answer`), CLI (`inbox`, `ticket`, `send --yes`, `kb`, `demo`),
  10 offline tests in `scripts/verify.sh`. Tested on fixtures only; never run against live data.
- Designed, not built: confidence score from `Draft.signals` + Slack thread approval loop (README "Future").

## Decisions
- Runs inside a Claude Code chat session (low volume); nothing is sent without the owner's explicit yes.
- Stage thresholds 2 / 4 / 10 days (unshipped), 14 days (shipped, undelivered); editable in `config/support.json`.
- Shopify query avoids Protected Customer Data fields; the name comes from Freshdesk.
- Slack over Telegram for the future approval loop (threads + buttons).

## Open (owner)
- Install `mj4u-orders` on the store (install link in `sessions/2026-11-23-mj4u-133-c0-shopify-ids.md`, product-research branch).
- Create the Freshdesk account; add `FRESHDESK_DOMAIN` + `FRESHDESK_API_KEY` to `~/.global-keys.env`.
- Confirm the 4 store facts (production time, shipping time, edit window, support hours) and the stage thresholds.
- Answer the 32 KB questions (`python3 -m cs.run kb`).
