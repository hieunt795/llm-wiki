---
title: Private Credit Valuation and Mark-to-Model
aliases:
- Mark-to-Model
- Stale Valuations
- Fair Value
- Valuation Smoothing
type: mechanism
tags:
- private-credit
- accounting
- valuation
- volatility
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: Do các khoản vay [[Private_Credit]] hiếm khi được giao dịch công khai, việc
  xác định giá trị của chúng không dựa trên giá thị trường (Mark-to-Market) mà dựa
  trên các mô hình tài chính (**Mark-to-Model**) và đánh giá chuyên gia (Fair Value).
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: Deep Dive_ Private Credit.md
---

# Private Credit Valuation and Mark-to-Model

## Mechanism

Do các khoản vay [[Private_Credit]] hiếm khi được giao dịch công khai, việc xác định giá trị của chúng không dựa trên giá thị trường (Mark-to-Market) mà dựa trên các mô hình tài chính (**Mark-to-Model**) và đánh giá chuyên gia (Fair Value).

> [!IMPORTANT]
> Câu hỏi chuyên môn sạch sẽ nhất hiện nay là liệu **độ biến động thấp (low volatility)** là đặc tính của việc thẩm định tốt hay là hệ quả của việc **trì hoãn khám phá giá (delayed price discovery)**. [extracted]

### Quy trình định giá

1. **Sử dụng Proxy**: Dựa trên các chỉ số thị trường có tính thanh khoản cao như các khoản vay hợp vốn (syndicated loans) hoặc trái phiếu lợi suất cao (high-yield bonds) để suy luận sự thay đổi điều kiện thị trường. [extracted]
2. **Đánh giá Công ty (Borrower)**: Theo dõi chất lượng tín dụng, tỷ lệ bao phủ lãi suất (ICR) và tiến độ kinh doanh của doanh nghiệp đi vay. [inferred]
3. **Third-party Pricing**: Thuê các dịch vụ định giá độc lập để cung cấp chứng chỉ giá trị hàng quý. [extracted]

### Rủi ro và Lợi thế

- **Smoothing (Làm mượt)**: Việc định giá theo mô hình cho phép các quỹ "làm mượt" biến động, giảm bớt áp lực tâm lý cho nhà đầu tư định kỳ. [extracted]
- **Discretion (Tùy ý)**: Tính thiếu minh bạch tạo không gian cho sự tùy ý của người quản lý trong việc duy trì mức định giá cao và trì hoãn ghi nhận các khoản lỗ thực tế. [extracted]
- **Stale Valuations (Định giá lỗi thời)**: Trong bối cảnh lãi suất tăng nhanh, các mô hình định giá có thể không phản ánh kịp thời sự suy giảm giá trị thực tế của khoản vay. [extracted]

> [!WARNING]
> Trong các đợt căng thẳng thị trường kéo dài, việc định giá lỗi thời sẽ dẫn đến sự tích tụ lỗ và bùng phát bất ngờ thông qua làn sóng vỡ nợ (default spikes) hoặc hạ giá hàng loạt (valuation markdowns). [extracted]

### Hình ảnh minh họa (Idea)

> **Volatility Comparison Chart**: Vẽ hai đường diễn biến giá. Đường 1 (Răng cưa mạnh): Syndicated Loan Index (Mark-to-Market). Đường 2 (Tương đối thẳng, trễ hơn): Private Credit Portfolio (Mark-to-Model). Minh họa vùng khoảng cách giữa hai đường (Label: "Valuation Gap / Smoothing Buffer"). Thêm một điểm rơi mạnh (Label: "Loss Realization Cliff") khi Mark-to-Model bị buộc phải điều chỉnh theo thực tế. [inferred]

## Evidence / Source Anchors

- [extracted] Arya Deniz, *Deep Dive: Private Credit*, Substack, 2026-04-07
- [extracted] Kroll, "Valuation Insights H1 2024" (Fair value best practices)
- [extracted] IMF GFSR, April 2024 (Opacity and delayed loss realization)
- [extracted] FSOC Annual Report 2024 (Incentives for high valuations)

### Liên kết

- [[Private_Credit]] — bối cảnh mẹ
- [[Direct_Lending]] — đối tượng chính của cơ chế định giá này
- [[Payment_In_Kind_PIK]] — công cụ giúp duy trì NAV ổn định mặc dù có stress thanh khoản
- [[Private_Credit_Secondary_Market]] — nơi khám phá giá thực tế thách thức các mô hình định giá
- [[Business_Development_Company]] — nơi NAV công bố hàng quý là yếu tố quyết định giá trị cổ phần
