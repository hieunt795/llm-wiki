---
type: definition
aliases: [CMT Floater, CMS Floater, Constant-maturity treasury, TEC10, ISDAfix, ICE Swap Rate]
trigger: "Trái phiếu trả Coupon thả nổi, nhưng lại bốc Lãi suất tham chiếu là 10-Year Yield (Đuôi dài) thay vì Lãi qua đêm ngắn hạn nộp tiền điện?"
output: "Đó là CMT/CMS Floaters! Quặp chặt định giá lãi suất vào Đuôi Dài 10 năm của nền kinh tế"
constraints: ["Không có tác dụng bình ổn giá tự động hồi phục về Mệnh Giá 100 (Par-pulling mechanism) như đám FRN Money Market"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# CMT And CMS Floaters

## Lá Bùa Thả Nổi Khổng Lồ

Khác biệt một trời một vực so với đám OIS/LIBOR FRNs chuyên đi bết dính với Tỷ giá R ngắn hạn (Overnight/3M), các Chính phủ Châu Âu đã tạo một con Ác thú mới: Cột mức Coupon của Trái phiếu FRN thả nổi đâm thẳng vào Dải Cực (Long-end) 10 Năm đến 30 Năm của Đường Cong! [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]

- **CMT (Constant-Maturity Treasury) Floater:** Chỉ số được ghim cứng vào Định Giá Phát Hành Giấu Kín Của Đống Trái Phiếu Chính Phủ Mốc (Ví dụ: Thằng Pháp có Chỉ số Khắc Khoải TEC10 lấy cung từ tụi Primary Dealers). Ở Nhật thì cắp rập nhặt Yield đấu thầu 10 Năm nóng hổi. [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]
- **CMS (Constant-Maturity Swap) Floater:** Coupon đâm ngập vào rốn Lãi Swap Mốc (10Y Swap Rate). Thay vì móc nối Dealer khép kín, CMS lấy Fixing niêm yết do Cỗ Máy ICE ban thưởng (Ngày xưa còn mang tên Sát Thủ Thao Túng ISDAfix). [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]

Đỉnh cao của sự Trí Trá Cấu Trúc là **CMS Steepener**: Ăn tiền Coupon ăn mập mờ qua khoảng dốc (Spread) giữa [10Y CMS - 2Y CMS]! Đường cong (Yield Curve) càng Ngóc Đầu Chết Kéo (Steepens), Coupon văng lên Tột Đỉnh Dương! [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=6-7]] — Structure overview of CMT vs CMS floaters, referencing the famous French TEC10 and ICE benchmark inputs.
