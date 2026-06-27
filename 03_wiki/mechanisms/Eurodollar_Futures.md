---
title: Eurodollar Futures
aliases:
- Eurocurrency Futures
- ED Futures
type: mechanism
tags:
- derivatives
- futures
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Eurodollar futures are standardized exchange-traded contracts for hedging
  3-month LIBOR exposure, featuring a linear quoting convention and daily marking-to-market.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 89
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4634-4773
  section: "Chapter 6.2.2: Interest Rate Futures (STIR) and Eurodollar Spread Trading"
created: '2026-04-21'
updated: '2026-05-07'
---

## Thesis
[RAW] Eurodollar Futures là một trong những công cụ phái sinh lãi suất thanh khoản nhất thế giới. Điểm đặc thù của nó là quy ước báo giá tỷ lệ nghịch với lãi suất, giúp đồ thị Payoff trở nên tuyến tính như một hợp đồng kỳ hạn cổ phiếu.

## 1. Quoting Convention
[RAW] Giá Eurodollar Futures ($P$) được tính bằng:
$$P = 100 - \text{Interest Rate}$$
- **Transmission:** Khi lãi suất tăng -> Giá $P$ giảm. Khi lãi suất giảm -> Giá $P$ tăng.
- **Tick Value:** Mỗi tick $0.01$ (hoặc $0.005$) tương ứng với một giá trị tiền mặt cố định (e.g., $25 cho hợp đồng 1 triệu USD, kỳ hạn 3 tháng).

## 2. Worked Example: Marking-to-Market
[RAW] Trader mua 1 hợp đồng ED Futures tại giá 95.00 (tương đương lãi suất 5%).
- **Day 1:** Cuối ngày giá tăng lên 95.10 (lãi suất giảm còn 4.90%).
- **Mechanism:** Clearing house hạch toán lãi ngay lập tức: $10 \text{ ticks} \times \$25 = \$250$. Tiền được cộng vào tài khoản ký quỹ của trader.
- **Result:** Khác với FRA (đợi đến ngày settlement), Futures hiện thực hóa lãi/lỗ hàng ngày.

## 3. The Convexity Bias (Futures vs. FRA)
[RAW] Neftci giải thích ranh giới định giá giữa hai công cụ:
- Vì Futures có marking-to-market, dòng tiền lãi được nhận sớm hơn và có thể tái đầu tư.
- **The Bias:** Giá Futures thường thấp hơn giá FRA tương đương (tức là lãi suất Futures cao hơn lãi suất Forward) để bù đắp cho lợi thế về dòng tiền của bên nắm giữ vị thế mua trong điều kiện lãi suất biến động.
$$\text{Futures Rate} = \text{Forward Rate} + \text{Convexity Adjustment}$$

## 4. Failure Conditions
- **LIBOR Transition:** Hậu 2021, Eurodollar Futures (dựa trên LIBOR) đang được chuyển dịch sang **SOFR Futures**.
- **TED Spread Stress:** Khi chênh lệch giữa ED Futures và Treasury Futures dãn rộng, nó phản ánh sự thắt chặt tín dụng và thanh khoản nghiêm trọng trong hệ thống liên ngân hàng.

## Related
- [[Forward_Rate_Agreements_FRA]] — Công cụ OTC tương ứng.
- [[TED_Spread]] — Chỉ số đo lường rủi ro hệ thống.
- [[Variation_Margin_Vs_Initial_Margin]] — Cơ chế vận hành Futures.
