---
title: Coupon Washing Tax Strategies
aliases:
- Coupon Washing
- Tax Arbitrage via Repo
- Giao dịch rửa coupon
type: convention
tags:
- tax-strategies
- repo-market
- fixed-income
- regulation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Coupon washing is a tax arbitrage technique using repurchase agreements (Repo)
  to transfer bond ownership to a tax-exempt entity just before coupon payment, converting
  a taxable gross coupon into a non-taxable manufactured dividend.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 186
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

[RAW] Coupon washing là một ví dụ điển hình về việc sử dụng các công cụ kỹ thuật tài chính (Repo) để khai thác các lỗ hổng trong hệ thống thuế. Salih Neftci chỉ ra rằng cơ chế này dựa trên sự khác biệt về trạng thái thuế (Tax Status) giữa các đối tác trong thị trường Repo toàn cầu. [[Principles_of_Financial_Engineering_Neftci.md#page=186]]

---

## 1. The Mechanism: Repo-Based Transfer

Cơ chế vận hành của một giao dịch rửa coupon tiêu chuẩn:

1.  **Pre-payment Repo:** Một nhà đầu tư nội địa (đối tượng chịu thuế khấu trừ - Withholding Tax) thực hiện Repo trái phiếu cho một đối tác nước ngoài hoặc thực thể được miễn thuế ngay trước ngày trả coupon.
2.  **Gross Coupon Receipt:** Bên mua (Buyer - thực thể miễn thuế) nhận được 100% giá trị coupon (Gross Coupon) từ tổ chức phát hành.
3.  **Manufactured Dividend:** Bên mua chuyển lại giá trị coupon này cho bên bán (Seller - nhà đầu tư nội địa) dưới dạng một khoản thanh toán thay thế (Manufactured Dividend).
4.  **Tax Conversion:** Khoản thanh toán này thường được hạch toán như một phần của chân giao dịch Repo (giá mua lại) hoặc phí dịch vụ, từ đó tránh được định nghĩa là "thu nhập từ lãi vay" bị đánh thuế khấu trừ.

---

## 2. Regulatory Countermeasures

Các cơ quan quản lý tài chính đã phát triển các cơ chế đối soát để ngăn chặn hành vi này:

### A. Accrued Interest Taxation
Thay vì chỉ đánh thuế vào người nắm giữ trái phiếu tại thời điểm trả coupon, các quy định mới (như tại Indonesia) yêu cầu khấu trừ thuế dựa trên **Lãi cộng dồn (Accrued Interest)**.
- **Impact:** Nhà đầu tư bị đánh thuế trên phần lãi phát sinh trong thời gian nắm giữ thực tế, làm triệt tiêu lợi ích của việc chuyển giao tạm thời qua Repo.

### B. Beneficial Ownership Rules
Yêu cầu xác định "Chủ sở hữu hưởng lợi" (Beneficial Owner) thực sự của dòng tiền coupon. Nếu dòng tiền được chứng minh là quay trở lại thực thể chịu thuế, giao dịch có thể bị truy thu.

---

## 3. CASE STUDIES (Neftci Nuance)

- **Thailand:** Nhu cầu rửa coupon tăng mạnh do sự bùng nổ của các quỹ tương hỗ nội địa, buộc Ngân hàng Trung ương phải thắt chặt quy định về đối tác nước ngoài tham gia Repo.
- **Indonesia:** Ministry of Finance ban hành chỉ thị tạm dừng hoạt động này bằng cách yêu cầu khấu trừ thuế ngay trên phần Accrued Interest khi thực hiện giao dịch mua bán.
- **Australia (Kangaroo Bonds):** [RAW] Trái phiếu phát hành tại thị trường nội địa Úc (Domestic bonds) chịu thuế khấu trừ 10%. Ngược lại, **Kangaroo Bonds** (trái phiếu AUD phát hành bởi tổ chức nước ngoài) được miễn thuế này.
    - **Arbitrage:** Các nhà đầu tư nước ngoài ưu tiên Kangaroo Bonds (như của Fannie Mae), tạo ra sự chênh lệch giá (Exchangeable issues trade through domestic issues), buộc các tổ chức phát hành nội địa phải dùng Swap để lách thuế nhằm duy trì tính cạnh tranh. [[Principles_of_Financial_Engineering_Neftci.md#page=208]]

---

## Evidence / Source Anchors

- Description of coupon washing as a widespread tax avoidance tactic: [[Principles_of_Financial_Engineering_Neftci.md#page=186]]
- Implementation details in Thailand and Indonesia: [[Principles_of_Financial_Engineering_Neftci.md#page=186]]
- The role of manufactured dividends in tax conversion: [[Principles_of_Financial_Engineering_Neftci.md#page=186]]

## Related

- [[Repurchase_Agreement_Mechanism]] — Hạ tầng thực thi giao dịch.
- [[Yield_Curve_Trading_Strategies]] — Các chiến thuật tối ưu hóa dòng tiền.
- [[Bond_Pricing_And_Accrued_Interest_Conventions]] — Cơ chế tính lãi cộng dồn là chìa khóa của quản lý thuế.
