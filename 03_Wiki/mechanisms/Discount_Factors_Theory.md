---
type: mechanism
aliases: [Df(t), Chiết khấu, Dòng tiền chiết khấu]
trigger: "Giá trị của 1 đồng tiền nhận được ở thời điểm t trong tương lai không bằng với 1 đồng hôm nay"
output: "Quy đổi tất cả về giá trị hiện tại thông qua Hệ số chiết khấu"
constraints: ["Định giá dựa trên thanh khoản, rủi ro lạm phát, rủi ro đối tác và chi phí cơ hội"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# Discount Factors Theory

## Trái tim của Phân tích Cố định (Fixed Income)

Dù thị trường hay quen mồm nói chuyện với nhau bằng Lãi suất (Interest rates), nhưng lãi suất quá phức tạp (vì thay đổi theo kỳ hạn và quy chuẩn đếm ngày). Trái tim thực sự của toàn bộ học thuyết định giá là **Discount factor** $Df(t)$. [extracted] [[Fixed Income - Alexander During-14.pdf#page=2-3]]

$Df(t)$ đại diện cho câu hỏi: *Tôi nên bỏ ra bao nhiêu cents ngay bây giờ để mua lời hứa sẽ nhận được tròn 1 Đôla từ chính phủ vào thời điểm $t$ trong tương lai?*

### Ý nghĩa kinh tế
Discount factor trừng phạt giá trị tương lai dựa trên 4 mũi nhọn ma sát:
1. Lạm phát (Inflation)
2. Rủi ro quỵt nợ của đối tác (Credit risk)
3. Rủi ro chốt lãi sớm (Interest rate risk - nhỡ ngày mai lãi ngân hàng tăng cao hơn)
4. Sự ưu tiên thanh khoản (Liquidity preference) [extracted] [[Fixed Income - Alexander During-14.pdf#page=2]]

### Rào cản Kinh tế học vi mô
Theo lý thuyết, Hệ số chiết khấu $Df(t)$ của cùng 1 nhà phát hành phải là Độc nhất (Unique), nếu không thì giới Arbitrage sẽ lao vào mua thấp bán cao ăn chênh lệch phi rủi ro. Tuy nhiên, thị trường thực tế đầy rẫy ma sát: Muốn khống chế giá, bạn phải Vay (Borrow) được tờ giấy đó để Bán khống (Short). Mà việc vay giấy cực tốn kém phí Repo, khiến lợi nhuận Arbitrage bị nuốt chửng, do đó $Df(t)$ ngoài đời đôi khi lồi lõm phi lý. [extracted] [[Fixed Income - Alexander During-14.pdf#page=3]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=2-4]] — Lý luận triết học về thời gian của Tiền và những ma sát ngăn chặn Arbitrage tuyệt đối.
