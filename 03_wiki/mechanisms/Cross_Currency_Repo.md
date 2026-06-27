---
title: Cross-Currency Repo Mechanics
aliases:
- CCY Repo
- Repo xuyên tiền tệ
type: mechanism
tags:
- repo
- fx
- funding
- collateral
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Salih Neftci - Principles of Financial Engineering (2008)
thesis: Repo xuyên tiền tệ (Cross-currency Repo) là một giao dịch trong đó bên vay
  nhận được nguồn vốn bằng một loại tiền tệ trong khi cung cấp tài sản đảm bảo bằng
  một loại tiền tệ khác, kết hợp việc huy động vốn qua repo với quản lý rủi ro tỷ
  giá.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 209
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis

[RAW] Cross-currency Repo là một biến thể nâng cao của Repo truyền thống, nơi rủi ro lãi suất và rủi ro tỷ giá đan xen. Nó cho phép một tổ chức có tài sản bằng đồng tiền A (e.g., EUR Bond) nhưng cần thanh khoản bằng đồng tiền B (e.g., USD Cash) thực hiện huy động vốn mà không phải bán đứt tài sản. [[Principles_of_Financial_Engineering_Neftci.md#page=209]]

---

## 1. Mechanics of the Invoice Price

Trong một giao dịch Cross-currency Repo, việc định giá tài sản đảm bảo (Invoice Price/Dirty Price) tuân thủ quy tắc:

1.  **Dirty Price (EUR):** Giá sạch + Lãi cộng dồn (Accrued Interest) của trái phiếu tính bằng đồng EUR.
2.  **Haircut Application:** Áp dụng tỷ lệ chiết khấu (Haircut) để bảo vệ bên cho vay tiền mặt trước biến động giá trái phiếu.
3.  **FX Conversion:** Chuyển đổi giá trị đã áp Haircut sang đồng tiền cho vay (USD) theo tỷ giá giao ngay ($e_{t0}$).

**Formula for Cash Received ($C_{USD}$):**
$$ C_{USD} = \frac{Dirty\_Price_{EUR} \times (1 - Haircut)}{e_{t0}} $$

---

## 2. Settlement and Interest

- **Interest Calculation:** Lãi Repo được tính trên số tiền mặt thực nhận bằng đồng USD, sử dụng lãi suất Repo USD.
- **Return Leg:** Tại thời điểm đáo hạn, bên vay trả lại số tiền $C_{USD}$ cộng với lãi Repo tích lũy và nhận lại trái phiếu EUR gốc.
- **Risk:** Bên vay chịu rủi ro tỷ giá nếu đồng EUR mất giá so với USD, dẫn đến việc phải bổ sung ký quỹ (Margin Call) bằng EUR hoặc USD.

---

## 3. Strategic Applications

- **Global Liquidity Management:** Các kho bạc (Treasury) toàn cầu sử dụng Cross-currency Repo để tối ưu hóa việc sử dụng tài sản đảm bảo trên nhiều thị trường khác nhau.
- **Funding Efficiency:** Nếu chi phí vay USD qua Repo (sử dụng EUR collateral) rẻ hơn vay USD trực tiếp, nó tạo ra cơ hội tiết kiệm chi phí vốn.

---

## Evidence / Source Anchors

- Calculation of invoice price and haircut in cross-currency repo: [[Principles_of_Financial_Engineering_Neftci.md#page=209]]
- Mechanics of cash reception and interest payment: [[Principles_of_Financial_Engineering_Neftci.md#page=209]]

## Related

- [[Repurchase_Agreement_Mechanism]] — Nền tảng Repo.
- [[FX_Swap_Engineering]] — Sự tương đồng về mặt kinh tế (collateralized loan).
- [[Haircut_And_Margin_Mechanics]] — Quản trị rủi ro tài sản đảm bảo.
- [[Cross_Currency_Rates_Synthetics]]
- [[Cross_Currency_Basis]]
