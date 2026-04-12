---
type: mechanism
aliases: [SOFR, TONA, ESTR, OIS, Cải cách tỷ giá tham chiếu]
trigger: "Scandal tàn sát thị trường của bọn trader bơm thối Libor"
output: "Giết Libor, đẻ ra nhóm benchmark mốc neo vào thị trường Overnight có giao dịch thực tế"
constraints: ["Không có kỳ hạn tương lai vắt dài (term premium), chỉ báo chốt lãi ở sau lưng"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# OIS And Benchmark Reform

## Cuộc Đại Trừng Phạt Trục Xuất Libor

Sau cơn bão đẫm máu thao túng [[LIBOR_Benchmark_Mechanism]], giới chức toàn thân nổi gân xanh ép ngành Tài chính vứt bỏ những ước lượng suông (trader opinion), quy luật cải cách (Benchmark reform) chia thành mũi giáp đánh thẳng: Sốt Overnight. [extracted] [[Fixed Income - Alexander During-14.pdf#page=10]]

### Thế hệ "Risk-Free" Benchmark
Dẹp dứt điểm việc cho vay Unsecured nguy hiểm, những đứa con mới SOFR (Mỹ), €STR (Châu Âu) và SONIA (Anh), TONAR (Nhật) là kết quả đo lường những Vệ Khí tiền tệ được **chuyển tay Mua Đứt có cam kết (Secured)** hoặc quét trên hệ sinh thái Giao dịch Qua Đêm 1 ngày (Overnight). Tỷ lệ giao dịch thực tế nên éo thể nào gõ mõ thao túng trên volume khủng nghìn tỷ. [extracted] [[Fixed Income - Alexander During-14.pdf#page=9]]

### Cách thức nhào nặn kỳ hạn dài bằng OIS
Vì cái benchmark mới bẩm sinh chỉ ôm qua đêm, muốn biết mượn 3 tháng nhiêu tiền thì sao? Dùng cỗ máy **OIS (Overnight Index Swap)**. Dân chơi Swap sẽ ngồi gõ hợp đồng ăn chênh lệch: Khoán 1 tay nhả Rate cố định, 1 tay ôm lãi kép (Compounded) tích lũy hằng ngày của cái lãi suất qua đêm SOFR. Lãi kép sinh ra cầu vồng kéo điểm OIS 3 tháng lên sàn. [extracted] [[Fixed Income - Alexander During-14.pdf#page=9-10]]

### Cơn ác mộng Backward Looking (Đếm trễ Lagged period)
Ngân hàng bán mảng vay thế chấp (Mortgages/Quỹ vay sinh viên) thường nương nhờ Libor trước kì lĩnh lãi để Báo tiền đóng họ cho Dân. Nay nếu thay SOFR (đợi tụt quần tới ngày thu mới biết Compound nhảy sao), thì Dân la làng. Thống đốc ngân hàng nhà nước xì xụp sáng tạo kiểu lấy *Quá khứ Lagged xích về 5 ngày*. Khốn nạn là kiểu cưa sừng này không chứa cái "Term premium" (chênh lệch cược kỳ hạn) của Libor tẹo nào, biến đường cong Tín dụng ngân hàng thành công viên. [extracted] [[Fixed Income - Alexander During-14.pdf#page=11]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=9-11]] — Cái chết thương vong của Libor, con quái vật qua đêm gốc Secured (SOFR), và sự ngây thơ của OIS Lagged.
