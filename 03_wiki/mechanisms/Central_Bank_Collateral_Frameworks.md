---
title: Central Bank Collateral Frameworks
aliases:
- Eligible Collateral
- Central Bank Haircuts
- Collateral Widening
- Asset Eligibility
- Khung tài sản đảm bảo của NHTW
type: mechanism
tags:
- central-banking
- liquidity
- fixed-income
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: The collateral framework is the set of rules defining which assets a central
  bank accepts in exchange for liquidity, serving as both a primary risk-management
  shield and a powerful tool for influencing market pricing and credit allocation.
source_refs:
- file: During_Fixed_Income_Ch08.md
  page: 55
- file: Perry_Central_Bank_Policy_P4.md
  page: 209
- file: During_Fixed_Income_Ch10.md
  page: 58
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Ai là người quyết định tài sản nào có giá trị "như tiền"? Alexander Düring bóc tách ranh giới của sự méo mó thị trường (Việc chấp nhận một tài sản làm đảm bảo tại NHTW sẽ trực tiếp làm tăng giá của nó), trong khi Perry Warjiyo giải mã cơ chế sử dụng rổ tài sản để hỗ trợ các phân khúc tín dụng ưu tiên. Khung tài sản đảm bảo không chỉ là chốt chặn rủi ro cho bảng cân đối của NHTW, mà còn là "chiếc đũa thần" có thể thay đổi toàn bộ cấu trúc thanh khoản của một loại trái phiếu. [[During_Fixed_Income_Ch08.md#page=55]] [[Perry_Central_Bank_Policy_P4.md#page=209]]

---

## 1. The Risk Management Function: Haircuts

Để tự bảo vệ mình, NHTW không bao giờ cho vay 100% giá trị tài sản đảm bảo.
- **Haircut (Chiết khấu):** Tỷ lệ phần trăm bị trừ đi từ giá trị thị trường của tài sản.
- **Mechanism:** Một trái phiếu trị giá $100 với haircut 10% chỉ cho phép ngân hàng vay $90.
- **The Anchor:** Düring bóc tách ranh giới kỹ thuật: Haircut phụ thuộc vào biến động giá (volatility), kỳ hạn (maturity) và xếp hạng tín nhiệm của tài sản. Trong thời kỳ stress, NHTW có thể tăng haircut để bảo vệ bảng cân đối, nhưng hành động này có thể gây ra hiện tượng **Deleveraging** cưỡng ép cho hệ thống. [[During_Fixed_Income_Ch08.md#page=55]]

---

## 2. Market Impact: The Eligibility Premium

Việc một tài sản trở thành **Eligible Collateral** (đủ điều kiện làm đảm bảo) tạo ra một hiệu ứng định giá:
- **Price Boost:** Tài sản đủ điều kiện sẽ có lợi suất thấp hơn (giá cao hơn) so với các tài sản tương đương nhưng không đủ điều kiện, do nó sở hữu tính năng "Thanh khoản NHTW".
- **Distortion:** Düring giải mã cơ chế "Chọn lựa rủi ro": Các ngân hàng có xu hướng giữ lại các tài sản tốt nhất trên bảng cân đối và mang các tài sản "kém thanh khoản nhất trong số các tài sản đủ điều kiện" đến nộp cho NHTW (Gresham's Law of Collateral). [[During_Fixed_Income_Ch10.md#page=58]]

---

## 3. EME Strategic Use: Targeted Eligibility

Perry Warjiyo bóc tách ranh giới thực thi tại Indonesia:
- **Collateral Widening:** Trong các cuộc khủng hoảng, BI có thể nới rộng rổ tài sản đảm bảo, chấp nhận các loại trái phiếu doanh nghiệp hoặc nợ công có xếp hạng thấp hơn để bơm thanh khoản cứu hệ thống.
- **Sectoral Support:** BI sử dụng việc chấp nhận các khoản vay SME hoặc trái phiếu xanh (Green bonds) làm tài sản đảm bảo để khuyến khích ngân hàng bơm vốn vào các lĩnh vực này. [[Perry_Central_Bank_Policy_P4.md#page=209]]

---

## 4. Strategic Implications: The Stigma and Availability

- **Stigma Risk:** Düring nhấn mạnh ranh giới hành vi — nếu NHTW yêu cầu tài sản đảm bảo quá khắt khe, nó sẽ làm trầm trọng thêm hoảng loạn vì thị trường coi đó là dấu hiệu của sự thiếu hụt thanh khoản trầm trọng.
- **Availability:** Tổng lượng tài sản đủ điều kiện trong hệ thống (Collateral pool) là giới hạn thực tế cho toàn bộ các nghiệp vụ OMO và Standing Facilities. [[During_Fixed_Income_Ch08.md#page=56]]

---

## Evidence / Source Anchors

- Analysis of haircuts as a risk-mitigation tool for the central bank: [[During_Fixed_Income_Ch08.md#page=55]]
- Description of the eligibility premium and its impact on market pricing: [[During_Fixed_Income_Ch10.md#page=58]]
- Rationale for collateral widening during periods of market stress in Indonesia: [[Perry_Central_Bank_Policy_P4.md#page=209]]
- Distinction between market volatility and collateral valuation adjustments: [[During_Fixed_Income_Ch08.md#page=55]]

## Related

- [[Lender_Of_Last_Resort_Mechanism]] — The safety net that relies on this framework.
- [[Open_Market_Operations_And_Instruments]] — The tools that execute these transactions.
- [[Repurchase_Agreement_Mechanism]] — The primary contract type for collateral exchange.
- [[Significant_Risk_Transfer]] — How collateral limits are optimized in banking.
