---
title: Present Value Of A Basis Point
aliases:
- PVBP
- DV01
- BPV
- Basis Point Value
- Giá trị của một điểm cơ bản
type: mechanism
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch17.md"
thesis: Trong bộ máy đo rủi ro lãi suất, Quỹ đầu tư thì thích dùng *[[Modified_Duration]]*
  (D* - đo lường theo tỷ lệ phần trăm % thay đổi giá để quy về Size của tệp quản lý).
  Nhưng các Trader trên Sàn Giao Dịch thì chỉ thích nhìn rủi ro bằng [[Money|tiền]]
  TƯƠI. Đó là sứ mệnh của **PVBP (Present Value of a
source_refs:
- file: Fixed_Income_Alexander_During_Ch17.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 16
---

# [[Present_Value_Of_A_Basis_Point]]

## Mechanism

Trong bộ máy đo rủi ro lãi suất, Quỹ đầu tư thì thích dùng *[[Modified_Duration]]* (D* - đo lường theo tỷ lệ phần trăm % thay đổi giá để quy về Size của tệp quản lý). Nhưng các Trader trên Sàn Giao Dịch thì chỉ thích nhìn rủi ro bằng [[Money|tiền]] TƯƠI. Đó là sứ mệnh của **PVBP (Present Value of a Basis Point)** - hay trong giới Swap gọi là **DV01 (Dollar Value of an 01)**. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=27]]

### Phương trình nền tảng
Hai công cụ này chẳng qua là Đạo hàm bậc nhất của Giá dơ (Dirty Price) $P$ đối với Lợi suất $y$:

$$PVBP = \frac{\partial P}{\partial y}$$
Trong khi đó Duration:
$$D^* = \frac{1}{P} \frac{\partial P}{\partial y}$$

Nói cách khác: **PVBP** chính là số [[Cash|tiền mặt]] trực tiếp biến mất (hay mọc thêm) trên tay Trader nếu cầm 1 đơn vị Notional trái phiếu và Yield đường cong giật $\pm 1$ basis point (0.01%). [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=27]]

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch17.md#page=27-28]] — Phân biệt PVBP, D* trong góc nhìn giữa Quản lý quỹ (AUM) và Trader (Trading book).
