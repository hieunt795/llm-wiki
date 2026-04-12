---
type: mechanism
aliases: [Dự phóng chính sách, Term Risk Premium, O/N Rolling Account]
trigger: "NHTW thay đổi lãi suất từng khoang 0.25%, nhưng đường cong lãi suất trên thị trường lại chạy trơn mượt"
output: "Đường cong kỳ hạn chính là xác suất đặt cược vào đường đi của Lãi suất qua đêm, cộng thêm tiền bo rủi ro kỳ hạn"
constraints: ["Đường cong đi ngang không có nghĩa là lãi suất giữ nguyên, nó đang dự báo lãi suất sẽ giảm để bù trừ vào rủi ro kỳ hạn"]
sources: ["Fixed Income - Alexander During-16.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 15
---

# Policy Rate Expectations

## Thuật Ngoại suy Quả cầu pha lê

Chỉ định Lãi suất chính sách (Policy Rate) là đặc quyền của [[Central_Bank]]. Thông thường nó là các lãi suất siêu tốc như Tỷ giá qua đêm ([[Federal_Funds_Rate]]). Làm sao từ lãi suất qua đêm này, thị trường vẽ ra được nguyên một đường cong 1 năm, 2 năm, 10 năm? Giải pháp của dân định giá là giả lập một **Tài khoản Ký quỹ Lăn vòng qua đêm (Overnight Rolling Account)**. [extracted] [[Fixed Income - Alexander During-16.pdf#page=4]]

### Nghệ thuật khớp nối Probability
Khi FED dự tính thay đổi lãi suất, họ không thay đổi bất kỳ ngày nào mà chỉ đổi tại các **kỳ họp (Meeting Dates)**. 
- Không tự nhiên có cái rate nào nhích 10 basis points. Nếu hợp đồng tương lai ngụ ý ra mức chênh 10 bp, điều đó có nghĩa thị trường đang **Cược 40% xác suất FED sẽ tăng 25 bp**. (10/25 = 40%). [extracted] [[Fixed Income - Alexander During-16.pdf#page=5]]
- Mô hình phải khớp Lịch họp của NHTW vào lịch làm việc. Tại bất cứ điểm nào không có lịch họp, lãi suất được neo phẳng.

### Bước ngoặt: Term Risk Premium (Tiền bo cút nhốt)
Nếu đường cong Lãi suất chỉ đơn thuần là Cược vào tương lai Policy rate, thì mọi thứ đã quá dễ dàng. Cú lừa vĩ đại nằm ở khái niệm **Term Risk Premium** (Phần bù rủi ro kỳ hạn). [extracted] [[Fixed Income - Alexander During-16.pdf#page=5-6]]

- Một gã cho vay qua đêm (O/N) mỗi sáng mai thức dậy đều nắm trong tay tùy chọn: Dừng không cho vay nữa.
- Một gã đem tiền đi khóa vào kì hạn 6 tháng đã tự bẻ gãy quyền lựa chọn (optionality) của đời mình. Gã bị trói tay nếu ngày mai FED nổi điên tăng vọt lãi suất lên 5%.
- Do đó, để dụ dỗ gã khóa tiển 6 tháng, thị trường bắt buộc phải nhét thêm một phần **Term Risk Premium** dương vào lãi suất kỳ hạn.

> [!WARNING] **Trực giác Bị Lừa Dối**
> Sự hiện diện của Term Risk Premium ép đường cong thường phải Dốc Lên (Upward sloping). Rất hệ trọng: Nếu bạn nhìn thấy một đường cong nằm PHẲNG LÌ (Flat curve), điều đó **không** có nghĩa thị trường cược lãi suất Đứng Yên. Nó có nghĩa: Thị trường đang cược **Lãi suất Policy sẽ CẮT GIẢM** để cấn trừ lại toàn bộ độ dày của Term risk premium đang trương nở theo thời gian! [extracted] [[Fixed Income - Alexander During-16.pdf#page=6]]

## Nguồn

- [[Fixed Income - Alexander During-16.pdf#page=4-6]] — Cơ chế mô phỏng O/N Account để fit curve, diễn dịch Xác suất thay đổi rate, và Nghịch lý đường cong bằng phẳng ngụ ý rate cut do Term risk premium.
