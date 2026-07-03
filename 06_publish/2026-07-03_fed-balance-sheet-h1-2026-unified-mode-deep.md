# Fed Balance Sheet H1 2026 — Tổng Hợp MODE DEEP: Ngưỡng Sàn, RMP/TGA, Duration
> MODE DEEP | 2026-07-03 | Analyst: Claude (claude-sonnet-5)
> Nguồn: [RAW-OFFICIAL: H.4.1 24/06/2026] · [RAW-OFFICIAL: Fed_H41_Weekly_Flow_H1_2026 — 23 điểm] · [RAW-OFFICIAL: Treasury Q2 2026 Refunding] · [RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026] · [RAW-BOOK: Duffie BPEA 2026] · [RAW-BOOK: Copeland–Duffie–Yang 2025] · [WEB-2026-04-11: Andreopoulos] · [WEB-2026-02-17: Cochrane] · [WEB-2026-06: ACM 10Y term premium] · [LLM-ref: Krishnamurthy-Vissing-Jorgensen 2011/2013, Gagnon et al. 2011, D'Amico-King 2013]
>
> **Ghi chú (2026-07-03):** Đã hợp nhất vào báo cáo tổng hợp toàn cảnh `06_publish/2026-07-03_us-macro-financial-master-synthesis-h1-2026.md` (CPI/PPI + Fed BS + Treasury/curve + Warsh). File này vẫn giữ nguyên làm nguồn chi tiết gốc.

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Bảng cân đối Fed H1 2026 chịu tác động của ba cơ chế nào — ngưỡng sàn hệ thống thanh toán, bất đối xứng nhịp RMP/TGA, và đảo chiều duration/term premium — và chuỗi thực nghiệm 23 điểm H.4.1 xác nhận hay điều chỉnh mỗi cơ chế ở mức nào? |
| **Asset / Currency** | USD · Bank Reserves · UST (bills/notes/bonds) · MBS · TGA |
| **Temporal Status** | CURRENT 🟢 — stock as-of 24/06/2026; flow 23/26 tuần Jan–Jun 2026 |
| **Thesis** | Ba cơ chế được xác nhận thực nghiệm ở các mức độ khác nhau trong H1 2026. (1) Ngưỡng sàn hệ thống thanh toán là ràng buộc cứng nhưng chưa từng bị chạm: đáy thật $2.901,8B (22/04) — thấp hơn mốc "$3.000B" hay trích dẫn ~$100B — không kích hoạt stress SOFR–IORB. (2) Bất đối xứng nhịp RMP (trend +$42B/tháng UST, RAW-OFFICIAL) và TGA (event, biên $310,1B/2 tuần quanh mùa quyết toán thuế) được xác nhận chặt qua một thí nghiệm tự nhiên khép kín — identity `ΔReserves≈RMP−ΔTGA` khớp với residual chỉ +$62,9B trên biến động -$277,3B dự đoán. (3) Đảo chiều duration: stock UST của Fed không đổi ở $4.488,1B (WAM 7,24 năm, CONFIRMED) trong khi Kho bạc phát hành ròng $683B gross H1 mà Fed không bù đắp — ACM 10Y term premium đã tăng về +0,6–0,8% (Apr–May), và cầu đấu thầu bắt đầu mềm cục bộ ở bills trung hạn, đúng vị trí TBAC cảnh báo vượt target. |

---

## MACRO LAYER

| Chiều | H1 2026 |
|-------|---------|
| **Regime** | Ample Reserves (Regime A) — Fed giữ reserves ở ngưỡng sàn hiện tại, không nới lỏng hay thắt chặt chủ động |
| **Policy Anchor** | IORB đóng vai trò ngưỡng sàn 3,75%; SRF = IORB+10bp trần (rò rỉ); SOFR 25/06 = 3,64% (SOFR−IORB −11bp) [RAW-OFFICIAL: sofrrate.com] |
| **Balance Sheet** | Total assets $6.735,6B: UST $4.488,1B (Bills $486B / Notes-Bonds $3.615B / TIPS $279B) / MBS $1.961,6B [RAW-OFFICIAL: H.4.1 24/06/2026] |
| **Fiscal** | Gross borrowing H1 $683B (+$249B YoY) [RAW-OFFICIAL: Treasury Q2 2026 Refunding]; trần nợ $41,1T (One Big Beautiful Bill Act) |
| **Tension** | QT kết thúc 01/12/2025; RMP chạy từ 10/12/2025; ON RRP $2,3B ≈ 0 (total reverse repo $333,6B gồm foreign pool); reserves $2.951,4B trong dải H1 đã xác nhận |

Ba chế độ cần phân biệt rõ vì mỗi chế độ có tác động duration khác nhau: QE (2008–2021) tạo net reserves mới đồng thời hút duration khỏi thị trường tư nhân — nới lỏng tài chính thực sự qua cả hai kênh reserves và term premium. QT (giữa 2022–01/12/2025) cắt assets, trả duration về thị trường nhưng là thắt chặt yếu qua kênh reserves (Atlanta Fed: $2,2T QT ≈ +0,29–0,74% rate-equivalent trong 3 năm [RAW-BOOK: Conks, citing Bin Wei]). RMP (từ 10/12/2025) giữ tổng assets phẳng — Perli [RAW-OFFICIAL: 26/03/2026] xác nhận trực tiếp: "hoàn toàn tách biệt khỏi chính sách tiền tệ" — nghĩa là RMP không hút thêm duration mới nhưng cũng không mở rộng để hấp thụ phát hành Kho bạc mới — khu vực tư nhân phải hấp thụ toàn bộ net issuance mới thay cho Fed.

## PLUMBING LAYER

Ngưỡng sàn cứng của reserves bắt nguồn từ cấu trúc hệ thống thanh toán hậu-GFC, không phải từ lựa chọn chính sách. Ba yếu tố neo cầu reserves ở mức cao: GSIB ngại daylight overdraft (toàn hệ thống hiện dưới $5B/ngày so với ~$120B/ngày của top-10 ngân hàng năm 2007 [RAW-BOOK: Duffie BPEA 2026 §I.D]); IORB trả gần lãi suất thị trường triệt tiêu động lực cho vay liên ngân hàng (thị trường fed funds liên ngân hàng co lại dưới $3B/ngày); và chi phí giám sát hậu-SVB (FDIC fee 42bp thường xuyên + 13bp đặc biệt, cộng leverage requirements) làm tăng ma sát tái phân phối reserves giữa các ngân hàng. Giám sát viên coi UST không phải cash-equivalent khi thanh lý quy mô lớn (CLAR/RLAP), khiến reserves — không phải UST — là tài sản thanh khoản ưu tiên. Mốc "$3.000B ≈ 9% GDP" [WEB-2026-04-11: Andreopoulos] từng được trích dẫn như ngưỡng sàn tham chiếu, nhưng chuỗi 23 điểm H.4.1 thực nghiệm cho thấy đáy thật của H1 thấp hơn: reserves chạm $2.901,8B ngày 22/04/2026 mà SOFR–IORB trung bình tháng 4 vẫn ở −11bp, không có tín hiệu payment throttling [RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026.md]. Ngưỡng sàn "binding" theo nghĩa Duffie — mức mà dưới đó dealer bắt đầu trì hoãn thanh toán ra để tự bảo vệ số dư — vẫn chưa từng bị chạm trong H1 2026; mốc $3.000B nên được đọc là ước tính biên trên thận trọng, không phải ngưỡng đã kiểm chứng.

Với ON RRP đã cạn gần như hoàn toàn ($2,3B, so với >$2.000B năm 2023 từng làm đệm hấp thụ toàn bộ TGA swing), identity flow co lại còn `ΔReserves ≈ RMP_trend − ΔTGA_event − ΔCurrency`, và mọi biến động TGA truyền gần như 1:1 vào reserves mà không có tầng trung gian. RMP bơm đều đặn +$42B/tháng UST ròng — nay CONFIRMED RAW-OFFICIAL từ chuỗi 23 điểm, thay cho ước tính [LLM-E] "~$40B/tháng" trước đó — trong khi MBS runoff đo được −$14B/tháng (thấp hơn ước tính ban đầu $15–20B/tháng). Đối lập với nhịp trend đều này, TGA di chuyển theo sự kiện: hai tuần 08/04→22/04/2026, quanh ngày quyết toán thuế thu nhập cá nhân 15/04, tạo thành một thí nghiệm tự nhiên khép kín — TGA tăng $310,1B (từ $697,1B lên $1.007,2B) trong khi reserves giảm $214,4B (từ $3.116,2B xuống $2.901,8B), tổng tài sản gần như không đổi (+$13,5B) và currency-in-circulation phẳng tuyệt đối (+$0,5B). Kiểm định identity đầy đủ cho cửa sổ này cho `ΔReserves_dự_đoán = ΔAssets−ΔTGA−ΔRRP−ΔCurrency = −277,3B`, so với ΔReserves thực tế −214,4B — residual "other factors" chỉ +$62,9B. Đây là bằng chứng thực nghiệm chặt nhất trong cả cluster nghiên cứu cho identity `ΔReserves≈RMP−ΔTGA`: một sự kiện tài khóa đơn lẻ, có thể dự báo trước theo lịch thuế hàng năm, di chuyển reserves hơn $200B trong hai tuần, không qua bất kỳ tầng trung gian nào khác ngoài quan hệ identity trực tiếp nêu trên.

Song song với biến động ngắn hạn ở đầu reserves, một lực chậm hơn nhưng có tác động tương đương đang vận hành ở đầu dài của đường cong: đảo chiều duration extraction. Khi Fed mua một trái phiếu dài hạn trong kỷ nguyên QE, Fed hút DV01 khỏi khu vực tư nhân và ghi có reserves qua đêm — cơ chế mà đồng thuận học thuật (Gagnon et al. 2011; Krishnamurthy–Vissing-Jorgensen 2011/2013; D'Amico–King 2013 [LLM-ref]) ước tính nén khoảng 91–100bp lợi suất 10Y trên mỗi $1T duration ròng bị hút, và mức nén này tăng thêm do cầu preferred habitat không co giãn của bảo hiểm nhân thọ và quỹ hưu trí. Tại 24/06/2026, Fed vẫn giữ $4.488,1B UST với WAM 7,24 năm CONFIRMED [RAW-OFFICIAL: H.4.1 maturity buckets calc] — stock effect không đổi ở mức này vì RMP trung lập (MBS runoff được bù bằng mua UST tương đương, không mở rộng danh mục ròng). Nhưng mẫu số thị trường đang tăng: Kho bạc phát hành gross $683B H1 2026 (+$249B YoY) mà khu vực tư nhân phải hấp thụ toàn bộ, không có Fed bù đắp phần mới. Tỷ lệ duration Fed nắm giữ trên tổng thị trường giảm theo cơ học, và ACM 10Y term premium phản ánh đúng hướng đó — tăng dần về +0,73% (30/04) và đỉnh +0,83% (15/05) trước khi giảm nhẹ về +0,67% (28/05) [WEB-2026-06], còn xa dưới mức cơ sở lịch sử tiền-QE (~+150–200bp [LLM-E]) nhưng đã ra khỏi vùng âm ghi nhận tại đỉnh QE (~-100bp [LLM-E]).

Ba dòng bằng chứng — ngưỡng sàn reserves chưa từng bị test dù đã chạm mức thấp hơn ước tính, TGA event lớn nhất H1 được identity xác nhận chặt, và term premium đầu dài đang nới rộng dần cùng lúc cầu đấu thầu bắt đầu phân hóa — cho một kết luận nhất quán. Ở phần đấu thầu, notes/bonds vẫn khỏe suốt H1 (BTC 2,30–2,99, không xu hướng), nhưng bills kỳ hạn trung (13/17/26 tuần) mềm khoảng 30–50bp từ Jan-Feb (BTC 2,71–3,30) xuống June (2,32–2,79), đúng vị trí TBAC cảnh báo (Q2 Refunding Statement 06/05/2026) rằng bills đã vượt target 15–20% danh mục nợ khả mại — hệ quả trực tiếp của extraordinary measures Jan–Apr 2026 [RAW-OFFICIAL: Treasury_Q2_2026_Refunding_Details.md]. Điều chỉnh giá hiện tập trung đúng ở đoạn cung dư thừa nhất của đường cong, chưa lan sang đầu ngắn nhất (vẫn được đỡ bởi cầu quasi-cash) hay đầu dài nhất (nơi ACM term premium là gauge vận hành riêng). H1 2026 vì vậy là một hệ thống đã hấp thụ ít nhất một cú sốc tài khóa định kỳ lớn ở đầu ngắn (mùa thuế, +$310B TGA/2 tuần) mà không đẩy reserves xuống dưới ngưỡng sàn thật, đồng thời hấp thụ nguồn cung Treasury mới chủ yếu qua điều chỉnh giá ở đầu dài — cả hai là biểu hiện đồng thời của cùng một áp lực tài khóa-tài chính cơ bản: Kho bạc vay nhiều hơn, và khu vực tư nhân phải hấp thụ nhiều hơn cả rủi ro thanh khoản lẫn rủi ro duration so với bất kỳ thời điểm nào kể từ 2008.

## TREASURY LAYER

Desk cần phân biệt ba loại rủi ro đồng thời hiện diện và dùng dải tham chiếu đã xác nhận thay cho ước tính biên rộng trước đây. Ở chân trời ngắn (ngày–tuần), SOFR–IORB là gauge chính, không phải EFFR — dải reserves tham chiếu nay là $2.901,8B–$3.129,6B (không phải $2.918,6B–$3.111,5B từ ước tính trước), và lịch quyết toán thuế cá nhân (15/04, và các mốc quý/năm tương tự) nên được đưa vào lịch rủi ro reserves cùng cấp độ với FBO cuối quý — đây là sự kiện TGA lớn nhất quan sát được trong H1 và có thể dự báo trước theo lịch cố định hàng năm, khác với FBO (cũng dự báo được) hay TGA rebuild sau debt-ceiling (khó dự báo hơn). Ở chân trời trung hạn (tuần–tháng), RMP là backstop trend +$42B/tháng, không phải van điều chỉnh theo ngày; nếu một event hút TGA vượt nhịp bơm trend trong cùng khung thời gian, reserves có thể giảm xuống dưới $2.901,8B trước kỳ RMP tiếp theo — theo dõi riêng BTC bills 13–26 tuần như gauge sớm cho áp lực cấu trúc, vì điểm mềm này xuất hiện trước khi lan tới notes/bonds hay ACM term premium. Ở chân trời dài (tháng–năm), sự phân tách giữa mức lợi suất 10Y quan sát được và cấu phần term premium là thông tin cần thiết cho quyết định vị thế duration: 4,40% với term premium +0,7% và kỳ vọng đường đi ~3,7% là một trạng thái khác hẳn 4,40% với term premium -0,2% (kỷ nguyên QE) và kỳ vọng đường đi cao hơn — chỉ ACM decomposition mới tách được hai lực này, không thể suy ra từ yield tuyệt đối.

- **Ngắn hạn:** SOFR–IORB daily + lịch quyết toán thuế/FBO cuối quý (Q2-end 30/06 vừa qua; Q3-end 30/09 kế tiếp) là hai biến dự báo chính cho reserves event; nếu reserves in dưới $2.901,8B kèm SOFR–IORB nới rộng đồng thời, đó là bằng chứng đầu tiên ngưỡng sàn thật đã bị chạm.
- **Trung hạn:** RMP composition (bills vs coupons) là tín hiệu về intent thể chế; map lịch coupon refunding mid-month vào funding cost model; theo dõi BTC bills 13–26 tuần như gauge cấu trúc sớm.
- **Dài hạn:** Track ACM 10Y term premium (NY Fed) song song với BTC notes/bonds — hai kênh áp lực khác nhau (cấu trúc bills vs duration dài hạn coupon supply) không nên gộp chung một chỉ báo; nếu Warsh chuyển RMP sang bills-only, WAM 7,24 năm rút ngắn nhanh, trả duration về thị trường và tạo thắt chặt cấu trúc từ phía cung, độc lập với lộ trình lãi suất chính sách.

---

## TIMING LAYER

| | Past | Present H1 2026 (23 điểm xác nhận) | Future |
|--|------|-------------------------------------|--------|
| **Reserves / Floor** | 2019: reserves $1,4T → SOFR–IORB +315bp [RAW-BOOK: Duffie Fig.9]; 2023: ON RRP >$2.000B làm đệm hấp thụ TGA swing | Dải $2.901,8B–$3.129,6B; đáy 22/04 (mùa thuế) không kích hoạt stress; ON RRP $2,3B ≈ 0, không còn đệm | Nếu TGA event $310B+ trùng FBO cuối quý (30/09), đáy reserves mới có thể thấp hơn 22/04 — ngưỡng sàn thật chưa xác định |
| **RMP / TGA** | QT2 kết thúc 01/12/2025; RMP khởi động 10/12/2025 | RMP +$42B/tháng UST, MBS −$14B/tháng (CONFIRMED, ổn định 23 điểm); TGA đỉnh gắn quyết toán thuế 15/04, không ngẫu nhiên | Lịch thuế Q3/Q4 doanh nghiệp + FBO 30/09 là điểm rủi ro kế tiếp có thể dự báo |
| **Duration / Term Premium** | QE 2008–2021: hút ~$4,5T UST + ~$1,8T MBS duration; ACM 10Y chạm ~-100bp [LLM-E] tại đỉnh | Stock không đổi ở $4.488,1B (WAM 7,24yr); ACM +0,67–0,83% (Apr-May), tăng dần từ vùng nén | Nếu phát hành gross tiếp tục ~$683B/H1 không Fed bù đắp, term premium tiếp tục nới; Warsh bills-only sẽ đẩy nhanh về +150-200bp [LLM-E] |
| **Auction Demand** | — | Notes/bonds khỏe (BTC 2,30–2,99); bills 13-26wk mềm ~30-50bp, đúng vị trí TBAC cảnh báo | Q3 refunding (08/2026) là phép thử coupon; theo dõi tỷ trọng bills nếu không giảm dưới target |

**Velocity:** Flow reserves truyền dẫn trong ngày (Fedwire); TGA event tài khóa theo lịch tuần-đến-hai-tuần; RMP/MBS trend hiện rõ ở tần suất tháng; term premium phản ứng theo tháng–quý; auction demand phản ứng theo phiên.

**Synchronization risk:** Ba yếu tố — TGA event lớn, FBO cuối quý, và khe nhịp RMP — nếu trùng thời điểm có thể cùng lúc làm tăng áp lực ở đầu ngắn mà không có ON RRP làm đệm; đồng thời, nếu term premium tiếp tục nới đúng lúc reserves căng ở đầu ngắn, hai áp lực (thanh khoản ngắn hạn + duration dài hạn) cùng làm tăng chi phí funding và chi phí tài sản thế chấp cho cùng một loại tổ chức (bảo hiểm/hưu trí nắm cả reserves-adjacent short paper lẫn duration dài).

## FEEDBACK / BOUNDARY

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|------------------|-------------------|---------|
| Reserves floor | SOFR–IORB daily | Đáy dưới $2.901,8B kèm SOFR nới rộng đồng thời | 24/06: $2.954,5B — trong dải |
| TGA event | Lịch thuế + FBO cuối quý | Swing >$310,1B/2 tuần trùng FBO | Theo dõi FBO 30/09 như điểm tương tự kế tiếp |
| Term premium | ACM 10Y (NY Fed) | Nới >50bp trong <3 tháng | +0,67–0,83% (Apr-May), thiếu điểm tháng 6 [gap] |
| Auction demand | BTC bills 13-26wk | BTC dưới 2,3 liên tiếp | Đã mềm về 2,32–2,79, gần ngưỡng |
| Deferred asset | Fed remittance to Treasury | Tiếp tục $0 kéo dài + tăng quy mô | $0 ước tính, đỉnh lịch sử ~$200B 2023-24 [LLM-E] |

**Failure conditions:** Cú sốc mùa thuế (+$310B/2 tuần) là sự kiện TGA lớn nhất quan sát được trong H1 và KHÔNG đẩy reserves xuống dưới ngưỡng sàn — kịch bản kiểm định ngưỡng sàn thật đòi hỏi một cú sốc lớn hơn hoặc trùng thời điểm với FBO cuối quý (30/09); hai điều kiện này chưa từng xảy ra đồng thời trong dữ liệu hiện có. Đối với duration/term premium: nếu Fed triển khai TOMO sterilization theo sự kiện (Duffie, ưu tiên số một, không cần luật mới), rủi ro khe nhịp RMP/TGA giảm mạnh nhưng không thay đổi hướng đảo chiều term premium; nếu Warsh chuyển RMP sang bills-only, hai chỉ báo di chuyển ngược chiều nhau (rủi ro chạm ngưỡng sàn giảm vì bills runoff nhanh hơn, rủi ro term premium tăng vì WAM rút ngắn) — đây là biến số thể chế chưa xác nhận, quyết định toàn bộ quỹ đạo H2 2026.

---

## DIAGRAM

```
FED BALANCE SHEET H1 2026 — TỔNG QUAN BA CƠ CHẾ (Total Assets $6,735.6B | 24/06/2026)
════════════════════════════════════════════════════════════════════════════════

  ASSETS                                    LIABILITIES
  ┌─────────────────────────────┐          ┌──────────────────────────────┐
  │ UST $4,488.1B                │  P&L     │ RESERVES $2,951.4B           │
  │  Notes/Bonds $3,615B (81%)   │ MISMATCH │  H1 band: $2,901.8B–$3,129.6B│
  │  Bills $486B · TIPS $279B    │◄────────►│  22/04 = đáy H1, ngưỡng sàn  │
  │                              │          │  CHƯA TEST                   │
  │  WAM 7.24yr [RAW-OFFICIAL]   │coupon~2-3%│  (SOFR-IORB avg -11bp/th.4,  │
  │                              │ cố định  │   không stress tại đáy này)  │
  │ MBS $1,961.6B                │ vs IORB  │                              │
  │  runoff -$14B/th [RAW-OFF]   │ 3.75% nổi│ + RMP +$42B/th UST (TREND)   │
  └─────────────────────────────┘          │ − TGA: event, không đều      │
                                            │ ON RRP $2.3B ≈ 0 (hết đệm)   │
                                            └──────────────────────────────┘

  ĐẦU DÀI — DURATION/TERM PREMIUM            ĐẦU NGẮN — THÍ NGHIỆM TỰ NHIÊN
  ─────────────────────────────              (mùa thuế, 08/04→22/04/2026)
  Fed stock không đổi $4,488.1B UST          TGA   $697.1B → $1,007.2B (+310.1B)
  Kho bạc phát hành mới $683B/H1 gross       Reserves $3,116.2B → $2,901.8B (-214.4B)
  (tư nhân hấp thụ toàn bộ, Fed không bù)    ΔRes dự đoán = Assets-TGA-RRP-Curr = -277.3B
  → ACM 10Y term premium +0.67→+0.83%        residual "other factors" = +62.9B
    (Apr-May 2026), hướng nới dần            ⇒ TGA giải thích gần trọn biến động reserves
  → Bills 13-26wk BTC mềm ~30-50bp           ⇒ bằng chứng thực nghiệm chặt nhất cho
    (đúng vị trí TBAC cảnh báo vượt target)     identity ΔReserves ≈ RMP_trend − ΔTGA_event
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed — ba cơ chế được xác nhận ở các mức độ khác nhau: ngưỡng sàn hệ thống thanh toán là ràng buộc cứng chưa từng bị chạm (đáy $2.901,8B không stress); bất đối xứng nhịp RMP/TGA được identity xác nhận chặt qua thí nghiệm tự nhiên mùa thuế; đảo chiều duration đang diễn ra chậm nhưng nhất quán (term premium +0,67→+0,83%, bills demand mềm cục bộ) |
| **Net Plumbing Effect** | Reserves dao động trong dải đã xác nhận, không giảm xuống dưới ngưỡng sàn; TGA event mùa thuế là biến động lớn nhất H1 và được giải thích gần trọn bởi một biến số duy nhất; term premium nới dần khi tư nhân hấp thụ toàn bộ net issuance mới |
| **Treasury Action** | Dùng dải $2.901,8B–$3.129,6B làm ngưỡng sàn tham chiếu; đưa lịch thuế vào cùng cấp rủi ro với FBO cuối quý; theo dõi BTC bills 13-26 tuần và ACM term premium như hai gauge độc lập cho hai loại áp lực khác nhau |
| **Confidence** | TIER B — stock (H.4.1) và flow (23/26 điểm tuần) đều RAW-OFFICIAL; RMP/MBS pace CONFIRMED; WAM 7,24yr CONFIRMED; term premium mức Apr-May RAW/WEB nhưng lịch sử 2010-2021 và hệ số cung KVJ vẫn [LLM-E]/[LLM-ref]; deferred asset và "other factors" residual đầy đủ chưa decompose |
| **Critical Caveat** | Kết luận "ngưỡng sàn thấp hơn $3.000B" chỉ dựa trên các lần chạm đáy chưa gây stress — chưa có bằng chứng ngưỡng sàn thật nằm ở đâu, chỉ có bằng chứng về nơi nó KHÔNG nằm; đồng thời, quỹ đạo term premium phụ thuộc vào một biến số thể chế chưa xác nhận (Warsh bills-only hay giữ nguyên composition RMP) |

---

## NEXT STEPS

```bash
# Data gaps còn lại (ưu tiên giảm dần)
# → ACM tháng 6/2026 — vẫn thiếu, đã thử nhiều nguồn (NY Fed 403, macromicro 403)
# → SOFR daily Jan-May 2026 — chỉ có monthly avg
# → "Other factors" H.4.1 residual decomposition đầy đủ (~$47-63B tùy cửa sổ)
# → Krishnamurthy-Vissing-Jorgensen (2011,2013); Gagnon et al. (2011); D'Amico-King (2013) — định lượng hệ số kênh cung
# → H.4.1 tuần đầu tiên 07/2026 — chưa publish

# File này hợp nhất 3 báo cáo nguồn (không thay thế, chỉ tổng hợp góc nhìn mới nhất):
# - 2026-06-29_fed-balance-sheet-synthesis.md (3 cơ chế cấu trúc, stock)
# - 2026-07-02_fed-balance-sheet-flow-mechanics-h1-2026.md (flow thực nghiệm 23 điểm)
# - 2026-06-29_fed-duration-extraction-term-premium.md (kênh cung duration/term premium)

python librarian.py embed --incremental && python librarian.py sync
```

*MODE DEEP v1 (unified) | 2026-07-03 | Refs: P1 · P2 · P3 · P4 | [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Standing_Repo_Facility_SRF_Mechanics]] · [[Fed_Duration_Extraction_Term_Premium]] · [[ACM_Curve_Decomposition]]*
