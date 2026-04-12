---
type: mechanism
aliases: [Quoted margin, Độ trễ Reset, Reset lag, In-arrears FRN, Spread biên]
trigger: "Hôm nay là Ngày 15 bắt đầu kỳ tính chốt lãi FRN, nhưng tỷ giá Repo Index của hôm nay đến hai ngày sau mới thanh toán. Lấy mốc nào để gán (Reset) Coupon?"
output: "Dùng Lookback Lag T-2 để chốt giá, đảm bảo dòng tiền lãi sẽ rơi xuống đúng hạn"
constraints: ["Nếu dùng cấu trúc In-arrears (chốt lãi trễ bét nhè vào ngày thanh toán), tờ Bond sẽ phải giao dịch theo giá dơ (dirty price)"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# FRN Coupon Reset Mechanics

## Đồng Hồ Báo Thức Của Coupon Tương Lai

Việc Gán lãi suất (Reset) của FRN đòi hỏi một bộ Luật ngặt nghèo về Timeline. 
Công thức tính Coupon kỳ $i$:
$$C_i = R(t_i - 2) + \mu$$
*(Trong đó $\mu$ là Quoted Margin - Phần Spread tín dụng của nhà phát hành cộng thêm trên nền Benchmark).* [extracted] [[Fixed Income - Alexander During-18.pdf#page=2]]

### Rào Cản T-2 Định Mệnh
Vì thị trường tiền tệ (Money Market) mất $T+2$ ngày hì hục quyết toán lệnh, nên Lãi suất tại điểm ngày bắt đầu sinh lãi $T$ thực chất phải quay ngước Cỗ máy thời gian Lùi lại nhìn Bảng điện của Ngày Hôm Kia ($T-2$). Một số cấu trúc FRN điên rồ thậm chí dồn độ lùi (Lag) tới tận 20 ngày kinh doanh (gần nguyên một tháng). [extracted] [[Fixed Income - Alexander During-18.pdf#page=2]]

### In-arrears FRNs (Chốt Xổ Số Phút Chí Tử)
Đây là cấu trúc "Nhờn" nhất: Khoảng thời gian sinh lãi cứ chạy mải miết, và Tác giả dời ngày Fixing Coupon xuống tận cái ngày Trả Tiền Lãi (Payment Date)! 
**Hậu quả toán học:** Trong suốt cái kì sống ngắc ngoải ấy, không ai biết chính xác Lãi đang dồn (Accrued interest) cựa quậy ở số bằng bao nhiêu. Thế nên, thị trường phẫn nộ không thể yết giá chúng bằng Clean Price, In-arrears FRNs bị ép giao dịch nuy trần bằng **Giá bẩn (Dirty Price)**. [extracted] [[Fixed Income - Alexander During-18.pdf#page=2]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=2-3]] — Giải phẫu lịch trình fixing, độ trễ quan sát T-2, và cái giá phải trả của In-arrears (Dirty price only).
