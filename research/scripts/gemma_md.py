# -*- coding: utf-8 -*-
"""Dịch file Markdown tiếng Anh sang tiếng Việt bằng Gemma qua OpenRouter. Ghi ra file MỚI."""
import re, json, os, sys, urllib.request

KEY=None
for line in open(os.path.expanduser('~/.global-keys.env'),encoding='utf-8'):
    if line.startswith('OPENROUTER_API_KEY'):
        KEY=line.split('=',1)[1].strip().strip('"').strip("'")

SRC, OUT = sys.argv[1], sys.argv[2]
lines=open(SRC,encoding='utf-8').read().split('\n')

KEEP=("hook, hook rate, hold rate, concept, angle, offer, CTA, CTR, link CTR, CPM, CPC, CPA, ROAS, "
      "add-to-cart, ATC, landing page, LPV, retarget, scale, creative, ads, ad set, tệp, learning, "
      "Phase, proof, pacing, voice, length, structure, POV, UGC, BTS, PAS, AIDA, Meta, Reels, Stories, "
      "Shop Now, Order Now, suncatcher, fleece blanket, fridge magnet, POD, Etsy, TikTok, Andromeda, "
      "OFAT, ThruPlay, Advantage+, EMQ, power, A/B test")
SYS=("Bạn là biên tập viên tiếng Việt cho dân chạy quảng cáo Facebook/POD. Dịch từng dòng Markdown sang "
     "tiếng Việt tự nhiên, gọn, đúng giọng người trong nghề. QUY TẮC CỨNG:\n"
     "1. GIỮ NGUYÊN tiếng Anh các thuật ngữ: "+KEEP+"\n"
     "2. GIỮ NGUYÊN 100% mọi câu thoại/chữ in trên sản phẩm đang nằm trong dấu ngoặc kép — không dịch.\n"
     "3. GIỮ NGUYÊN cú pháp Markdown: #, |, -, >, **, `, [[...]], link, số, %, $, ·, →, ⚠️, emoji.\n"
     "4. Dòng nào là bảng (có |) thì giữ đúng số cột.\n"
     "5. Dòng trống hoặc dòng chỉ có ký hiệu thì trả lại y nguyên.\n"
     "6. Xưng hô lịch sự: cháu/bà/mẹ — tuyệt đối không dùng 'nó' cho người.\n"
     "Trả về DUY NHẤT một mảng JSON các dòng đã dịch, đúng thứ tự và đúng số lượng.")

def call(batch):
    req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps({"model":"google/gemma-3-27b-it","temperature":0.25,
          "messages":[{"role":"system","content":SYS},
                      {"role":"user","content":json.dumps(batch,ensure_ascii=False)}]}).encode(),
        headers={'Authorization':'Bearer '+KEY,'Content-Type':'application/json'})
    r=json.loads(urllib.request.urlopen(req,timeout=240).read())
    c=r['choices'][0]['message']['content'].strip()
    c=re.sub(r'^```(?:json)?|```$','',c,flags=re.M).strip()
    return json.loads(c)

out=[]; B=18
for i in range(0,len(lines),B):
    b=lines[i:i+B]
    if not any(x.strip() for x in b):
        out+=b; continue
    try:
        r=call(b)
        if not isinstance(r,list) or len(r)!=len(b): r=b
    except Exception as e:
        print('lỗi batch',i,str(e)[:70]); r=b
    out+=[x if isinstance(x,str) else b[j] for j,x in enumerate(r)]
    print('xong',min(i+B,len(lines)),'/',len(lines),flush=True)

open(OUT,'w',encoding='utf-8').write('\n'.join(out))
print('GHI ->',OUT)
