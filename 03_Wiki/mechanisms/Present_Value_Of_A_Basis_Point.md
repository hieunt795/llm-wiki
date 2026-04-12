---
type: mechanism
aliases: [PVBP, DV01, BPV, Basis Point Value, Giá trị của một điểm cơ bản]
trigger: "Trader muốn biết Lãi/Lỗ ra tiền tươi (USD/VND) thay vì số phần trăm mỗi khi Yield nhúc nhích 1 điểm cơ bản"
output: "Dùng PVBP/DV01, tức đạo hàm bậc 1 của Giá dơ (Dirty Price) theo Yield"
constraints: ["PVBP phóng đại rủi ro của trái phiếu dài hạn do nó giả định đường cong lãi suất phẳng tịnh tiến"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Present Value Of A Basis Point

## Khẩu Súng Đo Lường Rủi Ro Giới Trader

Trong bộ máy đo rủi ro lãi suất, Quỹ đầu tư thì thích dùng *Modified Duration* (D* - đo lường theo tỷ lệ phần trăm % thay đổi giá để quy về Size của tệp quản lý). Nhưng các Trader trên Sàn Giao Dịch thì chỉ thích nhìn rủi ro bằng TIỀN TƯƠI. Đó là sứ mệnh của **PVBP (Present Value of a Basis Point)** - hay trong giới Swap gọi là **DV01 (Dollar Value of an 01)**. [extracted] [[Fixed Income - Alexander During-17.pdf#page=27]]

### Phương trình nền tảng
Hai công cụ này chẳng qua là Đạo hàm bậc nhất của Giá dơ (Dirty Price) $P$ đối với Lợi suất $y$:

$$PVBP = \frac{\partial P}{\partial y}$$
Trong khi đó Duration:
$$D^* = \frac{1}{P} \frac{\partial P}{\partial y}$$

Nói cách khác: **PVBP** chính là số tiền mặt trực tiếp biến mất (hay mọc thêm) trên tay Trader nếu cầm 1 đơn vị Notional trái phiếu và Yield đường cong giật $\pm 1$ basis point (0.01%). [extracted] [[Fixed Income - Alexander During-17.pdf#page=27]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=27-28]] — Phân biệt PVBP, D* trong góc nhìn giữa Quản lý quỹ (AUM) và Trader (Trading book).
