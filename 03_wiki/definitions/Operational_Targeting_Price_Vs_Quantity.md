---
title: 'Operational Targeting: Price vs. Quantity'
aliases:
- Interest Rate vs Money Supply Targeting
- Poole Model
- Price vs Quantity Instruments
- Mỏ neo hoạt động: Giá hay Lượng
type: definition
tags:
- monetary-policy
- central-banking
- economics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The choice of operational target—interest rates (price) or money supply (quantity)—depends
  on the relative stability of the goods market versus the money market, as formally
  modeled by William Poole (1970).
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 197
- file: Perry_Central_Bank_Policy_P4.md
  page: 198
- file: Perry_Central_Bank_Policy_P4.md
  page: 199
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

NHTW không thể đồng thời kiểm soát cả lãi suất và cung tiền. Perry Warjiyo giải mã bài toán tối ưu: việc chọn mỏ neo nào làm mục tiêu hoạt động hàng ngày phụ thuộc vào việc "cú shock" nào đang đe dọa nền kinh tế mạnh hơn. Đây không chỉ là vấn đề kỹ thuật, mà là quyết định về việc NHTW muốn gánh chịu rủi ro ở khu vực nào: khu vực thực (sản lượng) hay khu vực tài chính (lãi suất). [[Perry_Central_Bank_Policy_P4.md#page=197]]

---

## 1. The Poole Model (1970)

Poole sử dụng hệ phương trình IS-LM để xác định mỏ neo tối ưu:
- **IS Curve (Khu vực thực):** $y = \alpha_0 + \alpha_1 r + u$ (u là cú shock cầu).
- **LM Curve (Khu vực tiền tệ):** $m = \beta_0 + \beta_1 y + \beta_2 r + v$ (v là cú shock cầu tiền).

### Scenario A: Shock khu vực Tiền tệ thống trị ($\sigma^2_v > \sigma^2_u$)
- **The Problem:** Người dân thay đổi ý định nắm giữ tiền mặt đột ngột (do đổi mới tài chính, thẻ tín dụng).
- **Optimal Target:** **Interest Rate ($r$)**.
- **Logic:** Bằng cách ghim lãi suất, NHTW triệt tiêu hoàn toàn tác động của cú shock cầu tiền lên sản lượng ($y$). Đường LM trở nên nằm ngang tại mức lãi suất mục tiêu. [[Perry_Central_Bank_Policy_P4.md#page=198]]

### Scenario B: Shock khu vực Thực thống trị ($\sigma^2_u > \sigma^2_v$)
- **The Problem:** Đầu tư hoặc tiêu dùng biến động mạnh.
- **Optimal Target:** **Money Supply ($m$)**.
- **Logic:** Khi cầu thực tăng mạnh, lãi suất sẽ tự động tăng (do cung tiền cố định), tạo ra một cơ chế "phanh tự động" giúp ổn định sản lượng. Ghim lãi suất trong trường hợp này sẽ làm sản lượng biến động mạnh hơn. [[Perry_Central_Bank_Policy_P4.md#page=198]]

---

## 2. The Global Shift to Price-based Targeting

Kể từ những năm 1990, hầu hết các NHTW (bao gồm BI từ năm 2005) đã chuyển sang **Interest Rate Targeting**.

### Why Quantity Targeting Failed?
1.  **Velocity Instability:** Đổi mới tài chính (FinTech, thanh toán điện tử) làm tốc độ lưu thông tiền tệ trở nên không thể dự báo.
2.  **Weak Link:** Quan hệ giữa Base Money ($M0$) và lạm phát trở nên mờ nhạt.
3.  **Communication:** Lãi suất (ví dụ: 5.25%) dễ hiểu và tạo tín hiệu rõ ràng cho công chúng hơn là các con số cung tiền tỷ Rupiah. [[Perry_Central_Bank_Policy_P4.md#page=202]]

---

## Strategic Implications: EME Context

Perry Warjiyo highlights that for EMEs like Indonesia:
- **Pre-2005:** BI used **Base Money** targeting because of high inflation and the need for a rigid quantity brake.
- **Post-2005 (ITF):** Chuyển sang **BI Rate**. Điều này yêu cầu NHTW phải có khả năng dự báo thanh khoản cực tốt để đảm bảo lãi suất thị trường liên ngân hàng (PUAB) bám sát BI Rate. [[Perry_Central_Bank_Policy_P4.md#page=203]]

## Evidence / Source Anchors

- Mathematical derivation of the Poole IS-LM framework: [[Perry_Central_Bank_Policy_P4.md#page=197]]
- Analysis of shock variance ($\sigma^2_u, \sigma^2_v$) on target optimality: [[Perry_Central_Bank_Policy_P4.md#page=198]]
- Identification of financial innovation as the driver of velocity instability: [[Perry_Central_Bank_Policy_P4.md#page=202]]
- Description of the BI transition from quantity to price targeting in 2005: [[Perry_Central_Bank_Policy_P4.md#page=203]]

## Related

- [[Central_Bank_Operational_Frameworks]] — The implementation map.
- [[Interest_Rate_Corridor_Mechanism]] — How the price target is defended.
- [[Reserve_Requirement_GWM_Evolution]] — The tool used to manage the quantity of reserves.
- [[Inflation_Targeting_Framework_ITF]] — The strategic regime that mandates price-based targeting.
