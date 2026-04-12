---
type: mechanism
aliases: [Global note, CSD, LCSD, GCSD, Lưu ký chứng khoán]
trigger: "Thị trường cần tốc độ giao dịch chứng khoán siêu tốc mà không thể cầm giấy chạy ship ngoài đường"
output: "Chứng khoán vật lý bị gom làm một cục nằm chết dí tại CSD, mọi giao dịch ghi có/nợ trên sổ điện tử"
constraints: ["Đòi hỏi cấp bậc tin tưởng (Trust agreement) nối vòng giữa CSD và Clearer"]
sources: ["Fixed Income - Alexander During-11.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 10
---

# Book Entry Securities System

## Cơ chế Đâm sổ điện tử

Giao dịch chứng khoán hiện đại quá nhanh để chờ các mẩu giấy chứng nhận tráo tay nhau. Thế giới tiến lên hình thái **Book-entry form**. [extracted] [[Fixed Income - Alexander During-11.pdf#page=4]]

### Cách thức hoạt động
Sự kết hợp hoàn hảo giữa logic của pháp lý [[Bearer_Vs_Registered_Securities]]:
1. **Phát hành (Global Note):** Về mặt pháp lý, Tổ chức in duy nhất **một** tờ Chứng khoán vô danh to đùng (global note) có giá trị bao trùm toàn bộ một lô phát hành ngàn tỷ.
2. **Lưu ký (CSDs):** Đem tờ Global Note đó cất sâu xuống hầm bảo mật của một Tổ chức lưu ký đáng tin cậy gọi là ***Central Securities Depository (CSD)***. Hệ thống này phân làm 2 cấp: Local CSD (nội bộ quốc gia, ví dụ Monte dei Titoli ở Ý, Bundesschuldenverwaltung ở Đức) và Global GCSD (quốc tế). [extracted] [[Fixed Income - Alexander During-11.pdf#page=4-5]]
3. **Thanh toán bù trừ (Clearing House):** Việc mua bán tài sản không đụng chạm gì tới cái tờ giấy nằm trong hàm. Các nhà Thanh toán bù trừ (như Euroclear hay Clearstream) móc kết nối Trust agreement vào CSD. Khi 2 người dùng mua bán lệnh, Clearer chỉ cần thay đổi "Entry" (số liệu ghi đè sổ) trên phần mềm máy tính.

Chính nhờ hệ thống dây xích này, một trader ở Nhật mua Trái phiếu Chính phủ Đức sẽ thấy chứng khoán vào tk mình nhấp nháy trong 10 mili-giây, còn tờ giấy thực tế của nước Đức vẫn nằm chết dí vĩnh viễn ở hầm hầm lưu ký Bundesschuldenverwaltung. [extracted] [[Fixed Income - Alexander During-11.pdf#page=5]]

## Nguồn

- [[Fixed Income - Alexander During-11.pdf#page=4-5]] — Khái niệm Global Note, CSDs và các tay chơi Clearstream/Euroclear.
