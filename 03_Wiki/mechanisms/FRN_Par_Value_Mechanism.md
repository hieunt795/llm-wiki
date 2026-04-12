---
type: mechanism
aliases: [Cơ chế bình ổn giá FRN, Pull-to-par on reset, Hồi quang mệnh giá]
trigger: "Tại sao biểu đồ Giá (Price) của một Trái phiếu FRN thả nổi lúc nào cũng phẳng lỳ chạy ôm sát mặt nước mốc 100 (Par), hiếm khi nào thủng sâu như Trái phiếu Fixed Rate thủng 80%?"
output: "Do cứ mỗi lần nó Reset Coupon Rate cho bằng đúng Tỷ giá TT hiện tại, mức Chiết khấu (Discount Rate) trên mẫu số lại Đẳng Cấu (triệt tiêu) với cái Coupon trả trên Tử số. Đưa giá về đúng 100!"
constraints: ["Nó chỉ quay về chuẩn xác 100 nếu Spread rủi ro tín dụng của tổ chức phát hành hoàn toàn đứng im (Không tăng Credit Risk)"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# FRN Par Value Mechanism

## Ma Thuật Tự Chữa Lành Giá Trị (Pull-to-Par at Reset)

Điều vĩ đại nhất của FRN (Floating-rate notes) nằm ở khả năng Miễn Nhiễm Biến Động Định Giá. Bí mật nằm trong phương trình hiện tại hóa Giá $P$ ngay tại cái ngày (t) ấn định Reset Coupon:

$$P = \frac{100 + C \times DCF}{1 + r \times DCF}$$
[extracted] [[Fixed Income - Alexander During-18.pdf#page=3]]

Trong đó:
- Dòng tiền dội về 1 kỳ mốc: Gốc 100 + Lợi tức $C$.
- Lãi trốc rễ thị trường chiết khấu: $r$.
- Công thức ấn định Coupon FRN đã nạp: $C = R + \mu$ (với $\mu$ là Quoted Margin).

Nếu $\mu$ chính xác bằng với cái Credit Spread rủi ro của Công ty phát hành ngày hôm đó, thì $C$ chốt sổ bằng khít với $r$. Tử số bị Mẫu số Hủy Diệt Đồng Nhất (Triệt tiêu), đẩy $P$ bay thẳng đứng về số tròn vành vạnh **100 (Par Value)**. [extracted] [[Fixed Income - Alexander During-18.pdf#page=3]]

*Hệ quả quy nạp:* Ngọ nguậy từ năm thứ T-1, rồi lùi về T-2, cho đến tận năm T-n, Cứ MỖI LẦN một Trái phiếu FRN bóp mốc Reset, thì cái Giá bẩn (Price) của nó lại gột sạch bụi trần hoàn lại 100.
Việc ngụp lặn rớt giá chỉ sinh tồn lay lắt MỎNG DÍNH Ở GIỮA hai dải Reset Dates, chỉ do Tỷ suất Bank Trung Ương bất ngờ giật sập hoặc Do Mức Xếp hạng tín nhiệm (Credit spread) của con nợ thối lên. [extracted] [[Fixed Income - Alexander During-18.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=3-4]] — Phương trình toán học chứng minh quy nạp tại sao FRN tự kéo giá trị PV về Par.
