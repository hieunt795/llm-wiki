---
title: Open Market Operations and Instruments
aliases:
- OMO
- Outright Operations
- Monetary Operations Instruments
- SBI vs SBN
- FASBI
- Nghiệp vụ thị trường mở
type: mechanism
tags:
- central-banking
- monetary-policy
- implementation
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: Open Market Operations (OMOs) are the primary indirect instruments used by
  central banks to manage systemic liquidity and signal policy rates through the purchase
  or sale of securities in the secondary market, characterized by their flexibility
  and market-oriented nature.
source_refs:
- file: During_Fixed_Income_Ch08.md
  page: 51
- file: During_Fixed_Income_Ch10.md
  page: 58
- file: Perry_Central_Bank_Policy_P4.md
  page: 208
- file: Perry_Central_Bank_Policy_P4.md
  page: 218
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

OMOs represent the "Active" mode of central bank intervention. Alexander Düring bóc tách ranh giới của thiết kế kỹ thuật (Price risk vs. Maturity decoupling), trong khi Perry Warjiyo giải mã cơ chế thực thi tại các nền kinh tế mới nổi (Sự chuyển dịch từ SBI sang SBN). Thành công của OMO không chỉ nằm ở việc bơm/hút tiền mà còn ở khả năng truyền dẫn tín hiệu chính sách (BI Rate) đến thị trường liên ngân hàng mà không gây ra "thuế" trung gian như GWM. [[During_Fixed_Income_Ch08.md#page=51]] [[Perry_Central_Bank_Policy_P4.md#page=208]]

---

## 1. Technical Taxonomy of Instruments

Central banks choose their tools based on the desired impact on the balance sheet and market signalling:

| Instrument | Ownership | Maturity Link | Risk Profile |
| :--- | :--- | :--- | :--- |
| **Outright Purchase (OMO)** | Central Bank becomes absolute owner. | Operation maturity < Asset maturity. | High **Price Risk** (CB bears volatility). |
| **Repo (Repurchase)** | Temporary transfer of title. | Decoupled (maturity set by CB). | Low Price Risk (Fixed buy-back price). |
| **Rediscounting** | Outright (Passive window). | Linked to asset maturity. | Recourse risk to bank & borrower. |

[[During_Fixed_Income_Ch08.md#page=51-52]]

---

## 2. The EME Evolution: The Indonesia Case (SBI vs. SBN)

Perry Warjiyo bóc tách sự tiến hóa của OMO tại Bank Indonesia (BI), phản ánh sự trưởng thành của thị trường tài chính:

### A. The SBI Era (1984–2010s)
- **Instrument:** Bank Indonesia Certificates (SBI) — a 0% interest liability issued *by* the central bank.
- **Rationale:** Used when government bond markets (SBN) were thin or non-existent.
- **Downside:** Highly expensive for the central bank as it must pay interest on its own debt (Cost of Monetary Control). [[Perry_Central_Bank_Policy_P4.md#page=218]]

### B. The SBN Transition (Modern Era)
- **Instrument:** Government Securities (SBN/SUN).
- **Rationale:** BI purchases SUN on the primary or secondary market.
- **Benefit:** Alleviates the central bank's cost of operations as the government bears the coupon cost. It simultaneously promotes domestic secondary market development and yield curve formation. [[Perry_Central_Bank_Policy_P4.md#page=285]]

---

## 3. Operational Mechanics & Signaling

### OMO vs. Accomodation (Düring's Lens)
Düring bóc tách ranh giới cực hay: OMO thông thường là để "phục vụ" (Accomodate) nhu cầu thanh khoản tự thân của thị trường.
- **Example:** Fed buying T-bills in 2019 was a response to a Repo squeeze, not a change in monetary stance. 
- **Signaling:** Standard OMOs are "Neutral" if they only offset autonomous factors (like tax payments), but become "Policy-driven" if they seek to push rates away from their current trend. [[During_Fixed_Income_Ch10.md#page=58]]

### FASBI (Rupiah Intervention)
Tại Indonesia, BI bổ sung công cụ **FASBI (Bank Indonesia Facilities)**:
- **Function:** A contractionary/expansionary instrument to alleviate interest rate shocks on the interbank market (PUAB).
- **Hierarchy:** Acting as a secondary buffer when OMO auctions are insufficient to hit the operational target. [[Perry_Central_Bank_Policy_P4.md#page=218]]

---

## Evidence / Source Anchors

- Definition of OMOs as outright buying/selling for liquidity control: [[During_Fixed_Income_Ch08.md#page=51]]
- Analysis of the cost-efficiency of using government securities (SUN) over SBI: [[Perry_Central_Bank_Policy_P4.md#page=209]]
- Distinction between Repo fixed maturity and OMO discretionary resale: [[During_Fixed_Income_Ch08.md#page=51]]
- Historical transition from SBI to SBN in Indonesia: [[Perry_Central_Bank_Policy_P4.md#page=218]]

## Related

- [[Central_Bank_Operational_Frameworks]] — The strategic use of OMO.
- [[Repurchase_Agreement]] — The primary alternative to outright OMO.
- [[Interest_Rate_Corridor_Mechanism]] — How OMO ghim rates within bounds.
- [[Quantitative_Easing]] — OMO taken to its extreme limit across the yield curve.
