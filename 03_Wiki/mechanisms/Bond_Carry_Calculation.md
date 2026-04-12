---
type: mechanism
aliases: [Tính toán độ bù Carry, Carry trade trong Bond, Spread Roll-down, Lãi ròng đòn bẩy Repo]
trigger: "Mua khống Bond và đem đi Repo, tiền đẻ ra do Coupon thừa sức bù tiền nộp cho bên cắm chứng"
output: "Gỡ lại bằng độ chênh giữa Spot Yield và Forward Yield, quy kết tính toán Carry cho Quỹ đầu cơ"
constraints: ["Việc ước lượng Carry bằng chênh lệch Spot vs Repo Yield x Số ngày ôm hàng chỉ là cách tiếp cận xấp xỉ thô thiển"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Bond Carry Calculation

## Gieo Gió Lãi Gộp Đục Khoét Repo
Trong chiến trường Fixed Income, Cỗ máy kiếm tiền thụ động vĩ đại nhất của các Quỹ Đầu Cơ là **Carry**.
Về cơ bản: Bạn mua một trái phiếu $100 triệu, bạn có tự bỏ tiền riêng ra không? KHÔNG. Bạn bấm lệnh vay Nóng Repo (Lãi suất rất rẻ) để đập hộp tờ Bond này (Lãi suất cao hơn do bù rủi ro kỳ hạn). Khoản chênh lệch gọi là Income gác túi (Carry). [extracted] [[Fixed Income - Alexander During-17.pdf#page=31]]

### Công thức Gốc Máu Lạnh (Forward Method)
Định nghĩa hàn lâm nhất của Carry được khắc vào đá như sau:
$$Carry = Spot\ Price\ (Kéo\ Tươi) - Forward\ Price\ (Tương\ Lai)$$
Quy chiếu vào hệ Mĩ Tộc (US): 
$$Carry = Forward\ yield - Spot\ yield$$
[extracted] [[Fixed Income - Alexander During-17.pdf#page=31]]

#### Phương Trình Định Giá Đi Tới Bến (Arbitrage-Free Forward Pricing)
Giả định tờ Bond không quẳng cho bạn đồng Coupon rớt rãi nào từ T0 đến thời điểm xả hàng Tf. Giá Tương lai buộc phải tuân theo Định lý Không 차차 (No-Arbitrage) gánh cước Repo ($r$) bít bùng:
$$P_f = \frac{P_0}{Df(t_0, t_f)} = P_0 (1 + r(t_0, t_f)DCF(t_0, t_f))$$
Lãi Repo kéo tời lôi giá $P_f$ văng lên. [extracted] [[Fixed Income - Alexander During-17.pdf#page=31]]

Nhưng! Nếu xui rủi ở khúc giữa có một thỏi Coupon $C$ văng trúng mặt, bạn bắt buộc phải cầm Cục Coupon đó ném ngược vào cỗ máy Repo hòng tái đầu tư ép ra tiền! [extracted] [[Fixed Income - Alexander During-17.pdf#page=32]]
$$P_f = \frac{P_0}{Df(t_0, t_f)} - C \times \frac{DCF(t_{i-1}, t_i)}{Df(t_i, t_f)}$$

### Xấp Xỉ Giới Buôn Đạn Mù (Quick Approximation)
Quá phức tạp? Giới ngân hàng phán: Kệ mẹ công thức, chém tắt mẹ nó đi!
*Carry Xấp Xỉ* = `(Yield Của Trái Phiếu - Lãi Suất Repo) x Thời Gian Nắm Giữ`

Bất trị thay, nếu ép biểu diễn toán học, cái Xấp xỉ Nông dân này ĐÁNH BẠI ĐƯỢC CHUẨN MỰC nếu thay thế "Yield Của Trái Phiếu" từ ngai vàng Compound Yield lùi xuồng **Simple Yield**! (Vì Simple yield đã dội vào đầu mồi câu phép trừ Hao Mòn Tuyến Tính Capital Loss y hệt bản chất bồi đắp của Repo). [extracted] [[Fixed Income - Alexander During-17.pdf#page=32]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=31-32]] — Carry equations base on spot and forward difference. Repo curve implementation and approximating tricks.
