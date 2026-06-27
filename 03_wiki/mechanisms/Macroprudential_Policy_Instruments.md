---
title: Macroprudential Policy Instruments
aliases:
- Macroprudential Tools
- LTV Ratio
- CCyB
- GWM-LDR
- Haircuts and Margins
- Công cụ chính sách an toàn vĩ mô
type: mechanism
tags:
- central-banking
- macroprudential
- banking-regulation
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (Warjiyo, During & Basel)
thesis: Macroprudential instruments are surgical tools designed to mitigate systemic
  risk by regulating the price and quantity of credit, categorized into capital-based
  (CCyB), liquidity-based (GWM-LDR), and asset-based (LTV) constraints.
source_refs:
- file: Perry_Central_Bank_Policy_P6.md
  page: 432
- file: During_Fixed_Income_Ch24.md
  page: 260
- file: Perry_Central_Bank_Policy_P6.md
  page: 454
- file: During_Fixed_Income_Ch28.md
  page: 345
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Lãi suất là một công cụ "vô cảm" (blunt instrument)—nó tác động lên toàn bộ nền kinh tế. Alexander Düring bóc tách ranh giới của các ràng buộc vi mô (Cơ chế LTV và rủi ro định giá), trong khi Perry Warjiyo giải mã cơ chế can thiệp có mục tiêu (**Macroprudential**). Công cụ này cho phép NHTW hạ nhiệt một bong bóng bất động sản cụ thể (thông qua LTV) mà không làm tổn thương các doanh nghiệp sản xuất đang cần lãi suất thấp. [[Perry_Central_Bank_Policy_P6.md#page=432]] [[During_Fixed_Income_Ch28.md#page=345]]

---

## 1. Technical Taxonomy (The Triple Pillars)

Perry Warjiyo bóc tách bộ công cụ thành 3 nhóm tác động chính:

| Pillar | Instruments | Goal |
| :--- | :--- | :--- |
| **Credit-based** | **LTV (Loan-to-Value)**, **DTI (Debt-to-Income)** | Kiểm soát ranh giới đòn bẩy của người đi vay. Ngăn chặn bong bóng tài sản. |
| **Liquidity-based** | **GWM-LDR**, **LCR (Liquidity Coverage Ratio)** | Đảm bảo ngân hàng có đủ "oxy" thanh khoản và không cho vay quá đà trên nền tảng vốn ngắn hạn. |
| **Capital-based** | **CCyB (Countercyclical Capital Buffer)**, **CAR surcharges** | Xây dựng bộ đệm vốn trong thời kỳ boom để xả ra trong thời kỳ bust. |

[[Perry_Central_Bank_Policy_P6.md#page=454]]

---

## 2. Micro-Mechanics of Collateral (Düring's Lens)

Düring giải mã ranh giới "cơ học" của LTV và Haircut:
- **Mechanical Deleveraging:** LTV không phải là hằng số. Khi giá tài sản ($q$) giảm, LTV ($Loan / qW$) tự động tăng lên. Nếu vượt ngưỡng quy định, ngân hàng buộc phải thực hiện **Margin Call**.
- **Haircut Strategy:** NHTW áp dụng "chiết khấu" lên giá trị tài sản đảm bảo trước khi cho vay. Một haircut 20% nghĩa là LTV tối đa chỉ là 80%. Đây là mỏ neo bảo vệ bảng cân đối của NHTW khỏi biến động giá tài sản (Price risk). [[During_Fixed_Income_Ch24.md#page=260]]

---

## 3. EME Customization: The Indonesia Case

Bank Indonesia bổ sung các mỏ neo đặc thù:
- **Targeted LTV:** Chỉ áp cho bất động sản/ô tô thứ hai trở đi để giảm đầu cơ mà không ngăn cản người mua nhà lần đầu.
- **GWM-LFR (Reserve Requirement based on Funding):** Tỷ lệ dự trữ bắt buộc thay đổi dựa trên mức độ huy động vốn và cho vay. Nếu ngân hàng cho vay quá ít (<78%) hoặc quá nhiều (>92%), họ phải gửi thêm dự trữ không hưởng lãi tại BI. [[Perry_Central_Bank_Policy_P6.md#page=211]]

---

## 4. Strategic Implications: The Leakage Risk

Perry Warjiyo cảnh báo về ranh giới hiệu lực:
- **Shadow Banking:** Khi thắt chặt LTV tại các ngân hàng thương mại, dòng vốn có thể chuyển dịch sang các công ty tài chính phi ngân hàng hoặc **Private Credit**.
- **Regulatory Arbitrage:** Các định chế tài chính tìm cách lách luật thông qua các sản phẩm phái sinh hoặc định giá lại tài sản ảo.
- **Inference:** Macroprudential chỉ thực sự hiệu quả khi có sự giám sát tích hợp toàn bộ hệ sinh thái tài chính. [[Perry_Central_Bank_Policy_P6.md#page=456]]

---

## Evidence / Source Anchors

- Classification of 10 Asian macroprudential tools: [[Perry_Central_Bank_Policy_P6.md#page=456]]
- Analysis of LTV as a mechanical failure trigger in real estate lending: [[During_Fixed_Income_Ch28.md#page=345]]
- Rationale for CCyB as a time-series dimension risk mitigator: [[Perry_Central_Bank_Policy_P6.md#page=435]]
- Definition of the GWM-LFR corridor (78-92%) in Indonesia: [[Perry_Central_Bank_Policy_P6.md#page=211]]

## Related

- [[Central_Bank_Policy_Mix_Paradigm]] — Coordination with interest rates.
- [[Financial_Procyclicality_Mechanism]] — The risk these tools aim to dampen.
- [[Systemic_Risk_Taxonomy]] — The theoretical housing for these tools.
- [[Lender_Of_Last_Resort_Mechanism]] — Macroprudential seeks to prevent the need for LoLR.
