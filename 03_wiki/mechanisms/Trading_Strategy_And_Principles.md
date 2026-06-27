---
title: Trading Strategy and Principles
aliases:
- Trading Principles
- Stop-loss
- Profit target
- Greater fool approach
- Stand-still as a trade
- Trailing Stop-loss
- Nguyên tắc giao dịch
- Trade Rationale
- Stop-loss and Exit Strategy
- Trade Consistency
- Trade Identification
- Nguyên tắc giao dịch trái phiếu
type: mechanism
tags:
- trading-strategies
- risk-management
- fixed-income
- psychology
- behavioral-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens:
- "Alexander Düring"
provenance:
- "Alexander Düring - Fixed Income Trading and Risk Management (2021), Ch30-31"
thesis: Giao dịch là sự nhận thức rủi ro thị trường có chủ đích, được điều hành bởi
  4 trụ cột — Rationale, Profit Target/Stop-loss, Exit Strategy, và Consistency.
  Düring nhấn mạnh rằng kỷ luật nhất quán quan trọng hơn kết quả ngắn hạn; một giao
  dịch có lãi nhưng vi phạm quy trình vẫn là thất bại về mặt hệ thống.
source_refs:
- file: During_Fixed_Income_Ch31.md
  page: 343
- file: During_Fixed_Income_Ch31.md
  page: 344
- file: During_Fixed_Income_Ch31.md
  page: 345
- file: During_Fixed_Income_Ch30.md
  page: 343
- file: During_Fixed_Income_Ch30.md
  page: 345
created: '2026-04-18'
updated: '2026-05-04'
---

# Trading Strategy and Principles

## Định nghĩa tổng quát

Giao dịch không phải là đánh bạc. Düring bóc tách ranh giới: sự khác biệt giữa nhà giao dịch chuyên nghiệp và người may mắn nằm ở **kỷ luật nhất quán (Consistency)**. Ông mở rộng định nghĩa "trade" để bao gồm cả **Stand-still** — quyết định *không* điều chỉnh vị thế khi có thông tin mới cũng là một hành động nhận thức rủi ro chủ động. [[During_Fixed_Income_Ch31.md#page=343]]

---

## 4 Trụ cột của một Trade

> *[[During_Fixed_Income_Ch31.md#page=343]] | [[During_Fixed_Income_Ch30.md#page=343]]*

Mọi vị thế giao dịch phải trả lời được 4 câu hỏi:

1. **Rationale (Lý do):** Tại sao giá sẽ di chuyển theo hướng đó? (Dựa trên mô hình NS, PCA, hay kỳ vọng chính sách?) Đây là bộ lọc phân tách rủi ro có tính toán khỏi cờ bạc.
2. **Profit Target & Stop-loss:** Mục tiêu lợi nhuận là bao nhiêu và khi nào chấp nhận sai để cắt lỗ? → **Trailing Stop-loss:** Nâng dần Stop-loss theo chiều lợi nhuận để "let profits run, cut losses short."
3. **Exit Strategy:** Sẽ thoát vị thế như thế nào? Chi phí thanh khoản khi thoát là bao nhiêu? (Phải đánh giá *trước* khi mở vị thế.) → **Greater Fool Approach:** Chiến lược thoát phi phân tích, giả định có người mua ở giá cao hơn — đặc trưng của giai đoạn cuối bong bóng.
4. **Consistency (Nhất quán):** Các công cụ được chọn có thực sự phản ánh đúng lý luận không?

---

## 4 Bẫy Consistency thường gặp

> *[[During_Fixed_Income_Ch30.md#page=345]]*

- **Model Error:** Dùng mô hình spline tìm rẻ/đắt nhưng mô hình bị lỗi → mua tài sản "rẻ ảo."
- **Basis Risk:** Thực hiện trade bằng Futures để tiết kiệm nhưng không kiểm tra chênh lệch Basis có ổn định không.
- **Sample Bias:** Kết luận nhóm tài sản rẻ nhưng chỉ mua 1 mã duy nhất → gánh idiosyncratic risk thay vì group risk.
- **Carry Bias:** Điều chỉnh trọng số chỉ để có Carry dương → phá hỏng tính trung lập rủi ro ban đầu.

---

## Quản trị vị thế động

> *[[During_Fixed_Income_Ch31.md#page=344]] | [[During_Fixed_Income_Ch30.md#page=344]]*

- **Trailing Stops:** Nâng Stop-loss dần theo lợi nhuận, bảo vệ thành quả.
- **Time Stops:** Nếu trade đi ngang quá lâu, đóng vị thế để giải phóng bảng cân đối cho cơ hội khác — dù chưa chạm Stop-loss hay Target.

---

## Rủi ro thanh khoản tương quan

> *[[During_Fixed_Income_Ch31.md#page=344]]*

Düring cảnh báo: thanh khoản thường **tương quan với kết quả thị trường**. Một trade được thiết kế để bảo vệ trước biến động lớn (ví dụ: long volatility) có thể không thể thoát tại mức giá kế hoạch — vì chính biến động đó khiến bid-offer spread nổ tung hoặc thị trường Repo đóng băng.

---

## Evidence / Source Anchors

- Định nghĩa trade và stand-still: [[During_Fixed_Income_Ch31.md#page=343]], [[During_Fixed_Income_Ch30.md#page=343]]
- Trailing stop-loss logic (Figure 30.1): [[During_Fixed_Income_Ch31.md#page=344]], [[During_Fixed_Income_Ch30.md#page=344]]
- Greater Fool approach và giới hạn của nó: [[During_Fixed_Income_Ch31.md#page=344]], [[During_Fixed_Income_Ch30.md#page=344]]
- 4 bẫy Consistency (Model, Basis, Sample, Carry): [[During_Fixed_Income_Ch30.md#page=345]]
- Tương quan thanh khoản và chi phí ma sát: [[During_Fixed_Income_Ch31.md#page=344]]

## Related

- [[Yield_Curve_Trading_Strategies]]
- [[Basis_Trade_Mechanics]]
- [[PCA_Yield_Curve_Decomposition]]
- [[Bond_Trading_Simplicity_Principle]]
- [[Portfolio_Risk_Budgeting_And_Optimization]]
- [[Bid_Ask_Bounce_Mechanism]]
- [[Statistical_Arbitrage_And_Smart_Beta]]
