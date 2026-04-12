---
type: mechanism
aliases: [Dựng sổ, Book-building, Bought deal, Pot deal, Fixed-price reoffer]
trigger: "Muốn bán nguyên cục trái phiếu 10 tỷ đô trong 1 ngày nảy trên phần mềm Bloomberg"
output: "Giao mâm chóp bu cho dàn syndicate banks để chúng gọi điện chào khách, dựng sổ, và chốt giá (Fixed-price reoffer)"
constraints: ["Không xài cho chính phủ to vì chúng nó dùng Đấu thầu Auction"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Bond Syndication Mechanics

## Bếp Núc Phân Phối Trái Phiếu Sơ Cấp (Primary Market)

Trừ các siêu chính phủ có năng lực tự mở sòng đấu thầu ([[Bond_Auction_Mechanics]]), các tập đoàn và chính phủ nhỏ phải thuê các Ngân hàng đầu tư (Investment Banks) đứng ra rao bán trái phiếu. Quá trình này gọi là **Syndication (Bảo lãnh phát hành vòng kín)**. [extracted] [[Fixed Income - Alexander During-17.pdf#page=18]]

Các đầu nậu ngân hàng lập thành nhóm phân cấp: Sói chúa (Lead Manager), Sói phụ (Co-lead), và Ruồi muỗi (Syndicate member). Vị thế League tables (xếp hạng giang hồ) quyết định lượng phí (Fee) cắn từ Issuer. [extracted] [[Fixed Income - Alexander During-17.pdf#page=18]]

### Phương thức ép giá định đoạt số phận:
1. **Bought deal (Chơi tới bến - Firm underwriting):** Nhóm ngân hàng mua ĐỨT toàn bộ 10 tỷ từ tay công ty phát hành ở mức giá cố định, xong tự đi bán giang hồ kiếm chênh. Bán không hết → Ôm sẹo (balance sheet). Phí gánh cái này cực cao! [extracted] [[Fixed Income - Alexander During-17.pdf#page=18]]
2. **Best efforts (Sống chết mặc bay):** Chỉ là môi giới ăn hoa hồng. Bán bao nhiêu rọc bấy nhiêu. Cơ chế đi xin lệnh chạy qua hệ thống **Book-building (Dựng sổ)**.
   - Bank thả ra một viên mồi *Spread guidance* (Ví dụ: Chênh 25 basis points so với benchmark).
   - Trader gọi điện ép giang hồ đặt cược. Giang hồ gửi order vào. 
   - Tổng lệnh mua / Lệnh bán gọi là **Bid-Cover ratio**. Một issue xịn phải bị Oversubscribed (thừa lệnh mua). Đứa bán không hết lệnh là bị Uncovered (ế) và xấu hổ với thiên hạ. [extracted] [[Fixed Income - Alexander During-17.pdf#page=18-20]]

### Quyền Lực Pot Deal
Mô hình cũ: Ai nắm khách VIP thì giấu tịt, lùa hết hàng ngon vào bụng ăn riêng.
Mô hình mới: **Pot Deal**. Bắt buộc mọi lệnh đặt chung vào một nồi (book) độc nhất cho Issuer ngắm. Cắt giảm thủ đoạn lùa gà và giúp Issuer phân bổ (allocation) đúng người để tránh bị xả lén ra thị trường thứ cấp. [extracted] [[Fixed Income - Alexander During-17.pdf#page=19]]

### Cột mốc chốt tử: Fixed-price Reoffer
Giây phút khóa sổ (pricing), ngân hàng phát giá niêm yết chào sân (Fixed-price reoffer). Trong thời gian chập chững (stabilisation period), các Ngân hàng Bảo lãnh *Bắt Buộc* phải đặt lệnh mua đỡ giá nếu cái trái phiếu mới này rớt giá xuống dưới mốc Fixed-price Reoffer, dọa dẫm để kẻ xả bậy phải chờ! [extracted] [[Fixed Income - Alexander During-17.pdf#page=19]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=17-19]] — Mechanics, league tables, bought deal vs book-building, và thủ thuật ép sổ Pot deal để làm trong sạch market.
