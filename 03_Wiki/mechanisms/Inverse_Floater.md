---
type: mechanism
aliases: [Trái phiếu FRN nghịch đảo, Nghịch đảo thả nổi, max(0, mu - R)]
trigger: "Tôi tin rằng Lãi suất liên ngân hàng sắp cắm đầu xuốg đáy (Dovish), làm sao dùng FRN để phóng đại lợi nhuận cược điều này nhưng không xài phái sinh?"
output: "Mua Inverse Floater. Thị trường càng hạ lãi, hệ số bị trừ càng nhỏ, Coupon bỏ túi càng to"
constraints: ["Rủi ro đu đỉnh Yield: Nếu ngân hàng trung ương bất thình lình thắt chặt, Coupon Inverse Floater lập tức đập về 0"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# Inverse Floater

## Cửa Đặt Cược Trắng Trợn Đảo Chiều Lãi Suất

Đồ thị phái sinh của FRN thông thường là đồng thuận (Lãi TT tăng, Tỷ suất Coupon tăng). Nhưng để chọc khe những nhà đầu cơ (Speculator) cuồng phong Lãi Suất Giảm, nhóm Ngân hàng Cấu Trúc phất ra thứ vũ khí có tên **Inverse Floater** (Trái phiếu nghịch đảo thả nổi).

Công thức vắt ruột của nó:
$$C_i = max(0, \mu - R(t_i - 2))$$

- Hệ số Chỉ số Tham chiếu $R$ (Benchmark) đã bị đặt vào Cực âm. 
- Mức $\mu$ lúc này không còn là một Quoted Margin xuyênh xoàng vài spread lẻ tẻ, nó sẽ được set là một Rào cản tuyệt đối khổng lồ (VD: 8%).

*Cơ chế kiếm tiền:* Lãi suất thị trường càng sụp đổ, phần bị trừ hao $-R$ càng teo tóp, Nhà đầu tư ôm quả Coupon cồng kềnh no nê. Còn lỡ bói sai thời cuộc, $R$ vọt lố qua Vạch trần $\mu$, Trái phếu nín họng tịt nòi rớt về Lãi 0đ. [extracted] [[Fixed Income - Alexander During-18.pdf#page=3]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=3]] — Giới thiệu ngắn gọn cấu trúc toán học của Inverse Floater max(0, mu - R(ti-2)).
