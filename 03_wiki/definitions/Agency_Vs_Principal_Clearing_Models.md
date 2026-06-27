---
title: Agency vs. Principal Clearing Models
aliases:
- Clearing Models
- Indirect Clearing
- Agency Clearing
- Principal Clearing
- Clearing Agent Risk
- Mô hình bù trừ đại lý và ủy thác
type: definition
tags:
- market-infrastructure
- central-clearing
- risk-management
- banking
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income (2021)
thesis: The distinction between agency and principal clearing models defines the legal
  and risk-sharing relationship between a non-clearing member, their clearing agent,
  and the central counterparty (CCP), dictating how margin obligations and default
  risks are allocated within the financial plumbing.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 106
- file: During_Fixed_Income_Ch12.md
  page: 107
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Không phải mọi giao dịch qua CCP đều giống nhau. Alexander Düring bóc tách ranh giới của việc bù trừ gián tiếp: khi một định chế (như quỹ hưu trí) không đủ điều kiện làm thành viên trực tiếp của CCP, họ phải qua một trung gian (Clearing Agent). Cách thức trung gian này kết nối với CCP—theo mô hình **Agency** (Đại lý) hay **Principal** (Ủy thác)—sẽ quyết định ai là người chịu rủi ro khi thị trường sụp đổ và mức độ minh bạch của hệ thống. [[During_Fixed_Income_Ch12.md#page=106]]

---

## 1. Agency Clearing Model (Standard Mỹ)

Trong mô hình này, CCP có quan hệ hợp đồng trực tiếp với khách hàng cuối, nhưng đại lý bù trừ chịu trách nhiệm thực thi các nghĩa vụ.
- **Transparency:** CCP có toàn quyền quan sát vị thế của từng khách hàng cuối. Điều này giúp CCP thực hiện stress-test chính xác hơn.
- **Risk Allocation:** Khách hàng cuối chịu trách nhiệm nộp ký quỹ (margin). Đại lý chỉ là bên đảm bảo việc thanh toán diễn ra đúng hạn.
- **Benefit:** Nếu đại lý bù trừ phá sản, vị thế của khách hàng có thể được chuyển sang đại lý khác dễ dàng hơn vì CCP đã nắm rõ dữ liệu. [[During_Fixed_Income_Ch12.md#page=106]]

---

## 2. Principal Clearing Model (Standard Châu Âu & Nhật)

Trong mô hình này, đại lý bù trừ đứng hoàn toàn ở giữa. Đối với CCP, khách hàng cuối không tồn tại.
- **Transparency:** CCP chỉ thấy một "khối" vị thế tổng hợp (block) của đại lý. CCP không biết bên trong đó gồm những khách hàng nào.
- **Risk Allocation:** Đại lý bù trừ là bên chịu trách nhiệm duy nhất trước CCP. Khách hàng cuối có quan hệ hợp đồng song phương với đại lý.
- **The Catch:** Nếu khách hàng cuối sử dụng nhiều đại lý khác nhau, CCP không thể tính toán được tổng rủi ro hệ thống của khách hàng đó, dẫn đến khả năng đánh giá thấp rủi ro lây lan (contagion). [[During_Fixed_Income_Ch12.md#page=107]]

---

## 3. The Clearing Bottleneck: Risk Rationing

Düring nhấn mạnh ranh giới thực thi:
- **Capital Requirements:** Việc làm đại lý bù trừ tiêu tốn rất nhiều vốn tự có (capital charges).
- **Rationing:** Do chi phí rủi ro và vốn cao, các ngân hàng lớn đang có xu hướng "định mức" (ration) dịch vụ bù trừ, chỉ phục vụ các khách hàng lớn nhất. Điều này tạo ra rào cản gia nhập thị trường cho các định chế nhỏ và làm giảm tính cạnh tranh của thị trường OTC.
- **Liquidity Transformation:** Đại lý bù trừ thực chất đang thực hiện việc biến đổi tài sản: chấp nhận tài sản phi tiền mặt của khách hàng và nộp tiền mặt (cash margin) cho CCP. [[During_Fixed_Income_Ch12.md#page=107-108]]

---

## Evidence / Source Anchors

- Distinction between US (Agency) and European (Principal) clearing standards: [[During_Fixed_Income_Ch12.md#page=106]]
- Analysis of position visibility and stress-testing in Agency models: [[During_Fixed_Income_Ch12.md#page=106]]
- Description of the clearing agent as a buffer in Principal models: [[During_Fixed_Income_Ch12.md#page=107]]
- Rationale for clearing service rationing due to capital constraints: [[During_Fixed_Income_Ch12.md#page=107]]

## Related

- [[Central_Counterparty_CCP]] — The infrastructure housing these models.
- [[Risk_and_Valuation_Adjustments_xVA]] — How clearing models affect FVA and MVA.
- [[Counterparty_Credit_Risk]] — The risk these models seek to mitigate.
- [[Repurchase_Agreement_Mechanism]] — Used to mobilize cash for margin payments.
