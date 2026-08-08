#!/usr/bin/env python3
"""Burned caption overlays (720x1280 RGBA, transparent). Auto-shrinks so no line
ever overflows the frame. Edit the CAPTIONS table below; build.sh references caps by id.
Styles: 'bold' (hooks), 'italic' (dialogue/VO), 'reg'. y_center 0.5 = note/insert style."""
from PIL import Image, ImageFont, ImageDraw
import os
W, H = 720, 1280
SERIF   = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SERIF_I = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
SERIF_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
FONTS = {"reg": SERIF, "italic": SERIF_I, "bold": SERIF_B}

# ---- EDIT THIS TABLE PER FILM ----  id: (lines[], style, size, y_center)
CAPTIONS = {
    "c1":  (["Your hook line here,", "wrapped to two lines."], "bold",   46, 0.82),
    "c2":  (["“A line of dialogue.”"],                 "italic", 44, 0.82),
    # add c3, c4, ... to match your scenes
}
# ----------------------------------

def make(name, lines, style, size, y_center):
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build/caps")
    os.makedirs(outdir, exist_ok=True)
    img = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(img)
    MARGIN = 64
    while size > 26:
        font = ImageFont.truetype(FONTS[style], size)
        if max(d.textbbox((0,0), ln, font=font)[2] for ln in lines) <= W - 2*MARGIN: break
        size -= 2
    font = ImageFont.truetype(FONTS[style], size)
    line_h = size + 16; y0 = int(H*y_center - line_h*len(lines)/2)
    # feathered dark band for legibility
    band = Image.new("RGBA",(W,H),(0,0,0,0)); bd = ImageDraw.Draw(band)
    top, bot = y0-30, y0+line_h*len(lines)+30
    for yy in range(max(0,top), min(H,bot)):
        a = int(150*min(1.0, min(yy-top, bot-yy)/40.0)); bd.line([(0,yy),(W,yy)], fill=(0,0,0,a))
    img = Image.alpha_composite(img, band); d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        tw = d.textbbox((0,0), ln, font=font)[2]; x=(W-tw)//2; y=y0+i*line_h
        d.text((x+2,y+2), ln, font=font, fill=(0,0,0,220)); d.text((x,y), ln, font=font, fill=(255,255,255,255))
    img.save(os.path.join(outdir, name+".png"))

if __name__ == "__main__":
    for cid, spec in CAPTIONS.items(): make(cid, *spec)
    print("captions built:", ", ".join(CAPTIONS))
