---
type: mechanism
aliases: [Collateral Swap, Securities lending, Hoán đổi thế chấp]
trigger: "Bạn có rác (MBS) nhưng bạn lại cần tiền từ một ông chỉ chấp nhận cầm đồ bằng Vàng (Treasury)"
output: "Giao dịch lọt khe 3 bên để nâng hạng tài sản (Upgrade) cho hợp khẩu vị"
constraints: ["Bị tính phí thuê trên tài sản nâng hạng, biến tiền lãi được ngốn 2 lần"]
sources: ["Fixed Income - Alexander During-15.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 14
---

# Collateral Transformation

## Thuật Giả Kim của Thị Trường Đồ Cũ (Collateral Swap)

Đôi khi, việc mượn tiền sụp đổ không phải vì bạn nghèo tài sản, mà vì khẩu vị của Kẻ nắm Tiền khép kín (Ví dụ: Nó chỉ lấy đúng Trái phiếu Kho bạc Mỹ xịn, còn bạn lại đang ôm rác thế chấp nhà cửa MBS). 
Cuộc đời đẻ ra hệ thống **Collateral Transformation (Hoán đổi thế chấp)** hay Securities Lending. [extracted] [[Fixed Income - Alexander During-15.pdf#page=3-4]]

### Quá trình tẩy trắng 3 cánh
Người Vay (A) đi lấy mớ Rác của mình (X) để nộp cho 1 bên Quỹ môi giới khổng lồ (C).
Bên C thu rác X, nhả lại ra Bức tượng Vàng (Y).
Người Vay (A) vui vẻ ôm bức tượng Vàng Y lên đập vào mặt Chủ nợ (B) để rút Cash về. [extracted] [[Fixed Income - Alexander During-15.pdf#page=4]]
=> **Tiền mướn Vàng:** A phải cõng 2 gánh lãi = Tiền lãi trả Chủ Nợ B + Phí chênh lệch thuê Vàng từ thằng C.

### Cuộc Giải Cứu Thế Kỷ: TSLF 
Công cụ ảo thuật này đã từng gánh còng lưng Phố Wall thời đổ vỡ 2008. Fed dội thẳng hỏa lực gọi tên **Term Securities Lending Facility (TSLF)** (Xem thêm: [[Collateral_Widening_As_Policy]]). 
Fed New York lôi rương sắt đầy ắp công trái Mỹ (Vàng Y) ra cho khối Ngân Hàng cầm Rác vỡ nợ (X) vào tráo đổi kỳ hạn. Chóp bu Fed trong phút chốc biến thành Trùm Cò Biến Đổi Collateral vĩ đại nhất lịch sử để thông mạch tắc máu nợ tư nhân. [extracted] [[Fixed Income - Alexander During-15.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-15.pdf#page=3-4]] — Quy trình mượn rác đắp vàng Collateral Swap. Lật mở hồ sơ TSLF dùng quỹ SOMA ra tay tẩy rác cho Wall Street.
