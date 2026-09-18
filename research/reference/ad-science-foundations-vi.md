# Nền tảng khoa học cho quảng cáo — tâm lý học, khoa học marketing và hệ thống test dựa trên power

> 🇬🇧 Bản gốc tiếng Anh: [[ad-science-foundations]] — bản gốc là nguồn chuẩn.

Nghiên cứu 2026-09-18. **Vì sao có tài liệu này:** bóc tách Macorner/Wander Prints chỉ cho biết *họ* đã dừng
lại ở đâu. Đó là **một điểm tối ưu cục bộ, và là cái trần** — copy thì giỏi lắm là hoà. Tài liệu này là tầng
nguyên lý gốc: tâm lý học về sự chú ý, về tính liên quan tới bản thân, về **hành vi tặng quà**, nền bằng chứng
của khoa học marketing, và quan trọng nhất — **với ngân sách của mình thì thống kê cho phép học được cái gì.**
Bóc tách đối thủ trở thành *tham chiếu*, không phải nguồn chân lý.

**[GỐC]** = nghiên cứu bình duyệt · **[NỀN BẰNG CHỨNG]** = phân tích tổng hợp quy mô lớn của ngành · **[Ý KIẾN]**.

> **Phát hiện quan trọng nhất:** với ngân sách hiện tại, **so sánh tỷ lệ mua giữa hai creative tốn ~$1.315**
> để đạt power 80%. Cả Giai đoạn 1 của mình là **$360**. Nhưng **so sánh hook rate chỉ tốn ~$21.** Vậy nên
> chính thống kê — chứ không phải sở thích — quyết định chỗ nào được chạy thí nghiệm, chỗ nào chỉ được đặt lan
> can an toàn. Xem §5 — nó lật ngược khung hiện tại của mình.

---

## 1. Sự chú ý — cái gì thật sự kéo và giữ được nó

**① Chuyển động BẮT ĐẦU ăn đứt chuyển động đều. Điều này sửa lại lời khuyên trước đó của chính tôi.**
Tế bào hạch võng mạc phát tín hiệu báo động khi chuyển động *khởi phát*; "chuyển động khởi phát kéo chú ý rất
mạnh và **nổi bật hơn chuyển động mượt đều**" `[GỐC: pmcid:PMC3711149]`. Mô hình saliency cho cảnh động tái
lập đúng hiện tượng **bất đối xứng này** `[GỐC: pmid:23314730]`.
- **Hệ quả:** mục tiêu *không phải* "nhiều chuyển động hơn". Trôi mượt liên tục — đúng cái clip của mình đang
  làm — lại là loại chuyển động **ít** nổi bật nhất. Đơn vị gây chú ý là một cú **đứng yên → bật động đột ngột**.
- **Điều này đổi `motion_qa.py`:** chuyển động trung bình là chỉ số sai. Cần đếm **sự kiện khởi phát** (đạo hàm —
  bao nhiêu lần chuyển động nhảy từ gần 0 lên cao), không phải mức trung bình.

**② Tính mới và tính nổi bật là hai thứ khác nhau và cạnh tranh nhau** `[GỐC: pmid:32088400]`. Một khung hình
"nổi bật" chưa chắc là khung hình *mới*. Trong một newsfeed toàn creative quà tặng bóng bẩy, nước đi mới có khi
lại là khung hình *không* bóng bẩy.

**③ Sự chú ý bị kéo không phải là vô điều kiện.** Nó bị điều tiết bởi nhiệm vụ đang làm, xác suất xuất hiện và
nguồn lực còn lại `[GỐC: pmid:20377287, pmcid:PMC2668614]`. Việc kéo chú ý còn có **một bước đánh giá** để quyết
xem có đáng phản ứng không `[PMC4099520]` — nên một cú phá mạch kéo được mắt nhưng phát tín hiệu "quảng cáo vô
quan" là tiêu tiền vô ích. **Phải phá mạch + liên quan ngay, không thì mất trắng.**

**④ Ngưỡng chú ý–ghi nhớ: ~2,5 giây.** Cần khoảng 2,5 giây *chú ý thật* thì mới có cơ hội tác động tới trí nhớ,
và **~85% quảng cáo số không bao giờ đạt tới đó** `[NỀN BẰNG CHỨNG: Nelson-Field / System1]`. Liên quan:
**chưa tới một phần tư thời gian "hiển thị được" là chú ý thật**, và mỗi nền tảng có một **trần chú ý** giới hạn
kết quả *bất kể creative hay tới đâu*.
- **Hệ quả:** đích thật của mình không phải "được xem" mà là **≥2,5 giây chú ý**. Nó cũng có nghĩa một phần kết
  quả do nền tảng quyết định chứ không phải mình — nên chỉ chấm creative *tương đối trong cùng một nền tảng*.

---

## 2. Tính liên quan tới bản thân và cá nhân hoá — vì sao nó chạy, và giới hạn thật của nó

Cá nhân hoá là toàn bộ sản phẩm của mình, nên cơ chế của nó rất đáng quan tâm — và tài liệu khoa học khắt khe
hơn nhiều so với lời đồn trong ngành marketing.

**Cái đúng:** tên riêng của một người tạo ra **sóng N250 trên điện não, phản ánh việc bị kéo chú ý**
`[GỐC: pmid:21256923]`. Người ta **ước lượng thời lượng dài hơn** khi nhìn tên mình — kích thích liên quan tới
bản thân được xử lý lâu hơn `[GỐC: pmid:31707077]`. Mã hoá theo hướng tự quy chiếu tạo lợi thế ghi nhớ rõ rệt
`[GỐC: pmid:38963906]`.

**Cái KHÔNG đúng — ba phản chứng phải tôn trọng:**
- Hiệu ứng chú ý của tên riêng **chỉ tạm thời và có điều kiện**, chỉ xuất hiện khi còn đủ nguồn lực
  `[GỐC: pmid:18413272]`; lợi thế nhận diện mặt mình **không** đến từ việc bị kéo chú ý tự động `[GỐC: PMC4206440]`.
- Lợi thế đó đòi hỏi **ý thức nhận ra** manh mối liên quan tới bản thân `[GỐC: pmid:30218945]`.
- **Quyết định nhất:** "**Chỉ trưng tên một người bên cạnh vật thể là KHÔNG ĐỦ** để tạo lợi thế ghi nhớ… vai trò
  then chốt thuộc về **xử lý quan hệ**" `[GỐC: pmcid:PMC6368470]`.

**Suy luận làm đổi creative — và nó không hiển nhiên.** Trong ads của mình, người lướt là **người tặng**; cái tên
trên sản phẩm là của **người nhận**. Nên hiệu ứng *tự quy chiếu* không hề áp dụng cho người xem. Chớp tên một
người lạ ("MARGARET") chẳng được gì — và ngay cả với người nhận, chỉ một cái tên cũng không đủ nếu thiếu xử lý
quan hệ. Cái mình có thể kích hoạt là **xử lý quan hệ với người thân cận**: ads phải khiến người xem *liên hệ
món đồ đó với đúng người của họ.*
- **Vậy nên: gọi MỐI QUAN HỆ, đừng hiện cái TÊN.** "Tên bà của bạn in trên đó" / "dành cho bà hay bảo đừng mua
  gì cho bà" làm được việc mà một cái tên hiện lên không làm được.
- Điều này cho ra một phép so sánh **kiểm chứng được**: *hiện tên* đấu với *gọi mối quan hệ*. Một phép test
  hook cho cặp này tốn ~$21 (§5). **Đây là thí nghiệm đáng giá nhất để chạy đầu tiên.**

---

## 3. Tâm lý học tặng quà — tầng riêng biệt nhất và bị bỏ quên nhất

Đây là một dòng nghiên cứu thật, nói đúng về giao dịch của mình, và chưa có gì trong repo dùng tới nó.

**① Giả thuyết "tìm nụ cười" — định nghĩa lại hoàn toàn cảnh phản ứng.** Người tặng "thường không chọn đúng thứ
người nhận muốn nhất"; họ được thúc đẩy và được tưởng thưởng bởi **phản ứng cảm xúc tức thì** của người nhận
(nụ cười ngay lúc mở quà), tách biệt với mức hài lòng tổng thể `[GỐC: pmid:29920154]`.
- **Hệ quả:** cảnh phản ứng **không phải "bằng chứng xã hội".** Nụ cười được hình dung trước **chính là thứ người
  tặng đang mua.** Bảng xếp hạng bằng chứng của mình để "phản ứng thật của người nhận" ở hạng 1 là đúng kết quả
  nhưng sai lý do — nó không phải bằng chứng, nó là **lợi ích**. Nghĩa là cảnh phản ứng thuộc về **hook**, không
  phải một nhịp bằng chứng ở giây thứ 20.

**② Lệch giữa người tặng và người nhận là có hệ thống.** Người tặng thiên về món độc đáo nhưng nhỏ; người nhận
thích món ít sang hơn nhưng **dùng được** `[GỐC: pmid:15901395]`. Người tặng **đánh giá thấp** mức độ người nhận
thấy một món quà "chưa trọn vẹn nhưng đúng ý" là chu đáo `[GỐC: pmid:28914152]`.
- **Hệ quả:** mình bán cho **người tặng**, nên phải bán theo tiêu chí quyết định của người tặng — sự chu đáo,
  độc nhất, "bằng chứng bạn để tâm" — **chứ không phải** tính hữu dụng với người nhận. Điều này chứng minh bằng
  cơ chế cho góc "được để ý", và cảnh báo không nên dẫn bằng chất lượng/công năng với tệp lạnh.

**③ "Của cho không bằng cách cho" là có điều kiện.** Tâm ý của người tặng chỉ làm người nhận trân trọng hơn
**khi người nhận được gợi để nghĩ tới tâm ý đó** `[GỐC: pmid:22774790]`.
- **Hệ quả:** một món kỷ vật cá nhân hoá chính là **tâm ý được vật chất hoá và không thể phớt lờ** — nó cung cấp
  đúng cái gợi ý mà nghiên cứu nói là bắt buộc. Đây là lập luận khoa học mạnh nhất cho chính ngành hàng này, và
  là lý do nên cho thấy *hành động chọn* (chọn tên), chứ không chỉ kết quả.

**④ Sự gần gũi mới là thứ được giao.** Món quà khả thi (so với món xa xỉ) làm người nhận thấy **gần gũi hơn về
tâm lý** với người tặng `[GỐC: pmid:30027819]`.

**⑤ Một tín hiệu phân khúc.** Quà lấy người nhận làm trung tâm — nêu đích danh cả **"cá nhân hoá bằng tên người
nhận"** — ít nói về người tặng hơn và **ít tạo gần gũi hơn** với người tặng có tính ái kỷ, nên nhóm này né
`[GỐC: pmid:39425564]`.
- **Hệ quả:** người mua của mình nghiêng về **coi trọng mối quan hệ, ít ái kỷ**. Các cách đóng khung kiểu khoe
  địa vị ("thành đứa con được cưng nhất") có thể đang hút nhầm người mua. Cái này kiểm chứng được.

---

## 4. Khoa học marketing — cái gì khái quát được ra ngoài một ngách

- **Tăng trưởng đến từ mở rộng tệp mua, không phải lòng trung thành; người mua nhẹ mới là nhóm quan trọng nhất**
  `[NỀN BẰNG CHỨNG: Ehrenberg-Bass]`. Với mình: ưu tiên phủ rộng hơn là dồn vào retarget.
- **Mental availability = độ rộng và sâu của liên kết trí nhớ, dựng trên các Điểm Vào Ngành hàng (CEP)** — những
  manh mối (tâm trạng, sự kiện, nhu cầu, thời điểm) khiến người ta nghĩ tới ngành hàng `[NỀN BẰNG CHỨNG]`.
  **Điều này định nghĩa lại thư viện 12 góc của mình:** với một shop quà tặng, CEP *chính là* **dịp × mối quan hệ
  × biến cố đời người** ("Ngày của Mẹ", "sinh nhật 80 của bà", "chó nhà mình vừa mất"). Nên viết các góc dưới dạng
  CEP để mỗi góc là một manh mối gợi nhớ mình sở hữu.
- **Tài sản thương hiệu đặc trưng** là cấu trúc trí nhớ và sẽ **mai một nếu không được nhắc lại** `[NỀN BẰNG CHỨNG]`.
  Hiện mình gần như chỉ có một thứ (logo end-card) — mà §0 của tài liệu Ad Video Director cho thấy nó chạy thành
  3 giây đứng hình bằng 0. Tệ hơn là không có.
- **Nhân vật/thiết bị lặp lại (fluent device) cho kết quả vượt trội** về thị phần và lợi nhuận `[NỀN BẰNG CHỨNG: System1/WARC]`.
  Một nhân vật lặp lại xuyên các phim là đòn bẩy thật, rẻ, mà mình chưa dùng.
- **Quảng cáo tác động qua liên tưởng và cảm xúc nhiều hơn là qua thuyết phục** `[NỀN BẰNG CHỨNG: Binet & Field;
  Feldwick & Heath]` — đây là chỗ dựa bằng chứng cho quyết định chọn mạch cảm xúc thay vì PAS.

---

## 5. ⭐ Hệ thống test — dựa trên power, vì kinh tế của việc đo lường rất phũ

### 5a. Bằng chứng bên ngoài
Lewis & Rao, **QJE 2015**, 25 thí nghiệm thực địa lớn, $2,8 triệu chi phí, đa số phủ hàng triệu người `[GỐC]`:
- **Khoảng tin cậy trung vị của ROI rộng hơn 100 điểm phần trăm.**
- Doanh số ở mức cá nhân biến động cực mạnh — **hệ số biến thiên ≈ 10** là bình thường.
- Thí nghiệm đủ thông tin "dễ dàng cần tới **hơn 10 triệu người-tuần**".
- Chỉ **3 trong 25** thí nghiệm đủ power để phân biệt một ROI *bom tấn* 50% với 0%; cái trung vị phải lớn gấp
  **9 lần**. "Phân biệt ROI 50% với 0% một cách đáng tin thường là **không làm được với một thí nghiệm $100.000
  trên hàng triệu người.**"
- **Thiên lệch chọn lọc do phân phối nhắm mục tiêu là "mối lo chí mạng" cho các phương pháp quan sát** — được
  Gordon, Zettelmeyer, Bhargava & Chapsky (*Marketing Science* 2019) trên dữ liệu Facebook xác nhận lại.

### 5b. Với NGÂN SÁCH CỦA MÌNH thì nghĩa là gì — tính ra, không phán bừa
Kiểm định hai tỷ lệ, α=0,05 hai phía, **power 80%**, theo đúng giả định PAR của mình (CPM $13, CPC $0,50):

| Phép so sánh | n mỗi nhánh | đơn vị | **Chi phí cả hai nhánh** | Kết luận |
|---|---|---|---|---|
| Hold rate 12% → 30% | 76 | lượt hiển thị | **$2** | ✅ không đáng kể |
| Hook rate 22% → 28% | 814 | lượt hiển thị | **$21** | ✅ **chạy cái này** |
| Link CTR 1,2% → 2,5% | 1.683 | lượt hiển thị | **$44** | ✅ kham được |
| Hook rate 25% → 28% (3 điểm) | 3.393 | lượt hiển thị | **$88** | ✅ kham được |
| Link CTR 2,0% → 2,5% | 13.806 | lượt hiển thị | **$359** | ⚠️ = cả ngân sách |
| Tỷ lệ add-to-cart 4,6% → 7,5% | 1.057 | click | **$1.057** | ❌ không kham nổi |
| **Tỷ lệ mua 1,4% → 3,0%** | 1.315 | click | **$1.315** | ❌ **gấp 3,7 lần cả ngân sách** |
| Tỷ lệ mua 2,0% → 2,5% | 13.806 | click | **$13.806** | ❌ khỏi bàn |

### 5c. Hệ quả — nó LẬT NGƯỢC khung của mình
`TESTING-MATRIX-FRAMEWORK.md` Phần B.1 nói Giai đoạn 1 là "bộ lọc yếu… quyết định thật nằm ở Giai đoạn 2–3".
**Thống kê nói ngược lại.** Giai đoạn 1 là giai đoạn *duy nhất* mình đủ tiền chạy một thí nghiệm đúng power;
so sánh ở Giai đoạn 2–3 tốn gấp 3–40 lần ngân sách. Vậy:

| Bậc | Chỉ số | Tình trạng với ngân sách này | Xử lý thế nào |
|---|---|---|---|
| **A — Thí nghiệm** | hook rate, hold rate, link CTR thô | **Đủ power với $2–$90** | Khoa học thật. Ghi giả thuyết trước, một biến, báo cáo cả hiệu ứng lẫn khoảng tin cậy. **Đây là chỗ mình học được.** |
| **B — Tín hiệu yếu** | phân biệt CTR tinh, tỷ lệ add-to-cart | $350–$1.100 — nhiều lắm mỗi quý một lần | Chỉ định hướng. Không bao giờ tắt dựa trên một lần đọc. |
| **C — Lan can, KHÔNG phải test** | CPA, ROAS, tỷ lệ click→mua | $1.300–$13.800 mỗi phép so sánh | **Không bao giờ so creative ở đây.** Chỉ dùng như một mốc kinh tế tuyệt đối so với điểm hoà vốn. Một "mẫu thắng" theo ROAS ở mức chi $66 là nhiễu. |

**Việc chấm CPA/ROAS theo 5 bậc ở mức chi $47–66 là vô nghĩa về mặt thống kê nếu dùng để so sánh.** Nó vẫn là
một *lan can* hợp lệ (có vượt điểm hoà vốn không? dừng). Tài liệu phải nói rõ nó đang làm cái nào.

### 5d. Tính hợp lệ nội tại — lỗ hổng nằm ngay trong phương pháp của mình
Cơ chế phân phối của Meta **giao tệp khác nhau cho các ad khác nhau**. Nên nhét nhiều ad vào một nhóm quảng cáo
**không phải thí nghiệm ngẫu nhiên** — nó đúng là loại thiên lệch chọn lọc mà Lewis & Rao gọi là chí mạng. Câu
"gom vài cái một nhóm rồi để phân phối tự lọc" là *mua quảng cáo* giỏi nhưng **suy luận sai**.
- **Cách sửa, theo thứ tự chặt chẽ:** (1) dùng **công cụ A/B Test** của Meta (chia người ngẫu nhiên) cho mọi
  khẳng định bậc A; (2) một creative một nhóm quảng cáo, ngân sách và lịch chạy như nhau; (3) đo lift/holdout cho
  bất cứ thứ gì thuộc bậc C, chấp nhận rằng ở mức chi của mình nó sẽ thiếu power.
- **Giữ nhóm gộp để scale. Đừng bao giờ đọc kết luận nhân quả từ đó.**

### 5e. Kỷ luật thí nghiệm (rẻ, và chính nó làm cho cái này thành khoa học)
1. **Ghi trước khi bật:** giả thuyết, cơ chế lấy từ §1–§4, biến thay đổi, chỉ số chính, ngưỡng cỡ mẫu, quy tắc quyết định. Không đổi chỉ số sau khi đã thấy số liệu.
2. **Mỗi test bậc A chỉ đổi một thứ.** Loạt concept đa dạng là *khám phá* (sinh giả thuyết); nó không phải test và không được báo cáo như test.
3. **Không xem giữa chừng.** Nhìn số liệu liên tục sẽ thổi phồng dương tính giả. Chốt cỡ mẫu trước; các mốc T0 là *phanh an toàn*, không phải kiểm định ý nghĩa.
4. **Đếm số phép so sánh.** 18 ads so từng cặp = 153 phép; ở α=0,05 thì ~8 "mẫu thắng" thuần do may rủi. So với **một mốc chuẩn đã đặt tên trước**, không phải tất-cả-với-tất-cả.
5. **Báo cáo cả độ lớn hiệu ứng và khoảng tin cậy**, không bao giờ chỉ nói ai thắng. Với Lewis & Rao thì khoảng tin cậy mới là phát hiện.
6. **Ghi lại mọi kết quả — kể cả kết quả rỗng.** Cơ sở dữ liệu nội bộ tích luỹ dần là nguồn duy nhất *đúng* ngách của mình; tài liệu công bố thì không bao giờ đúng ngách.

---

## 6. Những chỗ buộc phải sửa trong các tài liệu hiện có
| Tài liệu | Sửa gì |
|---|---|
| `research/scripts/motion_qa.py` | Thêm chỉ số **khởi phát chuyển động** (đếm cú nhảy), không chỉ mức trung bình — §1①. Mức trung bình cho điểm quá cao cho kiểu trôi mượt, vốn là loại ít nổi bật nhất. |
| `ad-video-director-research.md` | Đích của hook thành **≥2,5 giây chú ý** và **có một sự kiện khởi phát ngay khung hình đầu**, không phải "chuyển động trung bình cao". Đưa cảnh phản ứng vào **hook** (§3①). |
| `video-ad-decomposition-2026.md` | Bảng bằng chứng: phản ứng của người nhận là **lợi ích, không phải bằng chứng** (§3①). Thư viện góc → viết lại thành **CEP** (§4). Hook cá nhân hoá → **gọi mối quan hệ, không hiện tên** (§2). |
| `TESTING-MATRIX-FRAMEWORK.md` | Thêm **thang power** (§5b–c): GĐ1 = thí nghiệm, GĐ2 = tín hiệu yếu, GĐ3 = lan can. Ghi rõ các bậc CPA/ROAS là lan can chứ không phải phép so sánh. Thêm **lỗ hổng phân phối** (§5d). |
| `PHASE1-TOURNAMENT-3-products.md` | Giải đấu được phép xếp hạng theo **hook/hold/CTR** (bậc A). **Không được** xếp hạng sản phẩm theo ROAS ở mức chi $47–66. |

## 7. Trung thực và giới hạn
- **Rủi ro lớn nhất là chuyển giao.** §1–§3 là kết quả phòng thí nghiệm (điện não, theo dõi mắt, tình huống chọn quà). Không cái nào chạy trên video Meta cho quà tặng cá nhân hoá. Chúng tạo ra **giả thuyết mạnh, có cơ chế**, không phải bảo đảm. Mọi cái đều phải qua thang bậc A ở §5.
- **§4 là phân tích tổng hợp của ngành, không phải bình duyệt** — mẫu lớn và lặp lại được, nhưng phần lớn là dữ liệu độc quyền (IPA, System1, Ehrenberg-Bass) mà mình không kiểm tra được.
- **Lewis & Rao nói về đo ROI ở quy mô lớn.** Các chỉ số tương tác bậc A của mình rẻ hơn hẳn để đo, chính vì chúng có tần suất cao và ít biến động. Sự bi quan của họ áp cho **bậc C**; nó **không** có nghĩa là mình không học được gì.
- **Bảng power giả định** CPM $13, CPC $0,50, các quan sát độc lập và không có lỗ hổng phân phối. Phân phối thật thì có phân cụm và không ngẫu nhiên, nên hãy coi mọi con số là **cận dưới**.
- **Hai tóm tắt nghiên cứu đi ngược cách hiểu ngây thơ về chính kế hoạch của mình** (§2 xử lý quan hệ; §3⑤ ái kỷ / quà lấy người nhận làm trung tâm). Cả hai đều mới đọc ở phần tóm tắt, chưa đọc toàn văn. Đã gắn cờ chứ chưa hành động.
