# Ad Video Director — research + spec for a separate skill/repo

Research 2026-09-18. **Question:** why does our AI video come out dull and not eye-catching, and what should
a separate "ad video director" skill/repo do differently?
**[DATA]** = measured/primary · **[OPINION]** = practitioner/vendor consensus.

> **The finding in one line:** the repo has exactly **one** prompt-craft doc —
> [[image-to-video-prompt-method]] — and it is deliberately **stability-first**, built to stop a product
> photo from warping. The Film Studio applied that low-motion method to **every shot of a narrative ad.**
> Stability is the enemy of eye-catching. **We have no energy-first method, and that is the gap.**

This is *not* "we forgot cinematography." It is more specific and cheaper to fix: the craft knowledge is
in the repo, it is aimed at the wrong regime, and nothing enforces the parts that are right.

---

## 1. Cause one — a stability-first method applied to shots that needed energy

`image-to-video-prompt-method.md` is a good document. Its explicit levers:

| Lever | What it prescribes | Correct for… | Catastrophic for… |
|---|---|---|---|
| **Motion amount** | "**LOW.** Say 'slow, subtle, minimal motion'; motion-strength ~0.6–0.8" | a product beauty shot | a hook that must stop a thumb |
| **Camera** | "ONE clean move, **or locked**… 'locked-off camera, perfectly still'" | holding a product true | the first 2s of an ad |
| **Clip length** | "3–5s. Drift compounds with length" | fidelity | rhythm |
| **First+last frame** | "feed the **same image to both** (a '**living still**')" | engraving macro | anything |
| **THE ONE RULE** | "the prompt's only job is **what moves**… never re-describe the product" | product i2v | — (this one is right everywhere) |

Every one of those is correct **for its stated use case**, which the doc names in its first line: *"you have
a finished product photo and want a short motion clip."* It was then used as the house prompt method for an
eight-scene narrative film. The result is a film whose every shot is tuned toward *not moving*.

**There is no counterpart document for the energy regime.** Nothing in the repo tells anyone how to make a
shot arresting — only how to keep one from breaking.

### 1b. The rules that *were* right got violated anyway (an enforcement gap)
The i2v doc says **"Lead with the camera move — models weight the first ~5 words most; a buried camera
instruction gets ignored."** The shipped Scene-1 prompt from `MJ4U-111/ads/film/script.md`:

> `Vertical 9:16 cinematic thriller, rainy night outside a nostalgic American cottage, white American woman
> age 28 with brown shoulder-length hair and dark jacket holding an old brass key and folded note, anxious
> emotional expression, wet porch, dramatic streetlight reflections, handheld 35mm film look, no product,
> no flowers, no text`

- **No camera instruction anywhere** — let alone leading. Meanwhile the script's own `### Camera` block for
  that scene reads *"macro close-up: brass key shaking / low-angle: dark house / tight close-up: she steels
  herself."* **Three designed shots, none compiled into the prompt.** The DP's work is written down and thrown away.
- **"Never re-describe what the reference already defines"** was applied to the product and ignored for
  people: we feed a locked character turntable *and* re-describe her in full noun-phrase detail. Same
  anti-pattern, different subject — and per the doc, re-describing is "the #1 cause of warping/morphing."
- **Negation-led** (`no product, no flowers, no text`) against the doc's own "positive phrasing only" guidance.

### 1c. "Vary the angle" is not directing the camera
`.claude/agents/film-director.md` enforces *"ONE camera move per shot"* and *"vary the angle across scenes
(wide / medium / close / over-shoulder)."* Those are **shot sizes** — composition, not motion. The agent has
no vocabulary of **moves** (dolly, push-in, pull-back, orbit, tracking, crane, rack focus, whip pan), no
speed, no direction, and no lens/DOF spec. Its other five rules are prohibitions. So the Director role can
say *"one move"* without ever being able to name one.

### 1d. What the outside research says this produces
| Our prompt trait | Documented consequence |
|---|---|
| no camera tokens | "Without camera specification, the model picks… usually a **mid-level, stationary or gently drifting camera. It produces functional but visually generic output.**" · "Camera is 50% of the result. **Without direction, the model defaults to a static shot.**" |
| opens with `cinematic` | "The word **'cinematic' often triggers generic slow-drift presets**; replacing it with single named moves like *dolly in* or *orbit* yields clearer output." |
| all static noun phrases, no verbs | "Image models reward rich noun phrases… **video models need to know what happens over time. A prompt optimized for image generation will produce static-feeling video.**" Describing a static photographic scene instead of change-over-time is "the **primary cause of prompt failure**." |
| subject "holding", "standing" | Diffusion models "favor slow, smooth motion because it is easier to maintain temporal consistency… the model defaults to the safest option: **make everything slow.**" Fix = explicit action verbs + speed + direction. |
| one comma-soup string | "One block for the subject and setting, one block for the camera. **It is the single biggest fix for morphing and warping artifacts.**" |
| `no product, no flowers, no text` | "**Negation rarely tells the model how** the subject, camera, or environment should move." |

Six-for-six. Any one alone yields "gently drifting, generic."

---

## 2. Cause two — the house format is the one our own research demotes for cold traffic

`video-ad-decomposition-2026.md` rates **"High-production emotional short film" = MEDIUM** ("costly/risky —
sparingly"); reveal · gift-reaction · occasion · POV-giving · testimonial · UGC · hyper-personalization are
all **HIGH**. The studio is built exclusively on the MEDIUM one.

A Thai-ad film's mechanism is *slow build → late payoff*. That works at 60–90s with an opted-in viewer.
Compressed into a 15s cold Meta cut it keeps the slowness and loses the payoff — the build has no time to
earn anything. Two direct conflicts with numbers we already hold:

| Studio hard rule | Conflicting evidence |
|---|---|
| **Rule 8: product appears late (≈60% mark)** → sec ~21 of a 35s film, sec ~9 of the 15s cut | **[DATA]** Kantar 2026 Super Bowl study: performance tied to **brand presence within 2s** and **product-forward storytelling across the first 10s**. "If your product waits until second eight, your viewer may never meet it." |
| Opening beat = a woman standing on a porch — no motion, no contrast, no text | **[DATA]** DTC hook-rate spread: 75th pct **>35%** vs 25th pct **<18%**, and the gap is "**almost entirely attributable to pattern-interrupt quality in the first 1–2 seconds**" (MHI). Our own Part D T0 red line is <21%. |

Keep the emotional film — it is a real asset for warm/brand/organic. But it must stop being the **only**
format, and it should not be the default for cold acquisition.

---

## 3. Cause three — post-production removes what energy survived

`ai-film-studio.md` Editor rules: *cool→warm grade; **crossfades** + match cuts; auto-fit captions; music
bed; logo end card.*
- **Crossfades are the lowest-energy transition that exists.** Eight 5s clips joined by crossfades is a
  slideshow. **[OPINION]** high-converting Meta creative runs **cuts every 1.5–3s in the opening segment**;
  our opening 5s contains **zero cuts**.
- **Uniform 5s beats = no rhythm.** Dullness is largely *evenness*: no speed ramp, no held beat, no hard cut
  on a sound accent, no scale jump (WS→ECU).
- **Shot density was designed and then discarded** (§1b: 3 shots → 1 generation). Density is where energy lives.
  - ⚠️ **Verify before designing around this:** Seedance bills ~**$0.195/s**, so 3 × 1.7s ≈ 5s ≈ the same
    spend as one 5s clip **only if sub-3s durations are accepted**. If there is a ~3s floor, the same 5s of
    screen time costs ~1.8× more. **Unverified and load-bearing.**

---

## 4. The energy regime — what the new skill needs to encode

### 4a. Shot prompt grammar (blocks, kept separate — never comma soup)
```
[SHOT]      shot size + angle         WS / MS / CU / ECU / OTS / low-angle / Dutch
[CAMERA]    ONE named move + speed    dolly in · pull back · pan L→R · orbit · tracking · crane · rack focus · whip pan
[SUBJECT]   ONE primary action, verb-led, with speed + direction (+ light secondary micro-motion)
[LIGHT]     direction + quality + how it CHANGES across the clip
[LENS]      focal length + DOF        35mm / 85mm / shallow DOF / deep focus
[GRADE]     named palette + contrast  (never the word "cinematic")
[NEG]       last, minimal, never load-bearing
```
Consensus rules: **one primary subject action + one restrained camera move per clip** — not both aggressive
("keep the subject mostly still when the camera is the hero move," and vice versa; overloading is what
causes warping and staged-looking motion) · **verb-led motion with speed and direction** ("whips around",
"snaps her head up" — not "anxious expression") · **describe change over time** ("begins with… then… as the
camera moves…") · **ban "cinematic," name the move** · **negation is not a control surface.**

### 4b. Timeline prompting — Seedance 2.x responds to it **[OPINION, vendor-documented]**
One camera position, one action, one atmospheric detail per mark; global style line **last**:
```
[0s] ECU brass key trembling, rain streaking the frame
[2s] camera snaps up — low angle, the house looms
[4s] hold; her hand shoves the door, light spills out
```
5s clips → three marks `[0s] [2s] [4s]`. Seedance 2.0 also has **native multi-shot generation** (per-shot
duration, size, perspective, move) — precisely the multi-setup scene our scripts already write and discard.

### 4c. Frame-1 pattern-interrupt taxonomy **[OPINION, converging]**
Bold colour break (high-contrast colour is *rare* in aspirational gift creative → cheap differentiation) ·
**text-first opening** (most video leads with a face, so big bold type *is* the interrupt — and it works
sound-off) · unusual framing/angle · motion against the scroll direction · CU after WS, or static after fast ·
product in the "wrong" setting · subject frozen mid-action · a visual mistake that gets fixed fast ·
cognitive dissonance. Audio interrupts matter on TikTok (~95% sound-on), barely on Meta feed (~80–85% sound-off).

### 4d. Per-shot model routing **[OPINION, vendor tests]**
Push-in / orbit: all majors competent — **Seedance** for product & still-life, **Kling** for
character/food. Pull-back & wide geography: **Veo**. Tracking/follow: **Kling**, keep **under ~6s**.
Crane / single-axis rise: try **Veo Fast** first. **Seedance 2.5 can transfer a camera path from a reference
video** onto a different subject → reuse a proven hook's camera energy. (This supplements, not replaces, the
per-model cheat sheet already in `image-to-video-prompt-method.md` §3, which stays authoritative for syntax.)

---

## 5. Spec — the "Ad Video Director"

### The core idea: two regimes, explicitly routed
| | **Stability regime** (exists) | **Energy regime** (missing) |
|---|---|---|
| Doc | `image-to-video-prompt-method.md` | *this skill* |
| Goal | product must not warp | shot must stop a thumb |
| Motion | LOW, locked-off, living stills | named move + verb-led action + speed |
| Use for | product hero, engraving macro, CTA beauty shot | **frame 1 / hook, narrative beats, pattern interrupts** |

Every shot gets tagged with its regime **before** prompting. Today everything silently defaults to
stability. That single routing decision is most of the fix.

### Scope boundary vs the existing Film Studio
| | **AI Film Studio** (keep) | **Ad Video Director** (new) |
|---|---|---|
| Unit of work | a *film* (one story, ~35s) | a *shot*, and a *batch of ad variants* |
| Optimises for | emotional arc, continuity | **hook rate, hold rate, thumb-stop** |
| Format | Thai-ad emotional film only | **routed**: reveal · reaction · compare · UGC · occasion · BTS · emotional film |
| Owns | story, cast/product continuity, cost model | **the image**: shot grammar, camera, motion, rhythm, interrupt |
| Product timing | late payoff (~60%) | **brand ≤2s, product-forward in first 10s** (cold); late payoff only warm/brand |

**Explicitly keep and reuse:** the turntable gate (identity + scale-anchored product refs), the real cost
model (~$0.98/5s @720p), composite-real-text-in-post, "avoid mechanical hand-object actions", and the
"shows family/connection, not a lonely giftee" QA check. These were expensive lessons and they are correct.

### The five things it must do
1. **Prompt compiler.** Shot row → block-structured prompt (§4a), regime-aware. Mechanical, not vibes:
   **if `[CAMERA]` is empty it refuses to emit.** This alone closes the §1b enforcement gap — the
   `### Camera` block can no longer be written and discarded.
2. **Format router.** product × buyer × traffic temperature × occasion → format, from the fit-rated list
   instead of defaulting to emotional film.
3. **Shot-rhythm planner.** Shot list with **varied** durations, target cut rate (opening 1.5–3s/cut),
   mandatory scale jump between adjacent shots, one designated frame-1 interrupt. **Hard cuts default;**
   crossfade only where a time jump is intended.
4. **Motion QA — the gate the studio lacks.** Per clip, auto-reject: no discernible camera move · static
   subject where action was specified · slow-motion drift · warping/morph · fewer than 2 distinct shot sizes
   across the cut. First pass is cheap and programmatic — **ffmpeg frame-difference / optical-flow magnitude;
   a near-zero motion score is a fail.** This catches exactly the defect we shipped, before a human watches.
5. **Hook bench.** Native output = **N openers against one body** (our OFAT hook test), so it feeds
   `marketing/facebook-ads/PHASE1-TOURNAMENT-3-products.md` directly instead of delivering one film.

### Roles (4 — and the new one is the whole point)
- **Creative Director** — format routing, the frame-1 interrupt, which of N hooks get built.
- **DP / Shot Designer** ⭐ *the missing department* — regime, shot size, lens, camera move, blocking, light
  change, motion budget per clip. Owns the compiler.
- **Generator** — per-shot model routing (§4d), batch submission, best-of-N, seed discipline, cost tally.
- **Motion QA + Editor** — the motion gate, then rhythm-aware assembly, grade, captions, end card.

### Repo layout (standalone)
```
ad-video-director/
├── SKILL.md                    # route format → plan shots → compile → generate → motion-QA → assemble
├── references/
│   ├── regimes.md              # stability vs energy; how to tag a shot  ← the core concept
│   ├── shot-grammar.md         # §4a blocks + the six anti-patterns as hard rules
│   ├── camera-vocabulary.md    # named moves + per-model reliability (§4d)
│   ├── motion-verbs.md         # verb + speed + direction bank, to beat the slow-motion bias
│   ├── pattern-interrupts.md   # frame-1 taxonomy (§4c)
│   ├── format-router.md        # format ← product × buyer × temperature × occasion
│   └── rhythm.md               # cut rates, scale jumps, speed ramps, when a crossfade is allowed
├── scripts/
│   ├── compile_prompt.py       # shot row → block prompt; REFUSES on empty [CAMERA]
│   ├── motion_qa.py            # ffmpeg frame-diff / optical-flow score per clip
│   └── assemble.py             # rhythm-aware cut assembly (reuse the film-studio kit)
└── templates/shot-list.csv     # one row per shot: regime, size, move, action, duration, interrupt flag
```

### Recommendation: **standalone repo installed as a Claude Code plugin**, not a skill inside this repo
(a) It is product-agnostic craft, reusable across every store and future project, whereas `madejustforyou`
is one store's docs. (b) It needs independent version history — the shot grammar will iterate fast against
real hook-rate data. (c) The `film-*` agents already occupy `.claude/agents/` here and would collide
conceptually. (d) `madejustforyou` then *consumes* it and keeps only store-specific assets (brand palette,
cast refs, product turntables).
**Cost of this choice:** one more repo to maintain, and the plugin must be installed per machine.
**Migration note:** `image-to-video-prompt-method.md` should move into it as `references/regimes.md`'s
stability half, leaving a pointer here — otherwise the two halves drift apart again.

---

## 6. Honesty notes
- **[DATA]:** Kantar 2026 (brand ≤2s / product-forward first 10s); DTC hook-rate spread (75th >35% / 25th
  <18%); Meta/Nielsen 47%-in-3s and ~80–85% sound-off (already in our decomposition doc).
- **[OPINION / vendor-reported]:** every prompt-craft claim in §4. Self-reported model-behaviour reports, not
  independently benchmarked — but they converge across five unrelated sources and each **names a mechanism**
  (diffusion temporal-consistency bias; "cinematic" as a learned slow-drift token; image-noun-phrase vs
  temporal-change prompting). Treat as strong priors, not proof.
- **Unverified and load-bearing:** Seedance's **minimum billable clip duration** (§3). The dense-cutting plan
  is cost-neutral only if sub-3s generations bill per second.
- **Not yet tested:** that fixing shot grammar raises hook rate on *our* ads. The six failure modes are
  documented and present; the *lift* is a hypothesis. The hook bench (§5.5) is how we would measure it — and
  the Phase-1 tournament is the place to run it.
- **What this research does NOT claim:** that the Film Studio was wasted. Its continuity gate, cost model and
  hard-won prohibitions are correct and get reused. The gap is one missing department and one missing regime.

## Sources
ltx.io/blog/common-prompt-mistakes-in-ai-video-generation · ltx.io/blog/how-to-fix-slow-motion-in-ai-generated-video ·
aivid.video/blog/why-ai-video-motion-looks-unnatural-and-how-to-fix-it · passiveon.com/how-to-fix-ai-video-warping-with-camera-motion-prompting ·
hiapi.ai/en/blog/cinematic-camera-movements-ai-video-prompts · kling.ai/blog/kling-ai-camera-control-video-guide ·
mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video · atlabs.ai/blog/ultimate-guide-ai-camera-moves-prompts ·
clipia.ai/en/blog/seedance-2-vs-kling-3-vs-veo-3 · mhigrowthengine.com/blog/pattern-interrupt-ads-dtc ·
increditors.com/video-editing-for-meta-ads · zeely.ai/blog/7-scroll-stopping-hooks (Kantar 2026) ·
entropik.io/resources/blog-articles/scroll-stopping-ads-strategies · adsights.ai/resources/glossary/creative/thumb-stopping-creative ·
inceptly.com/simple-video-tricks-that-stop-the-scroll
Internal: [[image-to-video-prompt-method]] · [[ai-film-studio]] · [[video-ad-decomposition-2026]] · [[ai-emotional-video-ad-playbook]]
