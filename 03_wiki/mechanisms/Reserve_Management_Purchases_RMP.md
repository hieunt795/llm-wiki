---
title: Reserve Management Purchases (RMP)
aliases:
- RMP
- Reserve Management Purchases
- Organic Balance Sheet Growth
- Trend-Growth Treasury Purchases
type: mechanism
tags:
- central-banking
- liquidity
- monetary-operations
- fed
- central-bank-balance-sheet
status: reviewed
confidence: 4
half_life_years: 8
school: ''
superseded_by: null
superseded_date: null
expert_lens: Roberto Perli (NY Fed Desk) | Roc Armenter
provenance: "[RAW-OFFICIAL: NY Fed Perli speech (2026-03-26)]; [RAW-OFFICIAL: Fed H.4.1 weekly series Jan-Jun 2026]"
thesis: Reserve Management Purchases (RMP) là cơ chế Fed mua ròng UST với quy mô đủ
  khớp tăng trưởng theo trend của cầu dự trữ (reserve demand), nhằm giữ reserves trên
  ngưỡng ample floor sau khi QT kết thúc (01/12/2025) mà không nới lỏng chính sách —
  khác QE về intent (kỹ thuật vận hành, không phải kích thích). RMP bơm theo xu hướng
  (trơn, có độ trễ), tạo bất đối xứng nhịp với các cú rút reserves theo sự kiện của
  TGA.
source_refs:
- file: Reflections on the Early Days of Reserve Management Purchases.md
created: '2026-06-27'
updated: '2026-07-02'
---

# [[Reserve_Management_Purchases_RMP]]

## Thesis

Sau khi QT2 kết thúc ngày 01/12/2025 (cắt >$2.2T securities trong ~3.5 năm), Fed chuyển sang chế độ **duy trì** bảng cân đối thay vì thu hẹp. RMP là công cụ chính của giai đoạn này: Fed mua ròng UST với khối lượng **đủ khớp tăng trưởng theo trend của cầu dự trữ** (chủ yếu do currency in circulation và các autonomous factors tăng theo GDP danh nghĩa). Mục tiêu là giữ reserves trên ngưỡng "Lowest Ample" (~9% GDP ≈ $3,000B) — **không** phải nới lỏng chính sách.

Điểm phân biệt cốt lõi với QE: **intent**. QE = mua quy mô lớn để hạ term premium và nới lỏng (stimulus). RMP = mua kỹ thuật để bù hao hụt reserves cơ học, giữ tổng asset gần phẳng. Xem [[QE_Liquidity_Distortion]] để đối chiếu.

---

## 1. Operational Mechanism (Cơ chế vận hành)

- **Công cụ:** Mua outright UST trên thị trường thứ cấp (bills + coupons), thực hiện bởi NY Fed Desk.
- **Quy mô:** Khớp trend reserve demand — không phải mục tiêu cố định, điều chỉnh theo dự báo autonomous factors.
- **Tương tác với MBS runoff:** Fed vẫn để MBS chạy off (không tái đầu tư vào MBS), dùng proceeds + RMP để mua UST → cơ cấu asset dịch chuyển **UST↑ / MBS↓** trong khi **tổng asset giữ phẳng**. Tại H.4.1 24/06/2026: UST $4,487.9B / MBS $1,963.4B trên tổng securities $6,452.0B.
- **Phân biệt với SRF:** [[Standing_Repo_Facility_SRF_Mechanics]] là van trần cứng phản ứng theo **spike** (intraday/overnight); RMP là bơm cấu trúc theo **trend**. SRF xử lý cú sốc tức thời, RMP xử lý hao hụt dần.

---

## 2. T-Account Transmission

(Ví dụ: Fed thực hiện RMP $50B mua UST từ dealer)

```text
        FEDERAL RESERVE                          PRIMARY DEALER
  Assets          │   Liabilities         Assets            │   Liabilities
──────────────────┼─────────────────   ────────────────────┼──────────────
UST    [+$50B]    │ Reserves [+$50B]    UST      [-$50B]    │ (không đổi)
                  │                     Reserves [+$50B]    │
```

=> Fed tạo reserves mới (liability) để mua UST (asset). Reserves hệ thống tăng $50B. Đây là chiều **ngược** với cú nạp TGA của Treasury (xem [[Treasury_General_Account_Mechanism]]).

---

## 3. Regime Context — Defending Regime A

Theo [[Central_Bank_Balance_Sheet_Trilemma]] (Armenter), RMP là công cụ giữ Fed ở **Regime A (Ample Reserves)**: bảo vệ cạnh "Low Volatility + Limited Intervention" của tam giác. Nếu không có RMP, reserves sẽ bị bào mòn bởi autonomous factors (currency↑, TGA rebuild) và tụt về Regime B (Scarcity → high vol), buộc Fed phải quay lại OMO can thiệp hàng ngày (Regime C).

---

## 4. Asymmetry — Trend vs. Event (Treasury Insight)

**Bất đối xứng nhịp là đặc tính quan trọng nhất:**

- **Fed (RMP)** bơm theo **trend**: trơn, có lịch, độ trễ giữa các kỳ.
- **Treasury (TGA rebuild)** rút theo **sự kiện**: đột ngột, gắn lịch phát hành/tax date, biên độ lớn.

Khe hở giữa hai nhịp này — đặc biệt khi **ON RRP đã cạn (~$2.3B tại 24/06/2026)** không còn làm đệm — là nơi reserves dao động mạnh và **SOFR–IORB spread** nới rộng từng đợt. RMP không phản ứng kịp spike; van xử lý spike là SRF.

**So what cho Treasury desk:** RMP là backstop cấu trúc nhưng **không** che được cú sốc TGA ngày-cụ-thể. Desk vẫn phải map lịch phát hành Treasury vào dự báo funding cost, và theo dõi SOFR–IORB như gauge stress chính (không phải EFFR).

**Xác nhận thực nghiệm (H.4.1 weekly, 23 điểm Jan–Jun 2026):** Đáy reserves của cả H1 2026 (22/04/2026, $2,901.8B) trùng khớp chính xác với đỉnh TGA của cả H1 (22/04/2026, $1,007.2B) [RAW-OFFICIAL: Fed_H41_Weekly_Flow_H1_2026.md]. Hai tuần 08/04→22/04 (mùa quyết toán thuế cá nhân 15/04) tạo thí nghiệm tự nhiên khép kín: TGA +$310.1B, reserves −$214.4B, identity check trực tiếp cho residual "other factors" chỉ +$62.9B trên biến động dự đoán −$277.3B — TGA giải thích phần lớn cú giảm reserves. RMP đã bơm UST +$252.6B qua ~24 tuần (~$42B/tháng), khớp sát ước tính $40B/tháng trước đây — nay xác nhận RAW-OFFICIAL thay vì [LLM-E]. Nhưng tốc độ trend này không đủ làm phẳng biến động tuần: reserves dao động trong biên $227.8B (rộng hơn ước tính ban đầu) dù tổng assets tăng đều — xác nhận luận điểm "RMP chỉ neo trung bình nhiều tháng, TGA event (đặc biệt sự kiện tài khóa theo lịch như mùa thuế) chi phối phương sai tần suất cao."

---

## 5. Ranh giới rủi ro (Boundary)

- **Lag risk:** Nếu nhịp phát hành Treasury (vay ~$683B trong 2 quý 1–6/2026) vượt nhịp RMP, reserves có thể thủng floor giữa hai kỳ bơm → SOFR spike trước khi Fed bù.
- **Calibration risk:** RMP định cỡ theo *dự báo* trend reserve demand. Nếu việc chuyển sang **central clearing** repo làm tăng cấu trúc nhu cầu HQLA/reserves (margin tại CCP), ước lượng "ample floor" cũ ($3,000B) có thể bị dịch lên — RMP undersized. Xem [[Treasury_Central_Clearing_Repo_Netting]]. *(Lưu ý: mốc "deadline 30/06/2026" nêu trước đây chưa có raw source xác nhận — cần ingest văn bản SEC clearing rule.)*
- **Signaling risk:** RMP dễ bị thị trường hiểu nhầm là "QE quay lại". Fed phải truyền thông rõ intent (kỹ thuật, không stimulus) để tránh nới lỏng financial conditions ngoài ý muốn.

---

## Related

- [[Treasury_General_Account_Mechanism]] — lực rút reserves đối nghịch (theo sự kiện)
- [[Central_Bank_Balance_Sheet_Trilemma]] — RMP giữ Fed ở Regime A
- [[Standing_Repo_Facility_SRF_Mechanics]] — van trần cứng xử lý spike (bổ trợ RMP)
- [[QE_Liquidity_Distortion]] — đối chiếu intent (stimulus vs. operational)
- [[Autonomous_Factors_In_Central_Bank_Balance_Sheet]] — nguồn hao hụt reserves mà RMP bù
