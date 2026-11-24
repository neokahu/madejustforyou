#!/bin/bash
# usage: render_svg.sh in.svg out.png [px_height]   -> transparent PNG of the ornament (crop of the artwork viewBox)
set -e
IN="$1"; OUT="$2"; H="${3:-3000}"
TMP=$(mktemp -d)
python3 - "$IN" "$TMP/page.html" "$H" <<'PY'
import sys,re
svg=open(sys.argv[1]).read(); H=int(sys.argv[3])
# crop to the ornament (hanger + body) in artwork units; source viewBox is 805 x 1610
vb=(-30,800,860,810); W=round(H*vb[2]/vb[3])
svg=re.sub(r'viewBox="[^"]*"',f'viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}"',svg,1)
svg=re.sub(r'preserveAspectRatio="xMidYMin slice"','preserveAspectRatio="xMidYMid meet"',svg,1)
svg=svg.replace('<svg ',f'<svg width="{W}" height="{H}" ',1)
html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Chewy&family=Fredoka+One&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:transparent}}svg{{display:block}}</style></head><body>{svg}
<script>document.fonts.ready.then(()=>{{document.title='ready'}})</script></body></html>'''
open(sys.argv[2],'w').write(html); print(W,H)
PY
read W HH < <(python3 -c "print(round($H*860/810), $H)")
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --default-background-color=00000000 --window-size=$W,$HH --virtual-time-budget=15000 \
  --screenshot="$OUT" "file://$TMP/page.html" >/dev/null 2>&1
rm -rf "$TMP"
python3 -c "from PIL import Image; im=Image.open('$OUT'); print('$OUT', im.size, im.mode, 'alpha range', im.getchannel('A').getextrema() if im.mode=='RGBA' else 'n/a')"
