---
title: Term Structure Bootlacing
aliases:
- Bootlacing representation
- Precedents tracing
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch20.md"
thesis: '"Bootlacing" là thuật ngữ dùng để mô tả tính chất phụ thuộc lẫn nhau mang
  tính chuỗi (iterative precedents) trong quy trình [[Bootstrapping_Techniques|bootstrapping]]
  khi được thực hiện trên các ứng dụng bảng tính. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=7]]'
source_refs:
- file: Fixed_Income_Alexander_During_Ch20.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 19
---

# Term Structure Bootlacing

## Mechanism

"Bootlacing" là thuật ngữ dùng để mô tả tính chất phụ thuộc lẫn nhau mang tính chuỗi (iterative precedents) trong quy trình [[Bootstrapping_Techniques|bootstrapping]] khi được thực hiện trên các ứng dụng bảng tính. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=7]]

### Logic vận hành
Trong quá trình bootstrapping, hệ số chiết khấu (discount factor) tại bất kỳ điểm thời gian $t_i$ nào cũng được tính toán dựa trên:
1. Giá thị trường của công cụ tại kỳ hạn $t_i$.
2. **Tất cả các hệ số chiết khấu** đã được tính toán từ các bước trước đó ($t_1, t_2, ..., t_{i-1}$).

### Ý nghĩa của hình thái "Bootlacing"
Khi người dùng thực hiện truy vết các ô [[Money|tiền]] tố (trace precedents) trong phần mềm bảng tính, các đường nối sẽ tạo thành một hình thái giống như "dây giày" thắt chặt dần. Điều này hàm ý rằng:
- Một lỗi nhỏ hoặc một sự méo mó giá ở các kỳ hạn ngắn sẽ lan truyền (propagated) và khuếch đại vào toàn bộ các điểm lãi suất ở kỳ hạn dài hơn.
- Cấu trúc đường cong không phải là tập hợp các điểm độc lập mà là một hệ thống các biến số có tính liên kết chặt chẽ về mặt toán học. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=7]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch20.md#page=7]] — Khái niệm Bootlacing và tính lan truyền sai số trong bootstrapping.


## Related

- [[Global_Sovereign_Bond_Markets]]
- [[Inverse_Floater_Structure]]
- [[Repurchase_Agreement_Repo_Market_Structure]]
- [[Supranational_Capital_Structure]]
- [[Term_Risk_Premium_Mechanics]]
- [[TIPS_Bond_Structure]]
- [[Yield_Curve_Structure_And_Mechanics]]
- [[Nonbank_Financial_Intermediation]]
- [[Structured_Notes]]
- [[Structured_Vs_Statutory_Covered_Bonds]]
- [[Disintermediation_and_Credit_Crunch_Indonesia]]
- [[Exchange_Rate_Determination_Theories]]
- [[CLO_Tranche_Structure_And_Loss_Allocation]]
- [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]]
- [[Asset_Swap_Structure]]
- [[Credit_Default_Swaps_Schofield]]
- [[Monetary_Survey_Banking_System_Structure]]
- [[Credit_Trading_Applications_Term_Structure_And_Single_Entity]]
- [[Fed_Duration_Extraction_Term_Premium]]
- [[Foreign_Capital_Flows_Determinants]]
- [[Order_Flow_FX_Determination]]
- [[PBOC_CFETS_Infrastructure]]
