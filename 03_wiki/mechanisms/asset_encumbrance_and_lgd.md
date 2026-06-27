---
title: Asset Encumbrance and Effective LGD Dynamics
aliases:
- Asset Encumbrance
- LGD#
- Effective Loss Given Default
type: mechanism
tags:
- collateral
- banking
- risk-management
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Bindseil
provenance: bindseil_collateral_constraints.md
thesis: Asset encumbrance due to central bank funding significantly increases the
  effective Loss Given Default (LGD#) for unsecured creditors, potentially cutting
  off banks from market funding.
source_refs:
- file: bindseil_collateral_constraints.md
  page: 211
created: '2026-04-26'
updated: '2026-04-26'
---

## Thesis
[LLM] Sự phụ thuộc quá mức vào thanh khoản NHTW dẫn đến hiện tượng "thế chấp hóa tài sản" (Asset Encumbrance), làm gia tăng tỷ lệ tổn thất thực tế (LGD#) đối với các chủ nợ không có tài sản đảm bảo, từ đó đẩy chi phí huy động vốn thị trường lên cao và tạo ra rủi ro loại trừ tài chính.

## 1. Core Logic / Mechanism

### The Asset Encumbrance Problem
[RAW] The asset encumbrance problem is not only linked to the recourse of banks to collateralized central bank credit, but always arises when banks pledge a relevant part of their assets for collateralized credit or debt issuance (e.g. covered bonds).
[LLM] Trong bối cảnh khủng hoảng, khi thị trường tín dụng không đảm bảo (unsecured) bị đóng băng, các ngân hàng buộc phải dựa vào nguồn vốn có bảo đảm từ NHTW. Việc thế chấp các tài sản tốt nhất (hoặc một lượng lớn tài sản với mức Haircut cao) khiến phần tài sản còn lại cho các chủ nợ khác bị thu hẹp đáng kể.

### Mathematical Derivation of LGD#
[LLM] Bindseil thiết lập mô hình tính toán tỷ lệ tổn thất thực tế (LGD#) dựa trên mức độ Haircut và tỷ lệ tài sản bị phong tỏa (C):
[RAW] The value of C can then be derived from the haircut-setting formula. We also know that $C(1 - \text{effective average haircut}) = (1 - D - E)$.
[LLM] Công thức tính tỷ lệ hồi phục thực tế ($rr^{\#}$) và tỷ lệ tổn thất thực tế ($LGD^{\#}$) cho người gửi tiền không bảo đảm:
$$rr^{\#} = \frac{rr(1-E) - C}{D}$$
$$LGD^{\#} = 1 - \frac{(1-LGD)(1-E) - C}{D}$$
[LLM] Trong đó:
*   $rr$: Tỷ lệ hồi phục tài sản gốc.
*   $E$: Vốn chủ sở hữu.
*   $C$: Giá trị tài sản bị thế chấp tại NHTW.
*   $D$: Tổng tiền gửi/nợ không bảo đảm.

## 2. Worked Example
[RAW] D = 0.7; E = 0.1; LGD = 50%. With a very conservative collateral haircut, e.g. $\delta = 0.1$, the bank needs to pledge collateral with a value of 0.36 to collateralize its central bank credit of 0.1.
[LLM] Nếu ngân hàng phụ thuộc nhiều hơn vào NHTW (ví dụ: 20% tổng tài sản), với tham số haircut $\delta = 0.1$, người gửi tiền sẽ mất gần như toàn bộ (LGD# = 99%) trong trường hợp vỡ nợ. 
[RAW] Interest rate add-on displayed is the interest rate surcharge resulting from asset encumbrance due to positive haircuts. For $\delta = 0.1$ and 20% CB funding, the interest rate add-on reaches 98 bp.

## 3. Failure Conditions / Boundaries
[LLM] Cơ chế này trở nên cực đoan khi:
1. **Haircut Pro-cyclicality:** NHTW tăng haircut trong khủng hoảng, buộc ngân hàng phải thế chấp nhiều tài sản hơn cho cùng một lượng vốn.
2. **Low Asset Valuation:** Tài sản (như trái phiếu chính phủ Bồ Đào Nha/Hy Lạp năm 2011) bị định giá thấp dưới giá trị danh nghĩa, làm trầm trọng hóa tình trạng thiếu hụt tài sản đảm bảo (Collateral Scarcity).
3. **Stigma:** Sự gia tăng LGD# khiến ngân hàng không thể thu hút tiền gửi không bảo đảm, dẫn đến vòng xoáy thanh khoản - khả năng thanh toán.

## Related
- [[Collateral_Scarcity_Transmission]]
- [[Haircut_Mechanics_Bindseil]]
- [[Emergency_Liquidity_Assistance]]
- [[Cover_Pool_And_Overcollateralisation]]
- [[Bank_Deposit_Types]]
