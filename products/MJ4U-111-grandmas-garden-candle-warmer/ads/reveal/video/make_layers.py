#!/usr/bin/env python3
"""Static visual layers for the seamless product-reveal video (9:16, 1080x1920).
Matches the static-carousel look (same palette/fonts). Outputs to ./layers/."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
LAY  = os.path.join(HERE, "layers"); os.makedirs(LAY, exist_ok=True)
KIT  = os.path.abspath(os.path.join(HERE, "..", "..", "film", "assets"))  # logo.png

W, H = 1080, 1920
CREAM_TOP=(247,238,226); CREAM_BOT=(233,212,183)
INK=(46,41,34); GREEN=(59,82,54); TERRA=(176,92,66); WHITE=(255,255,255)

def _scan(path, want, size):
    for i in range(0,24):
        try:
            f=ImageFont.truetype(path,size,index=i)
            if want.lower() in " ".join(f.getname()).lower(): return f
        except Exception: break
    raise RuntimeError(want)
GEO_B  = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", s)
GEO_I  = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", s)
SAVOYE = lambda s: ImageFont.truetype("/System/Library/Fonts/Supplemental/Savoye LET.ttc", s, index=0)
AV_BOLD= lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Bold",s)
AV_MED = lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Medium",s)
AV_DEMI= lambda s: _scan("/System/Library/Fonts/Avenir Next.ttc","Demi Bold",s)

def warm_canvas(glow=True):
    bg=Image.new("RGB",(W,H)); px=bg.load()
    for y in range(H):
        t=y/H
        px_row=(int(CREAM_TOP[0]+(CREAM_BOT[0]-CREAM_TOP[0])*t),
                int(CREAM_TOP[1]+(CREAM_BOT[1]-CREAM_TOP[1])*t),
                int(CREAM_TOP[2]+(CREAM_BOT[2]-CREAM_TOP[2])*t))
        for x in range(W): px[x,y]=px_row
    if glow:
        gl=Image.new("L",(W,H),0); gd=ImageDraw.Draw(gl)
        gd.ellipse([W*0.05,H*0.28,W*0.95,H*0.72],fill=70)
        gl=gl.filter(ImageFilter.GaussianBlur(180))
        bg=Image.composite(Image.new("RGB",(W,H),(255,240,212)),bg,gl)
    return bg

def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def center_block(d,cx,top,lines,font,fill,lh,shadow=True):
    y=top
    for ln in lines:
        w=d.textlength(ln,font=font)
        if shadow:
            d.text((cx-w/2+2,y+3),ln,font=font,fill=(0,0,0,150))
        d.text((cx-w/2,y),ln,font=font,fill=fill)
        y+=lh
    return y

def letterspace(d,cx,y,text,font,fill,ls):
    ws=[d.textlength(c,font=font) for c in text]; total=sum(ws)+ls*(len(text)-1)
    x=cx-total/2
    for c,w in zip(text,ws): d.text((x,y),c,font=font,fill=fill); x+=w+ls
    return total

def caption(fname, text, pos="bottom", eyebrow=None, script=None, italic_sub=None):
    """transparent 1080x1920 overlay: soft scrim + white caption."""
    img=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(img)
    band_h=int(H*0.42)
    scrim=Image.new("L",(W,H),0); sd=ImageDraw.Draw(scrim)
    if pos=="bottom":
        for y in range(H):
            t=max(0,(y-(H-band_h))/band_h); sd.line([(0,y),(W,y)],fill=int(150*t))
    else:
        for y in range(H):
            t=max(0,(band_h-y)/band_h); sd.line([(0,y),(W,y)],fill=int(150*t))
    img.paste(Image.new("RGBA",(W,H),(20,14,8,255)),(0,0),scrim)
    cx=W//2
    if pos=="bottom":
        lines=wrap(d,text,GEO_B(72),W-150)
        top=H-150-len(lines)*88
        if eyebrow: letterspace(d,cx,top-70,eyebrow,AV_DEMI(34),(255,225,190,255),8)
        y=center_block(d,cx,top,lines,GEO_B(72),(255,255,255,255),88)
        if italic_sub:
            for ln in wrap(d,italic_sub,GEO_I(40),W-160):
                w=d.textlength(ln,font=GEO_I(40)); d.text((cx-w/2,y+6),ln,font=GEO_I(40),fill=(240,232,222,255)); y+=52
    else:
        y=120
        if eyebrow: letterspace(d,cx,y,eyebrow,AV_DEMI(40),(255,225,190,255),10); y+=70
        if script:
            w=d.textlength(script,font=SAVOYE(180)); d.text((cx-w/2+2,y+3),script,font=SAVOYE(180),fill=(0,0,0,140)); d.text((cx-w/2,y),script,font=SAVOYE(180),fill=(255,255,255,255)); y+=180
        if text:
            for ln in wrap(d,text,GEO_I(44),W-160):
                w=d.textlength(ln,font=GEO_I(44)); d.text((cx-w/2,y),ln,font=GEO_I(44),fill=(245,238,228,255)); y+=58
    img.save(os.path.join(LAY,fname)); print("wrote",fname)

def orbit_mask():
    """1080x1080 feathered white — soft edges so the orbit blends into the warm canvas."""
    m=Image.new("L",(1080,1080),0); d=ImageDraw.Draw(m)
    d.rectangle([70,70,1010,1010],fill=255)
    m=m.filter(ImageFilter.GaussianBlur(60))
    m.save(os.path.join(LAY,"orbit_mask.png")); print("wrote orbit_mask.png")

def turntable_bg():
    c=warm_canvas(glow=True); c.save(os.path.join(LAY,"turntable_bg.jpg"),quality=92); print("wrote turntable_bg.jpg")

def endcard():
    c=warm_canvas(glow=True).convert("RGBA"); d=ImageDraw.Draw(c); cx=W//2
    # logo wordmark
    try:
        logo=Image.open(os.path.join(KIT,"logo.png")).convert("RGBA")
        lw=560; logo=logo.resize((lw,int(logo.height*lw/logo.width)))
        lx,ly=(W-lw)//2,300
        # soft dark shadow so the white wordmark reads on cream
        sh=Image.new("RGBA",(W,H),(0,0,0,0)); a=logo.split()[3]
        tint=Image.new("RGBA",logo.size,(40,28,16,180)); tint.putalpha(a)
        sh.alpha_composite(tint,(lx,ly)); sh=sh.filter(ImageFilter.GaussianBlur(7))
        c.alpha_composite(sh); c.alpha_composite(logo,(lx,ly))
    except Exception as e: print("logo skip",e)
    letterspace(d,cx,560,"GRANDMA'S GARDEN",AV_DEMI(40),TERRA,10)
    st="Love Grows Here"; w=d.textlength(st,font=SAVOYE(210)); d.text((cx-w/2,610),st,font=SAVOYE(210),fill=GREEN)
    for i,ln in enumerate(wrap(d,"Give her a garden that never fades.",GEO_I(52),W-200)):
        w=d.textlength(ln,font=GEO_I(52)); d.text((cx-w/2,920+i*66),ln,font=GEO_I(52),fill=INK)
    # pill
    pw,ph=680,132; px0=cx-pw//2; py=1120
    d.rounded_rectangle([px0,py,px0+pw,py+ph],66,fill=TERRA)
    label="Personalize hers"; lw2=d.textlength(label,font=AV_BOLD(52))
    asz=48; gap=30; total=lw2+gap+asz*1.5; sx=cx-total/2; cyy=py+ph//2
    d.text((sx,cyy-34),label,font=AV_BOLD(52),fill=WHITE)
    d.line([(sx+lw2+gap,cyy),(sx+lw2+gap+asz,cyy)],fill=WHITE,width=8)
    hs=asz*0.5; d.polygon([(sx+lw2+gap+asz-2,cyy-hs),(sx+lw2+gap+asz+hs,cyy),(sx+lw2+gap+asz-2,cyy+hs)],fill=WHITE)
    letterspace(d,cx,py+ph+40,"madejustforyou.net",AV_MED(38),GREEN,5)
    letterspace(d,cx,1420,"NO FLAME  ·  JUST SOFT LIGHT  ·  SHIPS WORLDWIDE",AV_DEMI(26),(120,108,94),4)
    c.convert("RGB").save(os.path.join(LAY,"endcard.jpg"),quality=93); print("wrote endcard.jpg")

if __name__=="__main__":
    turntable_bg(); orbit_mask()
    caption("cap1.png","One flower for every grandchild she's raised",pos="bottom",eyebrow="PERSONALIZED CANDLE WARMER")
    caption("cap2.png","",pos="top",eyebrow="GRANDMA'S GARDEN",script="Love Grows Here")
    caption("cap3.png","every light feels like love growing at home",pos="bottom",italic_sub=None)
    endcard()
    print("layers done")
