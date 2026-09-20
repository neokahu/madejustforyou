# Video Ad Decomposition & Phase-1 Test Plan (Meta DTC/ecom, 2026)

> 📄 **Google Doc mirror:** https://docs.google.com/document/d/1obX8brgMHnwmV1c4rpeZLkmC-ww7NXA-NC99hO84kaQ/edit
> *(the Markdown file in this repo is the source of truth; re-import after edits)*
>
> 🇻🇳 **Bản tiếng Việt:** https://docs.google.com/document/d/1rCt4W2x1f72tYpHIgHyXV-82xNveBTrX4i8RIEJAp70/edit

Nghiên cứu 13/09/2026. Mục đích: chia nhỏ video quảng cáo ecom dạng ngắn để test, và xếp hạng các thành phần cho Phase 1.
(Tương tác), và quyết định **test bao nhiêu kịch bản video cho mỗi sản phẩm.** Nhóm Feeds A (creative) + cái
Mô hình vận hành creative trong `TESTING-MATRIX-FRAMEWORK.md`. **[DATA]** = số liệu đo được; **[OPINION]** = ý kiến đồng thuận đáng tin cậy.

## Phân tích — rút ra từ các nguồn (hai góc nhìn thống nhất)
Bất kỳ nguồn nào nghiêm túc đều sử dụng một trong hai hoặc cả hai cách này, và chúng bổ trợ cho nhau:
- **Khung thời gian (diễn biến video):** **Hook → Nội dung (Câu chuyện + Bằng chứng) → CTA.** (Sovran, Barry Hott, Meta).
  Thời điểm lý tưởng của Hott: 3s đầu = thu hút sự chú ý · ~10s tiếp theo = chứng minh · ~5s cuối = kêu gọi hành động.
- **Các yếu tố tùy chỉnh (thứ bạn thực sự thay đổi để test):** cách các công cụ phân tích gắn thẻ cho mỗi ads — **Motion**
  (Hook · Messaging/Angle · Visual/Format · Persona) và **creads.io** 6 chiều (Hook · Concept/Angle ·
  Sự kết nối cảm xúc · Thiên kiến tâm lý · Cách dùng từ · Bố cục hình ảnh).

**Các yếu tố LẶP LẠI trên tất cả các nguồn (phân tích thực tế):**
1. **Hook** (0.5–3s: hình ảnh + chữ trên màn hình + giọng đọc/âm thanh tùy chọn)
2. **Concept / Angle / Persona** (ý tưởng chính + giai đoạn nhận diện đối tượng mục tiêu)
3. **Body / Retention** ("Story + Proof" — cơ chế thuyết phục)
4. **Offer** ("the offer is the hook")
5. **CTA / close**
6. **Format / phong cách sản xuất** (UGC · lifestyle · high-production; skit/listicle/founder/testimonial/demo)
7. **Cross-cutting craft:** captions/on-screen text (thiết kế cho xem không âm thanh), pacing/cut-frequency, music/sound

> Các nguồn đều đồng ý về nội dung chính, chỉ khác nhau về mức độ chi tiết: người làm cấu trúc nói về Hook/Proof/CTA;
> team phân tích thêm Angle/Format/Offer là các yếu tố cần test riêng. Timeline = Hook→Body→CTA; các yếu tố cần test =
> Hook/Angle/Format/Offer/Body/CTA.

## Per-component table
| Thành phần | Tác động tới | Các loại / khung | Benchmark / dữ liệu | Cách test | Nguồn |
|---|---|---|---|---|---|
| **Hook** (0.5–3s) | **Hook rate** — yếu tố quyết định mọi thứ phía sau | tactics: tạo sự tò mò · đi ngược lại số đông · số liệu cụ thể · thay đổi/trước-sau · câu hỏi · kêu gọi · bằng chứng xã hội · phá vỡ khuôn mẫu · góc nhìn POV, tập trung vào khuôn mặt+ánh mắt. Meta chia 3 loại: giá trị hứa hẹn · gợi ý/teaser · gây sốc/thống kê | **[DATA]** tốt là 25–35%, trên 30% có thể scale, trên 40% là xuất sắc, dưới 20% cần làm lại (AdLibrary/Triple Whale/hawky thống nhất). Các yếu tố ảnh hưởng: payoff xuất hiện ở khung hình đầu tiên (+5–12pt), chuyển động trong 0.5s đầu (+3–8), text hiển thị trước 0.5s (+4–9), tỷ lệ khung hình 9:16 (+5–15) | **OFAT** — giữ nguyên body, thay đổi opener. **Tối thiểu ≥3 opener/concept**; test nhanh 10–20 hook/angle chiến thắng | motionapp.com/blog/best-dtc-meta-ad-hooks-2025 · adlibrary.com/posts/hook-rate |
| **Concept / Angle / Persona** | hook + hold + CTR + CPA (toàn bộ ý tưởng) | khớp với giai đoạn nhận diện (chưa biết → tò mò/thay đổi; biết vấn đề → thấu hiểu; biết giải pháp → bằng chứng; biết sản phẩm → ưu đãi) | **[DATA-ish]** 4+ góc độ khác biệt → **tuổi thọ creative dài hơn 30–50%** trước khi bị chai (creads.io) | **toàn bộ các concept đa dạng, KHÔNG OFAT.** Gắn thẻ mỗi concept theo góc độ để dễ dàng xác định concept chiến thắng | creads.io/ad-creative-performance-guide · help.motionapp.com AI-tagging |
| **Body / Retention** ("Story+Proof") | **Hold rate** (15s÷3s), thời gian xem trung bình, ThruPlay | PAS · AIDA · BAB · Vấn đề-Giải pháp-Bằng chứng; các yếu tố: demo, lời chứng thực, trước/sau, cắt nhanh, mở vòng lặp, danh sách | **[DATA]** hold tốt **40–50%** (Motion); ổn định 30–40%; <25–35% với hook mạnh = "lừa đảo" | sửa phần giữa 5–15s **mà không chạm vào opener** khi hook ổn/hold thấp; test loại bằng chứng | adlibrary.com/posts/hold-rate · sovran.ai |
| **Offer** | CTR, CPA, CVR | BOGO/quà tặng · không rủi ro · bảo hành · giảm giá; hiển thị rõ trong khung hình | **[OPINION]** xây dựng lại offer trước khi làm ad (Hott) | test dưới dạng biến thể thông điệp | LinkedIn (Elefante-Smith on Hott) · Motion offer tag |
| **CTA** | **outbound/link CTR**, CVR | bước tiếp theo rõ ràng · tính cấp bách/hiếm có · nhắc lại ưu đãi; đặt lên trước (nhiều người hành động trước khi hết) | **[DATA-ish]** Meta: "hook+watch cao, click thấp → tập trung vào CTA" | **OFAT** — ad giống nhau, thay đổi CTA/end-card | help.motionapp.com metrics · facebook.com/business/help/188534925073536 |
| **Format / phong cách sản xuất** | hook + hold + thời lượng | **Đối với POD quà tặng cá nhân hóa, hãy sử dụng danh sách đánh giá phù hợp bên dưới** (reveal · gift-reaction · occasion · POV-giving · testimonial · UGC = CAO). ⚠️ **founder-story = THẤP, podcast = BỎ QUA** (chung chung-DTC, không phù hợp với cửa hàng quà tặng). | **[DATA]** native/UGC luôn thắng thiết kế trau chuốt trên Reels/Stories; tái sử dụng *thông điệp* thắng lợi thành *định dạng* mới = chiến lược đa dạng hóa #1 sau Andromeda | test toàn bộ định dạng mới của một angle đã được chứng minh (đa dạng hóa) | xem phần dành riêng cho POD bên dưới |
| **Caption / không âm thanh** (cắt chéo) | hook + hold | text trên màn hình sau 0.5s; caption | **[DATA]** ~**80–85% số lượt xem là không có âm thanh** (Meta); caption ↑ thời gian xem ~12% | luôn hiển thị; test nội dung overlay như một biến thể hook | facebook.com/business |
| **Pacing / chuyển cảnh / độ dài** (cắt chéo) | hold | tần suất cắt, phong cách chuyển cảnh, độ dài | **[DATA]** Meta: **6–15s** tốt nhất trên Feed/Stories; cắt mỗi 1–2s cho nội dung ngắn. **[OPINION] Tốc độ cắt phụ thuộc vào định dạng, không có một con số duy nhất:** ~**1.5s/cut** cho các định dạng thuyết phục nhanh · ~**5s/cut** cho UGC/tính xác thực (cắt nhanh khiến nội dung trông *được sản xuất* và giết chết cảm giác tự nhiên) · cắt theo nhịp điệu cho unboxing/reaction · tăng dần tốc độ cho BTS | test độ dài + cắt 0.5s đầu (+2–5pt hook); **hướng dẫn tốc độ cắt, đừng để cho biên tập viên tự quyết** | facebook.com/business/help/188534925073536 · Bảng khung kịch bản tiếng Việt (xem mẫu brief bên dưới) |
| **Giọng đọc / VO & âm thanh** (cắt chéo) | hook + hold (và *tính chân thực*) | ai nói (người thật vs AI vs không có) · cung bậc cảm xúc · nhạc nền · SFX/ASMR | **[DATA]** 80–85% không âm thanh có nghĩa là giọng đọc không thể mang toàn bộ quảng cáo — nhưng nó quyết định 15–20% những người *có* nghe, và là cơ chế duy nhất cho các sản phẩm phức tạp cần trình bày bằng chữ | **[OPINION]** chỉ định theo định dạng: reaction/unboxing = nhạc nền ấm áp + cảm xúc chân thật · UGC = giọng nói tự nhiên từ điện thoại · so sánh = phân tích + SFX động · BTS = chia sẻ chân thành + ASMR thật · xây dựng cảm xúc = **giọng đọc của người thật, không dùng giọng tổng hợp** | trình bày chi tiết; chỉ test như một trục khi concept dẫn đầu bởi VO | Bảng khung kịch bản tiếng Việt · xếp hạng proof POD của chúng ta |

## Ưu tiên Phase 1 (tương tác: hook rate, hold rate, CTR)
Test in this order:
1. **Hook** – quan trọng nhất, test trước và nhiều nhất.
2. **Concept/Angle** – angle yếu sẽ làm giảm hiệu quả hook (test hook trong một tập angle nhỏ để validate).
3. **Nội dung/Giữ chân** (hold) – chỉ tối ưu khi hook đã vượt qua ngưỡng đánh giá.
4. **CTA/Offer** (CTR) — giữ chân người xem là quan trọng nhất; càng về Phase 2 thì càng quan trọng hơn.

**Hook dominance — the evidence:**
- **[DATA] Meta + Nielsen: có tới 47% giá trị của chiến dịch video được hiển thị trong 3 giây đầu tiên**; 65% người xem 3 giây sẽ xem tới 10 giây, 45% xem tới 30 giây → 3 giây đầu tiên quyết định việc người xem có xem hết video hay không. (facebook.com/business/news/updated-features-for-video-ads)
- **[DATA]** các creative sống sót sau ngày thứ 21 thường có **hook rate** trên 30% ngay khi ra mắt; còn những creative chết sau 7 ngày thì **hook rate** chỉ từ 15–20% (tập dữ liệu saved-ads của AdLibrary).
- **[DATA]** yếu tố **hook** có độ biến động cao nhất: "cắt một body giống nhau thành 3 phiên bản → **hook rate** từ 18% đến 38%" (AdLibrary). Đó là *lý do* tại sao mọi người lại test **hook** nhiều nhất.
- **[DATA] Google/YouTube: creative ≈ 50% của ROAS.**

**Phân tích Hook × Hold 2×2 (để ưu tiên công việc):**
- Hook thấp / Hold thấp → Concept sai, cần thay đổi.
- **Hook cao / Hold thấp** → Chỉ cần chỉnh lại nội dung chính (body).
- **Hook rate thấp / Hold rate cao** → ROI cao nhất: chỉ cần làm lại ~1.5s đầu (chỉ số tăng 10–15 điểm).
- high hook / high hold → scale.

## Cần test bao nhiêu concept cho MỘT sản phẩm
**Dự đoán 2026 = HYBRID (kỷ nguyên Andromeda):** *đa dạng các concept toàn diện để KHÁM PHÁ ra chiến thắng; OFAT đổi hook để
TỐI ƯU/scale.* Phương pháp micro-OFAT thuần túy để tìm kiếm đã lỗi thời (những chỉnh sửa hook nhỏ "không tạo ra
"needle" — Anh Matt Steiner, VP của Meta chia sẻ qua Caleb Kruse). Andromeda ưu tiên **đa dạng + số lượng.**

**Gợi ý batch đầu tiên Phase-1 cho một sản phẩm POD/quà tặng:**
- **3–4 concept/angle khác biệt** (ví dụ: chân dung người nhận: ông bà vs cặp đôi vs thú cưng; hoặc các góc độ cảm xúc) — những ý tưởng táo bạo.
- **× 3 hook cho mỗi concept** (ví dụ: hình ảnh/tạo sự chú ý · vấn đề/cảm xúc · tò mò/kêu gọi) → **≈ 9–12 ads** cho batch đầu tiên.
- **Structure:** 3–5 creatives mỗi ad set (để đảm bảo thoát khỏi giai đoạn learning); **khoảng $20–40 mỗi concept** là tối thiểu trước khi đánh giá (Motion cần ≥$50/ads để có đủ dữ liệu); **chỉ dùng số liệu settled-day.**
- **Đánh giá Phase-1 dựa trên:** hook rate (25–35%+), hold rate (40–50%), link CTR → đánh giá dựa trên ma trận hook × hold.
- **Sau khi tìm được creative chiến thắng (chế độ velocity):** **thay đổi 10–20 hook** trên body thắng, đồng thời **tận dụng message đó để tạo thêm 2–3 format mới**; **refresh sau mỗi ~2–3 tuần** (Andromeda dễ bị 'mệt' quảng cáo).

**Các con số tham khảo (theo ý kiến chung của media buyer):**
| Item | Number | Source |
|---|---|---|
| Số concept mỗi vòng tìm kiếm | 8–12 concept, mỗi concept 2–3 biến thể, refresh sau 2–3 tuần | Segwise (growwithsakib.com) |
| Số creative mỗi ad set | 3–5 (thường trên 20 lại phản tác dụng) | AdManage.ai |
| Hệ điều hành (OS) cho creative | 3 angle × 3 format; 6–9 concept/tuần | Salman Munir |
| Sprint hook | 6–8 hook / offer, các góc độ khác nhau, trong vòng 48h | Salman Munir |
| Số lượng hook trên mỗi concept thắng (tốc độ) | 10–20 biến thể trên body thắng | Koro / Savannah Sanchez |
| Tỷ lệ new vs iteration | ~90% mới / ~10% lặp lại; 2–4 biến thể/test; ưu tiên những thay đổi lớn | Dara Denney |
| Khối lượng creative của tài khoản | ~50–100 biến thể ads/tháng; dự kiến tăng ~4x creative năm 2026 so với 2024 | Caleb Kruse (truyền đạt từ VP Meta) |
| Tỷ lệ trúng thưởng (kỳ vọng) | ~1–3 winners trên 10 creatives | AdManage.ai |

## 🎁 Thiết kế POD quà tặng cá nhân hóa (format fit + thư viện angle + hook)
*Nghiên cứu 13/09/2026, phương án dự phòng: EXACT (POD cá nhân hóa) → RỘNG HƠN (POD/hàng hóa tổng quát) → CUỐI CÙNG
(DTC chung, được đánh dấu). **Thẳng thắn: không có bộ dữ liệu hiệu suất quảng cáo công khai nào cho video ads quà tặng cá nhân hóa** —
Bậc EXACT mang tính định tính (chiến lược Etsy, định vị thương hiệu trực tiếp, văn hóa phản ứng quà tặng trên TikTok); tất cả đều dựa trên dữ liệu thực tế
Các con số là chung cho POD/DTC nói chung, chỉ mang tính chất tham khảo thôi ạ.

### Định dạng phù hợp (đánh giá cho cửa hàng quà tặng cá nhân hóa)
| Format | Fit | Why | Rung |
|---|---|---|---|
| **Hiển thị cá nhân hóa/tùy chỉnh** (trống → tên/ảnh xuất hiện) | **CAO** | chính sự tùy chỉnh *là* sản phẩm; "cá nhân hóa bán chạy nhất khi được nhìn thấy" | gần CHÍNH XÁC |
| **Phản ứng khi nhận quà** (người nhận mở/phản ứng) | **CAO** | phần thưởng cảm xúc của danh mục; lan tỏa tự nhiên | KHÁ CHÍNH XÁC |
| **Occasion / seasonal montage** (order-by-date) | **HIGH** | gifting là mua theo dịp lễ, tính khẩn cấp là yếu tố kích hoạt | EXACT |
| **POV: you're giving the gift** | **HIGH** | tạo cảm giác người mua là người trao tặng, biến họ thành nhân vật chính | WIDER/EXACT |
| **Testimonial / review** | **HIGH** | giải quyết nỗi lo "sản phẩm POD có rẻ tiền không?" | WIDER |
| **UGC-raw** ("I ordered this for my mom…") | **HIGH** | tự nhiên, chi phí thấp, dễ tái sử dụng | WIDER |
| **Hyper-personalization flex** (handwriting · kid's drawing · paw print · recipe) | **CAO** | đánh bại đối thủ bằng cách đề cập tên chung chung; hành vi phát triển nhanh nhất trên Etsy | CHÍNH XÁC |
| **Unboxing / "look what I got"** | **TRUNG BÌNH - CAO** | thể hiện chất lượng in/vật liệu thực tế | RỘNG HƠN/CHÍNH XÁC |
| **Listicle** ("5 gifts that'll make grandma cry") | **TRUNG BÌNH** | sự tò mò dễ đọc; làm ấm các tệp khách hàng mới | RỘNG HƠN |
| **Phim ngắn cảm xúc chất lượng cao** | **TRUNG BÌNH** | câu chuyện với kết quả trả chậm hiệu quả với thương hiệu nhưng tốn kém/rủi ro — sử dụng có chọn lọc | CHÍNH XÁC |
| **Screen-record của công cụ cá nhân hóa** | **MEDIUM** | trả lời câu hỏi "Nó có thực sự ghi TÊN TÔI không?" — phù hợp retarget hơn là tiếp cận khách hàng mới | WIDER |
| **BTS / quá trình sản xuất** (sản xuất → đóng gói → vận chuyển) | **MEDIUM** | giải quyết nỗi lo #1 của khách hàng trong ngành ("Sản phẩm có rẻ tiền không?") bằng sự tỉ mỉ thực tế + ASMR. ⚠️ Tuy nhiên, cận cảnh quá trình làm sản phẩm là **proof (bằng chứng) ít cảm xúc nhất (xếp hạng #5)** → **Tài sản cho Stage-2 / retargeting, không phải concept Phase-1 để tiếp cận khách hàng mới** | WIDER |
| **Lifestyle / skit / demo** | **MED-LOW** | kết nối / thu hút sự chú ý khi lướt feed, nhưng một món quà tĩnh tại khó có thể "demo" được | WIDER |
| **Câu chuyện người sáng lập** | **LOW** | ⚠️ dạng nội dung chung chung của DTC; người mua quà quan tâm đến cảm xúc của *người nhận*, không phải câu chuyện nguồn gốc của bạn | LAST-RESORT |
| **Podcast format** | **SKIP** | ⚠️ Loại này thường cho DTC/sản phẩm thông tin, không hợp với quà tặng cảm xúc, bốc đồng | PHƯƠNG ÁN CUỐI CÙNG |

### Thư viện Angle (12, tùy chỉnh) — cùng sản phẩm, cách tiếp cận khác nhau
1. **"Made just for them" — personalization reveal** *(bất kỳ người nhận nào; yếu tố tùy chỉnh là giá trị)* — gần như CHÍNH XÁC.
2. **Tear-jerk gift reaction** *(mẹ/bà/người yêu; phần thưởng là sự biết ơn)* — GẦN CHÍNH XÁC.
3. **"She'll know you actually thought about her" (feel truly seen)** *(mẹ/bà/vợ)* — EXACT (luận điểm Etsy).
4. **Tính cấp thiết dịp lễ / "order by [date]"** *(Ngày của Mẹ/Cha, Giáng sinh, kỷ niệm)* — EXACT.
5. **Kỷ niệm / món quà lưu giữ ("keep them close")** *(mất thú cưng, tưởng nhớ)* — EXACT (cường độ cảm xúc cao nhất).
6. **POV: bạn là người tặng** *(các cặp đôi, con cái → bố mẹ)* — WIDER/EXACT.
7. **Độ cá nhân hóa cực cao** *(chữ viết tay / tranh vẽ của bé / dấu chân thú cưng / công thức nấu ăn)* — CHÍNH XÁC.
8. **Chứng minh chất lượng qua video unboxing ("chất lượng làm tôi bất ngờ")** *(khách hàng hoài nghi)* — MỞ RỘNG.
9. **Lời kêu gọi đặc biệt dựa trên mối quan hệ ("dành cho bà ngoại người luôn có tất cả")** *(tệp khách hàng niche)* — MỞ RỘNG.
10. **Phim ngắn cảm xúc, sản phẩm xuất hiện sau (phong cách quảng cáo Thái Lan)** *(gia đình/mẹ; sản xuất công phu/rủi ro cao)* — GẦN CHÍNH XÁC.
11. **Gift-for-yourself / self-gifting** *(tự thưởng cho bản thân; góc độ 'xin phép' ít được khai thác)* — Mở rộng đối tượng.
12. **Listicle "gifts that'll make them cry"** *(dạng bài viết tổng hợp quà tặng khiến người nhận xúc động)* — Mở rộng đối tượng.

### Thư viện hook (tập trung vào 3 giây đầu: text trên màn hình + cảnh mở đầu)
- **Reveal:** "Xem điều gì xảy ra khi bạn nhập tên của cô ấy…" (cốc trắng → tên các cháu hiện lên) · "Cùng một chiếc áo. Hoàn toàn khác khi có *tên của họ*." (so sánh chia đôi màn hình giữa áo trơn và áo cá nhân hóa).
- **Phản ứng khi nhận quà:** "POV: cô ấy mở món quà duy nhất khiến cô ấy không ngờ lại khóc." · "Ông ấy im lặng suốt 10 giây. Rồi điều này xảy ra." (tập trung vào biểu cảm trên khuôn mặt ông).
- **Cảm xúc được thấu hiểu:** "Cô ấy đã có mọi thứ. Vì vậy, tôi tặng cô ấy một món quà mà không ai khác có thể tặng." · "Đây không phải là một món quà. Đây là bằng chứng cháu đã để ý đến cô ấy."
- **Tính cấp thiết dịp lễ:** "Ngày của Mẹ còn 9 ngày nữa. Sản phẩm được làm theo yêu cầu — đừng chần chừ." (hiển thị đếm ngược trên sản phẩm cá nhân hóa).
- **Tưởng niệm:** "Ông vẫn được treo trên cây thông Noel mỗi năm." (treo vật trang trí tưởng niệm thú cưng với dấu chân).
- **POV giving:** "POV: you finally found the gift that makes *you* the favorite child." · "Watch her face — I'll wait."
- **Hyper-personalization:** "Anyone can put her name on it. We put her grandkid's actual drawing on it." · "That's not a font. That's your dad's real handwriting."
- **Quality-proof:** "I was scared it'd look cheap. Then I opened it." · "Custom thường là dễ hỏng. Không phải cái này."
- **Relationship callout:** "For the grandma who says 'don't get me anything.'" · "Nếu bà là một 'mẹ chó', món này chắc chắn sẽ khiến bà xúc động."

### Nội dung / Giữ chân khách — tùy biến (quảng cáo quà tặng KHÔNG phải là quảng cáo vấn đề → giải pháp)
PAS/AIDA kích hoạt tư duy logic System-2 (chỉ hoạt động với những người đang tích cực mua sắm). Creative cảm xúc hiệu quả gấp ~2 lần.
Quảng cáo dài hạn (Binet & Field/IPA) và quảng cáo cảm xúc tích cực cho thấy mức tăng tương tác ~6 lần (System1) `[BIỆN PHÁP CUỐI CÙNG — tất cả các danh mục]
dữ liệu, nhưng ủng hộ một cung bậc cảm xúc hơn là PAS]. Vì vậy, cỗ máy quảng cáo quà tặng = **mong đợi → leo thang → phần thưởng**
(reveal + reaction). **Cảm xúc của người nhận là cái 'arc' chính; sản phẩm chỉ là công cụ tạo ra cảm xúc đó.**
Phân khúc này xây dựng dựa trên **khoảnh khắc phản ứng** (các thương hiệu thực sự thuê creator để có được "phản ứng chân thật, thậm chí là nước mắt").
joy") `[EXACT — creator briefs]`.

**Xếp hạng 'proof' cho quà tặng cá nhân hóa (cái gì được tính là 'proof' ở đây):**
1. **Phản ứng chân thật của người nhận** (khóc/hụt hơi) — #1 'proof'; nó chứng minh tác động cảm xúc, mà đó *chính là* sản phẩm. `[EXACT]`
2. **Chi tiết cá nhân hóa hiển thị rõ ràng** (tên/ảnh/ngày tháng thực tế của khách) — cho thấy trước kết quả mà người mua sẽ nhận được; tên là yếu tố kích thích sự chú ý mạnh mẽ nhất. `[WIDER]`
3. **Bằng chứng về số lượng/độ bền** ("Đã bán hơn 10.000 sản phẩm") — dành cho tệp khách hàng mới cần sự xác thực (Etsy: CVR 1–2% với dưới 10 đánh giá → 10–15% với 500+ đánh giá). `[WIDER]`
4. **Ảnh/video UGC đánh giá về chất lượng in ấn** — giải quyết nỗi lo "sản phẩm có rẻ tiền không?". `[WIDER]`
5. **Cận cảnh sản phẩm** (khắc/vải canvas/ánh sáng ấm hơn) — ít cảm xúc nhất, giúp khách hàng loại bỏ nghi ngờ về chất lượng. `[WIDER]`
> Với khách hàng mới (cold), ưu tiên sự đáng tin cậy (số lượng/reviews); với khách hàng ấm (warm) hoặc retarget, tập trung vào bằng chứng giải quyết nỗi đau (chất lượng, giao hàng).

**Cấu trúc video cơ bản (15–30s):**
- **A · Dựa vào phản ứng (cold, UGC):** 0–2s mở đầu bằng phản ứng gây chú ý ("She didn't expect this") → 2–6s giới thiệu bối cảnh (ai/dịp gì) → 6–12s **reveal** (hiển thị rõ tên, giữ hình) → 12–20s hoàn thành phản ứng (ôm, cả gia đình trong khung hình) → 20–27s bằng chứng + offer ("10,000+ · free personalization · order by [date]") → 27–30s CTA.
- **B · Xây dựng cảm xúc (warm, kiểu Thái-ad):** 0–3s hook = mối quan hệ/tầm quan trọng (không phải sản phẩm) → 3–10s xây dựng (người tặng đang đặt hàng, hé lộ sản phẩm) → 10–16s reveal + phản ứng → 16–24s tăng cảm xúc (đọc to dòng cá nhân hóa) → 24–30s kết quả + CTA.
- **C · Personalization-demo hybrid (retarget):** 0–2s reveal cold-open (màn hình trống → tên được gõ vào) → 2–8s menu dịp lễ ("For Grandma. For Mom. For your dog's memorial.") → 8–16s chứng minh chất lượng (cận cảnh + đánh giá ảnh) → 16–24s giảm thiểu rủi ro ("Không thích? Chúng tôi làm lại miễn phí" + ngày hết hạn đặt hàng) → 24–30s CTA "Xem với tên của bạn →".
> **Đặt phần reveal vào giữa, không phải cuối** — bạn cần thời lượng sau reveal để ghi lại phản ứng + CTA trong khi mức độ giữ chân người xem cao nhất.

### Offer — tùy chỉnh (ưu tiên các offer liên quan đến quà tặng)
1. **Đặt hàng trước ngày/đảm bảo giao hàng trước dịp lễ** — đòn bẩy cao nhất (quà tặng có thời hạn + POD cần thời gian sản xuất). Sự khẩn cấp/rõ ràng dịp lễ ~30–40% tăng CVR. `[WIDER]`
2. **Chính sách làm lại / đảm bảo hài lòng cho các sản phẩm cá nhân hóa không đổi trả** — loại bỏ rào cản "lỗi chính tả/in ấn kém, không có phương án giải quyết" đặc trưng của hàng cá nhân hóa (hàng thanh lý). Đặt chính sách này *tại điểm nghi ngờ*. `[WIDER]`
3. **Cá nhân hóa miễn phí (trình bày như một món quà tặng, không phải giảm giá)** — việc trình bày dưới dạng quà tặng làm tăng ý định mua hàng hơn so với mức giảm giá tương đương (vì giảm giá làm giảm giá trị cảm nhận). Hãy nói "tặng kèm cá nhân hóa miễn phí," thay vì "giảm 20%". `[LAST-RESORT — nghiên cứu ngang hàng, bán lẻ nói chung]`
4. **Gói sản phẩm dành cho nhiều người / bộ quà tặng** — phù hợp với hành vi mua hàng theo danh sách quà tặng, tăng AOV (giá trị đơn hàng trung bình) từ 25–40%. `[WIDER]`
5. **Dịch vụ gói quà miễn phí / tin nhắn quà tặng / vận chuyển sẵn sàng để tặng** — chi phí thấp, loại bỏ nỗi lo "tôi vẫn phải tự gói quà". `[WIDER]`
6. **Giảm giá cho lần mua đầu tiên** — vẫn hiệu quả nhưng thường xếp hạng cuối (cạnh tranh về giá, làm giảm giá trị món đồ lưu niệm); một offer *cá nhân hóa* sẽ tốt hơn hẳn offer chung chung. `[LAST-RESORT]`
> Chiến lược mạnh nhất: **ưu tiên 'đặt hàng theo ngày' + làm lại miễn phí + cá nhân hóa miễn phí**; giảm giá là phương án dự phòng, không nên làm tiêu đề chính.

### CTA — tailored (gift language)
Nút *button* của Meta bị giới hạn khoảng 17 mẫu sẵn (dùng **"Order Now"** khi có deadline/khách hàng có ý định mua cao, còn lại dùng "Shop Now" nhé). Nhớ nói **CTA tặng quà** trong text trên màn hình / giọng đọc / end-card luôn ạ:
- **"Make it for them" / "Make one with their names"** — CTA cảm xúc mặc định (lạnh, dẫn dắt bằng câu chuyện).
- **"Personalize hers/his/theirs"** — chạy ad set nhắm mục tiêu theo đối tượng nhận (Mẹ/Bà/người yêu).
- **"See it with your names"** — quảng cáo retarget / demo cá nhân hóa, giảm cam kết (Skeleton C).
- **"Create theirs / Design theirs in 60 seconds"** — giảm cảm giác tốn công sức.
- **"Order by [date] — get it before [occasion]"** — CTA thúc đẩy đặt hàng theo mùa (+ nút "Order Now").
- Tránh dùng thẳng "Buy Now" cho tệp khách hàng lạnh tìm quà — quá giao dịch với một món quà kỷ niệm mang tính cảm xúc. *(CTA cá nhân hóa/gọi bằng người thứ nhất thường test tốt hơn CTA chung chung — dữ liệu chung từ các thương hiệu DTC.)* `[LAST-RESORT]`

### Chiến thuật hook — tùy chỉnh (xếp hạng cho quà tặng)
**Tier 1 — hook chuyên biệt cho quà tặng (mạnh nhất, ưu tiên làm):** ① **Hook mở đầu bằng phản ứng** (bắt đầu bằng cảnh khóc/hụt hơi trước khi cho bối cảnh) · ② **Hook mở đầu bằng cá nhân hóa** (trống → tên của họ xuất hiện) · ③ **Hook dựa trên dịp/thời hạn** ("Mother's Day còn 6 ngày và cần 5 ngày để làm").
**Tier 2 — chiến thuật chung phù hợp với các sản phẩm mua theo cảm xúc:** ④ POV/cảm xúc dễ đồng cảm · ⑤ Proof xã hội ("món quà khiến 10,000 bà nội khóc" — cold) · ⑥ Sự tò mò ("Tôi không nghĩ một chiếc cốc có thể khiến mẹ khóc") · ⑦ Mở đầu bằng nhân vật/mối quan hệ.
**Tier 3 — giảm thứ hạng (đối đầu với cảm xúc):** số liệu · đi ngược lại/gây tranh cãi · chỉ ra vấn đề (System-2/chức năng). Trước/sau sụp đổ vào hook chính.
> **Kết hợp Tier-1 + Tier-2** (mở đầu bằng phản ứng → sau đó mới lộ tên) — người có kinh nghiệm lưu ý "nhiều hook" sẽ hiệu quả hơn.

> ⚠️ **Thành thật:** bốn cách tùy chỉnh này là **giả thuyết dựa trên bằng chứng**, không phải là cải thiện đã được chứng minh — **không có dữ liệu A/B test nào tách biệt được chúng trong danh mục quà tặng cá nhân hóa.** Mức độ EXACT = hành vi thị trường/bản tóm tắt của người tạo (định tính); các con số được định lượng là RỘNG HƠN (POD/lễ) hoặc LẦN CUỐI CÙNG (khoa học quảng cáo toàn ngành). Hãy test, đừng giả định.

### POD tailoring — source rungs
- **EXACT (định tính):** Cẩm nang người bán Etsy (dịp lễ, xu hướng cá nhân hóa cao, "đĩa công thức" +110% YoY) · Marketing Dive (chiến dịch lễ hội "cảm thấy được nhìn thấy" của Etsy) · Hướng dẫn cá nhân hóa Etsy của Printify · Sale Samurai · GetNameNecklace (định vị tưởng niệm thú cưng trực tiếp) · Văn hóa phản ứng quà tặng trên TikTok + cuộc gọi của người tạo Kinfold Gifts · Góc độ quảng cáo tặng quà của Influee.
- **MỞ RỘNG:** Các góc độ quảng cáo quà tặng của The Performers (10 góc) · DesignRush (Ví dụ cá nhân hóa Ultimate Ears; completion >15s +38%; cá nhân hóa ≈ gấp 3 lần intent — áp dụng cho POD nói chung) · Cơ chế quảng cáo POD của Printful/Gelato/Prodigi/Justin Cener.
- **PHƯƠNG ÁN CUỐI CÙNG (cần lưu ý):** Bảng xếp hạng DTC của Fraser Cottrell (founder-ad S-tier là một tuyên bố *chung chung cho DTC*, không thể áp dụng cho trường hợp khác) · Lý thuyết UGC của Promer/Vlad Alexander/Sovran.

## 🎬 Mẫu brief sáng tạo (12 trường) — kết hợp với bảng framework kịch bản bên ngoài

*Thêm ngày 18/09/2026. Nguồn kết hợp: bảng "Kịch bản content phổ biến" bên ngoài (5 mẫu kịch bản ×
8 yếu tố tạo nên một creative chất lượng: Hook · Cốt truyện · Chuyển cảnh · Hình ảnh · Voice · Caption & Text · Proof · CTA),
so sánh với tài liệu này. **Đây là spec sản xuất; tài liệu này là hệ thống test.** Của họ thiếu
lớp đo lường; của mình thì chưa đủ chi tiết về craft. Họ là người tạo ra — phần hợp nhất bên dưới là kết quả.*

### Brief — mỗi test case cần điền đầy đủ 12 trường trước khi quay.
| # | Field | Who supplies it | Note |
|---|---|---|---|
| 1 | **Concept** | chiến lược | ý tưởng tổng thể, một câu |
| 2 | **Angle / Persona** ⭐ | chiến lược | *của chúng ta — bảng bên ngoài không có ô cho mục này.* Người mua ≠ người nhận quà; thay đổi persona trên cùng một sản phẩm là một bài test thực tế |
| 3 | **Hook** (0.5–3s) | chiến lược | text trên màn hình + cảnh quay mở đầu; Ưu tiên hook hướng đến gifting (tặng quà) |
| 4 | **Storyline / Body** | chiến lược | cấu trúc câu chuyện (A dựa trên phản ứng / B xây dựng cảm xúc / C kết hợp demo) |
| 5 | **Social-Proof beat** ⭐ | chiến lược | *được ưu tiên thành trường bắt buộc* — loại proof nào (xếp hạng 1–5) và **vị trí hiển thị** |
| 6 | **Offer** ⭐ | chiến lược | *của mình — không có trong bảng đối thủ.* Thiếu nó, một mẫu quảng cáo đẹp cũng có thể bán một cấu hình không có lời |
| 7 | **CTA** | chiến lược | dòng ngôn ngữ khuyến khích + lựa chọn một trong ~17 tùy chọn nút có sẵn của Meta |
| 8 | **Transitions / cut rate** | chỉnh sửa | **một con số** (1.5s / 5s / beat-matched / progress-paced), không phải là "cắt nhanh" |
| 9 | **Visual** | chỉnh sửa | nhiệt độ màu, background, khoảng cách camera |
| 10 | **Voice** ⭐ | chỉnh sửa | người nói, diễn biến giọng điệu, nhạc nền, hiệu ứng âm thanh/ASMR |
| 11 | **Caption & Text** | chỉnh sửa | kiểu chữ đè, font chữ, nội dung được làm nổi bật; luôn đảm bảo dễ đọc khi tắt âm thanh |
| 12 | **Length** ⭐ | chỉnh sửa | *của mình* — 6–15s Feed/Stories; 15–30s cho các concept cơ bản |

⭐ = Trường này không có trên bảng ngoài. Các trường 8–11 là những trường **nó** cung cấp mà trước đây chúng ta chưa có.
left to the editor's judgement.

### Adopted from the external table
- **① Voice** là một yếu tố brief riêng biệt. Trước đây, chúng ta gộp VO/music/sound vào một mục chung là "cross-cutting craft".
và chưa từng kê đơn nó. Bây giờ là một dòng trong bảng thành phần ở trên. Cái này dính ngay: một đoạn văn bản quá dài
Sản phẩm (ví dụ: tranh in chữ/thơ) không làm được reveal cá nhân hóa, nên các **concept** phải tập trung vào giọng đọc (VO) —
  và Voice chính là yếu tố quyết định cần thiết trong brief.
- **② Giá rẻ được tính theo số lượng, trên mỗi định dạng.** ~1.5s/cắt cho kiểu thuyết phục nhanh, so với ~5s/cắt cho UGC. Thể hiện rõ
  insight rằng **các định dạng chân thật cần cắt chậm hơn**. Quan trọng với những đối tượng có 60+ người tiếp cận, nơi mà cắt nhanh
  short-form pacing likely hurts.
- **③ Social Proof được ưu tiên lên thành yếu tố bắt buộc.** Thứ hạng proof của chúng tôi (số lượng reaction #1 · chi tiết cá nhân hóa
 #2 · Khối lượng/Thời lượng #3 · Ảnh UGC #4 · Quay cận cảnh sản phẩm #5) đã tồn tại nhưng bị ẩn trong phần thân video, nên dễ bị bỏ qua. Khi biến thành trường bắt buộc, nó sẽ buộc mọi video phải trả lời câu hỏi *"beat chứng minh là gì, và ở đâu?"
 - **④ Công thức "So sánh" như một thông số sản xuất** — chia đôi màn hình, cắt song song, zoom vào chi tiết khác biệt. Đây là thông số quay cho video so sánh chung vs. cá nhân hóa hiện tại của mình.
 
 
  hook; adopt verbatim.
- **⑤ BTS như một format mới** (đã thêm vào bảng format-fit ở trên, MEDIUM) — nhưng chỉ dùng cho giai đoạn 2/retargeting thôi.
  since craft proof is our rank #5.

### Loại bỏ — vì bảng bên ngoài mâu thuẫn với nghiên cứu này
| Their prescription | Why refused |
|---|---|
| **PAS / Problem-Solver như script #1** | PAS/AIDA kích hoạt hệ thống System-2 lý trí, chỉ hoạt động với những người đang tìm giải pháp; mua quà lại đi theo **cung bậc cảm xúc** (mong đợi → leo thang → hé lộ + phản ứng). Thông số hình ảnh càng làm tình hình tệ hơn: *màu tối cho vấn đề, chữ gây đau đớn màu đỏ/vàng* — hoàn toàn ngược lại với vẻ ngoài của một món quà kỷ niệm. "Nhấn mạnh vấn đề" đã là **Tier 3** trong bảng xếp hạng hook của chúng ta. **Bỏ qua cho các sản phẩm quà tặng.** |
| **Social proof = số đơn hàng + ảnh chụp màn hình bình luận khen ngợi + số liệu trước/sau** | Đây không phải proof phù hợp với khách hàng này. Proof #1 của chúng ta là **phản ứng chân thật của người nhận**; proof về số lượng đơn hàng là #3 và chỉ dùng cho mục đích chứng minh tính hợp pháp ban đầu. Việc chồng chất ảnh chụp màn hình bình luận trông giống như dropship đối với người dùng Meta ở Mỹ trong độ tuổi 50–60. |
| **"Trending AI voice"** (được đề xuất trong UGC + so sánh các dòng) | Chống lại điểm yếu lớn nhất của ngành — giọng người thật bị méo mó. Ưu tiên sử dụng voice thật. |
| **CTA tạo FOMO/khẩn cấp mạnh** (trong dòng UGC của họ) | Thứ hạng offer của chúng ta cho thấy **hạn chót đặt hàng** đứng #1 về mức độ khẩn cấp, còn *áp dụng giảm giá/tạo áp lực FOMO* lại xếp cuối — điều này làm giảm giá trị kỷ niệm. Hạn chót ≠ FOMO. |
| **Hướng dẫn đặt hàng ở giữa video** (trong storyline Unboxing của họ) | Chúng ta đặt **phần reveal vào giữa video** để còn thời lượng cho phản ứng của khách hàng, đồng thời giữ chân người xem ở thời điểm retention cao nhất. |
| **Cột CTA như một mục tiêu cảm xúc** ("tác động vào cảm xúc") | Không thể giao việc cụ thể. Yêu cầu của chúng ta phải chỉ rõ dòng chữ cụ thể + preset nút Meta. |

> ⚠️ Chú ý về nguồn gốc: bảng này là của **TikTok / dropship**. Khách hàng của chúng ta là người dùng Meta tại Mỹ, thường xuyên
> 55 tuổi trở lên, mua những món quà lưu niệm mang ý nghĩa cảm xúc. Cháu nên học hỏi cách họ làm *sản phẩm*; đừng bê nguyên *cách thuyết phục* của họ.

### 5 kịch bản của họ, được ánh xạ vào đánh giá phù hợp với format của mình
| Kịch bản của họ | Ánh xạ vào format của mình | Đánh giá |
|---|---|---|
| **Unboxing Review** | Phản ứng khi nhận quà (CAO) + Mở hộp (CAO VỪA) | **Giữ lại — định dạng hàng đầu.** ≈ Sử dụng khung A (dẫn dắt bởi phản ứng). Chú trọng chuyển cảnh theo nhạc + tông ấm; chèn hướng dẫn đặt hàng giữa video |
| **UGC** | UGC thô (CAO) | **Giữ lại.** Cắt 5s/clip + phụ đề từng chữ + quay bằng điện thoại. Loại bỏ giọng AI, thêm proof số lượng đơn hàng, CTA tạo cảm giác FOMO |
| **Compare** | Thể hiện cá nhân hóa vượt trội (CAO) | **Giữ lại.** Công thức chia đôi màn hình/zoom có thể áp dụng trực tiếp cho các concept so sánh chung vs. cá nhân hóa |
| **BTS** | *(thiếu trong các video của mình — đã thêm, VỪA)* | **Áp dụng, Giai đoạn 2 / chỉ dùng cho retargeting** |
| **Problem-Solver (PAS)** | vấn đề cần giải quyết = nhóm **Tier 3** của chúng ta | **Drop** cho các sản phẩm quà tặng |

### Những hạn chế của bảng bên ngoài (tại sao bảng này vẫn là nguồn dữ liệu chính xác)
Không có trường offer · không có trường angle/persona · không có đánh giá độ phù hợp với format (hiện tại nó coi 5 script là ngang nhau, trong khi chúng ta đánh giá 15 cái và loại bỏ 2 cái khó) · không có phân loại theo giai đoạn nhận biết · không có quy định về length · **và hoàn toàn không có lớp đo lường** —

Không có hook rate, hold rate, sample gate, hay kill line. Nó chỉ cho bạn biết *cần làm gì*; chỉ có Phần D của
`TESTING-MATRIX-FRAMEWORK.md` mới nói cho bạn biết *cần loại bỏ gì*.

## Honesty notes
- **Số liệu thực tế:** Meta/Nielsen 47%-trong-3 giây + 65%/45% tỷ lệ xem hết [Meta chính]; tắt âm ~80–85% [Meta]; creative của Google ≈ 50% ROI.
- **Chỉ số từ người làm thực tế (các vendor có xu hướng đồng thuận nhưng tự báo cáo):** hook 25–35% / hold 40–50% — đây là quy ước, không phải tiêu chuẩn (mẫu số khác nhau → phạm vi 20–45% tồn tại).
- **Quan điểm chung:** Sự chuyển đổi từ OFAT sang đa dạng hóa Andromeda và tất cả các con số về volume (8–12 concepts, 50–100/tháng, 3×3, 10–20 hooks, 90/10). Câu nói của Meta-VP về việc "4× sáng tạo hơn" là một paraphrase gián tiếp – mang tính định hướng.

### Source URLs
motionapp.com/blog/key-creative-performance-metrics · help.motionapp.com/en/articles/8991407 (Hook/Watch/Click/Convert) · help.motionapp.com/en/articles/12461770 (AI-tagging) · creads.io/ad-creative-performance-guide · sovran.ai/blog/hook-body-cta-video-ad-structure · adlibrary.com/posts/hook-rate · adlibrary.com/posts/hold-rate · facebook.com/business/news/updated-features-for-video-ads (47% data) · facebook.com/business/help/188534925073536 · triplewhale.com/blog/facebook-ad-analytics · growwithsakib.com/meta-ads-creative-testing (Segwise/Andromeda) · admanage.ai/blog/how-many-ad-creatives-to-test · motionapp.com/blog/best-dtc-meta-ad-hooks-2025 (Savannah Sanchez) · buildingadswithbarry.com (Barry Hott) · Dara Denney (Point Guard Media, LinkedIn/YouTube)
