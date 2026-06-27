---
title: Conversion Factor and Notional Coupon
aliases:
- Conversion factor
- Notional coupon
- CF
type: mechanism
tags:
- fixed-income
- derivatives
- math
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Hệ số quy đổi (Conversion Factor) và Lãi suất quy ước (Notional Coupon) là
  các công cụ toán học dùng để chuẩn hóa các trái phiếu có đặc tính khác nhau trong
  một rổ tài sản đủ điều kiện giao hàng, tạo ra một mặt bằng giá chung cho hợp đồng
  tương lai và xác định trái phiếu nào là rẻ nhất để giao (CTD) dựa trên biến động
  của lợi suất thị trường.
source_refs:
- file: Fixed_Income_Alexander_During_Ch29.md
  page: 14
created: '2026-04-13'
updated: '2026-04-22'
---

# [[Conversion_Factor_And_Notional_Coupon|conversion factor]] And Notional Coupon

## Mechanism

Tính chất của Trái phiếu thực rất đa dạng (kỳ hạn dài ngắn, lãi suất cao thấp khác nhau). Nếu sàn giao dịch yêu cầu tất cả Trái phiếu trong rổ ([[CTD_Cheapest_To_Deliver_Bond|deliverable basket]]) có cùng 1 mức giá hợp đồng (Futures) quy chung mà không có số nhân hiệu chỉnh, thì trái phiếu nào có Coupon thấp nhất sẽ nghiễm nhiên luôn luôn trở thành CTD. Sàn đã sinh ra Conversion Factor để phá vỡ kịch bản nhàm chán này. [extracted] [[Fixed_Income_Alexander_During_Ch29.md#page=14-16]]

### 1. Hệ Số Quy Đổi (Conversion Factors - CF)
Conversion Factor là một hệ số riêng biệt cho từng loại trái phiếu, dùng để quy đồng giá trị thật của nó nhằm "thiết lập mức độ cạnh tranh sòng phẳng" giữa các trái phiếu để xác định ngôi vương CTD trong rổ.
- **Công thức tính CF ($c_{i,t_D}$):**
$$c_{i,t_D} = \sum_{k} \frac{Cf_{i,k}}{(1 + C)^{DCF(t_D, t_{i,k})}} - A_i(t_D)$$
Trong đó $C$ là [[Conversion_Factor_And_Notional_Coupon|notional coupon]], $Cf_{i,k}$ là các dòng tiền của trái phiếu, $t_D$ là ngày giao hàng, và $A_i(t_D)$ là lãi tích lũy tại ngày giao hàng. [extracted] [[Fixed_Income_Alexander_During_Ch29.md#page=14]]

- **Giá thanh toán (Invoice Price - $I_{i,t_D}$):**
$$I_{i,t_D} = F \cdot c_{i,t_D} + A_i(t_D)$$
Với $F$ là giá Futures. [extracted] [[Fixed_Income_Alexander_During_Ch29.md#page=14]]

### 2. Notional Coupon (Coupon Quy ước)
Làm thế nào để CF được tính ra một con số đẹp? Sàn giao dịch sẽ định ra một khái niệm Lãi suất Coupon hư cấu (thông thường là 6% ở đa số mọi Futures trên thế giới).
- **Mối liên hệ Lợi suất:** Nếu tất cả trái phiếu trong rổ đều giao dịch tại mức lợi suất bằng đúng Notional Coupon ($y = C$), thì giá Futures $F$ sẽ bằng chính xác 100 và tất cả trái phiếu đều có khả năng trở thành CTD như nhau. [extracted] [[Fixed_Income_Alexander_During_Ch29.md#page=15]]
- **Hệ lụy của Duration:** Vì quy ước này là hằng số, nhưng Lãi suất giao dịch thực trên thị trường của thế giới hiếm khi nào nằm đúng 6%.
    - Khi lợi suất thị trường thấp hơn Notional Coupon ($y < C$), các trái phiếu có **thời lượng (duration)** thấp hơn thường có xu hướng trở thành CTD.
    - Ngược lại, khi lợi suất thị trường cao hơn Notional Coupon ($y > C$), các trái phiếu có duration cao hơn dễ trở thành CTD hơn. [extracted] [[Fixed_Income_Alexander_During_Ch29.md#page=15]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch29.md#page=14-16]] — Toán học đằng sau việc san phẳng rổ tài sản tương lai bằng Notional coupon.
