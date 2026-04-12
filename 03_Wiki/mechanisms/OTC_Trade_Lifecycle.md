---
type: mechanism
aliases: [Quy trình vòng đời giao dịch, Allocation, DK, Don't Know]
trigger: "Trader gào lên 'Done' qua điện thoại, nhưng bằng cách nào tờ trái phiếu lọt được vào kho của khách?"
output: "Quy trình ống nước 8 bước đi từ Bàn Front Office xuống hầm Back Office để dọn dẹp xác thực"
constraints: ["Bất kỳ sai sót nào ở khâu chốt đuôi sẽ tốn kém gấp ngàn lần sẩy miệng trên điện thoại"]
sources: ["Fixed Income - Alexander During-12.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 11
---

# OTC Trade Lifecycle

## Vòng đời của một giao kèo OTC

Giao dịch trên Sàn (Exchange) thì máy móc làm rẹt. Nhưng giao dịch OTC là sự thỏa thuận bằng mồm, qua chat, qua mớ giấy lộn. Tránh việc "ông nói gà bà nói vịt", một cỗ máy **Trade Lifecycle** khổng lồ được thiết kế dựa trên nguyên tắc Vạn vật chống lưng chéo (Redundancy & independent checks). [extracted] [[Fixed Income - Alexander During-12.pdf#page=4-5]]

### 1. The Deal (Thỏa thuận tiền tuyến)
- **Inquiry & Negotiation:** Đoán ý nhau bằng giá [[Firm_Vs_Indicative_Quotes]].
- **Agreement:** Miệng hô `Mine` (Tôi mua), kia đáp `Done` (Chốt). Bút sa gà chết.

### 2. Dọn rác hậu cần (Middle & Back Office)
- **Recording & Enrichment:** Trader gõ lệnh vào máy. Hệ thống tự móc nối lấy thông tin tài khoản (SSI - Standard settlement instructions) chắp vá vào lệnh. [extracted] [[Fixed Income - Alexander During-12.pdf#page=8]]
- **Allocation (Cắt miếng bánh):** Thường các tay Quản lý quỹ (Fund Manager) sẽ đánh 1 Lệnh To đùng, rồi bắt Dealer xẻ cái xác lệnh đấy ra làm 10 mảnh nhỏ để đút (allocate) vào mồm 10 quỹ con nội bộ. Điều này dằn vặt hệ thống dữ dội vì 1 lệnh gốc bị xóa, đẻ ra 10 lệnh con đi Settlement! [extracted] [[Fixed Income - Alexander During-12.pdf#page=9]]
- **Confirmation:** Bàn Middle Offices hai rạp đối chiếu với nhau bằng điện tín SWIFT. Nếu gã B thấy gã A gửi 1 cái xác nhận cực kì vô lý (mà nội bộ B đéo hề ghi nhận có mua), B sẽ phản hồi lại chữ **DK (Don't Know)** - Tấm thẻ từ chối kinh điển. [extracted] [[Fixed Income - Alexander During-12.pdf#page=10]]

### 3. Về vạch đích
- **Settlement Instructions:** Bắn trát lệnh cho bọn Custodians (Ngân hàng Cất trữ) đi nhặt và chuyển hàng (xem [[Delivery_Versus_Payment]]).
- **Reconciliation:** Đối chiếu lại với Custodian xem tiền chạy về rương chuẩn số chưa, hay thằng nào cuỗm mất. Lỗi ở bước này là thảm họa vì lỡ tay cho Custodian duyệt sai từ đầu. [extracted] [[Fixed Income - Alexander During-12.pdf#page=12]]

## Nguồn

- [[Fixed Income - Alexander During-12.pdf#page=4-12]] — Mô tả đồ sộ về chuỗi cung ứng Back-office, sự rắc rối của cơ chế Allocation làm nát vé giao dịch ban đầu, và khái niệm DK (Don't know).
