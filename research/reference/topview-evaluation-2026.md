# TopView.ai — evaluation for our ad-video pipeline (2026-09-25)

> ## ✅ TESTED 2026-09-25 — verdict below is now evidence, not projection
> Ran on the real product (German Shepherd · "Alex"). Canvas
> `4ed6f979c13244c9b8ba102ae2d14d91`, renders in `products/suncatcher-dog-memorial/tests/`.
> **Cost: $0** — OAuth granted free quota (5 MiniMax-H3 video, 5 Wan 3.0 video, 10 GPT Image 2.5),
> so the 80 plan credits were never touched.
>
> | Test | Result |
> |---|---|
> | **A · product scale in a wide shot** | **PASS** — stayed hand-sized against the window sash, the exact framing where our rule #3 says models oversize |
> | **B · identity across a camera change** | **PASS** — same man from ONE reference across a ¾ turn, pose and framing change; room continuity preserved unprompted |
> | **C · motion gate** | **PASS** — hook3 **12.11** vs gate 8.0, motion **11.83**, static **0%** |
> | **product fidelity in video** | **FAIL** — the dog shadow morphs sitting → standing across 5s; "Alex" grows from small script to a body-spanning word |
>
> **What the tests changed:**
> - **B is the headline.** Our rule #2 requires a locked turntable because otherwise the model invents
>   a new person per clip (the MJ4U-111 failure). TopView held identity from a single image. That is a
>   capability we did not have.
> - **I was wrong about OFAT.** I argued TopView would break the test because it auto-plans scenes.
>   Driving `image_edit` / `image_to_video` directly through the MCP gives explicit per-shot control —
>   no auto-storyboarding involved. OFAT is ours to enforce in prompts, and it is enforceable here.
> - **I was wrong about the projection.** I claimed an opaque silhouette cannot project a legible name.
>   The name and florals are printed *pale on the black dog*, making them the panel's most translucent
>   areas — they read as bright script inside the dark shadow, and the wall gives the name more pixels
>   than the glass does.
> - **The image/video split is now measured, not assumed.** Image models held the product; the video
>   model drifted over 5 seconds. That is precisely the morph our QA rule #10 exists to catch.
>
> **Division of labour, settled:** TopView generates plates, camera and motion. **PIL composites the
> panel, shadow and name.** `motion_qa.py` stays the gate. ffmpeg stays the assembler.
>
> ⚠️ **The pretty-but-wrong trap is real.** Test C passed every number and still misrepresented the
> product. Never let the gate stand in for looking at the frames.

**Verdict: worth buying — but at the Pro tier, and not for the reason the marketing suggests.**
The headline "365-Day Unlimited Seedance" is explicitly barred from automation. What's actually worth
paying for is **Product AnyShoot location control**, **Omni Reference**, and model breadth behind one key.

---

## ⚠️ Two findings that change the purchase decision

### 1. Unlimited does not work with MCP or API — in their own words

> "Unlimited models and Free Generations on plans are accessible only via topview.ai and are **not
> accessible on MCP/CLI, API or other automation methods**."
> "Any signs of automation, scripting, or non-human activity can result in a temporary pause of your
> unlimited access for manual review."
> FAQ: *"Can I use Unlimited with Topview MCP, Plugin, or Skill?"* → **"No."**

So every "60-Day Unlimited Seedance 2.5" / "365-Day Unlimited" badge on the pricing page is **GUI-only**.
Through the MCP we pay credits like anyone else. Buying a tier *for* the unlimited deal and then driving
it from here would get nothing — and could flag the account.

### 2. The 3D Shot Composer — the feature we actually wanted — appears to be GUI-only

The full API index (`docs.topview.ai/llms.txt`, ~120 endpoints) has **no shot-composer or canvas
endpoint.** Closest is **Product AnyShoot**, which has a *Location Parameters Document* — real spatial
placement of a product in a scene, driveable by API — but that is product-in-scene compositing, not
character-and-prop 3D blocking with a virtual camera.

And their own 3D Shot Composer page carries this caveat:

> "Model outputs can still vary; **this locks the spatial plan, not pixel identity.**"

It's a previz tool using grey mannequins. It fixes *where things are and where the camera is*. It does
**not** fix who the person is across shots. Our character-turntable rule stays either way.

---

## What the API actually exposes (the useful parts)

| Endpoint group | Why it matters to us |
|---|---|
| **Image-to-Video V2** — single image, first/last frame, **multiple reference images** | direct replacement for our AtlasCloud Seedance ref-to-video calls |
| **Omni Reference** — reference *images and videos* guide generation | stronger conditioning than plain ref-to-video; we have no equivalent |
| **Product AnyShoot (Model + Background) + Location Parameters** | API-level control of where the product sits in the scene — the closest thing to "prompt exactly what appears where" |
| **Motion Control** — character image + motion reference | candidate fix for identity/motion consistency |
| **Storyboard** submit/query | boards as images |
| **Character Swap** (image + video) | consistency repair after the fact |
| Text-to-image / Image Edit / Remove BG / AI Music / TTS / Voice clone | we already have these via kie.ai + AtlasCloud |
| Boards, batch download, **credit query** | lets me keep a live cost tally, like our current budget rule |

Models behind one key: Seedance 2.5 / 2.0 / Fast / Mini, Wan 3.0, Kling 2.6 / o1, Veo 3.1, MiniMax H3,
Nano Banana 2 / Pro, Seedream 5.0, GPT Image 2.5.

## Cost — against our known $0.98/clip

Our suncatcher build is **18 clips of 4–5s plus ~8 reference images**.

| | Credits |
|---|---|
| 18 × Seedance 2.0 Fast (4 cr / 5s) | 72 |
| 8 × Seedream 5.0 2K (0.2 cr) | 1.6 |
| Music | ~1 |
| **Whole suncatcher build** | **≈ 75 credits** |

| Plan (annual) | Price/yr | Credits/yr | MCP | API | ≈ cost/clip | Suncatcher builds/yr |
|---|---|---|---|---|---|---|
| **Pro** | **$192** | 960 | ✅ | ✅ | **$0.80** | ~12 |
| Business | $528 | 3,000 | ✅ | ✅ | $0.70 | ~40 |
| Ultra | $600 | 500/mo | ✅ | ❌ *(not with plan credits)* | — | — |
| Team | $672/seat | 500/seat/mo | ✅ | ❌ | — | — |

**Ultra and Team are disqualified** — they carry MCP but not API on plan credits, and Ultra is the tier
the unlimited promo is designed to sell.

At Pro, cost per clip lands at **~$0.80 vs our current $0.98** — roughly parity, slightly cheaper. Cost is
not the reason to buy.

## What it would actually change in our pipeline

**Replaces:** the AtlasCloud generate call, and possibly our turntable stage if Omni Reference plus
Product AnyShoot hold identity and scale better than our reference images do.

**Does not replace:**
- **PIL text compositing.** The dog's name and breed on the glass, and the name projected on the wall,
  stay a post job. No endpoint renders reliable lettering.
- **`motion_qa.py`.** Still our gate, still benchmarked against the Macorner ad running 333 days.
- **ffmpeg assembly, grade, captions, end card.**
- **The OFAT discipline.** Whatever generates the footage, the body has to stay fixed while only the hook
  changes — that is a constraint on us, not a feature of theirs.

## Recommendation

**Buy Pro annual, $192.** It is the cheapest tier with both MCP and API, and 960 credits is ~12 complete
suncatcher builds — far more than the trial needs, and unused credits carry over if we upgrade.

Then run one test before committing the Phase-1 build to it, using the real product image:

1. **Product AnyShoot + Location Parameters** — place the suncatcher in a window at true scale. Does it
   hold scale in a wide? This is the direct test of "specify the location instead of trusting AI".
2. **Omni Reference** — same owner across a camera change. Does identity survive without our turntable?
3. **Image-to-Video V2 with multiple refs** — one beat, scored with `motion_qa.py` against
   `hook3 ≥ 8.0 · cuts_per_s ≥ 0.15 · static_pct ≤ 10`.

If 1 and 2 pass, TopView takes over generation and we keep PIL + ffmpeg + the gate. If they don't, we've
spent $192 to find out, and the answer is still a number rather than an opinion.

**Do not buy Ultra for the unlimited deal.** It cannot be driven from here.

## Sources
topview.ai/3d-shot-composer · topview.ai/mcp · topview.ai/pricing · docs.topview.ai/llms.txt ·
docs.topview.ai/docs/getting-started · github.com/topviewai/skill
