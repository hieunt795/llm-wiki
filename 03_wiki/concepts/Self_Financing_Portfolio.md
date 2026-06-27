---
title: Self-Financing Portfolio
aliases:
- Self-Financing Constraint
- No-Injection Rule
type: concept
tags:
- financial-engineering
- portfolio-theory
- replication
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: A portfolio is self-financing if its value changes only due to changes in
  asset prices, with no external cash injections or withdrawals after the initial
  setup cost.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 240
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Một danh mục được gọi là tự cấp vốn (self-financing) nếu sau khi thiết lập vị thế ban đầu tại $t_0$, kỹ sư tài chính không bao giờ phải bơm thêm tiền ($\Delta B > 0$) hoặc rút tiền ra ($\Delta B < 0$) để duy trì chiến lược cho đến khi đáo hạn. Mọi thay đổi về giá trị danh mục chỉ đến từ biến động giá của các tài sản thành phần.

## 1. The Mathematical Constraint
[RAW] Giả sử danh mục gồm $n$ tài sản với số lượng $w_i$ và giá $P_i$. Điều kiện self-financing trong thời gian liên tục là:
$$dV_t = \sum_{i=1}^n w_{it} dP_{it}$$
Trong đó $V_t$ là giá trị danh mục. Phương trình này ngụ ý rằng không có dòng tiền từ bên ngoài tác động vào $V_t$.

## 2. In Static Replication
[RAW] Trong mô phỏng tĩnh (Static Replication), các trọng số $w_i$ được cố định tại $t_0$ và giữ nguyên đến $T$.
- Tính chất self-financing được đảm bảo một cách tự nhiên nếu dòng tiền tại $T$ khớp hoàn toàn.
- Nếu xuất hiện nhu cầu điều chỉnh (e.g., rollover rủi ro lãi suất), tính chất này sẽ bị phá vỡ trừ khi có các công cụ kỳ hạn (forwards) để khóa trước dòng tiền.

## 3. In Dynamic Replication (Discrete Time)
[RAW] Trong mô hình thời gian rời rạc (như cây nhị thức), tính chất self-financing yêu cầu rằng tại mỗi thời điểm tái cân bằng $j+1$, giá trị của danh mục cũ (thiết lập tại $j$) phải bằng đúng chi phí thiết lập danh mục mới (tại $j+1$):

$$ \theta_j^{lend} B_{j+1}^i + \theta_j^{bond} B(j+1, 3)^i = \theta_{j+1}^{lend} B_{j+1}^i + \theta_{j+1}^{bond} B(j+1, 3)^i $$

Với $i \in \{up, down\}$ là trạng thái thị trường. Điều này đảm bảo rằng bất kể thị trường biến động thế nào, danh mục hiện tại luôn tạo ra vừa đủ tiền để thực hiện các điều chỉnh cần thiết mà không cần vốn bên ngoài.

### 3.1 Transmission Mechanism (Cơ chế truyền dẫn dòng tiền)
[RAW] Biến đổi phương trình trên cho thấy cơ chế bù trừ dòng tiền giữa các tài sản:
$$ (\theta_j^{lend} - \theta_{j+1}^{lend}) B_{j+1}^i = - (\theta_j^{bond} - \theta_{j+1}^{bond}) B(j+1, 3)^i $$
- **Ý nghĩa:** Số tiền thu được từ việc điều chỉnh tỷ trọng của công cụ này (ví dụ: bán bớt trái phiếu) phải khớp chính xác với số tiền cần thiết để điều chỉnh công cụ kia (ví dụ: tăng tài khoản tiền gửi).
- **Lưu ý:** Cơ chế này hoạt động ngay cả khi các mức giá $B_{j+1}^i$ là ngẫu nhiên, miễn là các tài sản có sự tương quan hệ thống (perfectly correlated trong mô hình 1-factor). [[Principles_of_Financial_Engineering_Neftci.md#page=255]]

## 4. Failure Example: The Missing Asset
[RAW] Khi cố gắng mô phỏng một trái phiếu 2 kỳ hạn bằng tài khoản tiền gửi 1 kỳ hạn (rollover strategy) mà không có Forward:
- Tại $t_1$, nếu lãi suất thực tế khác với dự tính, ta buộc phải bơm thêm tiền $\Delta B$ để đảm bảo nhận được đúng số tiền mục tiêu tại $t_2$.
- Hành động này biến chiến lược thành **Non-self-financing**, làm cho việc định giá tại $t_0$ trở nên bất khả thi vì chi phí thực tế không được xác định trước. [[Principles_of_Financial_Engineering_Neftci.md#page=243]]

## 5. The Result: Sequence of Weights (Section 8.8)
[RAW] Neftci kết luận rằng một synthetic động thực chất là một **chuỗi các trọng số** $\{\theta_1, \theta_2, \dots, \theta_n\}$ được xác định tại mỗi thời điểm tái cân bằng.
- Mục tiêu của chuỗi này là đảm bảo tại mọi nút, giá trị của danh mục cũ vừa đủ để tài trợ cho việc thiết lập danh mục mới.
- Điều này chuyển đổi bản chất của synthetic từ một danh mục tài sản cố định sang một **thuật toán** (algorithm) tự điều chỉnh để duy trì tính trung lập với rủi ro và tự túc về vốn.

## Related
- [[Synthetics_Replicating_Portfolios]] — Khung lý thuyết tổng quát.
- [[Dynamic_Replication_Methods]] — Phương pháp triển khai chuỗi trọng số self-financing.
- [[Delta_Hedging]] — Ứng dụng phổ biến nhất của self-financing trong Dynamic Replication.
