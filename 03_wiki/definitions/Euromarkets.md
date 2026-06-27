---
title: Euromarkets
aliases:
- Offshore Markets
- Eurocurrency Market
- Eurobond Market
type: definition
tags:
- market-structure
- regulation
- offshore
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Euromarkets are offshore financial markets operating outside the formal control
  of domestic regulators, characterized by the absence of reserve requirements and
  simplified security registration.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 27
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Thuật ngữ "Euro" trong Euromarkets không ám chỉ châu Âu hay đồng tiền Euro, mà ám chỉ các thị trường nằm ngoài tầm kiểm soát trực tiếp của các cơ quan quản lý và ngân hàng trung ương (Offshore).

## 1. Core Logic: Onshore vs. Offshore
[RAW] Sự khác biệt cốt lõi nằm ở hai đặc điểm:
1.  **Reserve Requirements (Dự trữ bắt buộc):** Các thị trường nội địa (Onshore) yêu cầu ngân hàng trích lập dự trữ không hưởng lãi, làm tăng chi phí vốn. Euromarkets loại bỏ chi phí này, tăng tính thanh khoản cho các giao dịch bán buôn (wholesale).
2.  **Registration Process (Đăng ký chứng khoán):** Onshore yêu cầu quy trình đăng ký phức tạp và công khai thông tin. Euromarkets sử dụng các công cụ vô danh (bearer securities) với quy trình đơn giản hơn và chi phí phát hành thấp hơn.

## 2. Taxonomy of Euromarkets
- **Eurocurrency Market:** Thị trường tiền gửi ngân hàng bằng ngoại tệ (thường là USD) nằm ngoài quốc gia phát hành tiền tệ đó (e.g., Eurodollar tại London). Đây là thị trường liên ngân hàng thuần túy.
- **Eurobond Market:** Trái phiếu được phát hành vô danh (bearer form) tại các trung tâm tài chính như London, Asia và không chịu thuế khấu trừ tại nguồn (withholding taxes).
- **Other Euro-instruments:** Euro-equity, Euro-commercial paper (ECP), và Euro medium-term notes (EMTN).

## 3. Worked Example (The Cost Advantage)
[RAW] Giả sử một ngân hàng Onshore nhận 100 USD tiền gửi và phải dự trữ 10% tại NHTW:
- **Mechanism:** Ngân hàng chỉ có thể cho vay 90 USD nhưng phải trả lãi cho toàn bộ 100 USD. Để bù đắp, lãi suất cho vay onshore phải cao hơn ~10% so với chi phí vốn.
- **Result:** Euromarkets cho phép cho vay toàn bộ 100 USD, giúp thu hẹp biên độ lãi suất và tạo ra một thị trường liên ngân hàng hiệu quả vượt trội.

## Related
- [[Synthetic_Loan_Engineering]] — Ứng dụng Euromarkets để vượt qua giới hạn tín dụng.
- [[Bearer_Vs_Registered_Securities]] — Phân loại chứng khoán theo quyền sở hữu.
- [[Nostro_Account]] — Hạ tầng thanh toán cho giao dịch offshore.
- [[Alternative_Investment_Funds]]
- [[Business_Development_Company]]
- [[CLOB_Vs_OTC_Execution]]
- [[Dark_Pools]]
- [[ELTIF_And_AIFMD_Framework]]
- [[Market_Maker_Vs_Liquidity_Provider]]
- [[OTC_Vs_Exchange_Trading]]
- [[Coupon_Washing_Tax_Strategies]]
- [[Preferred_Habitat_Market_Distortions]]
- [[Wash_Sale_Rules_Tactics]]
