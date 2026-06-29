# Fed & US Treasury — Bảng Cân Đối H1 2026
> MODE DEEP | 2026-06-29 | Analyst: Claude (claude-sonnet-4-6)
> Framework: 5 Lenses — Top-Down → Macro → Plumbing → Treasury → Timing
> Focus: Tích hợp stock + flow — tại sao quy mô neo cao và cơ chế nào tạo rủi ro dislocation
> Nguồn lõi: [RAW-BOOK: Duffie BPEA 2026 — "The Payment System Puts a Floor on the Fed's Balance Sheet"]; [RAW-OFFICIAL: Fed H.4.1 24/06/2026]; [RAW-OFFICIAL: Perli NY Fed 26/03/2026]; [RAW-OFFICIAL: Treasury Q2 2026 Refunding]; [WEB-2026-04-11: Andreopoulos]; [WEB-2026-02-17: Cochrane/Warsh]; [RAW-BOOK: Copeland–Duffie–Yang 2025]
> Wiki nodes: [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Receipt_Reactive_Payment_Throttling]] · [[Standing_Repo_Facility_SRF_Mechanics]] · [[Intraday_Liquidity_Regulation_Reserve_Demand]] · [[Poole_Curve_Reserve_Demand]]

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Tại sao bảng cân đối Fed H1 2026 không thu nhỏ được, và cơ chế nào tạo rủi ro SOFR dislocation khi ON RRP đã cạn? |
| **Asset / Currency** | USD · Bank Reserves · UST · MBS · TGA |
| **Temporal Status** | CURRENT 🟢 — snapshot as-of 24/06/2026 |
| **Analytical Scope** | Hệ thống Fed (bảng cân đối stock + flow H1 2026) + Thị trường repo USD |
| **Thesis** | Quy mô bảng cân đối Fed bị neo bởi nhu cầu reserves của hệ thống thanh toán (~9% GDP ≈ $3,000B) — không thể cắt bằng cách giảm cung. Với ON RRP đã cạn ($2.3B tại 24/06/2026), bất đối xứng nhịp giữa RMP (bơm theo trend ~$40B/tháng) và TGA rebuild (hút theo sự kiện $100–200B/tuần) là nguồn gốc cấu trúc của rủi ro SOFR–IORB dislocation trong H1 2026. |

---

## MACRO LAYER

| Chiều | Giá trị H1 2026 |
|-------|----------------|
| **Macro Regime** | Ample Reserves — Regime A (Armenter): Fed phòng thủ cạnh "Low Volatility + Limited Intervention" |
| **Policy Anchor** | IORB = sàn thực tế; SRF = IORB+10bp (trần lý thuyết, có rò rỉ do stigma + eSLR) |
| **Fiscal Stance** | Gross borrowing H1 ~$683B [LLM-E: Treasury Q2 2026 Refunding, +$249B YoY]; TGA $918.7B [RAW-OFFICIAL: H.4.1 24/06/2026]; trần nợ $41.1T (One Big Beautiful Bill Act) |
| **Institutional Constraint** | RMP là kỹ thuật vận hành, không phải stimulus; Fed không thể ép GSIB dùng daylight overdraft; SRF có nhưng không phải van phản ứng tức thì |
| **Structural Tension** | Cầu reserves tối thiểu ~$3,000B (~9% GDP) [WEB-2026-04-11: Andreopoulos] cao gấp ~300 lần mức 2007 (~$10B) [RAW-BOOK: Duffie BPEA 2026 §I]; muốn thu nhỏ bảng cân đối phải hạ cầu trước, không phải hạ cung |

**Tại sao cầu reserves cao cấu trúc.** Ba lực hậu GFC neo cầu reserves ở mức cao và không có dấu hiệu đảo chiều. **Thứ nhất**, GSIB chuyển từ dùng daylight overdraft sang giữ reserves: tổng peak overdraft toàn hệ thống từ ~$120B/ngày (top-10 ngân hàng, 2007) xuống <$5B/ngày (2025) [RAW-BOOK: Duffie BPEA 2026 §I.D] — vì giám sát viên đọc overdraft cao là chỉ báo vi phạm Regulation YY (yêu cầu tự chủ thanh khoản trong ngày). **Thứ hai**, IORB trả ~lãi thị trường cho mọi mức reserves → không còn chi phí cơ hội của việc giữ reserves dư thừa, loại bỏ động lực cho vay liên ngân hàng. Ví dụ: JPMorgan rút ~$350B khỏi tài khoản Fed từ 2023 (từ $409B xuống $63B) để mua UST — nhưng động thái này không giải phóng hệ thống khỏi nhu cầu giữ đệm dày để thanh toán. **Thứ ba**, ma sát liên ngân hàng tăng: FDIC insurance fee tới 42bp + special assessment 13bp (hậu SVB 2023), capital/leverage requirements cao hơn → thị trường fed funds teo còn <$3B liên ngân hàng/ngày (tổng ~$100B, phần lớn là FHLB cho ngân hàng ngoại) [RAW-BOOK: Duffie BPEA 2026]. Trên cùng, giám sát viên ưu tiên reserves hơn UST trong yêu cầu thanh khoản (CLAR/RLAP giả định UST thanh lý khối lượng lớn chịu chiết khấu đáng kể, không tính là cash-equivalent) — đây là lý do ngân hàng không thể thay thế reserves bằng UST trong danh mục thanh khoản.

**Bối cảnh tài khóa.** QT2 kết thúc 01/12/2025 sau khi cắt tổng cộng >$2.2T kể từ 06/2022 [RAW-OFFICIAL: FOMC 29/10/2025]; FOMC dừng không phải chủ động mà do SOFR–IORB +32bp ngày 31/10/2025 — tín hiệu reserves đang tiếp cận sàn. RMP khởi động 10/12/2025 (~$40B/tháng đến 5/2026) [RAW-OFFICIAL: Perli NY Fed 26/03/2026] là phản ứng kỹ thuật. Đồng thời, One Big Beautiful Bill Act nâng trần nợ lên $41.1T → Treasury thoát extraordinary measures → vay ồ ạt +$249B YoY [LLM-E]. TGA đạt đỉnh ~$1,025B trong T4/2026 (mùa thuế) rồi drawdown về $918.7B tại 24/06/2026 [RAW-OFFICIAL: H.4.1].

## PLUMBING LAYER

**Identity kế toán nền tảng.** Bảng cân đối Fed: `ΔAssets = ΔReserves + ΔTGA + ΔON_RRP + ΔCurrency + ΔOther`. Với QT đã xong (ΔAssets ≈ RMP purchases, không phải QE) và ON RRP cạn (ΔON_RRP ≈ 0), identity co lại thành `ΔReserves ≈ RMP_bơm − ΔTGA − ΔCurrency`. Hệ quả trực tiếp: **mọi swing TGA bây giờ truyền 1:1 vào reserves** — không có tầng trung gian. Đây là thay đổi cấu trúc so với H1 2023, khi ON RRP >$2,000B hấp thụ toàn bộ TGA swing và reserves gần như không động dù Treasury vay lớn [RAW-OFFICIAL: Fed H.4.1 series].

Hai dòng đối nghịch trên liability side của Fed và T-account tương ứng:

```
RMP (bơm ~$40B/tháng, trend):
  FEDERAL RESERVE                     PRIMARY DEALER
  UST      [+$40B] / Reserves [+$40B]  UST [-$40B] / Reserves [+$40B]

TGA rebuild (hút theo auction, event):
  FEDERAL RESERVE                     COMMERCIAL BANK / DEALER
  (không đổi)  / Reserves [−$X]       UST [+$X]   / (không đổi)
               / TGA      [+$X]
```

Hai dòng này đối nghịch về hướng nhưng **bất đối xứng về nhịp và biên độ**: RMP bơm đều ~$40B/tháng (lịch cố định, quy mô nhỏ); TGA hút $100–200B/tuần theo lịch auction (không đều, biên độ lớn, tập trung theo mùa). Khe giữa hai nhịp — đặc biệt khi ON RRP không còn làm đệm — là nơi reserves dao động mạnh.

| Entity | ΔAssets | ΔLiabilities | Vị thế H1 2026 |
|--------|---------|--------------|----------------|
| Fed | UST +$200–240B (RMP); MBS −$90–120B (runoff) [LLM-E] | Reserves ≈ phẳng (bơm − hút); TGA swing | Total assets ≈ $6,735.6B phẳng [RAW-OFFICIAL: H.4.1] |
| Treasury | UST issued +$683B gross [LLM-E] | TGA +$683B gross − chi tiêu ngân sách | TGA $918.7B tại 24/06 |
| GSIB / Dealers | UST +/− (auction + RMP); Reserves tại Fed | Unchanged wholesale | Giữ reserves dày; daylight OD <$5B/ngày hệ thống |
| FBO | Reserves − cuối quý (window-dressing) | Repo liabilities giảm tạm | Rút ≥$200B/quý (15 quý), ≥$400B (2 quý) [RAW-BOOK: Duffie, citing Crandall] |
| MMF | ON RRP → 0 (đã rút hết 2025); chuyển sang T-bills/repo trực tiếp | — | Không còn là buffer hấp thụ TGA swing |

**Chuỗi truyền dẫn stress.** Khi reserves tiếp cận hoặc chạm floor, cơ chế lan truyền đi qua tầng vi mô của hệ thống thanh toán — không chỉ qua TGA identity. Khi ngân hàng có reserves thấp, họ làm chậm thanh toán ra để chờ thanh toán vào (receipt-reactive throttling) [RAW-BOOK: Copeland–Duffie–Yang 2025]. Vì nhiều ngân hàng cùng chờ đồng thời, hệ thống rơi vào trạng thái kỳ vọng tự thỏa mãn: payment delay tăng → shadow price reserves nhảy vọt → repo rate bật vượt IORB. **Định lượng: +1 độ lệch chuẩn payment delay → +7bp SOFR–IORB** (hồi quy OLS) [RAW-BOOK: Copeland–Duffie–Yang 2025]. Quan hệ này phi tuyến và có đuôi dày — không trượt mượt. Tiền lệ: 17/09/2019, khi reserves ~$1.4T, SOFR–IORB nhảy từ +5bp (11/09) lên **+315bp** (17/09), interdealer repo ~+1,000bp tại đỉnh [RAW-BOOK: Duffie BPEA 2026, Figure 9].

**Tại sao SRF không giữ được trần.** SRF (rebrand SRP, full-allotment từ 10/12/2025, IORB+10bp) được thiết kế làm trần cho lãi repo. Hai nguồn rò rỉ làm trần không cứng. Một là stigma: lãnh đạo GSIB tại hội nghị ngành 11/2025 (Chatham House rules) xác nhận không dùng SRF trừ khi bắt buộc — chạm facility của Fed bị giám sát viên và thị trường đọc là thiếu tự chủ thanh khoản. Hai là netting friction: Fed không central-clear các nghiệp vụ repo của mình → dealer không thể net giao dịch SRF vay từ Fed với reverse repo cấp cho khách hàng → mỗi SRF transaction phình bảng cân đối dealer, đội yêu cầu eSLR. **Định lượng: 31/10/2025 SOFR +32bp trên IORB nhưng chỉ $50B rút SRF; 31/12/2025 = $75B** [RAW-BOOK: Duffie BPEA 2026 §V] — trần không giữ ngay cả khi chênh lệch rõ ràng.

**Điểm tắc nghẽn thanh khoản theo lịch.** Ba loại sự kiện có thể cộng hưởng: (i) auction settle lớn (thứ Tư/Năm hàng tuần, đặc biệt coupon refunding mid-month); (ii) quarter-end FBO window-dressing (≥$200B/quý trong 15 quý gần đây [RAW-BOOK: Duffie, citing Crandall]); (iii) tax date T4 (~April 15), nơi TGA đạt đỉnh. Khi (i) trùng với (ii) hoặc (iii) trong khoảng cách giữa hai kỳ RMP, Treasury hút mạnh trong khi Fed chưa bơm bù — reserves có thể chạm hoặc thủng floor trước khi SRF kịp hấp thụ, và SRF hấp thụ không đủ do hai nguồn rò rỉ trên.

## TREASURY LAYER

RMP là backstop cấu trúc — nhưng không phải van phản ứng theo ngày. RMP bơm theo lịch cố định (~$40B/tháng) và không điều chỉnh để bù cú sốc TGA ngày-cụ-thể. Trong khoảng cách giữa hai kỳ RMP, nếu Treasury có auction settle lớn ($100–200B trong một tuần), reserves sẽ dao động mạnh mà không có cơ chế bù ngay. SRF có nhưng rò rỉ. Desk không thể giả định trần IORB+10bp sẽ giữ trong mọi tình huống — cần map lịch auction Treasury hàng tuần vào dự báo funding cost, không phải theo tháng.

**Gauge theo dõi chính là SOFR–IORB daily**, không phải EFFR. EFFR phản ánh thị trường fed funds đã teo (<$3B liên ngân hàng/ngày) — không đại diện cho stress repo. SOFR là median gia quyền ~$3T giao dịch repo Treasury overnight [RAW-BOOK: Duffie BPEA 2026] — nơi chính sách tiền tệ truyền dẫn thực sự. Khi SOFR–IORB bắt đầu nới, leading indicator cần kiểm tra ngay là payment delay data (Fedwire statistics, NY Fed) và lịch auction Treasury tuần kế tiếp có trùng với quarter-end không.

Về tác động funding cost và ALM: khi SOFR–IORB spike, chi phí repo overnight của các vị thế UST financed qua repo tăng đột ngột. Nếu spike đủ lớn, áp lực mark-to-market có thể kích hoạt margin call / forced liquidation trên position leveraged — tạo phản hồi ngược vào thị trường UST cash (tiền lệ: tháng 3/2020, tháng 9/2019). Desk cần phân biệt spike do khe nhịp ngắn hạn (tự giải quyết sau kỳ RMP tiếp theo) với spike do cầu reserves cấu trúc tăng (ví dụ nếu SEC central clearing repo tăng nhu cầu margin/HQLA [LLM — mốc compliance chưa có raw source]) — hai loại cần phản ứng khác nhau.

Tranh luận Warsh/Cochrane [WEB-2026-02-17] đặt ba câu hỏi thể chế ảnh hưởng đến risk premium mà desk phải định giá: ai giữ duration risk (nếu Treasury giữ nhiều hơn → supply UST dài hạn tăng → yield higher → ALM cost tăng); Fed có thoát MBS (tư nhân hấp thụ thêm MBS → spread wide → funding cost mortgage tăng); crisis exception cần Quốc hội tuyên bố (chậm hơn nhưng credibility cao hơn). Những câu hỏi này chưa có kết quả nhưng định hình lại môi trường rủi ro mà desk đang vận hành trong.

- **SOFR–IORB daily**: gauge chính; nới >15bp liên tiếp 2 phiên = kiểm tra ngay lịch auction + payment delay data
- **Quarter-end 30/06/2026**: FBO window-dressing sắp tới; tính toán reserves impact trước, không chờ sau
- **RMP lag risk**: theo dõi quy mô RMP sau 5/2026 — hiện chưa có thông báo [LLM: cần raw source NY Fed Desk]; nếu quy mô giảm trong khi Treasury tiếp tục vay nhanh, khe nhịp nới rộng thêm

---

## TIMING LAYER

| | Past | Present (H1 2026) | Future |
|--|------|-------------------|--------|
| **Macro Regime** | QE 2009–2022 → QT2 06/2022–12/2025: cắt >$2.2T; reserves không giảm nhiều vì tới $2.5T được thay bằng ON RRP | Ample Reserves Regime A; QT xong; RMP chạy; reserves $2,951B sát floor; ON RRP $2.3B ≈ 0 | Duy trì Regime A nếu RMP + TOMO đủ giữ reserves trên floor; chuyển Regime B nếu không |
| **Plumbing** | 9/2019: reserves ~$1.4T, SOFR–IORB +315bp — điểm gãy phi tuyến [RAW-BOOK: Duffie Fig.9]. 2023: TGA rebuild $500B+ nhưng ON RRP >$2T làm đệm → reserves không động | Reserves $2,951B = floor; ON RRP $2.3B = 0; mọi swing TGA → reserves trực tiếp; SRF rò rỉ; Q2-end FBO sắp tới | Stress tăng nếu Treasury tiếp tục vay nhanh hơn nhịp RMP; SEC central clearing có thể đẩy floor lên [LLM] |
| **Treasury** | Post-2019: FOMC tăng đệm reserves, tránh xa điểm gãy; ON RRP dùng như buffer 2021–2023 | Không còn buffer; cần map lịch auction hàng tuần; SOFR–IORB là gauge duy nhất đáng tin | Nếu TOMO được triển khai → khe nhịp giảm; nếu Reg YY nới → cầu reserves cấu trúc giảm → biên an toàn tăng |

**Velocity:** Truyền dẫn từ TGA rebuild → SOFR spike là trong ngày đến overnight — Fedwire settle cùng ngày, payment delay tích lũy trong vài giờ. Không phải ngày hay tuần.

**Window of Exposure hiện tại:** Q2 end 30/06/2026 là điểm gần nhất — FBO window-dressing cộng với khe nhịp RMP. Tháng 9 và tháng 12 là hai điểm tiếp theo trong lịch theo mùa.

**Synchronization risk:** Ba cơ chế có thể cùng kích hoạt — TGA rebuild lớn + FBO window-dressing cuối quý + khe nhịp RMP. Không có ON RRP làm đệm, xác suất cộng hưởng cao hơn H1 2023 rõ rệt.

## FEEDBACK / BOUNDARY

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|-----------------|-----------------|---------|
| Reserves stress | SOFR–IORB daily | >15bp: theo dõi; >32bp: ngưỡng FOMC phản ứng (tiền lệ 31/10/2025) | Chưa có timeseries H1 2026 [gap] |
| Payment system | Fedwire delay statistics (NY Fed) | +1SD delay → +7bp SOFR–IORB [RAW-BOOK: CDY2025] | Không có real-time |
| TGA flow | TreasuryDirect daily balance | Rebuild >$100B/tuần = rủi ro cao; Q2-end drawdown giảm tải | $918.7B tại 24/06 |
| SRF utilization | NY Fed SRF daily operations | >$100B: stigma tan dần hoặc stress thực sự | $75B tại 31/12/2025; H1 2026 chưa có |

**Failure conditions — khi phân tích này sai:** (1) Nếu Fed triển khai TOMO sterilization theo sự kiện (offset cú sốc TGA ngay trong ngày) — bất đối xứng nhịp bị triệt tiêu, rủi ro khe nhịp giảm đáng kể. Đây là công cụ ưu tiên số một của Duffie [RAW-BOOK: Duffie BPEA 2026 §VIII] và không cần luật mới. (2) Nếu giám sát viên nới Regulation YY (daylight overdraft cao hơn, hoặc non-HLA tính vào thanh khoản) — cầu reserves cấu trúc giảm → floor thấp hơn → biên an toàn tăng. (3) **Ratchet effect:** nếu GSIB tiếp tục tích lũy reserves thêm (do quy chế hoặc hành vi) — cầu reserves tự tăng thêm theo thời gian [LLM-ref: Acharya–Rajan 2022], đẩy floor lên cao hơn nữa và làm phân tích hiện tại underestimate quy mô sàn.

---

## DIAGRAM

Điều phức tạp nhất không thể diễn tả bằng văn xuôi là bất đối xứng nhịp giữa hai lực đối nghịch và cơ chế khuếch đại phi tuyến khi reserves chạm floor. Diagram chọn góc nhìn flow qua thời gian + feedback loop khi stress xảy ra:

```
  FED (RMP)                              TREASURY (TGA)
  bơm theo TREND                         hút theo SỰ KIỆN
  ~$40B / tháng                          $100–200B / tuần (auction settle)

  ──Wk1────────Wk2────────Wk3────────Wk4────────Wk5──►  thời gian
        │            │            │            │
  RMP   ↑ +40B       ↑ +40B       ↑ +40B       ↑ +40B
        │            │            │            │
  TGA   ↓-120B↓-80B  ↓-150B↓-60B  ↓-90B↓-200B  ↓-70B
                                  [tax date]   [Q-end FBO +$200B]

  ══════════════════════════════════════════════════════
  Reserves $2,951B  ←  sát floor $3,000B
  [ON RRP $2.3B ≈ 0 — không còn đệm trung gian]
  ══════════════════════════════════════════════════════
           ↑                         ↑
     [KHE NHỊP]               [CỘT HỢP:
  RMP chưa bơm kỳ tiếp        tax date + Q-end FBO]
  TGA vừa hút $120B            → amplification
  Reserves < floor?

  Nếu reserves < floor → chuỗi phi tuyến:

  Dealer B giữ thanh toán ra
      → chờ tiền từ Dealer A (cũng đang chờ)
            → self-fulfilling delay toàn hệ thống
                  → shadow price reserves ↑
                        → SOFR bật vượt IORB
                              [+315bp tiền lệ 17/09/2019]
                                    → repo cost tăng đột ngột
                                          → margin call / forced liq.
                                                → UST cash market stress
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed — quy mô bảng cân đối Fed bị neo bởi cầu reserves cấu trúc; bất đối xứng nhịp RMP vs TGA là cơ chế rủi ro chính khi ON RRP = 0 |
| **Net Plumbing Effect** | Reserves $2,951B = đúng floor, biên ≈ 0; ON RRP cạn; mọi swing TGA truyền thẳng 1:1 vào reserves; SRF trần rò rỉ (stigma + eSLR) |
| **Treasury Action** | Map lịch auction Treasury hàng tuần vào dự báo funding; dùng SOFR–IORB daily làm gauge; đánh giá FBO impact trước Q2 end 30/06/2026; không giả định SRF giữ được trần |
| **Confidence** | TIER B — số liệu từ nguồn có chất lượng (H.4.1, Duffie BPEA 2026, Perli); flow H1 2026 là [LLM-E]; thiếu timeseries daily SOFR–IORB và TGA để xác nhận thực nghiệm |
| **Critical Caveat** | Nếu Fed triển khai TOMO sterilization theo sự kiện (offset TGA swing ngay trong ngày), bất đối xứng nhịp bị triệt tiêu và toàn bộ rủi ro khe nhịp giảm đáng kể — đây là biến số chính sách chưa được xác nhận |

---

## NEXT STEPS

```bash
# Verify trước khi spawn node mới
python librarian.py search "TOMO sterilization reserve supply shocks"
python librarian.py search "FBO quarter end window dressing reserves"

# Ingest data còn thiếu
# → FRED: IORB series + NY Fed SOFR daily → dựng SOFR–IORB timeseries H1 2026
# → TreasuryDirect: daily TGA balance H1 2026
# → NY Fed Desk: RMP purchase operations week-by-week
# → SEC: Treasury central clearing rule compliance timeline

# Node mới cần tạo:
# → 03_wiki/mechanisms/TOMO_Reserve_Supply_Sterilization.md
# → 03_wiki/evidence/FBO_Quarter_End_Window_Dressing.md
# → 03_wiki/evidence/SOFR_IORB_Timeseries_H1_2026.md  (sau khi có data)

python librarian.py embed --incremental
python librarian.py sync
```

---

*MODE DEEP v1 | 2026-06-29 | Template: T_MODE_DEEP.md | Refs: P1_awareness · P2_epistemic · P3_mechanistic · P4_output*
*Wiki nodes: [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Receipt_Reactive_Payment_Throttling]] · [[Standing_Repo_Facility_SRF_Mechanics]] · [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] · [[Intraday_Liquidity_Regulation_Reserve_Demand]] · [[Poole_Curve_Reserve_Demand]]*
