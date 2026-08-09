# AI Film Studio — MadeJustForYou

**Purpose:** a repeatable "small studio" for producing emotional short-film ads (Thai-ad style) with AI, end-to-end. This is the **source of truth** every studio role reads. Built 2026-08-07 from the MJ4U-111 "Everyone Is Still in Your Garden" production (see that film as the worked example).

Builds on — does not duplicate — the three method playbooks:
- [[ai-emotional-video-ad-playbook]] — emotion→angle→hook strategy, testing.
- [[image-to-video-prompt-method]] — i2v prompt craft (one move, don't re-describe the product).
- [[ai-product-review-consistency-method]] — multi-ref identity + product consistency.
Related memories: [[ad-style-thai-emotional-film]], [[video-ads-need-full-script]], [[emotional-ad-show-family-connection]].

> **One line:** lock the *turntables* (character + product references) BEFORE shooting; write a full script; generate scenes from the locked refs; verify every shot; composite real text/logo in post. Product appears only as the emotional payoff.

---

## 0. Inputs required (gather + validate at Phase 0 — before anything else)
The Producer collects these and the QA rejects any that fail the spec. Bad inputs (esp. the product image) silently break Phase 2 and cost reshoots.

### Product image — THE critical input
- **REAL product photo** — an actual photo of the manufactured product. **NOT an AI mockup / lifestyle render / marketing infographic.** (Renders have wrong details; infographics have baked-in text/"VS" graphics — unusable.)
- **Plain / blank background** (white or neutral studio), product isolated. A clean cutout lets Seedream place it into any scene and build the **scale-anchored reference** cleanly. **Avoid** busy lifestyle backgrounds, extra props, overlaid text/badges.
- **Sharp & high-res** — ≥1500px (2000px+ ideal); the printed **personalization (names/flowers) legible**.
- **Straight-on hero** + any extra angle if available.
- **Real personalization visible** — note whether the on-pack names are the buyer's real names or DEMO names to be swapped (everything on screen must match whatever ships).
- **Format jpg/png** (video models reject webp → convert `sips -s format jpeg` or weserv proxy). No watermark.
- *If only a lifestyle/mockup exists:* Art must first **isolate the product** (Recraft/Seedream remove-bg) and rebuild a clean plate before scale-anchoring — flag the extra step + risk.

### Other inputs
- **Character source (optional):** to feature a specific real person, provide a clean, front-facing, well-lit portrait (one person, neutral expression, no heavy filter). Otherwise the studio generates the cast (Seedream t2i).
- **Personalization data:** the actual names/flowers/photo to appear (buyer's real values, or demo set).
- **Brand:** logo `library/brand/logo/lockup-horizontal.png`, palette + fonts (design-system). Already on hand.
- **Copy/angle:** recipient, core emotion, competitor hook (`product.md` / `ads/ad-copy.md`).
- **Music (optional):** a track, or let the studio generate one.

### Input gate (QA)
Product photo is **real + blank-bg + sharp + legible names + jpg/png**? Character source (if given) usable? Personalization values confirmed? → only then proceed to Phase 1.

## 1. The crew (lean, 6 roles)
Each role is a bundle of hard rules learned in production. In the `.claude/` implementation each is a subagent; a human can also just wear the hat.

| Role | Owns | Enforces |
|---|---|---|
| **Producer** (orchestrator) | brief intake, scope (length/# variants), **credit + time budget**, sequencing, gates, delivery | step-gated turntables; parallel-batch shoot; live cost tally (~$1/clip) |
| **Screenwriter / Writer** | logline, emotional arc, **3s hook**, full shooting script, master character prompt, production rules — **AND the matching ad copy** (`ad-copy.md`: primary text, headline, CTA, hook variants, on-screen text) | full script before shooting; product as late payoff; resolve into family/warmth; **ad copy shares the film's hook + emotional thesis** |
| **Director (+DP + generation)** | shot list, per-shot camera angle for variety, generation prompts, the cool→warm arc, runs Seedance/Seedream | one move per shot; never re-describe the product; avoid mechanical hand actions; product only close/medium; vary angles; set each shot's `duration` from its beat length |
| **Art / Continuity** (Phase-2 owner) | **character turntable**, **product turntable (scale-anchored)**, location/wardrobe continuity, identity/text props | no ref → identity drift; product needs a scale anchor; AI garbles text → composite real; props that show identity/text are controlled, not AI-invented; use the REAL product image (animated) |
| **Editor (+sound + brand)** | ffmpeg assembly, crossfades, match cuts, auto-fit captions, grade, music, **logo end card** | cool→warm grade; captions carry dialogue (no lip-sync); no caption overflow; brand palette/fonts |
| **QA / Script Supervisor** | verify every turntable + every shot | identity / scale / morphs / text / mood / "not lonely"; nothing assembles on unverified footage |

---

## 2. The pipeline (phases + gates)
**Phase 0 — Brief & Greenlight** · Producer
Product, core emotion, recipient, scope, credit budget. Pull the competitor hook (Meta Ad Library). → **GATE: greenlight.**

**Phase 1 — Story + Copy** · Screenwriter/Writer
Two aligned deliverables in one pass: (a) the full shooting script `ads/film/script.md` (logline · arc · 3s hook · per scene Visual/Camera/Dialogue/VO/Sound/On-screen text/AI prompt · master character prompt · rules); (b) the matching **ad copy** `ads/ad-copy.md` (primary text ×3, headline ×3, CTA, **5 hook variants — each a DIFFERENT methodology** (emotional / curiosity / personalization-act / confession / DR), not rewordings, on-screen text) — sharing the film's hook + emotional thesis. Template: `research/templates/film-script-template.md`. → **GATE: user approves script + ad copy.**

**Phase 2 — Pre-Production / TURNTABLES** · Art + Casting · **HARD GATE**
- **Character turntable** — per recurring person: lock ONE reference (Seedream t2i portrait, or a clean harvested frame) → generate ¾-left / ¾-right angles → host → **QA identity**.
- **Product turntable** — from the REAL product photo: a **scale-anchored reference** (product beside a mug at true size) + front/¾ angles (Seedream Edit) → host → **QA scale + on-model**.
- **Text/identity props** staged (notebook, note, lamp-name plate, wall-photo source = our character).
→ **GATE: user approves cast + product turntables. NO scene is shot until this is locked.** This gate prevents the three most expensive failures: identity drift, product-scale jumps, pasted-in props — each of which otherwise costs a full reshoot (~$1/clip).

**Phase 3 — Production / Shoot** · Director + QA
After the gate, scenes are independent → **submit all scene prompts as one parallel batch** (Seedance Ref-to-Video, feed the locked refs). Then **QA every shot together** (identity/scale/morph/text/mood). Reshoot only the failures (best-of-N). Set each shot's `duration` to its beat length (4–5s), not a blanket 5s.

**Phase 4 — Post** · Editor
Composite real text props + logo; cool→warm grade; crossfades + match cuts; auto-fit burned captions; music bed; end card. Kit: `products/_templates/film-studio/`. Export master + a 15s FB cut.

**Phase 5 — Delivery** · Producer
Export the 15s cut + the hook-variant creatives + ad copy → **hand off to the FB advertiser** for testing. Ad economics (break-even/ROAS), ad-set structure, kill/scale = **separate media-buyer expertise, out of studio scope.** Update the product tracker `ad_status`.

---

## 3. Hard rules (the expensive lessons)
1. **Turntables first, gated.** Never generate scenes before the character + product references are locked and approved. Identity/scale fixes are ~$0.05 at the ref stage vs ~$1/clip as reshoots.
2. **One character reference per person, fed every shot.** No ref → the model invents a new person each clip (the MJ4U-111 "memory clip" failure). Multi-angle (¾-L/¾-R) lets you vary camera while identity holds.
3. **Product needs a scale-anchored reference** — the product beside a familiar object (a mug) at true size. A bare product crop has no scale cue and the model oversizes it in wide shots. Keep the product in **close/medium** framing.
4. **Use the REAL product image, animated** — animate the actual store photo (gentle push-in/drift, flame flicker) rather than a static paste or an AI re-render. Match all on-screen names to the real product's names.
5. **AI garbles printed text → composite real text in post.** Names on the lampshade, the notebook page, the note: render sharp with PIL and composite. Match notebook names to lamp names exactly (match-cut).
6. **Identity/text props are controlled, not AI-invented.** Wall photos must show OUR character (feed the ref, or composite a real still). 
7. **Avoid mechanical hand-object actions** (key-in-lock, unboxing, precise manipulation) — the model botches them. Reframe to imply the action (clutch the key, push the door).
8. **Product as plot payoff** — it appears late (≈60% mark), as the emotional turn, never a showcase. Cool→warm grade: cold/desaturated setup → warm gold at the reveal.
9. **Dialogue = on-screen captions** (default) — dodges lip-sync, works sound-off. Auto-shrink captions so no line overflows the frame. VO optional.
10. **Verify every shot before it ships** — identity, scale, morphs/extra fingers, text legibility, mood, and "shows family/connection, not a lonely giftee."

---

## 4. Cost & time model (REAL, from billing 2026-08)
- **Seedance 2.0 Fast Ref-to-Video: ~$0.98 per 5s clip at 720p** (~$0.195/s; token-billed). At **480p ≈ $0.67/clip** (~$0.134/s). *(The old "$0.09/clip" figure was wrong by ~10×.)*
- **Seedream v5.0 Pro Edit / t2i: ~$0.045 per image.** MiniMax Music: **$0.15**. ElevenLabs VO: **~$0.01–0.10**.
- **A clean ~35s film ≈ 9 clips + 4 refs + music ≈ $9 at 720p (~$6 at 480p).** Add reshoots/variants and it's $12–18.
- **Trim waste is real:** generating a blanket 5s for a 3s beat throws away ~$0.4/clip. Set `duration` from the beat.
- **Render time:** ~1.5–2.5 min per clip (720p), ~1.5–2 min per ref image, ~1 min music, ~1–2 min local assembly.
  - Sequential (verify-each) ≈ **25–30 min/film**. **Parallel batch** (all scenes at once, after the turntable gate) ≈ **5–8 min wall-clock**.
- **Producer budget rule:** ~**$0.70–1.00/clip**; keep a live tally; the turntable gate + QA pay for themselves (every avoided reshoot ≈ $1).

---

## 5. Tool stack
- **AtlasCloud MCP:** `bytedance/seedance-2.0-fast/reference-to-video` (scenes, up to 9 ref images, `ratio`/`resolution`/`duration` params), `bytedance/seedream-v5.0-pro/edit` (turntable angles, scale anchor, text), `.../text-to-image` (new cast portraits), `elevenlabs/v3/text-to-speech` + `minimax/music-2.6` (audio). Async: submit → `atlas_get_prediction`. Cost/usage: `atlas_get_model_costs`/`_usage`.
- **blotato MCP:** `blotato_create_presigned_upload_url` → PUT `--data-binary` → publicUrl to host local refs. (Re-paste the exact JWT; mangling it = 400.)
- **Local:** `ffmpeg` (grade/caption/crossfade/mux — note: this build has **no drawtext/libass**, so captions are PIL PNG overlays), `PIL` (captions, props, end card), `sips`.
- **Gotchas:** video models reject WebP → `sips -s format jpeg` or weserv proxy. Seedance `ratio` not `aspect_ratio`. 720p max on the fast tier for some outputs. Frames >2000px fail multi-image Reads → downscale for review.

---

## 6. How to run a new film
1. `cp -r products/_templates/film-studio products/<ID>/ads/film` (the kit).
2. Fill `production.md` (product, cast, scenes table with per-scene `duration`, budget).
3. Phase 1: write the script into `<ID>/ads/<script>.md` (use the template).
4. Phase 2: build + host the turntables; **get sign-off**.
5. Phase 3: batch-generate scenes; QA together; reshoot failures.
6. Phase 4: edit `captions.py`/`props.py`/`build.sh` tables; run `build.sh`.
7. Phase 5: cut variants, update tracker.
Invocable: `/film:new` (Producer orchestrates all of the above, step-gated).

## 7. Asset & folder convention (STANDARD — enforce it)
One film = one `ads/film/` folder (multiple films → `film-<slug>/`). Never invent ad-hoc folders (`clips/`, `scene-videos/`, `scene-stills/`, `final/`, `source-images/` — all deprecated). Flow reads **refs → shots → build → out**:
```
ads/film/  production.md  script.md
  refs/{cast,product,props}   # Phase 2 locked turntables (the inputs)
  shots/                      # Phase 3 raw scene clips sc01-*.mp4 (WINNERS only)
  audio/                      # music.mp3, vo.mp3
  build.sh captions.py props.py endcard.py   # the kit
  build/                      # Phase 4 ephemeral intermediates (gitignored)
  out/                        # deliverables: <title>_master.mp4, _15s.mp4
  assets/  _scratch/          # logo/brand ; verify frames + rejects (gitignored)
```
Rules: winners in `shots/`, rejects/verify in `_scratch/`; `build/` + `_scratch/` regenerable → gitignore; binaries Drive-synced, only text/scripts committed. Kit + skeleton: `products/_templates/film-studio/`.

## Worked example (also the reference implementation of the folder standard)
`products/MJ4U-111-grandmas-garden-candle-warmer/ads/film/` — organized in the STANDARD layout: `production.md`, `script.md`, `refs/{cast,product}`, `shots/` (9 winners), `audio/`, `assets/logo.png`, `out/EveryoneStillInYourGarden_v2.mp4` (36s). As-built scripts in `_scratch/as-built/`; pre-standard dirs in `ads/_archive/`. Clean-path cost ≈ $9 / ~8 min parallel.
