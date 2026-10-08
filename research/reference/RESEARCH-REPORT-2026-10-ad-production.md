# Research report — ad production, 2026-10

> Consolidates every research doc from the 2026-09-25 → 2026-10-08 research run into one scannable
> reference. Source docs are cited per row; read them for full detail, not this summary. Where this
> report states something that is NOT yet written into the source doc itself (found only in conversation),
> that is marked **⚠️ NOT ON DISK ELSEWHERE**.

---

## 1. Video prompting (Seedance)

Source: `research/reference/seedance-prompt-method.md`.

| Finding | Detail | Evidence |
|---|---|---|
| Prompt = engineering instruction, not ad copy | Spatial layer (what's in frame) + temporal layer (how it changes). Formula for i2v: `subject+movement, background+movement, camera+movement` | BytePlus official Seedance 2.0 guide |
| **One camera movement per shot** | Compound motion (push+pan+rotate+drift) causes instability | testC: 4 simultaneous motions → dog morphed sitting→standing |
| Define subject once, reuse the label | `Define [2–3 stable features] in @Image N as <Subject>`, then always refer to `<Subject>` | BytePlus guide |
| **Storyboard by named shot, never by timecode** | `Shot 1 / Shot 2`, no `0–3s` style timing — "unstable, may lead to abnormal generation" | BytePlus guide, verbatim |
| Actions: body-part specific, quantified, gentle | "slowly raise a hand", not "very sad" | BytePlus guide |
| Emotion as physical detail, never adjective | Relief = "letting out a long breath, tense shoulders relaxing" | BytePlus table; reproduced in Test E |
| **Constraint words are essential, contra the TopView contract** | Keep constraints naming OUR failure mode (pose, identity, geometry); drop generic boilerplate | testC2: "the dog stays seated" fixed the morph |
| Symbol grammar | Music `（）`, SFX `<>`, dialogue `{}`, subtitle `【】` | BytePlus guide |
| Asset count: 4–5 total, one duty each | 1–2 character + 1 scene + 1 camera-ref + 1 audio. "Too many assets → model can't judge priority" | BytePlus guide |
| **Use Seedance 2.0, not 2.5, for people** | 2.5 is the platform's *preferred* model but scored ~half the motion and produced a lens-flare smear vs 2.0's correct prism band | Test E: 2.0 hook3 8.10–14.90 vs 2.5 4.64–6.88 |
| **The two-shot recipe is THE recipe** | One shot → two (same model/frame): hook3 8.10→14.90, motion 7.63→14.96, and buys `cuts/s 0.21` (a single shot leaves cuts at 0) | Test E3 |
| **Opening shot must itself carry one camera move** | A static Shot 1 crashed hook3 14.68→5.87 even though the rule "one move per shot" was followed | testC2 vs testC3 |
| **Locate the action in space, not just on the body** | "Raises hand into the light" (body-specific, quantified) still produced a palm-out "stop" gesture with eyes closed, in a grief ad | Test E, rule 4 |
| **Name the light source, keep it off-screen** | Unsourced light → lens flare. Naming an off-screen stained-glass panel caused Seedance to **invent one in frame** — the model drawing the product it must never draw | Test E rule 5–6 |
| Scope warning | All of the above is Seedance-specific grammar (BytePlus + TopView contract). Running it unmodified on another model confounds a comparison | Doc's own scope note |

---

## 2. Image prompting (GPT Image 2/2.5 · Nano Banana 2/Pro · Seedream 5.0)

Source: `research/reference/image-prompt-method.md`.

| Model | Structure | Key rule | Evidence |
|---|---|---|---|
| **GPT Image 2/2.5** | Background → Subject → Details → Constraints ("Golden Order") | Editing = terse direct commands, no prose ("Change background to X. Keep subject unchanged.") | OpenAI image-prompting guide |
| **Nano Banana 2/Pro** | `[Subject]+[Action]+[Location]+[Composition]+[Style]`, or with refs: `[Reference images]+[Relationship]+[New scenario]` | Assign each reference a **job** ("structure", "texture"); start with a strong verb; refine don't regenerate at 80% right | Google Cloud Nano Banana prompting guide |
| **Seedream 5.0** | Quote exact text to render; use **visual markers** (arrows/boxes drawn on the input image) for placement instead of describing it | Keep prompts <600 words; resolution set in params, not prose | ByteDance Seed / BytePlus ModelArk docs |

**Universal checklist this session produced:**

| Rule | Statement | Caused by |
|---|---|---|
| THE LIMB RULE | Never describe a body part by what is hidden ("only her face and one hand show"). Say where it is and what it touches | D5a: "only her face and one hand show" → hand reading as punching through the fabric |
| Positive framing always | Never "only X", "no Y", "without Z" | Google best-practice #2 |
| Assign a role to every reference | character / style / pose / composition / background / texture | OpenAI multi-ref format |
| Never re-describe what the reference already carries | Same as THE ONE RULE in the i2v doc | D4 failure (below) |

**Model routing decided from testing:**

| Need | Model | Why |
|---|---|---|
| Product artwork / printed text exact | **Nano Banana Pro** | Best measured text fidelity |
| Deterministic element placement | **Seedream 5.0** + visual markers on input | Replaces TopView AnyShoot's coordinate control |
| Identity-preserving edit, multiple refs | **GPT Image 2.5** + `input_fidelity="high"` + role-labelled refs | Strongest multi-ref role system |
| Avoid | GPT Image at 4K/max for artwork | 4× Nano Banana Pro's cost, and it rendered the **wrong typeface** |

**The D5a/D6 fix (demonstrates THE LIMB RULE):** "Only her face and one hand show" → ambiguous punched-through shape. Rewrite locating the hand ("rests on the blanket's top edge near her collarbone, fingers relaxed and fully visible") → correct hand, five fingers, on top of the fabric. Trade-off: slightly more headline occlusion. Evidence: `compare-D5a-vs-D6.png`.

---

## 3. Product text fidelity

Source: `research/reference/product-text-fidelity-2026.md` (**amended 2026-10-08** — see §4 below for the TopView-specific cost/verdict changes; this section is the text-fidelity findings only, unchanged).

| Claim going in | Reality found | Evidence |
|---|---|---|
| "AI cannot render legible text" | **Wrong.** Given the real product as reference at 2–4K: a 4-letter name renders word-perfect on Nano Banana Pro, Seedream 5.0, and GPT Image 2.5 | Test F stage 1 |
| Legibility = fidelity | **Wrong.** GPT Image spelled "Alex" correctly in a different, bolder typeface | Test F stage 1 |
| Video re-synthesis holds a name | **Partial.** The word stays legible through Seedance 2.0 i2v, but the **letterform drifts** to a bolder typeface mid-shot, and rigid-product geometry (the silhouette, the ornate frame) deforms | testF2-name-in-video.mp4: hook3 21.61, all gates pass; letterform still wrong |
| ~50-word printed poem will come back as gibberish | **Wrong.** Nano Banana Pro 4K held every line, colour, weight and apostrophe, flat *and* draped, following cloth folds in correct perspective, unprompted | Test D1/D2 (blanket) |
| A flat composite can't follow cloth drape (needs mesh warp) | **Wrong.** The model follows the drape unprompted | Test D2 |
| Video corrupts long printed text | **Wrong — was a misread.** "Feeling" read as "ceeling" in the final frame only; frames 80/95 show a complete, correct "f". A fold occluded the ascender. **Rule: never judge printed text from a single frame — sample across the clip** | testD3-video.mp4, corrected in commit `0404e0d` |

**Settled shot policy:**

| Shot | Method |
|---|---|
| Wide/medium, name present but not read closely | Seedance 2.0 — model lettering fine, drift invisible |
| Close-up where the name **is** the proof, rigid product | **4K still + ffmpeg Ken Burns at native resolution** — beats Seedance on letterform, silhouette, frame and sharpness, clears the motion gate (hook3 11.02/motion 10.73), at ~0.2 credits vs ~4 |
| Text on **cloth**, moderate camera move | Seedance 2.0 is acceptable — verified on the blanket (testD3) |

⚠️ Build the Ken Burns zoom on **native resolution** — scaling to 1080 before `zoompan` softens the exact lettering being protected.

**The compositing engine (per-frame shadow tracking, heart-anchor template match) was built as a spike, proven to work on one frame, and then proven unnecessary** — the stills Ken Burns alternative beats it on every axis at 1/20th the cost.

---

## 4. Platforms & cost

### 4a. TopView — ⚠️ VERDICT REVERSED since the source doc was written

Source: `research/reference/topview-evaluation-2026.md`, **now amended 2026-10-08** to change its bottom-line recommendation from "buy Pro annual, $192" to **DROP**. The amendment is in that file; summarized here.

| Fact | Detail | ⚠️ On disk? |
|---|---|---|
| **New verdict: DROP** | Previously recommended "buy Pro annual, $192" based on a cost-parity estimate (~$0.80/clip). That estimate is now superseded by measured per-model credit costs (below) | Was NOT on disk — fixed in `topview-evaluation-2026.md` this session |
| Measured credit costs, Pro monthly ($29/80cr = $0.363/credit) | Seedance 2.0 5s@720 = 5cr ($1.81) · @1080 = 12.5cr ($4.53) · Seedance 2.5 @720 = 7.5cr · GPT Image 2.5 4K/max = 5.64cr · Nano Banana Pro 2K = 0.8cr / 4K = 1.4cr | ⚠️ NOT ON DISK ELSEWHERE |
| AtlasCloud comparison | Seedance 2.0 Fast = $0.027/s list, ~30% discount → **~$0.09–0.14 per 5s clip** — **~13× cheaper** than TopView for the identical model | ⚠️ NOT ON DISK ELSEWHERE |
| Part of the overspend is on us | Never used TopView's Fast tier or 720p drafts on first passes — a documented rule we ignored, not a platform flaw | ⚠️ NOT ON DISK ELSEWHERE, consistent with `_SESSION-LOGS/sessions/2026-09-26-testing-complete-both-products.md` |
| **Motion Control (Kling) is BROKEN via MCP** | Backend error "duration must be positive seconds, or -1"; MCP validator rejects `duration` in both `parameters` and top-level ("not supported by the selected capability"); both `std` and `std-v3` fail, routed as video-edit. 4 attempts, 0 credits charged | ⚠️ NOT ON DISK ELSEWHERE |
| TopView's three advertised differentiators, scored | "Unlimited" tier = **GUI-only**, confirmed in the doc's own FAQ quote. "3D Shot Composer" = **no API**. **Motion Control = broken via MCP** (new this session). All three are unusable from automation | `topview-evaluation-2026.md` (first two already documented); Motion Control is new |
| Product AnyShoot | Real, narrow-fit for these products, untested. Seedream visual markers (§2) give similar deterministic placement for less | ⚠️ NOT ON DISK ELSEWHERE |
| Untested substitutes for Motion Control | AtlasCloud has Kling i2v/t2v but no motion-control endpoint. kie.ai has `wan_animate` / `kling_avatar` as possible substitutes — untested | ⚠️ NOT ON DISK ELSEWHERE |

### 4b. kie.ai Seedance 2.0 Fast — a direct reproduction test

| Test | Result |
|---|---|
| Reproduced testE3 on kie.ai Seedance 2.0 Fast | hook3 9.50 / motion 8.38 (vs TopView `seedance-2.0-style` 14.90/14.96) — and reproduced the palm-to-camera stop-gesture issue from Test E |
| Tier difference | Fast vs standard untested at matched settings — the gap could be tier, not provider |

⚠️ NOT ON DISK ELSEWHERE — this comparison exists only in conversation; record it here and consider promoting it into `product-text-fidelity-2026.md` or a new file if repeated.

### 4c. Routing decided this session (⚠️ NOT ON DISK ELSEWHERE)

| Media | Primary | Fallback |
|---|---|---|
| Images | kie.ai | AtlasCloud |
| Video | AtlasCloud | kie.ai `seedance_2_video` (also supports first+last frame) |
| TopView | Dropped for video generation (plates/scenes role retired — see §6, §8) | — |

### 4d. Reference-to-video not yet used (⚠️ NOT ON DISK ELSEWHERE)

**Every scene clip produced to date used `image_to_video`** (one start frame). The mechanism meant to fight identity drift — `reference_to_video` (up to 9 reference images) — has not been used on any scene yet. This is the first thing the recommended vertical slice (§8, §9) should exercise.

### 4e. ComfyUI — deferred, not adopted (⚠️ NOT ON DISK ELSEWHERE)

| For | Against |
|---|---|
| More control available: character LoRA, PuLID/InstantID, ControlNet, inpainting | Can't run Seedance / Nano Banana / GPT Image / Kling natively |
| — | Open video models are likely behind Seedance in quality — **unverified, past the assistant's knowledge cutoff** |
| — | Needs a 24GB+ NVIDIA GPU; the user is on a Mac, so cloud GPU rental would be required |

**Decision: revisit only if the vertical slice (§9) shows identity drift that 8 reference images can't fix** — at that point, consider training a character LoRA.

---

## 5. Script method (rules with strength + evidence)

Source: `research/reference/script-method.md`, built from `research/sprints/2026-09-script-method/*.md`.

### Evidence-base honesty (read before trusting any rule below)

| Code | Source | n | Longevity verified? |
|---|---|---|---|
| NW | Niche winners (grandparent→grandchild) | 3 | Partly — only A fully confirmed in Ad Library |
| GW | General winners (8 gift + 8 non-gift) | 16 | No — "days live" is WinningHunter-only, unverified |
| PF | Published frameworks (Meta/Google ABCD/TikTok/IPA/Motion) | — | n/a, graded A–C per source |
| AUD | Existing-docs audit + our motion measurements | 1–2 | Partly; motion benchmark is **n=1** |
| OWN | Our own tests (C/D/E/F, D2–D7) | — | n/a — facts about production, not ad performance |

⚠️ **WinningHunter's "days live" is unreliable.** Two ads shown at 350+ days actually ran **11 hours** and **3 days** in the real Meta Ad Library — the only two blanket candidates found, both rejected. Always check "Started running on" before calling anything a winner.

### Key rules (full list of 24 rules + strength grading is in `script-method.md` §1; highest-impact ones below)

| # | Rule | Strength | Evidence |
|---|---|---|---|
| R1 | Product on screen by 1s (frame 1, not a room/face/logo) | **STRONG** | NW 3/3 at 0s; GW gift 8/8 ≤1s |
| R2 | Personalization (name/photo/letter) is the hero visual, legible, large share of runtime | **STRONG** | NW letter fills 10–32 of 14–56s |
| R6 | Meta Personal Attributes — describe the character, never the viewer | **HARD** | Meta policy text; age-example worked case |
| R7 | Burned-in captions carry the story sound-off | **STRONG** | PF, GW 5/8 text-led |
| R11 | Vary shot length 2–5s, hard cuts not crossfades, never uniform 5s | **MODERATE** (n=1 motion benchmark) | MJ4U-111 used uniform 5s + crossfades, hook3 3.59 vs winner's 18.05; `scdet` couldn't see its cuts at all |
| R16 | People on screen are optional — hands + product is proven | **MODERATE** | NW 0/3 faces |
| R18 | When grandma is the buyer, she is alive and present in the ad — never read as dead | **HARD** (house) / MODERATE (evidence) | NW 3/3 present via voice or words |
| R19 | Casting must match the customized printed figures (skin tone, hair texture/colour/style) | **HARD** | Test D2: model cast a white woman against Black printed figures; user confirmed as hard rule |
| R20 | Story-film (Thai style, late reveal) is NOT the cold default — test cell only | **MODERATE** | 0/16 GW, 0/3 NW are story-film; MJ4U-111 failed the motion gate 3 of 4 |
| R21 | Product always comes from real artwork/still — model never draws it | **HARD** | Test F: model-drawn close-ups deform; Test E: model invented a stained-glass panel |
| R22 | Long printed text: video OK on cloth; rigid product → 4K still + Ken Burns | **HARD** | §3 above |
| R23 | QA printed text by eye across several frames, never one frame | **HARD** | The "ceeling" misread |
| R24 | For a hand near a product face, the simplest correct fix may be **no hand** | **HARD** for blanket | D5a→D6→D7: "both hands inside the blanket" beat locating the hand |

### What this changes in the current shooting script

`marketing/facebook-ads/PHASE1-SUNCATCHER-shooting-scripts.md` needs revision per `script-method.md` §4a: HOOK-2 currently opens on an empty window (product not visible until A-3 at 6s) — violates R1; Body C's product is absent 2–11s — same violation; the "5s-native" beat sheet uses uniform 5.0s beats — violates R11; assembly defaults to crossfades — violates R11. Fixes are specified row-by-row in `script-method.md` §4a. **This revision has not yet been applied to the live shooting-script doc** — see the handoff doc's awaiting-user item.

For the blanket (`script-method.md` §4b): no verified long-running blanket video winner exists anywhere — every script for this product is a test, not a known-good pattern. Build the cheap NW-pattern control first (hands + poem + grandma VO). The user's "growing up" timelapse concept is scripted as the **T3 challenger**, not the default, with four required fixes: blanket visible in every age shot from 0s, grandma alive and present throughout (returning in the final beat), every age cast to the printed figure, and third-person writing per R6/Meta policy.

---

## 6. Character references

Source: `research/reference/image-prompt-method.md` §"Character reference set — template".

| Decision | Detail |
|---|---|
| **8 separate full-resolution images, never one multi-panel sheet** | Resolution per face collapses in a sheet (~200–300px per face in a 50-panel 2–4K frame); the video model (`reference_to_video`) takes up to 9 separate images anyway, so 8 full views + 1 spare slot fits exactly; sheets need text labels that contradict the "no text" instruction; Nano Banana has **no negative-prompt field**, so a negative block in a sheet prompt is wasted text |
| The 8 slots | Front, 3/4 left, 3/4 right, full body standing, full body seated, hands close-up, expression "quiet relief", expression "gentle smile" |
| Generation method | Views 1–3 first (the base turntable); **views 4–8 each take views 1–3 as their reference**, not the previous new view, to avoid drift-chaining |
| QA result, owner set (`products/suncatcher-dog-memorial/assets/turntable-owner/`) | Identity (face/glasses/beard/brows/hair/clothing) consistent across all 8. **Two views flagged**: `owner-hands.png` (hands overlap on one knee, can't confirm 5 fingers per hand, adds an unestablished gold wedding band) and `owner-expr-relief.png` (reads as a plain smile, nearly identical to `owner-expr-smile.png`, not "quiet relief") |

**⚠️ User's proposed alternative — a single JSON reference-sheet prompt — was rejected** (⚠️ NOT ON DISK ELSEWHERE as a standalone decision record, though consistent with the 8-image rule above): a ~50-panel sheet gives each face only ~200–300px; the text-label rules self-contradict "no text"; Nano Banana has no negative-prompt field; the prompt ran ~700 words.

**REF-GIVER and the blanket product's characters have no reference sets built yet** — this is listed as next work in the handoff doc.

---

## 7. Prompt guard hook

Source: `research/reference/generation-prompt-guard.md`.

**Why it exists:** on 2026-09-26 the documented prompt method was ignored three times in one session (Test C: no named shots/constraints → dog morphed; Test E: one shot, action not located → stop-gesture in a grief ad; Test D4: ~190-word prompt re-describing the printed poem → catalogue packshot instead of the wrapped shot). Documentation alone did not change behaviour, so a `PreToolUse` hook now blocks the call before it runs.

| Layer | Rules | Word cap |
|---|---|---|
| **Video** (structured prompts) | `LENGTH`, `REDESCRIBE` (THE ONE RULE), `SHOTS` (named shots required), `TIMECODE` (ban `0–3s` style), `OPENMOVE` (opening shot must move), `ONEMOVE` (one camera move/shot), `CONSTRAINT` (must pin a failure mode) | 220 words |
| **Image, generic** | `NEGFRAME` (exclusionary framing), `LIMB` (unlocated limb), `REFROLE` (reference with no role) | 250 words |
| **Image, model-specific** | `GPTTERSE` (GPT Image edits must be terse commands) · `NANOREL` (Nano Banana refs need a relationship instruction) · `SEEDQUOTE` (Seedream text needs quotes) | — |
| **Freeform** | — | 100 words |
| **Exemption** | `motion_control` task type is exempt from the shot-structure rules | — |

**Location:** `~/.claude/hooks/generation-prompt-guard.py`, mirrored at `research/scripts/generation-prompt-guard.py` in this repo, registered in `.claude/settings.json`. Covers kie.ai, AtlasCloud, and TopView image+video generation calls.

**Coverage history:** image models (`nano_banana`, `gpt_image`, `seedream`, `flux2_image`, `imagen4`, `ideogram_v3`, `wan_image`) were initially absent from the tool list — every kie.ai image call ran unguarded, including the call that produced the punched-through hand. AtlasCloud needed a different fix because it routes every image model through one generic tool (`atlas_generate_image`) with the model id as a parameter; `model_of()` now recovers the model id from `model`/`modelId`/`parameters.model`.

**Override:** add `ACK-<RULE>` to `commandId` (e.g. `beat3-ACK-OPENMOVE`) — a conscious, explained exception, not a silent bypass.

**What it cannot check:** whether an action is located in space (passes mechanically, fails visually — the Test E stop-gesture), whether casting matches customized artwork, or whether a shot serves the concept. Judgement still belongs to the doc read before prompting.

---

## 8. What it changes

| Area | Before | Now |
|---|---|---|
| Video generation platform | TopView (Pro plan, recommended "buy annual $192") | **Dropped.** AtlasCloud primary, kie.ai `seedance_2_video` fallback (§4) |
| Image generation platform | — | kie.ai primary, AtlasCloud fallback (§4c) |
| Seedance model for people | Assumed "restricted with people", avoid | **Seedance 2.0, confirmed best for people**; 2.5 underperforms it (§1) |
| Printed text on a rigid product in motion | Assumed unrenderable, needed a PIL compositing engine | **4K still + native-resolution Ken Burns** — cheaper, sharper, no engine needed (§3) |
| Printed text on cloth in motion | Assumed needed mesh-warp compositing | Video holds it natively, unprompted (§3) |
| Character reference method | Single reference per character (reverted), then one multi-panel sheet (rejected) | **8 separate full-resolution images per character** (§6) |
| Scene generation endpoint | `image_to_video` (one start frame) for every clip so far | Should move to `reference_to_video` (up to 9 refs) — **not yet done** (§4d) |
| Prompt discipline | Documented but not enforced — same 3 rules broken repeatedly in one session | **Mechanically enforced** by a `PreToolUse` hook across both providers and all media types (§7) |
| ai-film-studio.md pipeline | Was the house pipeline | **Demoted** — its MJ4U-111 film scored hook3 3.59 vs the measured benchmark of 18.05 |
| Shooting script status | `PHASE1-SUNCATCHER-shooting-scripts.md` treated as ready | **Needs revision** per `script-method.md` §4a before it can be approved (§5) |
| ComfyUI | Not evaluated | Evaluated and **deferred**, not adopted (§4e) |

---

## 9. Open questions

| Question | Status | Who/what resolves it |
|---|---|---|
| Does `reference_to_video` (8-ref) actually reduce identity drift across multiple independently-generated clips vs the single-start-frame method used so far? | Untested — no scene clip has used it yet | The recommended vertical slice: shot S-C1-H1 end to end on AtlasCloud, ~$2 |
| Is kie.ai Seedance 2.0 Fast's lower score (9.50/8.38 vs TopView's 14.90/14.96) a tier difference or a provider difference? | Untested at matched settings | Re-run the same test on kie.ai's non-Fast / standard Seedance 2.0 |
| Can `owner-hands.png` and `owner-expr-relief.png` be fixed with a regeneration, or do they need a structural change (e.g. separate the hands further, add an explicit "no ring" constraint)? | Flagged, not regenerated (~$0.60 estimated) | Next session, per handoff doc |
| Do AtlasCloud's Kling endpoints, or kie.ai's `wan_animate` / `kling_avatar`, substitute for TopView's broken Motion Control? | Untested | Needs a dedicated trial once a use case for motion control actually comes up |
| Child vs adult rendering for the blanket-granddaughter product? | Open, blocks nothing yet, but blocks the "growing up" timelapse concept's final form | User decision |
| Is `marketing/facebook-ads/PHASE1-SUNCATCHER-shooting-scripts.md`'s revision (per script-method §4a) going to be a new version of that doc, or an in-place edit? | Not yet started | Next session |
| Does `motion_qa.py`'s benchmark (n=1, the Macorner visor ad) generalize? | Open since the script-method audit | Run `motion_qa.py` on ≥10 Ad-Library-verified winners (script-method.md §6 gap list) |
| Is TopView worth keeping for stills (Nano Banana Pro text fidelity, scene plates) even though video is dropped? | Not explicitly decided — the DROP verdict in §4a is stated for video; image use wasn't re-costed the same way | Worth a quick credit-cost check before cancelling the plan outright |
