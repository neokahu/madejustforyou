#!/usr/bin/env python3
"""Branded end card (720x1280): headline + brand logo lockup + product line + url,
over a blurred/darkened still. Brand palette per library/brand/design-system.
Put the logo at assets/logo.png (from library/brand/logo/lockup-horizontal.png)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
base = os.path.dirname(os.path.abspath(__file__))
W, H = 720, 1280
SERIF, SERIF_I, SERIF_B = (f"/System/Library/Fonts/Supplemental/Georgia{s}.ttf" for s in ["", " Italic", " Bold"])
CLAY, HONEY, CREAM = (193,95,60), (212,175,120), (255,244,230)

# ---- EDIT PER FILM ----
BG_STILL   = "build/endcard-bg.png"           # a warm frame from the hero shot (ffmpeg-extracted)
HEADLINE   = ["Her garden.", "Her people. Her light."]  # italic
PRODUCT    = "Personalized Grandma's Garden Candle Warmer"
URL        = "madejustforyou.net"
LOGO       = "assets/logo.png"
# -----------------------

def center(d, W, t, f, y, fill=CREAM):
    tw=d.textbbox((0,0),t,font=f)[2]; x=(W-tw)//2
    d.text((x+2,y+2),t,font=f,fill=(0,0,0)); d.text((x,y),t,font=f,fill=fill)

def build():
    p=os.path.join(base,BG_STILL)
    bg=Image.open(p).convert("RGB") if os.path.exists(p) else Image.new("RGB",(W,H),(26,21,18))
    bg=bg.resize((W,H)).filter(ImageFilter.GaussianBlur(16))
    bg=Image.blend(bg,Image.new("RGB",(W,H),(0,0,0)),0.55); d=ImageDraw.Draw(bg)
    fi=ImageFont.truetype(SERIF_I,58); y=int(H*0.30)
    for ln in HEADLINE: center(d,W,ln,fi,y,CREAM); y+=72
    d.line([(W*0.30,H*0.47),(W*0.70,H*0.47)],fill=HONEY,width=2)
    lp=os.path.join(base,LOGO)
    if os.path.exists(lp):
        logo=Image.open(lp).convert("RGBA"); lw=460; lh=int(logo.height*lw/logo.width); logo=logo.resize((lw,lh))
        bg=bg.convert("RGBA"); bg.alpha_composite(logo,((W-lw)//2,int(H*0.52))); bg=bg.convert("RGB"); d=ImageDraw.Draw(bg)
    center(d,W,PRODUCT,ImageFont.truetype(SERIF,30),int(H*0.63),(226,214,198))
    center(d,W,URL,ImageFont.truetype(SERIF,30),int(H*0.70),HONEY)
    out=os.path.join(base,"build/endcard.png"); os.makedirs(os.path.dirname(out),exist_ok=True); bg.save(out); print("endcard built")

if __name__ == "__main__": build()
