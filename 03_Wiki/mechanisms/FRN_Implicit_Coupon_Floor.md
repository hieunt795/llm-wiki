---
type: mechanism
aliases: [Sàn không âm, Coupon floor, Zero-floor, max(0, C)]
trigger: "Trong kỷ nguyên lãi suất âm (NIRP), chỉ số EURIBOR rớt thảm xuống -0.5%. Nếu trái phiếu FRN có Margin là +0.2%, Coupon sẽ là -0.3%. Người mua vác mồm lại đền tiền cho Công ty vay nợ?"
output: "Quên đi, pháp luật và sổ cái CSD cấm tiệt thanh toán đứt mạch. FRN luôn có Sàn Ảo (Implicit Floor) chặn cửa ở mức 0%"
constraints: ["Không có Zero-floor, FRN mang lãi suất âm sẽ biến thành vũ khí thảm sát đạn ngược cho Chủ nợ"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# FRN Implicit Coupon Floor

## Bức Tường Lửa Ngăn Đạn Đảo Chiều Lãi Suất Âm

Sau kỷ nguyên Nới lỏng định lượng cực đoan áp dụng chính phủ Âm (Negative Interest Rates), giới làm giá Trái phiếu FRN nhận ra lỗ hổng búa bổ của công thức Lõi: Lãi chuẩn bị âm sâu quá bóp nát cái Spread Margin, dìm Coupon lặn vào vùng Lãi Âm.

Nếu Coupon âm, Người Đi Vay bỗng nhiên trở thành Người Thu Tiền, và Giới Chóp Bu Cho Vay bị ép nộp vào mâm phạt!
Đại đa số khung pháp lý hành pháp (Jurisdictions) và Lưu ký chứng khoán Trung ương (CSDs) hoàn toàn **ngu loạn / không có tính năng hệ thống** xử lý thu tiền ngược thế này. [extracted] [[Fixed Income - Alexander During-18.pdf#page=3]]

Hệ quả là mọi Khế ước FRN hiện đại đều đúc ngầm vào một hàm max, còn gọi là **Zero-floor (Sàn 0%)**.
$$C_i = max(0, R(t_i - 2) + \mu)$$

Thế giới dù có đóng băng, kẻ cho vay ít nhất vẫn húp được 0 đồng chứ tuyệt k bị chảy máu ngược. Mức Sàn này không ai tước ép ở giá 0, các Issuer có quyền đặt Cap (trần) hoặc Floor (Sàn) ở trên mức 0 để tùy biến rủi ro độ võng. [extracted] [[Fixed Income - Alexander During-18.pdf#page=3]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=3]] — The legal and systematic necessity of writing implicit max floors into FRN indentures.
