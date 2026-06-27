---
title: Entity-Netted Notionals (ENNs)
aliases:
- ENN
- Risk-Adjusted Swap Market Size
- Five-Year Equivalent Notionals
type: mechanism
tags:
- derivatives
- fixed-income
- market-structure
status: reviewed
confidence: 5
half_life_years: 10
expert_lens: Bruce Tuckman | Angel Serrat
provenance: '[RAW-BOOK: Tuckman & Serrat (2022) Ch 13]'
thesis: Entity-Netted Notionals (ENNs) provide a more accurate measure of systemic risk and market size in derivatives by netting offsetting positions between counterparty pairs and standardizing exposures across maturities using a duration-equivalent metric (e.g., Five-Year Equivalent).
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 320
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 321
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 322
created: '2026-04-28'
updated: '2026-04-29'
---

## Thesis

Trong khi con số "Gross Notional" thường gây ra sự hiểu lầm về quy mô thực sự của rủi ro hệ thống (systemic risk), **Entity-Netted Notionals (ENNs)** bóc tách rủi ro thực tế bằng cách gộp các vị thế đối ứng. Tuckman & Serrat nhấn mạnh rằng ENN mới là thước đo phản ánh "lượng rủi ro lãi suất thực sự đang được chuyển giao" trong nền kinh tế. Sự khác biệt giữa $210T (Gross) và $16.1T (ENN) minh chứng cho mức độ nén và netting cực cao trong hạ tầng thị trường hiện đại. [[Tuckman_Serrat_2022#page=345]]

---

## 1. The Netting Mechanism: From Gross to ENN

DENSE UNPACK:
- **INTENT:** Loại bỏ "rác" dữ liệu từ các chuỗi trung gian (intermediary chains) và các vị thế phòng vệ đối ứng để xác định rủi ro ròng mà một định chế thực sự nắm giữ.
- **MECHANISM:** 
  1. **Bilateral Netting:** Gộp tất cả các hợp đồng giữa Bên A và Bên B. Nếu A trả cố định $100M và nhận cố định $80M từ B, Notional ròng chỉ là $20M.
  2. **Risk Standardization:** Chuyển đổi các kỳ hạn khác nhau về một mốc chuẩn (thường là 5 năm).
- **INTERACTIONS:** Kết nối trực tiếp với [[Swap_Trade_Compression_And_Recouponing]]. Khi ENN thấp so với Gross, nó cho thấy thị trường đang vận hành hiệu quả qua các CCP (Central Counterparties).
- **BOUNDARY:** ENN không phản ánh rủi ro thanh khoản (liquidity risk) hoặc rủi ro vận hành (operational risk) phát sinh từ số lượng lớn các hợp đồng Gross, ngay cả khi rủi ro lãi suất đã được net.

---

## 2. Risk Standardization: The Five-Year Equivalent

Để so sánh rủi ro giữa một swap 2 năm và 30 năm, thị trường sử dụng khái niệm **Five-Year Equivalent (5Y Eq)**:

$$ENN_{5Y} = Notional \times \frac{Duration_{Target}}{Duration_{5Y}}$$

- **Logic:** Một swap 30 năm có độ nhạy lãi suất (DV01) cao hơn nhiều so với swap 2 năm. Việc quy đổi về 5Y Eq cho phép cộng dồn rủi ro của toàn bộ danh mục một cách nhất quán.
- **Market Impact:** Theo báo cáo của ISDA được dẫn bởi Tuckman, tổng thị trường swap lãi suất tính theo Gross Notional là khoảng $210 nghìn tỷ USD, nhưng khi tính theo ENN quy đổi 5Y, con số này chỉ còn khoảng **$16.1 nghìn tỷ USD** (số liệu 2021). [[Tuckman_Serrat_2022#page=346]]

---

## 3. Macro Significance

- **Systemic Risk Assessment:** Các cơ quan quản lý (Fed, BIS) ưu tiên ENN để đánh giá khả năng lan tỏa rủi ro khi một định chế lớn sụp đổ.
- **Capital Requirements:** Basel III và các quy định ký quỹ (Initial Margin) dựa trên mức độ rủi ro ròng, thúc đẩy các ngân hàng thực hiện compression để giảm Gross Notional mà không đổi ENN.

---

## Evidence / Source Anchors

- Market size comparison ($210T vs $16.1T ENN): [[Tuckman_Serrat_2022#page=346]]
- Definition of ENN and bilateral netting rationale: [[Tuckman_Serrat_2022#page=345]]
- Standardizing risk via Five-Year Equivalent formula: [[Tuckman_Serrat_2022#page=346]]

## 4. Tuckman Ch 13 Market-Size Audit

[RAW-BOOK] Tuckman & Serrat's Chapter 13 separates three layers that are often conflated in swap-market commentary: gross notional, five-year-equivalent notional, and entity-netted notional. Gross notional answers "how much contractual principal is referenced"; five-year equivalents answer "how much rate DV01 is embedded after maturity standardization"; ENN answers "how much bilateral, directionally un-offset risk remains after long and short positions are netted between the same counterparty pair." [[Tuckman_Serrat_Fixed_Income_2022.md#page=320]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=321]]

[RAW-BOOK] The dense claim is that IRS market size cannot be inferred from gross notional. INTENT: Tuckman is trying to prevent notional from being mistaken for loss-at-default or economic balance-sheet size. MECHANISM: a $100 million 10-year swap with DV01 0.090 carries twice the five-year-equivalent exposure of a $100 million 5-year swap with DV01 0.045; after this duration standardization, opposite-direction trades between the same two entities are netted to ENN. INTERACTIONS: this metric connects directly to [[Swap_Trade_Compression_And_Recouponing]], [[DV01_Risk_Management]], and [[Central_Counterparty_CCP]], because compression and clearing reduce operational clutter without necessarily reducing the final sectoral risk direction. BOUNDARY: ENN is a cleaner market-size metric for interest-rate risk, but it does not measure liquidity calls, MPOR gap risk, legal close-out frictions, or concentration risk at CCPs. [[Tuckman_Serrat_Fixed_Income_2022.md#page=322]]

[RAW-BOOK] Sectoral signs are economically meaningful only after netting: banks appear net short in Tuckman's table, consistent with hedging mortgage assets, while pensions and insurers appear net long because receiving fixed in swaps can hedge long-duration liabilities. The table's point is not that every entity in the sector behaves the same way; it is that ENN exposes residual sector direction after dealer intermediation and bilateral offsets have been stripped out. [[Tuckman_Serrat_Fixed_Income_2022.md#page=322]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The underlying instrument for ENN calculations.
- [[Swap_Trade_Compression_And_Recouponing]] — The process that reduces Gross Notional while keeping ENN stable.
- [[DV01_Risk_Management]] — The metric used to calculate duration-based equivalents.
- [[Interest_Rate_Swap_Use_Cases]] — Sector behavior that gives ENN its directional interpretation.
