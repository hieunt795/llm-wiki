# Bảng Cân Đối Fed H1 2026 — Phân Tích Tích Hợp: Stock + Flow

*Research note — 29/06/2026. Nguồn lõi: Darrell Duffie, BPEA Spring 2026 ("The Payment System Puts a Floor on the Fed's Balance Sheet"); Fed H.4.1 (24/06/2026); NY Fed Perli (26/03/2026); Treasury Q2 2026 Refunding; Andreopoulos (11/04/2026); Cochrane/Warsh (17/02/2026); Copeland–Duffie–Yang (2025).*

---

## Tóm Tắt Điều Hành

Bảng cân đối Fed H1 2026 là câu chuyện về **hai thứ xảy ra đồng thời nhưng với nhịp khác nhau**: (1) sàn cứng ~$3T reserves do hệ thống thanh toán + quy chế chốt lại — không thể cắt được, và (2) Treasury hút reserves theo sự kiện với biên độ $100–200B/tuần trong khi Fed chỉ bơm lại theo trend đều ~$40B/tháng qua RMP. ON RRP đã cạn ($2.3B), nghĩa là không còn đệm trung gian — mọi swing TGA đổ thẳng 1:1 vào reserves. Tại H.4.1 24/06/2026: reserves $2,951B sát đúng floor, biên an toàn ≈ 0.

Hai hàm ý cốt lõi: (i) muốn bảng cân đối nhỏ hơn, Fed phải *hạ cầu* reserves trước, không thể cắt cung đơn thuần; (ii) rủi ro dislocation không đến từ xu hướng mà từ **khe nhịp** — khoảng trống giữa hai kỳ RMP trùng với auction settle lớn hoặc cuối quý FBO.

---

## Phần I — Khung Stock: Tại Sao Bảng Cân Đối Lớn Là Hệ Quả, Không Phải Lựa Chọn

### 1.1 Snapshot H.4.1 — 24/06/2026

| Khoản mục | Giá trị | So sánh / Ý nghĩa |
|---|---|---|
| **Total Assets** | $6,735.6B | Phẳng (QT kết thúc 01/12/2025) |
| UST holdings | $4,487.9B | Tăng so với QT-end (RMP mua ròng) |
| MBS holdings | $1,963.4B | Giảm liên tục (runoff, không tái đầu tư) |
| **Reserve Balances** | **$2,951.4B** | Sát floor ~$3,000B — biên an toàn ≈ 0 |
| TGA | $918.7B | Giảm từ đỉnh ~$1,025B (T4/2026, mùa thuế) |
| **ON RRP (others)** | **$2.3B** | Đệm đã cạn — không còn hấp thụ swing TGA |
| RRP foreign official | $331.4B | Structural, không phải biến đệm |

### 1.2 Ba Lực Chốt Sàn Reserves (~$3T)

**Lực 1 — Ngại daylight overdraft:**
- Top-10 ngân hàng overdraft trung bình ~$120B/ngày trên Fedwire (2007)
- Toàn hệ thống <$5B/ngày (2025) — GSIB sợ supervisor đọc là vi phạm tự chủ thanh khoản (Reg YY)
- Hệ quả: ngân hàng giữ reserves dày thay vì dựa vào overdraft trong ngày

**Lực 2 — Mất động lực cho vay liên ngân hàng:**
- Fed trả IORB ~lãi thị trường cho *mọi* mức reserves → không còn động lực cho vay như pre-GFC
- VD: JPMorgan rút ~$350B khỏi tài khoản Fed từ 2023 ($409B → $63B) để mua UST — nhưng *cả hệ thống* vẫn cần giữ đệm dày để vận hành thanh toán

**Lực 3 — Ma sát liên ngân hàng tăng:**
- FDIC insurance fee 42bp + special assessment 13bp (hậu SVB 2023)
- Capital/leverage requirements cao hơn
- Thị trường liên ngân hàng teo: <$3B/ngày vs repo Treasury ~$8.8T outstanding (~$6T overnight)

**Kết quả:** Giám sát viên ưu tiên reserves hơn UST trong yêu cầu thanh khoản (CLAR/RLAP coi UST không cash-equivalent khi thanh lý lớn). "Red line" Dimon: balance tại Fed không được chạm 0 ngay cả khi stress trong ngày. Đây là sàn cứng — không thể phá bằng cách cắt cung.

### 1.3 Vì Sao SRF Không Giữ Được Trần

Standing Repo Facility (rebrand thành SRP, full-allotment từ 10/12/2025, giá IORB+10bp) được thiết kế làm trần cho lãi repo. Trên thực tế trần bị rò rỉ vì hai lý do:

- **Stigma:** Lãnh đạo GSIB tại hội nghị Chatham House 11/2025 nói thẳng — "chỉ dùng khi sống còn". Không ngân hàng nào muốn bị đọc là phụ thuộc Fed.
- **Netting friction:** Fed không central-clear repo → dealer không thể net giao dịch SRF với reverse repo cấp cho khách → mỗi SRF transaction phình bảng cân đối, đội eSLR.

*Bằng chứng:* 31/10/2025 SOFR vượt +32bp trên IORB, cơ hội chênh lệch rõ ràng, nhưng chỉ $50B rút SRF. 31/12/2025 = $75B. Trần không giữ.

---

## Phần II — Khung Flow: Biến Động Thực Tế H1 2026

### 2.1 Identity Kế Toán — Trước Khi Phân Tích Flow

Bảng cân đối Fed tuân theo đẳng thức:

```
ΔAssets = ΔReserves + ΔTGA + ΔON_RRP + ΔCurrency + ΔOther_liab
```

**Điểm ngoặt cấu trúc H1 2026:** ON RRP ≈ 0, QT đã xong, tổng asset gần phẳng. Identity co lại thành:

```
ΔReserves ≈ RMP_bơm − ΔTGA − ΔCurrency_in_circulation
```

**Hệ quả:** Mọi đồng TGA rebuild đổ thẳng 1:1 vào reserves. Không còn đệm trung gian.

### 2.2 Timeline Sự Kiện — H2 2025 → H1 2026

```
QT2 ĐANG CHẠY         │FOMC DỪNG│  RMP BẮT ĐẦU │  H1 2026
(Cắt assets ~$2.2T)   │  QT2    │  (~$40B/mo)  │  (TGA rebuild $683B)
──────────────────────┬──────────┬──────────────┬──────────────────────►
 6/2022             29/10/2025 10/12/2025     Q1–Q2 2026       24/06/2026
                    +32bp       SRF rebrand   Tax season       H.4.1 snapshot
                    SOFR spike  full-allotment  TGA → đỉnh      Reserves $2,951B
                    kích hoạt   IORB+10bp      ~$1,025B         sát floor
```

**Điểm ngoặt quan trọng:**
- **29/10/2025** — FOMC tuyên bố dừng QT, *kích hoạt bởi* SOFR–IORB +32bp, không phải chủ động
- **01/12/2025** — QT2 chính thức kết thúc (cắt tổng cộng >$2.2T kể từ 6/2022)
- **10/12/2025** — RMP khởi động (~$40B/tháng đến 5/2026); SRF rebrand full-allotment
- **T1–T4/2026** — Treasury vay ồ ạt (+$683B H1, +$249B YoY) sau khi One Big Beautiful Bill Act nâng trần nợ lên $41.1T
- **T4/2026 (tax season)** — TGA đạt đỉnh ~$1,025B, reserves chịu lực hút cực đại
- **T5–T6/2026** — Chi tiêu ngân sách + drawdown TGA giảm tải một phần
- **24/06/2026** — Reserves $2,951B, TGA $918.7B, ON RRP $2.3B

### 2.3 Flow Phía Tài Sản (Asset Side)

| Khoản mục | Hướng Flow | Quy mô ước tính H1 2026 | Cơ chế |
|---|---|---|---|
| MBS holdings | **−↓** tự nhiên | ~$15–20B/tháng runoff = ~$90–120B trong 6 tháng | Prepayment + maturity, không tái đầu tư vào MBS |
| UST holdings | **+↑** qua RMP | ~$40B/tháng → ~$200–240B trong 6 tháng | NY Fed Desk mua secondary market |
| **Net tổng tài sản** | **≈ phẳng** | $6,735.6B | MBS proceeds → UST; tổng giữ nguyên |

**Cơ chế xoay cơ cấu:** MBS runoff proceeds + RMP → Fed mua UST (không mua MBS mới) → portfolio xoay **UST↑ / MBS↓** trong khi tổng gần phẳng. Đây là cấu trúc lại danh mục, *không phải* nới lỏng.

**T-account RMP (ví dụ $40B/tháng):**
```
         FEDERAL RESERVE                      PRIMARY DEALER
  Assets          │ Liabilities         Assets         │ Liabilities
──────────────────┼─────────────     ───────────────── ┼────────────
UST    [+$40B]    │ Reserves [+$40B]  UST    [-$40B]   │ (không đổi)
                  │                   Reserves [+$40B]  │
```

### 2.4 Flow Phía Nguồn Vốn (Liability Side)

#### Reserves — Bị Kẹp Hai Đầu

```
     RMP bơm +$200–240B                  TGA hút −$400–500B
     (trend, đều, ~$40B/tháng)           (event, đột ngột, theo lịch)
              ↘                                    ↙
         Reserves $2,951.4B ← kẹp giữa → sát floor $3,000B
              ↗
     Currency drain ~−$15–20B (tự trị, ổn định, theo GDP danh nghĩa)
```

**Flow ước tính H1 2026:**

| Nguồn | Hướng ΔReserves | Quy mô ước tính | Nhịp |
|---|---|---|---|
| RMP mua UST | **+** | ~+$200–240B | Trend, đều |
| TGA rebuild (gross $683B − chi tiêu) | **−** | ~−$400–500B net | Event, đột ngột |
| Currency in circulation | **−** | ~−$15–20B | Tự trị, ổn định |
| MBS runoff (tái đầu tư vào UST) | Neutral | Đã offset trong asset side | |
| FBO window-dressing cuối quý | **−** (tạm thời) | ≥−$200B (15 quý gần đây) / ≥−$400B (2 quý) | Cuối Q1, Q2 |

**Net:** Reserves gần phẳng theo xu hướng — nhưng dao động lớn theo từng sự kiện. Kết quả cuối H1: $2,951B.

*Lưu ý về gross vs net TGA:* $683B là gross borrowing Treasury. TGA thực tế = borrowing − chi tiêu ngân sách; chi tiêu trả reserves lại hệ thống. Cần phân biệt khi đọc số liệu tuần.

#### TGA — Vận Động Theo Mùa

```
T1–T3 (Jan–Mar):  Phát hành Bills + Coupons → TGA tăng → Reserves hút mạnh
T4 (Apr):         Tax season → TGA đạt đỉnh ~$1,025B ← Reserves chịu lực hút cực đại
T5–T6 (May–Jun):  Chi tiêu > vay mới → TGA drawdown → Reserves bơm lại một phần
24/06/2026:       TGA $918.7B (giảm $106B từ đỉnh T4)
```

**T-account TGA rebuild điển hình (Treasury phát hành $100B):**
```
         FEDERAL RESERVE                    COMMERCIAL BANKS / DEALERS
  Assets          │ Liabilities          Assets          │ Liabilities
──────────────────┼──────────────     ──────────────────┼─────────────
(không đổi)       │ Reserves [-$100B]  Reserves [-$100B] │ (không đổi)
                  │ TGA      [+$100B]  UST      [+$100B] │
```

#### ON RRP — Đệm Biến Mất

| Mốc | ON RRP | Chức năng đệm |
|---|---|---|
| Đỉnh 2023 | >$2,000B | Hấp thụ *toàn bộ* swing TGA → reserves gần không động |
| Giữa 2024 | ~$300–500B | Đệm giảm dần |
| Cuối 2025 | ~$100B | Đệm mỏng |
| **24/06/2026** | **$2.3B** | **Đệm = 0 → mọi swing TGA → reserves** |

**Khác biệt cấu trúc 2023 vs 2026:**
- 2023: Cú nạp TGA rút từ ON RRP trước → reserves gần như không động dù Treasury vay lớn
- 2026: ON RRP cạn → identity `dTGA = −dReserves` áp dụng ngay tức thì, không trung gian

### 2.5 Flow Tài Khóa — Treasury Phía Bên Kia

**Gross borrowing H1 2026: ~$683B (+$249B YoY)**

Bối cảnh: One Big Beautiful Bill Act nâng trần nợ lên $41.1T → Treasury thoát extraordinary measures → vay ồ ạt để rebuild TGA sau khoảng thời gian bị kẹt. Flow vay +$249B YoY là cú sốc tài khóa lớn nhất phía cầu reserves trong H1 2026.

| Loại công cụ | Tác động flow reserves | Nhịp |
|---|---|---|
| T-bills (ngắn hạn, rollover thường xuyên) | Rút mạnh, liên tục | Hàng tuần (thứ Tư/Năm auction) |
| Notes/Bonds (dài hạn) | Rút lớn theo lịch refunding | Hàng tháng (mid-month settle) |
| TIPS | Nhỏ hơn | |

---

## Phần III — Tổng Hợp: Bất Đối Xứng Nhịp Là Rủi Ro Cốt Lõi

### 3.1 Sơ Đồ Flow Tích Hợp

```
         ASSET SIDE                              LIABILITY SIDE
  ┌───────────────────────┐            ┌────────────────────────────────────┐
  │ MBS runoff            │            │ RESERVES $2,951.4B (sát floor)     │
  │ ~$15–20B/tháng        │──RMP bơm──►│                                    │
  │ (proceeds → UST)      │  +$200–    │  + RMP +$200–240B (trend, đều)     │
  │                       │   240B     │  − TGA rebuild ~$400–500B (event)  │
  │ UST mua qua RMP       │            │  − Currency ~$15–20B (tự trị)      │
  │ +$40B/tháng           │            │  − FBO window-dress ≥$200B (Q-end) │
  │                       │            ├────────────────────────────────────┤
  └───────────────────────┘            │ TGA $918.7B                        │
           ▲                           │ (đỉnh ~$1,025B T4 → drawdown T5–6) │
           │                           ├────────────────────────────────────┤
  Net assets ≈ phẳng                   │ ON RRP $2.3B ≈ 0                   │
  $6,735.6B                            │ (đệm biến mất — swing TGA thẳng    │
                                       │  vào reserves, không có trung gian) │
                                       └────────────────────────────────────┘
```

### 3.2 Khe Nhịp — Nơi Stress Nổ

Rủi ro không đến từ xu hướng (RMP bù được theo trend) mà từ **khe hở giữa hai nhịp khác tần số:**

```
Fed bơm (RMP):          ├──────$40B──────┤          ├──────$40B──────┤
                        ^                ^          ^
                     bơm kỳ 1        bơm kỳ 2   bơm kỳ 3
                                     ↑
Treasury hút:      ──$100B──$80B──$120B──$60B── (auction settle hàng tuần)
                                     ↑
                            [KHE NGUY HIỂM]
                        Treasury hút mạnh trong tuần
                        RMP chưa bơm kỳ tiếp
                        → Reserves chạm floor hoặc thủng
                        → SOFR–IORB nới đột ngột
```

**Stress calendar — điểm nóng theo lịch:**

| Thời điểm | Sự kiện flow | Hướng ΔReserves | Nguy cơ |
|---|---|---|---|
| Thứ Tư/Năm hàng tuần | Treasury auction settle | **Hút mạnh** ($100–200B) | Cao trong tuần auction lớn |
| Giữa hai kỳ RMP | Chưa bơm bù | **Chưa bù** | Khe tích lũy |
| Cuối tháng 3/6/9/12 (quarter-end) | FBO window-dressing | **Hút thêm ≥$200B** | Cộng hưởng với khe RMP |
| Tax date (T4/2026 ~ April 15) | TGA đạt đỉnh | **Cực đại lực hút** | Biên reserves thấp nhất |
| SRF kích hoạt (nếu cần) | Van trần, nhưng stigma + eSLR | **Bù không đủ** | Trần vẫn rò rỉ |

### 3.3 Gauge Stress — SOFR–IORB

SOFR–IORB spread là thước đo stress đáng tin nhất (không phải EFFR — thị trường fed funds <$3B liên ngân hàng/ngày, không đại diện).

**Cơ chế khuếch đại phi tuyến (payment throttling):**
1. Reserves thấp → dealer throttle thanh toán ra, chờ tiền vào (receipt-reactive)
2. Nhiều dealer cùng chờ → kỳ vọng tự thỏa mãn (self-fulfilling delay)
3. Shadow price reserves nhảy bậc → SOFR bật vượt IORB
4. Định lượng: **+1SD payment delay → +7bp SOFR–IORB** (Copeland–Duffie–Yang 2025 OLS)

**Mốc lịch sử:**
| Ngày | SOFR–IORB | Bối cảnh |
|---|---|---|
| 17/09/2019 | **+315bp** (interdealer ~+1000bp) | Reserves chạm ~$1.4T; payment delay lớn nhất 10 năm |
| 03/2020 (COVID) | **+44bp** | Cú sốc; Fed mua ồ ạt → SOFR phẳng lại |
| 31/10/2025 | **+32bp** | Kích hoạt FOMC dừng QT; chỉ $50B rút SRF |

Hiện tại (H1 2026): ON RRP cạn → SOFR–IORB nhạy hơn hẳn với *mọi* cú rút reserves. Không còn lớp đệm hấp thụ.

---

## Phần IV — Hàm Ý Chính Sách

### 4.1 Menu Hạ Sàn (Duffie §VIII — theo thứ tự khả thi)

| Ưu tiên | Công cụ | Trạng thái | Ghi chú |
|---|---|---|---|
| **1** | **TOMO sterilize** cú sốc TGA/FIMA/FBO cuối quý | Khả thi ngay — không cần luật mới | Cho phép đường reserves thấp và trơn hơn |
| **2** | **Nới Reg YY** — cho non-HLA tính vào thanh khoản; bình thường hóa daylight overdraft | Cần regulatory action | Bỏ thiên vị reserves > UST |
| **3** | **LSM cho Fedwire** — net thanh toán lớn | Dự án nhiều năm | CHAPS/BOJ-NET tiết kiệm 15–30% reserves |
| **4** | **Tiered IORB** — kích interbank lending | Dự án nhiều năm | Norway/NZ đã làm sống lại interbank market |

### 4.2 Hàm Ý Cho Treasury Desk

- **RMP là backstop cấu trúc nhưng không che cú sốc TGA ngày-cụ-thể** — cần map lịch auction Treasury vào dự báo funding cost
- **Theo dõi SOFR–IORB là gauge chính**, không phải EFFR
- **Leading indicators:** payment-delay data (NY Fed) + lịch FBO window-dressing cuối quý
- **Điểm nguy hiểm nhất:** khe nhịp giữa hai kỳ RMP *trùng với* auction settle lớn *và/hoặc* cuối quý

### 4.3 Tranh Luận Thể Chế Warsh/Cochrane ("Accord Mới")

Ba câu hỏi bên trên tất cả cơ chế:
1. **Ai giữ duration risk?** Treasury hay Fed? (Hiện Fed giữ ~$4.5T UST dài hạn)
2. **Fed có nên rút khỏi credit allocation?** MBS = can thiệp vào thị trường nhà ở; nhiều người muốn Fed thoát hoàn toàn
3. **Crisis exception có nên cần Quốc hội tuyên bố?** Tăng accountability, giảm moral hazard — nhưng chậm hơn khi khủng hoảng

---

## Phần V — Gaps Cần Ingest (Data Còn Thiếu)

| Thiếu | Ghi chú |
|---|---|
| Daily SOFR–IORB timeseries H1 2026 | Cần FRED (IORB) + NY Fed (SOFR daily) |
| RMP purchase data theo từng tuần (NY Fed Desk reports) | Hiện chỉ có "~$40B/tháng đến 5/2026" |
| TGA daily từ TreasuryDirect H1 2026 | Chỉ có mốc đỉnh ~$1,025B và 24/06 snapshot |
| FBO window-dressing Q1/Q2 2026 số liệu thực | Hiện chỉ có pattern lịch sử (Crandall: ≥$200/300/400B) |
| SEC Treasury central clearing compliance deadline | Mốc thực tế chưa có raw source; có thể đẩy sàn reserves lên |
| RMP quy mô sau 5/2026 | Perli 3/2026 nói "đến 5/2026"; điều chỉnh sau chưa rõ |

---

## Kết Luận

Bảng cân đối Fed H1 2026 lớn vì *hệ thống bắt buộc như vậy* — payment system + Reg YY chốt sàn cứng ~9% GDP. Nhưng rủi ro không nằm ở quy mô trung bình mà ở **bất đối xứng nhịp giữa RMP (trend) và TGA (event)** trong một môi trường ON RRP đã cạn. Reserves $2,951B sát đúng floor, không còn đệm, và mọi cú sốc tài khóa từ Treasury (auction settle lớn, tax date, debt ceiling dynamics) đổ thẳng vào reserves với không có tầng trung gian hấp thụ.

Gauge theo dõi: **SOFR–IORB daily**. Lịch rủi ro: **auction settle weeks + quarter-end FBO**. Con đường thoát dài hạn: **hạ cầu reserves** (TOMO → nới Reg YY → LSM → tiering) — không thể thoát bằng cắt cung đơn thuần mà không tái diễn tháng 9/2019.

---

*Note này tích hợp phân tích stock (cấu trúc và nguyên nhân) và phân tích flow (biến động H1 2026 theo từng dòng). Phân tích kỹ thuật đầy đủ theo 5 Lenses: xem `Fed_Treasury_Balance_Sheet_H1_2026_MODE_DEEP_v2.md`. Wiki nodes nền: [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Receipt_Reactive_Payment_Throttling]] · [[Standing_Repo_Facility_SRF_Mechanics]].*
