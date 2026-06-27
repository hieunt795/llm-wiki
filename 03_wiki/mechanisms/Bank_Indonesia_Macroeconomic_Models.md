---
title: Bank Indonesia Macroeconomic Models
aliases:
- BI Modeling System
- SOFIE vs MODBI vs ARIMBI
- Forecasting and Policy Analysis System (FPAS)
- Hệ thống mô hình vĩ mô của BI
type: mechanism
tags:
- economics
- modeling
- indonesia
- central-banking
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Bank Indonesia vận hành một hệ sinh thái mô hình vĩ mô phân tầng, từ các phương
  trình cấu trúc quy mô nhỏ (SSM) đến các mô hình semi-DSGE quy mô lớn (ARIMBI), nhằm
  cung cấp các dự báo lạm phát nhất quán và mô phỏng các phản ứng chính sách đa công
  cụ.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 287
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

Dự báo lạm phát là "mỏ neo trung gian" của ITF. Perry Warjiyo giải mã bộ máy tính toán của Bank Indonesia: NHTW không dựa vào một mô hình duy nhất mà vận hành một "vườn bách thú" mô hình (The Modeling Zoo), nơi mỗi mô hình giải quyết một tầm nhìn khác nhau, từ các biến động ngắn hạn (SSM) đến các mô phỏng chính sách dài hạn (ARIMBI). Sự phối hợp này giúp BI kiểm soát được tính bất ổn của nền kinh tế Indonesia. [[Perry_Central_Bank_Policy_P4.md#page=287]]

---

## 1. The Modeling Tier System

| Model | Scale / Type | Purpose | Primary Variables |
| :--- | :--- | :--- | :--- |
| **SSM** | Small (7 equations) | Short-term inflation forecasting. | NKPC, IS Curve, Taylor Rule. |
| **SOFIE** | Medium (279 equations) | Quarterly macroeconomic analysis. | 6 blocks (Demand, Price, Monetary, Fiscal, Banking, External). |
| **MODBI** | Large (87 equations) | Medium-long term projections (5 years). | 5 structural blocks, focus on behavioral identities. |
| **ARIMBI** | Semi-DSGE (Modern) | Policy Mix simulation & FPAS. | Endogenous risk, Credit, Default risk, Capital flows. |

[[Perry_Central_Bank_Policy_P4.md#page=287-288]]

---

## 2. Key Model Mechanisms

### A. SOFIE (Structural Model for the Indonesian Economy)
- **Mechanism:** Sử dụng kỹ thuật Hiệu chỉnh sai số (Error-correction) để bóc tách các mối quan hệ ngắn hạn và dài hạn.
- **Role:** Là công cụ chính phục vụ các cuộc họp Hội đồng Thống đốc (RDG) hàng quý. [[Perry_Central_Bank_Policy_P4.md#page=287]]

### B. ARIMBI (Aggregate Rational Inflation Targeting Model)
- **Mechanism:** Dựa trên lý thuyết New Keynesian, tích hợp kỳ vọng hợp lý (Rational Expectations).
- **The Upgrade:** Đây là mô hình duy nhất có khả năng mô phỏng đồng thời **Lãi suất** và **Macroprudential** (LTV, GWM). Nó tích hợp các biến số BOP (Cán cân thanh toán) và rủi ro tín dụng để kiểm tra tính nhất quán của [[Central_Bank_Policy_Mix_Paradigm|Policy Mix]]. [[Perry_Central_Bank_Policy_P4.md#page=288]]

---

## 3. Strategic Implications: The FPAS Approach

Từ năm 2010, BI áp dụng hệ thống **FPAS (Forecasting and Policy Analysis System)** của IMF:
- **Consistency:** Đảm bảo các dự báo từ các mô hình khác nhau không mâu thuẫn.
- **Judgment Integration:** Kết quả mô hình luôn được kết hợp với nhận định định tính (Qualitative judgment) từ các khảo sát thực địa (SKDU, SK).
- **Cross-check:** Sử dụng các mô hình VAR và Time-series để kiểm tra chéo (benchmarking) độ chính xác của các mô hình cấu trúc. [[Perry_Central_Bank_Policy_P4.md#page=287]]

---

## Evidence / Source Anchors

- Taxonomy of the four primary BI macroeconomic models: [[Perry_Central_Bank_Policy_P4.md#page=287]]
- Description of SOFIE as a 279-equation structural model: [[Perry_Central_Bank_Policy_P4.md#page=287]]
- Identification of ARIMBI as the semi-DSGE core for policy mix simulation: [[Perry_Central_Bank_Policy_P4.md#page=288]]
- Formulation of the SSM model based on 7 core equations: [[Perry_Central_Bank_Policy_P4.md#page=287]]

## Related

- [[Inflation_Targeting_In_Indonesia]] — The strategic context for these models.
- [[New_Keynesian_Phillips_Curve_NKPC]] — The mathematical engine of SSM and ARIMBI.
- [[Central_Bank_Policy_Mix_Paradigm]] — The complex policy set these models seek to simulate.
- [[Taylor_Rule_Monetary_Policy]] — The reaction function embedded in the models.
