---
title: OIS and Benchmark Reform
aliases:
- LIBOR Transition
- SOFR vs LIBOR
- OIS Discounting Standard
- €STR
- Cải cách lãi suất tham chiếu
type: mechanism
tags:
- central-banking
- money-market
- derivatives
- conventions
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat | Alexander Düring"
provenance: Multi-source (During & Tuckman)
thesis: The global benchmark reform represents a structural shift from credit-sensitive
  term rates (LIBOR) to risk-free overnight rates (SOFR, €STR), necessitating the
  universal adoption of OIS discounting as the unique no-arbitrage valuation standard.
source_refs:
- file: During_Fixed_Income_Ch23.md
  page: 200
- file: Tuckman_Serrat_2022.md
  page: 9
- file: Tuckman_Serrat_2022.md
  page: 65
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Thế giới tài chính đang trải qua một cuộc "thay máu" hạ tầng. Alexander Düring bóc tách ranh giới rủi ro của LIBOR (Sự thiếu hụt giao dịch thực tế), trong khi Tuckman & Serrat (2022) giải mã cơ chế vận hành của thế giới hậu-LIBOR. Sự chuyển dịch sang các lãi suất qua đêm (RFRs) như **SOFR** và **€STR** không chỉ là thay đổi một con số, mà là thay đổi toàn bộ triết lý định giá: từ việc chiết khấu bằng lãi suất ngân hàng sang chiết khấu bằng mỏ neo thanh khoản tuyệt đối (**OIS Discounting**). [[Tuckman_Serrat_2022.md#page=9]]

---

## 1. The Death of LIBOR: From Judgment to Data

Düring nhấn mạnh ranh giới thất bại của LIBOR:
- **Expert Judgment Trap:** LIBOR dựa trên báo cáo của các ngân hàng về mức lãi suất họ "nghĩ" là có thể vay được. Khi thanh khoản liên ngân hàng cạn kiệt, các báo cáo này trở thành hư cấu.
- **The Reform:** Các mỏ neo mới (RFRs) được xây dựng hoàn toàn dựa trên **Giao dịch thực tế (Transaction-based)**. [[During_Fixed_Income_Ch23.md#page=200]]

---

## 2. The New Anchors (Tuckman's Lens)

Tuckman & Serrat bóc tách đặc tính của các mỏ neo hiện đại (2022 Standard):

| Benchmark | Market | Type | Description |
| :--- | :--- | :--- | :--- |
| **SOFR** | USD | **Secured** | Dựa trên thị trường Repo kho bạc Mỹ (~1000 tỷ USD giao dịch/ngày). Mỏ neo rủi ro thấp nhất. |
| **€STR** | EUR | **Unsecured** | Dựa trên các khoản vay qua đêm liên ngân hàng tại Eurozone. |
| **SONIA** | GBP | Unsecured | Mỏ neo truyền thống của Anh, được cải cách để dựa trên giao dịch thực. |

### The Compounding Logic (Forward vs. Backward-looking)
Vì các lãi suất mới (RFRs) là qua đêm (overnight), để tạo ra một lãi suất kỳ hạn (ví dụ 3 tháng) tương đương với LIBOR, thị trường bắt buộc phải sử dụng cơ chế **Daily Compounding** (lãi kép cộng dồn từng ngày) thay vì một con số cố định dự phóng từ trước. [[Tuckman_Serrat_2022.md#page=65]]

**Worked Example: Cơ chế truyền dẫn dòng tiền khoản vay 3 tháng (90 ngày)**

```text
Trục thời gian:   t=0 (Hôm nay)                            t=1 (Sau 3 tháng)
                   │────────────────────────────────────────│
[Khoản vay LIBOR]  Biết trước L = 5%.                       Trả lãi: Dựa trên mức L tĩnh
(Forward-looking)  Dòng tiền chốt ngay tại t=0.             (Ví dụ: Principal × 5% × 90/360)

[Khoản vay SOFR]   Rate chưa biết. Bắt đầu cộng dồn         Trả lãi: Dựa trên tích phân của
(Backward-looking) SOFR hàng đêm: r_1, r_2, ..., r_90       Π(1 + r_t). Dòng tiền thực tế
                   (Daily Compounding)                      chỉ biết vào ngày cuối cùng.
```

**Hệ quả kỹ thuật:** 
Cấu trúc Backward-looking tước đi khả năng biết trước dòng tiền của doanh nghiệp tại $t_0$, đồng thời tạo ra ma sát lớn trong việc tính toán lãi dồn tích (Accrued Interest) trên thị trường thứ cấp cho các công cụ như trái phiếu thả nổi (FRN).

---

## 3. The Multi-Curve Framework & OIS Discounting

Ranh giới định giá đã thay đổi:
- **The Old World:** Dùng LIBOR để vừa dự báo dòng tiền vừa chiết khấu (Single curve).
- **The New World:** Dùng lãi suất cụ thể (ví dụ SOFR) để dự báo dòng tiền, nhưng **BẮT BUỘC** dùng đường cong **OIS** để chiết khấu.
- **Rationale:** OIS phản ánh chi phí tài trợ thấp nhất (risk-free) của một định chế tài chính có khả năng tiếp cận thị trường qua đêm. [[Tuckman_Serrat_2022.md#page=66]]

---

## 4. Strategic Implications: The Value Shift

Tuckman cảnh báo về ranh giới rủi ro trong quá trình chuyển đổi:
- **Value Transfer:** Khi chuyển một hợp đồng từ LIBOR sang SOFR, vì SOFR thấp hơn LIBOR (do không có rủi ro tín dụng ngân hàng), một bên sẽ bị lỗ cơ học.
- **The Credit Spread Adjustment (CAS):** Để bù đắp, các hợp đồng mới phải cộng thêm một biên độ cố định (thường là trung bình 5 năm của chênh lệch LIBOR-SOFR). [[Tuckman_Serrat_2022.md#page=67]]

---

## Evidence / Source Anchors

- Analysis of OIS discounting as the post-GFC industry standard: [[Tuckman_Serrat_2022.md#page=9]]
- Description of SOFR as a secured rate based on US Treasury repo: [[Tuckman_Serrat_2022.md#page=12]]
- Rationale for the daily compounding of overnight rates (RFRs): [[Tuckman_Serrat_2022.md#page=65]]
- Comparison of credit-sensitive vs. risk-free benchmarks: [[During_Fixed_Income_Ch23.md#page=200]]

## Related

- [[Overnight_Index_Swaps_OIS_Pricing_Dynamics]] — The operational engine of OIS.
- [[Repurchase_Agreement_Mechanism]] — The market that SOFR is built upon.
- [[Risk_and_Valuation_Adjustments_xVA]] — How benchmark reform affects CVA and FVA.
- [[LIBOR_And_Term_Benchmark_Fragility]] — The historical reason for the reform.
