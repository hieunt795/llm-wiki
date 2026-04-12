---
type: mechanism
aliases: [Bond Tap Funging, Gộp mã ISIN, Funging]
trigger: "Tổ chức phát hành một lô đợt 2 cho một dòng trái phiếu vốn đã trôi nổi trên market"
output: "Gắn mã ISIN tạm thời cho đợt 2, chờ qua vòng luân hồi thanh toán rối ghép xác lại mã ISIN cũ"
constraints: ["Cần đảm bảo lô mới phải match hoàn toàn đặc tính dòng tiền tương lai của mã gốc"]
sources: ["Fixed Income - Alexander During-11.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 10
---

# Bond Tap Funging

## Cơ chế Gộp mã 

Phát hành thêm một lượng Trái phiếu gối tiếp vào một dòng Trái phiếu đã tồn tại gọi là **Taps**. Lô Taps này về bản chất là bản clone giống hệt tờ trái phiếu Gốc (cùng coupon, cùng maturity). [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]]

**Vấn đề T+ Settlement:**
Tuy nhiên, lô mới in ra có cấu trúc "Ngày thanh toán nộp tiền cho đợt IPO lần đầu" khá oái oăm (ví dụ T+5 sau ngày định giá). Trong khi tờ Trái phiếu Gốc đang chạy ngoài chợ lại tuân thủ luật thanh toán Secondary Market là T+2. Nếu nhập nhèm lấy ngay [[ISIN_Code]] gốc gắn cho lô con mới mở bán, toàn bộ hệ thống book-entry settlement sẽ báo lỗi sập nguồn. [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]]

### Thuật ngữ "Funging"

Cách xử lý của lưu ký thanh toán:
1. Phát hành cho lô Tap một mã lô ISIN tạm thời, khác biệt hoàn toàn với mã Gốc.
2. Ép cục ISIN mới này chạy xong đợt settlement kỳ dị của nó.
3. Sau một giai đoạn an toàn (certain period of time), hệ thống **"Merge"** mã tạm vào lại mã Gốc, khai tử mã tạm thời. Hành vi hợp lưu này được dân chuyên môn gọi là thuật ngữ **"Funged"** (Biến nó thành Hàng hóa chuẩn hóa phân mảnh - Fungible). [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]]

Hậu quả: Bạn soi vào portfolio của mình, hôm qua đang ôm một con ISIN lạ hoắc, sáng nay tỉnh dậy bỗng nhiên cái ISIN đó biến mất và số dư nhồi thẳng vào con Trái phiếu Gốc.

## Nguồn

- [[Fixed Income - Alexander During-11.pdf#page=6]] — Kỹ thuật Tap, settlement dates friction, và khái niệm Funged.
