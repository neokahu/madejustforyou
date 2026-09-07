# Playbook Facebook Ads — Cấu trúc / Tắt / Scale

Bộ quy tắc vận hành quảng cáo Facebook/Meta cho e-commerce (đặc biệt store/pixel mới).
Nguyên tắc xuyên suốt: **quyết định dựa trên dữ liệu đã chốt, so với điểm hòa vốn (break-even), và đúng giai đoạn.**

## 0. Nền tảng (đọc trước)

- **Break-even CPA** = Giá bán − tổng chi phí biến đổi mỗi đơn (giá vốn/in ấn + phí ship + phí sàn/thanh toán) ≈ lợi nhuận gộp mỗi đơn. Mọi quyết định tắt/scale đều so với con số này.
- **Learning phase:** Meta cần ~**50 sự kiện tối ưu / ad set / tuần** để tối ưu ổn định; mỗi lần sửa lớn (ngân sách, creative, audience, đối tượng) **reset learning** → phải học lại. *(Meta Business Help)*
- **Số liệu trong ngày là ước tính** (phồng lên trong ngày rồi lắng xuống) → chỉ ra quyết định trên **ngày đã chốt**.
- **Chỉ số dẫn (leading) trước, chỉ số trễ (lagging) sau:** đọc hook/ThruPlay → CTR → CPC → cost-per-event trước; đơn hàng cần thời gian + đủ mẫu mới đánh giá được.

## 1. Cấu trúc chiến dịch (Campaign structure)

**1.1 Thang sự kiện tối ưu — pixel/trang mới:** `Traffic/LPV → ViewContent → Add to Cart → Purchase`. Bắt đầu ở sự kiện rẻ & nhiều dữ liệu, leo lên khi rung đủ ~50 sự kiện/tuần ở bậc hiện tại. **Không bắt đầu bằng Purchase trên pixel mới** — pixel chưa có tín hiệu mua, Meta phân phối vào nhóm quá hẹp → CPM rất cao, đốt tiền mà không đủ mẫu. *(Modern Marketing Institute; Stackmatix; Influee; Shopify Community)*

**1.2 Giai đoạn TEST — dùng ABO (ngân sách ở cấp ad set):**
- Mỗi **creative một ad set riêng**, ngân sách bằng nhau. Nhồi nhiều creative vào 1 ad set → Meta dồn tiền vào cái nó "đoán" tốt, không luân phiên → không test công bằng được.
- Audience **broad** (rộng), để thuật toán tự tìm; chọn quốc gia + độ tuổi phù hợp.
- Ngân sách test đủ để đạt mẫu; tránh chạy nhiều ad set gần giống nhau (tự cạnh tranh trong đấu giá).

**1.3 Giai đoạn SCALE — dùng CBO (ngân sách ở cấp chiến dịch):** khi đã có creative + audience thắng → gom winner vào chiến dịch **CBO** để thuật toán phân bổ ngân sách. *(Consensus media-buyer: ABO để test → CBO để scale)*

**1.4 Creative:** ưu tiên nội dung **liên quan trực tiếp sản phẩm** (product-first) hơn nội dung chỉ "bắt mắt". Nội dung câu view nhưng lệch sản phẩm thường kéo sai đối tượng → lead kém chất lượng, không chuyển đổi.

**1.5 Kỷ luật:** 1 pixel / 1 trang; audience broad; **tối thiểu chỉnh sửa**; kiên nhẫn qua learning phase.

## 2. Quy tắc TẮT quảng cáo (Kill)

Trước khi tắt, soi đúng **(1) sự kiện tối ưu · (2) giai đoạn · (3) tầng vấn đề** — sai một trong ba là tắt nhầm quảng cáo tốt.

| Tình huống | Hành động |
|---|---|
| CTR (link) < ~1.5–2% hoặc hook/ThruPlay quá thấp | Tắt/đổi **creative** (vấn đề nội dung) |
| cost-per-event vượt ~**3–4× mức tốt đã quan sát** | Tắt **creative/ad set** |
| Đã chi < ~2–3× break-even CPA, chưa có đơn | **KHÔNG tắt** — chưa đủ mẫu, không phải creative kém |
| Đã chi ~2–3× break-even CPA + đủ lượt checkout, vẫn 0 đơn | Vấn đề ở **on-site** (giỏ→checkout) → sửa web, **không** tắt ad |
| Đang trong learning phase, số xấu | **KHÔNG sửa/tắt** — chờ hết learning (sửa = reset) |
| Ad set thua rõ sau đủ chi tiêu (CPA ≫ break-even, không cải thiện) | Tắt, dồn ngân sách cho winner |

**Nguyên tắc vàng:** đầu phễu tốt (CTR/ATC ổn) nhưng không ra đơn thường là lỗi **on-site** (giỏ→thanh toán), không phải lỗi quảng cáo → sửa website, đừng tắt creative tốt.

## 3. Quy tắc SCALE (nhân rộng)

**Điều kiện được scale (đủ cả 3):** ad set đã **thoát learning** + **CPA ≤ break-even** (có lãi) + **ổn định ≥ 3–4 ngày**.

**3.1 Scale dọc (tăng ngân sách):** tăng ngân sách ad set winner **~20–30% mỗi 3–4 ngày**. Tăng đột ngột > ~30% có thể **reset learning** → mất ổn định. *(Consensus media-buyer, dựa trên cơ chế learning phase của Meta)*

**3.2 Scale ngang (nhân bản):** nhân winner sang **audience mới / creative mới** ở ad set riêng; hoặc chuyển winner vào **CBO** gom nhiều winner.

**3.3 Giữ winner:** **không** sửa creative/audience của ad set đang lãi. Muốn thử cái mới → mở ad set test riêng, đừng đụng winner.

**3.4 Leo thang khi scale:** khi volume đủ, feed sự kiện sâu hơn (ATC → Purchase) để thuật toán tối ưu đúng người mua thật.

**3.5 Theo dõi frequency:** freq tăng cao + CPA xấu đi = "cháy" creative → **làm mới creative** (đổi góc/hook), không cố tăng ngân sách.

## 4. Checklist nhanh (vòng lặp)

1. **Cấu trúc:** ABO test, mỗi creative 1 ad set, audience broad, đúng bậc thang sự kiện.
2. **Đọc:** chỉ số dẫn trên ngày đã chốt (hook/CTR/CPC/cost-per-event).
3. **Tắt** cái thua theo bảng mục 2; **giữ** cái thắng.
4. **Scale** winner +20–30%/3–4 ngày (dọc) hoặc nhân bản/CBO (ngang).
5. **Leo thang** sự kiện khi đủ ~50/tuần; **làm mới creative** khi frequency cao / CPA xấu.
6. Đầu phễu tốt mà không ra đơn → **sửa on-site**, không tắt ad.

## 5. Cơ sở nghiên cứu (nguồn)

- **Meta Business Help — About the Learning Phase** *(chính chủ):* ~50 sự kiện tối ưu/ad set/tuần; chỉnh sửa lớn reset learning. facebook.com/business/help/112167992830700
- **Modern Marketing Institute — "How to Exit the Meta Ads Learning Phase Fast":** Optimization-Event Ladder — chọn sự kiện mà volume đủ nuôi, leo dần theo thời gian.
- **Shopify Community — pixel mới không có dữ liệu mua:** với vài chục lượt truy cập bạn chưa có "vấn đề chuyển đổi", mà là **chưa đủ mẫu** → chạy Traffic trước.
- **Influee — Meta Campaign Objectives:** mục tiêu Sales chỉ tối ưu tốt khi pixel đang bắn sự kiện Purchase; nếu chưa, chạy **Traffic** một thời gian.
- **Stackmatix — Meta Ads Funnel Strategy:** store mới dùng traffic/video-view để xây tệp warm; ưu tiên sự kiện pixel ViewContent → AddToCart → InitiateCheckout → Purchase.
- **Consensus media-buyer (ABO→CBO, scale 20–30%/3–4 ngày):** thông lệ ngành, suy ra từ cơ chế learning phase của Meta ở trên — không phải quy tắc "chính chủ", điều chỉnh theo dữ liệu thực tế của tài khoản.
- Tài liệu nội bộ liên quan: `AD-KILL-RULES.md`, `research/reference/new-pixel-coldstart-methodology.md`.

*Lưu ý: các con số cụ thể (2–3× break-even trước khi xét "0 đơn", 3–4× cho ngưỡng cost-per-event, 20–30% khi scale) là ngưỡng thực hành theo thông lệ — dùng làm khung, hiệu chỉnh theo margin & dữ liệu thật của từng tài khoản.*
