---
title: SOFR–IORB Spread — Gauge Stress Thanh Khoản
aliases:
- SOFR IORB spread
- SOFR-IORB
- Repo rate stress gauge
- Chênh lệch SOFR IORB
type: evidence
tags:
- monetary-policy
- repo
- liquidity
- fed
- money-market
- current-events
status: reviewed
confidence: 4
half_life_years: 3
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie
provenance: "[RAW-BOOK: Duffie BPEA 2026 — Payments, Reserves & Liquidity]; [RAW-OFFICIAL: Fed H.4.1 (2026-06-24)]"
thesis: "SOFR–IORB spread là gauge stress thanh khoản chính của hệ thống Fed (KHÔNG phải EFFR): khi reserves của dealer bank xuống thấp, repo rate vọt trên IORB. Các mốc lịch sử: 31/10/2025 = +32bp (kích hoạt dừng QT); 17/09/2019 = +315bp (interdealer ~+1000bp); COVID 03/2020 = +44bp. EFFR thường không phản ánh stress vì fed funds market đã teo (~$3B liên ngân hàng/ngày)."
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[SOFR_IORB_Spread_Stress_Gauge]]

## Thesis

**SOFR–IORB spread** là thước đo stress thanh khoản đáng tin nhất của hệ thống Fed, thay cho EFFR. Lý do cấu trúc: thị trường fed funds đã teo — tổng vay/ngày ~$100B (2/2026), trong đó **<$3B là liên ngân hàng** (phần lớn là FHLB cho ngân hàng nước ngoài vay). Trong khi đó repo Treasury là thị trường ~**$8.8T outstanding (~$6T overnight)**, nơi chính sách tiền tệ thực sự truyền dẫn. **EFFR thường không phản ánh stress** trên thị trường repo lớn hơn nhiều này. [RAW-BOOK: Duffie BPEA 2026]

> SOFR = median gia quyền theo khối lượng của ~$3T giao dịch repo Treasury overnight. Logan & Schulhofer-Wohl (2025) đề xuất **TGCR** có thể là target phù hợp hơn EFFR cho FOMC.

---

## 1. Cơ chế: Reserves thấp → Repo rate vọt trên IORB

Khi reserves abundant, ngân hàng arbitrage chênh lệch IORB vs repo rate → SOFR bám sát IORB (floor system). Khi reserves khan, **shadow price của reserves tăng vọt**, dealer trì hoãn thanh toán ra, và repo rate bật lên trên IORB. Duffie (Figure 9): khi tổng reserves của 10 dealer bank thấp → SOFR–IORB nới rộng và spike.

**Predictor định lượng:** Tăng 1 độ lệch chuẩn của *trailing payment delay* (độ trễ thanh toán đến dealer bank) → dự báo **+7bp SOFR–IORB** (hồi quy OLS, Copeland-Duffie-Yang 2025).

---

## 2. Các mốc spread lịch sử (sourced anchors)

| Ngày | SOFR–IORB | Bối cảnh |
|---|---|---|
| **17/09/2019** | **+315bp** (interdealer repo ~+1000bp) | Repo crunch; reserves chạm đáy mẫu; payment delay lớn nhất 10 năm |
| **03/2020 (COVID)** | **+44bp** | Cú sốc COVID; Fed sau đó mua ồ ạt UST → reserves dồi dào → SOFR phẳng lại |
| **31/10/2025** | **+32bp** | Wholesale rate leo thang → kích hoạt FOMC dừng QT (29/10/2025); SRF rate lúc đó = IORB+10bp |

---

## 3. Bối cảnh H1 2026

- **29/10/2025:** FOMC tuyên bố ngừng thu hẹp bảng cân đối (kết thúc QT2), kích hoạt bởi chính đà nới rộng SOFR–IORB.
- **10/12/2025:** Fed khởi động [[Reserve_Management_Purchases_RMP]] — mua T-bills tạo **~$40B reserves/tháng đến 5/2026**.
- **QT2 (6/2022–12/2025):** Tổng reserves *không* giảm nhiều dù QT, vì tới **$2.5T reserves được thay bằng ONRRP**. Khi ONRRP cạn (còn $2.3B tại 24/06/2026 — xem [[Treasury_General_Account_Mechanism]]), tấm đệm này biến mất → SOFR–IORB nhạy hơn hẳn với mọi cú rút reserves.
- **Minh họa hành vi reserves:** JPMorgan rút gần **$350B** khỏi tài khoản Fed từ 2023 (từ $409B cuối 2023 còn $63B Q3/2025) để mua UST — cho thấy phần lớn reserves "dư" được coi là danh mục đầu tư, không phải nhu cầu vận hành.

### SOFR–IORB Monthly H1 2026 — Confirmed Data

*IORB = 3.75% (upper bound Fed funds 3.50–3.75%, unchanged H1 2026). SRF = 3.85%.*

| Tháng | SOFR avg | SOFR–IORB avg | High/Low | Stress? |
|-------|---------|--------------|---------|---------|
| Jan | 3.66% | **−9bp** | H: 3.75%=IORB ⚠️ / L: 3.63% | Tháng căng nhất — Jan high chạm floor |
| Feb | 3.67% | −8bp | H: 3.73% / L: 3.63% | Bình thường |
| Mar | 3.65% | −10bp | H: 3.71% / L: 3.62% | Bình thường |
| Apr | 3.64% | −11bp | H: 3.72% / L: 3.57% | Bình thường |
| May | 3.59% | **−16bp** | H: 3.64% / L: 3.50% | Very ample (SOFR −25bp IORB) |
| Jun | 3.63% | −12bp | H: 3.69% / L: 3.59% | Bình thường; spike Jun 15 (−6bp) |

**Kết luận H1 2026:** Không có SRF breach (max SOFR = 3.75% = IORB đúng, Jan). Spread range −25bp đến 0bp — ample reserves regime. Q2-end 30/06 là điểm rủi ro gần nhất (FBO window-dressing, không có ON RRP buffer).

*[RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026.md — sourced từ sofrrate.com + global-rates.com, June 2026]*

---

## 4. Ranh giới / Diễn giải (Boundary)

- **Gauge, không phải nhân quả tức thời:** spread có thể nhảy "với rất ít cảnh báo" (17/09/2019) — quan hệ reserves↔spread là phi tuyến, đuôi dày. Mức reserves "an toàn" hôm nay không đảm bảo an toàn ngày mai nếu payment delay tăng.
- **Data đã ingest H1 2026:** Chuỗi monthly SOFR H1 2026 + June daily đã ingest → `SOFR_IORB_Spread_H1_2026.md`. Xác nhận không có SRF breach. Khoảng trống còn lại: daily Jan–May (chưa có ngày cụ thể), và IORB timeline chi tiết nếu có thay đổi Fed funds target trong H1.

---

## Evidence / Source Anchors

- [RAW-BOOK] Spread mốc, cơ chế payment-delay, EFFR vs repo: [[Duffie_BPEA_Payments_Liquidity_2026.md]] (Figure 1, 9, 10)
- [RAW-OFFICIAL] Levels reserves/ONRRP/TGA: Fed H.4.1 (2026-06-24)

## Related

- [[Standing_Repo_Facility_SRF_Mechanics]] — van trần; spread đo độ "rò rỉ" của trần này.
- [[Reserve_Management_Purchases_RMP]] — bơm reserves theo trend để nén spread.
- [[Treasury_General_Account_Mechanism]] — cú rút TGA đẩy spread khi ONRRP cạn.
- [[Treasury_Central_Clearing_Repo_Netting]] — friction làm dealer ngại hấp thụ → khuếch đại spread.
- [[Central_Bank_Balance_Sheet_Trilemma]] — spread là tín hiệu Regime A đang căng.
