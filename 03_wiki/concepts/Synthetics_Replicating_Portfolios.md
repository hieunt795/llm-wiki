---
title: Synthetics & Replicating Portfolios
aliases:
- Synthetic Instrument
- Replicating Portfolio
- Static Replication
type: concept
tags:
- financial-engineering
- pricing
- replication
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: A synthetic is engineered by forming a portfolio of simple, liquid instruments
  that exactly replicate the cash flows of a complex target instrument, serving as
  the foundational logic for pricing and risk management.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 55
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Nguyên lý của Synthetics là "chia để trị": Biến một công cụ phức tạp, khó định giá thành một tổ hợp các công cụ đơn giản, thanh khoản cao. Nếu dòng tiền của hai bên khớp nhau hoàn toàn, giá của chúng phải bằng nhau (No-arbitrage).

## 1. Core Logic: The Contractual Equation
[RAW] Mọi công cụ tài chính đều có thể được biểu diễn bằng một phương trình đại số của các dòng tiền.
- **Example:** $A = B + C$
- Nếu ta muốn sở hữu đặc tính của $A$ nhưng thị trường $A$ kém thanh khoản hoặc bị hạn chế, ta có thể "chế tạo" $A$ bằng cách mua $B$ và $C$.

### The 4-Step General Engineering Methodology (Neftci)
[RAW] Salih Neftci đề xuất một quy trình 4 bước chuẩn hóa để "chế tạo" bất kỳ công cụ tài chính tuyến tính (linear instrument) nào:

1.  **Step 1 (Cash Flow Visualization):** Bắt đầu bằng việc vẽ sơ đồ dòng tiền (Cash flow diagram) của công cụ mục tiêu.
2.  **Step 2 (Detachment):** Tách (detach) các thành phần dòng tiền (ví dụ: chân thu và chân chi) thành các sơ đồ độc lập. Tại bước này, các sơ đồ rời rạc thường không đại diện cho các công cụ có thể giao dịch được (tradeable).
3.  **Step 3 (Normalization via Insertion):** Thêm và bớt (Add and subtract) các dòng tiền mới tại các thời điểm được chọn (thường là $t_0$) để biến các sơ đồ rời rạc thành các hợp đồng tài chính có ý nghĩa (e.g., loans, deposits, spot trades) mà thị trường sẵn sàng giao dịch.
4.  **Step 4 (Vertical Verification):** Đảm bảo rằng khi cộng tất cả các sơ đồ mới lại theo chiều dọc (vertically), các dòng tiền "thêm vào" ở Step 3 sẽ triệt tiêu lẫn nhau (cancel out) và sơ đồ dòng tiền gốc được khôi phục hoàn toàn. [[Principles_of_Financial_Engineering_Neftci.md#page=179]]

## 2. Taxonomy of Replication (Neftci)
Replication được phân loại dựa trên đặc tính của dòng tiền và tần suất điều chỉnh vị thế:

### 2.1 Static Replication (Review)
[RAW] Thiết lập vị thế tại $t_0$ và giữ nguyên đến khi đáo hạn $T$.
- **Quy trình 3 bước (Standard Review):**
    1. **Visualize:** Vẽ dòng tiền của tài sản mục tiêu.
    2. **Decompose/Reconstruct:** Tách dòng tiền và tái cấu trúc bằng các tài sản thanh khoản sao cho tổng dòng tiền theo chiều dọc khớp hoàn toàn với mục tiêu.
    3. **Credit Risk Matching:** Đảm bảo rủi ro tín dụng của các thành phần tương đương với tài sản mục tiêu.
- **Đặc tính cốt lõi:**
    - **No Rebalancing:** Không điều chỉnh tỷ trọng danh mục sau khi đã thiết lập tại $t_0$.
    - **Self-Financing:** Không yêu cầu bơm thêm tiền ($\Delta B = 0$) hoặc rút tiền ra trong suốt vòng đời.
    - **No-Arbitrage Price:** Giá trị của Synthetic tại $t_0$ phải khớp với giá thị trường của tài sản mục tiêu.

### 2.2 The "Missing Asset" Problem & Transition to Dynamic
[RAW] Trong thực tế, static replication thường thất bại khi thị trường thiếu các công cụ bắc cầu (e.g., Forward Rate Agreements - FRAs). Neftci sử dụng khung phân tích sau để minh chứng:

**The Framework:**
- **Thanh khoản:** Chỉ có $B_t$ (tài khoản tiền gửi 1 kỳ hạn) và $B(t, T)$ (trái phiếu chiết khấu kỳ hạn $T$) là thanh khoản.
- **Thiếu hụt:** Không có thị trường kỳ hạn (Forwards) hoặc các kỳ hạn trung gian.

**Failure Cases:**
1. **Rollover Strategy (Dùng $B_t$):** Để tạo $B(t_0, T_2)$ bằng cách gửi tiết kiệm và đáo hạn (roll over) tại $t_1$. Vì lãi suất $L_{t_1}$ tại $t_1$ chưa biết ở $t_0$, ta không thể xác định số vốn cần đầu tư ban đầu để có đúng 100 tại $t_2$. Việc bù đắp thiếu hụt tại $t_1$ vi phạm tính chất *Self-financing*.
2. **Long Bond Only (Dùng $B(t_0, T_3)$):** Để tạo $B(t_0, T_2)$ bằng trái phiếu dài hơn sẽ để lại dòng tiền "thừa" tại $T_3$ mà không thể triệt tiêu một cách tĩnh tại $t_0$.

**Conclusion:** Khi tài sản "bắc cầu" bị thiếu, Static Replication không còn khả thi, buộc kỹ sư tài chính phải sử dụng **Dynamic Replication** (điều chỉnh tỷ trọng liên tục) để mô phỏng dòng tiền mục tiêu. [[Principles_of_Financial_Engineering_Neftci.md#page=242]]

### 2.3 "Ad Hoc" Synthetics (Approximate Replication)
[RAW] Khi dynamic replication quá phức tạp hoặc chưa được thiết lập hoàn chỉnh, kỹ sư tài chính có thể sử dụng các giải pháp "ad hoc" — ít chính xác hơn nhưng thực dụng.

**Đặc tính:**
- **Sensitivity Matching:** Tạo danh mục có cùng các độ nhạy (sensitivities) với tài sản mục tiêu tại một thời điểm nhất định (ví dụ: khớp Duration nhưng bỏ qua Convexity).
- **Static-Dynamic Hybrid:** Bắt đầu bằng một thiết lập tĩnh tại $t_0$ dựa trên các partial derivatives, nhưng yêu cầu điều chỉnh (rebalancing) khi các biến số rủi ro (risk factors) thay đổi.
- **Non-Self-Financing:** Khác với dynamic replication chính xác, các chiến lược ad hoc thường yêu cầu bơm/rút tiền mặt (cash injections/withdrawals) tại các thời điểm tái cân bằng.
- **Example:** [[Immunization]] của danh mục trái phiếu.

## 3. Dynamic Replication
[RAW] Khi static replication thất bại do thiếu hụt thị trường, tính thanh khoản kém hoặc tính phi tuyến (convexity), kỹ sư tài chính phải sử dụng phương pháp điều chỉnh vị thế liên tục.

Xem chi tiết tại: [[Dynamic_Replication_Methods]]

## 4. Worked Example: Synthetic Bond
[RAW] Tạo một trái phiếu USD tổng hợp từ thị trường tiền tệ:
- **Target:** Một trái phiếu trả lãi cố định.
- **Constituents:** Một chuỗi các khoản vay lãi suất nổi (LIBOR loans) kết hợp với các hợp đồng hoán đổi lãi suất (IRS) hoặc FRA.
- **Mechanism:** Dùng FRA để "chốt" lãi suất cho từng kỳ hạn của khoản vay nổi, biến toàn bộ dòng tiền thành cố định.

## 4. Failure Conditions / Boundaries
- **Basis Risk:** [RAW] Nếu các thành phần của danh mục mô phỏng không khớp hoàn hảo với tài sản mục tiêu (e.g., khác biệt về ngày thanh toán, Credit rating), rủi ro basis sẽ phát sinh.
- **Transaction Costs:** Chi phí giao dịch của nhiều thành phần có thể làm cho việc nắm giữ synthetic đắt hơn tài sản gốc.
- **Liquidity Mismatch:** Khả năng thanh lý các thành phần trong danh mục mô phỏng có thể không đồng nhất.

## Related
- [[Synthetic_Loan_Engineering]] — Ứng dụng cụ thể trong thị trường FX.
- [[Forward_Rate_Agreements_FRA]] — Công cụ xây dựng synthetic bond.
- [[Interest_Rate_Swap_Engineering]] — Ứng dụng của nguyên lý cộng dồn dòng tiền.
