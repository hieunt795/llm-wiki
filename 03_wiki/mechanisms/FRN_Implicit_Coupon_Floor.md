---
title: FRN Implicit Coupon Floor
aliases:
- Sàn không âm
- Coupon floor
- Zero-floor
- max(0
- C)
type: mechanism
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch18.md"
thesis: 'Sau kỷ nguyên Nới lỏng định lượng cực đoan áp dụng chính phủ Âm (Negative
  Interest Rates), giới làm giá Trái phiếu [[Floating_Rate_Notes_FRN|frn]] nhận ra
  lỗ hổng búa bổ của công thức Lõi: Lãi chuẩn bị âm sâu quá bóp nát cái Spread Margin,
  dìm Coupon lặn vào vùng Lãi Âm.'
source_refs:
- file: Fixed_Income_Alexander_During_Ch18.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 17
---

# [[FRN_Implicit_Coupon_Floor]]

## Mechanism

Sau kỷ nguyên Nới lỏng định lượng cực đoan áp dụng chính phủ Âm (Negative Interest Rates), giới làm giá Trái phiếu [[Floating_Rate_Notes_FRN|frn]] nhận ra lỗ hổng búa bổ của công thức Lõi: Lãi chuẩn bị âm sâu quá bóp nát cái Spread Margin, dìm Coupon lặn vào vùng Lãi Âm.

Nếu Coupon âm, Người Đi Vay bỗng nhiên trở thành Người Thu [[Money|tiền]], và Giới Chóp Bu Cho Vay bị ép nộp vào mâm phạt!
Đại đa số khung pháp lý hành pháp (Jurisdictions) và [[Book_Entry_Securities_System|lưu ký chứng khoán]] Trung ương (CSDs) hoàn toàn **ngu loạn / không có tính năng hệ thống** xử lý thu tiền ngược thế này. [extracted] [[Fixed_Income_Alexander_During_Ch18.md#page=3]]

Hệ quả là mọi Khế ước FRN hiện đại đều đúc ngầm vào một hàm max, còn gọi là **Zero-floor (Sàn 0%)**.
$$C_i = max(0, R(t_i - 2) + \mu)$$

Thế giới dù có đóng băng, kẻ cho vay ít nhất vẫn húp được 0 đồng chứ tuyệt k bị chảy máu ngược. Mức Sàn này không ai tước ép ở giá 0, các Issuer có quyền đặt Cap (trần) hoặc Floor (Sàn) ở trên mức 0 để tùy biến rủi ro độ võng. [extracted] [[Fixed_Income_Alexander_During_Ch18.md#page=3]]

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch18.md#page=3]] — The legal and systematic necessity of writing implicit max floors into FRN indentures.
