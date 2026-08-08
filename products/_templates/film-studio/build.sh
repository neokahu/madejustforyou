#!/bin/bash
# Film assembly — STANDARD layout (one film per product):
#   film/ production.md script.md
#        refs/{cast,product,props}   <- Phase 2 locked inputs (turntables)
#        shots/  sc01-*.mp4 …        <- Phase 3 raw scene clips (WINNERS only)
#        audio/  music.mp3 vo.mp3
#        build/  <- EPHEMERAL intermediates (gitignored)   out/ <- deliverables
#        _scratch/ <- verify frames + rejected takes (gitignored)
# Edit the SCENES block below, then: bash build.sh
set -e
cd "$(dirname "$0")"
SHOTS=shots; AUD=audio; B=build; OUT=out
mkdir -p "$B" "$OUT"
python3 captions.py >/dev/null; python3 props.py >/dev/null; python3 endcard.py >/dev/null

NORM="scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps=24,setsar=1"
COLD="eq=contrast=1.08:saturation=0.66:brightness=-0.03,colorbalance=rs=-0.08:gs=-0.02:bs=0.10,vignette=PI/4.2"
WARM="eq=contrast=1.07:saturation=1.13:brightness=0.012,colorbalance=rs=0.07:gs=0.02:bs=-0.05,vignette=PI/4.5"
PAPER="eq=contrast=1.04:saturation=0.95,vignette=PI/5"
FMT="format=yuv420p"; T=0.4   # crossfade seconds

# scene w/ caption: sc <out> <infile> <ss> <dur> <grade> <capId|->
sc(){ if [ "$6" = "-" ]; then
  ffmpeg -loglevel error -y -ss "$3" -t "$4" -i "$2" -filter_complex "[0:v]$NORM,$5,$FMT[o]" -map "[o]" -an -r 24 "$B/$1"
 else
  ffmpeg -loglevel error -y -ss "$3" -t "$4" -i "$2" -loop 1 -t "$4" -i "$B/caps/$6.png" \
   -filter_complex "[0:v]$NORM,$5[v];[1:v]format=rgba,fade=in:st=0.3:d=0.4:alpha=1,fade=out:st=$(echo "$4-0.6"|bc):d=0.5:alpha=1[c];[v][c]overlay=0:0,$FMT[o]" -map "[o]" -an -r 24 "$B/$1"
 fi; }
# still insert: ins <out> <img> <dur> <grade>
ins(){ ffmpeg -loglevel error -y -loop 1 -t "$3" -i "$2" -filter_complex "[0:v]$NORM,$4,$FMT[o]" -map "[o]" -an -r 24 "$B/$1"; }

# ============ EDIT PER FILM: build each segment, in order ============
# (COLD for setup, WARM after the reveal. Product only in close/medium shots.)
sc  p01.mp4 $SHOTS/sc01-hook.mp4     0.3 4.0 "$COLD" c1
sc  p02.mp4 $SHOTS/sc02.mp4          0.3 4.0 "$COLD" c2
ins p03.mp4 $B/props/notebook.png    2.5 "$PAPER"
ins p04.mp4 $B/props/note.png        3.0 "$PAPER"
sc  p05.mp4 $SHOTS/sc06-reveal.mp4   0.3 3.5 "$WARM" c6
ins p06.mp4 $SHOTS/product-motion.mp4 0.4 2.5   # a live product clip; use sc for graded video
sc  p07.mp4 $SHOTS/sc08-hero.mp4     0.3 4.0 "$WARM" c8
ins p08.mp4 $B/endcard.png           3.0 "$FMT"
SEGS=(p01 p02 p03 p04 p05 p06 p07 p08)
DURS=(4.0 4.0 2.5 3.0 3.5 2.5 4.0 3.0)
# ====================================================================

inputs=""; for f in "${SEGS[@]}"; do inputs="$inputs -i $B/$f.mp4"; done
prev="[0:v]"; cum=${DURS[0]}; fc=""
for ((i=1;i<${#SEGS[@]};i++)); do
  off=$(echo "$cum-$T"|bc)
  [ $i -eq $((${#SEGS[@]}-1)) ] && out="[vout]" || out="[x$i]"
  fc="$fc$prev[$i:v]xfade=transition=fade:duration=$T:offset=$off$out;"; prev="[x$i]"; cum=$(echo "$cum+${DURS[$i]}-$T"|bc)
done
ffmpeg -loglevel error -y $inputs -filter_complex "${fc%;}" -map "[vout]" -c:v libx264 -crf 18 -pix_fmt yuv420p "$B/video.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$B/video.mp4")
ffmpeg -loglevel error -y -ss 6 -t "$DUR" -i $AUD/music.mp3 -af "afade=t=in:st=0:d=1.5,afade=t=out:st=$(echo "$DUR-2.5"|bc):d=2.5,volume=0.9" -ar 44100 "$B/music.m4a"
TITLE=${TITLE:-film}
ffmpeg -loglevel error -y -i "$B/video.mp4" -i "$B/music.m4a" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT/${TITLE}_master.mp4"
echo "=== DONE -> $OUT/${TITLE}_master.mp4 ($DUR s) ==="
