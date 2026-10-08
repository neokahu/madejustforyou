# Handoff — Research consolidated, TopView dropped, blanket script revision pending (2026-10-08)

## ⏸ IN PROGRESS — RESUME HERE

Nothing is mid-generation and nothing is broken; this is a **decision/approval queue**, in priority order.

### 1. REF-OWNER 8-image character reference set — two views flagged, need regeneration (~$0.60 total)

Lives at `products/suncatcher-dog-memorial/assets/turntable-owner/` (local only — see item 2):
`owner-front.png`, `owner-34left.png`, `owner-34right.png`, `owner-fullbody-standing.png`,
`owner-fullbody-seated.png`, `owner-hands.png`, `owner-expr-relief.png`, `owner-expr-smile.png`,
`reference-set-qa.png`.

| File | Problem | Fix to apply on regeneration |
|---|---|---|
| `owner-hands.png` | The two hands overlap on one knee — individual fingers can't be confirmed as 5-per-hand, and it adds a gold wedding band no other reference view establishes | Regenerate: hands apart, no ring |
| `owner-expr-relief.png` | Reads as a plain smile, nearly identical to `owner-expr-smile.png`, not "quiet relief" | Regenerate with a neutral mouth, breath-out cue, no smile |

Full QA table: `research/reference/image-prompt-method.md` §"Character reference set — template" → "QA result — 2026-09-29".

### 2. `*.png` is gitignored REPO-WIDE — the reference images have never been committed

Verified this session with:

```
$ git check-ignore -v products/suncatcher-dog-memorial/assets/turntable-owner/owner-front.png
.gitignore:7:*.png	products/suncatcher-dog-memorial/assets/turntable-owner/owner-front.png
```

`.gitignore` line 7 is a repo-wide `*.png` rule with no exception for `assets/`. **An earlier claim this
session that `assets/` paths survive the gitignore was WRONG** — they do not, at least not for `.png`.
(Two other product PNGs are tracked in git despite living under `assets/` —
`products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png`,
`.../REF-ALEX-PHOTO.png`, and `products/blanket-granddaughter/assets/product-sweetie-pie-blanket.png` —
but those were force-added in an earlier session, as recorded in
`_SESSION-LOGS/2026-09-26-testing-complete-both-products.md`'s "Committed assets" line. The 8-image
turntable set was never force-added, so it is untracked and would be lost on a fresh clone.)

**Decision needed next session:** whether to `git add -f` the reference images so they're versioned.
**Do not force-add them without the user's explicit go-ahead** — this handoff only records the decision
as pending.

### 3. Awaiting user approval

- `marketing/facebook-ads/PHASE1-SUNCATCHER-shooting-scripts.md` needs revision per
  `research/reference/script-method.md` §4a before it can be approved: product must be in frame from
  second 1 (fixes specified for Hook 2 and Body C in that table), shot lengths varied 2–5s with hard cuts
  only (no uniform 5s beats). **Not yet edited.**
- **Open, separate from the above:** child vs adult rendering of the granddaughter for the blanket
  product — the printed figure is a child, the current test renders (D4/D5) cast her as an adult. Blocks
  nothing yet, but blocks the "growing up" timelapse concept's final form.

### 4. Next build task (once the above approvals land)

A **vertical slice** of shot S-C1-H1, end to end, on AtlasCloud, using `reference_to_video` with all 8
owner reference images (~$2 estimated) — this is the first real test of whether the 8-image reference set
actually holds identity across multiple independently-generated clips, which no test has exercised yet
(every clip so far used single-frame `image_to_video`).

Then, for the blanket product, build two creatives in parallel:
- **Control:** hands + poem + grandma VO — the NW/niche-winner pattern (near-zero cost, closest to the
  only verified-adjacent winners).
- **Challenger:** the user's "growing up" timelapse concept — blanket visible in every shot across ages,
  grandma alive and present throughout and returning in the final beat, each age cast to match the
  product's printed figures, written in third person per Meta's Personal Attributes policy.

### 5. REF-GIVER and the blanket product's characters have no reference sets yet

Neither the sympathy-giver character (REF-GIVER, for the suncatcher's Body C) nor any of the blanket
product's characters (grandma, granddaughter at any age) has an 8-image reference set built. This blocks
clips 6–11 of the suncatcher inventory (all marked "person, model TBD" in the shooting script) and all of
the blanket build.

---

## Summary

This session did no new generation and ran no new tests. It **consolidated** everything produced across
the 2026-09-25 → 2026-09-29 research run into one report, corrected a stale recommendation that a later
finding had quietly invalidated, and recorded several facts that existed only in conversation (never
written to any doc) so they survive past this session.

## Key decisions this session

| Decision | Reasoning | Where recorded |
|---|---|---|
| **TopView dropped for video generation** | Measured cost ~13× AtlasCloud for the identical Seedance 2.0 model; Motion Control broken via MCP (4/4 failed attempts); all 3 advertised differentiators (Unlimited, 3D Shot Composer, Motion Control) are GUI-only or non-functional through automation | `research/reference/topview-evaluation-2026.md` (amended), `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` §4a, memory `topview-for-plates-not-products.md` (amended) |
| **Routing: images → kie.ai → AtlasCloud fallback; video → AtlasCloud → kie.ai fallback** | User decision this session | Research report §4c |
| **`ai-film-studio.md` pipeline demoted** | Its MJ4U-111 film scored hook3 3.59 vs the measured benchmark of 18.05 | memory `ai-film-studio.md` (amended), already partly reflected in repo commit `dc54dbe` |
| **Character reference method = 8 separate full-resolution images, not one multi-panel sheet** | A ~50-panel sheet gives ~200–300px per face; sheets need text labels that contradict "no text"; Nano Banana has no negative-prompt field; the user's proposed JSON reference-sheet prompt ran ~700 words and was rejected | `research/reference/image-prompt-method.md` |
| **ComfyUI deferred, not adopted** | Can't run our actual models (Seedance/Nano Banana/GPT Image/Kling) natively; needs a 24GB+ GPU the user doesn't have; revisit only if 8-image references can't fix identity drift | Research report §4e |

## Achievements

- Read and cross-referenced 13 source documents from the 2026-09 research run (prompt methods, text
  fidelity, TopView eval, prompt guard, script method, 4 sprint reports, blanket README, shooting script,
  prior handoff).
- Wrote `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` — one consolidated, table-first
  reference covering video prompting, image prompting, text fidelity, platforms/cost, script method,
  character references, the prompt-guard hook, what changed, and open questions. Every finding is cited
  to its source file or named test.
- Amended `research/reference/topview-evaluation-2026.md`: added a dated note at the top pointing to the
  reversal, and a new "SUPERSEDING VERDICT" section before Sources with the full DROP reasoning and cost
  table. The original 2026-09-25 test-run record is preserved unchanged as history.
- Verified, rather than assumed, the gitignore behavior on the turntable reference images (`git
  check-ignore -v`) — corrected a wrong claim from earlier in this session (see IN PROGRESS item 2).
- Updated 3 files in the separate project-memory directory (not this repo) — see "Memory" below.

## Current state

- Working tree is clean and pushed as of this handoff (verify with `git status` /
  `git log origin/HEAD..HEAD` — both should be empty by the end of this session's commits).
- No generation is in flight. No credits were spent this session (pure read/compile/write work).
- The shooting script (`PHASE1-SUNCATCHER-shooting-scripts.md`) and the blanket README reflect their
  state from the prior session (2026-09-29) — this session did not edit either; the required revision to
  the shooting script (item 3 above) is still pending.

## Operational state

| What | Value |
|---|---|
| TopView canvas | `4ed6f979c13244c9b8ba102ae2d14d91` |
| TopView credits remaining | **28.96** (user bought 25 on top of a free allotment; the 4 failed Motion Control attempts cost 0) — given the DROP verdict, consider cancelling the monthly plan |
| AtlasCloud balance | ~$48.89 as of last check |
| kie.ai balance | **Untracked/blind** — its balance-check endpoint returns no usable number |
| Free TopView MCP quota remaining | 4 MiniMax-H3 video · 3 Wan 3.0 video · 7 GPT Image 2.5 (1K) image |
| Prompt guard hook | `~/.claude/hooks/generation-prompt-guard.py`, mirrored at `research/scripts/generation-prompt-guard.py`, registered in `.claude/settings.json`. Covers kie.ai, AtlasCloud, TopView image+video generation. Per-model rules: `GPTTERSE`, `NANOREL`, `SEEDQUOTE`. `motion_control` task type is exempt from shot-structure rules. Word caps: image prompts 250, structured video prompts 220, freeform prompts 100 |
| Signed URLs | TopView canvas CloudFront URLs expire ~2026-10-04 — **already expired** as of today (2026-10-08). kie.ai tempfile URLs expire 14 days after generation. Any asset referenced by an old URL needs re-downloading/re-uploading before reuse |

## Files changed this session

| File | Change |
|---|---|
| `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` | **New.** Consolidated report, 9 sections, tables throughout |
| `research/reference/topview-evaluation-2026.md` | **Amended.** Dated note at top pointing to the reversal; new "SUPERSEDING VERDICT — DROP" section before Sources. Original 2026-09-25 record preserved |
| `_SESSION-LOGS/2026-10-08-research-consolidated-handoff.md` | **New** (this file) |
| `/Users/neovh34/.claude/projects/-Users-neovh34-Desktop-projects-madejustforyou/memory/topview-for-plates-not-products.md` | **Amended** — DROP verdict, reasons, historical note on what TopView was used for (see memory section below) |
| `/Users/neovh34/.claude/projects/-Users-neovh34-Desktop-projects-madejustforyou/memory/ai-film-studio.md` | **Amended** — demotion note added near top |
| `/Users/neovh34/.claude/projects/-Users-neovh34-Desktop-projects-madejustforyou/memory/MEMORY.md` | **Amended** — index line for `topview-for-plates-not-products.md` updated; one-line pointer to the new research report added |

No code files changed — this was a documentation/research-consolidation session. See `git log --oneline
-15` for everything before this session (research-report writing, script-method sprint, owner reference
set, prompt guard extension) — all already committed and pushed before this session began.

## Prior session's evidence, still valid

Everything in `_SESSION-LOGS/2026-09-26-testing-complete-both-products.md` and
`research/sprints/2026-09-script-method/*.md` remains the primary evidence; this session only compiled
and cross-checked it. See `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` for the
consolidated view — that report is now the fastest way back into this material, link to it rather than
re-deriving.
