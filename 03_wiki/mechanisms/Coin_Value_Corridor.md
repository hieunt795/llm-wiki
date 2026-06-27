---
title: Coin Value Corridor
aliases: []
type: mechanism
tags:
- history
- money
- arbitrage
status: archived
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Hành lang giá trị tiền xu (Coin Value Corridor) là ranh giới kinh doanh chênh
  lệch giá được xác định bởi giá trị kim loại nội tại, chi phí đúc/nấu chảy và lợi
  nhuận phát hành (seigniorage), ngăn chặn việc tiêu hủy hoặc đúc tiền trái phép trong
  các hệ thống tiền tệ dựa trên kim loại.
source_refs:
- file: During_Fixed_Income_Ch02.md
  page: 4
created: '2026-04-13'
updated: '2026-04-22'
---

> [!info] **Bản lưu trữ vĩ mô/vi mô**
> Nội dung này đã được hợp nhất và nâng cấp độ phân giải tại [[Interest_Rate_Corridor_And_Standing_Facilities]]. Bạn đang xem bản chi tiết của nguồn gốc.


# Coin Value Corridor

## Cơ chế

Giá trị $V$ của một đồng tiền xu (coin) bị ràng buộc trong một **corridor** xác định bởi: [extracted] [[Fixed Income - Alexander During-3.pdf#page=4]]

$$V_i - V_m \leq V \leq V_i + V_M + S$$

Trong đó:
- $V_i$ = Giá trị kim loại nội tại (inherent metal value)
- $V_m$ = Chi phí nấu chảy (melting cost)
- $V_M$ = Chi phí đúc (minting cost)
- $S$ = [[Seigniorage]]

### Arbitrage mechanism

- Nếu coin **giao dịch dưới** cận dưới ($V_i - V_m$): thương lái kim loại phế liệu sẽ **nấu chảy** coin → thu lợi
- Nếu coin **giao dịch trên** cận trên ($V_i + V_M + S$): sẽ hấp dẫn để **đúc tiền mới** từ kim loại

[extracted] [[Fixed Income - Alexander During-3.pdf#page=4-5]]

### Kỹ thuật phá corridor (qua debasement)

- **Sovereign:** Cố tình đưa coin độ tinh khiết thấp hơn → **debasement** → thường dẫn đến inflation
- **Private forgers:** Clipping (cắt rìa coin), giảm trọng lượng coin so với mệnh giá
- **Phòng thủ:** Sir Isaac Newton phát minh **rolling coins** (cạnh có rãnh) để chống clipping

[extracted] [[Fixed Income - Alexander During-3.pdf#page=5]]

## Điều kiện

- Coin phải có thể nấu chảy thành kim loại và đúc lại
- Seigniorage phải do sovereign kiểm soát
- Equation (2.1) trong sách gốc

## Ví dụ số

Xem Equation 2.1 trong sách. [extracted] [[Fixed Income - Alexander During-3.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-3.pdf#page=4]] — Equation 2.1 + arbitrage
- [[Fixed Income - Alexander During-3.pdf#page=5]] — Debasement, clipping, Newton
