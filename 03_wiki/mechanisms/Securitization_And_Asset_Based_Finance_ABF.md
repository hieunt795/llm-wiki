---
title: Securitization and Asset-Based Finance (ABF)
aliases:
- Asset-Backed Securities
- ABS
- ABF
- SPV Architecture
- Tranching and Waterfall
- RMBS
- Chứng khoán hóa và Tài chính dựa trên tài sản
type: mechanism
tags:
- structured-finance
- private-credit
- banking
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During, Warjiyo & IMF)
thesis: Securitization and Asset-Based Finance (ABF) are financial engineering processes
  that transform illiquid asset pools into tradable securities through Special Purpose
  Vehicles (SPVs), serving as a primary channel for off-balance sheet credit creation
  and the strategic core of the modern private credit ecosystem.
source_refs:
- file: During_Fixed_Income_Ch26.md
  page: 265
- file: Deep Dive_ Private Credit.md
  page: 5
- file: Perry_Central_Bank_Policy_P3.md
  page: 70
- file: During_Fixed_Income_Ch26.md
  page: 268
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Chứng khoán hóa (Securitization) là "máy giặt bảng cân đối" của hệ thống tài chính. Alexander Düring bóc tách ranh giới kỹ thuật của việc phân tầng rủi ro (Tranching), trong khi Perry Warjiyo và IMF giải mã cơ chế trỗi dậy của **Asset-Based Finance (ABF)** trong kỷ nguyên Private Credit. Từ việc đóng gói các khoản vay thế chấp nhà (RMBS) truyền thống, hệ thống đã tiến hóa thành một mạng lưới tài trợ dựa trên tài sản thực phức tạp, nơi rủi ro không biến mất mà chỉ chuyển dịch từ Solvency (ngân hàng) sang Network Liquidity (thanh khoản mạng lưới). [[During_Fixed_Income_Ch26.md#page=265]] [[Deep Dive_ Private Credit.md#page=5]]

---

## 1. The Architecture: Special Purpose Vehicle (SPV)

Trái tim của Securitization là **SPV** — một thực thể pháp lý được thiết lập với mục đích duy nhất là nắm giữ tài sản.
- **Bankruptcy Remoteness:** Ranh giới pháp lý tối thượng. Nếu ngân hàng phát hành (Originator) bị phá sản, các chủ nợ của ngân hàng không có quyền chạm vào tài sản trong SPV. Tài sản này chỉ thuộc về người giữ ABS.
- **True Sale:** Việc chuyển giao tài sản từ bảng cân đối ngân hàng sang SPV phải là một giao dịch "Bán đứt" thực sự để được công nhận về mặt kế toán và pháp lý. [[During_Fixed_Income_Ch26.md#page=268]]

---

## 2. Risk Engineering: Tranching and Waterfall

Düring giải mã cơ chế "biến đồng thành vàng" thông qua việc phân tầng:

### A. The Tranche Hierarchy
Dòng tiền từ SPV được chia thành các tầng (tranches) với mức độ ưu tiên khác nhau:
1.  **Senior Tranche:** Được trả nợ đầu tiên. Có xếp hạng tín nhiệm cao (AAA) và lãi suất thấp.
2.  **Mezzanine Tranche:** Tầng trung gian, chịu lỗ sau tầng Equity nhưng trước tầng Senior.
3.  **Equity/First-Loss Tranche:** Được hưởng phần lợi nhuận còn lại (Residual) nhưng là bên đầu tiên chịu lỗ nếu có nợ xấu. [[During_Fixed_Income_Ch26.md#page=269]]

### B. The Waterfall Mechanism
- **Sequential Pay:** Cơ chế trả nợ lần lượt. Senior được hoàn gốc 100% trước khi đồng Mezzanine đầu tiên được trả. Điều này giúp giảm **Duration** cho tầng Senior, bảo vệ họ khỏi rủi ro thời gian.
- **Credit Enhancement:** Tăng cường tín nhiệm qua: (1) Over-collateralization (tài sản > nợ), (2) Excess Spread (lãi vay > lãi trả cho ABS), và (3) Subordination (tầng dưới bảo vệ tầng trên). [[During_Fixed_Income_Ch26.md#page=270]]

---

## 3. The Modern Evolution: Asset-Based Finance (ABF)

Trong Private Credit, Securitization được nâng cấp thành **ABF**:
- **From Cash Flow to Hard Assets:** Khác với ABS truyền thống dựa trên dòng tiền từ các khoản vay lẻ, ABF dựa trên giá trị thanh lý của tài sản thực (hàng tồn kho, quyền thu nợ, bất động sản thương mại).
- **The Role of Sponsors:** Các quỹ PE đóng vai trò là bên bảo trợ, cung cấp tầng Equity và cam kết duy trì chất lượng tài sản, biến ABF thành một nền tảng tài trợ linh hoạt hơn nhiều so với trái phiếu đại chúng. [[Deep Dive_ Private Credit.md#page=8]]

---

## 4. Strategic Implications: Shadow Banking & Lags

Perry Warjiyo bóc tách ranh giới của sự mất kiểm soát tiền tệ:
- **Credit Creation Outside Banks:** Securitization cho phép tín dụng được tạo ra mà không bị ràng buộc bởi dự trữ bắt buộc (GWM).
- **M2 Blurring:** Người dân coi các chứng chỉ ABS/ABF có tính thanh khoản cao như một dạng "tiền", làm vô hiệu hóa các mỏ neo cung tiền truyền thống của NHTW.
- **The Masking Risk (PIK):** Cơ chế **Payment-in-Kind (PIK)** trong các hợp đồng ABF cho phép người nợ cộng lãi vào gốc. Điều này giữ cho tỷ lệ vỡ nợ (default rates) trông ổn định trong ngắn hạn nhưng làm tăng rủi ro "bom nợ" bùng phát đồng loạt khi chu kỳ đảo chiều. [[Deep Dive_ Private Credit.md#page=12]] [[Perry_Central_Bank_Policy_P3.md#page=70]]

---

## Evidence / Source Anchors

- Definition of SPV as a bankruptcy-remote legal vehicle: [[During_Fixed_Income_Ch26.md#page=268]]
- Analysis of sequential vs. pro-rata waterfall structures: [[During_Fixed_Income_Ch26.md#page=270]]
- Comparison of corporate private credit vs. asset-based finance (ABF): [[Deep Dive_ Private Credit.md#page=14]]
- Discussion on the impact of securitization on monetary aggregates (M2): [[Perry_Central_Bank_Policy_P3.md#page=70]]

## Related

- [[Covered_Bonds_Mechanism]] — The primary on-balance-sheet alternative to ABS.
- [[LTV_Ratio_In_Mortgage_Lending]] — The primary risk metric for RMBS.
- [[Principal_Component_Analysis_PCA]] — Used to analyze the correlation of assets within an ABS pool.
- [[Systemic_Risk_Taxonomy]] — Why ABF shifts risk into the "Network Liquidity" dimension.
