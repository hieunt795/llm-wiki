---
type: mechanism
aliases: [Compound yield, Moosmuller yield, Simple yield, C/P, Yield-to-maturity, Bond-equivalent yield, BEY, IRR của bond]
trigger: "Trái phiếu có 4 dòng tiền ở đủ mọi ngày t khác nhau, làm sao để so sánh tỷ suất lợi nhuận cho chung một mâm Benchmark?"
output: "Gắn 1 thông số Lợi suất Giả Định duy nhất bôi phẳng toàn bộ dòng thời gian"
constraints: ["Compound Yield mặc định Đường cong Lãi suất LÀ MỘT ĐƯỜNG THẲNG PHẲNG LỲ (Flat Curve) - sai số kinh khủng với thực tế"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Yield Calculations Variants

## 4 Lăng Kính Ánh Xạ Đường Cong Lợi Nhuận

Trong rổ thuật toán Fixed Income, chẳng có gì ảo giác bằng **Yield**. Bản chất nó chỉ là công cụ nặn lại mức giá $P$ (quá lộn xộn các thanh Coupon) về thành MỘT con số tỷ suất sinh lời phần trăm quy chuẩn dễ thở, dễ khoe khoang.

### 1. Running Yield (Bóc vỏ mì ăn liền)
$$y = \frac{C}{P}$$
*Lợi suất tức thời (Dividend-yield style)*: Nó vứt sọt rác toàn bộ cái Khoản Gốc khổng lồ mất đi hay vớt lại vào ngày đáo hạn. Nếu bạn mua lúc Trái phiếu 101, ăn Coupon 4%, thì bạn có lãi suất "Mì gói" là $4/1.01 \approx 3.96\%$. [extracted] [[Fixed Income - Alexander During-17.pdf#page=24]]

### 2. Simple Yield (Trường phái Samurai Nhật Bản)
$$y = \frac{C - \frac{P - 100}{t}}{P}$$
Bắt đầu khôn hơn, nó lôi khoản Tiền Lỗ/Lãi do mua sai mệnh giá (Capital Loss/Gain) đem cưa đôi xẻ dọc tạt đều vào các năm còn lại t. Nhật Bản đặc biệt cuồng công thức này! [extracted] [[Fixed Income - Alexander During-17.pdf#page=24]]

### 3. Compound Yield (Ma vương quy chuẩn - IRR)
$$P = \sum_i \frac{CF_i}{(1+y)^{DCF(t_s, t_i)}}$$
Chiết khấu chính quy chuẩn chỉ mọi dòng tiền $CF$! 
*Nhánh rẽ kỳ quái: Của Đức sinh đạo:* **Moosmüller Yield**. Cải dao bằng cách tính cái kỳ ngắn ngủn đầu tiên (từ hôm nay đến Coupon gần nhất) *theo kiểu Cắt Lãi Tiền Gửi Chợ Đen (Money Market tuyến tính)* còn các năm xa mới mũ Compound bình thường. Tại Đức, 1 tháng cầm hơi trước mốc Coupon gọi là Simple Money, không ép Loga! [extracted] [[Fixed Income - Alexander During-17.pdf#page=24-25]]

### 4. Bond-Equivalent Yield (Trò mèo Annual hoá BEY)
$$y_B = 2 \times (\sqrt{1+y} - 1)$$
Bọn Mỹ trả Coupon Semi-Annual (Bán niên 6 tháng lận). Khách hàng chửi rủa đòi đem đọ mặt ngửa với 1 thằng Mỹ trả Annually 1 năm ăn 1 lần. Công thức cắt BEY luôn kéo Yield xuống thấp hơn xíu so với Compound Yield ($y^2/4$). [extracted] [[Fixed Income - Alexander During-17.pdf#page=25]]

## Khe Hở Đọa Đày Của Compound Yield
Giao cho 1 cái Compound Yield nhiệm vụ đánh giá sự giàu có, nó giả định trắng trợn:
1. Bạn có thể Tái đầu tư mọi Coupon dớt dãi rụng xuống ở mức Rate ĐÓ! (Điều hư ảo). [extracted] [[Fixed Income - Alexander During-17.pdf#page=25]]
2. Đường cong Lãi suất (Yield Curve) phản ánh rủi ro Thời gian, tức là thằng ôm nợ 10 năm Yield phải khác xa 1 năm. Nhúng nguyên con cá chép vĩ đại 10 năm vào một vạc dầu Yield duy nhất y... vô tình đánh sập mọi chiết khấu của Đường Giá Zero-coupon cong! (Vạch mặt trò lường gạt: Tại sao lại giả định Lãi 1 năm bằng với lãi 10 năm trên cùng trái phiếu?) [extracted] [[Fixed Income - Alexander During-17.pdf#page=26]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=24-26]] — Running, Simple, Compound, Moosmuller and BEY. Criticisms of the internal rate of return yield measure.
