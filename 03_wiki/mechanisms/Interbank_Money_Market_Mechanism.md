---
title: Interbank Money Market Mechanism
aliases:
- Interbank Market
- PUAB
- Eurodollar Market
- Money Centers
- Thị trường liên ngân hàng
type: mechanism
tags:
- money-market
- banking
- central-banking
- infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: The interbank money market is the 'inner circle' of the financial system where
  banks trade liquidity to manage reserve requirements, serving as the primary battlefield
  for monetary policy transmission and a critical indicator of systemic risk.
source_refs:
- file: During_Fixed_Income_Ch23.md
  page: 200
- file: Perry_Central_Bank_Policy_P6.md
  page: 444
- file: Perry_Central_Bank_Policy_P6.md
  page: 449
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Thị trường liên ngân hàng là nơi thanh khoản của NHTW ngấm vào nền kinh tế. Alexander Düring bóc tách ranh giới của hạ tầng rủi ro (Sự chuyển dịch từ Unsecured sang Secured), trong khi Perry Warjiyo giải mã cơ chế mạng lưới và các điểm nghẽn truyền dẫn tại EME. Nếu thị trường này bị đóng băng (đặc biệt là mảng Eurodollar), toàn bộ hệ thống tài chính toàn cầu sẽ rơi vào trạng thái "thiếu oxy" thanh khoản. [[During_Fixed_Income_Ch23.md#page=200]] [[Perry_Central_Bank_Policy_P6.md#page=444]]

---

## 1. Structural Taxonomy (Düring's Lens)

### A. Unsecured Interbank (The Shrinking Core)
- **Mechanism:** Cho vay không đảm bảo dựa trên niềm tin giữa các ngân hàng. 
- **Indicator:** Lãi suất LIBOR/Euribor (cho mảng offshore) và Federal Funds Rate (cho nội địa Mỹ).
- **The Shift:** Hậu 2008, do **Rủi ro đối tác (Counterparty risk)** tăng vọt, mảng này đã bị thu hẹp đáng kể và thay thế bởi [[Repurchase_Agreement_Mechanism|Repo]].

### B. Eurodollar Market (Offshore Liquidity)
Düring bóc tách ranh giới của thị trường offshore:
- **Definition:** Các khoản tiền gửi bằng USD tại các ngân hàng nằm ngoài nước Mỹ.
- **Significance:** Đây là mỏ neo thanh khoản lớn nhất thế giới, cho phép USD luân chuyển toàn cầu mà không chịu sự điều tiết trực tiếp của Fed.
- **TED Spread:** Chênh lệch giữa Eurodollar (ngân hàng) và T-bills (chính phủ) là phong vũ biểu đo lường sức khỏe hệ thống. [[During_Fixed_Income_Ch23.md#page=200]]

---

## 2. EME Frictions: Market Segmentation (Warjiyo's Lens)

Perry Warjiyo bóc tách ranh giới thực tế tại các nền kinh tế mới nổi (như Indonesia):
- **Segmentation:** Thị trường bị chia cắt thành các nhóm (Clusters). Các ngân hàng lớn (Money Centers) thường dư thừa vốn nhưng từ chối cho các ngân hàng nhỏ vay do lo ngại rủi ro tín dụng.
- **Transmission Blockage:** Sự phân mảnh này khiến lãi suất chính sách của NHTW chỉ truyền dẫn đến các ngân hàng lớn, trong khi các ngân hàng nhỏ vẫn chịu chi phí vốn cao, làm giảm hiệu quả của ITF. [[Perry_Central_Bank_Policy_P6.md#page=449]]

### 2.1. Mechanism of Broken Transmission (Visual)

Trong các giai đoạn căng thẳng (Stress), thanh khoản bị kẹt lại tại các ngân hàng lớn ("Liquidity Trapped"):

**Flowchart: The Trust Gap**
```ascii
[CENTRAL BANK]
      │
      │ (1) Liquidity Injection (Repo/OMO)
      ▼
[MONEY CENTERS] (Big Banks)
      │
      │ ❌ (2) Counterparty Risk Spike (The Trust Gap)
      │      (Thanh khoản không chảy qua)
      ▼
 [SMALL BANKS] (Regional/Community Banks)
      │
      │ ❌ (3) Credit Crunch
      ▼
[REAL ECONOMY] (SMEs/Households)
```

**T-Shape: Balance Sheet of a Money Center (Hoarding Liquidity)**
```ascii
┌──────────────────────────────────────────────────────────┐
│             [MONEY CENTER BANK] (Risk Averse)            │
├──────────────────────────────┬───────────────────────────┤
│            ASSETS            │        LIABILITIES        │
├──────────────────────────────┼───────────────────────────┤
│ (1) + Excess Reserves at CB  │ (1) + CB Funding (Repo)   │
│ (2) - Interbank Loans (Cut)  │ (2) + Stable Deposits     │
│ (3) + High Quality Liquid Assets (HQLA)                  │
└──────────────────────────────┴───────────────────────────┘
(2) Trái ngược với kỳ vọng của NHTW, ngân hàng lớn cắt giảm cho vay liên ngân hàng
để bảo vệ bảng cân đối của mình, khiến thanh khoản bị tắc nghẽn.
```

---

## 3. Network Theory Analysis (Figure 14.6)

NHTW sử dụng lý thuyết mạng lưới để giám sát thị trường liên ngân hàng:
1.  **Centrality (Tính trung tâm):** Xác định các ngân hàng đóng vai trò "Money Centers" — nơi hầu hết các luồng lệnh đi qua.
2.  **Cohesion (Tính kết nối):** Thước đo mức độ gắn kết của hệ thống. Nếu cohesion thấp, hệ thống dễ bị tổn thương bởi các cú shock đơn lẻ.
3.  **Contagion (Lan tỏa):** Mô phỏng cách một ngân hàng vỡ nợ sẽ kéo theo các mắt xích khác thông qua các khoản vay liên ngân hàng chưa quyết toán. [[Perry_Central_Bank_Policy_P6.md#page=447]]

---

## Evidence / Source Anchors

- Analysis of the Eurodollar market as an offshore liquidity anchor: [[During_Fixed_Income_Ch23.md#page=200]]
- Description of interbank market segmentation and its impact on transmission: [[Perry_Central_Bank_Policy_P6.md#page=449]]
- Identification of Money Centers using centrality indicators (Figure 14.6): [[Perry_Central_Bank_Policy_P6.md#page=447]]
- Analysis of TED Spread as a systemic risk barometer: [[During_Fixed_Income_Ch23.md#page=204]]

## Related

- [[Interest_Rate_Corridor_And_Standing_Facilities]] — The bounds of the interbank rate.
- [[Repurchase_Agreement_Mechanism]] — The secured alternative to interbank lending.
- [[Counterparty_Credit_Risk]] — The driver of interbank market freezes.
- [[Real_Time_Gross_Settlement_RTGS]] — The plumbing for interbank settlement.
