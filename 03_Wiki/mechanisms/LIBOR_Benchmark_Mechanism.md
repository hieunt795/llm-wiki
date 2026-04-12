---
type: mechanism
aliases: [Euribor, Đóng họ lãi suất, Trimmed mean interbank rate]
trigger: "Cần tìm một lãi suất mỏ neo trên bờ biển đầy sương mù của chợ OTC"
output: "Thỏa thuận đóng họ (panel) để cắt ngọn bình quân thị trường Vay Tín chấp"
constraints: ["Bị thao túng man rợ trong khủng hoảng, mất đi tính đại diện vì Market nay đã chuyển qua đánh Repo có thế chấp"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 13
---

# LIBOR Benchmark Mechanism

## Cơ chế neo giá bằng khảo sát (Trimmed Mean)

Do thị trường tiền xu liên ngân hàng giao dịch thầm kín (OTC), không ai biết lãi suất chuẩn là bao nhiêu. Hiệp hội BBA Anh tung ra chiêu bài **LIBOR (London Interbank Offered Rate)**. [extracted] [[Fixed Income - Alexander During-14.pdf#page=7]]

- Cứ vào 10h sáng ở London, một nhóm ngân hàng thượng lưu sẽ nộp bảng trả lời cho câu hỏi: *"Anh nghĩ các ngân hàng xịn mượn tiền Tín chấp (Unsecured) của nhau kỳ hạn 3 tháng với giá bao nhiêu?"*.
- Người ta đập nát những bảng đưa giá quá cao và quá thấp, lấy trung bình ở giữa mâm (Trimmed mean). Hệ thống này bá đạo đến mức nó đẻ ra con rơi con rớt ở mọi lục địa (TIBOR ở Nhật, Euribor của Liên minh Châu  u...). Tỷ giá bán thì là LIBOR, tỷ giá mua của Bank được gọi là LIBID. [extracted] [[Fixed Income - Alexander During-14.pdf#page=7]]

## Bi kịch đẫm máu
Gót chân Achilles của Libor nằm ở chỗ: **Nó đéo phải là một Giao dịch thật**, mà chỉ là "Quan điểm khảo sát". 
- Vào khủng hoảng, thanh khoản cạn, 100% thị trường lôi mẹ tài sản ra vay có thế chấp (Repo), chẳng ai cho mượn tín chấp dài hạn nữa. Vậy số liệu đệ trình kia từ đâu? Đa phần trader chế cháo "điền bừa" (Spread off) từ hoán đổi qua đêm. [extracted] [[Fixed Income - Alexander During-14.pdf#page=8]]
- Sự lỏng lẻo này kích hoạt chuỗi **Thao túng Libor**, nơi phe phái của trader "nút ngón" nhau đẩy giá lên vài bp ở kỳ fixing để phái sinh đút túi bẫm. Cuộc khủng hoảng này tạo một lỗ hổng đạo đức mà dọn đường cho [[OIS_And_Benchmark_Reform]]. [extracted] [[Fixed Income - Alexander During-14.pdf#page=8-9]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=7-9]] — Chế tài khảo sát Libor/Euribor và quả bom nổ chậm của phương pháp xin ý kiến thay vì dòm giao dịch thật.
