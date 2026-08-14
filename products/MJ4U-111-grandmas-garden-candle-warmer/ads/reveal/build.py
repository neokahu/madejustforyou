#!/usr/bin/env python3
"""
Product-reveal creative builder for MJ4U-111 (Grandma's Garden candle warmer).
Copies the proven Macorner winner: product-as-hero, personalization roster visible
in the first second, warm emotional caption, no discount. Static hero + 6-slide carousel.
All 4:5 (1080x1350), mobile-first. Composed from the real Shopify product photos.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "src")
OUT  = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
MARGIN = 96

# ---- palette (warm, premium, botanical) ----
CREAM_TOP = (247, 238, 226)
CREAM_BOT = (236, 216, 190)
INK       = (46, 41, 34)
GREEN     = (59, 82, 54)
TERRA     = (176, 92, 66)
SOFT      = (120, 108, 94)
WHITE     = (255, 255, 255)

# ---- fonts ----
def _scan_ttc(path, want, size):
    for i in range(0, 24):
        try:
            f = ImageFont.truetype(path, size, index=i)
            if want.lower() in " ".join(f.getname()).lower():
                return f
        except Exception:
            break
    raise RuntimeError(f"{want} not found in {path}")

DIDOT   = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Didot.ttc", s, index=0)
GEO_B   = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", s)
GEO_R   = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", s)
GEO_I   = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", s)
SAVOYE  = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Savoye LET.ttc", s, index=0)
AV_BOLD = lambda s: _scan_ttc("/System/Library/Fonts/Avenir Next.ttc", "Bold", s)
AV_MED  = lambda s: _scan_ttc("/System/Library/Fonts/Avenir Next.ttc", "Medium", s)
AV_DEMI = lambda s: _scan_ttc("/System/Library/Fonts/Avenir Next.ttc", "Demi Bold", s)
AV_REG  = lambda s: _scan_ttc("/System/Library/Fonts/Avenir Next.ttc", "Regular", s)

# ---- helpers ----
def warm_bg(glow=True):
    bg = Image.new("RGB", (W, H))
    px = bg.load()
    for y in range(H):
        t = y / H
        r = int(CREAM_TOP[0] + (CREAM_BOT[0]-CREAM_TOP[0])*t)
        g = int(CREAM_TOP[1] + (CREAM_BOT[1]-CREAM_TOP[1])*t)
        b = int(CREAM_TOP[2] + (CREAM_BOT[2]-CREAM_TOP[2])*t)
        for x in range(W):
            px[x, y] = (r, g, b)
    if glow:
        gl = Image.new("L", (W, H), 0)
        gd = ImageDraw.Draw(gl)
        gd.ellipse([W*0.12, H*0.20, W*0.88, H*0.78], fill=90)
        gl = gl.filter(ImageFilter.GaussianBlur(160))
        warm = Image.new("RGB", (W, H), (255, 238, 205))
        bg = Image.composite(warm, bg, gl)
    return bg

def letterspace(draw, xy, text, font, fill, ls, anchor_center=True):
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + ls*(len(text)-1)
    x = xy[0]-total/2 if anchor_center else xy[0]
    y = xy[1]
    for c, w in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += w + ls
    return total

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur+" "+w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_center_block(draw, cx, top, lines, font, fill, lh, shadow=None):
    y = top
    for ln in lines:
        w = draw.textlength(ln, font=font)
        if shadow:
            draw.text((cx-w/2+shadow[0], y+shadow[1]), ln, font=font, fill=shadow[2])
        draw.text((cx-w/2, y), ln, font=font, fill=fill)
        y += lh
    return y

def rounded_card(canvas, img, box, radius=48, pad=0, shadow=True):
    """place img (fit) inside a rounded white card at box=(x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    bw, bh = x1-x0, y1-y0
    if shadow:
        sh = Image.new("RGBA", (W, H), (0,0,0,0))
        sd = ImageDraw.Draw(sh)
        sd.rounded_rectangle([x0, y0+14, x1, y1+14], radius, fill=(60,40,25,90))
        sh = sh.filter(ImageFilter.GaussianBlur(30))
        canvas.paste(Image.new("RGB",(W,H),(0,0,0)), (0,0), sh)  # noop guard
        canvas.alpha_composite(sh) if canvas.mode=="RGBA" else canvas.paste(sh, (0,0), sh)
    card = Image.new("RGB", (bw, bh), WHITE)
    fitted = ImageOps.contain(img, (bw-2*pad, bh-2*pad))
    card.paste(fitted, ((bw-fitted.width)//2, (bh-fitted.height)//2))
    mask = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,bw,bh], radius, fill=255)
    canvas.paste(card, (x0, y0), mask)

def fullbleed_cover(base_img):
    return ImageOps.fit(base_img, (W, H), method=Image.LANCZOS, centering=(0.5,0.5))

def scrim(canvas, where="bottom", strength=170, frac=0.5):
    ov = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(ov)
    if where == "bottom":
        for y in range(H):
            t = max(0, (y - H*(1-frac))/(H*frac))
            d.line([(0,y),(W,y)], fill=int(strength*t))
    else:
        for y in range(H):
            t = max(0, (H*frac - y)/(H*frac))
            d.line([(0,y),(W,y)], fill=int(strength*t))
    dark = Image.new("RGB", (W, H), (30, 22, 14))
    canvas.paste(dark, (0,0), ov)

def eyebrow(draw, cx, y, text, color=TERRA, size=30):
    letterspace(draw, (cx, y), text, AV_DEMI(size), color, 7)

def draw_arrow(d, x, cy, size, color, width=7):
    """vector right-arrow; returns right edge x."""
    d.line([(x, cy), (x+size, cy)], fill=color, width=width)
    hs = size*0.5
    d.polygon([(x+size-2, cy-hs), (x+size+hs, cy), (x+size-2, cy+hs)], fill=color)
    return x+size+hs

def save(canvas, name):
    p = os.path.join(OUT, name)
    canvas.convert("RGB").save(p, quality=92)
    print("wrote", p)

def load(n):
    return Image.open(os.path.join(SRC, f"{n}.jpg")).convert("RGB")

# ============================================================= SLIDES

def slide_hook(fname, swipe=False):
    c = warm_bg().convert("RGB")
    d = ImageDraw.Draw(c)
    cx = W//2
    eyebrow(d, cx, 120, "PERSONALIZED CANDLE WARMER")
    head = wrap(d, "One flower for every grandchild she's raised", GEO_B(66), W-2*MARGIN)
    y = draw_center_block(d, cx, 168, head, GEO_B(66), INK, 82)
    # product card (image 01: lamp with names Alice/Grace/Jade)
    lamp = load("01")
    rounded_card(c, lamp, (150, y+26, W-150, y+26+760), radius=54)
    yb = y+26+760
    # caption band
    cap = "Her whole garden — lit with a warm, living glow."
    d.text((cx - d.textlength(cap, font=GEO_I(38))/2, yb+30), cap, font=GEO_I(38), fill=SOFT)
    letterspace(d, (cx, yb+92), "GRANDMA'S GARDEN  ·  madejustforyou.net", AV_MED(26), GREEN, 3)
    if swipe:
        by = H-92
        d.rounded_rectangle([W-322, by, W-96, by+52], 26, fill=TERRA)
        letterspace(d, (W-238, by+13, ), "SWIPE", AV_DEMI(26), WHITE, 3)
        draw_arrow(d, W-168, by+26, 26, WHITE, width=5)
    save(c, fname)

def slide_meaning(fname):
    c = warm_bg().convert("RGB")
    d = ImageDraw.Draw(c)
    cx = W//2
    eyebrow(d, cx, 120, "WHAT MAKES IT HERS")
    # script title
    st = "Love Grows Here"
    d.text((cx - d.textlength(st, font=SAVOYE(150))/2, 150), st, font=SAVOYE(150), fill=GREEN)
    # tight crop of the printed shade from image 01
    lamp = load("01")
    crop = lamp.crop((360, 470, 1150, 1120))  # shade w/ names region
    rounded_card(c, crop, (150, 360, W-150, 360+560), radius=54)
    yb = 360+560
    lines = wrap(d, "Each birth-month flower is one of her grandchildren — Alice, Grace, Jade — planted together in one little garden.", GEO_R(40), W-2*MARGIN-40)
    draw_center_block(d, cx, yb+40, lines, GEO_R(40), INK, 54)
    save(c, fname)

def slide_lifestyle(fname):
    base = load("05")  # bedside infographic; crop to the clean glowing lamp+candle (no baked text/badge)
    crop = base.crop((1055, 470, 2048, 1620))
    c = ImageOps.fit(crop, (W, H), method=Image.LANCZOS, centering=(0.5, 0.5))
    scrim(c, "bottom", strength=200, frac=0.55)
    d = ImageDraw.Draw(c)
    cx = W//2
    lines = wrap(d, "A soft glow that fills her room every evening", GEO_B(60), W-2*MARGIN)
    y = H - 300 - (len(lines)-1)*74
    draw_center_block(d, cx, y, lines, GEO_B(60), WHITE, 74, shadow=(2,2,(0,0,0)))
    sub = "no flame, no smoke — just warm light and the people she loves"
    for ln in wrap(d, sub, GEO_I(36), W-2*MARGIN):
        d.text((cx - d.textlength(ln, font=GEO_I(36))/2, y+ (len(lines))*74 + 8), ln, font=GEO_I(36), fill=(240,232,222))
        y += 46
    save(c, fname)

def slide_personalize(fname):
    c = warm_bg().convert("RGB")
    d = ImageDraw.Draw(c)
    cx = W//2
    eyebrow(d, cx, 120, "MADE FOR HER FAMILY")
    head = wrap(d, "Add every name. Watch her garden grow.", GEO_B(64), W-2*MARGIN)
    y = draw_center_block(d, cx, 168, head, GEO_B(64), INK, 80)
    lamp = load("01")
    rounded_card(c, lamp, (170, y+24, W-170, y+24+700), radius=54)
    yb = y+24+700
    steps = ["1 — Pick her flowers by each grandchild's birth month",
             "2 — Type their names",
             "3 — We print & ship her one-of-a-kind lamp"]
    yy = yb+34
    for s in steps:
        d.text((cx - d.textlength(s, font=AV_MED(34))/2, yy), s, font=AV_MED(34), fill=INK)
        yy += 52
    save(c, fname)

def slide_utility(fname):
    c = warm_bg().convert("RGB")
    d = ImageDraw.Draw(c)
    cx = W//2
    eyebrow(d, cx, 120, "A REAL LAMP, NOT JUST A GIFT")
    head = wrap(d, "Beautiful by day. Glowing by night.", GEO_B(64), W-2*MARGIN)
    y = draw_center_block(d, cx, 168, head, GEO_B(64), INK, 80)
    lamp = load("02")               # warm glowing lifestyle (left panel), no baked text
    crop = lamp.crop((200, 470, 980, 1250))   # square crop of the lit shade + glow, avoids detail-circle
    rounded_card(c, crop, (230, y+24, 850, y+24+620), radius=54)
    yb = y+24+620
    badges = ["Melts any candle gently from above — no tunnelling, no wasted wax",
              "Built-in dimmer & 2/4/8-hour timer",
              "No open flame, no smoke — safe to leave glowing"]
    yy = yb+34
    for b in badges:
        wrapped = wrap(d, b, AV_MED(32), W-2*MARGIN-40)
        for j, ln in enumerate(wrapped):
            txt = ("•  "+ln) if j==0 else ln
            d.text((cx - d.textlength(txt, font=AV_MED(32))/2, yy), txt, font=AV_MED(32), fill=INK)
            yy += 44
        yy += 10
    save(c, fname)

def slide_cta(fname):
    c = warm_bg().convert("RGB")
    d = ImageDraw.Draw(c)
    cx = W//2
    eyebrow(d, cx, 128, "GRANDMA'S GARDEN")
    st = "Love Grows Here"
    d.text((cx - d.textlength(st, font=SAVOYE(160))/2, 158), st, font=SAVOYE(160), fill=GREEN)
    lamp = load("02")  # warm lifestyle + detail composite
    rounded_card(c, lamp, (170, 380, W-170, 380+560), radius=54)
    yb = 380+560
    lines = wrap(d, "Give her a garden that never fades.", GEO_I(46), W-2*MARGIN)
    y = draw_center_block(d, cx, yb+36, lines, GEO_I(46), INK, 60)
    # CTA pill
    pill_w, pill_h = 620, 108
    px0 = cx-pill_w//2
    d.rounded_rectangle([px0, y+24, px0+pill_w, y+24+pill_h], 54, fill=TERRA)
    label = "Personalize hers"
    lw = d.textlength(label, font=AV_BOLD(44))
    arrow_sz, gap = 40, 26
    total = lw + gap + arrow_sz*1.5
    sx = cx - total/2
    cy = y+24+pill_h//2
    d.text((sx, cy-30), label, font=AV_BOLD(44), fill=WHITE)
    draw_arrow(d, sx+lw+gap, cy, arrow_sz, WHITE, width=7)
    letterspace(d, (cx, y+24+pill_h+26), "madejustforyou.net", AV_MED(30), GREEN, 4)
    save(c, fname)

if __name__ == "__main__":
    slide_hook("hero.jpg", swipe=False)
    slide_hook("slide-1.jpg", swipe=True)
    slide_meaning("slide-2.jpg")
    slide_lifestyle("slide-3.jpg")
    slide_personalize("slide-4.jpg")
    slide_utility("slide-5.jpg")
    slide_cta("slide-6.jpg")
    print("done")
