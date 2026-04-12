---
type: definition
aliases: [Dấu '+' trái phiếu Mỹ, 1/32, Tick, 32nds fractions, 99-24+]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# US Thirty Seconds Quotation

## Sự Kì Dị Phi Thập Phân của Trái Phiếu Hoa Kỳ

Trong khi toàn bộ giới Tài chính trên Hệ mặt trời đã chuyển sang mã Thập phân (Decimal) (như 99.75), thị trường lõi là **Trái phiếu Chính phủ Mỹ (US Treasury Market)** vẫn ngang ngạnh duy trì hệ đếm Dị biệt: **Phân số thập lục 1/32 (Thirty-seconds)**. [extracted] [[Fixed Income - Alexander During-17.pdf#page=16]]

Nguồn gốc sâu xa bắt nguồn từ việc Cắt đôi mảnh tiền kim loại cho dễ chia (cắt bốn dễ hơn cắt mười). Khủng khiếp thay cái Di sản đó in hằn sâu tới mức toàn thế giới phải khom lưng nhẩm toán!

### Cách đọc Mã Cược Mạng US
Giá đập vào mặt bạn sẽ có cấu trúc: `Phần Nguyên - Phần 1/32 cộng thêm phụ gia`

Ví dụ: **Biển giá 99-24**
- 99 là 99% mệnh giá (Par).
- 24 có nghĩa là rớt thêm $24/32$ của 1%.
- Kết quả ở não trái: $99 + 24/32 = 99.75\%$

Thanh khoản càng cuồng loạn, cái tick 1/32 (tương đương 3 cents cho tờ $100) đâm ra... QUÁ TO! Trader phanh thây nó mỏng hơn nữa sinh ra biến thể: **Ký hiệu Dấu Cộng (+)** và **Bát phân**. [extracted] [[Fixed Income - Alexander During-17.pdf#page=16-17]]
- **Biển Giá 99-24+:** Dấu `+` ám chỉ một nửa của 1/32. Tức là thêm $1/64$. Phép tính: $99 + 24/32 + 1/64 = 99.765625\%$.
- **Biển Giá 99-245:** Số 5 chót đuôi thay cho chữ "5 phần 256" (tức $5/8$ của 1/32). Phép tính: $99 + 24/32 + 5/256 = 99.76953125\%$. [extracted] [[Fixed Income - Alexander During-17.pdf#page=17]]

Ảo giác đẫm máu: 99-244 CHÍNH LÀ 99-24+. Không bao giờ có chuyện tồn tại 99-248 (vì 8/8 của 1/32 sẽ nhảy số thành thẳng 99-25!) [extracted] [[Fixed Income - Alexander During-17.pdf#page=17]]

Tuy nhiên, Sàn phái sinh CBOT Options lại có truyền thuyết Option riêng... Chữ số thứ ba ở CBOT lại là Quarter (1/4 của 1/32). (Ví dụ 99.245 bên CBOT tức là $0.5 \times 1/32$, vô tình lặp lại Dấu + bên Bond nguyên gốc). Ma trận! [extracted] [[Fixed Income - Alexander During-17.pdf#page=17]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=16-17]] — Cú "mind-blown" về cơ chế bẻ nhỏ Thirty-Seconds pricing, plus, and eighths.
