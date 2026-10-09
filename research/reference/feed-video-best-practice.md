# Meta Feed Video Ads (Facebook + Instagram Feed): best practice, 2025–2026

Researched 2026-10-09 for the Suncatcher Phase-1 Feed cuts. Scope: the **Feed** placement only (FB Feed,
IG Feed). Reels/Stories rules live in `short-form-caption-design.md` and `script-method.md`.

**Grades:** **A** = Meta official (Ads Guide, Business Help Center, Meta for Business) ·
**B** = data-backed third party · **C** = practitioner opinion / our own measurement or inference.

Note: several Meta "creative considerations" (sound-off, capture attention quickly, brand early) come from
Meta tests published in 2016 and still sit on Meta's site unchanged. They are official (A) but old.

## The rules

### Format and spec
1. **Facebook Feed video: 4:5 is the recommended ratio.** Meta's placement table marks 4:5 as "Recommended for
   both images and videos" on FB Feed; 1:1, 16:9 and 1.91:1 are supported. (A) [Aspect ratios by placement](https://www.facebook.com/business/help/682655495435254),
   [Crop media for a video ad](https://www.facebook.com/business/help/268849943715692)
2. **Recommended resolution 1440×1800** (4:5) for FB Feed video. 1080×1350 is the common minimum and is accepted. (A for 1440×1800;
   1080×1350 floor is C/industry) [Ads Guide: Video, Facebook Feed](https://www.facebook.com/business/ads-guide/update/video)
3. **Encoding:** MP4/MOV, H.264, square pixels, fixed frame rate, progressive, **stereo AAC ≥128 kbps**. No edit lists. (A) same page.
4. **Instagram Feed video: Meta's Ads Guide now lists 9:16 (1080×1920) as the recommended ratio.** 4:5 and 1:1 are still supported.
   A 9:16 video in IG Feed **follows the Reels/Stories safe zone** (top, bottom, sides kept clear). (A)
   [Ads Guide: IG Feed video](https://www.facebook.com/business/ads-guide/update/video/instagram-feed), [Safe zones](https://www.facebook.com/business/help/980593475366490)
   - Third-party sources still say 4:5 for IG Feed, and on FB Feed a 9:16 asset is cropped or masked to roughly 4:5 with the top and bottom cut.
     (C) [adsuploader](https://adsuploader.com/blog/meta-ads-aspect-ratios), [Webtopia](https://www.webtopia.co/blog/meta-video-ads-the-9-16-creative-guide-for-dtc-brands)
   - We have **no published data on 4:5 vs 9:16 performance in IG Feed**. Claims like "9:16 gets +7% CTR" or "60% cheaper CPMs" are anecdotes (C). Test it; don't assume either way.
5. **Supply a separate asset for each placement.** Asset customization lets one ad show a different image or video in each placement:
   a 4:5 video for Feed and a 9:16 video for Stories/Reels. (A for the feature) [About asset customization](https://www.facebook.com/business/help/1044825198987622),
   [Customize creative for placements](https://www.facebook.com/business/help/127128577862845).
   If you don't, Meta auto-crops or letterboxes the one asset you gave it (C, [Blip](https://withblip.com/blog/meta-ads-placement-customization-guide/)).
   One Reddit thread (2026) reports the upload-per-placement UI moving inside Ads Manager, so check the flow at upload time (C).

### Safe zone and text
6. **4:5 / 1:1 in IG Feed: keep the bottom and side edges clear of key elements, text and logos.** The profile icon, CTA
   and tag/mute icons sit there. (A) [Safe zones](https://www.facebook.com/business/help/980593475366490). Meta gives **no pixel number** for
   4:5 Feed. Our working margin is **≥10% from the bottom (≥135px at 1350 tall) and ≥6% from each side (≥65px)**. The 6% side figure
   comes from Meta's Reels guidance; the rest is C.
7. **Text overlay rules: a clean font, large type, a contrasting colour, don't block the visuals, don't say too many things.** (A) same page.
   In practice: one idea per screen, ≤2 lines, ~60px cap height at 1080 wide (C; see `short-form-caption-design.md`).
8. **Design for sound off and caption the whole story.** Meta: "most video ads in mobile feed are viewed without sound… showing captions,
   logos and products can help communicate your message." (A) [Meta: building video for mobile feed](https://www.facebook.com/business/news/building-video-for-mobile-feed).
   Up to **85% of FB video views were silent** (B, publisher data, 2016, [Digiday](https://digiday.com/media/silent-world-facebook-video/)).
   Meta's internal test showed captioned video ads gained **+12% view time** (A, 2016, [Meta](https://www.facebook.com/business/news/updated-features-for-video-ads)).
   The repo's caption doc lists the +12% as unverified. It is Meta's own claim and it is old, so treat it as a direction, not a number to rely on.
   Captions are "optional, but recommended" in the FB Feed spec (A).
9. **Burned-in captions can collide with Meta's own CC.** FB can show auto-generated captions at the bottom of the video.
   Keeping our captions above the bottom ~10% lowers the overlap risk. (C)

### Story and edit
10. **Capture attention fast: brand, product or person visible in the first seconds.** Meta's examples: Finish moved the brand 25s
    earlier and got +68% 3-second views and +136% 10-second views. Wells Fargo moved the brand earlier, went square and added text, and got 2× more impressions reaching
    the brand. (A, 2016 tests) [Meta](https://www.facebook.com/business/news/building-video-for-mobile-feed)
11. **Feed length: aim for ≤15s, with the main message in the first 3–5s.** (A: Meta's collaborative-ads creative guide, "Keep length <15s and
    main message in the first 3-5s", [PDF](http://d24wuq6o951i2g.cloudfront.net/img/events/457787735/assets/9522e30f.fordistribution_collaborativeadscreativebestpractice_compressed.pdf).
    Meta's Wrigley test cut 15s to 9s and got +8 pts ad recall.) Ads under 15s had up to 38% higher completion (B, UMass Amherst study via
    [DesignRush](https://www.designrush.com/best-designs/video/trends/facebook-video-ad-examples)).
    Practitioners say 15–30s works mid-funnel in Feed (C). A 20s story ad is allowed but should be tested against a ≤15s cutdown.
12. **Frame the story for a small screen.** Meta: "play with zoom, crop and overall visual composition". (A) So when a 9:16 shot is
    re-framed to 4:5, check that nothing important (name, product, light, faces) sits on the crop edge (C).
13. **Pacing: Feed tolerates slower shots than Reels.** People can scroll past instead of swiping away, and the video sits next to the post text.
    We found **no Meta or data-backed cut-rate number for Feed vs Reels.** Working rule: keep motion in every shot and no
    static frame longer than ~4s. (C)
14. **One CTA, readable, inside the safe zone, held ≥2s at the end.** Meta: "ads usually only have one call to action". (A on single CTA;
    duration C) The footer CTA button and headline sit **below** the video in Feed. Primary text 50–150 characters, headline ≤27 (A, Ads Guide).
    With Awareness/reach objectives the footer is hidden on FB mobile Feed, so the in-video CTA matters more there (A).
15. **Logo/brand mark must be legible at phone size.** A 1080-wide frame shows ~390pt wide on a phone, so a wordmark under ~40px tall at 1080 cannot be read (C).
16. **Sound is still worth having** ("Video sound: optional, but recommended", A). Loudness around −16 LUFS integrated, true peak ≤ −1.5 dB (C, platform norm).

## What this changes for us
- **Keep making a separate 4:5 Feed cut.** That matches Meta's FB Feed recommendation, and the pipeline already re-frames instead of
  letterboxing. Assign it with **asset customization**: 4:5 → FB Feed (+ Explore and other feeds), 9:16 → Stories/Reels.
- **IG Feed is a live question.** Meta now recommends 9:16 there. Run one ad set where IG Feed gets the 9:16 Reels cut (its text is
  already in the Reels safe zone) and compare it with the 4:5 Feed cut. Don't decide this from opinion.
- **20s is above Meta's ≤15s Feed guidance.** Keep the 20s story as the control and make a ≤15s Feed cutdown to test against it.
- **Captions: keep them ≥10% off the bottom.** The logo also has to move up into the safe zone and get bigger.
- Every Feed re-frame needs a per-shot crop check (rule 12). Both known Phase-1 failures are crop/caption collisions.
