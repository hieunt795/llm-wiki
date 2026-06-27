---
title: Collateral Scarcity and Monetary Policy Transmission
aliases:
- Collateral Gap
- CVPH
- Term Funding Costs
type: mechanism
tags:
- collateral
- transmission
- monetary-policy
- liquidity-crisis
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Bindseil
provenance: bindseil_collateral_full.md
thesis: The probability of hitting collateral constraints (Collateral Gap > 0) increases
  effective term funding costs, distorting the transmission of monetary policy operational
  rates.
source_refs:
- file: bindseil_collateral_full.md
  page: 181
created: '2026-04-26'
updated: '2026-04-26'
---

## Thesis
[LLM] Sự khan hiếm tài sản đảm bảo (Collateral Scarcity) làm biến dạng cơ chế truyền dẫn tiền tệ bằng cách đẩy chi phí huy động vốn thực tế ($i^{\#}$) của ngân hàng lên cao hơn lãi suất chính sách ($i^*$), do rủi ro phải tiếp cận các nguồn vốn khẩn cấp (ELA) hoặc đối mặt với tình trạng mất khả năng thanh toán khi cạn kiệt đệm tài sản đảm bảo.

## 1. Core Logic / Mechanism

### The Collateral Value Post-Haircut (CVPH)
[LLM] Khả năng vay mượn từ NHTW bị giới hạn bởi giá trị tài sản đảm bảo sau khi trừ Haircut (CVPH).
[RAW] For the bank, CVPH is uncertain at that horizon, and in a crisis is likely to decline because: (i) Collateral may lose eligibility; (ii) Collateral may be assigned a lower market value; (iii) Haircuts applied by the central bank could increase.
[LLM] Trong khủng hoảng, CVPH có xu hướng giảm mạnh và trở nên khó dự báo, tạo ra sự thắt chặt điều kiện tài chính tự thân (inherent pro-cyclicality).

### The Collateral Gap (CG)
[LLM] Khoảng cách tài sản đảm bảo ($CG$) được định nghĩa là phần chênh lệch giữa nhu cầu vốn từ NHTW và khả năng vay mượn thực tế:
[RAW] $CG = \max(0, (B/2 + k) - (1 - h)(D/2 + B/2))$
[LLM] Trong đó $k$ là cú sốc rút tiền gửi. Khi $P(CG > 0)$ trở nên đáng kể, ngân hàng đối mặt với rủi ro thanh khoản nghiêm trọng.

### Effective Expected Term Funding Costs ($i^{\#}$)
[LLM] Lãi suất kỳ hạn thực tế của ngân hàng là trung bình trọng số của ba kịch bản:
1. **Lack of Collateral:** Ngân hàng phải dùng ELA với lãi suất phạt $i_{ELA}$.
2. **Normal:** Ngân hàng vay tại lãi suất chính sách $i^*$.
3. **Excess Reserves:** Ngân hàng gửi tiền thừa tại lãi suất tiền gửi $i_D$.
[RAW] $i^{\#} = P(CG>0)i_{ELA} + (P(CG=0) - P(\text{excess reserves}))i^* + P(\text{excess reserves})i_D$
[LLM] Nếu $P(CG>0)$ tăng, $i^{\#} > i^*$, dẫn đến việc thắt chặt điều kiện tín dụng đối với nền kinh tế thực ngay cả khi NHTW giữ nguyên lãi suất điều hành.

## 2. Worked Example
[LLM] Bindseil so sánh các kịch bản (Scenarios I-XI):
- **Scenario II:** Khi độ lệch chuẩn của dòng tiền gửi ($\sigma_k$) tăng từ 1 lên 4 và rủi ro haircut ($\sigma_h$) tăng, $i^{\#}$ tăng từ 4% lên 5.43% dù lãi suất chính sách $i^*$ vẫn ở mức 4%.
- **Scenario IV:** NHTW cố gắng hạ $i^{\#}$ bằng cách giảm Haircut về 0, nhưng đây là sự đánh đổi với mức độ chấp nhận rủi ro (risk tolerance) của NHTW.

## 3. Failure Conditions / Boundaries
[LLM] Cơ chế này thất bại hoặc bị bẻ gãy khi:
1. **Zero Lower Bound (ZLB):** Khi $i^*$ đã ở mức 0, NHTW không thể hạ thêm lãi suất để bù đắp cho sự gia tăng chi phí do thiếu hụt tài sản đảm bảo.
2. **Asset Ineligibility:** Nếu một lượng lớn tài sản bị mất tư cách đảm bảo đồng loạt (downgrade hàng loạt), đệm thanh khoản sẽ sụp đổ nhanh hơn mức NHTW có thể phản ứng bằng các công cụ truyền thống.

## Related
- [[Asset_Encumbrance_And_LGD]]
- [[Symmetric_Interest_Rate_Corridor]]
- [[Haircut_Mechanics_Bindseil]]
- [[Monetary_Policy_Transmission_Mechanism]]
- [[Monetary_Policy_Transmission_Mechanism_MPTM]]
- [[Policy_Mix_Transmission_Dual_Link]]
- [[Monetary_Policy_Implementation_Lags]]
- [[2026-04-26_monetary_policy_synthesis]]
- [[Monetary_Policy_Lags_Profile]]
