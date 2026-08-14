#!/usr/bin/env bash
# Seamless product-reveal video (9:16, 1080x1920) for MJ4U-111.
# 3 in-context clips under ONE warm grade + crossfades + branded endcard + music.
# Uses the "turntable" orbit — warm-graded & feathered into a designed frame so it
# no longer looks pasted onto a grey void. Re-run: bash build_video.sh
set -e
cd "$(dirname "$0")"
ADS="$(cd ../.. && pwd)"                       # .../ads
SRC_PM="$ADS/film/shots/product-motion.mp4"
SRC_ORB="$ADS/_archive/product-turntable/refvid-orbit.mp4"
SRC_KOL="$ADS/_archive/product-turntable/kol-holds.mp4"
MUSIC="$ADS/film/audio/music.mp3"
L="layers"; mkdir -p tmp out

# unified warm grade (in-context clips) and a stronger warm lift for the grey-void orbit
GRADE="eq=contrast=1.05:saturation=1.10:brightness=0.008,colorbalance=rm=0.05:bm=-0.06:rh=0.04:bh=-0.05"
GRADE_ORB="eq=contrast=1.03:saturation=1.06:brightness=0.05,colorbalance=rm=0.09:gm=0.02:bm=-0.09:rh=0.08:bh=-0.09"
DUR=4.8

echo "seg1 — hook (product-motion, warm scene)"
ffmpeg -y -v error -i "$SRC_PM" -i "$L/cap1.png" -filter_complex \
"[0:v]trim=0:$DUR,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,$GRADE,vignette=PI/6,setsar=1[b];\
[b][1:v]overlay=0:0,format=yuv420p[v]" -map "[v]" -r 30 -t $DUR -an tmp/seg1.mp4

echo "seg2 — turntable orbit, warm-graded & feathered into designed frame"
ffmpeg -y -v error -loop 1 -i "$L/turntable_bg.jpg" -i "$SRC_ORB" -i "$L/orbit_mask.png" -i "$L/cap2.png" -filter_complex \
"[0:v]scale=1080:1920,setsar=1[bg];\
[1:v]trim=0:$DUR,setpts=PTS-STARTPTS,scale=1080:1080,$GRADE_ORB,format=rgba[orb];\
[2:v]format=gray,scale=1080:1080[m];\
[orb][m]alphamerge[orbA];\
[bg][orbA]overlay=(W-w)/2:(H-h)/2[comp];\
[comp][3:v]overlay=0:0,vignette=PI/7,format=yuv420p[v]" -map "[v]" -r 30 -t $DUR -an tmp/seg2.mp4

echo "seg3 — human (grandma holds it)"
ffmpeg -y -v error -i "$SRC_KOL" -i "$L/cap3.png" -filter_complex \
"[0:v]trim=0:$DUR,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,$GRADE,vignette=PI/6,setsar=1[b];\
[b][1:v]overlay=0:0,format=yuv420p[v]" -map "[v]" -r 30 -t $DUR -an tmp/seg3.mp4

echo "seg4 — endcard (slow push-in)"
ffmpeg -y -v error -loop 1 -i "$L/endcard.jpg" -filter_complex \
"[0:v]scale=1080:1920,setsar=1,zoompan=z='min(zoom+0.0008,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=165:s=1080x1920:fps=30,format=yuv420p[v]" \
-map "[v]" -r 30 -t 5.0 -an tmp/seg4.mp4

echo "concat with crossfades + music"
TOTAL=17.6
ffmpeg -y -v error -i tmp/seg1.mp4 -i tmp/seg2.mp4 -i tmp/seg3.mp4 -i tmp/seg4.mp4 -i "$MUSIC" -filter_complex \
"[0:v][1:v]xfade=transition=fade:duration=0.6:offset=4.2[x1];\
[x1][2:v]xfade=transition=fade:duration=0.6:offset=8.4[x2];\
[x2][3:v]xfade=transition=fade:duration=0.6:offset=12.6[v];\
[4:a]atrim=0:$TOTAL,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.2,afade=t=out:st=16.0:d=1.6,volume=0.55[a]" \
-map "[v]" -map "[a]" -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 19 -c:a aac -b:a 160k -movflags +faststart -t $TOTAL out/grandmas-garden-reveal_9x16.mp4

echo "DONE -> out/grandmas-garden-reveal_9x16.mp4"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,nb_frames -of default=noprint_wrappers=1 out/grandmas-garden-reveal_9x16.mp4
