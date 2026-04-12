---
type: definition
aliases: [Tài khoản Nostro, Correspondent Banking]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Nostro Account

## Định nghĩa

**Nostro accounts** là các tài khoản vãng lai (current accounts) được sở hữu bởi một ngân hàng và **mở tại một ngân hàng khác**, dùng để thanh toán liên ngân hàng. Từ "Nostro" có nguồn gốc từ tiếng Ý ("của chúng tôi"), ngụ ý rằng ngân hàng xem nó như tài sản *của họ* được gửi ở nơi khác. [extracted] [[Fixed Income - Alexander During-5.pdf#page=4]]

### Cách thức hoạt động

Khi Ngân hàng A cần thanh toán cho Ngân hàng B (hoặc khách hàng của B):
1. A có một tài khoản Nostro tại B.
2. A yêu cầu B chuyển tiền từ tài khoản Nostro (tài sản của A đang nằm tại B) sang tài khoản của khách hàng tại B.
3. Bảng cân đối của A thu hẹp lại (Deposit của khách bị trừ, Nostro account tại B cũng bị trừ). Bảng cân đối của B ghi giảm nghĩa vụ với A (từ Nostro) bù đắp bằng tăng nghĩa vụ với khách (tăng Deposit). [extracted] [[Fixed Income - Alexander During-5.pdf#page=4-5]]

### Nhược điểm

- **Tiêu thụ bảng cân đối kết toán**: Các ngân hàng phải duy trì số dư lớn để xử lý luồng giao dịch, các quỹ này **bị nhàn rỗi (lie idle)** cho đến khi cần thiết. [extracted] [[Fixed Income - Alexander During-5.pdf#page=6]]
- **Correspondent banking risks**: Ngân hàng nhận (B) xử lý thanh toán cho (A) có thể **vô lây dính vào các dòng tiền gian lận** vì họ không biết chi tiết giao dịch gốc. [extracted] [[Fixed Income - Alexander During-5.pdf#page=5]]

## Phân biệt với

- **Central Bank accounts**: Hệ thống RTGS hiện đại thay thế nhiều Nostro accounts song phương bằng một tài khoản duy nhất tại [[Central_Bank]].

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=4]] — Định nghĩa cốt lõi
- [[Fixed Income - Alexander During-5.pdf#page=5]] — Double entry flow với Nostro Account (Figure 4.4)
- [[Fixed Income - Alexander During-5.pdf#page=6]] — Khuyết điểm về balance sheet
