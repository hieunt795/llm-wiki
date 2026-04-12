---
type: mechanism
aliases: [FRA, Hợp đồng kỳ hạn lãi suất, Forward-rate agreement]
trigger: "Muốn ôm giữ mức lãi suất phòng thủ cho một khoản vay ở thì Tương lai"
output: "Ký hợp đồng Swap chênh lệch tĩnh với Libor, tính chênh lệch và Thanh toán ngay lập tức ở lúc bắt đầu kỳ hạn"
constraints: ["Bất đối xứng đánh bù trừ trả tiền ngay lúc xuất phát kỳ (Start of the period)"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# Forward Rate Agreement

## Lãi suất phòng hờ đếm nấc (FRA)

**FRA (Forward-rate agreement)** là ông cố tổ của các sản phẩm phái sinh trên lãi suất cơ bản (như [[LIBOR_Benchmark_Mechanism|Libor]]). Nó là một giao kèo cá cược thuần túy hai chiều (Bilateral) được thiết kế đặc thù cho ai sợ hãi lãi suất. [extracted] [[Fixed Income - Alexander During-14.pdf#page=8]]

### Cấu trúc
Hai bên đồng ý rằng:
- Bên "Buyer" trả một lãi suất chết nêm móng ($r_{FRA}$).
- Bên "Seller" trả lãi suất nổi chìm theo thị trường ($r_{fix}$ — thường dính Libor).

Luật của chợ tiền đẻ ra chữ "Buyer" khá trái ngược với logic bond. "Buyer" ở đây mang nghĩa là thằng Mượn nợ để Hút tiền vào người. Khi lãi suất thị trường $r_{fix}$ tăng lên, Buyer cười mỉm vì được FRA rớt tiền đền bù lại, đỡ đạn cho phần lãi tiền thực nó đi mượn bị đội. [extracted] [[Fixed Income - Alexander During-14.pdf#page=8]]

### Quái chiêu: Cash Settled trả trước
Khác với thế giới thực nơi mượn tiền thì Tới mút mùa mới trả Lãi, một cái FRA **Thử nghiệm và trả tiền NGAY KHI CHIẾC CÂN BẮT ĐẦU CHẠY**.
- Ví dụ cái 6M9M FRA: (Trong 6 tháng nữa mở vị thế, và đếm tiền mượn trong 3 tháng). Lúc đồng hồ điểm giây chạm 6 tháng, tỷ giá trần trụi Libor $r_{fix}$ nhả số.
- Vụ chênh lệch giữa $r_{fix}$ và $r_{FRA}$ được khóa cứng, và dòng tiền bồi thường được **đạp chiết khấu ngược (discounted) bằng mẫu số $(1+r_{fix})$** thu thẳng vào túi mớm ngay lúc bắt đầu (Start of period) móc túi nhau. Không cọ chờn nợ. [extracted] [[Fixed Income - Alexander During-14.pdf#page=8]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=8-9]] — Kiến trúc định giá FRA và quy chế đóng sổ Discounted trả trước độc lạ của Money Market so với nợ dân sự.
