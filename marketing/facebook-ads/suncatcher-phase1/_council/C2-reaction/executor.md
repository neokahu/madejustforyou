C2 can be built, but beat 4 is written as a 5-second performance that Seedance won't deliver, and the before/after match cut breaks at the cut point. I looked at `owner-v1.png`. Here is what I'd fix before spending anything:

1. **The match cut doesn't hold.** B2 ends after a push-in, and B4 starts on the un-pushed `owner-v1` framing. That makes the cut a jump, not a match. Make the B2 camera fixed for the whole clip, and use push-in only in B4. Cut the B4 lateral track. Sideways moves cause face drift and show the edge of the frame, and this one adds nothing.

2. **The light band won't "move across his cheek."** `owner-v1` already has a fixed blue patch on his face. If you ask the model to move it, you get shimmer or a smear. Prompt for this instead: "the blue and gold light on his face slowly brightens and warms." That's achievable, and the before/after still lands.

3. **Too much acting for 5s.** Glisten, redden, breath, shoulders, smile: the model will either overact or skip half of it. Keep two of them: the long breath with the shoulders dropping, then a faint smile. Drop the tears, which read as AI-sad. Generate 3 takes, because 0–5.0s leaves no room to trim.

4. **The hand QA is wrong.** `owner-v1` shows one hand, the right one on the armrest. The left arm is out of frame. Checking for "both hands, 5+5" will fail every take, or prompt the model to add a hand. Change both prompts to "his right hand rests on the armrest."

5. **The B2 edit makes three changes at once:** remove the blue, flatten the light, add a bed. The floor strip at the lower left is narrow, so the bed will come out cropped or tiny. Run 3 tries and check identity first. If the bed fights you, drop it. The caption already carries "waited 11 years."

On the flagged conflicts: C2-e matters, and the swap is right. C2-d doesn't matter, because nobody tracks rooms across 3-second hard cuts. C2-a, b and c don't change what we build.

Monday: B2 edit ×3 (~$0.40) → B2 clip ×2 → B4 clip ×3 from `owner-v1`. That's about $5 and half a day.
