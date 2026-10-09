# Anonymized advisor responses — C1-personalization

**Response A:**
C1 is producible, and it's the cheapest of the three: only 2 new clips (B2, B4), about $2-3 with reshoots. Two prompts will fail as written. Fix them before spending anything.

**B4 is the shot that will die.** Its start frame is built from WALL-4K, which is a tight crop of the wall. Nano Banana then has to invent an armchair and a 70-year-old man at the right scale next to a shadow that fills the frame. You'll get a giant hand or a dollhouse shadow. Use `C3-room-first.png` as the room reference instead. In that frame the armchair already sits left of the low wall shadow, so the geometry is solved. Lock the scale in the prompt: "the shadow is about knee height when he is seated; he leans forward to reach it." Use WALL-4K only for the outline. Also cut Seedance to one move. "Push-in → lateral track" plus a hand placement in 5s at 720p means two chances to morph the hand and drift the shadow. Prompt one slow push-in while the palm settles flat. Budget 3 takes.

**B2 has a lighting trap.** Image 1 is a gold sunset frame, and the prompt asks for "cool even morning." Nano Banana half-relights it, and you get muddy amber, not blue. Say it explicitly: "relight to overcast cool daylight, no direct sun, no wall projection." Drop "first thin edge of warm sunlight" from the video prompt. Lighting changes in i2v flicker, and the cut to B3a already delivers the gold. Again, one move only: the tilt-up. Seedance can turn "Shot 1 / Shot 2" into a hard cut inside a 4s window.

**Conflicts:**
- C1-c doesn't matter. A palm flat on the wall barely occludes the beam, and nobody scrolling checks optics.
- C1-a is fine.
- C1-d is correct.
- C1-b matters, and it's cheap to fix: add `F-PHOTO.png` (owner hugging the living dog) as a framed photo on the side table in the B4 start frame. That's one extra image ref, zero extra video risk.

**Monday order:** WALL-4K → B4 frame (QA) → B2 frame (QA) → the 2 clips → assemble.

**Response B:**
I'm scrolling cold. Here's what I actually get.

**H1, frame 1:** a black blob with "Alex" in script. Who's Alex? "That's not a generic dog" answers a question I never asked. I read it as a sticker or decal ad until the pull-out around 1.5s. It works, but only just, and only because the window shows up before I've scrolled past.

**The bigger problem: I never find out the dog died.** A half-full water bowl, a coiled leash, an empty bed. That's a dog out on a walk. "His bowl hasn't moved" is too soft. "Every afternoon, he's back on the wall" sounds like a cute shadow trick. Without the word "memorial" or any loss cue, the old man touching the wall looks confused, not grieving. Fix it in beat 2: an empty, dry bowl and the collar hung on a hook by the door. Make the caption carry a time stamp: "His bowl hasn't moved since spring."

**I don't learn it's for MY dog.** Every caption is about Alex. Nothing says "any breed, any name" until the CTA's "theirs", and that's a pronoun switch I trip over. Put it in the beat 4 caption: "Any breed. Any name. Only theirs." Or keep the "only one Alex" line and add a second line under it.

**Trust:** a glowing, readable name *inside a shadow* looks like CGI. My first thought is "does it really do that?" If the real panel doesn't throw a legible name, this is a refund magnet. Show it honestly.

**Conflicts:** C1-b matters most. An old man alone with a shadow is just sad, and sad doesn't make me click. C1-c matters too: people notice when a hand throws no shadow of its own. C1-a and C1-d are internal bookkeeping and don't matter to me.

**Response C:**
Strip it down: C1 exists to sell one belief, "this is MY dog, not a dog." The viewer's dog is not Alex. What they must feel is that the panel matches a specific real animal so exactly that it would match theirs. The script never proves that match. It asserts it in captions.

Look at where C1 actually differs from C2/C3: beats 2 and 4, about 9 of the 20 seconds. Both are grief mood (a bowl, a hand on a wall). Neither does any personalization work. The only personalization proof is 3b, which is shared footage. So the concept slot carries none of the concept. That is the core flaw.

Fixes inside the locks:
- **Beat 2: plant the name on a real object.** Put Alex's collar with an engraved "ALEX" tag beside the bowl, sharp in the foreground, with the panel soft above it. Caption: "His collar's still by the door." When "Alex" lights up on the wall at 9s, the viewer recognizes the name instead of just reading it. It also gives H2 a personalization signal at 2–3s; right now H2×C1 proves nothing until 9s, which is the weakest pairing in the set.
- **Beat 4: hand holds a photo, not the wall.** The owner holds up an old photo of the living Alex (F-PHOTO crop) beside the shadow. Same ears, same stance. This is the visual match that "his actual breed" claims. It also kills C1-c (no hand in the beam) and softens C1-b (the dog is present and loved, so he isn't simply alone).

Conflicts:
- C1-b matters. Fix it with the photo, don't just flag it.
- C1-c disappears with the fix.
- C1-a and C1-d are fine as decided.
- S6 is a launch blocker: fill the offer.
- S3 and S4 are noise at $20/ad.
- S5 is real but locked. Accept it.

**Response D:**
The fatal flaw: C1's concept slot doesn't carry the concept. Personalization lives only in the shared beats (H1, B3b, B5), and those are identical in C2 and C3. C1's own beats, the bowl (B2) and the hand (B4), are grief beats. So the "Personalization" cell can't win or lose on personalization. If C1 beats C2, you won't know why. Spend the slot on proof. In B2, a 4s rapid flip of the same panel in three or four breeds and names (Lab "Daisy", Dachshund "Pepper", Golden "Murphy") that lands on the GSD "Alex". That proves "not a generic dog" and backs up "Choose the breed. Add the name." Right now the viewer only ever sees a GSD, so it reads as a GSD product. Move the bowl to B4, or cut it.

Second risk, and the one most likely to hurt you: the physics. B3b shows "Alex glowing inside" a crisp, wall-sized GSD shadow. A 6-inch panel with a painted black silhouette throws a small, soft, dark blob with coloured fringes. It won't project a glowing name. The headline "His Breed. His Name. In the Light." and "his shape lands on the wall" promise exactly that. Expect "fake/AI" comments that drag CTR, then refunds from buyers who got what physics allows. Either verify it with a real photo of the real product in sun, or rewrite B3b's caption and the headline so they stop claiming the name projects.

Conflicts:
- **C1-c** is understated. It's the same honesty problem, so QA'ing for a "believable result" won't fix it.
- **C1-b** matters. A man alone patting a wall is the saddest frame in the set and gives a cold scroller nothing to click on. Use F-PHOTO as a framed photo in the B4 shot (inside the slot, no lock broken).
- **C1-a** and **C1-d** are fine and don't matter.
- **S5** matters, but the hook line is locked. Hold it to 3.0s as written, and make sure B2's first second (2.0–3.0) doesn't fight it for the eye. The fast breed flip should start at 3.0.

**Response E:**
C1 is the only concept here whose buying reason works for every breed and every name, and the script treats it like a one-off. The upside isn't "Alex sells." It's that this skeleton can be cloned. The name goes on with a PIL paste and the shadow comes from a still, so making a Golden/"Bella" or a Lab/"Cooper" version means changing two assets: WALL-4K and PANEL-4K. If C1 wins, you have a breed-by-breed ad line you can aim at breed interest audiences (German Shepherd owners, Doodle groups), for about a dollar per variant. Build WALL-4K as a reusable template now, not a single still.

Beat 2 is the weakest 4 seconds. A bowl and a bed set up grief, but they don't sell personalization. Fix: put a brass collar tag engraved "ALEX" on the coiled leash, sharp in the foreground. The name then appears three times (tag, then wall, then panel), and the panel's name lands as the payoff: *his* tag, *his* panel. The QA line saying "no lettering on bowl" covers the bowl, not the tag. Composite the tag text in PIL like everything else.

Beat 4 caption, "There was only one Alex. So there's only one of these.", is the best line in the whole build. Make it the headline too. "His Breed. His Name. In the Light." is a feature list. This line is the reason to buy.

Conflicts:
- **C1-b matters most, and it's where the upside is.** Add a second, younger hand settling on top of his on the wall, a grandchild's or an adult child's. That ends the lonely-giftee problem and quietly signals "buy this for Dad" to adult children, a much bigger buyer pool than self-purchasers. It stays inside the concept slot and touches nothing locked.
- C1-a: fine, keep it face-free.
- C1-c: irrelevant. No scroller checks the physics of projection.
- C1-d: correct call.

Expect H1 to win C1, because the hook and the concept say the same thing. Read the comments for "do you do [breed]?" as free demand data for the clone line.

