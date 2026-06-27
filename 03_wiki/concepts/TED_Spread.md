---
title: TED Spread
aliases:
- Treasury-Eurodollar Spread
type: concept
tags:
- macro
- credit-risk
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: The TED spread measures the difference between 3-month LIBOR (interbank credit
  risk) and 3-month Treasury bill rates (risk-free), serving as a primary indicator
  of perceived credit risk and liquidity stress in the global banking system.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 92
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] TED Spread là "nhiệt kế" đo lường nỗi sợ hãi trên thị trường liên ngân hàng. Nó bóc tách rủi ro tín dụng thuần túy của các ngân hàng thương mại so với chính phủ Mỹ.

## 1. The Calculation
$$\text{TED Spread} = \text{3-month LIBOR} - \text{3-month T-bill Interest Rate}$$
- **Eurodollar Futures Implementation:** Vì giá ED Futures là $100 - \text{Rate}$, trader thực tế mua T-bill Futures và bán ED Futures (hoặc ngược lại) để thực hiện chiến lược spread này.

## 2. Worked Example (Market Stress)
[RAW] Trong điều kiện bình thường, TED Spread dao động khoảng 10-50 bps.
- **Scenario:** Một cuộc khủng hoảng tài chính xảy ra.
- **Mechanism:** Nhà đầu tư tháo chạy khỏi các khoản gửi liên ngân hàng (Eurodollars) để trú ẩn vào trái phiếu chính phủ (Fly to quality).
- **Result:** Lãi suất LIBOR tăng vọt do rủi ro tín dụng, trong khi lãi suất T-bill giảm mạnh do cầu tăng. TED Spread có thể vọt lên >300 bps (như thời điểm 2008).

## 3. Boundary Conditions
- **Liquidity Wedge:** [RAW] Đôi khi TED Spread dãn rộng không chỉ do rủi ro vỡ nợ (default risk) mà còn do sự khan hiếm thanh khoản (liquidity squeeze) tại một trong hai thị trường.
- **Post-LIBOR Era:** Với việc thay thế LIBOR bằng SOFR (lãi suất có đảm bảo), TED Spread truyền thống đang được thay thế bằng các chỉ số spread khác như **SOFR-OIS Spread**.

## Related
- [[Eurodollar_Futures]] — Công cụ để thực thi giao dịch.
- [[Central_Bank_Liquidity_Provision_Mechanics]] — Các can thiệp để thu hẹp TED spread.
- [[Credit_Risk_Taxonomy]] — Lớp rủi ro mà TED spread đo lường.
