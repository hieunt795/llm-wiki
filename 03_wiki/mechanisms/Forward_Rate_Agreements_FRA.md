---
title: Forward Rate Agreements (FRA)
aliases:
- FRA
- Kỳ hạn lãi suất
type: mechanism
tags:
- derivatives
- fixed-income
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: An FRA is an OTC derivative that allows participants to lock in an interest
  rate for a future period, cash-settling the difference between the agreed forward
  rate and the realized spot rate at the beginning of the accrual period.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 79
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] FRA là công cụ cơ bản nhất để quản lý rủi ro lãi suất trong tương lai mà không cần thực hiện các khoản vay hay gửi tiền thực tế (unfunded). Đặc điểm quan trọng nhất của FRA là việc thanh toán (settlement) diễn ra tại **thời điểm bắt đầu** của kỳ hạn tính lãi, yêu cầu một phép chiết khấu ngược (discounting backwards).

## 1. The Contractual Equation
[RAW] Một FRA có thể được mô phỏng (replicate) thông qua thị trường tiền tệ (Money Market):
$$\text{FRA} = \text{Long Long-term Loan} + \text{Short Short-term Loan}$$

**Cơ chế truyền dẫn:**
1.  Vay tiền kỳ hạn dài (e.g., 6 tháng).
2.  Gửi số tiền đó kỳ hạn ngắn (e.g., 3 tháng).
3.  Kết quả là bạn đã "chốt" được lãi suất cho giai đoạn từ tháng thứ 3 đến tháng thứ 6.

## 2. The FRA as a "Bridge Asset" (Neftci Framework)
[RAW] Trong kỹ thuật tài chính, FRA đóng vai trò là tài sản "bắc cầu" (bridge asset) thiết yếu để thực hiện **Static Replication** khi các kỳ hạn trung gian của trái phiếu bị thiếu hoặc kém thanh khoản.

- **The Missing Asset Problem:** Nếu ta muốn tạo một trái phiếu 2 kỳ hạn $B(t_0, T_2)$ nhưng thị trường chỉ có trái phiếu 3 kỳ hạn $B(t_0, T_3)$, ta cần một FRA $2 \times 3$ để "triệt tiêu" (offset) dòng tiền thừa tại $T_3$ và dời nó về $T_2$.
- **Mechanism:** 
    1. **Long** trái phiếu 3 kỳ hạn ($B(t_0, T_3)$).
    2. **Short** FRA $2 \times 3$ để khóa lãi suất nhận được giữa $T_2$ và $T_3$.
    3. Kết quả là dòng tiền tại $T_3$ được cố định và chiết khấu về $T_2$, mô phỏng chính xác $B(t_0, T_2)$.
- **Conclusion:** Nếu không có FRA, việc mô phỏng tĩnh các kỳ hạn bị thiếu là bất khả thi (do rủi ro rollover lãi suất), buộc phải chuyển sang phương pháp **Dynamic Replication**. [[Principles_of_Financial_Engineering_Neftci.md#page=244]]

## 3. Worked Example: Settlement Calculation
[RAW] Giả sử doanh nghiệp ký FRA $3 \times 6$ (kỳ hạn 3 tháng cho khoản vay 3 tháng) với lãi suất chốt 5%. Mệnh giá 100 triệu USD.
- **Scenario:** Sau 3 tháng, lãi suất LIBOR thực tế là 6%. 
- **Mechanism:** Ngân hàng phải trả cho doanh nghiệp phần chênh lệch 1% ($6\% - 5\%$).
- **The Discounting Nuance:** Vì lãi suất 6% chỉ được trả vào cuối tháng thứ 6, nhưng việc thanh toán FRA diễn ra ngay tại đầu tháng thứ 3, số tiền thanh toán phải được chiết khấu ngược về $t_3$:
$$\text{Payment} = \frac{(L_{spot} - r_{fra}) \times \text{Notional} \times \delta}{1 + L_{spot} \times \delta}$$
Trong đó $\delta$ là phân số năm (daycount fraction).

## 3. Failure Conditions / Boundaries
- **Credit Risk:** [RAW] Khác với Futures, FRA có rủi ro đối tác song phương (bilateral). Tuy nhiên, rủi ro này thấp hơn khoản vay thực tế vì chỉ thanh toán phần chênh lệch (net settlement).
- **Convexity Bias:** FRA là công cụ tuyến tính, trong khi Eurodollar Futures có cơ chế marking-to-market hàng ngày tạo ra sự khác biệt nhỏ về định giá (Convexity bias).

## Related
- [[Eurodollar_Futures]] — Đối trọng trên sàn giao dịch.
- [[Synthetics_Replicating_Portfolios]] — Nguyên lý cấu tạo FRA.
- [[Forward_LIBOR_Loan_Mechanism]] — Bản chất kinh tế của FRA.
