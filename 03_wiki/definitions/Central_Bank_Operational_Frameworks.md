---
title: Central Bank Operational Frameworks
aliases:
- Monetary Policy Implementation
- Operational Framework Criteria
- Central Bank Operating Procedures
- Liquidity Management
- Khung hoạt động chính sách tiền tệ
type: definition
tags:
- central-banking
- operations
- liquidity
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: A central bank's operational framework is the practical interface between
  policy goals and financial markets, comprising the instruments and procedures used
  to manage systemic liquidity while adhering to core design principles of parsimony
  and stability.
source_refs:
- file: During_Fixed_Income_Ch08.md
  page: 50
- file: Perry_Central_Bank_Policy_P4.md
  page: 195
- file: Perry_Central_Bank_Policy_P4.md
  page: 196
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The operational framework represents the "hands" of the central bank. Alexander Düring bóc tách ranh giới của thiết kế kỹ thuật (làm sao để công cụ không gây nhiễu thị trường), trong khi Perry Warjiyo giải mã cơ chế thực thi (làm sao để dẫn truyền lãi suất chính sách đến nền kinh tế thực). Một khung hoạt động tối ưu phải vừa đảm bảo tính kỷ luật kỹ thuật, vừa đủ linh hoạt để đối phó với các cú shock thanh khoản. [[During_Fixed_Income_Ch08.md#page=50]] [[Perry_Central_Bank_Policy_P4.md#page=195]]

---

## 1. Design Principles (The During Criteria)

Alexander Düring identifies four essential characteristics that prevent the operational framework from becoming a source of market distortion:

1.  **Parsimony (Sự tinh gọn):** Sử dụng tối thiểu các công cụ. Quá nhiều công cụ sẽ làm thị trường bối rối về mục tiêu thực sự của NHTW.
2.  **Stability (Tính ổn định):** Công cụ phải có tính **hysteresis** (duy trì liên tục). Sự thay đổi thường xuyên gây ra tác dụng phụ lớn hơn lợi ích kỹ thuật nhỏ nhoi thu được.
3.  **Moderation (Sự điều độ):** NHTW chỉ can thiệp tối thiểu. Khuyến khích các ngân hàng "test their name" (giao dịch tự thân) trên thị trường tư nhân thay vì coi NHTW là đối tác mặc định.
4.  **Separation (Sự tách bạch):** Phải tách biệt rõ ràng giữa bơm thanh khoản thông thường và cho vay khẩn cấp (LOLR) để tránh gửi tín hiệu sai lệch về stance của chính sách tiền tệ. [[During_Fixed_Income_Ch07.md#page=46]]

---

## 2. The Operational Hierarchy (Warjiyo Roadmap)

Perry Warjiyo bóc tách cấu trúc dẫn truyền từ công cụ đến mục tiêu cuối cùng thông qua một chuỗi các mỏ neo:

### A. The Transmission Chain
1.  **Instruments:** OMO, Standing Facilities, Reserve Requirements.
2.  **Operational Target:** Short-term interest rates (e.g., PUAB, BI Rate) or Monetary Base (M0).
3.  **Intermediate Target:** Broad money (M2) or Credit volume.
4.  **Final Target:** Price Stability and Sustainable Growth. [[Perry_Central_Bank_Policy_P4.md#page=196]]

### B. Selecting the Target (Poole Model)
The choice between targeting **Quantity (M)** or **Price (i)** depends on the source of shocks:
- **LM Shocks (Unstable money demand):** Target **Interest Rate**.
- **IS Shocks (Unstable aggregate demand):** Target **Money Supply**. [[Perry_Central_Bank_Policy_P4.md#page=197]]

---

## 3. Implementation Pillars: The Corridor

Used to bound volatility in the interbank market:
- **Ceiling:** Lending Facility (NHTW cho vay khẩn cấp).
- **Floor:** Deposit Facility (NHTW nhận tiền gửi dư thừa).
- **The Target:** OMO keeps the market rate ($PUAB$) close to the policy rate positioned within this corridor. [[Perry_Central_Bank_Policy_P4.md#page=205]]

---

## Strategic Implications: Operational Independence

Perry Warjiyo nhấn mạnh rằng tại các EME, thành công của khung hoạt động phụ thuộc vào **Độ sâu thị trường (Market Depth)**. Việc áp dụng **GWM Averaging** là một ví dụ về sự kết hợp giữa tính "Stability" của Düring và nhu cầu thanh khoản thực tế, cho phép dự trữ dao động trong kỳ để giảm sốc lãi suất. [[Perry_Central_Bank_Policy_P4.md#page=210]]

## Evidence / Source Anchors

- Hierarchy of central bank actions (Standard vs. LOLR): [[During_Fixed_Income_Ch08.md#page=50]]
- The four desiderata for operational design: [[During_Fixed_Income_Ch07.md#page=46]]
- Hierarchy of instruments and targets (Figure 7.1): [[Perry_Central_Bank_Policy_P4.md#page=196]]
- Mathematical derivation of the Poole model for target selection: [[Perry_Central_Bank_Policy_P4.md#page=197]]

## Related

- [[Operational_Targeting_Price_Vs_Quantity]] — Comparison of M vs i.
- [[Interest_Rate_Corridor_Mechanism]] — Technical view of the Ceiling/Floor.
- [[Reserve_Requirement_GWM_Evolution]] — The tool used to manage the quantity of reserves.
- [[Open_Market_Operations_OMO]] — The primary implementation tool.
