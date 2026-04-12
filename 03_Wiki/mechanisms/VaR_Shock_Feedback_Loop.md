---
type: mechanism
trigger: "Giao dịch không biến động trong thời gian dài làm triệt tiêu phe cược giá xuống (short sellers)"
output: "Khi có sốc ngược hướng, phe Long đồng loạt vấp VaR limit dẫm đạp điên dại"
constraints: ["Năng lực hấp thụ của phe tạo lập thị trường (market makers) mỏng dần theo thời gian bình ổn"]
sources: ["Fixed Income - Alexander During-10.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 9
---

# VaR Shock Feedback Loop

## Cơ chế tạo vòng lặp sụp đổ

Điều rùng rợn của một chu kỳ êm ả lặp đi lặp lại (do Trung ương ghim giá ổn định) là các công cụ Quản trị rủi ro ([[Role_Of_Market_Volatility]]) bị thui chột. **VaR Shock (Cú sốc VaR)** là minh hoạ đẫm máu cho lý thuyết Minsky. [extracted] [[Fixed Income - Alexander During-10.pdf#page=16]]

### Đồ thị thời gian
1. Trong nhiều năm điệp khúc giảm lợi suất, các nhà đầu cơ Short (bán khống) thua lỗ và bị thanh trừng sạch sẽ khỏi thị trường. Toàn bộ người chơi đều đang Long (ôm hàng) với mức đòn bẩy khổng lồ (bởi vì volatility đang thấp, Value-at-Risk cho phép vay bão táp). [extracted] [[Fixed Income - Alexander During-10.pdf#page=16]]
2. Bất ngờ, một cú shock ngược hướng vĩ mô ập đến (Ví dụ mùa hè 2003, lợi suất Mỹ và Nhật bung mạnh do Fed úp mở đổi giọng).
3. Những ai đang Long bắt buộc phải dừng lỗ ngay tắp lự (stop-loss) theo luật **VaR limits**.
4. **Tuyệt cảnh:** Thị trường không còn bất kỳ Short-seller nào (những người vốn dĩ sẽ "mua đóng lệnh" - cover shorts để đỡ giá rơi). Lệnh bán tháo giẫm đạp vào hư không, đục lủng thanh khoản, tạo ra Feedback Loop đè giá rớt tự do khiến đợt VaR call thứ hai bị vỡ. [extracted] [[Fixed Income - Alexander During-10.pdf#page=16-17]]

Cú sốc VaR 2003 ở thị trường Nhật JGB chính là bằng chứng đanh thép chối từ khái niệm bình yên cưỡng bức của trung ương.

## Nguồn

- [[Fixed Income - Alexander During-10.pdf#page=16-17]] — Cú sốc VaR Nhật bản 2003, positive feedback loop.
