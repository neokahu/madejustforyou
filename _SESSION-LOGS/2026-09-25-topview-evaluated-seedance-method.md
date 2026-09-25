# Handoff — TopView evaluated, Seedance prompt method established (2026-09-25)

## ⏸ IN PROGRESS — RESUME HERE

**TopView testing is NOT finished.** Tests A/B/C passed; two tests are still open:

| Test | State | Unblocked by |
|---|---|---|
| **E · people in video** | ▶️ running 2026-09-26 — 4 arms, see the 2026-09-26 log | nothing, it is running |
| **D · fleece blanket** | ⏸ blocked | the user supplying the product image |

Do **not** move on to scripting, turntables or generation until E returns and D has its image.
The scripts (`PHASE1-SUNCATCHER-shooting-scripts.md`) were written early, out of order — they are
done but 7 of their 12 clips are gated on Test E's result.

---

## Where we are
Previous session shipped the Phase-1 testing-plan page (approved-pending) and the suncatcher build plan.
This session answered the tooling question that was blocking production: **how do we actually generate
these clips, and with what prompt craft.** Both are now settled by measurement, not opinion.

Nothing is generated yet for the real build. The next session writes the three shooting scripts.

---

## ✅ DONE — 6 commits, all pushed

### 1. TopView installed, evaluated, adopted — for one specific job
Plugin `topview-browser@topview` v1.0.4, MCP at `mcp-browser.topview.ai`, OAuth complete.
Canvas: `4ed6f979c13244c9b8ba102ae2d14d91`. Full writeup: `research/reference/topview-evaluation-2026.md`.

**Cost so far ≈ 10 of 80 credits.** OAuth granted free quota (5 MiniMax-H3 video, 5 Wan 3.0 video,
10 GPT Image 2.5) which covered Tests A–C entirely; only the Seedance re-runs used credits.

| Test | Result |
|---|---|
| A · product scale in a wide shot | **PASS** — stayed hand-sized against the window sash, the framing where our rule #3 says models oversize |
| B · identity across a camera change | **PASS** — same man from **one** reference across a ¾ turn + pose + framing change; room continuity preserved unprompted |
| C · motion gate | **PASS** after prompt fix — `hook3 14.68` vs gate 8.0 |
| product fidelity in video (first attempt) | **FAIL** — then fixed by prompt, see below |

**Division of labour, now evidence-based:** TopView generates plates, camera and motion. **PIL composites
the panel, shadow and name** — image models held the product, the video model drifted. `motion_qa.py`
stays the gate; ffmpeg stays the assembler.

**Buy note:** Pro monthly ($29 / 80 credits) is the right tier. Ultra and Team carry MCP but **not API on
plan credits**. Every "365-Day Unlimited" badge is GUI-only — their docs bar it from MCP/API entirely.
3D Shot Composer has **no API endpoint** and their own page says it *"locks the spatial plan, not pixel
identity"*, so it never solved the problem we wanted it for.

### 2. Seedance prompt method — `research/reference/seedance-prompt-method.md`
This is the craft gap `ad-video-director-research.md` flagged. Sourced from the **BytePlus official
Seedance 2.0 prompt guide**, ByteDance Seed's 2.5 announcement, the **vendor contract shipped inside the
plugin** (`references/seedance-2.5.md`), plus three third-party guides.

Key rules we did not previously follow:
- **One camera movement per shot.** Verbatim: more *"will increase image instability."*
- **Image-to-video inverts the formula** — `subject + movement, background + movement, camera + movement`.
  Minimise static description; the start frame already holds the scene.
- **Storyboard by named `Shot 1 / Shot 2`, never timecode** — precise timing is *"unstable and may lead to
  abnormal generation results."* ⚠️ Our build plan's second-by-second beat sheets are **for us**, and must
  be converted to named shots before they reach the model.
- **Constraint words are essential** for avoiding deformity. Resolve against the TopView contract's ban on
  boilerplate by keeping only constraints that name **our** failure mode.
- **Define subjects by 2–3 stable features, reuse the label** every mention.
- **Emotion as physical detail**, never an adjective — the guide ships a table we can use directly.
- **Symbols:** `（music）` `<sfx>` `{dialogue}` `【subtitle】`
- **4–5 assets max, one duty each** — more makes feature priority ambiguous.

### 3. The three-run experiment that proved it
Same start frame, same 5s/720, only the prompt changed.

```
                                dur  hook3   peak  motion  cuts/s  static%
testC  Wan 3.0, bad prompt      4.9  12.11  18.87   11.83     0.0        0   dog morphed sit→stand
testC2 Seedance, fixed open     4.9   5.87  36.24    9.82    0.21        0   morph fixed, hook3 fail
testC3 Seedance, moving open    4.9  14.68  18.49   14.72     0.0        0   ✅ PASS, no morph
GATE                              —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
our shipped film                36.6   3.59      —    8.42    0.03       17
Macorner (333 days live)        17.7  18.05      —   12.62    0.40        3
```

**Settled recipe:** two named shots, each with its own single camera move, **the opening shot moving**;
describe only light and camera; pin the product with a constraint naming the exact failure mode
(*"The dog stays seated"*, *"Shadow's outline does not change"*).

`cuts/s 0` in run 3 is fine — the cut gate applies to the **assembled** film where cuts come from ffmpeg
editing. Within one clip, prefer motion over a manufactured cut.

### 4. Build plan corrected by the real product
`marketing/facebook-ads/PHASE1-SUNCATCHER-video-build-plan.md`. Product received: **German Shepherd,
"Alex"**, a printed acrylic panel — stained-glass landscape, solid black silhouette, name in small white
script *inside* the silhouette.

Beat 3 was rewritten twice:
1. I first said the name **cannot** project because the silhouette is opaque → **wrong**. The name and
   florals are printed *pale on the black dog*, making them the panel's most translucent areas; they read
   as **bright script inside the dark shadow**, and the wall gives the name more pixels than the glass.
2. Final beat 3: room floods blue-and-gold, **Alex's shadow falls across the wall with his name glowing
   inside it.** Confirmed visually in all three test clips.

Also: breed reads instantly in silhouette (Hook 1 needs no explanation), and the artwork already runs
cool→warm, so the grade rule doesn't have to be imposed — the product supplies it.

---

## Three of my assumptions that evidence overturned
Recorded because the pattern matters more than the individual errors.
1. *"TopView breaks OFAT because it auto-plans scenes"* — false when driven directly through
   `image_edit` / `image_to_video`; per-shot control is explicit.
2. *"An opaque silhouette can't project a legible name"* — false, see above.
3. *"The morph is model weakness"* — false. Four documented prompt-rule violations, fixed mechanically.

---

## ▶️ NEXT
1. **Write the three shooting scripts + ad copy.** Our own gate — nothing generates first. Use the 9-step
   framework in §05 of the plan page, then **convert beat timings to named shots** per the Seedance rule.
2. **⚠️ Verify Seedance with people before committing a human body to it.** RunDiffusion reports Seedance
   2.0 is *restricted with people*, recommending 1.5 Pro / Kling / Veo 3.1. **Every test so far was an
   empty room.** Test B proved identity in *stills* (GPT Image 2.5) — that says nothing about video.
3. **Compositing spike** — PIL perspective-warp of the real panel artwork onto the panel face and the wall
   shadow. Start from `solve_match.py` in the MJ4U-111 cartoon POC, which solved placement by
   grid-measuring and numerically solving crop rects.
4. **Test D — the fleece blanket.** ⏸ Blocked: needs the real product image from the user.
   Product: Granddaughter blanket **L 80×60**, $69.95, GP $30.36, BE ROAS 2.30×, printed line
   *"This old girl will always have your back"*. Harder than the suncatcher on three axes:
   - **Text load** — a full printed letter, not one word. The suncatcher only proved a single word comes
     back illegible. The risk here is *plausible-looking gibberish*, which is worse than blank because it
     can ship unnoticed. Read it at 100%.
   - **Scale, opposite direction** — the suncatcher tested whether a 6-inch object gets *oversized* in a
     wide; 80×60in tests whether a large object gets *undersized* or loses bulk when draped.
   - **Deformation** — fabric folds. **A flat PIL homography cannot follow cloth**, unlike the rigid
     suncatcher panel. Likely needs mesh warping, or reframe so the readable line sits on a flat section.

   Run the same A/B/C checks plus a legibility read. ⚠️ Judge against what the ad needs, not pixel
   fidelity: our research already made the blanket **Skeleton B (VO-led)** *because* the text can't be read
   on camera — grandma reads the letter aloud. Illegible text may **confirm** the structure choice rather
   than fail the tool.
5. Then: refs → 18 clips → QA → post → ship.

## Gotchas for next session
- **`.gitignore` excludes `*.png`** — all test renders are local-only in
  `products/suncatcher-dog-memorial/tests/` and in the Canvas. Commit messages cite them as evidence;
  force-add if the evaluation needs to be reproducible from the repo alone.
- **Google Workspace MCP** requires files staged in `~/.workspace-mcp/attachments/`.
- TopView renders: images ~60–120s, Seedance video ~4–6 min. Poll, don't assume.
- `nativeAudio` is **a decision, not a default** — we set it `false` because the film gets a music bed in
  post and in-shot audio would fight the mix.

---

## Operational state — what the next session needs to resume

**Live testing-plan page (approved-pending):** https://testing-plan-phase-1.namvu47.workers.dev
Deployed from `marketing/facebook-ads/testing-plan-page/` via `npx wrangler deploy` in the session
scratchpad `cf/` dir. §05 holds the 9-step content framework the scripts must follow.

**TopView Canvas:** `4ed6f979c13244c9b8ba102ae2d14d91` — "Suncatcher Phase-1 — Alex (German Shepherd)"

| Node | What it is |
|---|---|
| `node_1790348874995_7c5b5cea4f95` | **The real product image** (`img_1`) — feed this as reference |
| `node_gen_4f76bc324cd07aecb890b7d447ee1b76` | Test A plate — the wide living room, used as start frame |
| `node_gen_47f37218d0da9abb1e03939321d8287e` | Owner character reference (Test B) |

**Budget left:** ~70 of 80 credits, **plus unused free quota — 7 GPT Image 2.5 (1K/medium only),
4 Wan 3.0 video, 5 MiniMax-H3 video.** Use the free pools first.

**Models used this session** (the contract forbids hardcoding these — always call
`get_topview_canvas_generation_capabilities` first; listed only so the next session knows what worked):
`gpt-image-2.5-flare` for stills, `seedance-2.0-style` for the validated video beats,
`qwen-wan3.0-video` for the free-quota run.

**Call order that works:** capabilities → submit (with `capabilityVersion` + a unique `commandId`) →
refresh until `status: success` → `download_topview_canvas_nodes` for a signed URL → curl to disk.

**Local test renders** (gitignored, also in the Canvas): `products/suncatcher-dog-memorial/tests/` —
`testA-wide-scale.png`, `testB-owner-ref.png`, `testB-angle2.png`, `testB-compare.png`,
`testC-reveal-beat.mp4`, `testC2-seedance-corrected.mp4`, `testC3-moving-open.mp4` (the good one),
plus `*-frames.png` contact sheets.

**Product source image:** `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png`
(2048×2048) — this is the PIL compositing texture, not just a reference.
