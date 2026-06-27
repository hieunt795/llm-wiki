---
title: Price Quantization Noise
aliases:
- Price quantization
- Tick size noise
- Minimum price gradations
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
thesis: Nhiễu lượng tử hóa (Quantization noise) phát sinh từ việc các mức giá trên
  thị trường bị giới hạn bởi các bước giá tối thiểu ([[US_Thirty_Seconds_Quotation|tick]]
  sizes), làm sai lệch việc đo lường chênh lệch mua-bán thực tế. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=7]]
source_refs:
- file: Fixed_Income_Alexander_During_Ch19.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 18
---

# Price Quantization Noise

## Mechanism

Nhiễu lượng tử hóa (Quantization noise) phát sinh từ việc các mức giá trên thị trường bị giới hạn bởi các bước giá tối thiểu ([[US_Thirty_Seconds_Quotation|tick]] sizes), làm sai lệch việc đo lường chênh lệch mua-bán thực tế. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=7]]

### 1. Cơ chế giới hạn (Lower Bound)
- Trên thị trường Trái phiếu Kho bạc Hoa Kỳ (US Treasuries), quy ước báo giá theo bước 1/256 tạo ra một mức sàn cứng (effective lower bound) cho bid-offer spread. Ngay cả khi thanh khoản cực tốt, spread cũng không thể nhỏ hơn một "tick".
- Điều này có nghĩa là spread quan sát được trên màn hình có thể rộng hơn mức spread mà các bên thực sự sẵn lòng giao dịch nếu họ được phép báo giá tự do. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=8]]

### 2. So sánh đa quốc gia
Cấu trúc bước giá ảnh hưởng trực tiếp đến dữ liệu thanh khoản:
- **Mỹ:** [[IMM_Dates_And_Tick|tick size]] 1/256 (~0.04 bps yield) tạo ra ranh giới lượng tử hóa rõ rệt.
- **Châu Âu:** Thường báo giá theo bước 1/1,000 (0.1 cents), dẫn đến độ phân giải giá cao hơn và nhiễu lượng tử hóa thấp hơn so với thị trường Mỹ, mặc dù thanh khoản thực tế có thể kém hơn. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=8]]

Khi phân tích thanh khoản, nhà đầu tư cần tách biệt phần spread do rủi ro/thanh khoản và phần spread do ràng buộc kỹ thuật của bước giá. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=7]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch19.md#page=7-8]] — Tác động của [[Price_Quantization_Noise|minimum price gradations]] lên việc đo lường thanh khoản.
