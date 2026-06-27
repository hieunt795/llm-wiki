---
title: Asymmetric Lending Corridor
aliases:
- Floor System
- QE Pinned Rates
- Overnight Reverse Repo ON RRP
type: mechanism
tags:
- monetary-policy
- central-banking
- liquidity
- corridor-system
status: archived
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Sau kỷ nguyên QE, thanh khoản thặng dư khổng lồ khiến lãi suất thị trường
  bị ghim chặt vào cận dưới của hành lang lãi suất (Floor system); cấu trúc bất đối
  xứng này buộc các NHTW (như Fed) phải sử dụng các công cụ như ON RRP để ngăn lãi
  suất rơi xuống dưới mục tiêu khi dòng tiền từ khu vực phi ngân hàng tràn ngập hệ
  thống.
source_refs:
- file: Fixed_Income_Alexander_During_Ch07.md
  page: 10
created: '2026-04-13'
updated: '2026-04-22'
---

> [!info] **Bản lưu trữ vĩ mô/vi mô**
> Nội dung này đã được hợp nhất và nâng cấp độ phân giải tại [[Interest_Rate_Corridor_And_Standing_Facilities]]. Bạn đang xem bản chi tiết của nguồn gốc.


# Asymmetric Lending Corridor

## Cơ chế

Sau khủng hoảng tài chính tài sản rác độc 2008 và sự phổ biến của các chính sách phi quy ước (non-conventional - QE), hệ thống [[Symmetric_Interest_Rate_Corridor]] bị vô hiệu hóa. Nó bị thay thế bởi **Hành lang cho vay bất đối xứng (Asymmetric lending corridors)**. [extracted] [[Fixed Income - Alexander During-7.pdf#page=10]]

Trong cấu trúc này lượng thanh khoản thặng dư dội ra là quá lớn, **các ngân hàng không còn thiếu hụt quỹ** (No longer dependent on short liquidity).
Kết quả: Lãi suất thị trường không còn dao động ở phần giữa của hành lang nữa, mà nó bị **"Ghim vĩnh viễn" (Pinned)** sát vào đáy hấp thụ thanh khoản (lower boundary). [extracted] [[Fixed Income - Alexander During-7.pdf#page=10]]

### Tác động lan tỏa (Spillover)

Việc NHTW in tiền mua chứng khoán ồ ạt từ giới phi ngân hàng (non-banks) khiến khu vực phi ngân hàng bỗng ngập tiền mặt (nghịch lý bán tài sản) -> họ có dư quỹ đem gửi tiền vào ngân hàng thương mại -> Đè bẹp năng lực thương mại, ép các rate phi ngân hàng như `€STR` mài dao nằm lọt thỏm *dưới cả* đáy cơ sở vật chất của tiền gửi từ ECB (ECB's deposit facility rate). [extracted] [[Fixed Income - Alexander During-7.pdf#page=10]]

Ở Mỹ, để đối phó dòng thác này không vỡ đáy âm (fall below target rate), FED phải mở ra chương trình đêm qua đêm ngược **overnight reverse repo (ON RRP)** để gút lại số thanh khoản vô bờ bến ngoài biên cương hệ thống ngân hàng. [extracted] [[Fixed Income - Alexander During-7.pdf#page=10]]

## Nguồn

- [[Fixed Income - Alexander During-7.pdf#page=10]] — Rate pinned to the floor, Spillover to €STR, ON RRP
