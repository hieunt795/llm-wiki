---
title: Structured Notes
aliases:
- SNs
- Bonds with Embedded Derivatives
- Trái phiếu cấu trúc
type: concept
tags:
- bonds
- derivatives
- structured-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Multi-source
thesis: Structured Notes (SNs) represent the marriage of traditional fixed income
  debentures and derivatives, allowing for highly customized coupon types and risk
  profiles embedded within a single funded security.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 316
- file: Howard_Corb_Swaps.md
  page: 318
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Tại sao các nhà đầu tư không tự thực hiện hoán đổi (Swap) trực tiếp mà lại mua **Structured Notes**? Howard Corb giải mã ranh giới của sự tiện lợi và quy định: SN cho phép các thực thể bị hạn chế sử dụng phái sinh (như Money Market Funds) tiếp cận với các cấu trúc rủi ro phức tạp dưới dạng một trái phiếu truyền thống. Đây là sự kết hợp giữa tính thanh khoản của chứng khoán và tính linh hoạt của phái sinh.

---

## 1. Anatomy of a Structured Note

Một SN điển hình bao gồm:
1.  **Host Bond:** Trái phiếu nền tảng (thường do Ngân hàng hoặc định chế tài chính phát hành).
2.  **Embedded Derivative:** Một hoặc nhiều phái sinh (Options, Swaps) được tích hợp vào công thức tính Coupon hoặc hoàn trả gốc.

**Lợi thế cho nhà đầu tư:**
- **Funded Exposure:** SN yêu cầu bỏ vốn toàn bộ (Funded), khác với phái sinh trực tiếp thường là Unfunded.
- **Regulatory Arbitrage:** Vượt qua các rào cản pháp lý cấm đầu tư trực tiếp vào phái sinh nhưng cho phép mua trái phiếu có xếp hạng tín nhiệm. [[Corb_Swaps#page=316]]

---

## 2. Technical Glossary (Interest Rate SNs)

Dựa trên phân loại của Howard Corb:

| Loại Note | Cơ chế Coupon | Mục đích / View |
| :--- | :--- | :--- |
| **[[Inverse_Floater]]** | $max(0, \mu - R)$ | Cược lãi suất giảm. |
| **Deleveraged Floater** | $L \times R + Margin$ ($L < 1$) | Giảm độ nhạy với lãi suất. |
| **Capped Floater** | $R + Margin$, tối đa tại $K$ | Nhà đầu tư bán Cap để lấy thêm spread. |
| **Range Bond** | Coupon cao nếu $R$ nằm trong vùng $[A, B]$, ngược lại 0. | Cược lãi suất đi ngang (Range-bound). |
| **Multi-Step Bond** | Coupon tăng dần theo thời gian (Step-up). | Thường đi kèm quyền mua lại (Callable). |
| **Dual-Index Floater** | Phụ thuộc vào chênh lệch giữa 2 chỉ số (VD: 10y CMS - 3m LIBOR). | Cược vào độ dốc của đường cong (Steepener/Flattener). |

---

## 3. Risk and Evolution

- **The Early 1990s Boom:** Lãi suất ngắn hạn Mỹ giảm mạnh (từ 8% xuống 3%) khiến nhà đầu tư "đói" Yield, thúc đẩy sự ra đời của các cấu trúc đòn bẩy cao như Leveraged Inverse Floaters.
- **The Crash:** Khi Fed tăng lãi suất năm 1994, nhiều SN mất toàn bộ giá trị Coupon, dẫn đến các vụ phá sản chấn động như Orange County.
- **Modern Context:** SN hiện đại đa dạng hóa sang nhiều lớp tài sản khác như Equity-linked, Commodity-linked, và Credit-linked Notes (CLN).

---

## Evidence / Source Anchors

- Definition and rationale for funded form: [[Corb_Swaps#page=316]]
- Glossary of interest rate structured notes: [[Corb_Swaps#page=318]]
- Historical context and market rise: [[Corb_Swaps#page=317]]

## Related

- [[Inverse_Floater]] — Một loại SN điển hình.
- [[Credit_Default_Swaps_CDS]] — Cơ sở cho Credit-linked Notes.
- [[Repurchase_Agreements_Repo]] — Cơ chế đòn bẩy thường dùng kèm SN.
