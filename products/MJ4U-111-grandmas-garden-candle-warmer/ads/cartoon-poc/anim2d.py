#!/usr/bin/env python3
"""anim2d.py — code-driven 2D animation from AI-illustrated layers.

Proof of concept for the "illustrated world, real product" format
(see research/reference/ad-video-director-research.md + ad-science-foundations.md).

The point: consistency comes from REUSING one asset, not from prompting a style per clip.
Every frame here is the same PNG under a deterministic transform, so identity/scale/text
cannot drift. Motion is frame-exact, which is what lets us hit the measured targets our
shipped film missed (hook-window motion, cut rate, motion-ONSET events).

Structure (3.0s, 24fps, 720x1280):
  Shot A  0.00-0.96  illustrated wide.  STILLNESS (8 frames) -> hard ONSET: lamp blooms +
                     push-in starts. The stillness is deliberate: motion onset is more
                     salient than smooth motion (pmcid:PMC3711149), and onset needs a
                     still baseline to read against.
  Shot B  0.96-1.71  HARD CUT to illustrated close-up (scale jump = salience event).
  Shot C  1.71-3.00  HARD CUT to the REAL product photograph. The medium change is the
                     biggest frame-difference event in the piece and it is placed exactly
                     at the reveal - where our shipped film measured 3.09 (its coldest).
                     The real photo also carries the "will it look cheap?" objection,
                     which a drawing cannot answer.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, subprocess, sys

W, H, FPS = 720, 1280, 24
HERE = os.path.dirname(os.path.abspath(__file__))
L, B, OUT = (os.path.join(HERE, d) for d in ("layers", "build", "out"))
REAL = os.path.abspath(os.path.join(HERE, "..", "film", "refs", "product", "real-product.jpg"))

# shot boundaries in frames
A_END, B_END, TOTAL = 23, 41, 72
ONSET = 8                    # frame where stillness breaks

def font(sz, bold=True):
    for p in ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else
              "/System/Library/Fonts/Supplemental/Georgia.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "/System/Library/Fonts/Helvetica.ttc"):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except Exception: pass
    return ImageFont.load_default()

def cover(img, w, h):
    """scale-and-crop to exactly w x h (like CSS object-fit: cover)"""
    s = max(w / img.width, h / img.height)
    img = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)
    return img.crop(((img.width - w) // 2, (img.height - h) // 2,
                     (img.width - w) // 2 + w, (img.height - h) // 2 + h))

def ease(t):                 # smooth in/out
    return t * t * (3 - 2 * t)

def bloom(size, cx, cy, r, strength):
    """procedural warm radial light - drawn in code, so it is identical every run"""
    w, h = size
    g = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(g)
    steps = 26
    for i in range(steps, 0, -1):
        rr = r * i / steps
        v = int(255 * strength * (1 - i / steps) ** 1.7)
        d.ellipse([cx - rr, cy - rr * 0.92, cx + rr, cy + rr * 0.92], fill=v)
    g = g.filter(ImageFilter.GaussianBlur(r * 0.13))
    warm = Image.new("RGB", (w, h), (255, 196, 112))
    return warm, g

def shot_a(bg, char, i):
    """illustrated wide: still -> onset (bloom + push-in + parallax)"""
    t = 0.0 if i < ONSET else ease(min(1.0, (i - ONSET) / (A_END - ONSET)))
    micro = 0.0015 * math.sin(i * 0.5)               # barely-there breathing before onset
    z = 1.02 + 0.055 * t + micro
    frame = cover(bg, int(W * z), int(H * z))
    # character parallax: moves slightly more than the background
    cz = 0.62 * z
    c = char.resize((int(char.width * cz * (W / 1200)), int(char.height * cz * (W / 1200))), Image.LANCZOS)
    cx = int(W * 0.50 - c.width / 2 + 10 * t)
    cy = int(H * 0.52 - c.height * 0.40 + 14 * t)
    off = ((frame.width - W) // 2, (frame.height - H) // 2)
    frame = frame.crop((off[0], off[1], off[0] + W, off[1] + H)).convert("RGB")
    frame.paste(c, (cx, cy), c)
    if t > 0:                                        # the lamp coming on IS the onset
        warm, mask = bloom((W, H), int(W * 0.70), int(H * 0.44), 330, min(1.0, t * 1.9))
        frame = Image.composite(Image.blend(frame, warm, 0.55), frame, mask)
    return frame

def shot_b(bg, char, i):
    """HARD CUT to close-up - reuses the SAME layers, just a tighter transform"""
    t = ease((i - A_END - 1) / max(1, B_END - A_END - 1))
    z = 2.30 + 0.16 * t
    frame = cover(bg, int(W * z), int(H * z))
    cz = 0.62 * z
    c = char.resize((int(char.width * cz * (W / 1200)), int(char.height * cz * (W / 1200))), Image.LANCZOS)
    cx = int(W * 0.50 - c.width / 2)
    cy = int(H * 0.30 - c.height * 0.17 - 26 * t)
    off = ((frame.width - W) // 2, int((frame.height - H) * 0.42))
    frame = frame.crop((off[0], off[1], off[0] + W, off[1] + H)).convert("RGB")
    frame.paste(c, (cx, cy), c)
    warm, mask = bloom((W, H), int(W * 0.74), int(H * 0.30), 300, 0.9)
    return Image.composite(Image.blend(frame, warm, 0.42), frame, mask)

def shot_c(real, i):
    """HARD CUT to the REAL product. Medium change = the largest salience event, at the reveal."""
    t = ease((i - B_END - 1) / max(1, TOTAL - B_END - 2))
    z = 1.34 - 0.30 * t                              # push in toward the printed names
    frame = cover(real, int(W * z), int(H * z))
    off = ((frame.width - W) // 2, int((frame.height - H) * 0.30))
    frame = frame.crop((off[0], off[1], off[0] + W, off[1] + H)).convert("RGB")
    # text composited in code -> vector-sharp, never garbled, swappable per recipient
    if t > 0.18:
        d = ImageDraw.Draw(frame)
        a = min(1.0, (t - 0.18) / 0.3)
        f1, f2 = font(60), font(38, False)
        for txt, f, y in (("Her garden.", f1, H * 0.075), ("Their names.", f1, H * 0.075 + 68),
                          ("Made just for her.", f2, H * 0.075 + 156)):
            tw = d.textlength(txt, font=f)
            x = (W - tw) / 2
            d.text((x + 2, y + 2), txt, font=f, fill=(0, 0, 0, int(90 * a)))
            d.text((x, y), txt, font=f, fill=(255, 250, 240))
    return frame

def main():
    bgp, chp = os.path.join(L, "bg.png"), os.path.join(L, "char.png")
    for p in (bgp, chp, REAL):
        if not os.path.exists(p):
            sys.exit(f"missing layer: {p}")
    bg = Image.open(bgp).convert("RGB")
    char = Image.open(chp).convert("RGBA")
    real = Image.open(REAL).convert("RGB")
    os.makedirs(B, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    for i in range(TOTAL):
        f = shot_a(bg, char, i) if i <= A_END else shot_b(bg, char, i) if i <= B_END else shot_c(real, i)
        f.save(os.path.join(B, f"f{i:03d}.png"))
    mp4 = os.path.join(OUT, "cartoon-poc-3s.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
                    "-i", os.path.join(B, "f%03d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", mp4], check=True)
    print("wrote", mp4)

if __name__ == "__main__":
    main()
