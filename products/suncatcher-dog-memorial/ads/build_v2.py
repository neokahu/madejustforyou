#!/usr/bin/env python3
"""Assemble the Phase-1 v2 suncatcher ads (script: marketing/facebook-ads/PHASE1-SUNCATCHER-shooting-scripts.md).

Hard cuts only. Ken Burns shots are cut frame-by-frame from the 4K stills (nothing is re-synthesised,
so "Alex" stays exact). Video clips are trimmed to varied beat lengths. Captions are burned inside the
Reels safe zone. Output: ads/out/<ad>.mp4 (1080x1920, 25fps) + the 4:5 static.

    python3 ads/build_v2.py            # build everything
    python3 ads/build_v2.py S-C6       # one ad
"""
import os, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                     # products/suncatcher-dog-memorial
BUILD, OUT = f"{HERE}/build", f"{HERE}/out"
W, H, FPS = 1080, 1920, 25
LOGO = os.path.join(ROOT, "../../library/brand/logo/lockup-horizontal.png")
MUSIC = f"{HERE}/shots/music.mp3"
SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SERIF_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"

PANEL = f"{ROOT}/tests/testF-nanobananapro.png"   # PANEL-4K
BOX = f"{HERE}/frames/F-BOX.png"
PHOTO = f"{HERE}/frames/F-PHOTO.png"   # photo2-v1 upscaled; photo-v1 rejected (face-swap seam)
WALL = f"{ROOT}/tests/testC3-moving-open.mp4"

# Ken Burns paths in source pixels: (cx, cy, crop_width) start -> end. Height = width * 16/9.
KB = {
    "P_HOOK":  (PANEL, (1536, 2750, 3072), (1550, 2850, 2150)),
    "P_CTA":   (PANEL, (1500, 2660, 2350), (1540, 2780, 1880)),
    "BOX":     (BOX,   (1536, 2752, 3072), (1610, 2930, 1350)),
    "PHOTO":   (PHOTO, (1600, 2720, 2700), (1540, 2450, 2000)),
}

# Each shot: (kind, source, start_s, dur_s, caption, caption_style)
#   kind "kb" -> source is a KB key; "clip" -> source is a video path, start_s is the in-point.
#   caption_style: "hook" (bold, top), "story" (regular, lower third), "cta" (bold + logo)
ADS = {
    "S-C6": [
        ("kb",   "P_HOOK", 0,   1.8, "Her dog died on Tuesday.", "hook"),
        ("clip", f"{HERE}/shots/phone.mp4",   1.6, 2.4, "I didn't know what to send.", "story"),
        ("clip", f"{HERE}/shots/florist.mp4", 1.0, 2.6, "Flowers felt wrong. They die too.", "story"),
        ("kb",   "BOX",    0,   3.6, "So I sent him.\nHis breed. His name.", "story"),
        ("clip", f"{HERE}/shots/handoff.mp4", 1.4, 3.4, "", "story"),   # friend -> grieving owner (woman)
        ("clip", WALL,                        2.2, 2.8, "Now the room goes gold\nat four o'clock.", "story"),
        ("kb",   "P_CTA",  0,   3.4, "Make their dog's suncatcher", "cta"),
    ],
    "S-C1": [
        ("kb",   "P_HOOK", 0,   2.0, "Made with his breed.\nAnd his name.", "hook"),
        ("clip", WALL,                        0.0, 2.2, "Hang it where the\nafternoon sun comes in", "story"),
        ("clip", WALL,                        2.2, 2.8, "and his shape\nlands on the wall.", "story"),
        ("kb",   "PHOTO",  0,   3.8, "Choose the breed.\nAdd the name.", "story"),
        ("clip", f"{HERE}/shots/owner.mp4",   0.1, 4.8, "Every afternoon at four.", "story"),
        ("kb",   "P_CTA",  0,   4.4, "Make their dog's suncatcher", "cta"),
    ],
}


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def caption_png(text, style, path):
    """Transparent 1080x1920 overlay. Hook sits above the panel (y 0.17), story in the lower third
    (y 0.73), both clear of the Reels top bar (<14%) and bottom UI (>80%)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if not text:
        img.save(path); return
    bold = style in ("hook", "cta")
    size = 70 if bold else 60
    yc = {"hook": 0.17, "story": 0.73, "cta": 0.70}[style]
    lines = text.split("\n")
    d = ImageDraw.Draw(img)
    while True:
        font = ImageFont.truetype(SERIF_B if bold else SERIF, size)
        if max(d.textbbox((0, 0), ln, font=font)[2] for ln in lines) <= W - 2 * 90 or size <= 34:
            break
        size -= 2
    lh = int(size * 1.28)
    y0 = int(H * yc - lh * len(lines) / 2)
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
    top, bot = y0 - 46, y0 + lh * len(lines) + 46
    for yy in range(max(0, top), min(H, bot)):
        a = int(140 * min(1.0, min(yy - top, bot - yy) / 50.0))
        bd.line([(0, yy), (W, yy)], fill=(0, 0, 0, a))
    img = Image.alpha_composite(img, band); d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        tw = d.textbbox((0, 0), ln, font=font)[2]
        x, y = (W - tw) // 2, y0 + i * lh
        d.text((x + 2, y + 3), ln, font=font, fill=(0, 0, 0, 200))
        d.text((x, y), ln, font=font, fill=(255, 255, 255, 255))
    if style == "cta":
        logo = Image.open(LOGO).convert("RGBA")
        logo = logo.resize((380, int(logo.height * 380 / logo.width)), Image.LANCZOS)
        # white lockup on a soft band, under the CTA
        r, g, b, a = logo.split()
        white = Image.merge("RGBA", (a.point(lambda v: 255), a.point(lambda v: 255), a.point(lambda v: 255), a))
        img.alpha_composite(white, ((W - logo.width) // 2, int(H * 0.775)))
    img.save(path)


def kb_segment(key, dur, out):
    src, (cx0, cy0, w0), (cx1, cy1, w1) = KB[key]
    im = Image.open(src).convert("RGB")
    n = int(round(dur * FPS))
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16",
                          "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n):
        t = i / max(1, n - 1)
        t = t * t * (3 - 2 * t) * 0.35 + t * 0.65          # gentle ease, never stops moving
        cx, cy, w = cx0 + (cx1 - cx0) * t, cy0 + (cy1 - cy0) * t, w0 + (w1 - w0) * t
        h = w * 16 / 9
        box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
        p.stdin.write(im.resize((W, H), Image.LANCZOS, box=box).tobytes())
    p.stdin.close(); p.wait()


def clip_segment(src, start, dur, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-i", src, "-t", str(dur),
         "-vf", f"scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1", "-an",
         "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out])


def build(ad):
    os.makedirs(f"{BUILD}/{ad}", exist_ok=True); os.makedirs(OUT, exist_ok=True)
    parts = []
    for i, (kind, src, start, dur, cap, style) in enumerate(ADS[ad]):
        raw, capp, seg = (f"{BUILD}/{ad}/{i:02d}-{s}" for s in ("raw.mp4", "cap.png", "seg.mp4"))
        (kb_segment(src, dur, raw) if kind == "kb" else clip_segment(src, start, dur, raw))
        caption_png(cap, style, capp)
        run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-i", capp, "-filter_complex",
             "[0:v][1:v]overlay=0:0,eq=saturation=1.04", "-t", str(dur), "-r", str(FPS),
             "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", seg])
        parts.append(seg)
    lst = f"{BUILD}/{ad}/concat.txt"
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    total = sum(s[3] for s in ADS[ad])
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", MUSIC,
         "-filter_complex", f"[1:a]atrim=0:{total},afade=t=out:st={total-1.4}:d=1.4,loudnorm=I=-16:TP=-1.5[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", "-t", str(total), f"{OUT}/{ad}.mp4"])
    print(f"built {OUT}/{ad}.mp4  ({total:.1f}s, {len(parts)} shots)")


def static():
    """4:5 baseline image ad from PANEL-4K."""
    im = Image.open(PANEL).convert("RGB")
    w = 3072; h = int(w * 5 / 4)
    cy = 2700
    im = im.crop((0, int(cy - h * 0.46), w, int(cy + h * 0.54))).resize((1080, 1350), Image.LANCZOS).convert("RGBA")
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    top = 1030
    for yy in range(top - 120, 1350):
        a = int(205 * min(1.0, (yy - (top - 120)) / 140))
        d.line([(0, yy), (1080, yy)], fill=(14, 16, 22, a))
    im = Image.alpha_composite(im, ov); d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(SERIF_B, 62); f2 = ImageFont.truetype(SERIF, 34)
    for txt, f, y in (("His breed. His name. In the light.", f1, top + 20),
                      ("Personalized memorial suncatcher · 6 in", f2, top + 112)):
        while d.textbbox((0, 0), txt, font=f)[2] > 980:
            f = ImageFont.truetype(f.path, f.size - 2)
        tw = d.textbbox((0, 0), txt, font=f)[2]
        d.text(((1080 - tw) // 2, y), txt, font=f, fill=(255, 255, 255, 255))
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((300, int(logo.height * 300 / logo.width)), Image.LANCZOS)
    a = logo.split()[3]
    white = Image.merge("RGBA", (a.point(lambda v: 255),) * 3 + (a,))
    im.alpha_composite(white, ((1080 - 300) // 2, 1350 - 70 - logo.height))
    im.convert("RGB").save(f"{OUT}/S-STATIC.jpg", quality=93)
    print(f"built {OUT}/S-STATIC.jpg")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    targets = sys.argv[1:] or list(ADS) + ["S-STATIC"]
    for t in targets:
        static() if t == "S-STATIC" else build(t)
