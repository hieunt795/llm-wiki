---
type: definition
aliases: [act/360, 30/360, act/act, Số ngày tích lũy lãi]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# Daycount Conventions

## Di sản từ kỷ nguyên "Thước Loga"

Dù lãi suất luôn niêm yết theo năm (Annualised), số tiền thực đút túi phải dựa trên một định lý cực kỳ cục mịch: `Ngày thực tính` chia cho `Phân số năm`. Những quy ước (conventions) quái gở nhất của thị trường tài chính hiện đại bắt nguồn từ việc ở những năm 1970, kế toán trưởng không có máy tính bỏ túi mà phải dùng Thước trượt Loga (Slide rules), vì vậy họ nghĩ ra những cách đếm ngày "giả dối" để chia nhẩm cho dễ! [extracted] [[Fixed Income - Alexander During-14.pdf#page=4-5]]

### Các hệ phái chính:
- **Ngành Money Market (Thị trường tiền tệ - Mỹ, Nhật, Âu):** Chuộng **act/360**. Nghĩa là đếm đủ sống ngày thực tế, nhưng mồi tử số giả định 1 năm chỉ có 360 ngày (nhờ đó tiền lãi cuối tháng luôn phình ra to hơn thực tế $\frac{365}{360}$). [extracted] [[Fixed Income - Alexander During-14.pdf#page=4-5]]
- **Khối đồng tiền cũ (Anh, Úc):** Chuộng **act/365**.
- **Ngành Bond & Swap Futures:** Khắt khe hơn, đòi **act/act** (đếm thực/giới hạn thực) có tính tới cú xóc của Năm Nhuận (Leap year) chứa ngày 29/02; hoặc xài **ISDA 30/360** (Ném sạch lịch, giả bộ tháng đéo nào cũng tròn 30 ngày, năm 360 ngày để bóp dẹp công thức). [extracted] [[Fixed Income - Alexander During-14.pdf#page=4-5]]

### Luật Tính Ngược mốc Nhuận
Với những công cụ vắt ngang qua 2 năm mà dính 1 cái Năm nhuận, thị trường không chạy tịnh tiến, mà **tính lùi từ Mốc đáo hạn** (Work backwards from maturity) thay vì tính từ Mốc khởi tạo, ngấm ngầm phục vụ sự "lai tạp" (fungibility) giữa các lô trái phiếu ra mắt khác ngày. [extracted] [[Fixed Income - Alexander During-14.pdf#page=5-6]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=4-6]] — Tổng hợp các loại daycount đâm xoắn não mượn từ kỉ nguyên pre-computer. Daycount act/360 đặc hữu của Money market.
