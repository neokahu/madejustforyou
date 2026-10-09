C1 is producible, and it's the cheapest of the three: only 2 new clips (B2, B4), about $2-3 with reshoots. Two prompts will fail as written. Fix them before spending anything.

**B4 is the shot that will die.** Its start frame is built from WALL-4K, which is a tight crop of the wall. Nano Banana then has to invent an armchair and a 70-year-old man at the right scale next to a shadow that fills the frame. You'll get a giant hand or a dollhouse shadow. Use `C3-room-first.png` as the room reference instead. In that frame the armchair already sits left of the low wall shadow, so the geometry is solved. Lock the scale in the prompt: "the shadow is about knee height when he is seated; he leans forward to reach it." Use WALL-4K only for the outline. Also cut Seedance to one move. "Push-in → lateral track" plus a hand placement in 5s at 720p means two chances to morph the hand and drift the shadow. Prompt one slow push-in while the palm settles flat. Budget 3 takes.

**B2 has a lighting trap.** Image 1 is a gold sunset frame, and the prompt asks for "cool even morning." Nano Banana half-relights it, and you get muddy amber, not blue. Say it explicitly: "relight to overcast cool daylight, no direct sun, no wall projection." Drop "first thin edge of warm sunlight" from the video prompt. Lighting changes in i2v flicker, and the cut to B3a already delivers the gold. Again, one move only: the tilt-up. Seedance can turn "Shot 1 / Shot 2" into a hard cut inside a 4s window.

**Conflicts:**
- C1-c doesn't matter. A palm flat on the wall barely occludes the beam, and nobody scrolling checks optics.
- C1-a is fine.
- C1-d is correct.
- C1-b matters, and it's cheap to fix: add `F-PHOTO.png` (owner hugging the living dog) as a framed photo on the side table in the B4 start frame. That's one extra image ref, zero extra video risk.

**Monday order:** WALL-4K → B4 frame (QA) → B2 frame (QA) → the 2 clips → assemble.
