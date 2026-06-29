# Fed Balance Sheet H1 2026 — Tổng Hợp
> MODE DEEP | 2026-06-29 | Analyst: Claude (claude-sonnet-4-6)
> Nguồn: [RAW-OFFICIAL: H.4.1 24/06/2026] · [RAW-BOOK: Duffie BPEA 2026] · [RAW-OFFICIAL: Perli NY Fed 26/03/2026] · [WEB-2026-02-17: Cochrane] · [WEB-2026-04-11: Andreopoulos] · [RAW-BOOK: Copeland–Duffie–Yang 2025]

---

## TOP-DOWN ENTRY

| | |
|--|--|
| **Core Question** | Tại sao bảng cân đối Fed H1 2026 không thu nhỏ được, cơ chế nào tạo rủi ro dislocation, và cấu trúc kỳ hạn UST đặt duration risk ở đâu? |
| **Asset / Currency** | USD · Bank Reserves · UST (bills/notes/bonds) · MBS · TGA |
| **Temporal Status** | CURRENT 🟢 — as-of 24/06/2026 |
| **Thesis** | Ba lực quyết định bảng cân đối Fed H1 2026 hoạt động đồng thời: (1) hệ thống thanh toán chốt sàn cứng ~$3,000B reserves không thể cắt bằng cách giảm cung; (2) bất đối xứng nhịp giữa RMP (bơm theo trend ~$40B/tháng) và TGA rebuild (hút theo sự kiện $100–200B/tuần), trong môi trường ON RRP đã cạn ($2.3B), là nguồn gốc cấu trúc của rủi ro SOFR dislocation; (3) portfolio UST WAM ~7–8 năm [LLM-E] rút duration khỏi thị trường tư nhân, nén term premium, nhưng đồng thời tạo mismatch P&L khi Fed thu coupon cố định nhưng trả IORB thả nổi trên reserves. |

---

## MACRO LAYER

| Chiều | H1 2026 |
|-------|---------|
| **Regime** | Ample Reserves (Regime A) — Fed phòng thủ sàn reserves, không phải nới lỏng |
| **Policy Anchor** | IORB sàn / SRF = IORB+10bp trần (rò rỉ); Fed funds 3.50–3.75% [WEB-2026-05-08: Benigno] |
| **Balance Sheet** | Total assets $6,735.6B phẳng: UST $4,487.9B ↑ / MBS $1,963.4B ↓ [RAW-OFFICIAL: H.4.1] |
| **Fiscal** | Gross borrowing H1 ~$683B (+$249B YoY) [LLM-E]; trần nợ $41.1T (One Big Beautiful Bill Act) |
| **Tension** | QT kết thúc 01/12/2025; RMP chạy từ 10/12/2025; ON RRP $2.3B ≈ 0; reserves $2,951.4B sát floor |

Cần phân biệt ba chế độ: QE tạo net reserves mới + rút duration → nới lỏng tài chính thực sự. QT cắt assets → thắt chặt yếu (Atlanta Fed: $2.2T QT ≈ +0.29–0.74% rate-equivalent trong 3 năm [RAW-BOOK: Conks, citing Bin Wei]). **RMP giữ assets phẳng → không phải nới lỏng, chỉ phòng thủ floor** — Perli [RAW-OFFICIAL: 26/03/2026] nói thẳng: "hoàn toàn tách biệt khỏi chính sách tiền tệ".

## PLUMBING LAYER

**Sàn cứng từ hệ thống thanh toán.** Reserves hiện ~$3,000B — gấp ~300 lần mức 2007 (~$10B) [RAW-BOOK: Duffie BPEA 2026 §I]. Ba lực cấu trúc hậu GFC neo cầu ở mức cao: GSIB ngại daylight overdraft (toàn hệ thống <$5B/ngày vs ~$120B/ngày top-10 năm 2007 [RAW-BOOK: Duffie §I.D]); IORB trả ~lãi thị trường → không còn động lực cho vay liên ngân hàng (thị trường fed funds teo <$3B liên ngân hàng/ngày); FDIC fee 42bp + special 13bp (hậu SVB) cộng leverage requirements → ma sát liên ngân hàng cao. Giám sát viên ưu tiên reserves hơn UST trong thanh khoản (CLAR/RLAP coi UST không phải cash-equivalent khi thanh lý lớn) → **sàn ~9% GDP ≈ $3,000B** [WEB-2026-04-11: Andreopoulos] là ràng buộc cứng, không phải lựa chọn.

**Bất đối xứng nhịp và identity flow.** Với ON RRP ≈ 0, identity co lại thành `ΔReserves ≈ RMP_bơm − ΔTGA − ΔCurrency` — mọi swing TGA truyền 1:1 vào reserves, không có tầng trung gian (khác H1 2023 khi ON RRP >$2,000B hấp thụ toàn bộ TGA swing [RAW-OFFICIAL: H.4.1 series]). RMP bơm ~$40B/tháng đều đặn (trend); Treasury hút $100–200B/tuần theo lịch auction (event). Khe giữa hai nhịp — đặc biệt khi trùng với quarter-end FBO window-dressing (≥$200B trong 15 quý gần đây [RAW-BOOK: Duffie, citing Crandall]) hoặc tax date — là nơi reserves dao động dưới floor. Khi xảy ra, cơ chế lan truyền qua payment throttling [RAW-BOOK: Copeland–Duffie–Yang 2025]: dealer làm chậm thanh toán ra → self-fulfilling delay → shadow price reserves nhảy bậc → SOFR bật vượt IORB. Định lượng: **+1SD payment delay → +7bp SOFR–IORB** (OLS). Tiền lệ: 17/09/2019, SOFR–IORB +315bp; SRF không giữ trần do stigma + eSLR netting friction ($50B rút vs cơ hội +32bp ngày 31/10/2025 [RAW-BOOK: Duffie §V]).

**Cấu trúc kỳ hạn UST và mismatch P&L.** Fed nắm $4,487.9B UST với WAM ước tính ~7–8 năm [LLM-E], tập trung ở notes/bonds (từ QE era). Đây là lượng duration lớn rút khỏi tay tư nhân → nén term premium cấu trúc. Nhưng với total assets phẳng (RMP không mở rộng portfolio) và Treasury phát hành gross $683B H1, tư nhân phải hấp thụ toàn bộ net issuance mới → term premium có xu hướng nới dần. Đồng thời, mismatch kỳ hạn tạo bất đối xứng P&L [WEB-2026-02-17: Cochrane]: QE đã đổi nợ cố định dài hạn của Treasury thành nợ overnight thả nổi (reserves tại IORB) — khi rates cao, Fed thu coupon cố định ~2–3% (QE era) nhưng trả IORB ~4–5%, tích lũy deferred asset [LLM-E: đỉnh ~$200B, 2023–2024]. RMP đang thêm bills/short notes → WAM rút ngắn dần, nhưng stock notes/bonds vẫn chiếm ~75% portfolio [LLM-E].

## TREASURY LAYER

Desk cần hiểu sự phân biệt giữa ba loại rủi ro đang đồng thời hiện diện. **Rủi ro ngắn hạn (ngày → tuần):** SOFR–IORB là gauge chính, không phải EFFR. Khi spread nới >15bp liên tiếp 2 phiên, kiểm tra ngay lịch auction Treasury tuần đó và payment delay data (Fedwire statistics, NY Fed) — hai chỉ báo sớm trước khi SOFR spike. Q2 end 30/06/2026 là điểm FBO window-dressing gần nhất; tính toán reserves impact trước. SRF không đảm bảo giữ trần — đừng giả định IORB+10bp là ceiling cứng.

**Rủi ro trung hạn (tuần → tháng):** RMP là backstop trend không phải van ngày. Nếu nhịp vay Treasury vượt nhịp RMP (event hút > trend bơm trong khoảng thời gian cụ thể), reserves thủng floor trước kỳ RMP tiếp theo. Map lịch coupon refunding mid-month vào dự báo funding cost theo tuần. Theo dõi quy mô RMP sau 5/2026 — hiện chưa có thông báo [LLM: cần raw source].

**Rủi ro dài hạn (tháng → năm):** Term premium nới dần khi tư nhân hấp thụ thêm duration từ Treasury issuance mới mà Fed không mở rộng portfolio. Track ACM 10Y term premium (NY Fed) và Treasury auction tail như leading indicator. Nếu Warsh chủ động chuyển portfolio sang bills-only, WAM rút nhanh → duration được trả lại thị trường → 10Y yield tăng cấu trúc → thắt chặt financial conditions từ phía supply.

- **Ngắn hạn:** SOFR–IORB daily + Fedwire payment delay + lịch auction theo tuần; Q2-end 30/06 là điểm gần nhất
- **Trung hạn:** RMP composition (bills vs coupons) là signal về intent; coupon refunding calendar mid-month vào funding cost model
- **Dài hạn:** ACM term premium + Treasury auction bid-to-cover/tail + deferred asset trajectory dưới Warsh tenure

---

## TIMING LAYER

| | Past | Present H1 2026 | Future |
|--|------|-----------------|--------|
| **Regime** | QE: +$3.3T reserves, WAM kéo dài; QT2: −$2.2T, ON RRP làm đệm → reserves ổn định | RMP phẳng; reserves $2,951B = floor; ON RRP $2.3B = 0; WAM ~7–8 năm [LLM-E] | Phẳng trừ crisis; WAM rút ngắn nếu Warsh bills-only; term premium nới nếu không mở rộng portfolio |
| **Plumbing** | 9/2019: reserves $1.4T → SOFR–IORB +315bp [RAW-BOOK: Duffie Fig.9]; 2023: TGA rebuild $500B+ nhưng ON RRP >$2T làm đệm | Biên an toàn ≈ 0; swing TGA → reserves 1:1; SRF rò rỉ; Q2-end FBO sắp tới (30/06) | Synchronization risk: TGA event + FBO cuối quý + khe RMP → amplification |
| **Duration** | QE: rút ~$4T+ duration equivalent; Operation Twist: bán ngắn mua dài → WAM đỉnh ~8–10 năm | Giữ ~$4,488B UST; tư nhân hấp thụ $683B gross H1 mới; term premium tăng dần | Nếu Warsh thu nhỏ portfolio → term premium tăng nhanh; nếu rates giảm → deferred asset giảm, P&L cải thiện |

**Velocity:** Thanh khoản reserves truyền dẫn trong ngày → overnight (Fedwire settle). Term premium phản ứng theo tháng → quý. Deferred asset thay đổi theo quý.

**Synchronization risk H2 2026:** Ba lực TGA event lớn + FBO window-dressing cuối Q3 (30/09) + khe nhịp RMP có thể kích hoạt đồng thời — cộng hưởng không có ON RRP làm đệm.

## FEEDBACK / BOUNDARY

| Signal | Theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|----------|------------------|---------|
| Reserves stress | SOFR–IORB daily | >32bp = FOMC phản ứng (tiền lệ 31/10/2025) | Chưa có daily H1 2026 [gap] |
| Term premium | ACM 10Y (NY Fed) | Nới >50bp trong <3 tháng | Chưa có H1 2026 [gap] |
| Auction demand | Bid-to-cover + tail 10Y/30Y | BTC <2.3 liên tiếp 2 lần; tail >2bp | Cần ingest [gap] |
| Deferred asset | Fed remittance to Treasury | Tiếp tục $0 + tăng → áp lực chính trị Warsh | Vẫn $0 ước tính [LLM-E] |

**Failure conditions:** (1) Fed triển khai TOMO sterilization theo sự kiện (offset TGA swing trong ngày) → bất đối xứng nhịp bị triệt tiêu, toàn bộ rủi ro khe nhịp giảm — đây là công cụ Duffie ưu tiên số một, không cần luật mới [RAW-BOOK: Duffie BPEA 2026 §VIII]. (2) Warsh chuyển portfolio sang bills-only → WAM rút nhanh → term premium tăng mạnh → thắt chặt điều kiện tài chính từ phía duration, không phải phía rates.

**Liên kết cấu trúc — đầu ngắn và đầu dài là cùng một chuyển dịch:** Căng thẳng dự trữ (SOFR–IORB) và đảo ngược duration (term premium nới rộng) không phải hai rủi ro độc lập — chúng là hai biểu hiện đồng thời của cùng một lực tài khóa-tài chính: Kho bạc vay $683B gross H1 2026, tư nhân phải hấp thụ nhiều hơn cả rủi ro thanh khoản ngắn hạn (giải phóng TGA → hút reserves) lẫn rủi ro duration dài hạn (net issuance mới → cộng cung 10–30Y không có Fed bù đắp) so với bất kỳ thời điểm nào từ 2008. Phân tích chi tiết kênh duration: `2026-06-29_fed-duration-extraction-term-premium.md`.

---

## DIAGRAM

```
  ASSET SIDE                              LIABILITY SIDE
  ┌───────────────────────────┐          ┌────────────────────────────────┐
  │ UST Notes/Bonds ~75%      │ P&L      │ RESERVES $2,951.4B ← sát FLOOR│
  │ WAM ~7–8yr [LLM-E]        │ MISMATCH │                                │
  │ coupon ~2–3% (cố định)    │◄────────►│ IORB ~4–5% (thả nổi)          │
  │                           │          │                                │
  │ UST Bills ~5%             │ RMP bơm  │ + RMP +$40B/tháng (TREND)     │
  │ WAM <1yr (đang tăng)      │ +$40B/mo │ − TGA −$100–200B/tuần (EVENT) │
  │                           │─────────►│ − FBO ≥$200B cuối quý          │
  │ MBS $1,963.4B             │ Runoff   │                                │
  │ (giảm $15–20B/tháng)      │─────────►│ ON RRP $2.3B ≈ 0              │
  └───────────────────────────┘          │ (KHÔNG CÒN ĐỆM TRUNG GIAN)   │
                                         └────────────────────────────────┘
  DURATION RISK DISTRIBUTION                    KHI RESERVES < FLOOR:
  ┌──────────────────────────┐           Dealer throttle thanh toán ra
  │ Fed giữ ~$4,488B UST     │           → Self-fulfilling delay
  │ → nén term premium       │           → SOFR bật vượt IORB
  │ → nợ fixed → float       │           [+315bp tiền lệ 17/09/2019]
  │                          │
  │ Tư nhân: phải hấp thụ   │           KHI WARSH THU NHỎ PORTFOLIO:
  │ $683B gross H1 2026 MỚI  │           WAM rút ngắn → duration trả lại
  │ → term premium nới dần   │           → 10Y yield tăng cấu trúc
  └──────────────────────────┘           → thắt chặt từ phía supply
```

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | Confirmed — ba lực đồng thời: sàn cứng từ payment system; bất đối xứng nhịp RMP/TGA khi ON RRP = 0; mismatch P&L từ WAM dài trên nền IORB thả nổi |
| **Net Plumbing Effect** | Reserves $2,951B = floor, biên ≈ 0; tư nhân hấp thụ toàn bộ net issuance mới; term premium nới dần; SRF trần rò rỉ |
| **Treasury Action** | SOFR–IORB daily (gauge ngắn hạn) → ACM term premium (gauge dài hạn); map lịch auction tuần; Q2-end 30/06 là điểm rủi ro gần nhất; theo dõi RMP composition sau 5/2026 |
| **Confidence** | TIER B/C — stock data sourced (H.4.1); flow H1 2026 [LLM-E]; WAM/deferred asset [LLM-E]; thiếu daily timeseries và auction data để nâng TIER B |
| **Critical Caveat** | TOMO sterilization (nếu Fed triển khai) triệt tiêu rủi ro nhịp; Warsh bills-only (nếu xảy ra) tạo rủi ro term premium mới — hai biến số thể chế chưa xác nhận |

---

## NEXT STEPS

```bash
# Data gaps ưu tiên
# → H.4.1 maturity schedule UST (bills/notes/bonds/TIPS)
# → NY Fed ACM 10Y term premium daily H1 2026
# → Treasury auction results H1 2026 (BTC, tail, stop-out)
# → SOFR–IORB daily từ FRED + NY Fed

# Nodes đã tạo
# ✓ 03_wiki/mechanisms/Fed_Duration_Extraction_Term_Premium.md
# ✓ 03_wiki/mechanisms/TOMO_Reserve_Supply_Sterilization.md
# ✓ 03_wiki/evidence/Fed_Deferred_Asset_2022_2026.md
# ✓ 06_publish/2026-06-29_fed-duration-extraction-term-premium.md

python librarian.py embed --incremental && python librarian.py sync
```

*MODE DEEP v1 | 2026-06-29 | Refs: P1 · P2 · P3 · P4 | [[Payment_System_Floor_On_Fed_Balance_Sheet]] · [[Reserve_Management_Purchases_RMP]] · [[Treasury_General_Account_Mechanism]] · [[SOFR_IORB_Spread_Stress_Gauge]] · [[Receipt_Reactive_Payment_Throttling]] · [[Standing_Repo_Facility_SRF_Mechanics]] · [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]]*
