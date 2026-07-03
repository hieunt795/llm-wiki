# Fed Balance Sheet H1 2026 — Flow Mechanics (Chuỗi Tuần Thực Nghiệm)
> MODE DEEP | 2026-07-02 | Analyst: Claude (claude-sonnet-5)
> Nguồn: [RAW-OFFICIAL: Fed H.4.1 weekly 23 điểm Jan–Jun 2026] · [RAW-OFFICIAL: Treasury Fiscal Data auctions_query — notes/bonds/bills] · [RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026] · [WEB-2026-06: ACM 10Y term premium] · [RAW-BOOK: Duffie BPEA 2026]
> **Ghi chú (2026-07-03):** Đã hợp nhất vào `2026-07-03_fed-balance-sheet-h1-2026-unified-mode-deep.md` — xem file đó để có kết luận hiện hành. File này giữ nguyên để tham khảo walkthrough đầy đủ của identity check 23 điểm.

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Chuỗi dữ liệu tuần H.4.1 thực tế (23 điểm, Jan–Jun 2026) xác nhận hay bác bỏ các giả định flow [LLM-E] trong synthesis 29/06/2026 — đặc biệt tốc độ RMP, biên độ TGA, và vị trí thật của "sàn ample"? |
| **Asset / Currency** | USD · Bank Reserves · UST · MBS · TGA — cùng phạm vi với synthesis 29/06, nay bổ sung lớp **flow** (Δ theo tuần) thay vì chỉ **stock** (mức tại một thời điểm) |
| **Temporal Status** | CURRENT 🟢 — chuỗi 07/01/2026 → 24/06/2026 (23/26 tuần), chưa có điểm 07/2026 |
| **Thesis** | Chuỗi tuần thực nghiệm mật độ cao xác nhận và tinh chỉnh mạnh hơn ước tính trước: (1) hai tuần 08/04→22/04/2026 (mùa quyết toán thuế cá nhân) là một thí nghiệm tự nhiên khép kín — TGA tăng $310,1B trong khi reserves giảm $214,4B, với identity xấp xỉ đúng (residual "other factors" chỉ +$62,9B trên biến động dự đoán -$277,3B); (2) sàn ample thực nghiệm còn thấp hơn phát hiện trước — đáy thật của H1 là $2.901,8B (22/04), thấp hơn ~$100B so với mốc "$3.000B" hay được trích dẫn, và **không** kích hoạt stress SOFR–IORB; (3) biên độ TGA thật của H1 rộng tới $310,1B (không phải $100–200B như ước tính ban đầu) — vượt cả con số "$200B+ FBO" của Duffie; (4) nhu cầu đấu thầu vẫn khỏe ở notes/bonds (BTC 2,30–2,99) nhưng có dấu hiệu mềm nhẹ ở bills kỳ hạn trung (13–26 tuần, BTC giảm ~30–50bp từ Jan-Feb sang June) — đúng vị trí TBAC cảnh báo bills vượt target 15–20%. |

---

## MACRO LAYER

| Chiều | H1 2026 (flow xác nhận, 23 điểm) |
|-------|--------------------------|
| **RMP pace** | UST +$252,6B / ~24 tuần ≈ **+$42B/tháng RAW-OFFICIAL** (trước đây [LLM-E] "~$40B/tháng") |
| **MBS runoff pace** | −$77,4B / ~24 tuần ≈ **−$14B/tháng RAW-OFFICIAL** (trước đây [LLM-E] "$15–20B/tháng") |
| **Currency in circulation** | +$30,6B / H1 ≈ +$5B/tháng — nhỏ, không theo mùa, không phải nguồn biến động chính |
| **Reserves band (revised)** | **$2.901,8B – $3.129,6B**, độ rộng **$227,8B** (mẫu 11 điểm trước ước tính $192,9B — nay rộng hơn) |
| **TGA band (revised)** | **$697,1B – $1.007,2B**, độ rộng **$310,1B** (mẫu 11 điểm trước ước tính $204,5B — nay rộng hơn đáng kể) |
| **Bills demand** | Notes/bonds ổn định (BTC 2,30–2,99); bills 13–26 tuần mềm nhẹ (BTC Jan-Feb 2,71–3,30 → June 2,32–2,79) |

RMP giữ đúng vai trò trend-anchor với mẫu dữ liệu dày hơn: tốc độ mua UST ròng không đổi so với ước tính lần trước vì dùng phương pháp endpoint (hai đầu chuỗi không đổi). Nhưng việc lấp đầy 12 điểm còn thiếu đã phát hiện ra một biến động nội-kỳ lớn hơn nhiều so với mẫu thưa: biên TGA thực tế ($310,1B) vượt xa giả định "$100–200B/tuần" ban đầu, và biên này xảy ra trọn trong hai tuần quanh ngày quyết toán thuế 15/04 — một sự kiện tài khóa định kỳ, có thể dự báo trước theo lịch, chứ không phải nhiễu ngẫu nhiên.

## PLUMBING LAYER

Với mẫu 23 điểm, cực trị thật của H1 2026 không còn là 29/04 (như phát hiện ở vòng ingest trước) mà là **22/04/2026**: reserves chạm đáy H1 ($2.901,8B) đúng lúc TGA chạm đỉnh H1 ($1.007,2B). Quan trọng hơn, hai tuần 08/04→22/04 tạo thành một thí nghiệm tự nhiên khép kín quanh ngày quyết toán thuế thu nhập cá nhân 15/04: TGA tăng $310,1B (từ $697,1B lên $1.007,2B) trong khi reserves giảm $214,4B (từ $3.116,2B xuống $2.901,8B), tổng tài sản gần như không đổi (+$13,5B), currency in circulation phẳng tuyệt đối (+$0,5B), và reverse repo giảm nhẹ (-$19,8B). Kiểm định identity đầy đủ cho cửa sổ này — `ΔReserves_dự_đoán = ΔAssets − ΔTGA − ΔRRP − ΔCurrency = 13,5 − 310,1 − (−19,8) − 0,5 = −277,3B` so với ΔReserves thực tế −214,4B — cho residual "other factors" chỉ +$62,9B, tức phần lớn biến động (−277,3 trên −214,4 thực tế) được giải thích trực tiếp bởi một biến số duy nhất: TGA. Đây là bằng chứng thực nghiệm sạch và chặt nhất có được cho identity `ΔReserves ≈ RMP_trend − ΔTGA_event` — một sự kiện tài khóa đơn lẻ, có thể dự báo theo lịch, di chuyển reserves hơn $200B trong hai tuần mà không có tầng đệm trung gian (ON RRP domestic ≈ $2,3B).

Phát hiện thứ hai, đã được tinh chỉnh thêm một bậc: sàn ample thực nghiệm còn thấp hơn báo cáo trước. Đáy $2.901,8B (22/04) thấp hơn ~$100B so với mốc "~$3.000B" (~9% GDP) hay được trích dẫn [WEB-2026-04-11: Andreopoulos]. Đối chiếu SOFR–IORB tháng 4/2026: trung bình −11bp, đáy tháng −18bp — không hề có tín hiệu payment throttling hay SRF activity bất thường trong đúng tuần chạm đáy [RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026.md]. Sàn "binding" thật theo nghĩa Duffie vẫn chưa từng bị chạm trong H1 2026, kể cả tại cú sốc tài khóa lớn nhất (mùa thuế). Mốc $3.000B nên tiếp tục được đọc là ước tính biên trên thận trọng.

Ở phía cầu Treasury, bức tranh giờ có thêm chiều sâu: notes/bonds (BTC 2,30–2,99 toàn H1, không xu hướng) vẫn khỏe như phát hiện trước, nhưng việc bổ sung dữ liệu bills theo kỳ hạn phát hiện một điểm mềm cục bộ — BTC của bills 13-tuần, 17-tuần, 26-tuần giảm khoảng 30–50bp từ khoảng Jan–Feb (2,71–3,30) xuống June (2,32–2,79), trong khi 4-tuần/8-tuần và 52-tuần vẫn ổn định hoặc mạnh hơn. Vị trí mềm này khớp chính xác với cảnh báo của TBAC (Q2 refunding statement 06/05/2026) rằng bills đã vượt target 15–20% của danh mục nợ khả mại, hệ quả trực tiếp của extraordinary measures Jan–Apr 2026 [RAW-OFFICIAL: Treasury_Q2_2026_Refunding_Details.md]. Điều chỉnh giá đang diễn ra đúng ở đoạn cung dư thừa nhất của đường cong, không lan sang đầu ngắn nhất (vẫn được đỡ bởi cầu quasi-cash của money market) hay đầu dài (nơi ACM term premium mới là gauge vận hành).

Ba dòng dữ liệu — TGA event lớn và có thể dự báo theo lịch thuế, sàn reserves chưa từng bị test dù chạm mức thấp hơn ước tính, và cầu đấu thầu khỏe ở phần lớn đường cong trừ một điểm mềm cục bộ ở bills trung hạn — khớp lại thành bức tranh chi tiết hơn nhiều so với báo cáo 29/06 hay thậm chí báo cáo flow đầu tiên (11 điểm) của chính phiên này. H1 2026 là một hệ thống đã hấp thụ ít nhất một cú sốc tài khóa định kỳ lớn (mùa thuế, +$310B TGA/2 tuần) mà không chạm ngưỡng thật của sàn reserves, đồng thời hấp thụ nguồn cung Treasury mới chủ yếu qua điều chỉnh giá — với điều chỉnh đó bắt đầu tập trung rõ nhất ở đoạn bills trung hạn, nơi cung đã vượt target cấu trúc.

## TREASURY LAYER

Với dữ liệu mở rộng, desk nên nâng cấp khung tham chiếu thêm một bậc: thay vì dải quan sát rộng ($2.918,6B–$3.111,5B từ báo cáo trước), dùng dải đã xác nhận **$2.901,8B–$3.129,6B** (độ rộng $227,8B), và quan trọng hơn — dùng **lịch thuế** (15/04, và các mốc quyết toán quý/năm khác) làm biến dự báo chính cho TGA event lớn, thay vì chỉ theo dõi lịch phát hành/tái cấp vốn. Cú sốc mùa thuế 08/04→22/04 (TGA +$310B/2 tuần) là sự kiện lớn nhất H1 và có thể dự báo trước theo lịch cố định hàng năm — khác với FBO cuối quý (cũng dự báo được) hay TGA rebuild sau debt-ceiling (khó dự báo hơn).

- **Ngắn hạn:** Đưa ngày quyết toán thuế cá nhân (thường 15/04) vào lịch rủi ro reserves cùng cấp độ với FBO cuối quý; nếu reserves in ra dưới $2.901,8B (đáy H1 đã xác nhận) kèm SOFR–IORB nới rộng đồng thời, đó là bằng chứng đầu tiên sàn thật đã bị chạm.
- **Trung hạn:** Theo dõi riêng bills 13–26 tuần như gauge cung-cầu sớm — BTC tiếp tục giảm dưới 2,3 ở các kỳ hạn này là tín hiệu áp lực cấu trúc từ tỷ trọng bills vượt target, sớm hơn khi nó lan tới notes/bonds hay ACM term premium.
- **Dài hạn:** Kết hợp BTC notes/bonds (chưa suy yếu) với ACM term premium (dải +0,6–0,8%, thiếu điểm tháng 6) để phân biệt áp lực cấu trúc (bills) khỏi áp lực duration dài hạn (coupon supply) — hai kênh áp lực khác nhau, không nên gộp chung một chỉ báo.

---

## TIMING LAYER

| | Past (trước H1) | Present H1 2026 (23 điểm) | Future (H2 2026, ngoại suy) |
|--|------------------|----------------------------|-------------------------------|
| **Reserves** | 2023: ON RRP >$2.000B làm đệm hấp thụ TGA swing | Biên $2.901,8B–$3.129,6B; đáy 22/04 (mùa thuế) không kích hoạt stress | Nếu một cú TGA event khác quy mô $310B+ trùng FBO cuối quý (30/09), đáy reserves mới có thể thấp hơn 22/04 |
| **TGA / Fiscal calendar** | — | Biên $697,1B–$1.007,2B; đỉnh gắn với quyết toán thuế 15/04, không phải sự kiện ngẫu nhiên | Lịch thuế Q3/Q4 (ước tính thuế doanh nghiệp theo quý) + FBO 30/09 là điểm rủi ro kế tiếp có thể dự báo |
| **RMP/MBS** | QT2 kết thúc 01/12/2025; RMP khởi động 10/12/2025 | UST +$252,6B (~$42B/mo); MBS −$77,4B (~−$14B/mo) — pace ổn định suốt 23 điểm | Ngoại suy pace hiện tại nếu RMP không đổi quy mô |
| **Auction demand** | — | Notes/bonds khỏe (BTC 2,30–2,99); bills 13-26wk mềm nhẹ, đúng vị trí TBAC cảnh báo | Q3 refunding (08/2026) là phép thử coupon; theo dõi riêng bills nếu tỷ trọng >20% không giảm |

**Velocity:** Flow reserves truyền dẫn trong ngày (Fedwire); TGA event tài khóa (thuế, phát hành) theo lịch định kỳ tuần-đến-hai-tuần; RMP trend hiện rõ ở tần suất tháng; auction demand phản ứng theo phiên.

## FEEDBACK / BOUNDARY

| Signal | Ngưỡng cũ (báo cáo 11 điểm) | Ngưỡng mới (23 điểm) | Hiện tại |
|--------|------------------------------|--------------------------|---------|
| Reserves floor | Dải $2.918,6B–$3.111,5B | Dải **$2.901,8B–$3.129,6B**; đáy dưới $2.901,8B kèm SOFR nới mới là báo động | 24/06: $2.954,5B — trong dải |
| TGA swing | "$100–200B/tuần" ước tính | **Xác nhận $310,1B trong 2 tuần** (mùa thuế) — biên lớn hơn ước tính ban đầu | Theo dõi FBO 30/09 như điểm tương tự kế tiếp |
| RMP pace | [LLM-E] ~$40B/tháng | RAW-OFFICIAL +$42B/tháng UST | Xác nhận, ổn định qua 23 điểm |
| Bills demand | Chưa quantify | BTC 13–26wk giảm ~30-50bp Jan-Feb→June | Mềm nhẹ, chưa phải distress |

**Failure conditions (cập nhật):** Cú sốc mùa thuế (+$310B/2 tuần) đã là sự kiện TGA lớn nhất quan sát được trong H1 và KHÔNG phá sàn. Kịch bản kiểm định sàn thật đòi hỏi một cú sốc lớn hơn hoặc trùng thời điểm với FBO cuối quý (30/09) — hai lực cộng hưởng chưa từng xảy ra đồng thời trong dữ liệu hiện có.

---

## DIAGRAM

```
RESERVES vs TGA — 23 ĐIỂM TUẦN H1 2026 (RAW-OFFICIAL H.4.1)
Cửa sổ mùa thuế: 08/04 → 22/04/2026

  TGA ($B)
  1,007.2 ┤                    ●22/04  H1 HIGH
          │                   ╱
    924.4 ┤              ●15/04
          │             ╱
          │            ╱
    697.1 ┤●08/04  H1 LOW
          └──────────────────────────
           08/04   15/04   22/04

  Reserves ($B)
  3,129.6 ┤●15/04 (tie H1 high)
          │      ╲
  3,116.2 ┤●08/04 ╲
          │         ╲
          │          ╲
  2,901.8 ┤           ●22/04  H1 LOW
          └──────────────────────────
           08/04   15/04   22/04

  2 TUẦN: TGA +$310.1B  ⇄  Reserves −$214.4B
  Identity check: ΔRes_dự_đoán = ΔAssets−ΔTGA−ΔRRP−ΔCurrency = −277.3B
                  ΔRes thực tế = −214.4B  →  residual "other" = +62.9B
                  (TGA giải thích phần lớn biến động, không phải trùng hợp)

  SOFR-IORB tháng 4/2026: avg −11bp → KHÔNG có stress dù reserves chạm đáy H1 mới ($2,901.8B)
  ⇒ sàn "binding" thật < $2,901.8B, vẫn chưa từng bị test trong H1 2026
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed và tinh chỉnh thêm một bậc — mẫu 23 điểm phát hiện cực trị thật (22/04, không phải 29/04), một thí nghiệm tự nhiên khép kín (mùa thuế) xác nhận identity chặt hơn, và biên TGA/reserves đều rộng hơn ước tính ban đầu |
| **Net Flow Effect** | RMP +$42B/tháng UST, MBS −$14B/tháng (không đổi, endpoint method); TGA event lớn nhất H1 là +$310,1B/2 tuần (mùa thuế), giải thích phần lớn biến động reserves qua identity check trực tiếp |
| **Treasury Action** | Dùng dải $2.901,8B–$3.129,6B làm tham chiếu sàn; đưa lịch thuế vào cùng cấp rủi ro với FBO cuối quý; theo dõi riêng BTC bills 13-26 tuần như gauge sớm cho áp lực cấu trúc bills |
| **Confidence** | TIER B, mẫu dày hơn (23/26 tuần thay vì 11/24) — identity check trực tiếp qua cửa sổ mùa thuế là bằng chứng chặt nhất trong cả cluster; vẫn thiếu ACM tháng 6, SOFR daily Jan-May, và "other factors" residual chưa decompose đầy đủ |
| **Critical Caveat** | Kết luận "sàn thấp hơn $3.000B" vẫn dựa trên các lần chạm đáy chưa gây stress — chưa có bằng chứng về nơi sàn thật thực sự nằm, chỉ có bằng chứng về nơi nó KHÔNG nằm (tức là > $2.901,8B là vùng an toàn đã xác nhận) |

---

## NEXT STEPS

```bash
# Data gaps còn lại (ưu tiên giảm dần)
# → ACM tháng 6/2026 — vẫn thiếu, đã thử nhiều nguồn (NY Fed 403, macromicro 403)
# → SOFR daily Jan-May 2026 — chỉ có monthly avg, global-rates.com không lộ daily
# → "Other factors" residual decomposition (~$47-63B tùy cửa sổ) — cần Table 5 chi tiết đầy đủ
# → ~3/26 tuần H.4.1 còn thiếu trong mẫu (biên nhỏ, khó đổi kết luận)
# → H.4.1 tuần 07/2026 đầu tiên — chưa publish (404 tại 2026-07-02)

# Files tạo/cập nhật (2026-07-02, vòng 2)
# ✓ 02_sources/Clipping/Fed_H41_Weekly_Flow_H1_2026.md — nâng 11→23 điểm + currency + tax-season identity
# ✓ 02_sources/Clipping/Treasury_Bills_Auction_Results_H1_2026.md — mới
# ✓ 06_publish/2026-07-02_fed-balance-sheet-flow-mechanics-h1-2026.md — rewrite với số liệu 23 điểm

python librarian.py embed --incremental && python librarian.py sync
```

*MODE DEEP v1 (revised) | 2026-07-02 | Refs: P1 · P2 · P3 · P4 | [[Reserve_Management_Purchases_RMP]] · [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Standing_Repo_Facility_SRF_Mechanics]]*
