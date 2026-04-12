---
type: mechanism
trigger: "Đánh giá các động lực giá cả nền kinh tế"
output: "PT kiểm soát: MV = PY và vi phân hàm số tạo 3 biến quyết định"
constraints: ["Không mang tính ứng dụng thực tế cao do M bị mâu thuẫn định nghĩa"]
sources: ["Fixed Income - Alexander During-7.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 6
---

# Quantity Equation Of Money

## Phương trình gốc

Nền tảng của các chính sách nhắm mục tiêu lạm phát bắt nguồn từ **Phương trình Lượng tiền** (Quantity equation of the price level): [extracted] [[Fixed Income - Alexander During-7.pdf#page=4]]

$$MV = PY$$

Trong đó:
- $M$: Cung tiền (Money stock)
- $V$: Tốc độ quay vòng tiền (Velocity of money)
- $P$: Mức giá cả (Price level)
- $Y$: Tổng khối lượng hàng hóa dịch vụ giao dịch (Proxy cho GDP trừ hao kho tồn)

Nó biểu thị: *Tổng trị giá của mọi thứ được mua (PY) phải bằng với lượng tiền được cầm trao tay để đổi lấy (MV).* [extracted] [[Fixed Income - Alexander During-7.pdf#page=4]]

## Đạo hàm vi phân giá (Price total differential)

Đạo hàm để lấy $P$ làm biến rễ (Equation 6.2): [extracted] [[Fixed Income - Alexander During-7.pdf#page=4]]

$$ dP = \frac{M}{Y}dV + \frac{V}{Y}dM - \frac{MV}{Y^2}dY $$

Lạm phát (giá cả cao hơn - $dP$) có thể sinh ra từ:
1. $dV$ tăng (Vòng quay tiền nhanh đi)
2. $dM$ tăng (Tăng cung tiền dư)
3. $dY$ giảm (Giảm sản lượng sản xuất)

### Tính kém hữu dụng

Các nhà kinh tế thống nhất rằng biến $dV$ **không thể kiểm soát**. Biến $dM$ và $dY$ dẫn tới mâu thuẫn khổng lồ tạo nên sự chia rẽ học thuyết (xem [[Monetarist_Vs_Keynesian_Monetary_Views]]). 

Hơn nữa, phương trình mang nặng tính hư cấu vì $V$ thực tế là **không thể quan sát (unobservable)**, tạo ra nghịch lý là phương trình này thường chỉ được dùng nghịch lại để đi tìm định nghĩa cho $V$ chứ ít dùng để hoạch định chính sách thực thủ. [extracted] [[Fixed Income - Alexander During-7.pdf#page=5]]

## Nguồn

- [[Fixed Income - Alexander During-7.pdf#page=4]] — Equation 6.1 (MV=PY) & Equation 6.2 (Differential)
- [[Fixed Income - Alexander During-7.pdf#page=5]] — Fictional aspect of left side variables
