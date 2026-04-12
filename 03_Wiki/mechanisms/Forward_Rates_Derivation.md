---
type: mechanism
aliases: [Forward Rate, Forward Discount Factor, Lãi suất kỳ hạn]
trigger: "Biết lãi suất chạy 3 tháng và lãi suất chạy 6 tháng, vậy lãi suất của cục tiền bắt đầu chạy TỪ tháng thứ 3 ĐẾN tháng thứ 6 là bao nhiêu?"
output: "Dùng Discount Factor chia cho nhau để tránh lỗi ma trận phép nhân lãi suất"
constraints: ["Forward rates của deposit phải khớp hệ số ghép lãi (compounding) và Daycount chuẩn"]
sources: ["Fixed Income - Alexander During-16.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 15
---

# Forward Rates Derivation

## Xây cầu nối thời gian bằng Discount Factor

Trực giác thông thường khiến chúng ta thích cộng trừ Lãi suất (Interest rates) khi tính toán tương lai. Nhưng trong thế giới fixed income, mọi phép tính Forward Rate bắt buộc phải đi vòng qua **[[Discount_Factors_Theory|Discount Factor]]**. Tại sao? Vì chỉ có Present Value mới bù trừ đại số một cách hoàn hảo trong Không gian No-Arbitrage. [extracted] [[Fixed Income - Alexander During-16.pdf#page=1]]

Để tìm mức lãi suất kỳ hạn tương lai bắt đầu từ $t_1$ đến $t_2$:
Mệnh đề No-Arbitrage bắt buộc giá trị chiết khấu từ $t_2$ về $t_0$ phải bằng việc chiết khấu từng chặng $t_2 \to t_1$, rồi $t_1 \to t_0$:

$$Df(t_0, t_2) = Df(t_0, t_1) \times Df(t_1, t_2)$$

Trivially, phần Df chạy trong tương lai là:
**$$Df(t_1, t_2) = \frac{Df(t_0, t_2)}{Df(t_0, t_1)}$$**

## Từ Df dịch ngược ra Forward Interest Rate

Khi đã nắm trong tay $Df(t_1, t_2)$, ta chuyển nó trở lại ngôn ngữ giao tiếp của thị trường (Interest Rate) dựa vào quy ước trả lãi gốc:

1. **Với Simple Yield** (thị trường Money Market thông thường, act/360):
$$r(t_1, t_2) = \frac{1}{DCF(t_1, t_2)} \left( \frac{1 + r(t_0, t_2)DCF(t_0, t_2)}{1 + r(t_0, t_1)DCF(t_0, t_1)} - 1 \right)$$

2. **Với Discount Rate** (như thị trường T-bills bù trừ ngầm):
$$r(t_1, t_2) = \frac{1}{DCF(t_1, t_2)} \left( 1 - \frac{1 - r(t_0, t_2)DCF(t_0, t_2)}{1 - r(t_0, t_1)DCF(t_0, t_1)} \right)$$

## Nguồn

- [[Fixed Income - Alexander During-16.pdf#page=1-2]] — Toán học gốc của Forward Present Value và quy luật dịch ngược simple yield.
