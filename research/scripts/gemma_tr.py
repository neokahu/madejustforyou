# -*- coding: utf-8 -*-
"""Dịch lại phần tiếng Việt của trang bằng Gemma qua OpenRouter. Ghi ra FILE MỚI."""
import re, json, os, html, urllib.request

KEY=None
for line in open(os.path.expanduser('~/.global-keys.env'),encoding='utf-8'):
    if line.startswith('OPENROUTER_API_KEY'):
        KEY=line.split('=',1)[1].strip().strip('"').strip("'")
SRC='public/index.html'; OUT='public/index-gemma.html'
s=open(SRC,encoding='utf-8').read()
body=s.split('</style>',1)[1]

# lấy các đoạn text giữa thẻ + nội dung data-tip
segs=[]; 
for m in re.finditer(r'>([^<>]+)<', body):
    t=m.group(1)
    if t.strip() and re.search(r'[a-zA-ZÀ-ỹ]', t): segs.append(('txt',m.span(1),t))
for m in re.finditer(r'data-tip="([^"]+)"', body):
    segs.append(('tip',m.span(1),m.group(1)))

KEEP=("hook, concept, offer, CTA, CTR, ROAS, CPA, CPC, add-to-cart, landing page, retarget, "
      "scale, creative, ads, tệp, learning, Phase, proof, pacing, voice, length, structure, "
      "POV, UGC, BTS, PAS, T1, T2, T3, Meta, Shop Now, suncatcher, fleece blanket, fridge magnet")
SYS=("Bạn là biên tập viên tiếng Việt cho dân chạy quảng cáo Facebook. Nhiệm vụ: viết lại từng chuỗi "
     "cho tự nhiên, gọn, đúng giọng dân trong nghề nói chuyện với nhau. KHÔNG dịch các thuật ngữ sau, "
     "giữ nguyên tiếng Anh: "+KEEP+". KHÔNG đụng vào câu thoại/chữ in trên sản phẩm đang để trong dấu "
     "ngoặc kép tiếng Anh — giữ nguyên 100%. KHÔNG đổi số liệu, ký hiệu, mũi tên, dấu ·, %, $. "
     "Giữ nguyên số lượng phần tử. Trả về DUY NHẤT một mảng JSON các chuỗi đã sửa, cùng thứ tự.")

def call(batch):
    req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps({"model":"google/gemma-3-27b-it","temperature":0.3,
          "messages":[{"role":"system","content":SYS},
                      {"role":"user","content":json.dumps(batch,ensure_ascii=False)}]}).encode(),
        headers={'Authorization':'Bearer '+KEY,'Content-Type':'application/json'})
    r=json.loads(urllib.request.urlopen(req,timeout=180).read())
    c=r['choices'][0]['message']['content']
    c=re.sub(r'^```(?:json)?|```$','',c.strip(),flags=re.M).strip()
    return json.loads(c)

texts=[html.unescape(t) for _,_,t in segs]
out=[]
B=40
for i in range(0,len(texts),B):
    b=texts[i:i+B]
    try:
        r=call(b)
        if not isinstance(r,list) or len(r)!=len(b): r=b
    except Exception as e:
        print('batch',i,'lỗi:',str(e)[:80]); r=b
    out+= [x if isinstance(x,str) else b[j] for j,x in enumerate(r)]
    print('xong',i+len(b),'/',len(texts))

new=body; changed=0
for (kind,(a,z),orig),tr in sorted(zip(segs,out), key=lambda x:-x[0][1][0]):
    tr2=html.escape(tr,quote=(kind=='tip')) if kind=='tip' else tr
    if tr2!=orig: changed+=1
    new=new[:a]+tr2+new[z:]
open(OUT,'w',encoding='utf-8').write(s.split('</style>',1)[0]+'</style>'+new)
print('ĐỔI',changed,'/',len(segs),'->',OUT)
