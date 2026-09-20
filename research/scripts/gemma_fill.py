# -*- coding: utf-8 -*-
"""Vá các dòng mà gemma_md.py bỏ sót (còn nguyên tiếng Anh). Dịch lại theo batch NHỎ + retry.
Dùng: python3 gemma_fill.py <file_en> <file_vi_cần_vá>"""
import re, json, os, sys, time, urllib.request

KEY=None
for line in open(os.path.expanduser('~/.global-keys.env'),encoding='utf-8'):
    if line.startswith('OPENROUTER_API_KEY'):
        KEY=line.split('=',1)[1].strip().strip('"').strip("'")

EN, VI = sys.argv[1], sys.argv[2]
en=open(EN,encoding='utf-8').read().split('\n')
vi=open(VI,encoding='utf-8').read().split('\n')
assert len(en)==len(vi), 'lệch số dòng: %d vs %d'%(len(en),len(vi))

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
     "6. Xưng hô lịch sự: cháu/bà/mẹ — tuyệt đối không dùng 'nó' cho người hoặc thú cưng.\n"
     "Trả về DUY NHẤT một mảng JSON các dòng đã dịch, đúng thứ tự và ĐÚNG SỐ LƯỢNG dòng nhận vào.")

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

# dòng cần vá: còn y hệt tiếng Anh, có chữ, không phải tiêu đề/link/metadata giữ nguyên cố ý
SKIP=re.compile(r'^(>\s*(📄|🇻🇳)|>\s*\*\(the Markdown|\s*$|\s*[-|=*_·]+\s*$)')
todo=[i for i in range(1,len(en))
      if en[i]==vi[i] and len(en[i].strip())>40 and not SKIP.match(en[i])
      and re.search(r'[A-Za-z]{4}', en[i])]
print('cần vá: %d dòng'%len(todo), flush=True)

B=4; fixed=0
for s in range(0,len(todo),B):
    idx=todo[s:s+B]; batch=[en[i] for i in idx]
    got=None
    for attempt in range(4):
        try:
            r=call(batch)
            if isinstance(r,list) and len(r)==len(batch) and all(isinstance(x,str) for x in r):
                got=r; break
        except Exception as e:
            print('  lỗi',str(e)[:60],flush=True)
        time.sleep(1.5*(attempt+1))
    if got is None:                      # hạ xuống từng dòng một
        got=[]
        for one in batch:
            o=None
            for _ in range(3):
                try:
                    r=call([one])
                    if isinstance(r,list) and len(r)==1 and isinstance(r[0],str): o=r[0]; break
                except Exception: time.sleep(2)
            got.append(o if o else one)
    for j,i in enumerate(idx):
        if got[j]!=en[i]: fixed+=1
        vi[i]=got[j]
    print('vá %d/%d (đã dịch được %d)'%(min(s+B,len(todo)),len(todo),fixed),flush=True)

open(VI,'w',encoding='utf-8').write('\n'.join(vi))
print('XONG: vá được %d / %d dòng -> %s'%(fixed,len(todo),VI))
