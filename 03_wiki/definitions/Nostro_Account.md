---
title: Nostro Account
aliases:
- Vostro Account
- Correspondent Banking
- Nostro
- Tài khoản Nostro
type: definition
tags:
- banking
- accounting
- cross-border-finance
- international-settlement
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring
thesis: A Nostro account ('Ours') is a current account held by one bank at another
  bank, serving as the foundational building block for bilateral interbank settlement
  and cross-border correspondent banking.
source_refs:
- file: During_Fixed_Income_Ch04.md
  page: 4
- file: During_Fixed_Income_Ch04.md
  page: 5
created: '2026-04-18'
updated: '2026-04-26'
---

# [[Nostro_Account]]

## Thesis
[WIKI/LLM] The interbank market relies on a specialized accounting hierarchy to move value between disparate ledgers. The **Nostro account** is the primary mechanism for bilateral transfer, where one bank treats its deposit at another bank as a liquid asset. This system enables global correspondent banking but imposes high balance sheet costs and operational "blind spots." [[During_Fixed_Income_Ch04.md#page=4]]

## Definition
[RAW] **Nostro accounts** là các tài khoản vãng lai (current accounts) được sở hữu bởi một ngân hàng và **mở tại một ngân hàng khác**, dùng để thanh toán liên ngân hàng. Từ "Nostro" (tiếng Ý: "của chúng tôi") ngụ ý ngân hàng xem đó là tài sản của mình gửi tại nơi khác. Ngược lại, ngân hàng nhận tiền gọi đó là **Vostro account** ("của anh").

### 1. Cơ chế chuyển tiền (The Transfer Mechanism)
[RAW] Khi Ngân hàng A (nắm giữ tài khoản Nostro tại B) muốn trả tiền cho khách hàng tại B:
- **Bank A's Action:** Yêu cầu B ghi nợ (debit) tài khoản Nostro của mình. Bảng cân đối của A thu hẹp (giảm tài sản Nostro, giảm nghĩa vụ Deposit với khách).
- **Bank B's Action:** Ghi nợ tài khoản Nostro của A (giảm nghĩa vụ) và ghi có tài khoản khách hàng (tăng nghĩa vụ). Bảng cân đối của B giữ nguyên quy mô nhưng thay đổi chủ nợ. [[During_Fixed_Income_Ch04.md#page=5]]

### 2. Creation and Funding
[RAW] Nostro balances là "Inside Money" được tạo ra bởi ngân hàng nhận. Chúng được tài trợ thông qua:
- **Loans:** Bank A vay từ Bank B (thường qua chiết khấu hối phiếu).
- **Asset Sales:** Bán chứng khoán nợ tại thị trường của Bank B.
- **Reciprocal Flows:** Dòng tiền bù trừ ngược lại từ khách hàng của B sang A.

## Boundaries / Conditions

### 1. Nhược điểm về Bảng cân đối (Inefficiency)
[RAW] Các ngân hàng phải duy trì số dư lớn để xử lý luồng giao dịch dự kiến. Các quỹ này thường **bị nhàn rỗi (lie idle)** và hưởng lãi suất thấp, gây tốn kém chi phí cơ hội và tiêu thụ không gian bảng cân đối kế toán. [[During_Fixed_Income_Ch04.md#page=6]]

### 2. Rủi ro "Blind Spot" (KYC/AML)
[WIKI] Vì ngân hàng trung gian (Bank B) xử lý lệnh thanh toán cho Bank A mà không có thông tin trực tiếp về khách hàng cuối cùng của A, nó tạo ra một rủi ro về rửa tiền. Đây là lý do các ngân hàng lớn hiện nay đang thu hẹp mạng lưới correspondent banking để kiểm soát rủi ro tuân thủ.

## Evidence / Source Anchors
- [[During_Fixed_Income_Ch04.md#page=4]] — Định nghĩa và nguồn gốc thuật ngữ.
- [[During_Fixed_Income_Ch04.md#page=5]] — Double entry accounting flow (Figure 4.4).
- [[During_Fixed_Income_Ch04.md#page=6]] — Nhược điểm về hiệu dụng vốn và rủi ro vận hành.

## Related
- [[Interbank_Netting]]
- [[RTGS_Systems_Global]] — "Centralized Nostro" tại Ngân hàng Trung ương.
- [[Bank_Money_Creation]]
- [[Herstatt_Risk]] — Rủi ro khi chuyển khoản Nostro xuyên múi giờ thất bại.
