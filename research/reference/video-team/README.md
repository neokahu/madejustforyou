# Video Team: methodology for MadeJustForYou paid video ads

> **Status:** adopted 2026-11-18. It **supersedes** the AI Film Studio (`research/reference/ai-film-studio.md`, `.claude/agents/film-*`, `/film:new`). That studio was demoted on 2026-09-26.
> **Scope:** Meta (FB/IG) paid video ads for personalized gifts, 15–25s, 9:16 + 4:5, usually AI-made, tested as concepts × hooks.
> **Tool-agnostic by rule** (user, 2026-11-18): *"focus on methodology, not specific tools. Our method must work using whatever AI tool to generate videos."*
> Roles define decisions, inputs and outputs, rubrics and gates. Prompt craft for a specific tool lives in `adapters/`.
> **Origin:** adapted from a 7-assistant AI-reel pipeline (hook ideator → hook critic → hook selector → script → visual director → reel builder → QA). That pipeline makes organic 60s talking reels. Every change from it is listed and justified in §5.
> **Evidence:** each role's graded research (STRONG / MODERATE / WEAK, with URLs) is in `role-research/`. This file is the operating summary. The research files hold the detail and the reasons.

---

## 1. The pipeline at a glance

```
 PLAN CELL ──► 01 IDEATE ──► 02 CRITIQUE ──► 03 SELECT ──► 04 SCRIPT ──► 05 DIRECT ──► 06 ASSEMBLE ──► 07 QA ──► UPLOAD
 (concept ×      15+ hook      gates + blind    1 hook per     timed beat     shot list,      control first,    PASS/FAIL,
  hook arms)     cards         3-judge score    test arm       table + copy   refs, assets    variants derived  timestamped
                                                                    │              │                                  │
                                    GATE A: user approves ─────────┘   GATE B: refs │   GATE C: shots pass 07          │
                                    hooks + script                    approved      │   (shot mode) before assembly    │
                                                                                     └──────────── GATE D: final 07 PASS ┘
```

| # | Role | One-line mission | Main output |
|---|---|---|---|
| 00 | **Producer** (the run command / main session) | Runs the pipeline for one plan cell. Holds the budget, enforces the gates, and takes structural questions to the user. | run log |
| 01 | **Hook Ideator** | A wide pool of producible hooks across many mechanisms, built as *cards* (frame-1 visual + caption) | `hooks/01-candidates.md` |
| 02 | **Hook Critic** | Removes defective hooks and scores the rest on an anchored rubric. It is a **filter**, not a fortune-teller | `hooks/02-scores.md` |
| 03 | **Hook Selector** | **One hook per pre-registered test arm** (≥2 arms per concept). Arms must be visibly distinct; each has one reserve | `hooks/03-selection.md` |
| 04 | **Script Editor** | A timed, word-budgeted beat script. It pays off the hook, keeps the product present and reads with sound off. Plus the ad copy | `script.md` |
| 05 | **Visual Director** | Every second shows what its words say. Product truthful from frame 1. References locked before any shot | `shotlist.md`, `refs/`, briefs, assets |
| 06 | **Editor / Assembler** | Locked inputs → reproducible deliverables: 9:16 + 4:5 per ad, control first, variants derived | renders + `recipe.md` + log row |
| 07 | **QA / Gatekeeper** | Independent PASS/FAIL against the locked criteria. Defects are timestamped and each has a fix owner | `qa/<file>.md` |

## 2. Rules that hold across all roles

1. **The plan page is the test authority.** No role restructures a test (concepts, arms, length, CTA, offer). Structural questions go to the user. A council may fix craft *inside* a cell (memory `follow-plan-page-scripts-via-agent`).
2. **Criteria before building.** Before any render, the Producer compiles the criteria sheet from every relevant doc (template: `marketing/facebook-ads/suncatcher-phase1/EDIT-CRITERIA.md`) and locks it. 06 builds to that sheet and 07 judges against it.
3. **Separation of making and judging.** Whoever made something never gives it the final grade:
   - 02 is never 01, and 03 never wrote the hooks.
   - 05 self-checks, but 07 accepts its references and shots.
   - 06 self-checks, but 07 gives the final pass.

   A model rating its own output is biased toward it (self-preference: Panickssery et al., NeurIPS 2024 [STRONG]).
4. **Describe the character, never the viewer.** Meta's Personal Attributes policy applies to every text surface (`script-method.md` R6, HARD).
5. **The product is never invented.** Its shape, artwork and printed names come from the real product. A generator never draws the product's text, and when the name *is* the proof, the shot is a real high-res still with a camera move added in the edit (`role-research/05` c7–c8, c13).
6. **Show connection, not a lonely giftee.** Casting matches the printed artwork and every caption pronoun.
7. **No invented facts:** no stats, counts, reviews or testimonials unless they are in the product fact sheet and true (FTC rule 2024).
8. **Test integrity:** variants of a cell differ *only* on the tested axis, with zero frame or audio difference outside the tested window.
9. **Everything is logged:**
   - Hooks go to the **hook ledger** and visual attributes to the **scene ledger**.
   - Builds get a **recipe** with hashes.
   - QA verdicts are recorded verbatim.
   - Media is backed up to Drive and never committed to git.
10. **Tool-agnostic:** roles name no generator, editor or voice engine. The tool used is recorded as free text in the recipe.

## 3. Roles

Each role's agent is `.claude/agents/vt-0N-*.md`. The full spec (procedure, rubric, failure modes) is in `role-research/`.

### 01 · Hook Ideator → `role-research/01-03-hooks.md` §2
- **A hook is a card, not a line.** Its fields: `id · arm · mechanism · cep (relationship × occasion) · frame1_visual · onset_0_5s · caption (≤10 words) · audio_cue (never needed to understand) · promise · paid_by (second) · asset_source · policy · rationale`. A caption with no frame is not a hook.
- At least 15 cards across **≥6 mechanisms** from the gift library (M1–M11: personalization reveal, relationship callout, reaction cold-open, private ritual, light/transformation onset, concrete curiosity gap, generic-vs-theirs contrast, giver POV, occasion, thought made visible, quiet social proof).
- **Self-reject:** clichés, lines about the viewer's attributes, a gift not identifiable muted by 3s, promises the body can't pay, near-duplicates (same frame + mechanism). Keep 8–10, at least 2 per arm.
- If a model ideates, run ≥2 independent passes and merge (this guards against monoculture).

### 02 · Hook Critic → `role-research/01-03-hooks.md` §2
- **Blind panel of 3 judges.** Different model families where possible, or include a human. Each judge sees a fresh random order, scores one card at a time, and quotes its evidence before scoring. The panel takes the median and flags any ≥2-point spread. Rationale and author stay hidden.
- **Stage A, binary gates (any fail = cut):**
  - G1: gift and recipient identifiable muted in 3s
  - G2: policy
  - G3: the body pays the promise within 3s of the hook
  - G4: producible from the real product
  - G5: casting matches the caption
  - G6: fits its test arm
- **Stage B, anchored scores 1–5, total /100:**
  - Stop power 25
  - Right-buyer relevance 20
  - Concrete open loop 15
  - Body pays it 25
  - Caption/cover legibility 15
- **Kill rules:** total below 70, any criterion at 1, or body-pays ≤2.
- **Calibration:** blind 4 past hooks with known hook rates into every batch. If the panel can't rank them correctly, its scores become advisory.
- The critic never rewrites a hook and never names a winner. Unaided pre-launch judgment is right only ~55% of the time; a principle checklist with several raters reaches ~75% (Armstrong 2016 [STRONG]).

### 03 · Hook Selector → `role-research/01-03-hooks.md` §2
- Within each arm, compare the top 2–3 head to head, **in both orders**. A flip counts as a tie, broken on payability.
- **Muted 2-second outsider cold read:** what is sold, for whom, what happens next. If "for whom" comes back wrong, use the reserve.
- **Body-pays re-test:** watch the hook together with seconds 2–6.
- **Distinctness:** arm winners must differ in **mechanism and frame-1 picture**, not just caption. Meta groups ads with the same visuals and different text as one creative [STRONG].
- **Output:** 1 winner + 1 reserve per arm, ≥2 arms per concept, and a frozen pre-registration line (hypothesis, primary metric = hook rate, gate, control).
- After launch, measured hook and hold rates go into the **hook ledger**, which becomes the critic's calibration set.

### 04 · Script Editor → `role-research/04-script.md`
- **Inputs** (missing = stop): plan cell, 12-field brief, chosen hooks (verbatim), a **closed product fact sheet** (F-IDs), cast sheet, policy pack, locked reused assets.
- **Beats** (the creator's 6 blocks adapted to story): **HOOK → STAKES** (the character's situation, never the viewer's) **→ TURN → PROOF** (the personalization legible on the real product, which pays the hook) **→ CONNECTION** (the relationship payoff, pivot about 55–65%) **→ CTA**.
- **Product early, payoff late:** the product is identifiable by 1s and pulsed across beats; no logo card at the start. **Promise paid by 12s** (20s ad) or 9s (15s ad).
- **Budgets:** captions ≤2.5 words/s, ≥2.0s each, ≤2 lines.
  - 20s ad: ≤45 caption words (aim 35–40), VO ≤40.
  - 15s ad: ≤33 caption words.
- **Output:** a beat table (timecode · purpose · visual intent · product presence · caption · dialogue/VO · other text · sound · words vs budget · traces-to), a header (one message ≤15 words, thesis, promise-paid line), ad copy as line-broken arrays, and a 15-item check report.
- **Anti-generic guards:**
  - every factual line cites an F-ID
  - a banned-cliché list
  - a swap test (would this line fit any other product?)
  - variants come from different angles and ≥2 independent passes
- The visual director may change *how* a beat is shown. Any change to *what* it shows comes back to 04.

### 05 · Visual Director → `role-research/05-visual-director.md`
- **Shot list, one row per shot:** `shot_id · tc · serves (the exact words on screen) · regime (energy/stability) · size/angle · camera_move (ONE, required; shot 1 must move) · subject+action located in space · source_type · refs_required · text_to_composite · continuity · takes · acceptance · cut in/out`.
- **Rhythm:** hook shots 1.0–2.5s, others 2–5s, never uniform, at least one scale jump per beat, hard cuts by default. Cut-rate target ≈0.4 cuts/s, provisional (based on n=1).
- **Reference lock (GATE B):** before any scene asset, build a reference sheet:
  - each recurring person: 8 views, 2–3 stable features, a must-not-change list
  - the product: a real hero photo plus a **scale-anchored plate**
  - the real lettering, cut out

  07 and the user approve it, never 05. Art and continuity stay inside 05 as a gated sub-function. Split them into a librarian role only once a cross-ad reference library exists.
- **Source choice, first match wins:**
  1. Product as proof → REAL-PHOTO / still + move added in the edit
  2. Product in a wide scene → generated from a start frame containing the real product
  3. Personal proof → CUSTOMER-PHOTO (permissioned)
  4. Human emotion → generated video from locked references
  5. Hands manipulating the product → imply the action, or best-of-N
  6. Metaphor → generated
  7. Generic motion → STOCK
  8. Text, name reveal, CTA → MOTION-GFX
  9. Still → still + move, never a frozen frame
- **Generation brief** (tool-agnostic template, §4 of the research file). An adapter turns it into a prompt, and the prompt guard checks it before any spend.
- **Draft cheaply, select from N.** Accept a shot on ≥5 full-res frames across the clip, and only within its **verified in/out window**.
- **Scene ledger:** keyed on setting · cast · framing · story. Block repeats across *different* concepts (30-day default). Allow logged reuse *inside* a controlled test. Frame 1 must differ from every running ad's frame 1 on at least 2 of setting, cast, framing and colour.
- **Covers:** frame 1 *is* the cover in paid autoplay, so frame-1 variants belong to the hook test. Deliver one deliberate thumbnail still. No "3 backgrounds" variants.

### 06 · Editor / Assembler → `role-research/06-07-edit-qa.md` §2
- **Inputs, all locked** (otherwise stop): cell map, script, accepted shots with in/out windows, caption sheet, **criteria sheet**, music + **licence evidence**, brand assets.
- **Control first; each variant = the control recipe with only the tested segment swapped.** Never time-stretch a performance; re-cut the picture instead.
- **Deliverables per ad:**
  - 9:16: target 1440×2560, floor 1080×1920
  - 4:5: target 1440×1800, **re-framed per shot**
  - Both: H.264, constant fps, stereo AAC ≥128 kbps
  - Loudness −16 LUFS (−18 when VO leads), true peak ≤ −1 dBTP measured after encoding
- **Captions:** phrase captions with an outline or box, one fixed band per ad and format. Word-highlight only with VO, inside a stable phrase.
- **Safe zones:** 9:16 keeps the top 14%, bottom 35% and 6% each side clear. 4:5 keeps ≥10% bottom and ≥6% sides clear.
- **Naming:** `{PRODUCT}_{CONCEPT}-{HOOK}_{VAR}_{RATIO}_v{NN}`. Versions are immutable. Each ad gets a **recipe** (hashes, in/out points, transforms, licence ID, the tool named as free text) that rebuilds the same frames, plus a measured self-check.
- The editor never marks its own work PASS and never chooses anything at random.

### 07 · QA / Gatekeeper → `role-research/06-07-edit-qa.md` §3 (+ `05` §2.7 for shot mode)
- **Two modes:**
  - **Shot mode (GATE B/C):** references and each generated shot, judged on identity, product truth, text, anatomy, physics, casting and the usable window.
  - **Final mode (GATE D):** the deliverables.
- It is a **different agent from the builder**. It measures first and reads the builder's self-check only afterwards. It judges only against the **locked** sheet; anything new becomes an S3 proposal.
- **Frame sampling:**
  - frame 1, 0.5s, 1s, 3s
  - every cut ±1 frame (planned vs detected)
  - every caption on/off
  - each shot's midpoint and the last frame
  - name beats on ≥5 frames
  - each variant's window against the control
  - then **real-time playback on a phone-sized screen, muted and then unmuted**
- **Checklist groups:** T technical · V visual · C captions · S story/brief · B brand · P policy/legal (personal attributes, product truth, **music licence**, FTC dramatization, **AI-performer disclosure**, flashing) · I test integrity (zero diff outside the window, same length/end card/formats, Advantage+ creative enhancements OFF for test cells).
- **Severity:** S1 blocker / S2 major / S3 minor. **PASS = zero S1 and zero S2.** Only the user waives an S2; S1 policy and rights items are never waived. A partial cell does not ship.
- **Defect line:** `[S#] file · timestamp · criterion · evidence · fix owner · re-check items`.

## 4. Artifacts and where they live

| Artifact | Path (docs in git; media gitignored → Drive) |
|---|---|
| Test cell docs | `marketing/facebook-ads/<test-id>/<cell>/` → `hooks/01-candidates.md`, `hooks/02-scores.md`, `hooks/03-selection.md`, `script.md`, `shotlist.md`, `briefs/`, `recipe.md`, `qa/` |
| Criteria sheet (locked per batch) | `marketing/facebook-ads/<test-id>/CRITERIA.md` |
| Media (refs, takes, renders) | `products/<product>/ads/<test-id>/…` (gitignored; `scripts/backup-media.sh`) |
| Hook ledger | `marketing/facebook-ads/_ledgers/hook-ledger.csv`: every shipped hook + mechanism + hook/hold rate |
| Scene ledger | `marketing/facebook-ads/_ledgers/scene-ledger.csv`: one row per shipped shot (§3 05) |
| Ad-creative log | `products/_registry/ad-creatives.csv` + Sheet `1gUb0PNN_My3vPlXJI2uR1cCJf6vBC79CMV4ulsZHFw0` (one row per ad × format) |
| Tool adapters | `research/reference/video-team/adapters/` |

## 5. What changed from the source pipeline (and why)

| Source pipeline | Ours | Why |
|---|---|---|
| Hooks are spoken/text lines | Hook **cards** with the frame-1 visual first | Feeds are watched sound-off. First-party guidance from all three platforms centres the opening visual |
| 15 → 6 → 3 → **1** winner | 15+ → 8–10 → survivors → **1 per arm, ≥2 arms per concept**, + reserves | In a paid test the market picks. Pre-launch picks are ~55–75% accurate, and a hook-rate test costs ~$21–88 |
| Critic scores its own team's hooks | Blind, independent 3-judge panel, gates first, calibrated against past hooks | Judge biases (self-preference, position, verbosity) |
| "Warning" mechanism | Dropped or rewritten in the third person | Addressing the viewer's loss breaks Meta's personal-attributes rule |
| 60s argument: hook-problem-reframe-proof-result-CTA | 15–25s story: hook-stakes-turn-proof-connection-CTA | Gift buyers buy the recipient's smile, and proof is the visible personalization, not statistics |
| "Pay the hook within 15s" | Paid by about 60% of runtime (12s in a 20s ad) | Same principle, scaled to our length |
| 3–6s per scene | Hook shots 1–2.5s, varied, hard cuts | Value is front-loaded (TikTok, Meta/Nielsen, eye square). Our film that cut every 36s failed |
| 4 visual sources | 9 source types by first-match rule, with real product mandatory as proof | FTC and Meta rules on misleading representation; generators draw the product wrong |
| Anti-repeat scene log | Scene ledger keyed on Meta's grouping attributes | Meta groups look-alike ads and counts fatigue per creative across campaigns |
| Characters 25–50, local | Casting by story role and printed artwork | Our hard rules (artwork, pronouns, connection, policy) come before demographics |
| 3 covers, one picked at random | Frame-1 variants belong to the hook test, plus one deliberate thumbnail | Randomness breaks a paid test; autoplay makes frame 1 the cover |
| Word-by-word karaoke captions | Phrase captions; highlight only with VO | No lift evidence, an accessibility cost, and the user found fast text unreadable |
| Fixed AI male voice | Voice is a per-concept variable; music-only by default | `script-method.md` R13; VO vs none is still open test T4 |
| QA: specs + frames + captions + visuals | Adds loudness and peaks, flashes, policy, **rights**, **test integrity**, severities, independence | A broken test cell wastes the spend even when the craft is perfect |

## 6. Open decisions (user)

1. ~~**AI-performer disclosure, New York.**~~ **Ruled 2026-11-18: no disclosure.** User decision, made knowing NY GBL §396-b (in effect 2026-06-09; $1k/$5k penalties) applies to AI-generated people in ads reaching NY. QA P5 = PASS by this ruling. Revisit if Meta starts requiring it or a complaint arrives.
2. ~~**Music licence.**~~ **Resolved 2026-11-18:** user says the suncatcher bed is AI-generated ("voicelabs"), no third-party IP. Licence evidence for AI music = service + plan tier (must be a paid/commercial plan) + generation date + terms URL, recorded in the build recipe. Still to confirm: generated on a paid plan.
3. ~~**Ad-creative log.**~~ **Done 2026-11-18:** `products/_registry/ad-creatives.csv` (canonical, git) mirrored to its own Google Sheet **`1gUb0PNN_My3vPlXJI2uR1cCJf6vBC79CMV4ulsZHFw0`** ("MJ4U Ad Creatives Log"). It is a separate spreadsheet because re-pushing the product tracker replaces that whole Sheet and would wipe an extra tab. Same sync rule: Claude is the only writer; update the CSV, then `update_drive_file` from `~/.workspace-mcp/attachments/ad-creatives.csv`.
4. ~~**"Your granddaughter…" hooks.**~~ **Ruled 2026-11-18: keep as is.** `script-method.md` R3 stands; second-person *relationship* hooks are allowed. Viewer-attribute rule still bans age, health, grief, money and the other listed attributes.
5. **Open tests** carried from the research (not decided by argument): VO vs captions-only (T4), story vs product-hero (T1), the cut-rate target (n=1), the 30-day ledger window.

## 7. Supersedes

- `research/reference/ai-film-studio.md` and `.claude/agents/film-producer|screenwriter|art-continuity|director|editor|qa.md` and `/film:new`. Kept for history; do not use for new builds. Their surviving ideas (the reference/turntable gate, scale anchoring, composited text, connection rule) are carried into 05 and 07.
- `research/reference/script-method.md` **stays the authority** for script rules. 04 applies it, and the conflicts are listed in `role-research/04-script.md` §4.
