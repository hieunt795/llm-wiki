---
title: Modified Duration
aliases: []
type: concept
tags: []
status: draft
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: legacy_migrated
thesis: Modified Duration (Thời lượng sửa đổi) là thước đo độ nhạy của giá trái phiếu
  khi lợi suất thay đổi. [RAW] Neftci làm rõ ranh giới giữa thay đổi tương đối (%)
  và thay đổi tuyệt đối (Dollar) thông qua DV01 và PV01.
source_refs:
  - file: Principles_of_Financial_Engineering_Neftci.md
    page: 85
  - file: Tuckman_Serrat_2022.md
    page: 112
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1949-1966
created: '2026-04-21'
updated: '2026-04-21'
---

﻿---
title: "Modified Duration"
aliases: [Mod Duration, D*, Độ nhạy lãi suất, Effective Duration, DV01, PV01]
type: definition
tags: [fixed-income, risk-measures]
status: active
confidence: 5
expert_lens: "Tuckman & Serrat | Salih Neftci"
provenance: "Principles_of_Financial_Engineering_Neftci.md"
thesis: "Modified Duration measures the percentage price change of a bond for a 1% (100bps) change in yield, serving as the first-order approximation of interest rate risk."
source_refs:
  - file: "Principles_of_Financial_Engineering_Neftci.md"
    page: 85
  - file: "Tuckman_Serrat_2022.md"
    page: 112
created: 2026-04-13
updated: 2026-04-21
---

## Thesis
Modified Duration (Thời lượng sửa đổi) là thước đo độ nhạy của giá trái phiếu khi lợi suất thay đổi. [RAW] Neftci làm rõ ranh giới giữa thay đổi tương đối (%) và thay đổi tuyệt đối (Dollar) thông qua DV01 và PV01.

## 1. Mathematical Definition
$$D = -\frac{1}{P} \frac{dP}{dy} = \frac{D_{mac}}{1 + y/k}$$
Trong đó $k$ là số lần ghép lãi trong năm.

### DV01 vs. PV01 (The Practitioner's Tools)
[RAW] Neftci cung cấp hai thước đo thực tế cho Traders:
1.  **DV01 (Dollar Value of an '01):** Thay đổi giá trị tuyệt đối (Dollar change) của trái phiếu khi lợi suất thay đổi 1 điểm cơ bản (0.01%).
    $$\text{DV01} \approx D \times P \times 0.0001$$
2.  **PV01 (Present Value of an '01):** Thường được dùng trong thị trường Swaps/Money Market để chỉ giá trị hiện tại của một dòng tiền khi lãi suất thay đổi 1bp. Về mặt toán học, PV01 và DV01 thường được dùng thay thế cho nhau nhưng PV01 nhấn mạnh vào khía cạnh "Present Value" của một bundle dòng tiền.

## 2. Risk Management: From Duration to VaR
[RAW] Neftci kết nối Duration trực tiếp với các mô hình rủi ro hiện đại:
- **Value-at-Risk (VaR):** Sử dụng Duration để ước tính khoản lỗ tối đa.
  $$\text{VaR} = \text{Price} \times \text{Duration} \times \Delta y_{max}$$
  Trong đó $\Delta y_{max}$ là mức biến động lãi suất tối đa ở một mức tin cậy nhất định (e.g., 99%).
- **Expected Shortfall (ES):** [RAW] Basel III yêu cầu chuyển dịch từ VaR sang ES để nắm bắt rủi ro ở "phần đuôi" (tail risk) mà Duration đơn thuần có thể bỏ sót do tính phi tuyến (Convexity).

## 3. Worked Example: JNJ Portfolio (Tuckman)
Sử dụng các trái phiếu Johnson & Johnson (JNJ) để minh họa độ phân giải rủi ro (Data as of May 2021):
- **JNJ 1.30s of 2030:** Duration thấp (~9 năm).
- **JNJ 2.45s of 2060:** Duration cao (~24 năm).
Trong quản trị quỹ hưu trí, Duration giúp khớp nối (matching) độ nhạy của tài sản với nghĩa vụ nợ (liabilities), đảm bảo tỷ suất sinh lời bù đắp được sự gia tăng giá trị hiện tại của các khoản chi trả hưu trí khi lãi suất giảm. [[Tuckman_Serrat_2022.md#page=142-145]]

## 4. Failure Conditions / Boundaries
- **Large Rate Shifts:** Duration chỉ là xấp xỉ bậc 1 (tuyến tính). Khi lãi suất thay đổi lớn, sai số sẽ tăng lên do đường cong lồi của trái phiếu. Phải bổ sung [[Convexity]].
- **Non-Parallel Shifts:** Giả định toàn bộ đường cong lãi suất dịch chuyển song song. Nếu đường cong bị xoắn (twist) hoặc dốc hơn (steepen), Duration đơn thuần có thể dẫn đến sai lệch lớn.

## Related
- [[Macaulay_Duration]] — Nền tảng thời gian của Duration.
- [[Convexity]] — Thước đo sai số bậc hai.
- [[Value_At_Risk_VaR]] — Ứng dụng trong quản trị rủi ro hệ thống.
- [[Immunization]] — Chiến lược hedging dựa trên độ nhạy bậc 1.
