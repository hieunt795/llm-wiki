# Fed & US Treasury: Bảng Cân Đối H1 2026 — MODE DEEP v2
> **Date:** 2026-06-27 | **Analyst:** Claude (claude-opus-4-8)
> **Framework:** 5 Lenses — Top-Down → Macro → Plumbing → Treasury → Timing
> **Focus:** Vì sao bảng cân đối Fed bị chốt sàn, cơ chế vi mô đẩy reserves đến giới hạn, và con đường duy nhất để thu nhỏ là hạ cầu reserves.
> **Nguồn lõi:** Duffie BPEA 2026 ("The Payment System Puts a Floor on the Fed's Balance Sheet"); Fed H.4.1 (24/06/2026); NY Fed Perli (26/03/2026); Treasury Q2 2026 Refunding; Cochrane/Warsh (17/02/2026); Andreopoulos (11/04/2026); Constâncio (28/11/2025).
> **Wiki nodes:** [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Receipt_Reactive_Payment_Throttling]] · [[Intraday_Liquidity_Regulation_Reserve_Demand]] · [[Poole_Curve_Reserve_Demand]] · [[Supply_Driven_Vs_Demand_Driven_Reserves]] · [[Liquidity_Savings_Mechanism_LSM]] · [[Tiered_Reserve_Remuneration]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[Standing_Repo_Facility_SRF_Mechanics]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Treasury_Central_Clearing_Repo_Netting]] · [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]]

---

## LAYER 1 — TOP-DOWN ENTRY: Câu Hỏi Đúng

Câu hỏi trung tâm của H1 2026 **không phải** "Fed nới hay thắt", cũng không chỉ là "reserves đang ở đâu so với floor". Câu hỏi đúng là: **floor đó từ đâu ra, và vì sao nó cứng?**

Câu trả lời (Duffie BPEA 2026): quy mô tối thiểu bảng cân đối Fed bị **chốt sàn bởi nhu cầu dự trữ của hệ thống thanh toán** cộng với liquidity regulation — **không** phải con số Fed tùy ý chọn. Reserves ~$3,000B hiện nay gấp ~300 lần mức đầu 2007 (~$10B), và Fed đang phải *tăng* reserves theo nhịp cầu của hệ thống thanh toán, chứ không thu nhỏ được.

> **Top-down frame:** Bảng cân đối Fed lớn không phải vì Fed *muốn* lớn, mà vì hệ thống thanh toán + quy chế chốt sàn cầu reserves. QT kết thúc (01/12/2025) và [[Reserve_Management_Purchases_RMP]] khởi động (10/12/2025) chỉ là Fed *phòng thủ cái sàn đó*. Con đường duy nhất để thực sự nhỏ lại là **hạ cầu reserves**, không phải cắt cung.

---

## LAYER 2 — MACRO: Regime & Đường Cầu Reserves

- **Regime = "Ample Reserves" (Regime A)** theo [[Central_Bank_Balance_Sheet_Trilemma]] (Armenter): Fed phòng thủ cạnh "Low Volatility + Limited Intervention".
- **Ngưỡng "Lowest Ample" ≈ 9% GDP ≈ $3,000B** (Andreopoulos, 11/04/2026) có vi nền tảng từ [[Poole_Curve_Reserve_Demand]]: đường cầu reserves chuyển từ **phẳng** (abundant, lãi do IORB dẫn) → **dốc** (ample) → **dốc đứng** (scarce).
- **Vấn đề cốt lõi — đường cong KHÔNG trượt mượt:** 17/09/2019, khi reserves chạm ~$1.4T, SOFR–IORB nhảy thẳng 5bp (11/09) → **315bp** (17/09), interdealer repo ~+1000bp. Bài học FOMC (Quarles): "giữ đệm dày, đừng bao giờ đến gần kink nữa" → thiên **supply-driven** → bảng cân đối lớn hơn về cấu trúc.
- **Lựa chọn chiến lược H1 2026:** Fed ở thế **hybrid** giữa [[Supply_Driven_Vs_Demand_Driven_Reserves]] — vừa khuyến khích dùng SRP, vừa dùng RMP kìm biến động. BoE (Short Term Repo) chứng minh demand-driven khả thi (sterling reserves £1,000B cuối 2021 → £646B tháng 1/2026), nhưng điều kiện cần là **stigma phải tan**.
- **Bối cảnh tài khóa:** Trần nợ nâng lên **$41.1T** (One Big Beautiful Bill Act) → Treasury thoát "extraordinary measures", vay **~$683B trong 2 quý (1–6/2026, +$249B YoY)** — động cơ vĩ mô hút reserves.

---

## LAYER 3 — PLUMBING: 4 Thành Phần

### 3.1 Entity + Flow Tracing
Hai dòng đối nghịch trên *liability side* của Fed, cộng tầng vi cơ chế thanh toán:
- **Fed bơm** qua RMP: mua ròng UST → `Assets UST +X / Liabilities Reserves +X`.
- **Treasury hút** qua TGA rebuild: `Reserves −X / TGA +X` (identity `dTGA = −dReserves`, sau khi ON RRP cạn).
- **Tầng vi mô:** reserves luân chuyển giữa ngân hàng qua Fedwire (RTGS); thời điểm thanh toán ra **nhạy với thanh toán vào** (receipt-reactive).

### 3.2 Stakeholder Impact Matrix
| Bên | Vị thế H1 2026 | Hệ quả |
|---|---|---|
| **Fed (Desk)** | Asset phẳng, xoay UST↑/MBS↓, RMP ~$40B/tháng đến 5/2026 | Phòng thủ sàn cầu reserves |
| **Treasury** | Vay $683B nạp TGA | Lực hút reserves theo *sự kiện* |
| **GSIB / dealer** | Ngại overdraft (<$5B/ngày toàn hệ thống), ngại SRP (stigma) | Cầu reserves kém co giãn → đẩy sàn lên |
| **FBO (ngân hàng ngoại)** | Window-dressing cuối quý | Rút ≥$200B (15 quý), ≥$400B (2 quý) → cú sốc cung reserves |
| **Money market** | ON RRP cạn → reserves là absorber biên | SOFR–IORB nới từng đợt |

### 3.3 Liquidity Narrative — Vì sao sàn cứng
Cầu reserves phình ~300× từ 2007 do ba động lực ([[Intraday_Liquidity_Regulation_Reserve_Demand]]):
1. **Ngại daylight overdraft:** top-10 ngân hàng overdraft ~$120B/ngày (2007) → toàn hệ thống <$5B (2025). GSIB sợ supervisor đọc là vi phạm tự chủ thanh khoản (Reg YY).
2. **Mất động lực cho vay reserves dư:** IORB trả ~lãi thị trường cho mọi mức reserves. VD JPMorgan rút ~$350B khỏi Fed từ 2023 ($409B→$63B).
3. **Ma sát liên ngân hàng:** FDIC fee tới 42bp + 13bp (hậu SVB), capital/leverage cao.

Supervisor còn **ưu tiên reserves hơn Treasuries** cho yêu cầu thanh khoản (CLAR/RLAP coi UST không cash-equivalent khi thanh lý lớn) → "red line" Dimon: balance tại Fed không được chạm 0 dù stress trong ngày.

### 3.4 Asset Price Mechanical Linkage
- Gauge stress chính = **SOFR–IORB spread** ([[SOFR_IORB_Spread_Stress_Gauge]]), KHÔNG phải EFFR (fed funds market teo: <$3B liên ngân hàng/ngày vs repo Treasury ~$8.8T, ~$6T overnight). Logan–Schulhofer-Wohl (2025) đề xuất TGCR thay EFFR làm target.
- **Cơ chế spread nới đột ngột** ([[Receipt_Reactive_Payment_Throttling]]): reserves thấp → dealer throttle thanh toán ra chờ tiền vào → self-fulfilling delay → shadow price reserves nhảy bậc. Định lượng: **+1SD payment delay → +7bp SOFR–IORB** (OLS).
- **Vì sao SRF không giữ được trần** ([[Standing_Repo_Facility_SRF_Mechanics]] · [[Treasury_Central_Clearing_Repo_Netting]]): stigma + Fed không central-clear repo → dealer không net SRP repo với reverse repo khách → đội eSLR. Bằng chứng: **31/10/2025 SOFR +32bp trên IORB nhưng chỉ $50B rút SRP**; 31/12/2025 = $75B.

### 📸 Snapshot H.4.1 — as-of 24/06/2026
| Khoản mục | Giá trị | Ý nghĩa |
|---|---|---|
| **Total Assets** | $6,735.6B | Phẳng (QT kết thúc 01/12/2025) |
| UST holdings | $4,487.9B | Tăng (RMP) |
| MBS holdings | $1,963.4B | Giảm (runoff) |
| **Reserve Balances** | **$2,951.4B** | Sát floor ~$3,000B → biên an toàn ≈ 0 |
| **TGA** | **$918.7B** | Giảm từ đỉnh ~$1,025B (cuối 4/2026) |
| **ON RRP (others)** | **$2.3B** | Đệm đã cạn |
| RRP foreign official | $331.4B | Structural |

---

## LAYER 4 — TREASURY: So What Cho Desk

- **RMP là backstop *cấu trúc* nhưng không che cú sốc TGA ngày-cụ-thể.** Map lịch phát hành Treasury + tax date vào dự báo funding cost.
- **Theo dõi SOFR–IORB là gauge chính**, nhưng dùng **payment-delay & quarter-end window dressing như leading indicator**: FBO rút ≥$200B/≥$400B cuối quý + tax date (April) là nơi sàn dễ thủng *giữa hai kỳ RMP*.
- **Rủi ro lịch:** nếu nhịp vay Treasury vượt nhịp RMP (trend, có độ trễ), reserves có thể thủng floor trước khi Fed kịp bù → SOFR spike.
- **Tín hiệu Perli:** "một chút biến động repo là có ích để thị trường phát tín hiệu" — nhưng nếu funding cost quá biến động → nguy cơ forced liquidation các vị thế UST financed bằng repo → bất ổn thị trường UST cash.

---

## LAYER 5 — TIMING: Past / Present / Future

- **PAST:** Reserves ~$10B (2007) → đỉnh $4.2T (9/2021, hậu QE). Crunch 9/2019 ở $1.4T (SOFR–IORB +315bp). QT2 cắt >$2.2T (đến 01/12/2025); trong QT2 reserves không giảm nhiều vì tới $2.5T được thay bằng ON RRP.
- **PRESENT (H1 2026):** Asset phẳng $6.74T; reserves $2.95T sát floor; ON RRP cạn; Treasury vay $683B; Fed hybrid (RMP + khuyến khích SRP); SRP rebrand full-allotment (10/12/2025, IORB+10bp); tranh luận Warsh/Cochrane về "Accord mới".
- **FUTURE — Menu hạ sàn cầu reserves (Duffie §VIII, theo thứ tự ưu tiên):**
  1. **TOMO sterilize** cú sốc TGA/FIMA/quarter-end → đường reserves thấp & trơn hơn (không cần luật mới — ưu tiên #1).
  2. **Nới Reg YY** — cho non-HLA collateral tính vào thanh khoản; bớt ưu tiên reserves hơn Treasuries; bình thường hóa daylight overdraft.
  3. **LSM cho Fedwire** ([[Liquidity_Savings_Mechanism_LSM]]) — net thanh toán lớn, tiết kiệm 15–30% reserves (CHAPS/BOJ-NET/Lynx); dự án nhiều năm.
  4. **Tiered remuneration** ([[Tiered_Reserve_Remuneration]]) — kích interbank lending (NZ/Norway); dự án nhiều năm.
  - **Biến chưa rõ:** chuyển central clearing repo Treasury có thể *tăng* nhu cầu HQLA/margin → đẩy sàn lên (mốc mandate cụ thể chưa có raw source).

---

## FEEDBACK / BOUNDARY

- **Lằn ranh đứt gãy:** reserves < ~9% GDP → SOFR dislocation kiểu 2019. Hiện biên an toàn ≈ 0; ON RRP không còn đệm.
- **Ratchet effect:** reserves dồi dào → ngân hàng "nghiện" reserves (Acharya-Rajan 2022) → cầu tự tăng → chi phí tuyệt đối của bảng cân đối lớn dần.
- **Nghịch lý demand-driven:** để stigma tan cần dùng SRP nhiều → cần chấp nhận biến động repo → nhưng biến động có thể bùng thành crunch khiến Fed buộc bơm reserves lại → phá cam kết demand-driven.
- **Vòng thể chế (Warsh/Accord):** ba trụ (Treasury giữ duration; Fed thoát credit allocation/MBS; Congress tuyên bố crisis exception) — Fed nói "không" nhiều hơn để củng cố độc lập. → [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]]

---

## DIAGRAM

```mermaid
flowchart TB
    subgraph DEMAND["CẦU RESERVES (sàn cứng)"]
        REGYY[Reg YY / CLAR / RLAP\nưu tiên reserves > UST] --> FLOOR[(Sàn cầu reserves\n≈ 9% GDP ≈ $3,000B)]
        PAY[Receipt-reactive throttling\nFedwire] --> FLOOR
        ODF[Ngại daylight overdraft\n<$5B/ngày] --> FLOOR
    end
    subgraph FED["FED — bơm theo TREND"]
        RMP[RMP ~$40B/tháng] -->|+reserves| R[(Reserves $2,951.4B\n≈ floor)]
    end
    subgraph TREAS["TREASURY — hút theo SỰ KIỆN"]
        ISS[Vay $683B] --> TGA[(TGA $918.7B)]
    end
    FLOOR -.định mức.-> R
    TGA -->|dTGA = −dReserves| R
    R -->|ON RRP cạn $2.3B| SOFR{{SOFR–IORB gauge}}
    SOFR -->|+7bp / 1SD delay| SRF[SRF/SRP\nstigma + netting friction]
    subgraph EXIT["HẠ SÀN (Duffie menu)"]
        TOMO[1. TOMO sterilize] -.-> FLOOR
        REG2[2. Nới Reg YY] -.-> FLOOR
        LSM[3. LSM Fedwire] -.-> FLOOR
        TIER[4. Tiered IORB] -.-> FLOOR
    end
    classDef d fill:#6A1B9A,color:#fff; classDef fed fill:#2962FF,color:#fff; classDef tre fill:#D50000,color:#fff; classDef risk fill:#424242,color:#FFD600; classDef ex fill:#00897B,color:#fff;
    class REGYY,PAY,ODF,FLOOR d; class RMP,R fed; class ISS,TGA tre; class SOFR,SRF risk; class TOMO,REG2,LSM,TIER ex;
```

---

## KẾT LUẬN

Bảng cân đối Fed lớn là **hệ quả nội sinh** của hai lực: (1) hệ thống thanh toán cần một lượng reserves tối thiểu để ngân hàng thanh toán đúng hạn cho nhau mà không chạm Fed, và (2) liquidity regulation đẩy GSIB tích trữ reserves thay vì dùng nguồn Fed hay Treasuries. Cộng lại, chúng chốt một **sàn cứng** ~9% GDP. RMP, SRP và việc dừng QT chỉ là Fed *phòng thủ cái sàn đó* — reserves $2.95T sát đúng floor, ON RRP cạn, Treasury hút $683B, và SOFR–IORB là gauge của áp lực. Truyền dẫn stress đi qua **payment throttling** (vi mô), không chỉ qua identity TGA–reserves (vĩ mô).

Hệ quả chính sách then chốt: **muốn bảng cân đối nhỏ hơn, Fed phải hạ CẦU reserves trước** (TOMO → nới Reg YY → LSM → tiering), chứ cắt cung đơn thuần sẽ tái diễn 9/2019. Tầng thể chế phủ lên là tranh luận Warsh/Cochrane về việc tái định nghĩa ranh giới Fed–Treasury.

---

## NEXT STEPS (mở rộng wiki)

1. Tạo node **TOMO sterilization of reserve supply shocks** (TGA/FIMA/quarter-end) — hiện chỉ là section trong [[Payment_System_Floor_On_Fed_Balance_Sheet]].
2. Tạo node evidence **FBO quarter-end window dressing** (số liệu Crandall: ≥$200B/≥$300B/≥$400B).
3. Ingest văn bản SEC Treasury central clearing để xác nhận mốc compliance (đang flag chưa nguồn trong [[Treasury_Central_Clearing_Repo_Netting]]).
4. Node timeseries **SOFR–IORB daily H1 2026** từ FRED/NY Fed (hiện chỉ có mốc tham chiếu).
