---
title: CLO Tranche Structure and Loss Allocation
aliases:
- CLO Waterfall
- Top-down Payment
- Bottom-up Losses
- CLO Capital Stack
type: mechanism
tags:
- credit
- securitization
- structured-finance
status: reviewed
confidence: 5
half_life_years: 10
expert_lens: Bruce Tuckman | Angel Serrat
provenance: '[RAW-BOOK: Tuckman & Serrat (2022) Ch 14]'
thesis: A Collateralized Loan Obligation (CLO) utilizes a tiered capital structure where cash flows are distributed top-down (Senior to Junior) and credit losses are absorbed bottom-up (Junior to Senior), creating distinct risk-return profiles tailored to different investor sectors.
---

## Thesis

CLO là trung tâm của thị trường vốn vay đòn bẩy (leveraged loans). Tuckman & Serrat giải mã logic của việc "phân tầng rủi ro" (tranching): Biến một rổ các khoản vay rủi ro cao thành các chứng khoán có xếp hạng từ AAA đến Equity. Cơ chế then chốt là sự bất đối xứng giữa luồng tiền (Payment Waterfall) và luồng lỗ (Loss Allocation). [[Tuckman_Serrat_2022#page=375]]

---

## 1. The Dual-Flow Mechanism: Waterfall vs. Absorption

DENSE UNPACK:
- **INTENT:** Tách biệt rủi ro vỡ nợ của tài sản cơ sở thành các mức chịu đựng khác nhau để tối ưu hóa chi phí vốn (WACC) cho cấu trúc.
- **MECHANISM:**
  1. **Top-Down Payment (Waterfall):** Tiền lãi và gốc từ rổ tài sản được trả cho Tranche X và A đầu tiên, sau đó đến B, C, D, E và cuối cùng là Equity.
  2. **Bottom-Up Losses:** Khi có nợ xấu, Tranche Equity bị xóa sổ đầu tiên. Chỉ khi Equity mất trắng, Tranche Junior mới bắt đầu chịu lỗ, và cứ thế tiến lên phía Senior.
- **INTERACTIONS:** Kết nối với [[Credit_Loss_Identity]]. Tỷ lệ thu hồi (Recovery Rate) của tài sản cơ sở trực tiếp quyết định tốc độ lan tỏa lỗ lên các tầng phía trên.
- **BOUNDARY:** Khi tỷ lệ vỡ nợ (Default Rate) vượt quá một ngưỡng nhất định (Overcollateralization Test), tiền mặt sẽ được chuyển hướng từ Equity để trả nợ cho Senior tranches, gây ra hiện tượng dừng trả lãi cho Equity.

---

## 2. Tranche Taxonomy and Investor Sectors

Tuckman & Serrat phân loại cấu trúc điển hình của một CLO:

| Tranche | Rating | Target Investors | Role in Structure |
| :--- | :--- | :--- | :--- |
| **A / X** | AAA/AA | Banks, Insurance | Senior-most safety, low yield. |
| **Mezzanine (B, C, D)** | A to BB | Asset Managers | Balanced risk/return, yield enhancement. |
| **Subordinated / Equity** | Unrated | Hedge Funds, CLO Managers | High yield, first-loss piece, captures "excess spread". |

[[Tuckman_Serrat_2022#page=376]]

---

## 3. Risk Transmission: The Thickening of Junior Tranches

- **Credit Enhancement:** Các tầng phía dưới (Equity, Mezzanine) đóng vai trò là "đệm bảo vệ" cho các tầng phía trên.
- **Diversification Benefit:** Tuckman nhấn mạnh rằng rủi ro lớn nhất của CLO không phải là các vỡ nợ riêng lẻ mà là **tương quan vỡ nợ (default correlation)**. Nếu toàn bộ nền kinh tế suy thoái, rổ tài sản sẽ vỡ nợ đồng loạt, phá vỡ các đệm bảo vệ Mezzanine nhanh chóng. [[Tuckman_Serrat_2022#page=377]]

---

## Evidence / Source Anchors

- Top-down payment and bottom-up loss principle: [[Tuckman_Serrat_2022#page=375]]
- CLO Tranche classification (Table 14.1): [[Tuckman_Serrat_2022#page=376]]
- Securitization of leveraged loans rationale: [[Tuckman_Serrat_2022#page=374]]

## Related

- [[ABS_Tranching]] — The broader concept of credit tranching.
- [[Credit_Loss_Identity]] — The fundamental calculation for underlying losses.
- [[Leverage_Ratio]] — Constraints on banks investing in senior tranches.
- [[Structured_Notes]]
- [[PAC_Vs_Sequential_Tranches]]
