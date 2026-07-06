# Bảng Cân Đối Fed Đầu Q3 2026 — Tổng Tài Sản, Thanh Khoản, Duration, và Khung "Ample Reserves" Chính Thức
> MODE DEEP | 2026-07-06 | Analyst: Claude (claude-sonnet-5)
> Nguồn: [RAW-OFFICIAL: Fed_H41_July2026_Balance_Sheet_Update.md — H.4.1 release 02/07/2026, as-of 01/07/2026] · [RAW-OFFICIAL: Fed_Ample_Reserves_Official_Framework_2026.md — FOMC statements 29/10/2025, 17/06/2026, minutes 29/04/2026] · [WEB-2025-11: NY Fed Staff Report 1019] · [RAW-OFFICIAL: Treasury_Buyback_Duration_Fresh_H1_2026.md — MSPD, TBAC 05/05/2026] · Đối chiếu với cluster nghiên cứu trước (`2026-07-03_fed-balance-sheet-h1-2026-unified-mode-deep.md`, baseline 24/06/2026)

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Đầu Q3 2026, bảng cân đối Fed đứng ở đâu trên bốn trục — tổng tài sản, thanh khoản/reserves, duration UST, và tiến trình chuẩn hóa — và khung "ample reserves" mà FOMC/NY Fed công bố chính thức định nghĩa ngưỡng đó bằng ngôn ngữ hay con số nào? |
| **Asset / Currency** | USD · Bank Reserves · UST (bills/notes/bonds) · MBS · TGA |
| **Temporal Status** | CURRENT 🟢 — stock as-of 01/07/2026 (H.4.1 release 02/07) |
| **Thesis** | Reserves phục hồi từ đáy mùa thuế lên gần đỉnh dải H1 ($3,077,0B, +$122,6B/tuần) khi TGA giảm $111,3B — khớp hướng với cơ chế RMP-TGA đã xác nhận trước. Nhưng khung "ample" mà chính FOMC dùng vẫn hoàn toàn định tính (statement 17/06/2026 chỉ nói "duy trì mức reserves ample", không có ngưỡng số); ngưỡng định lượng có trọng lượng nghiên cứu chính thức gần nhất — NY Fed Staff Report 1019 — đặt tại reserves >12-13% tổng tài sản ngân hàng cho chế độ abundant, một proxy khác hẳn về cơ sở đo so với mốc "$3,000B/9% GDP" đã dùng trước đây. Song song, RMP cho tín hiệu pace chậm lại (~$26-29B/tháng quy đổi từ chu kỳ tháng 7) so với trend +$42B/tháng đã CONFIRMED trước đó — chưa đủ dữ liệu để kết luận đây là thay đổi thật hay khác biệt định nghĩa đo lường. Duration Fed portfolio giữ nguyên hướng cũ (không thể recompute WAM mới từ bucket H.4.1 công bố), trong khi Treasury vận hành một cơ chế hoàn toàn tách biệt — buyback nợ chính mình ($38B liquidity support + $25B cash management/quý) — không phải công cụ chính sách tiền tệ dù cùng là "mua lại Treasury". |

---

## MACRO LAYER

| Chiều | Đầu Q3 2026 |
|-------|---------|
| **Regime** | Ample Reserves (Regime A) — không đổi so với H1; FOMC 17/06/2026 tái khẳng định "maintaining ample reserves in the banking system" [RAW-OFFICIAL] |
| **Policy Anchor** | IORB 3,75% là ngưỡng sàn tham chiếu; FOMC minutes 29/04/2026 ghi nhận reserves giảm "alongside orderly money market behavior" — dùng làm bằng chứng RMP đang giữ được trạng thái ample |
| **Balance Sheet** | Total assets $6.724,6B (01/07): UST $4.492,2B (Bills $489,3B / Notes-Bonds $3.611,8B / TIPS $282,6B) / MBS $1.948,4B [RAW-OFFICIAL: H.4.1 02/07/2026] |
| **Fiscal** | Nợ khả thị ~$31,52T; bills 21,7% tổng nợ (30/04, TBAC) — trên dải khuyến nghị 15-20%; Q3 refunding CHƯA công bố (dự kiến 05/08/2026) |
| **Tension** | QT kết thúc 01/12/2025 theo tuyên bố FOMC 29/10/2025 gắn trực tiếp với reserves "deemed to be ample" — không phải một chỉ báo stress cụ thể; RMP khởi động cùng lúc để duy trì trạng thái này |

Khung chuẩn hóa chính thức của Fed tách làm hai lớp cần phân biệt rõ. Lớp thứ nhất là quyết định vận hành: statement 29/10/2025 chấm dứt runoff (đã cắt >$2,2T kể từ 06/2022) và chỉ đạo Desk roll over toàn bộ Treasury principal đáo hạn tại đấu thầu, tái đầu tư MBS principal vào Treasury bills — đây chính là cơ chế "mua và roll" mà Fed dùng để giữ tổng assets gần phẳng. Lớp thứ hai là khung khái niệm: "ample reserves" được Powell định hình từ 01/2019 và vẫn nguyên vẹn trong ngôn ngữ FOMC hiện tại, nhưng Committee chưa bao giờ gắn một con số cụ thể cho nó — "ample" là một trạng thái vận hành được suy ra từ việc thị trường tiền tệ hoạt động trơn tru (SOFR-IORB không stress), không phải một ngưỡng được công bố trước.

---

## PLUMBING LAYER

Cơ chế "mua và roll" của Fed vận hành qua hai kênh song song và cần phân biệt rõ với một cơ chế cùng tên nhưng khác actor. Kênh thứ nhất là tái đầu tư SOMA: Fed roll over Treasury principal đáo hạn tại đấu thầu (giữ nguyên exposure danh nghĩa cho phần đã có) và chuyển MBS principal runoff sang mua Treasury bills mới (RMP, phần mở rộng ròng). Tại 01/07/2026, UST portfolio tăng nhẹ +$4,1B/tuần lên $4.492,2B trong khi MBS tiếp tục giảm còn $1.948,4B — đúng hướng cơ cấu UST↑/MBS↓ đã ghi nhận từ trước, tổng assets gần như đi ngang ($6.724,6B, giảm nhẹ so với $6.735,6B tuần trước đó). Kênh thứ hai, hoàn toàn tách biệt, là chương trình buyback riêng của Treasury: Treasury mua lại nợ của CHÍNH MÌNH trên thị trường thứ cấp qua hai track — liquidity support (tối đa $38B/quý, off-the-run, ~1 lần/tuần, cho holders lối thoát dự đoán được) và cash management (tối đa $25B/quý, bucket 1 tháng-2 năm, canh theo lịch quyết toán thuế giữa tháng 4/6/9/12, làm mượt biến động tiền mặt Treasury). Hai chương trình không có cơ chế phối hợp trực tiếp: một bên là ngân hàng trung ương bơm reserves mới qua tài sản ròng tăng thêm, bên kia là debt manager đổi cơ cấu kỳ hạn nợ đã phát hành bằng tiền tài trợ từ phát hành khác — tác động lên bảng cân đối Fed của track Treasury gần như bằng không.

Reserves phục hồi mạnh trong tuần kết thúc 01/07/2026: tăng $122,6B lên $3.077,0B trong khi TGA giảm $111,3B xuống còn $807,4B — chuyển động ngược chiều gần như tương xứng, khớp hướng với identity ΔReserves≈RMP−ΔTGA đã xác nhận chặt trong cluster trước qua thí nghiệm tự nhiên mùa thuế. Reserves hiện gần đỉnh dải H1 ($3.129,6B) sau khi đã chạm đáy $2.901,8B hồi tháng 4 mà không gây stress SOFR-IORB — cho thấy hệ thống hấp thụ được cả hai chiều biến động lớn trong cùng một quý mà không tiệm cận ngưỡng gây gián đoạn thanh toán. Một điểm chưa giải quyết xuất hiện ở tốc độ RMP: dữ liệu vận hành cho chu kỳ kết thúc 13/07/2026 gợi ý pace khoảng $26-29B/tháng quy đổi (10B bill purchases mới + 16,5B reinvestment mỗi chu kỳ ~4 tuần) — thấp hơn đáng kể so với trend +$42B/tháng đã CONFIRMED bằng phương pháp endpoint cho giai đoạn Dec 2025-Jun 2026. Ba khả năng chưa phân biệt được: pace thực sự chậm lại trong Q3, khác biệt định nghĩa giữa net UST change đo trên H.4.1 và gross RMP+reinvestment công bố theo lịch vận hành, hoặc đơn giản là chưa đủ điểm dữ liệu tháng 7-8 để xác nhận xu hướng — không nên vội kết luận từ một chu kỳ.

Về duration, cấu trúc kỳ hạn UST của Fed công bố trong bảng phân bố mới (01/07/2026) cho thấy tỷ trọng tập trung ở hai đầu: $1.613,0B (36%) ở kỳ hạn còn lại trên 10 năm và $1.431,9B (32%) ở kỳ hạn 1-5 năm. Tuy nhiên WAM chính xác không thể recompute đáng tin cậy từ bảng này vì bucket ">10 năm" không kèm kỳ hạn trung bình công bố — cùng giới hạn kỹ thuật đã gặp khi tính con số 7,24 năm trước đó, nên con số đó vẫn đứng làm điểm tham chiếu mới nhất chưa bị thay thế. Ở phía Treasury, WAM tổng nợ khả thị vẫn dừng ở 70 tháng (5,83 năm) tính đến tháng 3/2026 — không có điểm công bố mới hơn tháng 4-6. Bills chiếm 21,7% tổng nợ tại 30/04/2026 theo biên bản TBAC, gần khớp con số 21,44% đã ghi nhận từ MSPD tháng 5 — hai số liệu đo ở thời điểm và có thể cơ sở khác nhau nhưng cùng xác nhận bills vẫn trên dải khuyến nghị 15-20%. TBAC 05/05/2026 khuyến nghị giữ nguyên quy mô đấu thầu coupon/FRN "ít nhất vài quý tới", nhưng dự báo trung vị primary dealer ngụ ý thiếu hụt tài trợ $1,3T trong FY2027-28 ở mức phát hành hiện tại — một cờ rủi ro cấu trúc dài hạn, chưa phải áp lực của quý hiện tại.

Khung khái niệm cho toàn bộ các con số trên — điều gì được coi là "đủ" reserves — vẫn chưa có một định nghĩa số học thống nhất giữa các nguồn. Ba proxy khác nhau tồn tại song song trong nghiên cứu: mốc "$3.000B ≈ 9% GDP" (ước tính ngoài, đo theo GDP danh nghĩa), ngưỡng sàn payment-system của Duffie (mô tả cơ chế binding, không cho một con số), và ngưỡng mới xác nhận trong lượt nghiên cứu này — NY Fed Staff Report 1019 đặt reserves >12-13% tổng tài sản ngân hàng cho chế độ abundant, đo theo cơ sở hoàn toàn khác (tổng tài sản ngân hàng, không phải GDP). Ba proxy này có thể phân kỳ theo thời gian nếu tổng tài sản ngân hàng và GDP danh nghĩa tăng trưởng với tốc độ khác nhau — chưa có tính toán độc lập trong lượt nghiên cứu này để xác định vị trí thực tế của $3.077,0B trên đường cong SR1019 vì cần dữ liệu H.8 (Assets and Liabilities of Commercial Banks) chưa được ingest.

---

## TREASURY LAYER

Desk cần tách bạch ba việc đang thường bị gộp chung dưới nhãn "Fed mua Treasury": RMP (Fed bơm reserves mới), tái đầu tư SOMA (Fed giữ exposure hiện có qua roll over đáo hạn), và buyback của Treasury (Treasury tự mua lại nợ mình bằng tiền tài trợ từ phát hành khác). Ba cơ chế có tác động hoàn toàn khác nhau lên bảng cân đối hệ thống dù bề ngoài đều là "mua Treasury" — chỉ cơ chế đầu tiên tạo reserves mới. Với reserves đã phục hồi về gần đỉnh dải H1 ($3.077,0B) sau một cú giảm mùa thuế không gây stress, desk có thể tạm coi biến động ngắn hạn tuần vừa qua là bình thường trong dải đã xác nhận, nhưng nên chờ thêm 2-3 điểm H.4.1 tháng 7-8 trước khi đánh giá liệu pace RMP đã thực sự chậm lại hay chỉ là biến động đo lường giữa hai định nghĩa khác nhau của "pace".

Việc thiếu một ngưỡng số chính thức từ FOMC có nghĩa Committee sẽ tiếp tục dùng bằng chứng gián tiếp (SOFR-IORB, hành vi thị trường tiền tệ) để phán đoán "ample" thay vì một con số cố định — desk không nên chờ một tuyên bố ngưỡng cụ thể mà nên tự theo dõi cả hai proxy định lượng đang có (12-13% reserves/bank-assets từ SR1019, và $3.000B/9%GDP từ ước tính ngoài) như hai cận trên có trọng lượng khác nhau, không phải hai con số thay thế nhau được. Với Treasury debt duration, bills vẫn trên target 15-20% và Q3 refunding chưa công bố — desk nên đưa ngày 05/08/2026 vào lịch rủi ro funding cùng cấp độ với các mốc FOMC, vì đây là lần đầu tiên kể từ Q1 2026 khả năng điều chỉnh quy mô coupon (dù TBAC đã tín hiệu giữ nguyên) sẽ được xác nhận chính thức thay vì suy đoán.

- **Ngắn hạn:** theo dõi 2-3 điểm H.4.1 tháng 7-8 để xác nhận RMP pace $42B/tháng có tiếp tục hay đã chuyển sang $26-29B/tháng; nếu pace mới xác nhận, cần tính lại thời điểm reserves có thể chạm lại đáy dưới $2.901,8B.
- **Trung hạn:** đưa 05/08/2026 (Q3 refunding) vào lịch rủi ro cùng cấp FOMC; theo dõi bills share (21,4-21,7%) như tín hiệu áp lực cấu trúc chưa giải quyết dù coupon sizes được giữ nguyên.
- **Dài hạn:** không coi $3.000B hay 12-13% reserves/bank-assets là ngưỡng đã xác nhận chính thức — cả hai vẫn là ước tính nghiên cứu/ngoài, không phải cam kết công bố của FOMC; theo dõi song song cả hai cho đến khi có bằng chứng thực nghiệm cho thấy chúng hội tụ hay phân kỳ.

---

## TIMING LAYER

| | Past | Present (đầu Q3 2026) | Future |
|--|------|-------------------------------------|--------|
| **Reserves / Ample framework** | H1 2026: đáy $2.901,8B (22/04, mùa thuế) không gây stress; mốc "$3.000B" chỉ là ước tính ngoài | $3.077,0B (01/07), gần đỉnh dải H1; xác nhận thêm ngưỡng nghiên cứu SR1019 (12-13% bank-assets) tồn tại song song mốc GDP | Cần dữ liệu H.8 để định vị trên đường cong SR1019; FOMC vẫn chưa có kế hoạch công bố ngưỡng số |
| **RMP / Duration** | Trend +$42B/tháng UST CONFIRMED Dec-Jun; WAM Fed 7,24yr (24/06) | Pace tín hiệu chậm lại (~$26-29B/th, chưa xác nhận); WAM chưa recompute được từ bucket mới | 2-3 điểm H.4.1 tới sẽ xác nhận hoặc bác bỏ tín hiệu chậm lại |
| **Treasury Duration/Buyback** | WAM 70 tháng (03/2026); bills 21,44% (MSPD 05/2026) | Bills 21,7% (TBAC 30/04); buyback $38B liquidity+$25B cash mgmt/quý xác nhận là cơ chế tách biệt RMP | Q3 refunding 05/08/2026 sẽ xác nhận coupon sizes có đổi hay không |

**Velocity:** Reserves truyền dẫn trong ngày (Fedwire); RMP/tái đầu tư vận hành theo chu kỳ ~4 tuần; buyback Treasury theo lịch tuần (liquidity) và theo mùa thuế (cash management); khung "ample" thay đổi ở tần suất năm (chỉ dịch chuyển khi có quyết định FOMC mới, như 29/10/2025).

**Synchronization:** Nếu RMP pace thực sự chậm lại đúng lúc một cú sốc TGA lớn khác xảy ra (ví dụ quyết toán thuế doanh nghiệp Q3/Q4, hoặc FBO cuối quý 30/09), reserves có thể giảm nhanh hơn khả năng bù đắp của RMP — đây là kịch bản duy nhất trong dữ liệu hiện có có thể đẩy reserves xuống dưới đáy 22/04 đã ghi nhận, dù chưa xảy ra.

## FEEDBACK / BOUNDARY

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|------------------|-------------------|---------|
| Reserves floor | SOFR–IORB daily | Đáy dưới $2.901,8B kèm SOFR nới rộng đồng thời | 01/07: $3.077,0B — trong dải, gần đỉnh |
| RMP pace | H.4.1 weekly UST Δ | Pace dưới $30B/tháng kéo dài >2 chu kỳ | 1 chu kỳ tín hiệu ~$26-29B/th — chưa đủ xác nhận |
| Reserve/bank-assets ratio | H.8 weekly | Dưới 12-13% → tiệm cận ranh giới ample-scarce (SR1019) | Chưa tính được — cần ingest H.8 |
| Bills share | TBAC quarterly | Duy trì >20% qua nhiều quý liên tiếp không giảm | 21,4-21,7% — trên target, ổn định |
| Q3 refunding | home.treasury.gov | Tăng coupon sizes bất ngờ so với khuyến nghị TBAC | Chưa công bố (05/08/2026) |

**Failure conditions:** Nếu 2-3 điểm H.4.1 tới xác nhận RMP pace đã chậm lại thật (không phải khác biệt định nghĩa), và một cú sốc TGA sự kiện xảy ra cùng lúc (quyết toán thuế Q3, hay FBO 30/09), reserves có thể chạm mức thấp hơn đáy tháng 4 mà không có RMP bù kịp — đây là kịch bản kiểm định ngưỡng sàn thật chưa từng xảy ra trong dữ liệu H1. Về khung khái niệm: nếu FOMC công bố một ngưỡng số cụ thể trong tương lai (khác với cách tiếp cận định tính hiện tại), toàn bộ phân tích "ample là một dải không phải một điểm" trong node này cần viết lại.

---

## DIAGRAM

```
FED BALANCE SHEET 01/07/2026 — RESERVES REBOUND + KHUNG "AMPLE" ĐA TẦNG
════════════════════════════════════════════════════════════════════

  H.4.1 WEEKLY MOVE (24/06 → 01/07/2026)
  ┌──────────────────────────────────────────────────────────┐
  │ Total assets   $6,735.6B → $6,724.6B   (gần như phẳng)   │
  │ UST            $4,488.1B → $4,492.2B   (+4.1B, RMP nhẹ)  │
  │ MBS            $1,961.6B → $1,948.4B   (runoff tiếp diễn)│
  │ TGA            $918.7B  → $807.4B      (−111.3B)         │
  │ Reserves       $2,954.5B → $3,077.0B   (+122.6B) ◄────┐  │
  └────────────────────────────────────────────────────────┼──┘
                                                            │
              ΔReserves ≈ RMP_trend − ΔTGA_event ───────────┘
              (hướng khớp, độ lớn khớp gần đúng)

  BA NGƯỠNG "AMPLE" SONG SONG — KHÔNG PHẢI MỘT SỐ DUY NHẤT
  ┌───────────────────────┬───────────────────────┬───────────────────────┐
  │ Duffie (payment sys.)  │ Andreopoulos (ngoài)   │ NY Fed SR1019 (mới)   │
  │ Cơ chế binding, không  │ ~$3,000B ≈ 9% GDP      │ >12-13% tổng tài sản  │
  │ cho số cụ thể          │ (proxy vĩ mô)          │ ngân hàng (proxy vi mô)│
  └───────────────────────┴───────────────────────┴───────────────────────┘
                    Reserves hiện tại $3,077.0B — nằm trong dải "ample"
                    theo cả 3 khung, nhưng KHÔNG có khung nào là cam kết
                    số học chính thức của FOMC (statement 17/06/2026 vẫn
                    chỉ dùng ngôn ngữ định tính "maintaining ample reserves")
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed một phần, mở một câu hỏi mới — reserves phục hồi đúng hướng dự đoán bởi identity RMP-TGA đã xác nhận trước; khung "ample reserves" chính thức của FOMC xác nhận là hoàn toàn định tính (không có ngưỡng số công bố), với NY Fed SR1019 là nguồn định lượng có trọng lượng nghiên cứu chính thức gần nhất nhưng đo trên cơ sở khác hẳn các ước tính ngoài đã dùng trước; RMP pace cho tín hiệu chậm lại chưa đủ dữ liệu để xác nhận |
| **Net Plumbing Effect** | Reserves quay về gần đỉnh dải H1 sau đáy mùa thuế, không gây stress ở cả hai đầu biến động; duration Fed portfolio không đổi hướng (chưa recompute được số mới); Treasury buyback xác nhận là cơ chế hoàn toàn tách biệt RMP, không tác động bảng cân đối Fed |
| **Treasury Action** | Theo dõi 2-3 điểm H.4.1 tháng 7-8 để xác nhận/bác bỏ tín hiệu RMP chậm lại; đưa 05/08/2026 (Q3 refunding) vào lịch rủi ro; không coi bất kỳ ngưỡng số nào (12-13%, $3.000B) là cam kết chính thức FOMC — cả hai là ước tính nghiên cứu/ngoài |
| **Confidence** | TIER B — H.4.1 và FOMC statement/minutes là RAW-OFFICIAL trực tiếp; NY Fed SR1019 threshold và Perli speech chỉ có snippet WebSearch (newyorkfed.org 403 toàn bộ, cả WebFetch lẫn curl) — CHƯA verify toàn văn; RMP pace mới [WEB, chưa RAW-OFFICIAL] cần xác nhận thêm |
| **Critical Caveat** | Kết luận "RMP pace chậm lại" dựa trên đúng MỘT chu kỳ vận hành và một nguồn thứ cấp (WebSearch, không phải NY Fed trực tiếp) — có thể là khác biệt định nghĩa đo lường thay vì thay đổi chính sách thật; ngưỡng 12-13% reserves/bank-assets từ SR1019 chưa verify với văn bản gốc |

---

## NEXT STEPS

```bash
# Ưu tiên giảm dần
# → Verify trực tiếp NY Fed Staff Report 1019 (ngưỡng 12-13%) — cần route khác ngoài WebFetch/curl (cả hai đều 403 trên newyorkfed.org)
# → Verify toàn văn bài phát biểu Perli 26/03/2026 (cùng vấn đề 403)
# → Ingest H.8 (Assets and Liabilities of Commercial Banks) để tính tỷ lệ reserves/bank-assets thực tế, định vị trên đường cong SR1019
# → Theo dõi 2-3 điểm H.4.1 tháng 7-8 để xác nhận/bác bỏ RMP pace chậm lại
# → Q3 2026 refunding (05/08/2026) — chưa công bố, cần re-check sau ngày này
# → Verify trực tiếp home.treasury.gov/news/press-releases/sb0489 (hiện chỉ có qua search snippet)

python librarian.py ingest
python librarian.py embed --incremental
```

---
*MODE DEEP v1 (fresh independent research) | 2026-07-06 | Refs: P1 · P2 · P3 · P4 | [[Reserve_Management_Purchases_RMP]] · [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Demand_Curve_Scarce_Ample_Abundant_Regime]] · [[Treasury_Buyback_Program_Liquidity_Cash_Management]] · [[US_Treasury_Balance_Sheet_H1_2026]]*
