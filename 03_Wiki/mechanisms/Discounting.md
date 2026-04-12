---
type: mechanism
trigger: "Sở hữu một hối phiếu trả sau muốn chuyển thành tiền mặt tức thì"
output: "Người nắm giữ nhận được tiền nhỏ hơn face value"
constraints: ["Bị trừ phần bù rủi ro và lãi suất giá trị thời gian của tờ hóa đơn"]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Discounting

## Cơ chế

Nhà buôn ngoại thương khi nắm giữ [[Bills_Of_Exchange]] có thể bán chúng lại cho các ngân hàng để lấy **tiền mặt ngay lập tức (immediate cash)**. Đây là **chức năng cốt lõi lâu đời nhất của ngân hàng**. [extracted] [[Fixed Income - Alexander During-5.pdf#page=11]]

Lượng tiền mặt được trả luôn **nhỏ hơn** tổng giá trị danh nghĩa (face value) của tờ hóa đơn.

### Công thức: Discount Factor

Tỷ lệ giữa tiền nhận ngay và giá trị danh nghĩa được gọi là **Discount Factor** (Equation 4.2): [extracted] [[Fixed Income - Alexander During-5.pdf#page=11]]

$$ \text{Discount factor} = \frac{\text{Cash payment}}{\text{Face value}} $$

Ngân hàng tính hệ số chiết khấu dựa trên **Lãi suất chiết khấu (Discount rate)** — thuật ngữ được sử dụng đến nay với các tính chất rộng của trái phiếu rủi ro.

### Rediscounting

Nếu ngân hàng (đã chiết khấu) tiếp tục bán nó vào thị trường thứ cấp hoặc cho NHTW khác, hành vi đó gọi là **Rediscounting (tái chiết khấu)**. NHTW thường sử dụng tái chiết khấu để bơm thanh khoản. [extracted] [[Fixed Income - Alexander During-5.pdf#page=11]]

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=11]] — Discount factor equation, Rediscounting
