---
type: mechanism
aliases: [Discount Margin, Điểm chí mạng FRN, Lợi suất FRN Mặc định, Biên chiết khấu]
trigger: "Trái phiếu FRN không có dòng tiền cố định nên không thể dùng Yield To Maturity, làm sao để so sánh độ sinh lời rủi ro của 2 tờ FRN với mức giá P bị trật khỏi mốc 100?"
output: "Dùng Discount Margin. Ép ra một con Margin ảo bù đắp sao cho Current Price đánh võng thẳng về Par!"
constraints: ["Ám hại: Phương pháp thị trường ấn định Discount Margin mù quáng tin rằng Đường cong Forward tịnh tiến phẳng, cấm tuyệt đánh đồng kì hạn xa tít mù tắp"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# Discount Margin FRN

## Sát Nhân Nhắm Mắt Của Thước Đo Thị Trường (Market Convention)

Vì cấu tạo của Trái phiếu FRN bắn văng dòng tiền (Cashflows) đi hoang không đoán định được, Lợi suất thuần (Compound Yield) rơi vào tuyệt vọng (Dead-end). Giới Finance phải móc túi ra công cụ thứ 2: Biên Chiết Khấu (**Discount Margin** $\mu '$). [extracted] [[Fixed Income - Alexander During-18.pdf#page=5]]

$\mu '$ là hằng số Rủi ro Tín Dụng (Mức Spread) được nín thở Gài cắm vào Mẫu số sao cho: Kéo cái Giá Cùi Bắp P lật lại Bằng Chỉnh Đỉnh PAR (100). [extracted] [[Fixed Income - Alexander During-18.pdf#page=5]]

### Lý Tính Thuần Túy (The True Arbitrage-Free Method)
Trong một vũ trụ Tuyệt Mĩ, ta phải xả nguyên chuỗi Df (Discount Factors) lấy từ Forward Curve (Đường Cong Đuổi Đỉnh):
$$\mu' = \mu - \frac{P - 100}{\sum DCF(t_{i-1}, t_i) Df(t_i)}$$
Nó hệt như công nghệ phân rã Asset Swap Spread (Chi phí hoán đổi tài sản). Nhạy cảm khốc liệt với Cuộc Khởi Lên Hay Sụp Xuống Của Yield Curve Đường Cong. [extracted] [[Fixed Income - Alexander During-18.pdf#page=5]]

### Quy Chuẩn Thị Trường (The Bloody Market Convention)
Ngặt nỗi, giới Market chê cách 1 đắt đỏ (Khó bóc Forward Curve). Nên thiên hạ lùa nhau dùng Công thức Giải Ngược Ép Ép Phẳng (Market Equation 17.10). [extracted] [[Fixed Income - Alexander During-18.pdf#page=5]]

Nó mù quáng cho rằng: *Rate R(tl) của Cuộc Fixing tháng này sẽ Bị Đóng Băng vĩnh hằng Tịnh Tiến Bất Diệt cho tới Ngày Đáo Hạn rụng rời cuối cùng!*
Nó vứt Sọt rác Độ Dốc của Đường cong Lãi (Flat Forward Equation). [extracted] [[Fixed Income - Alexander During-18.pdf#page=5-6]]

**Trái Đắng:** 
1. Việc đánh đồng độ nghiêng Curve khiến Discount margin dửng dưng vô cảm dù Đường Lãi vểnh đầu.
2. Dân Newbie đem Discount Margin của Thằng FRN đáo hạn 1 năm đem Khoét so găng Bằng Khít với DM của 1 Thằng FRN đáo hạn 10 Năm... Phỉ Báng Sách Vở Toán Học. Phá Rỗng (Methodologically incorrect!) [extracted] [[Fixed Income - Alexander During-18.pdf#page=6]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=5-6]] — So sánh tàn khốc giữa Discount margin theo lý thuyết Forward curve vs Market convention mù quáng flat curve.
