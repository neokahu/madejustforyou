#!/usr/bin/env python3
"""Assemble the 6 Phase-1 suncatcher ads (S-C{1,2,3}-H{1,2}) — re-edit v2.

Spec: marketing/facebook-ads/suncatcher-phase1/CAPTION-SHEET.md + EDIT-CRITERIA.md §(f), with the user's
2026-10-09 decisions: H1 hook "His actual breed. / His actual name."; both hooks 0.0-3.2, beat-2 captions from
3.2; hard cuts everywhere except ONE 0.4s dissolve centred on 6.0 (all 6 ads); C3's 12.0 is a hard cut.
Shots: hook 2.0 · B2 4.0 · B3a 2.8 · B3b 3.2 · B4 5.0 (C3: B4a 3.0 + B4b 2.0) · B5 3.0. No media generated.

    python3 ads/build_phase1.py [S-C1-H1 ...]
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FMT = os.environ.get("FMT", "reels")            # reels = 9:16 1080x1920 · feed = 4:5 1080x1350 (re-framed, not letterboxed)
BUILD, OUT = f"{HERE}/build/phase1/{FMT}", f"{HERE}/out/phase1/{FMT}"
W, H, FPS = 1080, (1350 if FMT == "feed" else 1920), 25
# FEED re-aim: KB centre y per shot (start, end), "Alex" ~42% of the 4:5 frame (C3-B2 ends higher so the card stays in);
# clip crop = 720x900 window of the 720x1280 source at this y-offset (faces / panel / bed kept in frame).
KB_FEED_CY = {"HOOK-H1": (3212, 3310), "C3-B2": (3133, 2850), "B3b": (3313, 3268), "C3-B4b": (3826, 3790), "B5": (3375, 3300)}
CLIP_FEED_OFF = {"H2": 60, "C1-B2": 190, "C1-B4-t1": 190, "C2-B2": 150, "C2-B4-t2": 150, "C3-B4a-t1": 120, "testC3-moving-open": 190}
LOGO = os.path.normpath(os.path.join(ROOT, "../../library/brand/logo/lockup-horizontal.png"))
MUSIC = f"{HERE}/shots/music.mp3"
SANS_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
PANEL = f"{ROOT}/tests/testF-nanobananapro.png"
SH = f"{HERE}/shots/phase1"
FR = f"{HERE}/frames/phase1"
B3A = f"{ROOT}/tests/testC3-moving-open.mp4"
DISSOLVE_AT, DISSOLVE = 6.0, 0.4

# Ken Burns (cx, cy, crop_w) start -> end, source px. Spec §(f)3: end crops kept, start moved closer (slower).
KB = {
    "HOOK-H1": (PANEL, (1485, 3223, 1625), (1500, 3193, 2600)),            # 1.6x pull-out; "Alex" ~112px on frame 1, held at 44-47% height (above the band)
    "C3-B2": (f"{FR}/F-BOX-card.png", (1620, 3201, 1600), (1540, 3228, 2560)),  # 1.6x pull-out, "Alex" at 42-44% height
    "B3b": (f"{FR}/WALL-4K.png", (1987, 3291, 1950), (2137, 3331, 1500)),  # 1.3x push to "Alex" (~288px at end), "Alex" at 42-45% height
    "C3-B4b": (f"{FR}/C3-B4b.png", (1615, 3892, 1560), (1619, 3841, 1200)),  # 1.3x push; "Alex" at 42% height, 106px end
    "B5": (PANEL, (1514, 2745, 2600), (1500, 2640, 2000)),                 # 1.3x push-in
}

HOOK = {"H1": [("kb", "HOOK-H1", 0, 2.0)], "H2": [("clip", f"{SH}/H2.mp4", 0.0, 2.0)]}   # H2: 0.0-2.0 ONLY
BODY = {
    "C1": ([("clip", f"{SH}/C1-B2.mp4", 0.0, 4.0)], [("clip", f"{SH}/C1-B4-t1.mp4", 0.0, 5.0)]),
    "C2": ([("clip", f"{SH}/C2-B2.mp4", 0.0, 4.0)], [("clip", f"{SH}/C2-B4-t2.mp4", 0.0, 5.0)]),
    "C3": ([("kb", "C3-B2", 0, 4.0)], [("clip", f"{SH}/C3-B4a-t1.mp4", 0.0, 3.0), ("kb", "C3-B4b", 0, 2.0)]),
}
B3 = [("clip", B3A, 1.9, 2.8), ("kb", "B3b", 0, 3.2)]
B5 = [("kb", "B5", 0, 3.0)]

HOOK_CAP = {"H1": (0.0, 3.2, "His actual breed.|His actual name."),
            "H2": (0.0, 3.2, "We still leave the|window open for him.")}
B2_CAP = {"C1": "His bowl hasn't|moved since spring.",
          "C2": "His German Shepherd,|Alex, waited 11 years.",
          "C3": "My neighbor lost Alex.|Flowers felt wrong."}
B4_CAP = {"C1": "Only one Alex.|Only one of these.", "C2": "Alex is back|in his spot.", "C3": "This felt like Alex."}
BAND = (1000, 1210) if FMT == "reels" else (1010, 1210)  # feed: bottom third (75-90%); no Reels UI on Feed
BAND_R = (1000, 1210)          # one fixed body band (52-63%) in all 6: 36-47% covered the C1-B4 photo/shadow head and the hook dog head; "Alex" re-aimed above it
CTA_Y = 300 if FMT == "reels" else 1010
ADS = [f"S-{c}-{h}" for c in ("C1", "C2", "C3") for h in ("H1", "H2")]


def captions(c, h):
    a, b, t = HOOK_CAP[h]
    return [(a, b, t, "band"), (3.2, 6.0, B2_CAP[c], "band"),
            (6.0, 8.8, "Every afternoon,|he's back on the wall.", "band"),
            (8.8, 12.0, "His breed. His name.|In the light.", "band"),
            (12.5, 17.0, B4_CAP[c], "band"),
            (17.5, 20.0, "Make one that's|only theirs", "cta")]


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed: {' '.join(cmd)}\n{r.stderr[-2000:]}")


def nframes(d):
    return int(round(d * FPS))


def kb_segment(key, dur, out):
    src, (cx0, cy0, w0), (cx1, cy1, w1) = KB[key]
    if FMT == "feed":
        cy0, cy1 = KB_FEED_CY[key]
    im = Image.open(src).convert("RGB"); SW, SHh = im.size
    n = nframes(dur)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "15", "-pix_fmt", "yuv420p", out],
                         stdin=subprocess.PIPE)
    for i in range(n):
        t = i / max(1, n - 1)
        t = 0.6 * t * t * (3 - 2 * t) + 0.4 * t          # ease in/out, never stops (min speed 40%)
        cx, cy, w = cx0 + (cx1 - cx0) * t, cy0 + (cy1 - cy0) * t, w0 + (w1 - w0) * t
        h = w * H / W
        cx = min(max(cx, w / 2), SW - w / 2); cy = min(max(cy, h / 2), SHh - h / 2)
        p.stdin.write(im.resize((W, H), Image.LANCZOS, box=(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)).tobytes())
    p.stdin.close(); p.wait()


def clip_segment(src, start, dur, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start:.3f}", "-i", src, "-vf",
         (f"crop=720:900:0:{CLIP_FEED_OFF[os.path.basename(src)[:-4]]}," if FMT == "feed" else "") + f"fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1", "-an", "-frames:v", str(nframes(dur)),
         "-c:v", "libx264", "-crf", "15", "-pix_fmt", "yuv420p", out])


def caption_png(text, pos, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    font = ImageFont.truetype(SANS_B, 84)                # ~60px cap height, fixed size
    lines = text.split("|")
    d = ImageDraw.Draw(img)
    for ln in lines:
        assert d.textlength(ln, font=font) + 20 <= 950, (ln, d.textlength(ln, font=font))
    lh = 100
    block = lh * len(lines)
    y0 = CTA_Y if pos == "cta" else BAND[0] + (BAND[1] - BAND[0] - block) // 2
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(txt)
    for i, ln in enumerate(lines):
        td.text(((W - td.textlength(ln, font=font)) / 2, y0 + i * lh), ln, font=font, fill=(255, 255, 255, 255),
                stroke_width=10, stroke_fill=(0, 0, 0, 255))   # 10px black outline outside the glyph
    a = txt.split()[3]
    soft = Image.new("RGBA", (W, H), (0, 0, 0, 0)); soft.putalpha(a.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * 0.3)))
    img = Image.alpha_composite(Image.alpha_composite(img, soft), txt)
    if pos == "cta":
        logo = Image.open(LOGO).convert("RGBA"); lw = 340
        logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
        la = logo.split()[3]
        white = Image.merge("RGBA", (la.point(lambda v: 255),) * 3 + (la,))
        sh = Image.new("RGBA", white.size, (0, 0, 0, 0)); sh.putalpha(la.filter(ImageFilter.GaussianBlur(4)).point(lambda v: int(v * 0.6)))
        ly = int(H * 0.745) if FMT == "reels" else 1250
        img.alpha_composite(sh, ((W - lw) // 2 + 2, ly + 3)); img.alpha_composite(white, ((W - lw) // 2, ly))
    img.save(path)
    return y0, y0 + block


def build(ad):
    _, c, h = ad.split("-")
    b2, b4 = BODY[c]
    beats = HOOK[h] + b2 + B3 + b4 + B5
    d = f"{BUILD}/{ad}"; os.makedirs(d, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    # the dissolve is centred on 6.0: beat 2 runs 0.2s long, B3a starts 0.2s early (in-point 1.9 - 0.2)
    segs, t = [], 0.0
    for i, (kind, src, start, dur) in enumerate(beats):
        if abs(t + dur - DISSOLVE_AT) < 1e-6:
            dur += DISSOLVE / 2
        elif abs(t - DISSOLVE_AT) < 1e-6:
            start, dur = start - DISSOLVE / 2, dur + DISSOLVE / 2
        seg = f"{d}/{i:02d}.mp4"
        kb_segment(src, dur, seg) if kind == "kb" else clip_segment(src, start, dur, seg)
        segs.append((seg, t)); t += beats[i][3]
    assert abs(t - 20.0) < 1e-6
    k = next(i for i, (_, st) in enumerate(segs) if abs(st - DISSOLVE_AT) < 1e-6)
    inputs = sum((["-i", s] for s, _ in segs), []) + ["-i", MUSIC]
    na = len(segs)
    pre = "".join(f"[{i}:v]" for i in range(k)) + f"concat=n={k}:v=1:a=0,settb=AVTB,fps={FPS}[pa]"
    post = "".join(f"[{i}:v]" for i in range(k, na)) + f"concat=n={na - k}:v=1:a=0,settb=AVTB,fps={FPS}[pb]"
    chain = [pre, post, f"[pa][pb]xfade=transition=fade:duration={DISSOLVE}:offset={DISSOLVE_AT - DISSOLVE / 2}[v0]"]
    last = "v0"
    for j, (a, b, text, pos) in enumerate(captions(c, h)):
        png = f"{d}/cap{j}.png"; caption_png(text, pos, png)
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", "20", "-i", png]
        chain.append(f"[{last}][{na + 1 + j}:v]overlay=0:0:enable='gte(t,{a - 0.001})*lt(t,{b - 0.001})'[c{j}]")
        last = f"c{j}"
    chain.append(f"[{na}:a]atrim=0:20,asetpts=PTS-STARTPTS,afade=t=out:st=18.6:d=1.4,loudnorm=I=-16:TP=-1.5,aresample=48000[a]")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(chain), "-map", f"[{last}]", "-map", "[a]",
         "-r", str(FPS), "-frames:v", "500", "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", "-t", "20", f"{OUT}/{ad}.mp4"])
    print(f"built {OUT}/{ad}.mp4")


if __name__ == "__main__":
    for ad in sys.argv[1:] or ADS:
        build(ad)
