---
type: mechanism
aliases: [Cash stub, Stub rate, Mảnh cụt tiền mặt, Lãi suất neo t0]
trigger: "Hợp đồng tương lai lãi suất (Futures) chỉ bắt đầu vào các ngày IMM (tháng 3,6,9,12). Vậy khoảng trống từ hôm nay đến cái ngày IMM đó lấy lãi suất ở đâu ra?"
output: "Lấy lãi suất tiền gửi (deposit rate) ngoài đời thực làm cái mỏ neo nhổ neo"
constraints: ["Tuyệt đối không thể dùng quy tắc nội suy để đoán bừa khúc này vì nó dính trực tiếp đến O/N rate của hiện tại"]
sources: ["Fixed Income - Alexander During-16.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 15
---

# Cash Stub Rate

## Cái Mỏ Neo Của Đường Cong

Trong nghệ thuật dệt đường cong lãi suất (Curve construction), nguồn dữ liệu phong phú nhất và thanh khoản nhất để chiết xuất [[Forward_Rates_Derivation|Lãi suất kỳ hạn]] là Chuỗi hợp đồng tương lai ([[Money_Market_Futures|Futures strip]]). [extracted] [[Fixed Income - Alexander During-16.pdf#page=2]]

Tuy nhiên, có một lỗ hổng thời gian tử huyệt: Futures luôn có ngày đáo hạn quy chuẩn (ví dụ: [[IMM_Dates_And_Tick]]). Nếu hôm nay là một ngày bất kỳ giữa tháng, Futures hợp đồng gần nhất sẽ không bắt đầu "chạy" ngay lập tức mà phải đợi đến ngày IMM tiếp theo. Khoảng trống thời gian từ **Hôm nay ($t_0$)** đến **Ngày bắt đầu của hợp đồng Futures gần nhất ($t_1$)** được lấp đầy bằng một mảnh ghép gọi là **Cash stub** (hay **Stub rate**). [extracted] [[Fixed Income - Alexander During-16.pdf#page=2]]

- **Stub rate** KHÔNG lấy từ Futures, mà phải kéo từ thị trường tiền gửi thả nổi (Cash Deposit market).
- Kể từ ngày $t_1$ trở đi, tỷ giá ngụ ý của Futures mới được nối vào làm Lãi suất kỳ hạn, kế thừa từ $t_1$ đến $t_2, t_3...$ theo công thức đệ quy:
  $$1 + r(t_0, t_{i+1})DCF(t_0, t_{i+1}) = [1 + r(t_0, t_i)DCF(t_0, t_i)] \times [1 + r(t_i, t_{i+1})DCF(t_i, t_{i+1})]$$

Chữ *Stub* mang ý nghĩa "Mẩu thừa/Mảnh cụt". Nó đóng vai trò là Viên Gạch Nền Móng duy nhất neo toàn bộ Đường cong nội suy ảo lặp lại xuống mạn thuyền tỷ giá thực tế của ngày hôm nay. Thiếu Stub rate, cả hàm đệ quy không có điểm khởi tạo. [extracted] [[Fixed Income - Alexander During-16.pdf#page=2]]

## Nguồn

- [[Fixed Income - Alexander During-16.pdf#page=2-3]] — Sự cần thiết của Cash stub rate để vá khoảng trống rụng rời giữa mốc t0 và ngày bắt đầu của Libor futures strip đầu tiên.
