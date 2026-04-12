---
type: mechanism
aliases: [Thác vỡ nợ CCP, Default fund, Bidding obligation]
trigger: "Một ngân hàng thành viên của CCP vỡ nợ hoặc fail ký quỹ"
output: "Kích hoạt cỗ máy thanh lý dây chuyền để chặn việc sụp đổ lây lan tới sập bản thân cái CCP"
constraints: ["CCP không gánh tổn thất mà ép những quỹ còn sống khác gánh vác hộ"]
sources: ["Fixed Income - Alexander During-13.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 12
---

# CCP Default Waterfall

## Thác thanh lý Vỡ nợ (The Waterfall)

Sự sụp đổ của một tay chơi vĩ đại tạo ra một cái hố đen thanh khoản mà [[Central_Counterparty]] phải lấp lỗ. Trật tự hiến tế (Waterfall) của CCP là kiến trúc đáng gờm nhất của thị trường OTC Clearing: [extracted] [[Fixed Income - Alexander During-13.pdf#page=4-5]]

1. **Hút sạch Ký quỹ (Defaulter's Margin):** Lôi toàn bộ [[Variation_Margin_Vs_Initial_Margin|IM + VM]] của cái thằng vừa chết đem ra điền vào chỗ lõm của những người đang thắng cược.
2. **Ép mua giá bèo (Bidding Obligation / Close-out Auction):** Khi đống Margin đó bốc hơi sạch sành sanh vì thị trường gãy nát, CCP ép tất cả các ngân hàng/quỹ còn sống **phải vào đấu giá mua lại cục rác rủi ro đó**. Đám ruồi bu này luôn ra giá Đấu thầu mảng âm (Negative bids - *"Tôi cầm rác cho anh nhưng anh phải gán thêm tiền mặt cho tôi"*). [extracted] [[Fixed Income - Alexander During-13.pdf#page=4-5]]
3. **Móc Quỹ Mặc Định (Default Fund):** Nếu IM rỗng tuếch không đủ trả cho cái Bidding âm dã man của bọn kền kền, CCP phá rương **Default Fund (Quỹ Phòng Vệ Nét Chéo)**. Đây là một cái hồ chung do tất thảy mọi thành viên đóng hụi ngay từ lúc gia nhập. [extracted] [[Fixed Income - Alexander During-13.pdf#page=5]]
   - *Logic trừng phạt:* Đứa nào hồi nãy Bids quá thấp keo kiệt (ăn vạ), CCP sẽ phạt đứa đó phải è cổ đóng tiền nhiều nhất để đổ đầy lại cái rương Default Fund vừa vỡ. [extracted] [[Fixed Income - Alexander During-13.pdf#page=5]]
4. **CCP Vỡ Nợ Trắng Bụng:** Nếu cái rương thủng luôn và tư bản tự có của CCP tan biến, thị trường chính thức Reset.

Vì cấu trức Rủi ro liên đới (Mutual nature) mang tính tàn nhẫn này, để tham gia CCP, bạn không thể chỉ có tiền, bạn phải có **Nhân lực trading giỏi đi đấu giá dọn rác giùm CCP**. Điều này đẩy hàng vạn quỹ Pension / Non-financial ra rìa phải xài hệ thống ủy thác (Indirect clearing). [extracted] [[Fixed Income - Alexander During-13.pdf#page=5]]

## Nguồn

- [[Fixed Income - Alexander During-13.pdf#page=4-5]] — The waterfall of default management in Central Clearing.
