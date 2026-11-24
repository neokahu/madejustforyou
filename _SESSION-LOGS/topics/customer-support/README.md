# Customer support (Freshdesk + Shopify)

Code and design: `ops/customer-support/README.md`. Branch `customer-support`.

## State (2026-11-24)
- Built: Freshdesk client, read-only Shopify order lookup (app `mj4u-orders`), 15 order stages with reply
  templates, FAQ knowledge base (33 questions, all `needs_answer`), CLI (`inbox`, `ticket`, `send --yes`, `kb`, `demo`),
  offline tests in `scripts/verify.sh`.
- 2026-11-24: **live.** Shopify app installed, Freshdesk key added; `inbox` and `ticket` verified on the 3 Freshdesk
  sample tickets (all correctly "no order"). Order names are `#MJ4U####`. Email-based order lookup returns no error
  but is unconfirmed against a real customer email (the sample tickets aren't customers).
- Designed, not built: confidence score from `Draft.signals` + Slack thread approval loop (README "Future").

## Decisions
- Runs inside a Claude Code chat session (low volume); nothing is sent without the owner's explicit yes.
- Stage thresholds 2 / 4 / 10 days (unshipped), 14 days (shipped, undelivered); editable in `config/support.json`.
- Shopify query avoids Protected Customer Data fields; the name comes from Freshdesk.
- Slack over Telegram for the future approval loop (threads + buttons).

## Open (owner)
- Delete the 3 Freshdesk sample tickets; send one test ticket from an email that has a real order to confirm email lookup.
- Confirm the 4 store facts (production time, shipping time, edit window, support hours) and the stage thresholds.
- Answer the 32 KB questions (`python3 -m cs.run kb`).
