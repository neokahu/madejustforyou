# -*- coding: utf-8 -*-
"""Dịch Markdown EN->VI bằng Gemma theo KHỐI (đoạn/bảng/list), không theo dòng.
Mỗi khối gửi nguyên vẹn + kèm heading của mục đang đứng, để model có đủ ngữ cảnh.
Dùng: python3 gemma_block.py <en.md> <vi.md>"""
import re, json, os, sys, time, urllib.request

KEY=None
for line in open(os.path.expanduser('~/.global-keys.env'),encoding='utf-8'):
    if line.startswith('OPENROUTER_API_KEY'):
        KEY=line.split('=',1)[1].strip().strip('"').strip("'")

SRC,OUT=sys.argv[1],sys.argv[2]
lines=open(SRC,encoding='utf-8').read().split('\n')

KEEP=("hook, hook rate, hold rate, concept, angle, offer, CTA, CTR, link CTR, CPM, CPC, CPA, ROAS, "
      "add-to-cart, ATC, landing page, LPV, retarget, scale, creative, ads, ad set, learning, Phase, "
      "proof, pacing, voice, cut rate, length, structure, POV, UGC, BTS, PAS, AIDA, Meta, Reels, "
      "Stories, Shop Now, Order Now, suncatcher, fleece blanket, fridge magnet, POD, Etsy, TikTok, "
      "Andromeda, OFAT, ThruPlay, Advantage+, EMQ, power, A/B test, reveal, reaction, unboxing")
GLOS=("HIGH, MEDIUM-HIGH, MEDIUM, MED-LOW, LOW, SKIP, EXACT, NEAR-EXACT, WIDER, LAST-RESORT, "
      "[DATA], [OPINION]")
SYS=("Bạn là biên tập viên tiếng Việt cho dân chạy quảng cáo Facebook/POD. Bạn nhận MỘT KHỐI Markdown "
     "tiếng Anh (một đoạn văn, một bảng, hoặc một list) và dịch TRỌN KHỐI sang tiếng Việt.\n"
     "Vì nhận cả khối nên hãy dịch theo NGHĨA CẢ ĐOẠN, câu văn phải trôi chảy và nối mạch với nhau — "
     "đừng dịch từng dòng rời rạc.\n"
     "QUY TẮC CỨNG:\n"
     "1. GIỮ NGUYÊN tiếng Anh các thuật ngữ: "+KEEP+"\n"
     "2. GIỮ NGUYÊN, KHÔNG DỊCH các nhãn phân loại: "+GLOS+"\n"
     "3. GIỮ NGUYÊN 100% câu thoại / chữ in trên sản phẩm đang nằm trong dấu ngoặc kép.\n"
     "4. GIỮ NGUYÊN cú pháp Markdown: #, |, -, >, **, `, link, số, %, $, ·, →, ⚠️, emoji, ⭐, ①②③.\n"
     "5. Nếu khối là BẢNG: giữ đúng số dòng và đúng số cột mỗi dòng. Dòng phân cách |---| giữ nguyên.\n"
     "6. Nếu khối là LIST: giữ đúng số gạch đầu dòng.\n"
     "7. Văn phong tài liệu nghiên cứu: không dùng 'ạ', 'nhé', 'nha'. Không gọi người đọc là 'cháu'.\n"
     "8. Không dùng 'nó' cho người hoặc thú cưng.\n"
     "Trả về DUY NHẤT khối Markdown đã dịch. Không thêm lời dẫn, không bọc ```.")

def call(block, ctx):
    u=(("Mục đang đứng: "+ctx+"\n\n") if ctx else "")+"Khối cần dịch:\n\n"+block
    req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps({"model":"google/gemma-3-27b-it","temperature":0.25,
          "messages":[{"role":"system","content":SYS},{"role":"user","content":u}]}).encode(),
        headers={'Authorization':'Bearer '+KEY,'Content-Type':'application/json'})
    r=json.loads(urllib.request.urlopen(req,timeout=300).read())
    c=r['choices'][0]['message']['content'].strip()
    return re.sub(r'^```(?:markdown|md)?\n?|\n?```$','',c,flags=re.M).strip('\n')

# ---- gom dòng thành khối ----
def kind(l):
    s=l.strip()
    if not s: return 'blank'
    if s.startswith('|'): return 'table'
    if s.startswith('#'): return 'head'
    if re.match(r'^(-|\*|\d+\.)\s', s): return 'list'
    return 'para'

blocks=[]; cur=[]; ck=None
for l in lines:
    k=kind(l)
    # đoạn văn xuống dòng giữa chừng vẫn thuộc cùng khối; list/para nối tiếp nhau thì tách
    if ck and k==ck and k!='head': cur.append(l)
    elif ck=='list' and k=='para' and l.startswith(('  ','\t')): cur.append(l)
    elif ck=='para' and k=='para': cur.append(l)
    else:
        if cur: blocks.append((ck,cur))
        cur=[l]; ck=k
if cur: blocks.append((ck,cur))

def cols(l): return l.count('|')
def ok(kd, src, got):
    g=got.split('\n'); s=src.split('\n')
    if not got.strip(): return False
    if kd=='table':
        if len(g)!=len(s): return False
        return all(cols(a)==cols(b) for a,b in zip(s,g))
    if kd=='list':
        f=lambda x:len([1 for i in x if re.match(r'^\s*(-|\*|\d+\.)\s',i)])
        return f(g)==f(s)
    if kd=='head': return len(g)==1 and g[0].startswith('#')
    return True

out=[]; ctx=''; fails=[]; done=0
total=sum(1 for k,_ in blocks if k not in ('blank',))
for kd,ls in blocks:
    src='\n'.join(ls)
    if kd=='blank': out.append(src); continue
    if kd=='head': ctx=src.strip('# ').strip()
    got=None
    for a in range(4):
        try:
            r=call(src,ctx)
            if ok(kd,src,r): got=r; break
        except Exception as e: print('  lỗi',str(e)[:60],flush=True)
        time.sleep(1.5*(a+1))
    if got is None:
        fails.append((kd,ls[0][:70])); got=src
    out.append(got); done+=1
    print('khối %d/%d [%s] %s'%(done,total,kd,'OK' if got!=src else 'GIỮ EN'),flush=True)

open(OUT,'w',encoding='utf-8').write('\n'.join(out))
print('\nGHI -> %s'%OUT)
if fails:
    print('THẤT BẠI %d khối (giữ nguyên tiếng Anh):'%len(fails))
    for k,p in fails: print('  [%s] %s'%(k,p))
else:
    print('Tất cả khối đều dịch được.')
