---
title: Standing Repo Facility (SRF) Mechanics
aliases:
- SRF
- Standing Repo Facility
- Fed SRF
- Money Market Backstop
type: mechanism
tags:
- central-banking
- repo
- liquidity
- fed
status: reviewed
confidence: 4
half_life_years: 5
expert_lens: Darrell Duffie | Vítor Constâncio | Spyros Andreopoulos
provenance: "[RAW-BOOK: Duffie BPEA 2026 — Payments, Reserves & Liquidity]; [RAW-CLIP: Constâncio (2025-11-28)]; [RAW-CLIP: Andreopoulos (2026-04-11)]"
thesis: The Standing Repo Facility (SRF) is a permanent liquidity backstop by the Federal Reserve designed to cap overnight repo rates (SOFR) and prevent spikes by allowing primary dealers (and eventually a broader set of banks) to exchange Treasuries for cash at a fixed rate. Hiệu lực trần của nó bị bào mòn bởi stigma và friction vốn (Fed không central-clear repo nên dealer không net được) — bằng chứng 31/10/2025: SOFR vọt 32bp trên IORB nhưng chỉ $50B được rút từ SRF.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
- file: ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- file: Warsh and the Fed's Balance Sheet.md
created: '2026-05-08'
updated: '2026-06-27'
---

## Thesis

The SRF functions as the "ceiling" of the Fed's operational framework for secured markets, similar to how the Discount Window acts for unsecured markets. Its primary goal is to ensure the smooth transmission of monetary policy by keeping the SOFR-FFR spread in check, especially during periods of technical liquidity stress (e.g., month-ends, tax dates).

---

## 1. Operational Mechanism

- **Counterparties:** Initially limited to Primary Dealers; expanded to include eligible depository institutions.
- **Collateral:** Treasury securities, agency debt, and agency mortgage-backed securities (MBS).
- **Rate:** Set as a fixed rate (e.g., 5.00%), typically positioned at the top of the target range for the Fed Funds Rate.
- **The Ceiling Effect:** By offering a standing offer to lend cash against Treasuries, the Fed effectively prevents market repo rates from rising significantly above the SRF rate.

---

## 2. The "Fear of Stigma" Bottleneck

[RAW-CLIP: Constâncio (2025-11-28)] A critical constraint identified in late 2025 was that primary dealers were hesitant to use the SRF due to "stigma"—the fear that using a central bank facility would signal financial weakness.
- **Result:** This hesitation allowed SOFR to spike even when the facility was available.
- **Fed Response:** Meetings with dealers (Nov 2025) were required to encourage usage and clarify that the SRF is an "intended operational tool" rather than a crisis lender.

---

## 3. Interaction with Monetary Policy (The Warsh Bias)

[RAW-CLIP: Andreopoulos (2026-04-11)] The SRF is essential for the Fed's plan to shrink its balance sheet (Quantitative Tightening).
- **The Logic:** As reserves shrink, the risk of "money market dislocations" increases.
- **The Backstop:** The SRF provides a safety valve that allows the Fed to push reserves lower (potentially toward the 9% GDP threshold) without fearing a 2019-style repo crash.

---

## 4. H1 2026 Evidence — Stigma định lượng + SRP rebrand (Duffie BPEA 2026)

[RAW-BOOK: Duffie BPEA 2026]

- **Bằng chứng stigma định lượng:** Ngày **31/10/2025**, repo rate Treasury vượt xa SRF rate (lúc đó = IORB **+10bp**), tạo cơ hội arbitrage rõ ràng cho dealer (vay ở SRF, cho vay lại cao hơn) — nhưng **chỉ $50B** được rút từ SRF. Tại symposium ngân hàng 11/2025 (Chatham House), lãnh đạo GSIB nói thẳng họ ngại chạm SRF "trừ khi sống còn".
- **Friction vốn (mấu chốt):** Vì **Fed không central-clear các nghiệp vụ repo của mình**, dealer bank **không net được** SRF repo với reverse repo của khách → repo SRF nở bảng cân đối, đội eSLR/Tier-1 leverage → chi phí vốn làm nản việc dùng SRF (Logan 2025). Xem [[Treasury_Central_Clearing_Repo_Netting]].
- **Reg YY (2024 clarification):** Fed cho phép GSIB tính *borrowing capacity* tại Discount Window + SRF là nguồn thanh khoản đáp ứng Reg YY — nhưng chỉ tới mức HLA collateral đã ký quỹ. Nelson (2026a): nới rộng việc này sẽ giảm precautionary demand cho reserves, nhưng "cần thiết kế thận trọng".
- **Tiến hóa công cụ:**
  - **25/06/2025:** Fed làm **thường trực** phiên SRF buổi sáng mỗi ngày làm việc (trước đó là tạm thời cuối 2024).
  - **10/12/2025:** Fed **đổi tên SRF → Standing Repo Operations (SRP)** và chuyển sang **full-allotment** (không giới hạn tổng lượng/ngày, chỉ giới hạn theo từng firm). Kỳ hạn overnight, định giá **IORB +10bp**.
- **Đối chiếu quốc tế (BoE STR):** Anh cũng QT mạnh (reserves giảm từ đỉnh ~£1,000B cuối 2021 còn £646B cuối 1/2026); nhưng draw từ Short Term Repo (STR) của BoE **lớn hơn nhiều** (cả tương đối lẫn tuyệt đối) so với SRP của Fed — STR kỳ hạn 1 tuần ở Bank Rate, ít stigma hơn cơ chế overnight IORB+10bp của Fed.

> **So what:** SRF/SRP là van trần *trên lý thuyết*, nhưng dữ liệu 31/10/2025 cho thấy trần **rò rỉ** khi stigma + friction vốn còn đó. Đây là lý do reserves phải giữ đệm dày hơn (ample floor cao hơn) thay vì dựa hoàn toàn vào SRF.

---

## Boundaries / Failure Conditions

- **Collateral Scarcity:** If dealers lack the specific collateral required for the SRF (or if haircuts are too high), the facility cannot provide liquidity.
- **Transmission Lag:** If non-bank entities (who cannot access the SRF) are the ones needing liquidity, the "ceiling" might not hold for the entire market.
- **Stigma + Capital Friction:** Ngay cả khi full-allotment (SRP từ 10/12/2025), nếu stigma và bất lợi netting/leverage còn → take-up thấp, trần không giữ (bằng chứng $50B ngày 31/10/2025).

---

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The market context for the SRF.
- [[Repo_Event_September_2019]] — The crisis that led to the creation of the SRF.
- [[Discount_Window_Mechanism]] — The unsecured counterpart to the SRF.
- [[SOFR_Secured_Overnight_Financing_Rate]] — The rate the SRF is designed to control.
- [[SOFR_IORB_Spread_Stress_Gauge]] — gauge định lượng độ rò rỉ của trần SRF.
- [[Treasury_Central_Clearing_Repo_Netting]] — friction netting làm SRF kém hiệu lực.
- [[Reserve_Management_Purchases_RMP]] — bơm trend bổ trợ; SRF xử lý spike.
- [[Repo_Operations]]
- [[Central_Bank_Liquidity_Support_Programs]]
