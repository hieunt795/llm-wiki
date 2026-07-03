# US H1 2026 — Chuỗi Ba Lớp: CPI/PPI → Bảng Cân Đối Fed → Bảng Cân Đối Kho Bạc → Đường Cong Lợi Suất & Kỳ Vọng Thị Trường → Hàm Ý Chính Sách Fed
> MODE DEEP | 2026-07-03 | Analyst: Claude (claude-sonnet-5)
> Nguồn: tổng hợp bậc hai (second-order synthesis) — không ingest raw source mới, chỉ nối lại ba MODE DEEP đã publish trong cluster:
> - `06_publish/2026-07-03_us-cpi-ppi-nonlinear-inflation-h1-2026.md`
> - `06_publish/2026-07-03_fed-balance-sheet-h1-2026-unified-mode-deep.md`
> - `06_publish/2026-06-29_us-treasury-balance-sheet-yield-curve-h1-2026.md`
> Toàn bộ source label gốc ([RAW-OFFICIAL], [RAW-CLIP], [WEB], [LLM-E], [LLM-ref]) được giữ nguyên khi trích dẫn lại số liệu cụ thể từ ba tài liệu trên.

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Ba lớp dữ liệu độc lập trong cluster này — giá tiêu dùng/sản xuất, bảng cân đối Fed, bảng cân đối Kho bạc — kết nối với nhau qua kênh nào để tạo ra chuyển động đường cong lợi suất quan sát được trong H1 2026, và chuỗi kết nối đó hàm ý gì cho lộ trình chính sách Fed từ nay đến cuối năm? |
| **Asset / Currency** | USD · CPI/PPI/PCE · bảng cân đối Fed (reserves/RMP/TGA) · nợ khả thị Kho bạc · đường cong lợi suất danh nghĩa và thực |
| **Temporal Status** | CURRENT 🟢 — as-of 2026-07-03; nền dữ liệu đến hết tháng 5 (CPI/PPI), 24/06 (H.4.1), 02/07 (đường cong) |
| **Analytical Scope** | Tổng hợp bậc hai ba cluster đã confirmed riêng lẻ; mục tiêu là kiểm tra xem chuỗi nhân quả giả định (CPI/PPI → Fed BS → Treasury BS → Curve) có thực sự là một đường thẳng hay là nhiều kênh song song |
| **Thesis** | Chuỗi hỏi ban đầu ngụ ý một đường thẳng, nhưng ba cluster cho thấy đây là **hai kênh song song hội tụ tại đường cong**, không phải một chuỗi tuần tự. Kênh (1) — kỳ vọng chính sách: cascade CPI/PPI (năng lượng Hormuz + tariff + PPI stage-gap +5.73pp) đẩy Fed sang hawkish pivot, thị trường rút kỳ vọng cắt giảm, đầu ngắn đường cong tăng nhanh (2Y +67bp) gây bear-flattening — đây là kênh **thắng thế về biên độ** trong H1. Kênh (2) — cấu trúc cung-cầu duration: Kho bạc phát hành $683B gross mà RMP trung lập không hấp thụ thêm, khu vực tư nhân gánh toàn bộ duration mới, term premium dần dương trở lại (+0,67→+0,83%) — kênh **chậm hơn, mới ở giai đoạn đầu**. Bảng cân đối Fed không nằm "giữa" CPI/PPI và Kho bạc theo nghĩa nhân quả trực tiếp — nó phản ứng với inflation qua kênh lãi suất chính sách (mặt lãi suất) và phản ứng với Kho bạc qua kênh duration (mặt danh mục), hai mặt tách biệt của cùng một thể chế. Nếu PPI cascade tiếp tục xác nhận trong dữ liệu June (14–15/07) đồng thời Q3 refunding (08/2026) đẩy coupon size lên, hai kênh có thể lần đầu cùng kích hoạt mạnh — khi đó đường cong có thể chuyển từ bear-flattening sang bear-steepening đồng thời với hawkish hơn ở đầu ngắn, một tổ hợp chưa từng quan sát trong H1. |

---

## MACRO LAYER

| Chiều | H1 2026 |
|-------|---------|
| **Macro Regime** | Hai mặt tách biệt của cùng một Fed: hawkish hold/hike-bias ở mặt lãi suất chính sách; Ample Reserves (Regime A) ở mặt bảng cân đối |
| **Policy Anchor** | Fed funds 3,50–3,75% giữ nguyên toàn H1 [RAW-OFFICIAL: FOMC minutes]; IORB 3,75% neo mức sàn reserves, không liên quan trực tiếp đến lộ trình FFR |
| **Fiscal Stance** | OBBBA nâng trần nợ lên $41,1T; gross borrowing $683B H1 (+$249B YoY) [WEB-2026-05-06: Treasury Refunding]; TGA rebuild lên đỉnh $1.007,2B quanh mùa quyết toán thuế [RAW-OFFICIAL] |
| **Institutional Constraint** | Dual mandate đối mặt cú sốc cung (oil + tariff) không kiểm soát trực tiếp bằng công cụ cầu; RMP "hoàn toàn tách biệt khỏi chính sách tiền tệ" [RAW-OFFICIAL: Perli 26/03/2026] — nghĩa là không thể dùng RMP để hấp thụ issuance mới dù lạm phát hay lãi suất diễn biến ra sao |
| **Structural Tension** | FFR nén cầu trong khi Kho bạc bơm cung nợ kỷ lục và Fed không mở rộng danh mục bù đắp — hai áp lực tăng lợi suất xuất phát từ hai đầu khác nhau của đường cong, cùng chiều nhưng không cùng cơ chế |

## PLUMBING LAYER

Điểm khởi đầu của chuỗi là cú sốc giá xác định được ở lớp CPI/PPI. Hành động quân sự Trung Đông cuối tháng 2/2026 đóng cửa trên thực tế eo biển Hormuz, đẩy chỉ số năng lượng CPI tăng +26,9% trong bốn tháng và mở rộng khoảng cách headline-core (CPI 4,2% so với core 2,85%; PCE 4,1% so với core 3,4%) [RAW-OFFICIAL: BLS]. Song song, tariff nâng core goods trong khi core services/nhà ở tiếp tục giảm tốc [RAW-OFFICIAL: FOMC minutes], và ở cấp sản xuất — trước cả hai basket tiêu dùng này — khoảng cách PPI theo giai đoạn chế biến (Stage-1 trừ Stage-4) nới rộng từ +0,16pp (Jan) lên +5,73pp (May), vượt ngưỡng phân loại τ*≈+3pp từ tháng 4 [RAW-OFFICIAL: BLS Table D, tái xác nhận độc lập, xem `US_CPI_PPI_PCE_H1_2026.md`]. Ba cơ chế này — năng lượng, tariff, PPI broadening — là driver trực tiếp khiến FOMC bỏ ngôn ngữ cắt giảm và phát tín hiệu khả năng tăng lãi suất tại SEP 2026-06-17 [RAW-OFFICIAL: FOMC minutes 01/03/04-2026].

Điểm cần làm rõ ở đây là hawkish pivot này tác động lên **mặt lãi suất chính sách** của Fed, không tác động trực tiếp lên **mặt bảng cân đối**. RMP tiếp tục bơm đều +$42B/tháng UST bất kể diễn biến CPI/PPI, vì Perli đã xác nhận cơ chế này vận hành tách biệt khỏi chính sách tiền tệ [RAW-OFFICIAL, xem `fed-balance-sheet-h1-2026-unified-mode-deep.md`]. Vì vậy, đường dẫn từ CPI/PPI đến bảng cân đối Fed không đi qua RMP hay quy mô tổng tài sản, mà đi qua kỳ vọng lãi suất — thị trường định giá lại xác suất cắt giảm dựa trên cùng bộ dữ liệu lạm phát, và điều này thể hiện ở đầu ngắn đường cong (2Y) chứ không ở bảng H.4.1. Trong khi đó, một kênh thứ hai và độc lập đang vận hành giữa Fed và Kho bạc: vì RMP trung lập (không mở rộng danh mục ròng khi MBS runoff được bù bằng mua UST tương đương), Fed không hấp thụ bất kỳ phần nào trong $683B nợ gộp mà Kho bạc phát hành H1 2026 (+$249B YoY) [WEB-2026-05-06: Treasury Refunding]. Toàn bộ duration mới này — chủ yếu ở notes/bonds vì bills đã vượt mục tiêu TBAC 15–20% (hiện 21,44% nợ khả thị) — do khu vực tư nhân hấp thụ, và đây là cơ chế đứng sau ACM 10Y term premium chuyển dương trở lại (+0,67→+0,83% tháng 4–5, lần đầu từ 2023) [WEB-2026-06: NY Fed ACM].

Ở phía bảng cân đối Kho bạc, thành phần nợ phản ánh di sản extraordinary measures đầu năm: bills 21,44% ($6,76T, trên target), notes 50,58% ($15,94T) là mảng lớn nhất, bonds 17,14% ($5,40T), WAM toàn bộ nợ khả thị 70 tháng (5,83 năm) [WEB-2026-06-04: MSPD]. Average coupon 3,386% thấp hơn nhiều lợi suất thị trường hiện tại (10Y 4,49%), phản ánh phần lớn danh mục phát hành ở thời kỳ lãi suất thấp — nghĩa là mỗi đợt rollover đều tái định giá lên cao hơn, tự nó là một lực nâng chi phí lãi vay độc lập với issuance mới. Cầu đấu thầu phân hóa đúng theo kỳ hạn mà áp lực cung tập trung: notes/bonds vẫn khỏe (BTC 2,30–2,99) trong khi bills 13–26 tuần mềm 30–50bp — cho thấy áp lực cung dư thừa đang định vị đúng ở đoạn bills trung hạn, chưa lan sang coupon dài hạn nơi ACM term premium là gauge riêng.

Hai kênh hội tụ tại đường cong quan sát được ngày 02/07/2026 (2Y 4,14% / 10Y 4,49% / 30Y 4,98%), nhưng với tỷ trọng đóng góp rất khác nhau trong H1: 2s10s hẹp từ +72bp (Jan 2) xuống +35bp, do 2Y tăng +67bp trong khi 10Y chỉ +30bp và 30Y +12bp [RAW-OFFICIAL: Treasury.gov] — đây là bear-flattening front-end-led, tức kênh (1) kỳ vọng chính sách áp đảo biên độ. Real yield 10Y tăng gần trọn mức tăng danh nghĩa (+32bp so với +30bp tổng), trong khi breakeven đi ngang ~0 ròng — xác nhận thị trường TIPS **chưa** định giá rủi ro cascade PPI vào kỳ vọng lạm phát dài hạn, dù kênh (2) term premium đã bắt đầu dịch chuyển dương. Nói cách khác: trong H1 2026, thị trường phản ứng với lạm phát chủ yếu bằng cách rút kỳ vọng cắt giảm (đầu ngắn), chưa phải bằng cách định giá lại rủi ro lạm phát dài hạn hay áp lực cung duration (đầu dài) — hai lực sau vẫn đang tích lũy chứ chưa bộc lộ hết trong giá.

## TREASURY LAYER

Với desk thực hành, hàm ý là phải theo dõi hai kênh bằng hai bộ chỉ báo tách biệt thay vì gộp chung thành một câu chuyện "lạm phát đẩy lợi suất". Kênh kỳ vọng chính sách cần theo dõi CPI/PPI hàng tháng và ngôn ngữ FOMC/SEP song song với 2Y yield — đây là biến phản ứng nhanh nhất và đã dẫn dắt phần lớn chuyển động H1. Kênh cấu trúc duration cần theo dõi ACM 10Y term premium và BTC bills 13–26 tuần — biến phản ứng chậm hơn nhưng có thể tăng tốc nếu Q3 refunding (08/2026) nâng coupon size hoặc nếu Warsh đẩy RMP sang cấu hình bills-only, rút ngắn WAM Fed và trả duration về thị trường nhanh hơn hiện tại.

- **Trigger hội tụ kênh**: nếu June PPI (15/07) xác nhận Stage-3 vượt Stage-4 lần thứ ba liên tiếp VÀ Q3 refunding nâng size 10Y/30Y, hai kênh có thể cùng đẩy đường cong sang bear-steepening — theo dõi 2s10s đổi hướng như tín hiệu xác nhận sớm nhất.
- **Relative value**: TIPS breakeven 10Y hiện chưa phản ánh cascade risk từ PPI broadening — phân kỳ giữa PPI core-ex-trade tăng tốc và breakeven đi ngang là điểm relative-value cần theo dõi, không phải tín hiệu vào lệnh ngay.
- **Hedging**: duration hedge nên tính đến việc hai lực — hawkish pivot từ kênh lãi suất và duration extraction reversal từ kênh cung — đang cùng chiều làm tăng áp lực lên lợi suất, dù xuất phát từ hai cơ chế độc lập không triệt tiêu lẫn nhau.

---

## TIMING LAYER

| | PAST | PRESENT (H1 2026) | FUTURE |
|--|------|--------------------|--------|
| **Kênh kỳ vọng chính sách** | 2021–2022: Fed giữ khung "transitory" hơn một năm trước khi pivot | Fed pivot hawkish trong ~1–2 quý; 2Y +67bp trong khi FFR target đứng yên 3,50–3,75% — thị trường rút kỳ vọng cắt giảm | June CPI/PPI (14–15/07) và SEP kế tiếp là điểm định lại; nếu cascade tự tắt, kỳ vọng cắt giảm có thể quay lại và 2s10s mở rộng trở lại |
| **Kênh cấu trúc duration** | QE 2008–2021: Fed hút ~$4,5T UST duration, ACM 10Y chạm ~-100bp [LLM-E] | RMP trung lập ($4.488,1B UST, WAM 7,24yr không đổi); Kho bạc phát hành $683B gross mà Fed không bù; ACM +0,67→+0,83% | Q3 refunding (08/2026) là phép thử coupon size; nếu Warsh chuyển RMP sang bills-only, WAM Fed rút ngắn nhanh, đẩy nhanh term premium về vùng +150–200bp [LLM-E] |
| **Hội tụ tại đường cong** | 2022–2023 inversion → 2024–2025 re-steepening chậm | Bear-flattening nội bộ H1 (2s10s +72bp→+35bp), front-end-led, không phải long-end-led như khung đa năm gợi ý | Nếu hai kênh cùng kích hoạt (PPI cascade xác nhận + coupon supply tăng), khả năng chuyển sang bear-steepening đồng thời với hawkish hơn — tổ hợp chưa quan sát trong H1 |

**Velocity**: kênh kỳ vọng chính sách phản ứng theo phiên–tuần (mỗi công bố CPI/PPI, mỗi FOMC); kênh cấu trúc duration phản ứng theo tháng–quý (RMP/MBS pace theo tháng, refunding theo quý, ACM theo tháng).

**Synchronization risk**: ba mốc lịch có thể trùng nhau trong H2 — June CPI/PPI (14–15/07), Q3 refunding (08/2026), FBO cuối Q3 (30/09) — nếu trùng thời điểm, cả hai kênh có thể cùng lúc đẩy lợi suất tăng ở cả hai đầu đường cong mà không có ON RRP làm đệm (đã cạn còn $2,3B) cho phần reserves liên đới.

## FEEDBACK / BOUNDARY

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|-------------------|--------------------|---------|
| Kênh kỳ vọng chính sách | 2Y yield + PPI Stage-gap | Stage-gap tiếp tục tăng trên τ*≈+3pp kèm 2Y tăng thêm | Stage-gap +5,73pp (May), 2Y 4,14% (Jul 2) |
| Kênh cấu trúc duration | ACM 10Y term premium + BTC bills 13-26wk | Term premium nới >50bp trong <3 tháng; BTC bills dưới 2,3 liên tiếp | +0,67–0,83% (Apr-May); bills BTC 2,32–2,79, gần ngưỡng |
| Hội tụ tại đường cong | 2s10s spread | Đổi hướng từ flattening sang steepening trong khi 2Y vẫn tăng | +35bp (Jul 2), đang hẹp |
| Định giá rủi ro cascade | TIPS breakeven 10Y | Bắt đầu repricing lên | Đi ngang 2,20–2,48%, chưa phản ứng |

**Failure conditions**: khung hai-kênh này thất bại nếu một trong hai biến động độc lập với biến còn lại trong dữ liệu H2 — ví dụ nếu 2Y tiếp tục tăng nhưng ACM term premium đứng yên (kênh cấu trúc không kích hoạt dù kênh kỳ vọng mạnh lên), hoặc ngược lại nếu term premium nới rộng nhanh trong khi CPI/PPI hạ nhiệt (kênh cấu trúc tách khỏi driver lạm phát, thuần túy do cung). Cả hai kịch bản đều có thể xảy ra và đòi hỏi theo dõi tách biệt thay vì gộp chung thành một chỉ báo duy nhất.

---

## DIAGRAM

```
HAI KÊNH HỘI TỤ TẠI ĐƯỜNG CONG — H1 2026

KÊNH 1: KỲ VỌNG CHÍNH SÁCH (nhanh, thắng thế biên độ H1)
─────────────────────────────────────────────────────────
CPI/PPI cascade                FOMC hawkish pivot         Thị trường rút kỳ vọng cắt
(năng lượng +26,9%, PPI   ──►  (bỏ tín hiệu cắt,     ──►  (2Y: 3,47%→4,14%, +67bp)
 gap +5,73pp, vượt τ*)         phát tín hiệu hike)              │
                                                                 ▼
                                                    2s10s HẸP LẠI (+72bp→+35bp)
                                                    = BEAR-FLATTENING front-end-led

KÊNH 2: CẤU TRÚC CUNG-CẦU DURATION (chậm, mới bắt đầu)
─────────────────────────────────────────────────────────
Kho bạc phát hành gộp          RMP trung lập               Tư nhân hấp thụ toàn bộ
$683B H1 (+$249B YoY)     ──►  (Perli: tách biệt      ──►  duration mới; ACM 10Y term
                                khỏi CS tiền tệ,             premium +0,67%→+0,83%
                                WAM Fed không đổi 7,24yr)         │
                                                                   ▼
                                                    Bills 13-26wk BTC mềm 30-50bp
                                                    (đúng vị trí TBAC cảnh báo)

HỘI TỤ:  Yield 10Y quan sát (4,49%, 02/07) = phần lớn từ real yield (+32bp, kênh 1
         qua kỳ vọng đường đi FFR) + phần nhỏ từ term premium (kênh 2, mới dương
         trở lại). Breakeven đi ngang ⇒ TIPS chưa định giá rủi ro cascade từ PPI.

HÀM Ý CHÍNH SÁCH FED:
  - Nếu June PPI (15/07) xác nhận Stage-3>Stage-4 lần 3 → SEP revision hướng lên
  - Nếu Q3 refunding (08/2026) tăng size 10Y/30Y → kênh 2 tăng tốc, có thể đổi
    hướng 2s10s từ flattening sang steepening
  - RMP composition (giữ nguyên vs. Warsh bills-only) là biến thể chế quyết định
    tốc độ kênh 2 trong H2, độc lập với lộ trình lãi suất chính sách
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed với điều chỉnh cấu trúc — chuỗi CPI/PPI→Fed BS→Treasury BS→Curve không phải một đường thẳng mà là hai kênh song song (kỳ vọng chính sách qua lãi suất; cấu trúc duration qua bảng cân đối), hội tụ tại đường cong với tỷ trọng lệch mạnh về kênh kỳ vọng chính sách trong H1 2026 |
| **Net Effect** | Bear-flattening quan sát được (2s10s +72bp→+35bp) chủ yếu do thị trường rút kỳ vọng cắt giảm (kênh 1), không phải do term premium/cung duration đẩy đầu dài (kênh 2) — dù kênh 2 đã bắt đầu dịch chuyển và có thể đảo tỷ trọng trong H2 nếu PPI cascade và Q3 refunding cùng xác nhận |
| **Treasury Action** | Theo dõi hai bộ chỉ báo tách biệt (2Y+Stage-gap cho kênh 1; ACM term premium+BTC bills cho kênh 2) thay vì một chỉ báo gộp; 2s10s đổi hướng là tín hiệu sớm nhất cho việc hai kênh bắt đầu cùng kích hoạt |
| **Confidence** | TIER B — mỗi số liệu thành phần kế thừa mức tin cậy từ tài liệu gốc (CPI/PPI: RAW-OFFICIAL verified; Fed BS: RAW-OFFICIAL H.4.1 + CONFIRMED flow; Treasury/Curve: RAW-OFFICIAL Treasury.gov). Khung "hai kênh song song" là diễn giải tổng hợp bậc hai của Claude, chưa được kiểm chứng độc lập bởi nguồn thứ ba |
| **Critical Caveat** | Nếu dữ liệu H2 cho thấy hai kênh di chuyển độc lập nhau (xem Failure Conditions) thay vì hội tụ như mô tả, khung này cần viết lại — đây không phải kết luận đóng mà là giả thuyết đang theo dõi song song với ba cluster gốc |

---

## NEXT STEPS

```bash
# Tài liệu này là tổng hợp bậc hai — không tạo/sửa raw source hay wiki node mới
# ✓ 06_publish/2026-07-03_us-inflation-fed-treasury-curve-policy-chain-h1-2026.md (file này)

# Data gaps kế thừa từ ba cluster gốc (ưu tiên giảm dần)
# → June CPI (BLS, 14/07) + June PPI (BLS, 15/07) — xác nhận/phủ định kênh 1 tiếp tục dẫn dắt
# → ACM 10Y term premium tháng 6 — vẫn thiếu ở cả ba tài liệu gốc, cần cho kênh 2
# → Q3 2026 Refunding Announcement (08/2026) — phép thử trực tiếp cho tốc độ kênh 2
# → FBO cuối Q3 (30/09) trùng lịch coupon settle — điểm hội tụ rủi ro tiếp theo
# → RMP composition decision (Warsh bills-only hay giữ nguyên) — biến thể chế
#   chưa xác nhận, quyết định quỹ đạo kênh 2 toàn bộ H2

python librarian.py embed --incremental && python librarian.py sync
```

*MODE DEEP v1 (second-order synthesis) | 2026-07-03 | Refs: liên kết ba tài liệu gốc trong header | [[US_CPI_PPI_PCE_H1_2026]] · [[PPI_Stage_Differential_IO_Cascade_Diagnostic]] · [[Fed_Duration_Extraction_Term_Premium]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_Debt_Management_Strategy]] · [[ACM_Curve_Decomposition]]*
