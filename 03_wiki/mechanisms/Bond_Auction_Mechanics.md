---
title: Bond Auction Mechanics
aliases:
- Đấu thầu trái phiếu
- American auction
- Dutch auction
- Tail
- Khúc đuôi
- Bid-cover ratio
type: mechanism
tags:
- fixed-income
- issuance
- auction-theory
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Đấu thầu trái phiếu là cơ chế phát hành nợ sơ cấp của các chính phủ (như Mỹ,
  Đức) dựa trên việc ưu tiên lợi suất thấp nhất; các biến số như 'Khúc đuôi' (Tail)
  và tỷ lệ Bid-to-cover đóng vai trò là những chỉ báo quan trọng nhất về sức khỏe
  nhu cầu và tâm lý thị trường trái phiếu.
source_refs:
- file: Fixed_Income_Alexander_During_Ch17.md
  page: 19
created: '2026-04-13'
updated: '2026-04-22'
---

# [[Bond_Auction_Mechanics]]

## Mechanism

Khi Siêu Chính Phủ (Mỹ, Nhật, Đức) bán nợ, họ không thèm trả phí (Fee) cho Sói già Wall Street. Họ đè thẳng ra Cổng Đấu Thầu (Auction) — nơi các Tổ chức đấm đá nhau giành Lợi suất hời nhất! [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]

Đấu thầu hoạt động trên cơ chế ưu tiên Giá Tốt Nhất (Lợi suất Thấp nhất). Nhưng khi "Cắt Cầu", luật chơi chia thành hai nhánh độc địa:
- **American Auction (Đấu thầu vắt cạn):** Đăng ký giá nào bị trừ [[Money|tiền]] giá đó. Xui xui viết giá cắt cổ (Mua với lợi suất quá thấp), bạn bị phạt phải mua hớ (Winner's Curse), trong khi thằng đấu thầu hạng chót được mua giá hời. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]
- **Dutch Auction (Đấu thầu kiểu Nhật/Hà Lan):** Đồng Giá cho Toàn Dân! Dù bạn có đấu thầu điên cuồng ở giá cao nhường nào, khi chốt sổ, MỌI KẺ THẮNG đều trả đúng cái Giá chót bét nhất (Lowest accepted price) miễn là trúng thầu. Cơ chế này khuyến khích tay to đặt lệnh khống cực mạnh mà sợ "hớ". [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]

### Chỉ Số Khúc Đuôi "Tail"
Hàng đấu thầu bao giờ cũng có Giá Trung Bình (Average Price) và cái Giá Chót (Cut-off Price). Độ chênh lệch giữa hai vùng giá đó gọi là tiếng sấm **The Tail** (Khúc Đuôi). [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=19]]
- Đuôi càng Dài (Tail to), chứng tỏ Thị trường cực kỳ miễn cưỡng. Cầu mỏng nên Issuer vạch sâu xuống dăm ba cái nấc giá tồi tệ mới vét cạn được số tiền cần vay. Đuôi dài vọt lên trên lịch sử gào thét một chữ: Cú ngã sụp (Sloppy demand / Uncovered risk). [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=20]]

### Primary Dealers & Non-Competitive Bids
Chính quyền để mở van bù trừ cho bọn tay sai. Những con sói chuyên đi canh thanh khoản hàng ngày trên Secondary (gọi là **Primary Dealers**) bị ép chỉ tiêu phân bổ: Dù bão táp chúng mày cũng phải ôm rác! Đổi lại, chính quyền cấp đặc quyền: Lệnh **Non-Competitive (Viết khống giá)**. [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=20]]
- Tự động mua Trúng dù bầu trời sụp, và được áp mức giá Trung Bình Auction, không sợ đu đỉnh. Tại Đức, Ngân khố nước nhà cũng nhảy hẳn vào Đấu thầu (lưu kho lệnh Non-Comp) thao túng luôn giá trị Cut-off rồi nhả từ từ ra thị trường ngày hôm sau qua Sàn Điện tử hòng vắt chanh con mồi! [extracted] [[Fixed_Income_Alexander_During_Ch17.md#page=20-21]]

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch17.md#page=19-21]] — Anatomy của the Dutch/American auction, ý nghĩa chết chóc của đuôi (Tail), và trò thao túng kho (Retention) đỉnh cao của Ngân khố Đức.
