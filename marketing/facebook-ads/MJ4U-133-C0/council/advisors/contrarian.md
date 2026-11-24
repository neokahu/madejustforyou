**K10 — READY WITH FIXES**
- Beat 7 (15.0–17.5s): "Their first Christmas as three." is the stock pregnancy-announcement line; over a newlywed couple hugging, a cold viewer reads a baby reveal, not the dog. → "Daniel, Grace and Mochi's first Christmas." or "First Christmas as two. Plus Mochi."
- Beats 2–3 (2.0–6.4s): kraft box face-up near the top of the DECORATIONS box while she lifts baubles around it — she can't plausibly miss it; irony looks staged. → box under a fold of tissue in 1A and 2; in beat 4 she lifts the tissue first.
- Beat 7 (14.8–17.5s): 2-person embrace + live Corgi jumping between + two laughs + composited ornament sharp in foreground = riskiest shot in the script. → Mochi sits at their feet looking up; no jump.
- Beat 1B (0.0–3.2s): caption says "childhood ornaments" (plural); shot shows one bauble. → 2–3 old baubles on nearby branches.

**K13 — READY WITH FIXES**
- H16 (0.3–1.0s) + beat 2 (2.0–4.2s): Mom raises the ornament into lamp light right beside the kids, then "shows them" at 4.2s — the turn is already spent; logic breaks. → she holds it low behind her, out of their sight line, until beat 3.
- Caption lag (3.2–8.0s): picture cuts to Mom showing the ornament at 4.2s while "Lily wouldn't put his collar down" is up to 5.6s; "Mom had this year's ornament made" runs over the start of the name pan (7.0s). Every beat reads ~1.4s behind its picture (E50). → move picture cuts to 4.6 / 8.0, or shorten STAKES so its card ends at 4.6.
- Beat 6 (13.6–17.5s): one 3.9s clip = collar placement + look up + 3-way hug + smiles through wet eyes. AI tears + three faces drift. → Lily lays the collar and leans into Mom; no tears.
- Beat 6 caption "His collar stays right under him" implies the dog is physically there. → "His collar stays under his spot."

**K04 — READY WITH FIXES**
- H34 (0.0–2.0s), question for the owner: split-screen real face vs cartoon figure; "Same grin" claims a likeness the product can't customise (F6 has no expression option) and invites "that's not him". 07 claim check before generation, not after.
- Beat 2a (2.0–3.4s): 1.4s shot breaks E32 (2–5s). Grandma-sweater match plays under the hook caption; its own caption arrives as the picture moves to the glasses. → merge 2a+2b into one 4.0s shot (glasses then sweater) or reverse caption order.
- Beats 2–3 (2.0–8.8s): 6.8s of the same fingertip on the same tabletop. → vary framing (photo in her hand, then ledge close-up).
- Beat 5a (12.0–14.2s): Olivia (the giver) is absent when Grandpa opens it, appears only for the hug — "he sees she paid attention" loses its giver; "found his glasses" unreadable on a 5-in ornament in a wide. → Olivia in the 5a frame + 0.5s insert of his finger on the printed glasses.

**K06 — READY WITH FIXES**
- Beats 1–4 (0.0–12.0s): 60% of the ad is camera moves on one still render — no people, no stakes, no story; "STAKES" is a name roll call. It's the slideshow risk that already cost us. → replace beat 3 (6.0–8.8s) with live Sofia holding the ornament beside baby Mateo in Mom's arms; beat 4 stays the full-frame proof.
- Beat 2a (1.6s) breaks E32 → fold into 2b.
- H50 (0.0–0.2s): extreme close-up of the printed baby, far beyond render size. Confirm the K06 render has the pixels at 1080w, or start at a medium close.
- Beat 5 (12.0–17.0s): 4 live people incl. an infant + a hang + a point printed baby → real baby. → ornament already hung; 5a = Sofia, Mom and the baby only; Dad soft behind.

**K02 — READY WITH FIXES**
- Copy bullet 4: "big wooden numbers" is false — F9 says *3D-look* printed numbers. → use F9 wording.
- Beat 5a (12.0–14.6s): Dad + 3 kids + dog licking his face + composited ornament in a hand during a hug = hardest shot of the round. → Bailey's paws on the armrest; no lick.
- H63 (0.0–1.0s): "DAD'S LIST: 1. NOTHING" must be a composited prop, never generated text; mark it "composited" like K10's DECORATIONS.
- Beat 5b caption: nothing on screen shows "His idea." → he takes the kids' ornament from a side branch and moves it to the centre; or keep and accept a weak claim.

**K01 (control) — READY WITH FIXES**
- Beat 4 (6.9–9.0s): "Grandpa pushed up his glasses" + glasses match = K04's concept inside the control; muddies attribution and narrates a non-event. → "Grandpa needed a closer look."
- Beats 2 and 6a (2.0–4.6s, 12.2–14.8s): seven people + a dog, all identity-matched, twice. If either drifts the control is compromised (script admits H76 then fails E28). → beat 2 locked-off as two staged rows; 6a only Grandma + two members sharp.
- H79 (0.0–2.0s), question for the owner: "She counted every face" over a hand-over-mouth and a hug; no counting shown (E50).
- Beat 6a caption: "Cooper barked" describes a sound in a muted ad; "Everyone waved" flat. → script's own fallback "Everyone waved. Even Cooper."
- Copy: same "big wooden numbers" error → "3D-look".

**Across all six**
1. Shared end card (question for the owner): the hero plate is K02's family (Jacob, Mary, Kobe…). K02 is the only ad whose ending stays in its own story; in the other 11 a stranger's family appears right after the concept's ornament at 17.0–17.5s — a test-integrity tilt toward K02.
2. Composited artwork on moving hands: almost every script has the real render inside boxes, in moving hands, swinging on strings — each needs planar tracking in post, and RENDERS says the K02 hero isn't even a cut-out. → keep in-hand shots locked off with the ornament at VS1/VS2; save legibility for still beats; budget tracking before Gate A.
3. Hygiene: K04/K06 add a separate 0.5s own-ornament shot at 17.0s while K10/K13/K02 keep the ornament in frame inside the last story shot — pick the latter everywhere. CTA key is `call_to_action` in four scripts and `button` in K01/K02, but upload_draft.py reads `cta` — normalize at the ad-content.json step.
