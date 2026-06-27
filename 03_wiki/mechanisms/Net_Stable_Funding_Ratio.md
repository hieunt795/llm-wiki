---
title: Net Stable Funding Ratio
aliases:
- NSFR
- Stable Funding
- Basel III Liquidity
type: mechanism
tags:
- basel-iii
- liquidity-risk
- asset-liability-management
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**NSFR** là một chỉ số thanh khoản dài hạn của Basel III, yêu cầu các ngân
  hàng duy trì một mạng lưới nguồn vốn ổn định (Available Stable Funding - ASF) đủ
  để tài trợ cho các tài sản và hoạt động ngoại bảng trong khoảng thời gian 1 năm
  trong điều kiện căng thẳng kéo dài.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.bis.org/bcbs/publ/d295.pdf
---

# Net Stable Funding Ratio

## Mechanism

**NSFR** là một chỉ số thanh khoản dài hạn của Basel III, yêu cầu các ngân hàng duy trì một mạng lưới nguồn vốn ổn định (Available Stable Funding - ASF) đủ để tài trợ cho các tài sản và hoạt động ngoại bảng trong khoảng thời gian 1 năm trong điều kiện căng thẳng kéo dài.

Mục tiêu là hạn chế việc ngân hàng sử dụng quá nhiều nguồn vốn tài trợ ngắn hạn, không ổn định (như repo ngắn hạn) để nuôi dưỡng các tài sản dài hạn, kém thanh khoản (như nợ tư nhân hoặc nợ doanh nghiệp).

$$NSFR = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \ge 100\%$$ [extracted]

### Điều kiện
- **ASF (Nguồn vốn ổn định sẵn có)**: Được tính bằng cách gán trọng số (ASF factors) cho các loại vốn chủ sở hữu, nợ dài hạn và các loại tiền gửi của khách hàng. [extracted]
- **RSF (Nguồn vốn ổn định cần thiết)**: Được tính dựa trên quy mô và đặc thù thanh khoản của tài sản ngân hàng nắm giữ. Tài sản càng kém thanh khoản (như Loans to Corporates) thì hệ số RSF càng cao (thường là 85-100%). [extracted]

### Ví dụ số
Một khoản vay doanh nghiệp dài hạn có hệ số RSF là 85%. Để tài trợ cho 100 triệu USD khoản vay này, ngân hàng phải có ít nhất 85 triệu USD nguồn vốn ổn định (như kỳ hạn trên 1 năm). 
Nếu ngân hàng chỉ dùng tiền gửi qua đêm để tài trợ, chỉ số NSFR sẽ sụt giảm nghiêm trọng. [inferred]

### Hình ảnh minh họa (Idea)
> **Cân bằng Vững chãi**: Vẽ một cái bập bênh. Bên trái là "Nguồn vốn ổn định" (Equity, Long-term Deposits). Bên phải là "Tài sản dài hạn" (Private Credit, Corporate Loans). Nếu bên trái nhẹ hơn bên phải (tỷ lệ < 100%), cái bập bênh sẽ nghiêng và báo động đỏ "Illiquidity Risk".

## Evidence / Source Anchors
- [extracted] [Basel Committee on Banking Supervision, "Basel III: the net stable funding ratio", 2014](https://www.bis.org/bcbs/publ/d295.htm)
- [researched] [BIS Quarterly Review, March 2025](https://www.bis.org/publ/qtrpdf/r_qt2503b.htm)
