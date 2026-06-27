---
title: Commodity Futures Pricing
aliases:
- Backwardation
- Contango
- Convenience Yield
- Synthetic Commodity
- Spot-Futures Parity
type: mechanism
tags:
- commodities
- futures
- valuation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Salih Neftci - Principles of Financial Engineering (2008)
thesis: Định giá hợp đồng tương lai hàng hóa dựa trên nguyên tắc kinh doanh chênh
  lệch giá (no-arbitrage), được xác định bởi mối quan hệ giữa giá giao ngay, chi phí
  nắm giữ (lãi suất và lưu kho) và lợi suất tiện ích (convenience yield) phát sinh
  từ việc sở hữu vật chất.
source_refs:
- file: Neftci_Principles.md
  page: 215-221
created: '2026-04-16'
updated: '2026-04-22'
---

# Commodity Futures Pricing

## Term Structure: Backwardation vs. Contango
Hình thái của đường cong giá tương lai (Futures Curve) phản ánh sự cân bằng cung cầu và chi phí nắm giữ hàng hóa vật chất. [[Neftci_Principles#page=215]]

### 1. Backwardation (Bù hoãn bán)
Xảy ra khi giá tương lai $F < S$ (giá giao ngay). Đường cong dốc xuống (downward sloping).
- **Basis:** Dương ($S - F > 0$).
- **Nguyên nhân:** Thiếu hụt nguồn cung vật chất tức thời hoặc nhu cầu tiêu thụ hiện tại cực cao.
- **Biểu đồ ASCII:**
  Price
  ^
  │ S
  │  \
  │   \  F(t1)
  │    \    F(t2)
  │     \      F(tn)
  └──────────────────> Time (Maturity)

### 2. Contango (Bù hoãn mua)
Xảy ra khi giá tương lai $F > S$. Đường cong dốc lên (upward sloping).
- **Basis:** Âm ($S - F < 0$).
- **Nguyên nhân:** Cung vượt cầu, chi phí lưu kho và lãi suất cao.
- **Biểu đồ ASCII:**
  Price
  ^
  │              F(tn)
  │          F(t2)
  │      F(t1)
  │  S
  └──────────────────> Time (Maturity)

## Contractual Equation & Replication
Việc định giá dựa trên nguyên lý không có chênh lệch giá (No-arbitrage). [[Neftci_Principles#page=217]]

### 1. Synthetic Long Futures (Hợp đồng tương lai tổng hợp)
Công thức:
$$Long\ Futures = Buy\ Spot\ (S) + Store\ (q) + Borrow\ Cash\ (r)$$
- **Carry Cost (Chi phí nắm giữ):** Tổng của lãi suất (r) và chi phí lưu kho (q).

### 2. Synthetic Spot (Hàng giao ngay tổng hợp)
Rearranging Eq 7.1 allows for the creation of a synthetic spot position using futures:
$$Synthetic\ Spot = Long\ Futures - Store\ (q) - Loan\ (r)$$
[LLM] Cơ chế này cho phép các thực thể (như ngân hàng) "sở hữu" hàng hóa mà không cần kho bãi vật chất ngay lập tức, bằng cách kết hợp vị thế phái sinh và tài trợ vốn.

### Pricing Formula (Spot-Futures Parity)
1.  **Chi phí lưu kho tuyệt đối (q):**
    $$F_{t_0} = (1 + r \delta) S_{t_0} + q(T - t_0)$$
2.  **Chi phí lưu kho theo tỷ lệ (%) (q):**
    $$F_{t_0} = S_{t_0} (1 + r \delta + q \delta)$$ [[Neftci_Principles#page=218]]

## Convenience Yield (Lợi suất tiện ích)
[RAW][LLM] Lợi suất tiện ích ($cy$) là lợi ích phi tiền tệ từ việc sở hữu vật chất hàng hóa (ví dụ: tránh rủi ro đứt gãy sản xuất). Đây là "nút thắt" giải thích tại sao thị trường rơi vào trạng thái Backwardation. Xem chi tiết tại: [[Convenience_Yield]].

**Cơ chế truyền dẫn (Inventory-to-Yield):**
- **Scarcity (Khan hiếm):** Khi tồn kho thấp (low inventory), rủi ro stockout tăng cao, đẩy $cy$ lên mạnh.
- **Abundance (Dư thừa):** Khi cung cầu cân bằng hoặc dư thừa, $cy$ giảm dần về 0.

**Mô hình mở rộng (Extended Equation):**
$$F_{t_0} = (1 + r \delta) [S_{t_0} + q(T - t_0) - cy]$$
- Nếu $cy > r + q$, thị trường sẽ ở trạng thái **Backwardation**. [[Neftci_Principles#page=219]]


## Worked Example: Heating Oil (JPMorgan 2009)
[RAW] Phân tích cơ chế Cash and Carry trong trạng thái Contango mạnh:
- **Spot Price:** $150.969M (273k tấn @ $553).
- **Borrowing (1%):** $1.509M.
- **Insurance (0.25%):** $0.377M.
- **Shipping (Singapore -> EU):** $1.600M.
- **Storage ($3.85/tấn):** $1.051M.
- **Total Cost:** $155.507M.
- **Futures Revenue ($580/tấn):** $158.340M.
- **Net Profit:** $2.833M. [[Neftci_Principles#page=221]]

## Tracking Storage Costs ($q$)
[WEB][LLM] Chi phí lưu kho không cố định mà biến động theo cung cầu hạ tầng. Có hai phương pháp theo dõi:

### 1. Chỉ số theo dõi trực tiếp (Direct/Hard Costs)
- **BDTI (Baltic Dirty Tanker Index):** Dùng cho dầu thô. Khi kho trên cạn đầy, giá thuê tàu làm "kho nổi" tăng vọt, phản ánh rủi ro Contango mạnh.
- **LME Official Warehouse Rates:** Bảng phí lưu kho hàng ngày do sàn Kim loại Luân Đôn công bố cho mạng lưới kho toàn cầu.
- **FRED PPI - Warehousing (WPU32110101):** Chỉ số giá sản xuất vĩ mô cho dịch vụ kho bãi, dùng để track xu hướng chi phí logistics dài hạn.

### 2. Chỉ số ngụ ý từ thị trường (Market-Implied Index)
- **Calendar Spreads:** Chênh lệch giữa $F_{t+1}$ và $S$. Nếu spread vượt quá lãi suất phi rủi ro ($r$), phần dư thừa chính là mức phí lưu kho mà thị trường đang sẵn sàng chi trả.
- **Shadow Index:** $q_{implied} \approx \frac{F - S}{S} - r$.

## Failure Conditions & Transmission Risks
[LLM][RAW] Cơ chế truyền dẫn giá giữa Spot và Futures có thể đứt gãy do:
1.  **Physical Bottlenecks:** Kho bãi đầy (onshore tanks full) buộc phải dùng kho nổi (tankers) với chi phí biến động cực lớn.
2.  **Supply/Demand Imbalance:** Khi nhu cầu thực tế vượt xa khả năng cung ứng tức thời, $cy$ tăng vọt, phá vỡ liên kết arbitrage thuận (Cash and Carry).
3.  **Counterparty/Default Risk:** Dù không trao đổi gốc (no exchange of principals), rủi ro vỡ nợ vẫn tồn tại trong việc thanh toán chênh lệch giá (variation margin). [[Neftci_Principles#page=221]]

## Spot-Futures Parity Interpretation
Mua Futures thực chất không "miễn phí". Chênh lệch $(F - S)$ chính là chi phí vốn (cost of carry) ẩn. Long Futures tương đương với việc vay tiền để mua hàng ngay bây giờ và nắm giữ đến tương lai. [[Neftci_Principles#page=221]]

## Evidence / Source Anchors
- [[Neftci_Principles.md#page=215-221]] — Phân tích chi tiết về cấu trúc kỳ hạn, phương trình hợp đồng và Convenience Yield.
