#!/usr/bin/env python3
"""anim2d.py v2 — camera moves through coherent painted plates. NO layer compositing.

v1 was wrong and looked it: a separately-generated character cut out and pasted onto a
separately-generated room. Two light directions, no contact shadow, hard alpha edge against
painterly edges, mismatched paint-grain scale. A collage, not a scene.

v2 technique — matte-painting camera work:
  * Each shot is a crop-and-zoom out of ONE high-res painted plate, so lighting, shadow,
    edge quality and grain are internally consistent by construction. Nothing is pasted.
  * Consistency still comes from reuse (the same plate every frame), so identity/scale
    cannot drift - the v1 property we keep.
  * The product cut is now a MATCH CUT: a painted lamp close-up framed to align with the
    real product photograph, so the transition reads as "the drawing becomes real" instead
    of two unrelated ads spliced together.

3.0s / 24fps / 720x1280:
  A 0.00-1.00  plate-1 wide. 8 frames of stillness, then onset: push-in + the lamp's warm
               pool intensifies (the lamp is now PAINTED IN the plate, so light has a source)
  B 1.00-1.63  HARD CUT to her face - a tight crop of the SAME plate (scale jump, coherent)
  C 1.63-2.25  HARD CUT to the painted lamp plate (still in-style)
  D 2.25-3.00  MATCH CUT to the REAL product, framed to align with C
"""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, math, subprocess, sys

W, H, FPS = 720, 1280, 24
HERE = os.path.dirname(os.path.abspath(__file__))
L, B, OUT = (os.path.join(HERE, d) for d in ("layers", "build", "out"))
REAL = os.path.abspath(os.path.join(HERE, "..", "film", "refs", "product", "real-product.jpg"))

A_END, B_END, C_END, TOTAL = 23, 38, 53, 72
ONSET = 8

# --- framing: (centre_x, centre_y, zoom) in normalised plate coords. Tuned by eye. ---
# zoom = fraction of the plate's SHORT axis the frame spans; smaller = tighter.
SCENE_WIDE  = (0.50, 0.55, 1.00)
SCENE_WIDE2 = (0.52, 0.53, 0.92)   # push-in target
FACE        = (0.410, 0.390, 0.32) # her face in plate-1
FACE2       = (0.410, 0.383, 0.29)
# MATCH CUT pair, solved so the shade lands at screen x 0.50 / y 0.416 at identical size:
# MATCH CUT — solved from MEASURED shade geometry (grid-read, see solve_match.py):
#   painted plate 1429x2559: shade centre (0.4825, 0.380), width 0.545 of plate
#   real photo   2000x2000: shade centre (0.4375, 0.355), width 0.325 of plate
# The painted shade is large relative to its plate, so it cannot be shown smaller than
# ~55% of frame width; the real photo is square, so its crop cannot exceed the height.
# Those two constraints force the shared target: shade at screen (0.48, 0.35), width 0.60.
LAMP_PAINT_R = (0.0465, 0.0643, 0.9083)  # painted lamp, held static
LAMP_REAL_R  = (0.1775, 0.0180, 0.5417)  # real photo - shade matched in size AND position
LAMP_REAL_R2 = (0.2035, 0.0517, 0.4875)  # then push in, holding the shade put


def font(sz, bold=True):
    for p in ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else
              "/System/Library/Fonts/Supplemental/Georgia.ttf",
              "/System/Library/Fonts/Helvetica.ttc"):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except Exception: pass
    return ImageFont.load_default()


def ease(t):
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return tuple(x + (y - x) * t for x, y in zip(a, b))


def camera(plate, framing):
    """Crop a 720x1280 view out of a plate at (cx, cy, zoom). This is the camera."""
    cx, cy, z = framing
    pw, ph = plate.size
    fh = ph * z
    fw = fh * (W / H)
    if fw > pw:
        fw = pw; fh = fw * (H / W)
    x0 = max(0, min(pw - fw, cx * pw - fw / 2))
    y0 = max(0, min(ph - fh, cy * ph - fh / 2))
    return plate.crop((int(x0), int(y0), int(x0 + fw), int(y0 + fh))).resize((W, H), Image.LANCZOS)


def camera_rect(plate, rect):
    """Explicit crop rect as (x0, y0, width) in plate fractions - height follows 9:16.

    Used for the MATCH CUT: the painted lamp and the real photograph have to put the
    shade at the SAME screen position and the SAME screen size, which is a solved
    alignment, not something to eyeball. camera() clamps at plate edges and would
    silently break that alignment; this does not.
    """
    x0f, y0f, wf = rect
    pw, ph = plate.size
    fw = wf * pw
    fh = fw * (H / W)
    x0, y0 = x0f * pw, y0f * ph
    return plate.crop((int(x0), int(y0), int(x0 + fw), int(y0 + fh))).resize((W, H), Image.LANCZOS)


def warm(img, amount):
    """Lift the warm pool slightly as the lamp 'comes up'. Grade, not a pasted glow."""
    if amount <= 0:
        return img
    img = ImageEnhance.Brightness(img).enhance(1 + 0.055 * amount)
    img = ImageEnhance.Color(img).enhance(1 + 0.07 * amount)
    r, g, b = img.split()
    r = r.point(lambda v: min(255, int(v * (1 + 0.022 * amount))))
    b = b.point(lambda v: int(v * (1 - 0.018 * amount)))
    return Image.merge("RGB", (r, g, b))


def titles(frame, t):
    """Code-composited, so vector-sharp and swappable per recipient."""
    if t <= 0.20:
        return frame
    a = min(1.0, (t - 0.20) / 0.28)
    scrim = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(scrim)
    for y in range(int(H * 0.34)):                      # linear falloff, no hard edge
        sd.line([(0, y), (W, y)], fill=int(150 * a * (1 - y / (H * 0.34))))
    frame = Image.composite(Image.new("RGB", (W, H), (38, 24, 12)), frame, scrim)
    d = ImageDraw.Draw(frame)
    f1, f2 = font(58), font(34, False)
    for txt, f, y in (("Her garden.", f1, H * 0.068),
                      ("Their names.", f1, H * 0.068 + 66),
                      ("Made just for her.", f2, H * 0.068 + 150)):
        tw = d.textlength(txt, font=f)
        x = (W - tw) / 2
        d.text((x + 2, y + 2), txt, font=f, fill=(60, 40, 20))
        d.text((x, y), txt, font=f, fill=(255, 250, 242))
    return frame


def main():
    p1 = os.path.join(L, "plate-scene.png")
    p2 = os.path.join(L, "plate-lamp.png")
    for p in (p1, p2, REAL):
        if not os.path.exists(p):
            sys.exit(f"missing plate: {p}")
    scene = Image.open(p1).convert("RGB")
    lamp = Image.open(p2).convert("RGB")
    real = Image.open(REAL).convert("RGB")
    os.makedirs(B, exist_ok=True); os.makedirs(OUT, exist_ok=True)

    for i in range(TOTAL):
        if i <= A_END:                                   # A — wide, stillness then onset
            t = 0.0 if i < ONSET else ease((i - ONSET) / (A_END - ONSET))
            f = camera(scene, lerp(SCENE_WIDE, SCENE_WIDE2, t))
            f = warm(f, t)
        elif i <= B_END:                                 # B — cut to her face, same plate
            t = ease((i - A_END - 1) / max(1, B_END - A_END - 1))
            f = warm(camera(scene, lerp(FACE, FACE2, t)), 0.45)
        elif i <= C_END:                                 # C — painted lamp, STATIC
            # deliberately locked off: a static outgoing frame makes the match cut land,
            # and gives the incoming real photo a still baseline to move against
            f = camera_rect(lamp, LAMP_PAINT_R)
        else:                                            # D — MATCH CUT to the real thing
            k = i - C_END - 1
            HOLD = 6                                     # hold the matched frame, THEN move
            t = 0.0 if k < HOLD else ease((k - HOLD) / max(1, TOTAL - C_END - 2 - HOLD))
            f = titles(camera_rect(real, lerp(LAMP_REAL_R, LAMP_REAL_R2, t)), t)
        f.save(os.path.join(B, f"f{i:03d}.png"))

    mp4 = os.path.join(OUT, "cartoon-poc-3s.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
                    "-i", os.path.join(B, "f%03d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", mp4], check=True)
    print("wrote", mp4)


if __name__ == "__main__":
    main()
