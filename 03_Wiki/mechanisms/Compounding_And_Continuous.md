---
type: mechanism
aliases: [Lãi gộp, Lãi kép, Continuous compounding, Simple interest]
trigger: "Hai trader cãi nhau vì tính lãi ra 2 con số khác nhau trên cùng 1 mức coupon"
output: "Toàn bộ thế giới Fixed Income phải đồng thuận một quy ước tính lãi ghép trước khi so sánh tỷ suất"
constraints: ["Số lần ghép n → ∞ thì hội tụ về e^(rt), nhưng thị trường thực tế không bao giờ ghép liên tục"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# Compounding And Continuous

## Bản Chất Toán Học của Lãi Suất

Mọi thứ trong Fixed Income đều bắt đầu từ một câu hỏi ngu ngơ: *"Tao cho mày mượn 100 đồng, lãi suất 5% một năm, nhưng mày trả lãi hàng quý — vậy cuối năm mày nợ tao bao nhiêu?"* [extracted] [[Fixed Income - Alexander During-14.pdf#page=2-3]]

### 1. Simple Interest (Lãi đơn)
Chỉ tính lãi trên gốc ban đầu, bỏ qua `lãi trên lãi`:

$$I = P \cdot r \cdot t$$

Đơn giản nhưng chết người: Nó **đánh giá thấp** giá trị thật sự của khoản tiền nếu kỳ hạn dài.

### 2. Discrete Compounding (Lãi kép rời rạc)
Tính lãi trên (Gốc + Lãi tích lũy từ kỳ trước). Nếu ghép $n$ lần mỗi năm:

$$FV = P \cdot \left(1 + \frac{r}{n}\right)^{n \cdot t}$$

- $n = 1$: Annual (phổ biến ở thị trường Trái phiếu châu Âu)
- $n = 2$: Semi-annual (chuẩn của US Treasuries — **tất cả yield Mỹ đều quote ở tần suất này**)
- $n = 4$: Quarterly (phổ biến ở thị trường OIS/Swap)
- $n = 12$: Monthly (mortgages)

### 3. Continuous Compounding (Lãi kép liên tục)
Khi $n \to \infty$, phép ghép rời rạc hội tụ về giới hạn Euler:

$$FV = P \cdot e^{r \cdot t}$$

Đây là **quy ước chuẩn của giới Quant và Academia** (Black-Scholes, Hull-White...) vì tính chất toán học cực kỳ gọn gàng: Lãi suất liên tục có thể cộng trừ trực tiếp, trong khi lãi suất rời rạc phải nhân chia. [extracted] [[Fixed Income - Alexander During-14.pdf#page=3]]

### Hiểm họa so sánh Chéo
Düring nhấn mạnh: Khi một trader nói "5%", bạn PHẢI hỏi ngay: **"5% compounded thế nào?"** — Vì 5% semi-annual ≠ 5% continuous ≠ 5% annual. Sự chênh lệch tuy nhỏ (vài basis points) nhưng trên notional hàng tỷ đô la thì đó là cả triệu tiền lời/lỗ. Đây là lý do tại sao [[Daycount_Conventions]] phải luôn đi kèm với quy ước compounding.

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=2-4]] — Phân loại Simple / Discrete / Continuous compounding. Quy ước semi-annual của US Treasury vs annual của Eurozone.
