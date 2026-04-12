---
type: mechanism
aliases: [Lệch pha bù trừ CMT CMS, CMT Convexity, Swap-spread basis risk]
trigger: "Trái phiếu CMS/CMT trả coupon tỷ lệ theo Tỉ giá 10 năm, nghĩa là Lãi mà tăng thì Coupon tăng mạnh. Vây Mức Giá Trái Phiếu (Price) sẽ Tăng Hay Giảm?"
output: "Kẹt vào siêu lốc lực hút trái chiều (Convexity), giá sập do chiết khấu gãy lưng nhưng dòng tiền vọt nảy! Hedge kiểu gì cũng chảy máu chênh lệch."
constraints: ["CMT Hedging bị ăn tát 1 vố Swap Spread (Basis Risk) sinh tử do công cụ dập hỏa là CMS Swap dội vào"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# CMT CMS Convexity And Hedging Risk

## Cối Xay Thịt Lệch Pha Nhị Phân

Những Trái Phiếu mang dòng máu Ngắn hạn (Libor FRN) được Trời phú cỗ máy **Triệt Tiêu Par Value Môn Phái**. Mỗi lúc Reset, Lãi Phân số Khớp Lãi Lõi... Đẩy giá về chằn chặn 100. [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]

Nhưng CMS/CMT thì ăn trái đắng. Vì Tiền Lãi (Coupon fixing) được nặn từ Biến Cực Tĩnh Lặn Tăm 10 NĂM, trong khi Lãi Đè Nặng Dòng tiền Khứ Hồi chiết khấu Mẫu số (Discount Rate) trong 1 kỳ ngọ nguậy... là Lãi Trốc Dễ Đâm Mù 1 Tháng / 3 Tháng! [extracted] [[Fixed Income - Alexander During-18.pdf#page=6-7]]

Hai sức hút không ăn nhập.
Khi Lãi Suất Tín Dụng Dài Hạn Phóng Tên Lửa:
1. Giá Trị Tiền Kẹp Reset Lãi Tương Lai (Expected Coupon) Múa Khổng Lồ Lên.
2. Nòng Bơm Phát Thả Chiết Khấu (Discount Factors) ngâm xòa nát tươm RỤT GIÁ LUI VỀ ÂM TÀO ĐỊA PHỦ.
- Hai Áp bách CắnXé Gây Ra Nhào Lộn (Convexity Adjustment Substantial). Đâm rách bảng định giá Của Quants. [extracted] [[Fixed Income - Alexander During-18.pdf#page=7]]

### Chợ Tai Ương Basis Risk Đi Phá Rủi Ro
Việc dập rủi ro (Hedging) bó tay chịu trói.
Nếu Dân Trader định Hedge tờ **CMT Floater** bằng cách Tranh Mua Khống Hàng Trái Phiếu Chính Phủ Lót... Balance Sheet (Máy Cưa Chi phí Kho Repo/Ký Quỹ) ngốn Tiền như phá mả! [extracted] [[Fixed Income - Alexander During-18.pdf#page=7]]
Nên dân Lười dùng thẳng Hợp Đồng Hoán Đổi CMS (CMS Swaps) nhẹ têng Vốn Cấp Ký Quỹ...
Kết cục? Ăn Cú Tát Cháy Máy **Basis Risk (Rủi ro Chênh mâm Hàng Nhập Cảng)**: Một rủi ro phập phồng gọi là khoảng dốc Spread giữa Lãi Kịch Swaps trừ đi Lãi Trần Government Yield (Swap Spread Móc Lốp). Báo Phá Sản! [extracted] [[Fixed Income - Alexander During-18.pdf#page=7]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=6-7]] — Mathematical forces decoupling CMT/CMS pricing par stabilization leading to extreme convexity dynamics and Basis Risk in hedging.
