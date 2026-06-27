---
title: Information Leakage In Trading
aliases:
- Information Leakage
- Adverse price move
- Information disclosure cost
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch19.md"
thesis: Rò rỉ thông tin (Information Leakage) là hiện tượng ý định giao dịch của nhà
  đầu tư bị thị trường nhận diện trước khi giao dịch được thực hiện xong, dẫn đến
  sự dịch chuyển giá bất lợi (adverse price move). [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=3]]
source_refs:
- file: Fixed_Income_Alexander_During_Ch19.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 18
---

# [[Information_Leakage_In_Trading|information leakage]] In Trading

## Mechanism

Rò rỉ thông tin (Information Leakage) là hiện tượng ý định giao dịch của nhà đầu tư bị thị trường nhận diện trước khi giao dịch được thực hiện xong, dẫn đến sự dịch chuyển giá bất lợi (adverse price move). [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=3]]

### 1. Cơ chế lan truyền
- **Trên [[CLOB_Vs_OTC_Execution|clob]] (Lit markets):** Khi gửi một lệnh lên sàn giao dịch công khai, nhà đầu tư phải công bố (disclose) quy mô và giá. Nếu lệnh này quá lớn và không có lệnh đối ứng ngay lập tức, các thuật toán giao dịch khác sẽ nhận diện "áp lực" mua/bán và đẩy giá đi xa khỏi mức mong đợi của nhà đầu tư đó.
- **Trong RFQ (OTC):** Việc gửi yêu cầu báo giá đến quá nhiều Market Maker cùng lúc ("in competition") cũng tạo ra rò rỉ thông tin. Các Dealer nhận ra có một lệnh lớn đang được chào mời và có thể điều chỉnh giá yết của họ để tự vệ hoặc trục lợi. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=3]]

### 2. Hệ quả kinh tế
Rò rỉ thông tin tạo ra một chi phí ẩn: nhà đầu tư có thể tiết lộ thông tin nhưng cuối cùng **không thực hiện được giao dịch** (failed execution) nếu giá dịch chuyển quá nhanh. Đây là lý do chính khiến các nhà đầu tư tổ chức ưa chuộng các cơ chế thực thi ẩn danh như **[[Dark_Pools]]** hoặc sử dụng các thuật toán chia nhỏ lệnh (algorithmic trading) để che giấu ý định thực sự. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=3-4]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch19.md#page=3]] — Định nghĩa rò rỉ thông tin và sự đánh đổi giữa minh bạch và tác động giá.
