---
title: Treasury Central Clearing & Repo Netting Friction
aliases:
- Central Clearing Treasury
- Repo netting friction
- FICC sponsored repo
- Central clearing repo market
type: mechanism
tags:
- repo
- market-structure
- fed
- liquidity
- regulation
status: draft
confidence: 3
half_life_years: 6
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie | Lorie Logan
provenance: "[RAW-BOOK: Duffie BPEA 2026 — Payments, Reserves & Liquidity]; [RAW-OFFICIAL: OFR Blog — Cenicola et al. (2026-01)]"
thesis: "Việc Fed KHÔNG central-clear các nghiệp vụ repo của mình tạo friction netting: dealer bank không thể net repo với Fed (SRF) chống lại reverse repo của khách, nên repo SRF nở bảng cân đối và đội vốn (eSLR/leverage) → làm nản dùng SRF → trần lãi suất rò rỉ. Central clearing rộng hơn cho repo Treasury (OFR 2026) được kỳ vọng tái cấu trúc netting và nhu cầu thanh khoản của thị trường repo ~$8.8T."
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Treasury_Central_Clearing_Repo_Netting]]

## Thesis

Central clearing không chỉ là vấn đề rủi ro đối tác — nó trực tiếp quyết định **dealer net được bao nhiêu** trên bảng cân đối, và do đó quyết định **chi phí vốn** của việc trung gian repo. Đây là một mắt xích ẩn nhưng then chốt giải thích vì sao [[Standing_Repo_Facility_SRF_Mechanics]] kém hiệu lực như một trần lãi suất. [RAW-BOOK: Duffie BPEA 2026]

---

## 1. Friction Netting — Cơ chế lõi (sourced)

[RAW-BOOK: Duffie BPEA 2026, Logan 2025]

- Vì **Fed không central-clear repo operations của chính mình**, dealer bank **không thể net** repo vay từ Fed (SRF/SRP) chống lại reverse repo họ cấp cho khách hàng.
- Hệ quả: mỗi repo SRF **gross-up** bảng cân đối dealer → tăng exposure tính theo **eSLR (Enhanced Supplementary Leverage Ratio)** và Tier-1 leverage (vốn đánh đồng tỷ lệ cho reserves/repo như mọi tài sản).
- → Chi phí vốn biên của việc dùng SRF cao hơn mức cần thiết → cộng hưởng với stigma → take-up thấp (bằng chứng: chỉ $50B rút ngày 31/10/2025 dù SOFR +32bp trên IORB).

> **Logan (2025):** chi phí này "cao hơn mức cần thiết nếu Fed central-clear nghiệp vụ repo của mình" — vì khi đó dealer net được Fed-repo với customer-reverse-repo.

---

## 2. Central Clearing Treasury rộng hơn (market structure)

[RAW-OFFICIAL: OFR Blog, Cenicola/Heilbron/Mann/Paddrik (01/2026)]

- Thị trường repo Treasury ~**$8.8T outstanding** (~$6T overnight) — xương sống truyền dẫn chính sách tiền tệ.
- Chuyển sang **central clearing** (qua FICC/sponsored repo) thay đổi cách netting đa phương hoạt động → tác động tới: nhu cầu HQLA/reserves cấu trúc, haircut, và khả năng dealer hấp thụ cú sốc cung repo.
- OFR (1/2026) phân tích tác động này lên cấu trúc thị trường repo — hướng nghiên cứu mở.

---

## 3. Liên kết tới reserve demand & ample floor

Nếu central clearing (hoặc nới netting) làm **giảm** chi phí vốn trung gian → dealer sẵn sàng hấp thụ swing reserves hơn → có thể **hạ** ample floor cần thiết. Ngược lại, nếu mandate central clearing **tăng** nhu cầu cấu trúc về HQLA/reserves để ký quỹ (margin) tại CCP → **đẩy ample floor lên**, khiến [[Reserve_Management_Purchases_RMP]] có nguy cơ undersized. Chiều tác động ròng phụ thuộc thiết kế cụ thể.

---

## 4. Ranh giới / Khoảng trống dữ liệu (Boundary)

- ⚠️ **Mốc thời gian mandate chưa có raw source:** Một số tổng hợp nội bộ (node [[Reserve_Management_Purchases_RMP]]) nêu "central clearing mandate deadline 30/06/2026" — **con số này KHÔNG xuất hiện trong Duffie BPEA 2026 hay OFR blog đã ingest**. Cần ingest văn bản SEC (Treasury clearing rule) để xác nhận ngày tuân thủ thực tế trước khi khẳng định. [LLM — cần raw source: SEC Treasury central clearing compliance timeline]
- **Chiều tác động lên reserves chưa định lượng:** mới ở mức định tính; thiếu ước lượng quy mô margin/HQLA tăng thêm.

---

## Evidence / Source Anchors

- [RAW-BOOK] Friction netting SRF, eSLR/leverage, Logan 2025: [[Duffie_BPEA_Payments_Liquidity_2026.md]]
- [RAW-OFFICIAL] Central clearing impact on repo: OFR Blog, Cenicola/Heilbron/Mann/Paddrik (2026-01-29), financialresearch.gov

## Related

- [[Standing_Repo_Facility_SRF_Mechanics]] — đối tượng chịu tác động trực tiếp của friction netting.
- [[SOFR_IORB_Spread_Stress_Gauge]] — friction khuếch đại spread khi reserves căng.
- [[Reserve_Management_Purchases_RMP]] — ample floor có thể dịch theo thiết kế clearing.
- [[Repurchase_Agreement_Mechanism]] — thị trường nền.
