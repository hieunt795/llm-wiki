---
title: Bank Money Creation
aliases:
- Inside Money Creation
- Fractional Reserve Process
- Money Ex Nihilo
- Interbank Settlement Logic
- Tạo tiền qua ngân hàng
type: mechanism
tags:
- banking
- macroeconomics
- monetary-policy
- accounting
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: Modern money is primarily created through the extension of private bank credit,
  where the simultaneous recording of a loan (asset) and a deposit (liability) expands
  the money supply 'ex nihilo', constrained only by the bank's ability to settle interbank
  transfers in central bank money.
source_refs:
- file: During_Fixed_Income_Ch04.md
  page: 20
- file: During_Fixed_Income_Ch04.md
  page: 22
- file: During_Fixed_Income_Ch04.md
  page: 25
- file: Perry_Central_Bank_Policy_P3.md
  page: 51
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Hầu hết số tiền trong xã hội hiện đại không do NHTW in ra mà do ngân hàng thương mại tạo ra qua hoạt động cho vay. Alexander Düring bóc tách ranh giới của việc hạch toán (Quy trình nợ đối ứng), trong khi Perry Warjiyo giải mã cơ chế mỏ neo dự trữ. Một ngân hàng có thể tạo tiền "từ hư vô" (ex nihilo), nhưng ranh giới sinh tử của nó nằm ở việc có đủ **Tiền NHTW (Outside Money)** để thanh toán cho các ngân hàng khác khi khách hàng chuyển tiền đi. [[During_Fixed_Income_Ch04.md#page=20]]

---

## 1. The Single-Bank Mechanism: Ex Nihilo Expansion

Khi ngân hàng cho Khách hàng C vay $10,000:
- **Tài sản (Assets):** Xuất hiện một khoản mới "Loan to C". Đây là quyền đòi nợ trong tương lai.
- **Nợ phải trả (Liabilities):** Xuất hiện một khoản ký gửi mới "Deposit by C" trong tài khoản thanh toán.
- **The Accounting Event:** Bảng cân đối kế toán mở rộng đồng thời cả hai bên. Không có tờ tiền mặt nào di chuyển; tiền mới (Inside Money) được tạo ra ngay tại thời điểm bút toán. [[During_Fixed_Income_Ch04.md#page=21]]

---

## 2. The Multi-Bank Friction: The Settlement Constraint

Düring giải mã tại sao việc tạo tiền không phải là vô hạn:
- **Internal Loop:** Nếu C dùng số tiền đó để trả cho B (cùng ngân hàng), quy trình chỉ là thay đổi tên chủ nợ trên sổ sách. Ngân hàng không mất thanh khoản.
- **External Transfer:** Nếu C trả tiền cho một người ở Ngân hàng khác, ngân hàng khởi tạo phải chuyển giao một lượng tương đương **Dự trữ (Reserves)** tại NHTW cho ngân hàng nhận.
- **The Red Line:** Khả năng tạo tiền bị giới hạn bởi lượng Outside Money mà ngân hàng nắm giữ hoặc có thể vay mượn trên thị trường Repo. [[During_Fixed_Income_Ch04.md#page=22]] [[During_Fixed_Income_Ch04.md#page=25]]

---

## 3. The Reserve Anchor (Warjiyo's Lens)

Perry nhấn mạnh vai trò của **Dự trữ bắt buộc (GWM)**:
- Dự trữ đóng vai trò là "van điều tiết" (regulator). Bằng cách thay đổi tỷ lệ dự trữ, NHTW tác động trực tiếp vào khả năng tạo Inside Money của hệ thống ngân hàng.
- **M2 Blurring:** Vì Inside Money (tín dụng) chiếm tới 90-95% tổng lượng tiền, ranh giới kiểm soát của NHTW ngày càng trở nên khó khăn khi các ngân hàng tìm cách tối ưu hóa thanh khoản qua các công cụ thị trường tiền tệ. [[Perry_Central_Bank_Policy_P3.md#page=51]]

---

## Evidence / Source Anchors

- Analysis of money creation via double-entry bookkeeping: [[During_Fixed_Income_Ch04.md#page=20]]
- Identification of interbank settlement in central bank money as the primary constraint: [[During_Fixed_Income_Ch04.md#page=25]]
- Logic of simultaneous expansion of bank assets and liabilities: [[During_Fixed_Income_Ch04.md#page=21]]
- Rationale for reserve requirements as a tool to control credit creation: [[Perry_Central_Bank_Policy_P3.md#page=51]]

## Related

- [[Inside_Vs_Outside_Money]] — The two-tier structure created by this process.
- [[Interbank_Money_Market_Mechanism]] — Where settlement liquidity is traded.
- [[Money_Market_Instruments_Mechanics]] — How banks fund the settlement gaps.
- [[Reserve_Requirement_GWM_Evolution]] — The specific policy tool for this mechanism.
- [[Trade_Credit_And_Non_Bank_Lending]] — Credit creation outside this banking loop.
