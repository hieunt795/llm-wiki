---
type: mechanism
aliases: [VM, IM, Ký quỹ biến đổi, Ký quỹ ban đầu]
trigger: "Giao dịch được đưa vào bảo kê bởi CCP kéo dài nhiều ngày/năm"
output: "Quy đổi rủi ro tín dụng đối tác thành áp lực thanh khoản tiền mặt hàng ngày"
constraints: ["Không hiệu quả cho các sản phẩm kỳ dị (exotic) vì không có giá chuẩn để Mark-to-market hàng ngày"]
sources: ["Fixed Income - Alexander During-13.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 12
---

# Variation Margin Vs Initial Margin

## Cơ chế biến nợ thành rủi ro thanh khoản

Để bảo vệ bản thân, [[Central_Counterparty]] ép các tay chơi nộp bảo chứng thông qua hai lớp Ký quỹ với triết lý hoàn toàn khác biệt: [extracted] [[Fixed Income - Alexander During-13.pdf#page=2-3]]

### 1. Variation Margin (Ký quỹ biến đổi - VM)
- **Mục đích:** Xóa sạch nợ đọng cũ mỗi ngày. Đưa Exposure của CCP về đúng số 0.
- **Hoạt động:** Hàng ngày (Tối hạch toán), ai lỗ trên giá hạch toán (mark-to-market) phải nộp tiền tươi thóc thật khỏa lấp, ai cược đúng thì được rút mớ tiền tươi đó ra xài.
- **Bản chất:** Bắt buộc **100% bằng Tiền Mặt (Cash)**. VM về mặt bản chất đã chặt đứt Rủi ro đối tác (Counterparty risk) và hoán cải nó xảo quyệt thành Rủi ro thanh khoản (Liquidity risk — *bạn không vỡ nợ, chẳng qua là chiều nay bạn đéo đào đâu ra tiền mặt để nộp mà thôi*). [extracted] [[Fixed Income - Alexander During-13.pdf#page=3]]

### 2. Initial Margin (Ký quỹ ban đầu - IM)
- **Mục đích:** Khi một công ty đột tử, CCP mất và ngày để phong tỏa và bán giải lý nợ của nó. Việc thị trường gãy sụp trong vài ngày chân không đó sẽ không ai nộp VM nhồi thêm. Điểm mù đó do IM đỡ đạn.
- **Hoạt động:** Nộp ngay khi mới mở vị thế. Công thức sơ cấp là tính theo rủi ro sập hầm: $\rho \sqrt{t}$ (trong đó $\rho$ là phương sai daily, và $t$ là số ngày giải lý thanh khoản).
- **Bản chất:** CCP chấp nhận thả lỏng, cho phép dùng Tài sản có giá trị rủi ro thấp (Trái phiếu CP hạn mức cao) để thế chân thay cho tiền mặt, vì cái đống này đóng băng rất lâu, nếu bắt nộp tiền mặt thì thành giam vốn quá ác. [extracted] [[Fixed Income - Alexander During-13.pdf#page=3]]

## Nguồn

- [[Fixed Income - Alexander During-13.pdf#page=2-3]] — Phân tách logic giữa VM (đưa exposure về 0) và IM (chống shock thời gian thủng).
