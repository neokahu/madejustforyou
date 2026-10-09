# Anonymized advisor responses — C2-reaction

**Response A:**
C2 can be built, but beat 4 is written as a 5-second performance that Seedance won't deliver, and the before/after match cut breaks at the cut point. I looked at `owner-v1.png`. Here is what I'd fix before spending anything:

1. **The match cut doesn't hold.** B2 ends after a push-in, and B4 starts on the un-pushed `owner-v1` framing. That makes the cut a jump, not a match. Make the B2 camera fixed for the whole clip, and use push-in only in B4. Cut the B4 lateral track. Sideways moves cause face drift and show the edge of the frame, and this one adds nothing.

2. **The light band won't "move across his cheek."** `owner-v1` already has a fixed blue patch on his face. If you ask the model to move it, you get shimmer or a smear. Prompt for this instead: "the blue and gold light on his face slowly brightens and warms." That's achievable, and the before/after still lands.

3. **Too much acting for 5s.** Glisten, redden, breath, shoulders, smile: the model will either overact or skip half of it. Keep two of them: the long breath with the shoulders dropping, then a faint smile. Drop the tears, which read as AI-sad. Generate 3 takes, because 0–5.0s leaves no room to trim.

4. **The hand QA is wrong.** `owner-v1` shows one hand, the right one on the armrest. The left arm is out of frame. Checking for "both hands, 5+5" will fail every take, or prompt the model to add a hand. Change both prompts to "his right hand rests on the armrest."

5. **The B2 edit makes three changes at once:** remove the blue, flatten the light, add a bed. The floor strip at the lower left is narrow, so the bed will come out cropped or tiny. Run 3 tries and check identity first. If the bed fights you, drop it. The caption already carries "waited 11 years."

On the flagged conflicts: C2-e matters, and the swap is right. C2-d doesn't matter, because nobody tracks rooms across 3-second hard cuts. C2-a, b and c don't change what we build.

Monday: B2 edit ×3 (~$0.40) → B2 clip ×2 → B4 clip ×3 from `owner-v1`. That's about $5 and half a day.

**Response B:**
Cold scroller, sound off. Here's what I actually see.

**S-C2-H2 reads as a human death, not a dog.** An old man alone at a window, captioned "We still leave the window open for him." I assume a dead son or husband, or a hospice ad. Who is "we"? He's alone. The panel is the only dog cue, and a black silhouette backlit at a third of the frame reads as "pretty glass." Then beat 2: "Alex waited at this window for 11 years." Alex is a name, not a dog. The empty dog bed is what finally explains it, and it shows up in a medium-wide flat-light shot I've already scrolled past. Fix: put the dog bed in sharp focus in the first frame of beat 2, and caption it "**Alex, his German Shepherd,** waited at this window for 11 years." That spends 3 words to save the ad.

**Pronoun soup.** "He" is the man in beat 2, Alex in beat 3 ("he's back on the wall"), then the man again in beat 4. You know who each one is. I don't. Beat 4 should be "He still sits with Alex every afternoon," or just drop the pronoun.

**Copy written for insiders.** The headline "The Room Still Turns Gold at Four" means nothing to me. Lead with what it is: "Personalized Dog Memorial Suncatcher – His Breed, His Name." Same for the first line of the primary text: say "our German Shepherd."

**Believability.** A dark dog shape on the wall with "Alex" glowing inside it. My first thought is "CGI, mine won't do that." If the real 6-inch panel doesn't throw a legible name, someone will say so in the comments.

**Conflicts:** C2-c (sad old man alone, three times) is the one that matters. To me it's depressing, not something I'd buy as a gift, and the smile is too faint to fix it. C2-b matters only as a caveat when reading results. C2-a, C2-d (I will never notice two rooms) and C2-e don't matter to a viewer.

**Response C:**
The fatal flaw: beat 4 never shows what he is reacting to. A reaction ad sells cause and effect, and this script splits them across two rooms (C2-d) and never ties them together with an eyeline. The B4 prompt doesn't even say where he looks. Cut straight from a wall shadow in room B to an old man's glistening eyes in room A, and a cold scroller reads "sad AI grandpa." That is the lonely-giftee read (C2-c), and it lands in the beat that is supposed to carry the concept. Fix: in B4, have him turn his head and hold his gaze toward frame left, low, where the wall would be. B3b's push should end on the shadow at the right of frame so the cut becomes a real eyeline match.

Continuity bug the writer missed: C2-B2 is an edit of owner-v1 that adds the dog bed and flattens the light. C2-B4 starts from the unedited owner-v1, so the bed disappears and the "same framing" match cut breaks. Build the B4 start frame from the C2-B2 frame instead, with the bed kept and the gold band added in the still. Don't make Seedance invent light moving across glasses.

The emotional peak depends on micro-expression ("eyes glisten and redden"), which is the thing Seedance renders worst at 720p and the thing nobody can see on a phone. Put the reaction in his body: the long breath, the shoulders dropping, and his head tipping back against the chair.

Caption risk: "Alex waited at this window for 11 years" is past tense, but on its own, before beat 3, it can read like a lost or living dog. Add dates (e.g. "Alex, 2013–2024") or "still" phrasing so it reads clearly as a memorial.

Conflicts: C2-d matters most, and the writer underrated it. C2-c is real but gets fixed by the eyeline. C2-a and C2-b are academic, so ignore them. C2-e is correct.

**Response D:**
The script sets up its best payoff in beat 2 and then never uses it. The empty grey dog bed is the most powerful prop in all six ads, and beat 4 ignores it. Fix: in beat 4, the low sun throws the German Shepherd shape from the panel **into the dog bed beside his chair**. Alex is lying in his spot again. The man looks down at it, breathes out, and his shoulders drop. That one change gets you four things:

1. **It answers C2-c (the lonely-man risk) inside the locks.** He is no longer a man alone. He is sitting with his dog. The light stands in for the family connection, so no extra beat is needed.
2. **It mostly fixes C2-d (two rooms).** The projection now visibly lands in his room, so the "Every afternoon, he's back on the wall" line has a second, closer echo.
3. **It sells the product's mechanism on the man's face.** Viewers see what the panel *does* without being told: you buy a reason to sit by the window at four.
4. **It's the shot people will share in the comments.** It's the "I'm not crying, you're crying" frame, which is what pushes cold CPMs down.

Build it as a Nano Banana edit of owner-v1 with the dog-shaped colour in the bed, then a gentle Seedance push. Keep the band of colour on his cheek as well.

C2-b is upside, not a bug. S-C2-H2 is the most coherent ad of the six: a face, then the window, then the reaction, all one emotional line. Back it to be the scaling winner.

C2-a doesn't matter, because the locked proof is in B3b anyway. C2-e is correct: drop the palm clip.

Copy upside: "at four" is the most valuable two words in the set. Specific time plus ritual is a format you can franchise. Every breed and every name can get "The room still turns gold at four", and it can carry the whole C2 concept line through Phase 2.

**Response E:**
What does C2 have to prove? That this object does something to a grieving owner. A stranger's tear doesn't sell that. What sells it is visible cause and effect: Alex's light lands, and the man changes. The script cuts the cause off from the effect. C2-d (two rooms) is not a minor continuity note. It is the main flaw. In beat 4, a blue-gold band crosses his cheek, and nothing on screen says that band is Alex. It could be any stained glass. So the concept's buying reason never lands. It only gets implied.

The fix is already in the script. Beat 2 plants an empty grey dog bed. Pay it off. In beat 4, the German Shepherd-shaped light falls into the empty bed beside his chair, in the same frame as his face. That way the cause (Alex's shape, back in his spot) and the effect (him) are one image. It needs no B3 regeneration, it stays inside the concept slot, and it also defuses C2-c. He is no longer a lonely man in a chair. He is sitting with his dog again, which is the family-connection feeling the house rule wants.

Second, don't make a 720p micro-expression carry the load. "Eyes glisten, faint smile" will be invisible on a phone and is the most likely Seedance failure. Give him one readable act instead. His hand lowers from the armrest and rests on the bed's rim inside the light, with the back of the hand to camera so the palm rule holds. Keep the breath and the shoulder drop.

Third, beat 2's flat, cool light makes the panel look dead during 2–3s, which is inside Meta's 3-second window on both hooks. Keep his face neutral, but let the panel itself glow faintly.

On the conflicts: C2-d is critical and fixed as above. C2-c is real and fixed by the same shot. C2-a is moot because it's locked. C2-b is cosmetic. C2-e is correct as written.

