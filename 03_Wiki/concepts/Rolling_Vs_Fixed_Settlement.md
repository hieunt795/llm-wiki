---
type: definition
aliases: [T+2, T+0, Nguồn gốc Backwardation]
sources: ["Fixed Income - Alexander During-12.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 11
---

# Rolling Vs Fixed Settlement

## Phân Tách Khái Niệm Thời Gian
Trong đời sống Trading, có ranh giới vô cùng lớn giữa:
- **Trade Date / Valuation Date:** Là ngày mà hai bên thống nhất khớp lệnh (ví dụ: bốc múc cái giá 101.50). Nó khóa chết nghĩa vụ. [extracted] [[Fixed Income - Alexander During-12.pdf#page=15-16]]
- **Settlement Date / Value Date:** Tọa độ tương lai mà lúc đó Của cải (Tiền - Code bạc) thực sự trao tay hoàn tất quyền sở hữu. Giá khất thanh toán qua ngày phải đi kèm bù trừ cái quyền lợi tích tụ (accrued interest). [extracted] [[Fixed Income - Alexander During-12.pdf#page=16]]

## Khác biệt giữa Rolling và Fixed Settlement

### 1. Fixed Settlement (Thanh toán Cố định)
Phong cách cổ đại của thị trường (Ví dụ Sở Giao dịch Chứng khoán London xa xưa), nơi 100 trader đánh nhau cả tháng trời, rồi cùng chờ gom vào đúng **Một ngày cụ thể ở cuối tháng** để đẩy chung một mớ tiền và giấy. Cự ly có thể dãn tới 60 ngày. Rủi ro khuyếch tán vì đợi quá dài lỡ có người lăn đùng ra phá sản. [extracted] [[Fixed Income - Alexander During-12.pdf#page=16]]
- *Nguồn gốc Ngôn từ:* Nếu một trader thời đó không kịp chồng tiền ngày Settlement kì này, xin khất sang cái Ngày Fixed Settlement của tháng tiếp theo (Kế lùi), trò đó gọi là **Backwarded**. Tên gọi này chết danh di tích thành thuật ngữ "Backwardation" của TT Phái sinh hiện đại (Giá hợp đồng gần xa hơn hợp đồng gần). [extracted] [[Fixed Income - Alexander During-12.pdf#page=16]]

### 2. Rolling Settlement (Thanh toán Cuốn chiếu)
Hệ thống hiện tại răn đe rủi ro rách nợ (Credit risk) bằng dao bén. Giao dịch luôn luôn nằm ở cự ly T+2 (Ngày khớp lệnh + 2 ngày kinh doanh). Cứ đánh qua đánh lại trong ngày không mệt nghỉ, chỉ cần chốt hạ cuối buổi đúng T+2 móc đủ Tài sản bơm vào tài khoản. [extracted] [[Fixed Income - Alexander During-12.pdf#page=16]] (Chính phủ Anh Mỹ nhạy cảm tột độ còn ép Gilt/Treasury đánh sập sàn với T+0 tức ăn trao tiền ngay tắp lự).

Mặc dù giảm rủi ro nợ nần, thời gian Settlement thu ngắn bóp nghẹt thanh quản của khối Kế toán dọn rác đối chiếu (Reconciliation), làm các lệnh Fail ngớ ngẩn (chưa kịp nhận mail khớp đã trôi qua ngày) xảy ra phổ biến. [extracted] [[Fixed Income - Alexander During-12.pdf#page=16]]

## Nguồn

- [[Fixed Income - Alexander During-12.pdf#page=15-16]] — T+2 convention, Accrued interest implication, T+0 áp lực Back-office và mẩu gốc gác Backwardation học thuyết.
