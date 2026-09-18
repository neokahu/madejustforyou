#!/usr/bin/env python3
"""prep_layers.py — turn raw AI illustrations into clean animation layers. Deterministic.

char: flood-fill the flat grey studio background from the edges, then ERODE the alpha to
      eat the white "sticker" rim the model draws around isolated subjects, then feather.
bg:   crop the painted paper border so the frame is full-bleed.
Run once; the outputs are the assets every frame reuses, which is what makes identity
and scale impossible to drift.
"""
from PIL import Image, ImageDraw, ImageFilter
import os
HERE = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(HERE, "layers")

# ---- character ----
src = Image.open(os.path.join(L, "char-raw.png")).convert("RGB")
w, h = src.size
MARK = (255, 0, 255)
work = src.copy()
d = ImageDraw.Draw(work)
for seed in [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3), (w // 2, 2), (w // 2, h - 3), (2, h // 2), (w - 3, h // 2)]:
    ImageDraw.floodfill(work, seed, MARK, thresh=42)
px = work.load()
alpha = Image.new("L", (w, h), 255)
ap = alpha.load()
for y in range(h):
    for x in range(w):
        if px[x, y] == MARK:
            ap[x, y] = 0
# erode ~7px to remove the white outline, then soften the edge
alpha = alpha.filter(ImageFilter.MinFilter(15)).filter(ImageFilter.GaussianBlur(1.6))
out = src.convert("RGBA"); out.putalpha(alpha)
bbox = alpha.point(lambda v: 255 if v > 8 else 0).getbbox()
out = out.crop(bbox)
out.save(os.path.join(L, "char.png"))
print("char.png", out.size, "(cropped to subject)")

# ---- background: trim the painted paper border ----
bg = Image.open(os.path.join(L, "bg.png")).convert("RGB")
m = 0.045
bg = bg.crop((int(bg.width * m), int(bg.height * m),
              int(bg.width * (1 - m)), int(bg.height * (1 - m))))
bg.save(os.path.join(L, "bg.png"))
print("bg.png", bg.size, "(border trimmed)")
