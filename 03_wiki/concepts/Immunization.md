---
title: Immunization
aliases:
- Portfolio Immunization
- Duration Matching
- Interest Rate Immunization
type: concept
tags:
- fixed-income
- interest-rate-risk
- hedging
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Immunization is an ad hoc synthetic strategy used to protect a fixed-income
  portfolio from interest rate risk by matching its first-order sensitivities (duration)
  with those of a funding or replicating portfolio.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 246
created: '2026-05-22'
updated: '2026-04-22'
---

## Thesis
[RAW] Immunization là một chiến lược "Ad Hoc" nhằm vô hiệu hóa tác động của biến động lãi suất đối với giá trị danh mục bằng cách cân bằng các độ nhạy bậc một (Duration). Tuy nhiên, đây chỉ là giải pháp xấp xỉ vì nó bỏ qua các yếu tố phi tuyến (Convexity) và không có tính chất tự cấp vốn (Self-financing).

## 1. Core Mechanism: Sensitivity Matching
[RAW] Cơ chế cốt lõi của Immunization là thiết lập một danh mục (synthetic) sao cho phản ứng của nó đối với sự thay đổi nhỏ của lãi suất ($dy$) khớp với phản ứng của tài sản mục tiêu.

### Mathematical Formulation
Giả sử ta có tài sản mục tiêu $S_1$ và hai tài sản thanh khoản $S_2, S_3$ dùng để thiết lập danh mục mô phỏng. Ta cần tìm tỷ trọng $\{\theta_2, \theta_3\}$ sao cho:

1.  **Value Matching:** Giá trị danh mục bằng giá trị tài sản mục tiêu.
    $$S_1 = \theta_2 S_2 + \theta_3 S_3$$
2.  **Sensitivity Matching:** Đạo hàm bậc nhất theo nhân tố rủi ro $x$ (thường là yield $y$) phải khớp nhau.
    $$\frac{\partial S_1}{\partial x} = \theta_2 \frac{\partial S_2}{\partial x} + \theta_3 \frac{\partial S_3}{\partial x}$$

### In Fixed Income Context (Duration)
[RAW] Trong thị trường trái phiếu, đạo hàm bậc nhất này chính là **Duration**. Chiến lược immunization phổ biến nhất là khớp duration của tài sản (Assets) và nợ phải trả (Liabilities) để bảo vệ vốn chủ sở hữu trước rủi ro lãi suất.

## 2. Static vs. Dynamic Protection
[RAW] Neftci phân biệt rõ ranh giới của Immunization trong chuỗi tiến hóa của kỹ thuật tài chính:

-   **Static Setting:** Immunization được thiết lập tại $t_0$ dựa trên các partial derivatives tại thời điểm đó.
-   **Ad Hoc Dynamic Adjustment:** Khi thời gian trôi qua và $y$ thay đổi, các partial derivatives cũng thay đổi. Để duy trì trạng thái "immunized", kỹ sư phải tính toán lại $\{\theta_i\}$ và tái cân bằng danh mục.
-   **The Cash Flow Gap:** Khác với dynamic replication hoàn hảo (Self-financing), việc tái cân bằng trong immunization thường yêu cầu **bơm thêm tiền hoặc rút tiền mặt** (cash injections/withdrawals), làm cho nó trở thành một giải pháp "Ad Hoc".

## 3. Worked Example (Neftci Case)
[RAW] **Target:** Trái phiếu 2 năm $B(t_0, T_2)$.
**Constituents:** Trái phiếu 3 năm $B(t_0, T_3)$ và trái phiếu 6 tháng $B(t_0, T_{0.5})$.
**Yield curve:** Phẳng tại 8%, giả định parallel shifts.

**Equations:**
1.  $B(t_0, T_2) = \theta_1 B(t_0, T_3) + \theta_2 B(t_0, T_{0.5})$
2.  $\frac{\partial B(t_0, T_2)}{\partial y} = \theta_1 \frac{\partial B(t_0, T_3)}{\partial y} + \theta_2 \frac{\partial B(t_0, T_{0.5})}{\partial y}$

**Result:** Để mô phỏng trái phiếu 2 năm, cần short 0.65 đơn vị trái phiếu 3 năm và short 0.36 đơn vị trái phiếu 6 tháng (tạo nguồn vốn tài trợ cho việc nắm giữ trái phiếu 2 năm một cách miễn nhiễm với biến động lãi suất bậc 1).

## 4. Failure Conditions & Limitations
-   **Convexity Mismatch:** [RAW] Chỉ khớp đạo hàm bậc nhất. Nếu lãi suất biến động lớn ($dy$ lớn), sai số do đạo hàm bậc hai (Convexity) sẽ làm lệch mục tiêu bảo vệ.
-   **Parallel Shift Assumption:** [RAW] Chiến lược giả định toàn bộ đường cong lợi suất dịch chuyển song song. Trong thực tế, các kỳ hạn khác nhau biến động với biên độ khác nhau, phá vỡ sự tương đương của các độ nhạy.
-   **Rebalancing Costs:** Chi phí giao dịch phát sinh khi phải liên tục điều chỉnh tỷ trọng để duy trì duration matching.
-   **Non-Self-Financing:** Không thể tự duy trì nếu không có sự can thiệp dòng tiền từ bên ngoài.

## Related
- [[Macaulay_Duration]] — Công cụ đo lường độ nhạy bậc 1.
- [[Convexity]] — Nguồn gốc của sai số trong immunization.
- [[Synthetics_Replicating_Portfolios]] — Khung lý thuyết tổng quát.
- [[Dynamic_Replication_Methods]] — Phiên bản hoàn thiện hơn của immunization.
