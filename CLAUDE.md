# MadeJustForYou (MJ4U)

Shopify print-on-demand **personalized-gift** store. This repo is the research, ad production, FB-ads automation, Teeinblue asset and session-log workspace. The storefront theme is a separate repo (`THEME-REPO.md`). Product IDs are `MJ4U-NNN`.

## Start of every session

1. Read `_SESSION-LOGS/INDEX.md` (the `⏸ RESUME HERE` block and state table), then only the `topics/<topic>/README.md` for your task. Never load every session log.
2. Use `PROJECT-INDEX.md` as the map of where things live.
3. Run `bash scripts/verify.sh` for a green baseline before changing anything.
4. Active work is on branch `product-research` (worktree `~/Desktop/projects/worktree/madejustforyou/product-research`); `main` lags behind until merged.

## Hard rules

Each rule comes from a real incident; the detail is in the linked doc or session log.

- **Theme repo: code only, and `main` is the live store.** Merging or pushing to `main` in `madejustforyou-theme/shopify-theme-1` publishes to production; there is no separate publish step. Never write notes, logs or READMEs there; they live here. Why: Shopify syncs that repo.
- **Follow the plan page.** The Phase-1 testing plan (`marketing/facebook-ads/testing-plan-page/`) decides what gets tested. Scripts are written by the screenwriter agent and reviewed per case, never by hand, and the plan is never restructured. Why: ~$5 of assets built on an off-plan restructure (2026-10-08).
- **Read the prompt doc before any image/video generation.** The PreToolUse guard (`research/scripts/generation-prompt-guard.py`) blocks prompts that break `research/reference/seedance-prompt-method.md` and `image-to-video-prompt-method.md`. Why: three failed generations in one session from ignoring the documented method (2026-09-26).
- **Casting matches the caption.** Check every person shot's gender, age and role against the caption pronouns; avoid hands-only hand-offs when identity matters. Why: S-C6 read as "giving the gift to some other man" (2026-10-08).
- **Gift ads show family connection.** Relatives giving the gift and happy-family memories, never the giftee alone. Why: solo shots read as lonely on MJ4U-111.
- **Ad primary text uses line breaks**, authored as an array of lines in `products/<id>/ads/ad-content.json`; `engine/upload_draft.py --validate-only` enforces it.
- **Kill or scale only on settled days** (yesterday and earlier). Meta's in-day ATC and purchase counts are estimates that revise down.
- **WinningHunter: confirm the exact brand before a pull**, and query by landing domain (`searchkeyword=landingurl`), not page name. Why: fuzzy page matching pulled the wrong brand and burned credits.
- **Product tracker: one writer, two copies.** Update `products/_registry/product-tracker.csv` and re-push the Google Sheet in the same step (method in `products/_registry/README.md`).
- **Test-plan deck lives on Cloudflare only** (`marketing/facebook-ads/test-plan-deck/`, `npx wrangler@4 deploy`). Never recreate a claude.ai copy.
- **Media stays out of git.** Never `git add -f` media; back up with `scripts/backup-media.sh` (rclone to Drive). The pre-commit hook blocks files over 5 MB (`git config core.hooksPath .githooks`).
- **Secrets:** API keys are in `~/.global-keys.env` (check before asking for a key; never print values). `.env` files stay untracked.
- **Commits:** plain messages, no `Co-Authored-By` or Claude attribution. Another session may share this worktree: commit only your own paths.

## Definition of done

- `bash scripts/verify.sh` exits 0.
- **Ad builds:** plan page followed, guard passed (or an `ACK-<RULE>` explained to the user), casting checked against captions, media backed up.
- **Engine or kill-rule changes:** a test covers the change; if a sample verdict moves on purpose, update `EXPECTED` in `engine/tests/test_engine.py` in the same commit.
- **Anything live** (ads, deck, plan page, theme): the URL or ID is recorded in the topic README.
- **Handoff:** the `session-handoff` skill, with the `⏸ RESUME HERE` block first in `INDEX.md` and the session log (`Nothing in flight` if nothing is open).

## Where things are

| What | Where |
|---|---|
| Current state, decisions, open threads | `_SESSION-LOGS/INDEX.md` → `topics/` → `sessions/` |
| Map of the repo | `PROJECT-INDEX.md` |
| Video ad pipeline (7-role team, `/video:new`) | `research/reference/video-team/README.md`, `.claude/agents/vt-*` |
| FB-ads engine (read-only `run.py`, dry-run-by-default `execute.py`) | `marketing/facebook-ads/engine/`, `marketing/facebook-ads/README.md` |
| Ads database (Supabase `mj4u-ads`) | `marketing/facebook-ads/db/`, `engine/db_sync.py` |
| Teeinblue mechanics, asset library | `research/reference/teeinblue-assets-guide.md`, `library/personalizer/ASSET-SYSTEM.md` |
| SOPs (Vietnamese) | separate repo `../sop-docs` |
| Verification | `scripts/verify.sh`, rules in `harness-rules.json` |
