---
type: mechanism
trigger: "NHTW tạo ra một lượng tiền cơ sở mới nhỏ"
output: "Lượng cung tiền xã hội nở gấp nhiều lần so với nguồn"
constraints: ["Lý thuyết nhiều hơn thực tiễn do việc ngân hàng sử dụng tiền bù trừ cần central limit"]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Money Multiplier Formula

## Cơ chế

Lượng "tiền cơ sở" hay high-powered money trong một nền kinh tế được các ngân hàng thương mại "**nhân lên**" vô hạn thông qua thao tác cấp credit.

Ví dụ: Bạn gửi 10 vàng. Ngân hàng cất 1 đồng làm dự trữ (reserve = 10%) → cho vay 9 đồng. 9 đồng đó lại được deposit vào một ngân hàng → Giữ dự trữ 0.9, cho vay lại 8.1 → Cứ thế. Tổng cung ứng là $10 + 9 + 8.1 ...$ [extracted] [[Fixed Income - Alexander During-5.pdf#page=13]]

### Công thức: Equation 4.3

Giới hạn lý thuyết cho tổng lượng tiền ($M$) tạo ra từ 1 deposit gốc với tỷ lệ dự trữ ($r$) được hội tụ bởi chuỗi vô hạn: [extracted] [[Fixed Income - Alexander During-5.pdf#page=13]]

$$ M = \lim_{n\to\infty} \sum_{k=1}^n \frac{1}{(1+r)^k} = \frac{1}{r} $$

## Tính ứng dụng thực tế

Trên thực tế, theo Düring, công thức **monetary multiplier** này phần nhiều có giá trị lý thuyết vì các giao dịch thanh toán Liên ngân hàng thường phải đụng trần tài sản bằng tiền thật tại trung ương (hoặc hard currency). Việc này giới hạn mức giới hạn trần thực tế của Money multiplier. [extracted] [[Fixed Income - Alexander During-5.pdf#page=13-14]]

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=13]] — Ví dụ chuỗi vàng, Equation 4.3
- [[Fixed Income - Alexander During-5.pdf#page=14]] — Limit in practical applications
