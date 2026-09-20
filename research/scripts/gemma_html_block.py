# -*- coding: utf-8 -*-
"""Viết lại tiếng Việt của trang HTML bằng Gemma, THEO TỪNG SECTION (có ngữ cảnh cả mục),
không phải từng chuỗi rời. Chỉ thay text node + data-tip; không đụng vào thẻ/CSS.
Dùng: python3 gemma_html_block.py <in.html> <out.html>"""
import re, json, os, html, sys, time, urllib.request

KEY=None
for line in open(os.path.expanduser('~/.global-keys.env'),encoding='utf-8'):
    if line.startswith('OPENROUTER_API_KEY'):
        KEY=line.split('=',1)[1].strip().strip('"').strip("'")

SRC,OUT=sys.argv[1],sys.argv[2]
s=open(SRC,encoding='utf-8').read()
head,body=s.split('</style>',1)

KEEP=("hook, hook rate, hold rate, concept, angle, offer, CTA, CTR, link CTR, CPM, CPA, ROAS, "
      "add-to-cart, ATC, landing page, LPV, retarget, scale, creative, ads, ad set, tệp, learning, "
      "Phase, proof, pacing, voice, cut rate, length, structure, POV, UGC, BTS, PAS, Meta, "
      "Shop Now, Order Now, suncatcher, fleece blanket, fridge magnet, trust, checkout, upsell, "
      "abandoned-cart recovery, benchmark, reveal, close-up")
SYS=("Bạn là biên tập viên tiếng Việt cho dân chạy quảng cáo Facebook/POD. Bạn nhận TOÀN BỘ các chuỗi "
     "chữ của MỘT MỤC trong trang, theo đúng thứ tự xuất hiện. Đọc hết cả mục để hiểu mạch, rồi viết "
     "lại từng chuỗi cho tự nhiên, gọn, đúng giọng người trong nghề — các chuỗi phải ăn khớp với nhau "
     "như một mục hoàn chỉnh, không rời rạc.\n"
     "QUY TẮC CỨNG:\n"
     "1. GIỮ NGUYÊN tiếng Anh: "+KEEP+"\n"
     "2. GIỮ NGUYÊN 100% câu thoại / chữ in trên sản phẩm đang trong dấu ngoặc kép tiếng Anh — "
     "quảng cáo chạy cho người mua Mỹ.\n"
     "3. KHÔNG đổi số, %, $, khoảng thời gian (0–2s), mũi tên →, dấu ·, ≥, <.\n"
     "4. KHÔNG thêm/bớt phần tử. Mảng trả về phải ĐÚNG SỐ LƯỢNG như mảng nhận vào.\n"
     "5. Chuỗi nào đã ổn hoặc chỉ là ký hiệu/số thì trả lại y nguyên.\n"
     "6. Văn phong tài liệu: không 'ạ', 'nhé', 'nha'. Không gọi người đọc là 'cháu'.\n"
     "7. Không dùng 'nó' cho người hoặc thú cưng — dùng tên hoặc vai (bà, cháu, người chủ).\n"
     "Trả về DUY NHẤT một mảng JSON các chuỗi, đúng thứ tự, đúng số lượng.")

def call(items,ctx,full=None):
    u="Mục: "+ctx+"\n\n"
    if full:
        u+=("Toàn văn của mục này (để bạn nắm mạch, KHÔNG dịch phần này):\n"
            +json.dumps(full,ensure_ascii=False,indent=1)+"\n\n")
    u+="Các chuỗi CẦN viết lại (chỉ trả về đúng %d phần tử này):\n"%len(items)
    u+=json.dumps(items,ensure_ascii=False,indent=1)
    req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps({"model":"google/gemma-3-27b-it","temperature":0.25,
          "messages":[{"role":"system","content":SYS},{"role":"user","content":u}]}).encode(),
        headers={'Authorization':'Bearer '+KEY,'Content-Type':'application/json'})
    r=json.loads(urllib.request.urlopen(req,timeout=300).read())
    c=r['choices'][0]['message']['content'].strip()
    return json.loads(re.sub(r'^```(?:json)?|```$','',c,flags=re.M).strip())

# ---- cắt body thành từng section ----
spans=[m.span() for m in re.finditer(r'<section\b.*?</section>',body,re.S)]
if not spans: sys.exit('không thấy <section>')
print('có %d section'%len(spans))

edits=[]   # (start,end,newtext) trên toạ độ body
fails=[]
for si,(a,z) in enumerate(spans,1):
    chunk=body[a:z]
    h=re.search(r'<h2[^>]*>(.*?)</h2>',chunk,re.S)
    ctx=re.sub(r'<[^>]+>','',h.group(1)).strip() if h else 'mục %d'%si
    segs=[]
    for m in re.finditer(r'>([^<>]+)<',chunk):
        t=m.group(1)
        if t.strip() and re.search(r'[a-zA-ZÀ-ỹ]',t): segs.append(('txt',m.span(1),t))
    for m in re.finditer(r'data-tip="([^"]+)"',chunk):
        segs.append(('tip',m.span(1),m.group(1)))
    if not segs: continue
    src=[html.unescape(t) for _,_,t in segs]
    # section to thì chia nhỏ mảng, NHƯNG vẫn đưa toàn văn cả mục làm ngữ cảnh
    CH=25
    chunks=[(0,src)] if len(src)<=CH else [(i,src[i:i+CH]) for i in range(0,len(src),CH)]
    full=src if len(chunks)>1 else None
    got=[]; bad=0
    for off,part in chunks:
        r2=None
        for att in range(4):
            try:
                r=call(part,ctx,full)
                if isinstance(r,list) and len(r)==len(part) and all(isinstance(x,str) for x in r):
                    r2=r; break
            except Exception as e: print('  lỗi',str(e)[:60],flush=True)
            time.sleep(1.5*(att+1))
        if r2 is None: r2=part; bad+=len(part)
        got+=r2
    if bad: fails.append('%s (%d chuỗi)'%(ctx,bad))
    ch=sum(1 for x,y in zip(src,got) if x!=y)
    print('section %d/%d [%s] đổi %d/%d chuỗi%s'%(si,len(spans),ctx,ch,len(src),
          '  ⚠️ %d chuỗi giữ nguyên'%bad if bad else ''),flush=True)
    for (kind,(ra,rz),orig),tr in zip(segs,got):
        # giữ đúng khoảng trắng đầu/cuối của text node gốc — Gemma hay ăn mất,
        # làm dính chữ vào thẻ kế bên ("Nguồn:<a>", "mục tiêu.Cùng")
        lead=orig[:len(orig)-len(orig.lstrip())]
        trail=orig[len(orig.rstrip()):]
        esc=lead+html.escape(tr.strip(),quote=(kind=='tip'))+trail
        if esc!=orig: edits.append((a+ra,a+rz,esc))

new=body
for ra,rz,tx in sorted(edits,key=lambda e:-e[0]): new=new[:ra]+tx+new[rz:]
open(OUT,'w',encoding='utf-8').write(head+'</style>'+new)
print('\nGHI -> %s  (%d chuỗi đổi)'%(OUT,len(edits)))
print('THẤT BẠI: '+(', '.join(fails) if fails else 'không có'))
