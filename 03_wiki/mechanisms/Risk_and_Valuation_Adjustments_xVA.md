---
title: Risk and Valuation Adjustments (xVA)
aliases:
- xVA
- CVA FVA DVA
- Counterparty Credit Risk
- Valuation Adjustments
- Funding Value Adjustment
- Điều chỉnh giá trị rủi ro
type: mechanism
tags:
- quantitative-finance
- risk-management
- valuation
- central-clearing
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: xVA (Valuation Adjustments) represents the collective set of pricing corrections
  applied to financial contracts to account for counterparty credit risk, funding
  costs, and regulatory capital requirements, transforming theoretical 'risk-free'
  values into market-realistic prices.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 108
- file: During_Fixed_Income_Ch12.md
  page: 110
- file: Perry_Central_Bank_Policy_P6.md
  page: 444
- file: During_Fixed_Income_Ch35.md
  page: 379
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Trong lý thuyết, giá trị của một sản phẩm phái sinh chỉ phụ thuộc vào biến số thị trường. Alexander Düring bóc tách ranh giới của thực tại: giá trị thực tế còn phụ thuộc vào **"Ai"** là người giao dịch và **"Làm sao"** để tài trợ cho nó. Hệ thống **xVA** là bộ lọc chuyển đổi toán học thuần túy thành giá cả thị trường, nơi rủi ro tín dụng và chi phí vốn trở thành các thành phần định giá không thể tách rời. Một sự thay đổi trong xVA của các ngân hàng lớn có thể kích hoạt các đợt co thắt thanh khoản hệ thống theo lý thuyết của Perry Warjiyo. [[During_Fixed_Income_Ch12.md#page=108]] [[Perry_Central_Bank_Policy_P6.md#page=444]]

---

## 1. The Taxonomy of Adjustments (Düring's Lens)

Düring giải mã bộ ba mỏ neo định giá:

### A. CVA (Credit Value Adjustment)
- **Concept:** Chi phí dự phòng cho rủi ro đối tác vỡ nợ.
- **Mechanism:** Nếu bạn đang có lãi trên một hợp đồng, nhưng đối tác phá sản, bạn mất phần lãi đó. CVA là giá trị hiện tại của tổn thất dự kiến này.
- **Hedging:** Các ngân hàng thường hedge CVA bằng cách mua hợp đồng hoán đổi rủi ro tín dụng (CDS) của chính đối tác đó. [[During_Fixed_Income_Ch12.md#page=109]]

### B. FVA (Funding Value Adjustment)
- **Concept:** Chi phí tài trợ cho các khoản ký quỹ (margin).
- **Mechanism:** Khi một giao dịch yêu cầu nộp tiền ký quỹ, ngân hàng phải đi vay tiền mặt với lãi suất cao (unsecured) nhưng chỉ nhận được lãi suất thấp (OIS) cho số tiền ký quỹ đó.
- **The Trap:** FVA có thể biến một giao dịch arbitrage có lãi thành lỗ nếu chi phí vốn của ngân hàng quá cao. [[During_Fixed_Income_Ch12.md#page=109]]

### C. DVA (Debit Value Adjustment)
- **Concept:** Lợi nhuận từ rủi ro của chính mình.
- **Paradox:** Nếu xếp hạng tín nhiệm của ngân hàng *giảm*, giá trị nợ của họ giảm xuống, dẫn đến việc ghi nhận lợi nhuận trên sổ sách kế toán. Düring nhấn mạnh đây là một lợi nhuận "ảo" vì ngân hàng không thể thực sự kiếm tiền từ việc tự vỡ nợ. [[During_Fixed_Income_Ch12.md#page=110]]

---

## 2. Structural Pivot: Central Clearing vs. Bilateral

Ranh giới của xVA thay đổi hoàn toàn dựa trên hạ tầng thanh toán:
- **Bilateral (Song phương):** CVA là rủi ro chính. Giá cả phụ thuộc nặng nề vào uy tín của hai bên.
- **Central Clearing (CCP):** CVA gần như bằng không (do CCP đảm bảo). Tuy nhiên, **FVA và MVA (Margin VA)** tăng vọt do yêu cầu ký quỹ hàng ngày cực kỳ khắt khe. CCP chuyển đổi rủi ro tín dụng thành rủi ro thanh khoản. [[During_Fixed_Income_Ch12.md#page=103]]

---

## 3. Macro-Financial Linkages (Warjiyo's Lens)

Perry Warjiyo bóc tách ranh giới của sự lan tỏa hệ thống:
- **The xVA Feedback Loop:** Khi thị trường biến động, CVA của toàn bộ hệ thống tăng lên. Các ngân hàng đồng loạt tăng giá phí rủi ro, làm thắt chặt điều kiện tài chính toàn cầu.
- **Network Contagion:** Sự sụp đổ của một mắt xích làm tăng vọt chi phí FVA cho các mắt xích còn lại do thanh khoản bị đóng băng, tạo ra vòng xoáy deleveraging cưỡng ép. [[Perry_Central_Bank_Policy_P6.md#page=444]]

---

## 4. Market Risk: Duration and Convexity

Bên cạnh rủi ro đối tác, rủi ro thị trường được quản trị qua các mỏ neo:
- **Modified Duration:** Độ nhạy của giá với 1% thay đổi lãi suất.
- **PVBP (Price Value of a Basis Point):** Giá trị bằng tiền của 1 điểm cơ bản. Düring nhấn mạnh PVBP là công cụ thực thi để thiết kế các bộ hedge PCA-neutral. [[During_Fixed_Income_Ch35.md#page=379]]

---

## Evidence / Source Anchors

- Definition of CVA as the market value of counterparty risk: [[During_Fixed_Income_Ch12.md#page=108]]
- Analysis of the DVA paradox and its accounting implications: [[During_Fixed_Income_Ch12.md#page=110]]
- Identification of FVA as a funding mismatch between unsecured rates and OIS: [[During_Fixed_Income_Ch12.md#page=109]]
- Description of the xVA transmission channel in systemic risk: [[Perry_Central_Bank_Policy_P6.md#page=444]]

## Related

- [[Central_Counterparty_CCP]] — The infrastructure that alters xVA dynamics.
- [[Counterparty_Credit_Risk]] — The underlying driver of CVA.
- [[Principal_Component_Analysis_PCA]] — Used to hedge the market risk components of xVA.
- [[Systemic_Risk_Taxonomy]] — How xVA adjustments propagate through the network.
- [[Lender_Of_Last_Resort_Mechanism]] — The backstop when FVA shocks freeze the market.
