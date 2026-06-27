---
title: DSGE Modeling with Financial Frictions
aliases:
- Financial Frictions in DSGE
- Macro-Financial Linkages Modeling
- DSGE vs Structural Models
- Mô hình hóa ma sát tài chính
type: mechanism
tags:
- economics
- modeling
- financial-stability
- macroeconomics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (Warjiyo & During)
thesis: Integrating financial frictions into Dynamic Stochastic General Equilibrium
  (DSGE) models involves moving beyond representative agent assumptions to explicitly
  incorporate borrower heterogeneity, asymmetric information, and financial intermediation
  as endogenous drivers of the business cycle.
source_refs:
- file: Perry_Central_Bank_Policy_P6.md
  page: 486
- file: Perry_Central_Bank_Policy_P6.md
  page: 489
- file: During_Fixed_Income_Ch38.md
  page: 360
- file: Perry_Central_Bank_Policy_P6.md
  page: 490
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Tại sao các mô hình DSGE truyền thống lại thất bại trong việc dự báo khủng hoảng 2008? Alexander Düring bóc tách ranh giới của các giả định toán học (Tính phi stationary và hành vi phản xạ), trong khi Perry Warjiyo giải mã cơ chế nâng cấp mô hình thông qua **Ma sát tài chính (Financial Frictions)**. Để mô phỏng được thế giới thực, DSGE phải từ bỏ giả định về "Thị trường hiệu quả" và đưa vào các ràng buộc về tài sản đảm bảo cũng như hành vi rủi ro của ngân hàng. [[Perry_Central_Bank_Policy_P6.md#page=486]] [[During_Fixed_Income_Ch38.md#page=360]]

---

## 1. Approaches to Modeling Financial Frictions

Perry bóc tách 3 phương pháp cốt lõi để "bẻ gãy" sự hoàn hảo của thị trường trong mô hình:

| Approach | Key Mechanism | Theoretical Origin |
| :--- | :--- | :--- |
| **Financial Accelerator** | **External Financing Premium (EFP).** Chi phí vốn vay tỷ lệ nghịch với giá trị ròng của doanh nghiệp. | Bernanke, Gertler, Gilchrist (1999) |
| **Collateral Constraints** | **Credit Ceiling.** Hạn mức vay bị giới hạn cứng bởi giá trị tài sản đảm bảo (bất động sản, máy móc). | Kiyotaki & Moore (1997) |
| **Financial Intermediation** | **Endogenous Banking.** Ngân hàng được mô hình hóa như một thực thể có bảng cân đối, rủi ro đòn bẩy và CAR riêng. | Gerali et al. (2010) |

[[Perry_Central_Bank_Policy_P6.md#page=489]]

---

## 2. Structural Upgrades: From Homogeneity to Heterogeneity

Để tích hợp ma sát tài chính, mô hình DSGE hiện đại phải thay đổi cấu trúc:
- **Heterogeneous Agents:** Thay vì một "hộ gia đình đại diện," mô hình chia ra **Savers** (nhà đầu tư kiên nhẫn) và **Borrowers** (doanh nghiệp/hộ gia đình nợ nần).
- **Asymmetric Information:** Đưa vào chi phí giám sát (monitoring costs) và lựa chọn nghịch (adverse selection) làm phát sinh ranh giới EFP.
- **Endogenous Risk:** Rủi ro không còn là một cú shock ngoại sinh ngẫu nhiên mà là kết quả của việc tích tụ đòn bẩy trong thời kỳ boom. [[Perry_Central_Bank_Policy_P6.md#page=490]]

---

## 3. Operational Warning: The Model Trap (Düring's Lens)

Düring nhấn mạnh ranh giới thực thi mà các nhà kinh tế lượng thường bỏ qua:
- **Parameter Invariance:** DSGE giả định các tham số hành vi là cố định. Tuy nhiên, trong khủng hoảng, tâm lý con người thay đổi đột ngột, làm vô hiệu hóa toàn bộ các phương trình đã được ước lượng (The Lucas Critique).
- **Complexity vs. Useability:** Một mô hình quá phức tạp (ví dụ 300 phương trình) có thể khớp dữ liệu quá khứ hoàn hảo nhưng lại mất khả năng dự báo tương lai do hiện tượng Overfitting. [[During_Fixed_Income_Ch38.md#page=360]]

---

## 4. Strategic Implications: Policy Mix Simulation

Perry Warjiyo nhấn mạnh rằng DSGE nâng cấp là công cụ duy nhất để kiểm tra tính nhất quán của **Policy Mix**:
- **Coordination Check:** Mô phỏng xem việc tăng lãi suất 1% kết hợp với giảm LTV 10% sẽ tác động như thế nào đến lạm phát và nợ xấu (NPL).
- **Social Welfare Optimization:** Tìm ra các trọng số ($\omega$) tối ưu để tối thiểu hóa hàm tổn thất chung của xã hội. [[Perry_Central_Bank_Policy_P6.md#page=501]]

---

## Evidence / Source Anchors

- Taxonomy of financial frictions approaches in DSGE (Table 15.4): [[Perry_Central_Bank_Policy_P6.md#page=489]]
- Analysis of the external financing premium as a driver of the financial accelerator: [[Perry_Central_Bank_Policy_P6.md#page=488]]
- Identification of the Gerali et al. (2010) model for banking intermediation: [[Perry_Central_Bank_Policy_P6.md#page=491]]
- Rationale for the failure of representative agent models post-GFC: [[Perry_Central_Bank_Policy_P6.md#page=487]]

## Related

- [[Financial_Procyclicality_Mechanism]] — The dynamic captured by these models.
- [[Central_Bank_Policy_Mix_Paradigm]] — The policy framework these models seek to optimize.
- [[Bank_Indonesia_Macroeconomic_Models]] — The specific implementation (ARIMBI).
- [[Systemic_Risk_Taxonomy]] — The variables being endogenized.
- [[Macrostability_Without_Financial_Stability_Paradox]]
- [[Financial_Deepening]]
- [[Monetarist_Vs_Keynesian_Monetary_Views]]
- [[Exchange_Rate_Determination_Theories]]
