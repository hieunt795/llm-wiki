---
title: Bond Syndication Mechanics
aliases:
- Dựng sổ
- Book-building
- Bought deal
- Pot deal
- Fixed-price reoffer
type: mechanism
tags:
- fixed-income
- issuance
- investment-banking
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Syndication là cơ chế phát hành trái phiếu thông qua một nhóm các ngân hàng
  đầu tư (syndicate), sử dụng quy trình dựng sổ (book-building) để thăm dò nhu cầu
  và xác định mức giá chào bán (Fixed-price reoffer) nhằm tối ưu hóa việc phân bổ
  và ổn định giá trên thị trường thứ cấp.
source_refs:
- file: Fixed_Income_Alexander_During_Ch17.md
  page: 18
created: '2026-04-13'
updated: '2026-04-22'
---

# [[Bond_Syndication_Mechanics]]

## Mechanism

Trừ các siêu chính phủ có năng lực tự mở sòng đấu thầu ([[Bond_Auction_Mechanics]]), các tập đoàn và chính phủ nhỏ phải thuê các [[Bank|ngân hàng]] đầu tư (Investment Banks) đứng ra rao bán trái phiếu. Quá trình này gọi là **Syndication (Bảo lãnh phát hành vòng kín)**. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=18]]

Các đầu nậu ngân hàng lập thành nhóm phân cấp: Sói chúa (Lead Manager), Sói phụ (Co-lead), và Ruồi muỗi (Syndicate member). Vị thế League tables (xếp hạng giang hồ) quyết định lượng phí (Fee) cắn từ Issuer. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=18]]

### Phương thức ép giá định đoạt số phận:
1. **Bought deal (Chơi tới bến - Firm underwriting):** Nhóm ngân hàng mua ĐỨT toàn bộ 10 tỷ từ tay công ty phát hành ở mức giá cố định, xong tự đi bán giang hồ kiếm chênh. Bán không hết → Ôm sẹo (balance sheet). Phí gánh cái này cực cao! [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=18]]
2. **Best efforts (Sống chết mặc bay):** Chỉ là môi giới ăn hoa hồng. Bán bao nhiêu rọc bấy nhiêu. Cơ chế đi xin lệnh chạy qua hệ thống **Book-building (Dựng sổ)**.
   - Bank thả ra một viên mồi *Spread guidance* (Ví dụ: Chênh 25 basis points so với benchmark).
   - Trader gọi điện ép giang hồ đặt cược. Giang hồ gửi order vào.
   - Tổng lệnh mua / Lệnh bán gọi là **Bid-Cover ratio**. Một issue xịn phải bị Oversubscribed (thừa lệnh mua). Đứa bán không hết lệnh là bị Uncovered (ế) và xấu hổ với thiên hạ. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=18-20]]

### Quyền Lực Pot Deal
Mô hình cũ: Ai nắm khách VIP thì giấu tịt, lùa hết hàng ngon vào bụng ăn riêng.
Mô hình mới: **Pot Deal**. Bắt buộc mọi lệnh đặt chung vào một nồi (book) độc nhất cho Issuer ngắm. Cắt giảm thủ đoạn lùa gà và giúp Issuer phân bổ ([[OTC_Trade_Lifecycle|allocation]]) đúng người để tránh bị xả lén ra thị trường thứ cấp. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]

### Cột mốc chốt tử: Fixed-price Reoffer
Giây phút khóa sổ (pricing), ngân hàng phát giá niêm yết chào sân (Fixed-price reoffer). Trong thời gian chập chững (stabilisation period), các Ngân hàng Bảo lãnh *Bắt Buộc* phải đặt lệnh mua đỡ giá nếu cái trái phiếu mới này rớt giá xuống dưới mốc Fixed-price Reoffer, dọa dẫm để kẻ xả bậy phải chờ! [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch17.md#page=17-19]] — Mechanics, league tables, bought deal vs book-building, và thủ thuật ép sổ Pot deal để làm trong sạch market.
