---
title: Synthetic Commodities
aliases:
- Commodity Contractual Equation
- Synthetic Long Futures
- Synthetic Spot Commodity
type: concept
tags:
- commodities
- financial-engineering
- replication
- futures
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Commodity futures can be synthetically replicated using spot assets, storage,
  and financing, establishing the 'cost of carry' as the definitive link between spot
  and forward pricing.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 216
created: '2026-05-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Tương tự như ngoại hối và trái phiếu, các công cụ hàng hóa có thể được mô phỏng thông qua **Phương trình Hợp đồng (Contractual Equation)**. Điểm khác biệt cốt yếu là sự xuất hiện của **Chi phí Lưu kho (Storage Costs)** trong cấu trúc dòng tiền.

## 1. The Contractual Equation (Commodities)
[RAW] Một vị thế tương lai (Futures) dài hạn có thể được chế tạo bằng cách kết hợp ba thành phần cơ bản:
- **Spot Operation:** Mua hàng hóa giao ngay tại thời điểm $t_0$.
- **Storage:** Lưu kho hàng hóa đến thời điểm đáo hạn $T$.
- **Loan:** Vay tiền để tài trợ cho việc mua hàng hóa.

### 1.1 Synthetic Long Futures (Equation 7.1)
$$ \text{Long Commodity Futures} = \text{Spot Buy} + \text{Storage Cost} + \text{Loan (Borrowing)} $$

### 1.2 Synthetic Spot (Equation 7.2)
[RAW] Để mô phỏng sở hữu hàng hóa giao ngay mà không cần mua thực tế (hoặc để tách chiết giá trị giao ngay từ hợp đồng tương lai):
$$ \text{Spot Operation} = \text{Long Futures} - \text{Storage Cost} - \text{Loan (Borrowing)} $$
> **Note:** Việc "trừ" đi khoản vay (Loan) tương đương với việc thực hiện một khoản ký gửi/cho vay (Lending/Deposit).

## 2. Pricing & Fair Value
[RAW] Theo nguyên lý No-arbitrage, giá trị của Synthetic phải khớp với giá Futures trên thị trường.

### 2.1 Theoretical Futures Price ($F_{t_0}$)
Nếu chi phí lưu kho ($q$) được tính theo số tiền tuyệt đối mỗi ngày:
$$ F_{t_0} = (1 + r_{t_0} \delta) S_{t_0} + q_{t_0}(T - t_0) $$

Nếu chi phí lưu kho ($q$) được tính theo tỷ lệ phần trăm (giống lãi suất):
$$ F_{t_0} = (1 + r_{t_0} \delta + q_{t_0} \delta) S_{t_0} $$

Trong đó:
- $S_{t_0}$: Giá giao ngay (Spot) tại $t_0$.
- $r_{t_0}$: Lãi suất phi rủi ro (e.g., LIBOR).
- $q_{t_0}$: Chi phí lưu kho (bao gồm bảo hiểm và kho bãi).
- $\delta$: Hệ số điều chỉnh ngày (Day count factor).

## 3. Logic: 'Buy without Buying'
[RAW] Neftci nhấn mạnh logic này như một trong những nguyên lý nền tảng của kỹ thuật tài chính (Financial Engineering).

### 3.1 Definition
[RAW] **'Buy without buying'** (Mua mà không cần mua thực tế) là việc đạt được tỷ suất sinh lời (return) và rủi ro của một tài sản cơ sở mà không cần bỏ ra toàn bộ vốn tự có tại thời điểm $t_0$ hoặc trực tiếp nắm giữ vật chất tài sản đó.

### 3.2 Mechanism in Commodities
- **User Perspective:** Một người tiêu dùng (ví dụ: nhà máy lọc dầu) sử dụng hợp đồng tương lai để "khóa" giá dầu mua trong 12 tháng tới. Họ đạt được mục tiêu "mua" mà không cần thực hiện "Spot operation" hay chi trả "Storage cost" tại thời điểm hiện tại.
- **Financial Engineering:** Thay vì mua dầu thực, người dùng mua một "synthetic asset" được tạo thành từ hợp đồng phái sinh. Việc cấp vốn (funding) và lưu kho thực chất được đẩy sang cho bên trung gian (Bank/Dealer) — những người sẽ thực hiện nghiệp vụ Cash-and-carry để phòng vệ (hedge).
- **Efficiency:** Logic này giúp vị thế trở nên thanh khoản hơn, tránh các rào cản về hạ tầng vật chất và tối ưu hóa việc sử dụng vốn (Leverage).

### 3.3 Alternative Interpretation: Futures as a Synthetic Loan
[RAW] Neftci cung cấp một góc nhìn khác về phương trình Parity (Section 7.3.5):
- **Cost of Position:** Mặc dù không có thanh toán trả trước (upfront), việc mua Futures/Forward không hề "miễn phí".
- **The Interest Wedge:** Nếu giả định chi phí lưu kho bằng 0, sự chênh lệch $P^f_{t_0} - P_{t_0} = r_{t_0} \delta P_{t_0}$ chính là **chi phí tài trợ (financing cost)**.
- **Economic Equivalence:** Việc nắm giữ Futures tương đương với việc vay $P_{t_0}$ đô la trong kỳ hạn $\delta$ để duy trì vị thế Long mà không cần trao đổi gốc (principal).
- **[LLM] F as a Biased Predictor:** Nếu một nhà đầu tư kỳ vọng giá giao ngay không đổi ($E[P_T] = P_{t_0}$), thì giá Futures ($F$) sẽ là một **công cụ dự báo bị chệch (biased predictor)**. Sự chệch này không phải do sai số thị trường mà do thành phần lãi suất rủi ro ($r$) được tích hợp sẵn trong cấu trúc Parity. Để $F$ trở thành dự báo không chệch (unbiased predictor), kỳ vọng lợi nhuận của tài sản phải đúng bằng lãi suất phi rủi ro ($r$).

## 4. Transmission Mechanism (ASCII T-Shape)
[RAW] Luồng truyền dẫn từ Spot sang Futures thông qua bảng cân đối của Dealer:

  [DEALER BALANCE SHEET]
  Assets                  │  Liabilities
  ────────────────────────┼────────────────────────
  (1) + Spot Oil (+St0)   │ (2) + Loan (+St0)  <── (Vay vốn tài trợ)
  (3) + Storage Expense   │ (4) + Short Futures (Hedge)
  (5) Net Profit = F - Carry Cost

  (1) & (2) xảy ra đồng thời để tạo vị thế "Buy without buying" cho khách hàng (người Long Futures).

## 5. Complexity in Replication
[RAW][LLM] Neftci concludes Chapter 7 by emphasizing that commodity replication is structurally more complex than that of homogeneous financial assets:
- **Physical Basis:** Unlike [[Currencies]] or [[Bonds]], commodities require accounting for **Storage Costs** ($q$) which vary by location and time.
- **Heterogeneity:** Grade and quality differences mean that a synthetic position in one grade may not perfectly hedge a futures contract in another, introducing **Basis Risk**.
- **Contractual Parity:** While the *contractual equation* remains the primary tool, the "Interest Wedge" in commodities is heavily influenced by these physical variables.

## Related Concepts
- [[Convenience_Yield]] — Thành phần làm giảm giá Futures trong thị trường Backwardation.
- [[Synthetics_Replicating_Portfolios]] — Nguyên lý tổng quát về chế tạo công cụ tài chính.
- [[Backwardation_And_Contango]] — Các trạng thái của đường cong kỳ hạn.

─────────────────────────────────────────────
WRITEBACK
> SPAWN Synthetic_Commodities.md — Section 7.3.2 Contractual Equation and 'Buy without buying' logic.
- [[Dynamic_Replication_Methods]]
- [[Self_Financing_Portfolio]]
- [[Commodity_Futures_Pricing]]
- [[Commodity_Swap_Engineering]]
- [[Synthetic_Loan_Engineering]]
- [[Binomial_Trees]]
- [[Capital_Controls_Synthetic_Spot]]
- [[Cash_And_Carry_Arbitrage]]
- [[Commodities]]
- [[Japanese_Premium_Synthetic_Loans]]
- [[Model_Risk_And_Jumps]]
- [[Tax_Arbitrage_Synthetic_Bonds]]
- [[Bond_Futures_Pricing_CTD]]
- [[Eurodollar_Futures]]
- [[Basis_Trading_Mechanics_And_Options]]
- [[Forward_Swap_Relative_Value]]
