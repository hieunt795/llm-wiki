---
title: Liquidity Search Problem
aliases:
- Search problem
- Combinatorics of liquidity
- Bài toán tìm kiếm thanh khoản
type: concept
tags: []
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: extracted
thesis: Vấn đề thanh khoản về bản chất là một bài toán tìm kiếm (search problem) giữa
  người mua và người bán, bị chi phối bởi tính tổ hợp của số lượng tài sản.
source_refs:
- '[[Fixed_Income_Alexander_During_Ch18.md#page=1]]'
created: '2026-04-16'
updated: '2026-04-16'
chapter: 18
---

# [[Liquidity_Search_Problem]]

## Mechanism

Thanh khoản của một tài sản không chỉ là một con số (như [[Bid_Ask_Bounce|bid-ask spread]]), mà là kết quả của một **Bài toán tìm kiếm (Search Problem)**: Một người bán cần tìm một người mua sẵn lòng cho đúng tài sản đó, tại đúng thời điểm đó, với mức giá sát với chỉ báo thị trường. [extracted] [[Fixed_Income_Alexander_During_Ch18.md#page=1]]

### Quy luật tổ hợp đơn giản
Tính toán tổ hợp (Simple combinatorics) ngụ ý rằng bài toán tìm kiếm sẽ dễ dàng hơn khi:
1. **Số lượng loại tài sản (distinct assets) ít hơn.**
2. **Số lượng người mua tiềm năng lớn hơn.**

### Chiến lược của tổ chức phát hành (Issuers)
Các tổ chức phát hành có thể hỗ trợ thanh khoản bằng cách:
- **Hạn chế số lượng mã chứng khoán:** Thay vì phát hành nhiều mã nhỏ lẻ, họ tập trung vào các mã có khối lượng lớn (large volume securities).
- **Ví dụ về kỳ hạn 100 năm:** Nếu một issuer phát hành trái phiếu 100 năm mới mỗi năm, sau 100 năm họ sẽ có 100 mã khác nhau, làm phân tán thanh khoản. Nếu họ chỉ phát hành các mã 10 năm, mỗi mã có thể lớn gấp 10 lần và do đó thanh khoản hơn nhiều. [extracted] [[Fixed_Income_Alexander_During_Ch18.md#page=1]]
- **Loại bỏ rào cản nhân tạo:** Tránh các ràng buộc phức tạp về lưu ký (custody) và thanh toán (settlement) để thu hút đa dạng nhà đầu tư tham gia.

### Mối quan hệ với các hình thức giao dịch
- **Exchanges ([[CLOB_Vs_OTC_Execution|CLOB]]):** Giải quyết bài toán tìm kiếm bằng cách tập trung đám đông nhà đầu tư vào một địa điểm duy nhất (concentration).
- **Market Making ([[OTC_Vs_Exchange_Trading|OTC]]):** Triệt tiêu bài toán tìm kiếm bằng cách luôn sẵn sàng làm đối tác (willing counterparty), đổi lại là chi phí spread và lợi thế thông tin. [extracted] [[Fixed_Income_Alexander_During_Ch18.md#page=2]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch18.md#page=1-2]] — Phân tích bài toán tìm kiếm trong thanh khoản và chiến lược tập trung mã của issuer.
