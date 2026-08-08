#!/usr/bin/env python3
"""Real, sharp text-prop inserts (720x1280): a handwritten NOTE + a titled NOTEBOOK page.
AI garbles printed text, so these are composited real. Edit the tables below.
NOTEBOOK names MUST match the real product's names exactly (match-cut)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random
random.seed(7)
W, H = 720, 1280
SNELL = "/System/Library/Fonts/Supplemental/SnellRoundhand.ttc"   # grandma's cursive (note)
NOTE_F= "/System/Library/Fonts/Supplemental/Noteworthy.ttc"        # handwritten (notebook)

# ---- EDIT PER FILM ----
NOTE_LINES = ["If I forget the garden…", "remind me who grew there."]
NOTEBOOK_TITLE = "Grandma's Garden"
NOTEBOOK_ITEMS = [  # (name, flower, petal-color) — MUST match the real product
    ("Sophia","Cosmos",(224,120,150)), ("Donna","Aster",(150,110,200)),
    ("Sharon","Rose",(200,80,90)),     ("Helen","Marigold",(230,150,50)),
    ("Sarah","Poppy",(200,60,60)),
]
# -----------------------

def paper(w,h,col=(238,230,212)):
    img=Image.new("RGB",(w,h),col); px=img.load()
    for _ in range(int(w*h*0.04)):
        x=random.randint(0,w-1); y=random.randint(0,h-1); dd=random.randint(-10,8)
        px[x,y]=tuple(max(0,min(255,c+dd)) for c in px[x,y])
    return img.filter(ImageFilter.SMOOTH)

def flower(dr,cx,cy,r,petal):
    for a in range(0,360,45):
        x=cx+math.cos(math.radians(a))*r; y=cy+math.sin(math.radians(a))*r
        dr.ellipse([x-r*.55,y-r*.55,x+r*.55,y+r*.55],fill=petal)
    dr.ellipse([cx-r*.5,cy-r*.5,cx+r*.5,cy+r*.5],fill=(120,80,30))

def build():
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"build/props"); os.makedirs(out,exist_ok=True)
    # NOTE
    bg=Image.new("RGB",(W,H),(18,14,10)); card=paper(600,380); cd=ImageDraw.Draw(card)
    f=ImageFont.truetype(SNELL,52,index=0); y=100
    for ln in NOTE_LINES:
        tw=cd.textbbox((0,0),ln,font=f)[2]; cd.text(((600-tw)//2,y),ln,font=f,fill=(46,34,22)); y+=120
    card=card.rotate(-3,expand=True,fillcolor=(18,14,10))
    bg.paste(card,((W-card.size[0])//2,(H-card.size[1])//2)); bg.save(os.path.join(out,"note.png"))
    # NOTEBOOK
    bg2=Image.new("RGB",(W,H),(12,12,16)); page=paper(600,760,(236,228,208)); pd=ImageDraw.Draw(page)
    for yy in range(200,720,88): pd.line([(60,yy),(540,yy)],fill=(200,190,168),width=2)
    ft=ImageFont.truetype(NOTE_F,60,index=0); fi=ImageFont.truetype(NOTE_F,44,index=0)
    tw=pd.textbbox((0,0),NOTEBOOK_TITLE,font=ft)[2]; pd.text(((600-tw)//2,60),NOTEBOOK_TITLE,font=ft,fill=(60,44,28))
    pd.line([(150,138),(450,138)],fill=(150,110,70),width=3); y=180
    for name,fl,col in NOTEBOOK_ITEMS:
        flower(pd,95,y+30,19,col); pd.text((140,y),f"{name} — {fl}",font=fi,fill=(50,38,26)); y+=78
    page=page.rotate(1.5,expand=True,fillcolor=(12,12,16))
    bg2.paste(page,((W-page.size[0])//2,(H-page.size[1])//2)); bg2.save(os.path.join(out,"notebook.png"))
    print("props built: note.png, notebook.png")

if __name__ == "__main__": build()
