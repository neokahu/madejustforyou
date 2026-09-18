#!/usr/bin/env python3
"""solve_match.py — measure the lamp shade in both images and SOLVE the match-cut framing.

Eyeballing the alignment put the painted shade ~30% oversize and offset; a match cut that
close-but-wrong reads as a jump. So detect the shade (large bright low-saturation blob in the
upper half), then compute the crop rects that place it at the same screen position and size
in both. Deterministic - re-run if either plate changes.
"""
from PIL import Image
import os, json

W, H = 720, 1280
HERE = os.path.dirname(os.path.abspath(__file__))
SHADE_SCREEN = (0.50, 0.30, 0.46)   # target: shade centre x, centre y, width as frac of frame


def shade_bbox(path, ymax=0.62, vmin=228, smax=26, step=3):
    """bbox of the bright near-neutral shade, in plate fractions"""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = im.load()
    xs, ys = [], []
    for y in range(0, int(h * ymax), step):
        for x in range(0, w, step):
            r, g, b = px[x, y]
            mx, mn = max(r, g, b), min(r, g, b)
            if mx >= vmin and (mx - mn) <= smax:
                xs.append(x); ys.append(y)
    if not xs:
        raise SystemExit(f"no shade found in {path}")
    # trim outliers (stray highlights) to the central 96%
    xs.sort(); ys.sort()
    lo, hi = int(len(xs) * 0.02), int(len(xs) * 0.98)
    x0, x1 = xs[lo], xs[hi - 1]
    y0, y1 = ys[lo], ys[hi - 1]
    return dict(size=(w, h), cx=(x0 + x1) / 2 / w, cy=(y0 + y1) / 2 / h,
                wf=(x1 - x0) / w, px=(x0, y0, x1, y1))


def solve(b):
    """crop rect (x0f, y0f, wf) putting the shade at SHADE_SCREEN"""
    tcx, tcy, tw = SHADE_SCREEN
    pw, ph = b["size"]
    shade_px = b["wf"] * pw
    fw = shade_px / tw                       # frame width in plate px
    fh = fw * (H / W)
    x0 = b["cx"] * pw - tcx * fw
    y0 = b["cy"] * ph - tcy * fh
    clamped = []
    if x0 < 0: x0, c = 0, clamped.append("x<0")
    if y0 < 0: y0, c = 0, clamped.append("y<0")
    if x0 + fw > pw: x0, c = pw - fw, clamped.append("x>w")
    if y0 + fh > ph: y0, c = ph - fh, clamped.append("y>h")
    return (round(x0 / pw, 4), round(y0 / ph, 4), round(fw / pw, 4)), clamped, (fw, fh)


for name, path in (("painted", os.path.join(HERE, "layers", "plate-lamp.png")),
                   ("real", os.path.abspath(os.path.join(HERE, "..", "film", "refs", "product", "real-product.jpg")))):
    b = shade_bbox(path)
    rect, clamped, (fw, fh) = solve(b)
    print(f"{name:8} plate={b['size']}  shade centre=({b['cx']:.3f},{b['cy']:.3f}) "
          f"width={b['wf']:.3f}  ->  rect={rect}  frame={int(fw)}x{int(fh)}"
          + (f"  CLAMPED {clamped}" if clamped else ""))
