#!/bin/bash
set -e
cd "$(dirname "$0")"
SV=scene-videos
CL=clips
OUT=final
BUILD=$OUT/_build
mkdir -p "$BUILD"
FONT="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONTB="/System/Library/Fonts/Supplemental/Arial Black.ttf"

# common caption style: white, black border, drop shadow, wrapped, lower-third-safe
cap() {  # $1=text $2=y-expr $3=fontsize
  echo "drawtext=fontfile='$FONT':text='$1':fontcolor=white:fontsize=$3:borderw=5:bordercolor=black@0.9:shadowcolor=black@0.6:shadowx=2:shadowy=2:x=(w-text_w)/2:y=$2:line_spacing=10"
}

NORM="scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps=24,format=yuv420p"

# ---- Seg1 HOOK (3.0s) — reaction close-up ----
ffmpeg -loglevel error -y -i $SV/hook-refvid.mp4 -t 3.0 \
 -vf "$NORM,$(cap 'She went quiet when she saw' 'h*0.60' 50),$(cap 'all their names…' 'h*0.60+66' 50)" \
 -an "$BUILD/s1.mp4"

# ---- Seg2 MEMORY (3.5s) — family hug wide ----
ffmpeg -loglevel error -y -i $SV/memory-refvid.mp4 -t 3.5 \
 -vf "$NORM,$(cap 'She raised the whole family.' 'h*0.62' 48)" \
 -an "$BUILD/s2.mp4"

# ---- Seg3 GIFT (3.0s) — two-generation ----
ffmpeg -loglevel error -y -i $SV/gift-refvid.mp4 -t 3.0 \
 -vf "$NORM,$(cap 'A birth flower for every grandchild' 'h*0.62' 42)" \
 -an "$BUILD/s3.mp4"

# ---- Seg4 NAME-STACK DEMO (3.0s) — product plate + names bloom in ----
# product plate is 960x960 square -> fill 9:16, names appear one by one, headline pinned
ffmpeg -loglevel error -y -i $CL/final-A-hero.mp4 -t 3.0 \
 -vf "scale=1280:1280,crop=720:1280,fps=24,format=yuv420p,\
$(cap 'Emma' 'h*0.30' 56):enable='gte(t,0.2)',\
$(cap 'Liam' 'h*0.30+72' 56):enable='gte(t,0.7)',\
$(cap 'Ava' 'h*0.30+144' 56):enable='gte(t,1.2)',\
$(cap 'Noah' 'h*0.30+216' 56):enable='gte(t,1.7)',\
$(cap 'One bloom for every grandchild' 'h*0.72' 44)" \
 -an "$BUILD/s4.mp4"

# ---- Seg5 PAYOFF + CTA (2.5s) ----
ffmpeg -loglevel error -y -i $SV/payoff-refvid.mp4 -t 2.5 \
 -vf "$NORM,$(cap 'Personalized for Grandma' 'h*0.66' 46),drawtext=fontfile='$FONTB':text='SHOP NOW':fontcolor=white:fontsize=54:borderw=5:bordercolor=black@0.9:box=1:boxcolor=0xB5651D@0.9:boxborderw=22:x=(w-text_w)/2:y=h*0.75" \
 -an "$BUILD/s5.mp4"

# ---- concat ----
printf "file 's1.mp4'\nfile 's2.mp4'\nfile 's3.mp4'\nfile 's4.mp4'\nfile 's5.mp4'\n" > "$BUILD/list.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$BUILD/list.txt" -c:v libx264 -pix_fmt yuv420p -movflags +faststart "$OUT/MJP-111_ad_silent.mp4"
echo "SILENT CUT DONE -> $OUT/MJP-111_ad_silent.mp4"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUT/MJP-111_ad_silent.mp4"
