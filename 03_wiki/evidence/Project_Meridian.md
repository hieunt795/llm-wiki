---
title: Project Meridian
aliases:
- Meridian Project
- RTGS DLT Synchronization
type: evidence
tags:
- monetary-system
- technology
- fx-settlement
- dlt
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: BIS Innovation Hub & Bank of England (2023)
thesis: Dự án Meridian chứng minh rằng các hệ thống RTGS truyền thống có thể đồng
  bộ hóa với các sổ cái tài sản DLT thông qua một lớp vận hành trung gian để thực
  hiện quyết toán tức thời (atomic settlement), giúp giảm rủi ro và chi phí mà không
  cần thay thế hạ tầng cũ.
source_refs:
- file: https://www.bis.org/publ/othp63.pdf
  page: 1
created: '2026-04-13'
updated: '2026-04-22'
---

# Project Meridian

## Mechanism

**Project Meridian** là một sáng kiến thực nghiệm của BIS Innovation Hub phối hợp với Ngân hàng Trung ương Anh (Bank of England), nhằm kiểm tra việc đồng bộ hóa hệ thống thanh toán tức thời (RTGS) với các sổ cái tài sản dựa trên công nghệ sổ cái phân tán (DLT).

Dự án tập trung vào việc giải quyết các điểm nghẽn trong quy trình quyết toán tài sản, nơi các hệ thống tiền tệ và hệ thống tài sản hiện đang tồn tại trong các "ốc đảo" công nghệ riêng biệt.

### Kết quả thực nghiệm

1. **Sychronisation Operator (Nhà vận hành đồng bộ)**: Dự án đã phát triển một thực thể trung gian mới giúp kết nối lệnh thanh toán trên RTGS với lệnh chuyển giao tài sản trên DLT.
2. **Quyết toán đồng thời (Atomic Settlement)**: Chứng minh khả năng thực hiện thanh toán PvP (Payment-versus-Payment) và DvP (Delivery-versus-Payment) một cách tự động, giúp giảm rủi ro settlement và tối ưu hóa thanh khoản. [extracted]
3. **Giảm thiểu trung gian**: Quy trình mới cho phép các bên giao dịch trực tiếp xác thực và thực thi mà không cần qua nhiều lớp hòa giải (reconciliation) thủ công. [extracted]

## Definition
Project Meridian cung cấp minh chứng thực tế rằng các hệ thống ngân hàng truyền thống (RTGS) hoàn toàn có thể "bắt nhịp" với các công nghệ tài sản mới (như nợ tư nhân được mã hóa) thông qua một lớp giao thức đồng bộ hóa, thay vì phải thay thế hoàn toàn hệ thống cũ. [inferred]

### Hình ảnh minh họa (Idea)
> **Cầu nối Kỹ thuật số**: Vẽ hai hòn đảo. Một bên là "Old Financial World" (Hệ thống RTGS cũ). Một bên là "New Asset World" (Mã hóa tài sản). Một cây cầu tên "Meridian Synchroniser" kết nối hai bên, cho phép tiền và tài sản chạy qua lại nhịp nhàng mà không cần đi vòng qua các con tàu trung gian (Correspondent Banks).

## Evidence / Source Anchors
- [extracted] [BIS Innovation Hub, "Project Meridian: London Centre", 2023](https://www.bis.org/publ/othp63.htm)
- [researched] [Bank of England, "RTGS Renewal Programme", 2024](https://www.bankofengland.co.uk/payment-and-settlement/rtgs-renewal-programme)


## Related

- [[Tokenized_Monetary_System]]
- [[Cryptocurrencies]]
