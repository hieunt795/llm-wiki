---
title: IMM Dates And Tick
aliases:
- IMM Days
- IMM Dates
- Tick
- Tick size
- Ngày đáo hạn chuẩn
type: definition
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch14.md"
thesis: '**IMM Dates** là 4 ngày cố định mỗi năm mà hầu hết hợp đồng phái sinh lãi
  suất trên toàn cầu chọn làm ngày khởi đầu hoặc đáo hạn chuẩn. [extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=10-11]]'
source_refs:
- file: Fixed_Income_Alexander_During_Ch14.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 13
---

# [[IMM_Dates_And_Tick]]

## Definition

### IMM Dates (International Monetary Market Dates)
**IMM Dates** là 4 ngày cố định mỗi năm mà hầu hết hợp đồng phái sinh lãi suất trên toàn cầu chọn làm ngày khởi đầu hoặc đáo hạn chuẩn. [extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=10-11]]

- Quy ước: **Thứ Tư thứ 3** của tháng 3, 6, 9a, 12 (tức March, June, September, December).
- Tên gọi xuất xứ từ **International Monetary Market** — sàn giao dịch tương lai tài chính đầu tiên thuộc CME (Chicago Mercantile Exchange).
- Tất cả [[Money_Market_Futures]] (Eurodollar, Euroyen, [[OIS_And_Benchmark_Reform|sofr]] Futures...) đều đáo hạn vào IMM dates.
- Các hợp đồng [[Forward_Rate_Agreement|FRA]] cũng thường lấy IMM dates làm mốc quy chiếu.

Sự tập trung thanh khoản vào đúng 4 ngày này tạo ra hiệu ứng "cả thế giới cùng đáo hạn một lúc" — giúp tối đa hóa [[Interbank_Netting|bù trừ]] nhưng cũng tạo ra áp lực thanh khoản cục bộ cực lớn.

### [[US_Thirty_Seconds_Quotation|tick]] (Đơn vị nhảy giá nhỏ nhất)
**Tick** (hay tick size) là bước nhảy giá tối thiểu mà một hợp đồng tương lai được phép dao động. [extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=11]]

- Đối với [[Money_Market_Futures|Eurodollar Futures]] (notional $1M, kỳ hạn 3 tháng): **1 tick = 0.5 bp = $12.50**.

  Công thức: $1{,}000{,}000 \times 0.00005 \times \frac{90}{360} = \$12.50$

- Đối với **Eurex Bund Future** (FGBL, notional €100,000): **1 tick = 0.01 giá = €10**.
- Giá trị tick (tick value) là con số **Gamma ẩn** — vì nó cho biết PnL tức thì khi thị trường nhích 1 đơn vị nhỏ nhất. Trader thường đo rủi ro bằng "bao nhiêu tick" thay vì bằng đô la tuyệt đối.

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch14.md#page=10-12]] — Quy ước IMM dates (3rd Wednesday), cấu trúc tick value của Eurodollar và Eurex Bund futures.
