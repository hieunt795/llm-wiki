---
title: Central Counterparty
aliases:
- CCP
- Clearing House
- Đối tác bù trừ tập trung
type: concept
tags: []
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: 'Ch 12: Central Clearing'
thesis: Cơ chế bù trừ tập trung qua CCP giúp giảm thiểu rủi ro đối tác bằng cách thay
  thế các quan hệ song phương phức tạp thành các quan hệ đơn phương với một thực thể
  trung tâm duy nhất.
source_refs:
- Alexander Düring, Ch 12
created: '2026-04-13'
updated: '2026-04-18'
---

# Central Counterparty (CCP)

## Mechanism
Cơ chế bù trừ tập trung (Central Clearing) thay thế mạng lưới song phương gồm $n(n-1)/2$ quan hệ giữa $n$ thành viên thị trường bằng chỉ $n$ quan hệ song phương với CCP.

- **Give-up (Novation)**: Sau khi giao dịch được thỏa thuận song phương, nó được "give up" cho CCP. Hợp đồng gốc được thay thế bằng hai hợp đồng mới: một giữa người mua và CCP, một giữa người bán và CCP.
- **Lợi ích**: Giảm rủi ro tín dụng, tối ưu hóa lưới thanh toán (netting), và đơn giản hóa quản lý tài sản thế chấp.

### 2. Quản trị rủi ro tại CCP
CCP không tự tạo ra rủi ro vị thế nhưng đối mặt với rủi ro thành viên bù trừ (clearing member) vỡ nợ. Để bảo vệ hệ thống, CCP sử dụng cơ chế bảo vệ đa lớp:

- **Margining (Ký quỹ)**: Chuyển đổi rủi ro đối tác thành rủi ro thanh khoản.
    - **Variation Margin (VM)**: Thanh toán lãi/lỗ dựa trên định giá lại hàng ngày (Mark-to-Market). VM được trả bằng tiền mặt để đảm bảo tính thanh khoản tức thì.
    - **Initial Margin (IM)**: Khoản đệm chống lại biến động giá trong thời gian đóng vị thế của thành viên vỡ nợ. Thường được tính theo công thức $\sigma \sqrt{t}$.
- **Default Fund (Quỹ phòng ngừa rủi ro)**: Nguồn lực chung do tất cả thành viên đóng góp, được sử dụng sau khi IM của thành viên vỡ nợ đã cạn kiệt.
- **Bidding Obligation (Nghĩa vụ đấu thầu)**: Các thành viên còn lại có nghĩa vụ tham gia đấu thầu để tiếp nhận các vị thế của thành viên vỡ nợ, đảm bảo tính thanh khoản của thị trường ngay cả trong khủng hoảng.

### 3. Các mô hình bù trừ gián tiếp
Khi một thực thể không thể trở thành thành viên trực tiếp, họ phải thông qua **Clearing Agent**.
- **Agency Clearing (Mỹ)**: CCP có quan hệ hợp đồng với khách hàng cuối, Clearing Agent chỉ đóng vai trò đại lý. CCP có cái nhìn toàn cảnh về vị thế của khách hàng.
- **Principal Clearing (Châu Âu/Nhật)**: CCP chỉ biết đến Clearing Agent. Khách hàng cuối là "vô hình" đối với CCP. Mọi nghĩa vụ đều nằm ở Agent.
- **ISA Direct (Eurex)**: Mô hình lai (hybrid) cho phép khách hàng tự quản lý ký quỹ nhưng chuyển nghĩa vụ quản lý vỡ nợ cho một tổ chức tài chính.

### 4. Valuation Adjustments (xVA)
Giá trị của các giao dịch không được bù trừ tập trung (OTC song phương) cần điều chỉnh dựa trên chi phí vốn và rủi ro:
- **CVA (Credit Value Adjustment)**: Điều chỉnh rủi ro vỡ nợ của đối tác.
- **FVA (Funding Value Adjustment)**: Chi phí vốn để duy trì ký quỹ.
- **DVA (Debit Value Adjustment)**: Phản ánh chi phí kinh tế khi xếp hạng tín dụng của chính tổ chức đó bị giảm.

## Evidence / Source Anchors
- Alexander Düring, *Fixed Income Cash Instruments and Their Derivatives*, Ch 12.
