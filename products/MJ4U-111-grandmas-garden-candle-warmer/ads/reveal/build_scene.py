#!/usr/bin/env python3
"""In-scene product-reveal carousel (v2) for MJ4U-111.
LAYOUT RULE: photo on top (product + its printed text stay CLEAN, never covered),
all ad copy in a dedicated warm panel BELOW — so my text never fights the lamp's text.
4:5 (1080x1350). Re-run: python3 build_scene.py"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

HERE=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(HERE,"src")
OUT=os.path.join(HERE,"out_scene"); os.makedirs(OUT,exist_ok=True)
W,H=1080,1350
CREAM_TOP=(247,238,226); CREAM_BOT=(236,217,192)
INK=(46,41,34); GREEN=(59,82,54); TERRA=(176,92,66); SOFT=(120,108,94); WHITE=(255,255,255)

def _scan(p,w,s):
    for i in range(24):
        try:
            f=ImageFont.truetype(p,s,index=i)
            if w.lower() in " ".join(f.getname()).lower(): return f
        except: break
GEO_B=lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf",s)
GEO_I=lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf",s)
SAVOYE=lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Savoye LET.ttc",s,index=0)
AV_BOLD=lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Bold",s)
AV_MED=lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Medium",s)
AV_DEMI=lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Demi Bold",s)

def load(n): return Image.open(os.path.join(SRC,n)).convert("RGB")

def wrap(d,txt,f,mw):
    out=[];cur=""
    for w in txt.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)<=mw: cur=t
        else: out.append(cur);cur=w
    if cur:out.append(cur)
    return out

def ls(d,cx,y,txt,f,fill,sp):
    ws=[d.textlength(ch,font=f) for ch in txt]; tot=sum(ws)+sp*(len(txt)-1); x=cx-tot/2
    for ch,w in zip(txt,ws): d.text((x,y),ch,font=f,fill=fill); x+=w+sp
    return tot

def ctr(d,cx,y,lines,f,fill,lh):
    for ln in lines:
        w=d.textlength(ln,font=f); d.text((cx-w/2,y),ln,font=f,fill=fill); y+=lh
    return y

def arrow(d,x,cy,sz,col,wd=7):
    d.line([(x,cy),(x+sz,cy)],fill=col,width=wd); hs=sz*0.5
    d.polygon([(x+sz-2,cy-hs),(x+sz+hs,cy),(x+sz-2,cy+hs)],fill=col)

def base(img_name, panel_y, centering, crop=None):
    """photo in top area (0..panel_y), warm cream panel below. Returns (canvas,draw)."""
    im=load(img_name)
    if crop: im=im.crop(crop)
    photo=ImageOps.fit(im,(W,panel_y),Image.LANCZOS,centering=centering).convert("RGB")
    c=Image.new("RGB",(W,H),CREAM_TOP)
    # panel gradient
    px=c.load()
    for y in range(panel_y,H):
        t=(y-panel_y)/max(1,(H-panel_y))
        row=(int(CREAM_TOP[0]+(CREAM_BOT[0]-CREAM_TOP[0])*t),
             int(CREAM_TOP[1]+(CREAM_BOT[1]-CREAM_TOP[1])*t),
             int(CREAM_TOP[2]+(CREAM_BOT[2]-CREAM_TOP[2])*t))
        for x in range(W): px[x,y]=row
    c.paste(photo,(0,0))
    # soft shadow under the photo edge for separation
    sh=Image.new("RGBA",(W,60),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for i in range(60): sd.line([(0,i),(W,i)],fill=(30,20,10,int(70*(1-i/60))))
    c.paste(Image.new("RGB",(W,60),(30,20,10)),(0,panel_y),sh)
    return c, ImageDraw.Draw(c)

def save(c,n): c.save(os.path.join(OUT,n),quality=92); print("wrote",n)

# ---------------- slides ----------------
def hook(fname):
    PY=980
    c,d=base("scene-gift.jpg",PY,(0.5,0.34))
    mid=W//2
    ls(d,mid,PY+52,"PERSONALIZED CANDLE WARMER",AV_DEMI(28),TERRA,6)
    ctr(d,mid,PY+108,wrap(d,"One flower for every grandchild she's raised",GEO_B(52),W-150),GEO_B(52),INK,62)
    ls(d,mid,H-58,"GRANDMA'S GARDEN  ·  madejustforyou.net",AV_MED(24),GREEN,3)
    save(c,fname)

def meaning(fname):
    PY=980
    c,d=base("scene-gift.jpg",PY,(0.5,0.5),crop=(430,360,880,860))  # tight on the printed shade
    mid=W//2
    ls(d,mid,PY+56,"WHAT MAKES IT HERS",AV_DEMI(28),TERRA,6)
    ctr(d,mid,PY+112,wrap(d,"Each birth-flower is one of her grandchildren",GEO_B(48),W-150),GEO_B(48),INK,58)
    ctr(d,mid,PY+112+2*58+8,["planted together in one little garden."],GEO_I(34),SOFT,44)
    save(c,fname)

def lifestyle(fname):
    PY=980
    c,d=base("01-scene-flux.jpg",PY,(0.55,0.36))
    mid=W//2
    ls(d,mid,PY+58,"EVERY EVENING",AV_DEMI(28),TERRA,6)
    ctr(d,mid,PY+114,wrap(d,"A soft glow that fills her room",GEO_B(54),W-150),GEO_B(54),INK,64)
    save(c,fname)

def personalize(fname):
    PY=980
    c,d=base("scene-livingroom.jpg",PY,(0.5,0.34))
    mid=W//2
    ls(d,mid,PY+52,"MADE FOR HER FAMILY",AV_DEMI(28),TERRA,6)
    ctr(d,mid,PY+108,wrap(d,"Add every name. Watch her garden grow.",GEO_B(50),W-150),GEO_B(50),INK,60)
    ctr(d,mid,PY+108+2*60+6,["A name + birth-month flower for each grandchild."],AV_MED(28),SOFT,40)
    save(c,fname)

def byday(fname):
    PY=980
    c,d=base("scene-daytime.jpg",PY,(0.5,0.4))
    mid=W//2
    ls(d,mid,PY+52,"A REAL LAMP, NOT JUST A GIFT",AV_DEMI(26),TERRA,5)
    ctr(d,mid,PY+104,wrap(d,"Beautiful by day. Glowing by night.",GEO_B(50),W-150),GEO_B(50),INK,60)
    ctr(d,mid,PY+104+2*60+4,["No flame · built-in timer · melts any candle"],AV_MED(28),SOFT,40)
    save(c,fname)

def cta(fname):
    PY=900
    c,d=base("scene-gift.jpg",PY,(0.5,0.32))
    mid=W//2
    ls(d,mid,PY+46,"GRANDMA'S GARDEN",AV_DEMI(28),TERRA,7)
    st="Love Grows Here"; w=d.textlength(st,font=SAVOYE(120)); d.text((mid-w/2,PY+80),st,font=SAVOYE(120),fill=GREEN)
    # pill
    pw,ph=560,104; px0=mid-pw//2; py=PY+230
    d.rounded_rectangle([px0,py,px0+pw,py+ph],52,fill=TERRA)
    label="Personalize hers"; lw=d.textlength(label,font=AV_BOLD(42)); asz,gap=40,24
    tot=lw+gap+asz*1.5; sx=mid-tot/2; cyy=py+ph//2
    d.text((sx,cyy-28),label,font=AV_BOLD(42),fill=WHITE); arrow(d,sx+lw+gap,cyy,asz,WHITE,6)
    ls(d,mid,py+ph+26,"madejustforyou.net",AV_MED(28),GREEN,4)
    save(c,fname)

if __name__=="__main__":
    hook("slide-1.jpg"); meaning("slide-2.jpg"); lifestyle("slide-3.jpg")
    personalize("slide-4.jpg"); byday("slide-5.jpg"); cta("slide-6.jpg")
    hook("hero.jpg")
    print("scene carousel v2 (panel layout) done")
