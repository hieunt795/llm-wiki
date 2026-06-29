# Fed Total Assets & Cấu Trúc Kỳ Hạn UST Holdings H1 2026
> MODE DEEP | 2026-06-29 | Analyst: Claude (claude-sonnet-4-6)
> Framework: 5 Lenses — Top-Down → Macro → Plumbing → Treasury → Timing
> Focus: (1) Tổng tài sản tăng/giảm → cơ chế bơm/hút thanh khoản thị trường; (2) Cấu trúc kỳ hạn UST Fed nắm giữ → ai đang gánh duration risk, hệ quả term premium và tài khóa
> Nguồn lõi: [RAW-OFFICIAL: Fed H.4.1 24/06/2026]; [RAW-BOOK: Duffie BPEA 2026]; [WEB-2026-02-17: Cochrane — "A New Fed-Treasury Accord?"]; [RAW-OFFICIAL: Perli NY Fed 26/03/2026]; [RAW-OFFICIAL: FOMC 29/10/2025]; [WEB-2026-04-11: Andreopoulos]
> Wiki nodes: [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[QE_Balance_Sheet_Mechanics]] · [[Quantitative_Tightening_Mechanism]] · [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]]

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Tổng tài sản Fed thay đổi có nghĩa gì với thanh khoản thị trường? Cấu trúc kỳ hạn UST Fed nắm giữ đặt duration risk ở đâu, và hệ quả với term premium, tài khóa, và chính sách là gì? |
| **Asset / Currency** | USD · UST (bills/notes/bonds/TIPS) · MBS · Bank Reserves |
| **Temporal Status** | CURRENT 🟢 — H1 2026; tham chiếu lịch sử QE/QT |
| **Analytical Scope** | Bảng cân đối Fed (asset side) · Thị trường UST · Phân bổ duration risk toàn hệ thống |
| **Thesis** | Tổng tài sản Fed tăng → bơm reserves vào hệ thống ngân hàng → nới lỏng điều kiện tài chính; nhưng hiệu lực truyền dẫn phụ thuộc vào cơ chế (QE vs RMP vs crisis). Đồng thời, Fed nắm giữ ~$4,488B UST với kỳ hạn trung bình dài [LLM-E: WAM ~7 năm], tập trung ở notes/bonds — điều này rút duration risk khỏi thị trường tư nhân, nén term premium, và tạo bất đối xứng lãi suất: Fed thu coupon cố định nhưng trả IORB thả nổi trên reserves. |

---

## MACRO LAYER

| Chiều | Giá trị H1 2026 |
|-------|----------------|
| **Macro Regime** | Ample Reserves — Regime A; QT2 kết thúc 01/12/2025; RMP chạy từ 10/12/2025 |
| **Policy Anchor** | IORB (thả nổi, reset theo fed funds); Fed funds target 3.50–3.75% [WEB-2026-05-08: Benigno CB Commentary April 2026] |
| **Balance Sheet Stance** | Total assets ≈ phẳng $6,735.6B [RAW-OFFICIAL: H.4.1 24/06/2026]; UST ↑ / MBS ↓ (portfolio rebalancing không phải expansion) |
| **Fiscal Stance** | Treasury vay gross ~$683B H1 2026 [LLM-E: +$249B YoY]; Fed đang hấp thụ không tăng — private market phải hấp thụ toàn bộ net issuance mới |
| **Structural Tension** | Fed nắm $4,488B UST (notes/bonds dài kỳ) trong khi trả IORB thả nổi trên $2,951B reserves → mismatch kỳ hạn gây lỗ khi rates cao; đồng thời, Fed giữ lượng lớn duration nên nén term premium tự nhiên của thị trường |

**Ba giai đoạn và ý nghĩa tổng tài sản.** Để hiểu H1 2026, cần đặt trong bối cảnh ba chế độ:

**QE (2009–2022):** Fed mua UST và MBS quy mô lớn → total assets tăng từ ~$870B (2007) lên $8,965B (đỉnh 04/2022) [LLM-E: Fed historical H.4.1] → bơm ~$3.3T reserves vào hệ thống (chưa trừ ON RRP). Mỗi đồng asset mua = một đồng reserve tạo mới → nới lỏng điều kiện tài chính qua hai kênh: (i) trực tiếp — reserves dồi dào → SOFR/EFFR sát IORB, chi phí vay qua đêm thấp; (ii) gián tiếp — rút duration risk khỏi thị trường → nén term premium → yield dài hạn giảm → chi phí vốn dài hạn giảm → kích đầu tư.

**QT2 (06/2022–12/2025):** Fed để assets run off (không tái đầu tư khi đến hạn) → total assets giảm ~$2.2T [RAW-OFFICIAL: FOMC 29/10/2025]. Nhưng **hiệu lực thực tế giới hạn**: nghiên cứu Atlanta Fed ước tính $2.2T QT chỉ tương đương tăng lãi suất 0.29–0.74% trong ba năm [RAW-BOOK: Conks — citing Bin Wei, Atlanta Fed]; phần lớn reserves giảm được thay bằng ON RRP → không gây tắc nghẽn hệ thống thanh toán cho đến cuối QT.

**RMP (12/2025–hiện tại):** Total assets ≈ phẳng; Fed mua UST ~$40B/tháng [RAW-OFFICIAL: Perli NY Fed 26/03/2026] bù vào hao hụt reserves từ TGA và autonomous factors. **Đây không phải nới lỏng** — không bơm net reserves vào hệ thống, không nén thêm term premium. Ý nghĩa duy nhất với thanh khoản là giữ reserves ≥ floor ~$3,000B để hệ thống thanh toán vận hành.

## PLUMBING LAYER

**Cơ chế bơm thanh khoản: T-account qua ba giai đoạn.**

Cơ chế cơ bản không đổi: khi Fed mua asset (bất kể QE hay RMP), nó tạo reserves mới — `UST [+X] / Reserves [+X]` trên bảng cân đối Fed; phía đối lập, dealer ngân hàng nhận reserves và giao tài sản. Nhưng *hiệu quả kinh tế* của reserves đó phụ thuộc vào việc ngân hàng làm gì với chúng:

```
      QE (stimulus intent)            RMP (operational, không stimulus)
FED:  UST [+$X] / Reserves [+$X]    UST [+$40B] / Reserves [+$40B]
      → net mới vào hệ thống          → bù hao hụt autonomous factors
      → term premium giảm             → term premium không đổi
      → yield dài hạn giảm            → yield không đổi
      → tín dụng mở rộng              → chỉ giữ floor thanh toán
```

Trong giai đoạn QE, reserves mới dồi dào → ngân hàng có thể mở rộng tín dụng → tiền gửi tăng → broad money supply (M2) mở rộng → điều kiện tài chính nới lỏng. Trong giai đoạn RMP, reserves tạo ra chỉ bù hao hụt từ TGA rebuild và currency drain — không phải reserves "thừa" có thể dùng để mở rộng tín dụng. **Đây là lý do tại sao tổng tài sản phẳng trong H1 2026 không phải tín hiệu nới lỏng dù giống QE về hình thức.**

**Cấu trúc kỳ hạn UST: phân bổ duration risk.** Đây là mặt quan trọng nhất của phân tích asset side mà thường bị bỏ qua khi chỉ nhìn vào tổng tài sản.

| Loại | Tỷ trọng ước tính [LLM-E] | Kỳ hạn còn lại trung bình [LLM-E] | Ý nghĩa |
|------|--------------------------|-----------------------------------|---------|
| T-bills (≤1 năm) | ~5–8% UST holdings | <1 năm | RMP đang tăng dần tỷ trọng này |
| Notes (2–10 năm) | ~55–60% UST holdings | ~5–7 năm | Lõi của portfolio — tích lũy từ QE era |
| Bonds (>10 năm) | ~15–20% UST holdings | ~20–25 năm | Duration dài nhất, từ Operation Twist / QE3 |
| TIPS (indexed) | ~7–10% UST holdings | mixed | Inflation-linked; coupon nhỏ hơn nominal |
| **WAM ước tính toàn portfolio** | — | **~7–8 năm [LLM-E]** | Dài hơn nhiều so với pre-GFC |

*Ghi chú: Tỷ trọng và WAM là ước tính [LLM-E] từ cấu trúc lịch sử QE và hành vi QT runoff. Cần ingest H.4.1 maturity schedule để xác nhận.*

**Ý nghĩa của WAM dài ~7–8 năm:** Fed đã và đang giữ phần lớn duration risk của nền kinh tế. Bằng cách mua notes và bonds trong QE, Fed rút bớt lượng duration risk mà thị trường tư nhân phải gánh → **nén term premium**. Krishnamurthy–Vissing-Jorgensen ước tính QE1+QE2 giảm yield 10Y khoảng 100bp thông qua kênh duration extraction [LLM-ref: KVJ 2011, 2013]. Khi Fed giữ $4,488B UST với WAM ~7–8 năm, lượng duration được rút khỏi thị trường là rất lớn — nếu tư nhân phải hấp thụ lại (ví dụ Fed bán hoặc để run off), term premium sẽ tăng lên.

**Mismatch kỳ hạn và hàm ý tài khóa.** Đây là điểm Cochrane [WEB-2026-02-17] nhấn mạnh: QE tạo ra bất đối xứng kỳ hạn trong bảng cân đối của khu vực công (Fed + Treasury tính chung):

```
Treasury phát hành:    10Y Note (coupon cố định ~2%, lãi suất phát hành 2021)
Fed mua về:            10Y Note → trả bằng reserves (IORB thả nổi)
Net khu vực công:      Đổi nợ 10Y cố định → nợ overnight thả nổi
Khi rates tăng 4%:    Treasury "tiết kiệm" (đã lock 2% 10Y)
                       Fed thua lỗ (thu 2% coupon, trả 5% IORB)
                       Net: khu vực công có thêm 3% chi phí trên phần reserves
```

Hệ quả thực tế: từ cuối 2022, Fed đã trả IORB cao hơn coupon income từ portfolio cũ → **lỗ hoạt động** và phải ghi nhận "deferred asset" (số tiền Fed nợ Treasury sẽ không remit cho đến khi trở lại lợi nhuận) [LLM-E: deferred asset đỉnh ước ~$200B, 2023–2024]. Đây là chi phí ẩn của QE — không phải mất vốn theo nghĩa kỹ thuật, nhưng là chuyển dịch thu nhập từ Treasury sang hệ thống ngân hàng (ngân hàng nhận IORB cao).

**Stakeholder impact theo chiều maturity structure.**

| Entity | Cơ chế tác động | Hướng | Magnitude |
|--------|----------------|-------|-----------|
| Fed | Thu coupon cố định ~2–3% (QE era purchases); trả IORB 4–5%; deferred asset tích lũy | Bất lợi khi rates > coupon | Lớn: ~$100–200B deferred asset [LLM-E] |
| Treasury | Không trả interest cao hơn trên 10Y notes/bonds (đã issue ở rates thấp); thiếu remittance từ Fed | Trung tính → bất lợi gián tiếp | Mất ~$80–100B/năm remittance [LLM-E] |
| GSIB / Dealers | Không phải hấp thụ duration của $4,488B UST → lower inventory burden | Có lợi: term premium thấp hơn → giá UST cao hơn | Lớn |
| Private investors | Yield 10Y thấp hơn do term premium bị nén; phải chấp nhận rủi ro cao hơn để đạt yield | Bất lợi cho người tìm kiếm income, có lợi cho người hold bonds | Moderate |
| Mortgage borrowers | MBS runoff → Fed không mua mới → MBS spread với UST có xu hướng nới → 30Y mortgage rate cao hơn | Bất lợi với chi phí vay nhà | Moderate |

**Điểm tắc nghẽn quan trọng nhất.** Treasury đang phát hành ~$683B gross trong H1 2026 [LLM-E]. Fed KHÔNG tăng portfolio (RMP chỉ giữ flat). Toàn bộ net issuance mới của Treasury phải được thị trường tư nhân hấp thụ. Với Fed không tăng duration absorption, và Treasury đang phát hành thêm, **áp lực lên term premium là hướng tăng** — tư nhân phải đòi yield cao hơn để hold thêm duration. Đây là lý do 10Y yield duy trì ở mức cao dù Fed đã dừng QT.

## TREASURY LAYER

Từ góc nhìn Treasury desk, ba hàm ý vận hành từ phân tích tổng tài sản và cấu trúc kỳ hạn:

**Thứ nhất, tổng tài sản phẳng ≠ trung tính với yield curve.** Khi Fed dừng QT và chuyển sang RMP, total assets phẳng không có nghĩa là Fed đang trung tính với thị trường. Fed đang duy trì một lượng duration rất lớn (~$4,488B UST, WAM ~7–8 năm [LLM-E]) khỏi tay tư nhân. Điều này tiếp tục nén term premium so với thế giới không có Fed portfolio. Tuy nhiên, vì Fed không mở rộng portfolio (không mua thêm net), lượng nén này không tăng thêm — trong khi net new supply từ Treasury tăng liên tục. Kết quả: term premium có xu hướng nới dần theo thời gian kể cả khi Fed không làm gì.

**Thứ hai, composition shift (UST↑ / MBS↓) có hàm ý riêng.** RMP mua UST trong khi MBS tự run off → portfolio xoay từ MBS sang UST. Với desk:
- Kênh MBS: Fed không còn bơm vào thị trường nhà ở → MBS spread với UST có xu hướng nới → 30Y mortgage rate tăng tương đối → market MBS phải hấp thụ dần phần runoff
- Kênh UST: RMP mua thêm bills/short notes → thêm vào kho UST ngắn hạn của Fed → giảm nhẹ floating supply bills ở end ngắn → có thể nén bill yields nhẹ trong các tuần RMP bơm mạnh

**Thứ ba, mismatch kỳ hạn xác định "P&L sensitivity" của Fed với lãi suất.** Khi FOMC cắt lãi suất (scenario tương lai), hai hiệu ứng đồng thời xảy ra: (i) IORB giảm → chi phí trả reserves giảm → deferred asset giảm; (ii) UST notes/bonds tăng giá (duration dài, convexity lớn) → unrealized gain trên portfolio. Ngược lại, nếu rates tăng (ví dụ trong kịch bản Kashkari của bài CB Commentary tháng 4/2026 [WEB-2026-05-08]), deferred asset tích lũy thêm và Fed chịu thêm pressure về mặt tài khóa/chính trị.

- **Monitor term premium**: phân tách ACM model 10Y yield = expected path + term premium; khi term premium nới >50bp so với mức trước QT kết thúc → thị trường đang đòi bù duration cao hơn → signal Fed cần làm rõ intent với portfolio (không phải action ngay)
- **RMP composition signal**: nếu NY Fed Desk dịch chuyển RMP từ bills sang coupons dài hơn → signal họ đang cố nén term premium; nếu tiếp tục mua bills → signal thuần operational không có ý định yield-curve management
- **Deferred asset trajectory**: remittance zero tiếp tục → áp lực chính trị từ Warsh/Cochrane camp tăng → có thể ảnh hưởng đến quyết định bán sớm MBS (thay vì để run off tự nhiên)

---

## TIMING LAYER

| | Past | Present (H1 2026) | Future |
|--|------|-------------------|--------|
| **Total Assets** | ~$870B (2007) → $8,965B (đỉnh 04/2022) [LLM-E] → $6,735.6B hiện tại [RAW-OFFICIAL: H.4.1] | Phẳng; RMP bù autonomous drain ~$40B/tháng; MBS runoff $15–20B/tháng → UST | Phẳng trừ khi: (a) tăng nếu cuộc khủng hoảng → QE mới; (b) giảm nếu Warsh kích hoạt thu nhỏ aggressive sau khi cầu reserves giảm |
| **Maturity Structure** | QE1–3: tích lũy notes/bonds dài; Operation Twist: bán ngắn mua dài → WAM kéo dài đến ~8–10 năm; QT2: notes/bonds run off → WAM rút ngắn dần | WAM ~7–8 năm [LLM-E]; RMP đang thêm bills → WAM xu hướng ngắn lại dần; nhưng stock notes/bonds vẫn chiếm ~75% | WAM rút ngắn dần theo thời gian nếu RMP tiếp tục mua bills; maturity wall: các notes/bonds QE era sẽ đáo hạn → portfolio tự nhẹ đi nếu không tái đầu tư |
| **Duration Risk Distribution** | Pre-GFC: tư nhân giữ gần toàn bộ duration; Post-QE: Fed đã rút ~$4T+ duration equivalent khỏi thị trường | Fed giữ ~$4,488B UST; tư nhân phải hấp thụ thêm ~$683B gross H1 2026; term premium tăng dần | Nếu Fed không tăng portfolio và Treasury tiếp tục phát hành → term premium dần tăng; nếu Fed phải bán MBS chủ động → cộng hưởng tăng thêm |

**Velocity:** Tác động của tổng tài sản lên thanh khoản thị trường truyền dẫn qua hai tốc độ. Tác động đến reserves (short-term funding) là ngay lập tức (trong ngày → overnight, qua Fedwire và repo). Tác động đến term premium và yield dài hạn là từ từ — thị trường điều chỉnh theo tháng/quý, phụ thuộc vào supply/demand flows.

**Window of Exposure:** Rủi ro term premium tăng đột ngột xuất hiện khi: (i) Treasury auction lớn và thị trường không đủ capacity hấp thụ (bid-to-cover thấp, tail lớn); (ii) tin tức Warsh/Fed về ý định portfolio (ví dụ xác nhận bán MBS chủ động); (iii) rates tăng thêm → deferred asset tăng → áp lực chính trị → nghi ngờ về commitment của Fed.

**Synchronization:** Ba lực có thể cùng đẩy term premium lên: (a) Treasury issuance cao; (b) Fed không hấp thụ thêm duration; (c) thị trường lo ngại Fed sẽ chủ động thu nhỏ portfolio. Không cần cả ba — hai trong số đó đủ để tạo dislocation thị trường UST.

## FEEDBACK / BOUNDARY

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|-----------------|-----------------|---------|
| Term premium | ACM model 10Y term premium (NY Fed) | Tăng >50bp trong <3 tháng = thị trường re-pricing duration risk | Tăng so với 2021; chưa có raw data H1 2026 [gap] |
| Auction demand | Bid-to-cover 10Y/30Y + tail (stop-out vs WI yield) | Bid-to-cover <2.3 liên tiếp 2 auction, tail >2bp = absorptive capacity yếu | Cần ingest Treasury auction results H1 2026 [gap] |
| Deferred asset | Fed's remittance to Treasury | Tiếp tục $0 remittance + deferred asset tăng → áp lực Warsh chủ động shrink | Vẫn $0 remittance ước tính [LLM-E: H1 2026] |
| MBS spread | Agency MBS OAS vs UST | OAS >50bp nới so với 2024 average = tư nhân đòi bù rủi ro cho runoff | Cần ingest Bloomberg MBS data [gap] |

**Failure conditions — khi phân tích này sai về maturity/duration:** (1) Nếu Warsh–Cochrane "Accord" thành hiện thực và Fed chuyển sang chỉ mua T-bills (không phải notes/bonds) cho mọi nhu cầu tương lai, WAM portfolio sẽ rút ngắn nhanh hơn dự kiến → tư nhân hấp thụ duration trở lại → term premium tăng mạnh → yield dài hạn tăng → mortgage rate và corporate bond rate tăng → thắt chặt financial conditions. (2) Nếu FOMC cắt lãi suất sớm hơn dự kiến (ví dụ do Hormuz de-escalation, đình chiến) → IORB giảm → deferred asset giảm nhanh → Fed remit lại cho Treasury → áp lực chính trị giảm → portfolio strategy không thay đổi.

---

## DIAGRAM

Điều phức tạp nhất cần visualize là mối liên hệ giữa **tổng tài sản, loại tài sản, và ai đang gánh duration risk** — cùng với feedback loop tài khóa khi rates cao. Diagram chọn góc nhìn phân bổ duration + P&L mismatch:

```
  PHÂN BỔ DURATION RISK — H1 2026

  FED PORTFOLIO ($6,735.6B total)        THAY ĐỔI PORTFOLIO
  ┌─────────────────────────────┐         QE:  Fed hút duration khỏi market
  │ UST Bills    ~$250B  (4%)   │         QT:  tư nhân hấp thụ dần
  │ UST Notes   ~$2,700B (40%) ││←────── RMP: thêm bills/short notes
  │ UST Bonds    ~$850B  (13%) ││         (WAM ngắn lại dần)
  │ TIPS         ~$430B  (6%)  ││
  │ MBS         $1,963B  (29%) ││←────── Runoff $15–20B/tháng
  │ Other        ~$542B  (8%)  │         (portfolio xoay sang UST)
  └─────────────────────────────┘
  WAM ước tính ~7–8 năm [LLM-E]

  MISMATCH P&L (khi IORB > coupon):

  ASSET SIDE (thu)                     LIABILITY SIDE (chi)
  UST coupon ~2–3%                     IORB ~4.5% trên $2,951B reserves
  (cố định, từ QE era)          VS      (thả nổi, reset với policy)
  MBS coupon + prepay                   ON RRP đã cạn ($2.3B)
                                        TGA $918.7B (0% cost)

  KHI rates cao (2023–2026):           KHI rates giảm (tương lai):
  Thu < Chi → Deferred Asset ↑          Thu ≈ Chi → Remit lại Treasury
  [~$200B estimate peak, LLM-E]        UST tăng giá → unrealized gain

  PHÂN PHỐI DURATION RISK → THỊ TRƯỜNG

  Treasury phát hành gross $683B H1    Fed KHÔNG tăng portfolio
  ─────────────────────────────────    ──────────────────────────
  Toàn bộ net issuance mới             → tư nhân phải hấp thụ
  → Private market phải hold          → term premium tăng dần
  → Bid-to-cover + tail là signal      → 10Y yield duy trì cao
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed — tổng tài sản tăng (QE) = bơm reserves + rút duration; phẳng (RMP) = giữ floor không phải stimulus; cấu trúc kỳ hạn dài (WAM ~7–8 năm) = Fed giữ duration risk lớn, nén term premium, nhưng tạo mismatch P&L khi rates cao |
| **Net Plumbing Effect** | QT đã xong; RMP giữ flat; tư nhân hấp thụ toàn bộ $683B gross issuance H1; MBS runoff tạo áp lực spread; term premium có xu hướng nới dần |
| **Treasury Action** | Monitor ACM term premium; track RMP composition (bills vs coupons → intent signal); theo dõi Treasury auction tail để phát hiện absorptive capacity yếu; track deferred asset trajectory với Warsh tenure |
| **Confidence** | TIER C — maturity structure và WAM là [LLM-E]; cần ingest H.4.1 maturity schedule, Treasury auction results, NY Fed ACM daily, Bloomberg MBS OAS để nâng lên TIER B |
| **Critical Caveat** | Nếu Warsh chủ động thu nhỏ portfolio và chuyển toàn bộ RMP sang bills, WAM rút ngắn nhanh hơn dự kiến và term premium có thể tăng mạnh đột ngột — đây là biến số thể chế quan trọng nhất chưa được xác nhận |

---

## NEXT STEPS

```bash
# Ingest data maturity structure (ưu tiên cao)
# → H.4.1 Factors Affecting Reserve Balances — bảng maturity schedule UST
# → NY Fed ACM daily term premium H1 2026
# → FRED: DFII10 (10Y TIPS yield), DGS10 (10Y nominal) → implied breakeven
# → Treasury auction results H1 2026 (bid-to-cover, stop-out, tail)
# → Bloomberg/BAML: Agency MBS OAS H1 2026

# Verify trước khi spawn node mới
python librarian.py search "term premium duration extraction QE"
python librarian.py search "Fed deferred asset remittance Treasury"
python librarian.py search "Operation Twist WAM extension"

# Node mới cần tạo:
# → 03_wiki/mechanisms/Fed_Duration_Extraction_Term_Premium.md
# → 03_wiki/evidence/Fed_Deferred_Asset_2022_2026.md
# → 03_wiki/mechanisms/Balance_Sheet_Maturity_Structure_Risk.md

python librarian.py embed --incremental
python librarian.py sync
```

---

*MODE DEEP v1 | 2026-06-29 | Template: T_MODE_DEEP.md | Refs: P1_awareness · P2_epistemic · P3_mechanistic · P4_output*
*Wiki nodes: [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] · [[QE_Balance_Sheet_Mechanics]] · [[Quantitative_Tightening_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Balance_Sheet_Transmission_Channel]]*
