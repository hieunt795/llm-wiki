---
title: Liquidity Management Operations
aliases:
- Liquidity Management
- Central Bank Liquidity Forecasting
- Sterilization
- Market vs Funding Liquidity
- Quản trị thanh khoản hệ thống
type: mechanism
tags:
- central-banking
- operations
- liquidity
- money-market
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: Liquidity management is the central bank's process of forecasting and adjusting
  the level of reserves in the banking system to ensure that short-term interest rates
  remain aligned with policy targets while preventing systemic financial instability.
source_refs:
- file: During_Fixed_Income_Ch07.md
  page: 46
- file: During_Fixed_Income_Ch10.md
  page: 58
- file: Perry_Central_Bank_Policy_P4.md
  page: 196
- file: Perry_Central_Bank_Policy_P6.md
  page: 408
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Quản trị thanh khoản là "nghệ thuật cân bằng" của NHTW. Alexander Düring bóc tách ranh giới giữa hai loại hình thanh khoản (Thị trường vs. Nguồn vốn), trong khi Perry Warjiyo giải mã cơ chế dự báo và trung hòa (Sterilization) các cú shock ngoại lai. Nếu NHTW dự báo sai, lãi suất thị trường sẽ biến động hỗn loạn, làm gãy vỡ kênh truyền dẫn chính sách tiền tệ ngay từ điểm khởi đầu. [[During_Fixed_Income_Ch07.md#page=46]] [[Perry_Central_Bank_Policy_P4.md#page=196]]

---

## 1. The Two Faces of Liquidity (Düring's Lens)

Düring vạch rõ ranh giới mà NHTW phải giám sát:

### A. Market Liquidity (Asset side)
- **Definition:** Khả năng bán một tài sản nhanh chóng với số lượng lớn mà không làm thay đổi đáng kể giá của nó.
- **Risk:** Khi thị trường bị stress, thanh khoản này biến mất, dẫn đến hiện tượng **Bán tháo (Fire Sales)**.

### B. Funding Liquidity (Liability side)
- **Definition:** Khả năng của một ngân hàng trong việc vay tiền mặt ngay lập tức để đáp ứng các nghĩa vụ đến hạn (thường qua Repo hoặc Interbank).
- **The Feedback Loop:** Khi thanh khoản thị trường giảm, giá tài sản đảm bảo giảm, khiến ngân hàng bị Margin call, làm thanh khoản nguồn vốn bị đóng băng. Đây là tâm điểm của các cuộc khủng hoảng tài chính. [[During_Fixed_Income_Ch10.md#page=58]]

---

## 2. The Operational Cycle (Warjiyo's Lens)

NHTW điều hành thanh khoản qua một quy trình khép kín:

### Phase 1: Liquidity Forecasting
NHTW dự báo các **Yếu tố tự thân (Autonomous Factors)** nằm ngoài tầm kiểm soát:
- Luồng tiền mặt lưu thông (Currency in circulation).
- Chi tiêu và thu thuế của Chính phủ (Treasury flows).
- Biến động dự trữ ngoại hối (FX flows).

### Phase 2: Implementation (OMO & Facilities)
Dựa trên dự báo, NHTW sử dụng:
- **OMO:** Để bơm/hút thanh khoản chủ động nhằm đạt mỏ neo lãi suất (BI Rate).
- **Standing Facilities:** Để ghim lãi suất trong [[Interest_Rate_Corridor_And_Standing_Facilities|Hành lang]]. [[Perry_Central_Bank_Policy_P4.md#page=196]]

---

## 3. Advanced EME Strategies: Sterilization & Dual Intervention

Perry Warjiyo bóc tách các kỹ thuật đặc thù cho các nền kinh tế mở (như Indonesia):

### A. Sterilization (Trung hòa)
Khi NHTW mua USD để ngăn đồng tiền tăng giá, họ vô tình bơm một lượng nội tệ khổng lồ ra hệ thống.
- **The Move:** BI phải ngay lập tức hút số tiền này lại bằng cách bán chứng chỉ SBI hoặc Repo ngược.
- **The Cost:** Chi phí trả lãi cho SBI là gánh nặng tài chính lớn đối với NHTW (Monetary control cost). [[Perry_Central_Bank_Policy_P6.md#page=408]]

### B. Dual Intervention
Một "vi chất" của Perry — Trong các đợt rút vốn ngoại mạnh (Capital Reversal):
1.  **FX Market:** Bán USD để ổn định tỷ giá (hành động này hút tiền Rupiah về).
2.  **Bond Market:** Mua lại trái phiếu Chính phủ (SBN) để bơm tiền Rupiah ra.
- **Goal:** Ngăn chặn sự sụp đổ kép của cả tỷ giá và thanh khoản hệ thống ngân hàng nội địa. [[Perry_Central_Bank_Policy_P6.md#page=514]]

---

## Evidence / Source Anchors

- Analysis of the interplay between market and funding liquidity: [[During_Fixed_Income_Ch10.md#page=58]]
- Description of the autonomous factors in liquidity forecasting: [[Perry_Central_Bank_Policy_P4.md#page=196]]
- Logic of "Dual Intervention" to protect systemic liquidity: [[Perry_Central_Bank_Policy_P6.md#page=514]]
- Rationale for sterilization to mitigate inflationary pressure from FX inflows: [[Perry_Central_Bank_Policy_P6.md#page=408]]

## Related

- [[Open_Market_Operations_And_Instruments]] — The tools of liquidity management.
- [[Interest_Rate_Corridor_And_Standing_Facilities]] — The safety net of liquidity.
- [[FX_Sterilization_Mechanism]] — The specific case of FX-driven liquidity flows.
- [[Fire_Sale_Mechanism]] — The consequence of liquidity management failure.
