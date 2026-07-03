# US Treasury: Bảng Cân Đối, Đường Cong và Chính Sách H1 2026

**MODE DEEP | 2026-06-29**

**Ghi chú (2026-07-03):** Đã hợp nhất vào báo cáo tổng hợp toàn cảnh `06_publish/2026-07-03_us-macro-financial-master-synthesis-h1-2026.md` (CPI/PPI + Fed BS + Treasury/curve + Warsh). File này vẫn giữ nguyên làm nguồn chi tiết gốc.

**Thesis:** Bảng cân đối Kho bạc H1 2026 phản ánh ba lực đồng thời: (1) bình thường hóa hậu trần nợ dưới One Big Beautiful Bill Act ($41.1T), buộc vay gộp ~$683B H1 với TGA rebuild từ zero-buffer về $918.7B; (2) chiến lược quản lý nợ của Bessent cân bằng giữa bills linh hoạt và coupons dài hạn trong bối cảnh áp lực Warsh về phân quyền sở hữu rủi ro kỳ hạn; (3) đường cong Treasury phản ánh giao điểm của Fed neo đầu ngắn (3.50–3.75%) với term premium đầu dài đang phục hồi cấu trúc — tạo ra bear steepening kiểm soát nhưng có nguy cơ tăng tốc nếu cung coupon ramp lên mạnh trong H2.

## Top-Down Entry

Treasury không phải chỉ là người phát hành nợ — Treasury là đối tác vĩ mô của Fed trong hệ thống tài khóa-tài chính. Quy mô, thành phần và kỳ hạn của nợ phát hành quyết định: (a) ai gánh rủi ro lãi suất (dealer, tổ chức, nước ngoài, hay Fed); (b) mức reserves bị hút ra khỏi hệ thống ngân hàng qua TGA; (c) vị trí của đường cong tại mỗi kỳ hạn. Năm 2026, ý nghĩa của ba quyết định này đặc biệt lớn: OBBBA mở ra dư địa vay lớn, Bessent đang định hình lại chiến lược maturity management lần đầu tiên sau nhiều năm, và đường cong đang thoát ra khỏi trạng thái đảo ngược kéo dài.

Câu hỏi cốt lõi: **Ai đang mua $683B nợ mới của Treasury H1 2026, ở kỳ hạn nào, và giá nào?**

---

## Macro Layer

| Chiều | H1 2026 |
|-------|---------|
| **Tổng nợ bruto** | **$39.16T** (May 27, 2026) [WEB-2026-06-04: MSPD] — vượt $39T ngày 17/03/2026 |
| **Nợ do công chúng nắm** | $31.61T (80.4%); intragovernmental $7.55T [WEB-2026-06-04: MSPD] |
| **Nợ khả thị** | ~$31.52T: Bills $6.76T (21.44%) / Notes $15.94T (50.58%) / Bonds $5.40T (17.14%) / TIPS ~$2.2T / FRNs ~$0.6T [WEB-2026-06-04: MSPD] |
| **WAM (nợ khả thị)** | **70 tháng = 5 năm 10 tháng (5.83 năm)** [WEB-2026-03: MSPD] |
| **Avg coupon rate** | **3.386%** overall (Bills 3.69% / Notes 3.25% / Bonds 3.41%) [WEB-2026-06-04: MSPD] |
| **Gross H1 borrowing** | **$683B** (Q1 $574B + Q2 $109B; +$249B YoY) [WEB-2026-05-06: Treasury Refunding] |
| **Fed funds target** | 3.50–3.75% [WEB-2026-05-08: Benigno] |
| **2Y / 10Y / 30Y yield** | **4.14% / 4.49% / 4.98%** (July 2, 2026) [RAW-OFFICIAL: Treasury.gov daily par yield curve] |
| **2s10s / 2s30s (Jul 2)** | **+35bp / +84bp** — positive nhưng **đã hẹp lại** từ +72bp/+139bp đầu tháng 1 [RAW-OFFICIAL] |
| **10Y real yield / breakeven (Jul 2)** | **2.26% / 2.23%** — real yield tăng +32bp, breakeven đi ngang cả H1 [RAW-OFFICIAL: Treasury.gov real yield curve + FRED T10YIE, khớp gần như tuyệt đối] |
| **5Y5Y forward breakeven (Jul 2)** | **2.22%** — đáy H1 2.05% (30/03) → đỉnh H1 2.32% (19/05) → hồi lại điểm xuất phát [RAW-OFFICIAL: FRED T5YIFR] |
| **ACM 10Y term premium** | **+0.67–0.83%** (tháng 5/2026) [WEB-2026-05: NY Fed ACM] — dương lần đầu từ 2023 |
| **OBBBA 10Y fiscal cost** | ~$3.0–3.9T thêm vào nợ (CBO) [WEB-2026: CRFB] |

**Regime macro:** Không phải fiscal dominance (Fed vẫn độc lập), nhưng áp lực cung kéo dài. OBBBA ước tính thêm ~$3.3–3.8T thâm hụt 10 năm [LLM-ref: CBO] từ gia hạn TCJA + chi tiêu mới. Lãi suất ròng ($900B+/năm hiện tại [LLM-E]) chiếm ~14–15% chi ngân sách — compound loop: lãi suất cao → thâm hụt lớn → phát hành nhiều → term premium cao → lãi suất cao.

## Plumbing Layer

Thành phần nợ khả thị Kho bạc tại H1 2026 phản ánh di sản của hai thập kỷ quản lý nợ trong và sau khủng hoảng. Bills chiếm 21.44% nợ khả thị ($6.76T) [WEB-2026-06-04: MSPD] — **trên** TBAC target 15–20%, hệ quả trực tiếp của giai đoạn extraordinary measures tháng 1–4/2026 khi Treasury bị giới hạn coupon issuance và phải dựa nhiều vào cash management bills. Notes (2–10 năm) là mảng lớn nhất ở 50.58% ($15.94T), WAM toàn bộ marketable debt hiện ở 70 tháng (5.83 năm) [WEB-2026-03: MSPD] — ngắn hơn đỉnh 2020 (~6.8 năm). Bonds (>10 năm) ở 17.14% ($5.40T); mỗi 30Y auction ($25B/tháng theo Q2 refunding) là sự kiện thị trường trọng yếu H1 2026 vì nó định giá trực tiếp term premium. TIPS ~7% (~$2.2T) và FRNs ~2% (~$0.6T) hoàn chỉnh cơ cấu. Average coupon rate toàn portfolio ở 3.386% [WEB-2026-06-04: MSPD] — thấp hơn nhiều so với lợi suất thị trường hiện tại (4.37% cho 10Y), phản ánh phần lớn portfolio được phát hành ở thời kỳ lãi suất thấp (QE era). Q2 2026 refunding giữ nguyên coupon sizes ($58B 3Y / $42B 10Y / $25B 30Y) với cam kết "ít nhất vài quý tới" [WEB-2026-05-06: Treasury sb0305].

Đường cong Treasury tại July 2, 2026: 2Y 4.14% / 10Y 4.49% / 30Y 4.98% [RAW-OFFICIAL: Treasury.gov daily par yield curve], với 2s10s +35bp và 2s30s +84bp. Xét toàn bộ H1 2026 (Jan 2 → Jul 2, biweekly trajectory [RAW-OFFICIAL: Treasury_Yield_Curve_H1_2026_Trajectory_Real_Breakeven.md]): 2s10s **hẹp lại** từ +72bp xuống +31–35bp, và 2s30s hẹp từ +139bp xuống +80–84bp. Đây là phát hiện quan trọng: trong nội bộ H1 2026, đường cong **bear-flattening**, không phải bear-steepening như giả định ban đầu — chuyển động này do đầu ngắn (2Y +67bp: 3.47%→4.14%) tăng nhanh hơn nhiều so với 10Y (+30bp) và 30Y (chỉ +12bp: 4.86%→4.98%). Fed funds target giữ nguyên 3.50–3.75% suốt H1 (không cắt giảm) — 2Y tăng áp sát/xuyên đỉnh target trong khi target không đổi là dấu hiệu thị trường **rút lại kỳ vọng cắt giảm** đã định giá trước đó, không phải Fed thắt chặt thêm. 30Y gần như đi ngang cả H1 (đỉnh cục bộ ~5.12–5.14% giữa tháng 5 trùng thời điểm công bố Q2 refunding, sau đó thoái lui) — đầu dài ổn định nhất trên đường cong, không phải biến động nhất. Khung đa năm (2022–2025 inversion → re-steepening) trong bảng Timing vẫn đúng như một xu hướng dài hạn; điều cần điều chỉnh là chuyển động **bên trong** H1 2026 tự nó đi ngược hướng đó.

Khu vực TIPS và breakeven cho phép tách biệt hai thành phần lạm phát, nay có dữ liệu xác nhận thay cho ước tính trước đó. Real yield 10Y tăng từ 1.94% (Jan 2) lên 2.26% (Jul 2, +32bp), với đáy cục bộ ~1.76–1.79% giữa tháng 2 [RAW-OFFICIAL: Treasury.gov real yield curve]. Breakeven 10Y (tính bằng nominal 10Y trừ real 10Y) dao động đi ngang trong biên 2.20–2.48% suốt H1, không có xu hướng rõ ràng — điểm đầu (2.25%) và điểm cuối (2.23%) gần như bằng nhau; đối chiếu với chuỗi T10YIE chính thức từ FRED (lấy trực tiếp qua curl — WebFetch vẫn bị chặn 403 nhưng curl thành công), phép xấp xỉ nominal−real khớp gần như tuyệt đối tại mọi điểm kiểm tra (sai lệch ≤0.01pp), xác nhận độ tin cậy ở mức basis-point chứ không chỉ định hướng. Tổng hợp: gần như toàn bộ mức tăng lợi suất danh nghĩa 10Y trong H1 (+30bp) đến từ real yield (+32bp), breakeven đóng góp ròng ~0. Điều này khớp với ACM decomposition (term premium +0.67→+0.83% tháng 5): cả hai phép phân rã độc lập (real/breakeven và ACM expected-path/term-premium) đều đồng thuận — mức tăng lợi suất là câu chuyện lãi suất thực, không phải kỳ vọng lạm phát.

Tuy nhiên, breakeven 5Y5Y forward (T5YIFR, chính thức từ FRED — đo kỳ vọng lạm phát dài hạn, tách khỏi nhiễu ngắn hạn của cú sốc năng lượng) cho thấy bức tranh không tĩnh như con số ròng ~0 của 10Y gợi ý: đáy H1 2.05% (30/03, ngay trước khi cú sốc Hormuz leo thang mạnh nhất) → đỉnh H1 2.32% (19/05, ~6 tuần sau đỉnh giá Brent) → hồi gần như hoàn toàn về 2.22% (02/07). Đọc cùng PPI stage-cascade diagnostic (Stage1-Stage4 gap giãn nhanh nhất đúng giai đoạn tháng 4-5): thị trường **đã** định giá rủi ro cú sốc năng lượng/tariff làm lệch neo kỳ vọng lạm phát dài hạn trong giai đoạn cao điểm, rồi gỡ bỏ gần hết phần bù rủi ro đó vào cuối tháng 6 — nhất quán với việc uy tín neo lạm phát của Fed được giữ vững, nhưng cũng có nghĩa niềm tin thị trường đã bị thử thách thực sự chứ không phải "không hề dao động" suốt H1.

## Treasury Layer

Với người thực hành Treasury desk, ba động lực chính sách của Bessent có hàm ý vận hành riêng biệt trong H1 và H2 2026.

Hậu OBBBA, chiến lược Bessent là duy trì coupon auction sizes ổn định (không ramp đột ngột) trong khi dùng bills linh hoạt để điều chỉnh nhu cầu vốn ngắn hạn. Điều này phản ánh trường phái "regular and predictable" của TBAC nhưng trong bối cảnh cung tăng gộp $249B YoY — thực chất coupons vẫn phải tăng. Q3 2026 refunding (tháng 8/2026) là điểm quan sát chính: nếu Bessent tăng sizes 10Y/30Y đáng kể, term premium sẽ có thêm lực nới. Nếu giữ ổn định và tăng bills, rollover risk ngắn hạn tăng nhưng dài hạn được kiểm soát.

Áp lực Warsh-Cochrane ("New Accord") đặt vấn đề phân quyền: Treasury nên sở hữu maturity structure decision thay vì để Fed làm proxy thông qua danh mục QE. Điều này hàm ý Treasury nên chủ động phát hành nhiều hơn ở khu vực dài để bảo hiểm refinancing risk [WEB-2026-02-17: Cochrane]. Bessent chưa thể hiện rõ lập trường, nhưng áp lực từ thị trường (term premium widening) tự nhiên sẽ đẩy Treasury ra phát hành dài hơn khi chi phí ngắn hạn tăng tương đối.

- **Q3 2026 auction calendar**: Q3 refunding (tháng 8) + mid-September coupon settle là điểm rủi ro gần nhất; nếu trùng với FBO window-dressing cuối Q3 (30/09) → cộng hưởng reserve stress + coupon supply pressure
- **Bills concentration**: Nếu bills >20% marketable (tiếp tục hậu extraordinary measures) → rollover $5.5–6T/năm trong <1 năm → nhạy cảm với mọi SOFR spike; tracker: tỷ lệ bills trong TBAC quarterly report
- **Buyback program**: Treasury buyback off-the-run bonds để cải thiện thanh khoản — tín hiệu tích cực cho bid-to-cover nhưng trung tính với total supply; theo dõi regularity của buyback operations

---

## Timing Layer

| | Past | Present H1 2026 | Future |
|--|------|-----------------|--------|
| **Bảng cân đối** | COVID: $21T → $28T marketable trong 4 năm; extraordinary measures 2025-Q1 2026 → bills-heavy WAM rút ngắn | ~$28.5-29T marketable; WAM ~6.0-6.3yr; TGA $918.7B rebuilt [RAW-OFFICIAL] | OBBBA thêm ~$3.3-3.8T thâm hụt 10 năm → tổng nợ có thể đạt $40-42T đến 2030 [LLM-E] |
| **Đường cong** | 2020-2021: near-YCC (Fed ghim dài qua QE); 2022-2023: bear flattening → inversion; 2024-2025: re-steepening chậm ra khỏi inversion (2s10s về gần 0/dương nhẹ cuối 2025) | H1 2026 tự đảo hướng: 2s10s hẹp từ +72bp (Jan) xuống +31-35bp (Jun-Jul) [RAW-OFFICIAL]; front-end-led (2Y +67bp) chứ không phải long-end-led; 10Y 4.19%→4.49%; 30Y gần như đi ngang 4.86%→4.98% | Nếu thị trường tiếp tục rút kỳ vọng cắt giảm → 2s10s có thể về gần 0 lần nữa; nếu Fed xác nhận cắt H2 → 2Y giảm trở lại, 2s10s mở rộng; nếu OBBBA deficit xác nhận qua Q3 refunding ramp → áp lực riêng lên 30Y qua term premium [LLM-E] |
| **Chính sách** | Yellen: "regular and predictable"; coupon ramp 2021-2023 đẩy WAM từ 5.5 lên 6.2 năm; bills cap controversy 2023 | Bessent: duy trì sizes, flexibility ở bills; extraordinary measures → OBBBA; TGA rebuild | Q3 refunding: test case Bessent vs market cho coupon sizes; Warsh institutional pressure tăng |

**Velocity và nhịp điệu:** Refunding announcements (tháng 2, 5, 8, 11) là điểm định lại kỳ vọng supply theo quý. Auction settle mid-month là điểm TGA hút reserves hàng tháng. Hai nhịp này là driving force của đường cong và reserves đồng thời — không thể phân tích độc lập.

**Synchronization H2 2026:** Q3 end 30/09 là điểm FBO window-dressing (≥$200B) + coupon settle + Q3 refunding ramp → ba lực đồng thời, không có ON RRP đệm.

## Feedback và Ranh Giới

Vòng phản hồi tài khóa-tài chính là rủi ro cấu trúc dài hạn: lãi suất cao → chi lãi $900B+/năm → thâm hụt lớn hơn → phải phát hành nhiều hơn → term premium tăng → lãi suất cao hơn. Vòng này chỉ tự ổn định nếu có một trong hai lực ngắt: (a) Fed pivot mạnh (cắt lãi, ép kỳ vọng ngắn hạn xuống); (b) fiscal consolidation (cắt chi/tăng thu để giảm nhu cầu phát hành). OBBBA đi ngược chiều (b) — cắt thuế và tăng chi tiêu. Điều này có nghĩa là tất cả gánh nặng ổn định vòng phản hồi dồn vào kỳ vọng Fed, khiến mỗi FOMC communication quan trọng hơn bình thường với đường cong.

Ranh giới phân tích: tổng cầu Treasury (foreign CB, pension/insurance, bank, retail, Fed) không được phân tích trong phân tích này — nhu cầu nước ngoài (Nhật Bản, Trung Quốc, các nước Gulf) là biến số quan trọng nhưng cần nguồn dữ liệu riêng (TIC data). Sự kiện Moody's hạ xếp hạng tín dụng Mỹ xuống Aa1 (tháng 5/2025) [LLM-ref] là background risk đối với cầu nước ngoài nhưng chưa tạo dislocation rõ trong H1 2026.

---

## Diagram

```
TREASURY BALANCE SHEET & YIELD CURVE — H1 2026
═══════════════════════════════════════════════════════════════════

NỢ KHẢ THỊ $31.52T [WEB-MSPD May 2026]   ĐƯỜNG CONG July 2, 2026 [RAW-OFFICIAL Treasury.gov]
───────────────────────────────────────   ──────────────────────────────────────────────
  Bills (<1yr)  21.4% [$6.76T] ⚠️>TBAC    Yield
  Notes (2-10Y) 50.6% [$15.94T]       5.0%│                         ●30Y 4.98%
  Bonds (>10Y)  17.1% [$5.40T]        4.5%│                 ●10Y 4.49%
  TIPS           ~7%  [$2.21T]        4.1%│    ●2Y 4.14%
  FRNs           ~2%  [$0.63T]        3.7%│●3M 3.82%
                                          └──────────────────────────────────
  WAM: 70m = 5.83yr [MSPD Mar 2026]        3M    2Y        10Y            30Y
  Avg coupon: 3.386%  Chi lãi ~$1.3T+/yr    ← 2s10s: +35bp → ← 2s30s: +84bp →
  Gross debt: $39.16T (May 2026)            (Jan 2: +72bp / +139bp → đã HẸP LẠI cả H1)
  OBBBA: +$3-3.9T thâm hụt 10yr (CBO)

CHUỖI NHÂN QUẢ — ISSUANCE → CURVE → RESERVES
───────────────────────────────────────────────
Treasury phát hành coupon (notes/bonds)
           │
           ▼
Dealer mua bằng reserves → TGA tăng → Reserves hệ thống ↓
[đoạn ngắn: reserves stress, SOFR-IORB]
           │
           ▼
Private market tiêu hóa net new duration (~$683B H1)
Fed không mở rộng portfolio (RMP trung lập)
           │
           ▼
Term premium tăng dần → 10Y/30Y yield tăng → Bear steepening
[đoạn dài: financial conditions tighten from long end]

BILLS vs COUPONS — TRADE-OFF
───────────────────────────────────────────────
Bills-heavy                    Coupons-heavy
─ Rollover risk $5.5T+/yr      + WAM kéo dài → refinancing risk ↓
─ SOFR-sensitive               + Term premium tín hiệu rõ hơn
+ Flexibility (điều chỉnh      − Immediate supply → term premium ↑
  nhanh theo nhu cầu)          − 30Y auction pressure
+ Fed absorbs bills faster     
  (RMP mostly short UST)       
```

---

## Kết Luận

**Mức tin cậy: TIER B+** — Bảng cân đối Treasury (debt outstanding, WAM, coupon rates), refunding details (Q1+Q2), TIC foreign holdings, yield curve daily trajectory (nominal + real/TIPS, biweekly H1 2026), official breakeven (T10YIE + T5YIFR, FRED direct), và ACM term premium đều đã ingest từ nguồn RAW-OFFICIAL. Gap còn lại: NY Fed ACM daily timeseries đầy đủ (chỉ có 3 điểm tháng 4-5, tháng 6-7 vẫn bị chặn 403 ở mọi nguồn đã thử kể cả curl trực tiếp lên newyorkfed.org).

Treasury H1 2026 đang vận hành trong môi trường đặc thù: bình thường hóa hậu debt ceiling trong khi fiscal trajectory từ OBBBA mở ra giai đoạn phát hành kéo dài. Tuy nhiên, dữ liệu xác nhận (không phải ước tính) cho thấy một điều chỉnh quan trọng so với bản nháp trước: đường cong **không bear-steepen trong nội bộ H1 2026** — nó bear-flatten (2s10s hẹp từ +72bp xuống +31-35bp), do đầu ngắn tăng nhanh hơn đầu dài. Cơ chế là thị trường rút lại kỳ vọng cắt giảm lãi suất Fed (2Y tăng +67bp trong khi Fed funds target đứng yên 3.50-3.75%), không phải term premium đẩy đầu dài lên nhanh hơn. Khung đa năm (2022-2025: inversion → re-steepening) là bối cảnh nền đúng, nhưng chuyển động cụ thể trong H1 2026 tự nó đi ngược chiều đó — một sự phân biệt cần thiết giữa xu hướng dài hạn và động lực trong kỳ.

Phần real yield/breakeven xác nhận cùng kết luận từ góc độ khác: gần như toàn bộ tăng lợi suất danh nghĩa 10Y (+30bp H1) đến từ real yield (+32bp), breakeven đi ngang (~0 net). Kết hợp ACM decomposition (term premium +0.67→+0.83%, expected rate path ổn định) → bức tranh nhất quán: H1 2026 là câu chuyện "real rate bình thường hóa + rút kỳ vọng cắt giảm", không phải câu chuyện lạm phát hay term-premium-only.

Liên kết với Fed: mỗi $ nợ mới Treasury phát hành là $ reserves hút ra khỏi hệ thống ngân hàng (qua TGA rebuild), đồng thời là $ duration risk tư nhân phải hấp thụ mà không có Fed bù đắp. Xem: `2026-06-29_fed-balance-sheet-synthesis.md` và `2026-06-29_fed-duration-extraction-term-premium.md`. Nguồn dữ liệu curve mới: `02_sources/Clipping/Treasury_Yield_Curve_H1_2026_Trajectory_Real_Breakeven.md`.

## Next Steps

1. ~~Ingest raw source — MSPD H1 2026~~ RESOLVED (`US_Treasury_H1_2026_Refunding_And_Debt.md`)
2. ~~Ingest raw source — Q1+Q2 2026 Refunding Announcements~~ RESOLVED (`Treasury_Q2_2026_Refunding_Details.md`, `US_Treasury_H1_2026_Refunding_And_Debt.md`)
3. ~~Ingest raw source — TIC data H1 2026~~ RESOLVED (`TIC_Foreign_Holdings_April2026.md`)
4. ~~Ingest raw source — 2Y/5Y/10Y/30Y daily H1 2026, TIPS real yield, breakeven~~ RESOLVED 2026-07-03 (`Treasury_Yield_Curve_H1_2026_Trajectory_Real_Breakeven.md`, Treasury.gov direct — FRED blocked automated fetch with 403)
5. **Tạo node** — `03_wiki/mechanisms/Treasury_Debt_Management_Strategy.md` — debt management objectives, TBAC, bills-coupons framework, WAM targeting (đã tồn tại per memory — cần kiểm tra và liên kết finding mới về 2s10s flattening)
6. **Tạo node** — `03_wiki/evidence/US_Treasury_Balance_Sheet_H1_2026.md` — snapshot confirmed data với MSPD source
7. **Liên kết** — Update `03_wiki/mechanisms/Treasury_General_Account_Mechanism.md` với cross-reference đến phân tích này
8. Ingest NY Fed ACM daily timeseries đầy đủ H1 2026 (hiện chỉ có 3 điểm rời rạc: Apr30/May15/May28, thiếu June-July) để xác nhận ACM term premium có đồng pha với real yield tăng hay không — **thử lại 2026-07-03, vẫn 403 ở mọi nguồn kể cả curl trực tiếp**
9. ~~Official T10YIE (FRED) hoặc 5Y5Y forward breakeven để thay thế phép tính xấp xỉ nominal−real hiện tại~~ RESOLVED 2026-07-03 — T10YIE khớp gần như tuyệt đối với approximation cũ (xác nhận, không cần sửa số); T5YIFR cho thấy round-trip 2.05%→2.32%→2.22% (đáy 30/03, đỉnh 19/05) mà endpoint-only trước đó không thấy được (`Treasury_Yield_Curve_H1_2026_Trajectory_Real_Breakeven.md`)

---

*Note thuộc publish layer. Xem thêm: `2026-06-29_fed-balance-sheet-synthesis.md` (Fed side) + `2026-06-29_fed-duration-extraction-term-premium.md` (term premium mechanism). Cluster hoàn chỉnh: Treasury issuance ↔ TGA ↔ Reserves ↔ SOFR-IORB ↔ Term premium.*
