---
title: Asset Swap Spread (ASW)
aliases:
- ASW
- Asset Swap
- Par-Par Asset Swap
- Yield-Yield Asset Swap
- Market Value Asset Swap
- Chênh lệch hoán đổi tài sản
type: mechanism
tags:
- fixed-income
- derivatives
- credit-risk
- valuation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb | Tuckman & Serrat | Alexander Düring"
provenance: Multi-source
thesis: The asset swap spread (ASW) is the fixed spread over a floating benchmark
  rate that an investor receives by swapping a fixed-rate bond's coupons into floating
  payments, isolating credit and liquidity risk from interest rate risk.
source_refs:
- file: During_Fixed_Income_Ch23.md
  page: 202
- file: Howard_Corb_Swaps.md
  page: 395
- file: Howard_Corb_Swaps.md
  page: 400
- file: Tuckman_Serrat_2022.md
  page: 377
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4406-4458
  section: "Chapter 5.4.4: Forward asset swap spreads"
created: '2026-04-18'
updated: '2026-05-07'
---

## Thesis

Làm sao để so sánh rủi ro của một trái phiếu Chính phủ Mỹ và một trái phiếu doanh nghiệp Đức một cách công bằng? **Asset Swap Spread (ASW)** là bộ lọc tối thượng, cho phép nhà đầu tư bóc tách ranh giới tín dụng bằng cách chuyển đổi trái phiếu thành một công cụ lãi suất nổi ảo (Synthetic Floater).

---

## 1. Mechanism: The Synthetic Floater

**Asset Swap Spread (ASW)** được định nghĩa là mức lợi nhuận thặng dư trên lãi suất tham chiếu (thường là LIBOR/SOFR) mà nhà đầu tư nhận được khi hoán đổi dòng tiền của một trái phiếu lãi suất cố định [[Schofield_2011.md:L8079]][[Howard_Corb_Swaps.md:L4488]][[Tuckman_Serrat_2022.md:L24704]].

**Transmission Flow (MANDATORY):**
`[Risky Bond] --(Fixed Coupon C)--> [Investor] --(Fixed Coupon C)--> [Swap Desk] --(LIBOR + ASW)--> [Investor]`

[RAW] Các tác giả thống nhất rằng ASW không phải là một con số ngẫu nhiên mà được thiết lập để hợp đồng hoán đổi đạt trạng thái **hiện giá ròng bằng không (NPV=0)** tại thời điểm khởi tạo [[Howard_Corb_Swaps.md:L20877]][[Tuckman_Serrat_2022.md:L24727]]. Howard Corb bóc tách sâu hơn: ASW chính là biến số cân bằng sự chênh lệch giữa **LIBOR Price** (giá trị trái phiếu nếu chiết khấu bằng đường cong hoán đổi) và **Dirty Price** thực tế của nó [[Howard_Corb_Swaps.md:L20956]].

---

## 2. Technical Taxonomy: Par-Par vs. Market Value

### A. Par-Par Asset Swap
Cấu trúc cổ điển nơi nhà đầu tư mua trái phiếu ở mức Par (100). Nếu giá thị trường $P \neq 100$, một khoản phí **Upfront** ($P-100$) sẽ được trao đổi giữa Investor và Dealer [[Howard_Corb_Swaps.md:L20980]][[Tuckman_Serrat_2022.md:L24727]].

### B. Yield-Yield (Market Value) Asset Swap
Phương thức tiêu chuẩn hiện đại, không có phí upfront. Spread được tính nhanh bằng công thức:
$$ASW \text{ Spread} = \text{Bond Yield} - \text{Swap Rate}$$
[[Howard_Corb_Swaps.md:L21139]][[Tuckman_Serrat_2022.md:L24798]]. Schofield chỉ ra rằng có một sự liên hệ toán học chặt chẽ giữa hai loại ASW này dựa trên tỷ lệ giữa Par và Dirty Price [[Schofield_2011.md:L8211]].

---

## 3. Advanced Strategy & Funding (The Repo Link)

[RAW] Để thực hiện giao dịch này mà không tốn vốn (unfunded), nhà đầu tư sử dụng thị trường Repo [[Principles_of_Financial_Engineering_Neftci.md#page=162]]. Tuy nhiên, Schofield cảnh báo rằng việc bỏ qua rủi ro Repo (đặc biệt khi trái phiếu nằm trong trạng thái **Special**) sẽ làm sai lệch lợi nhuận thực tế, do đó cần sử dụng **Forward ASW** [[Schofield_2011.md:L8567]].

**Ứng dụng định giá CDS:** ASW là thành phần cốt lõi để tính toán **CDS Basis**:
$$CDS \text{ Basis} = CDS \text{ Spread} - ASW$$
[[Schofield_2011.md:L10513]][[Tuckman_Serrat_2022.md:L17408]].

---

## 3. Strategic Implications: The Credit Barometer

- **Pure Credit Signal:** Vì rủi ro lãi suất đã được hedge qua chân Swap, biến động của ASW Spread chỉ phản ánh sự thay đổi trong xác suất vỡ nợ (PD) và thanh khoản.
- **Sensitivity:**
  - Khi Credit Spread của tài sản tăng (rẻ đi) $\rightarrow$ ASW Spread tăng.
  - Khi Swap Spread tăng $\rightarrow$ ASW Spread giảm. [[Corb_Swaps#page=398]]

---

## 4. Operational Funding & Risks (The Repo Link)

[RAW] Salih Neftci nhấn mạnh rằng để thực hiện Asset Swap mà không tốn vốn tự có (unfunded), nhà đầu tư sử dụng thị trường Repo:
- **Chuỗi truyền dẫn:** `Mua Trái phiếu -> Repo trái phiếu để lấy tiền mặt trả cho giao dịch mua -> Thực hiện IRS`.
- **The Repo-SIBOR Basis:** Nhà đầu tư nhận SIBOR + ASW Spread (từ IRS) và trả Repo Rate (trên trái phiếu cầm cố). Lợi nhuận thực tế phụ thuộc vào việc spread Repo-SIBOR không thu hẹp bất ngờ.
- **Basis Risk:** Đây là rủi ro ranh giới (boundary risk) nơi tín nhiệm của chính phủ (Repo) và hệ thống ngân hàng (SIBOR/LIBOR) có thể biến động lệch pha.

---

## Evidence / Source Anchors

- Case study on Singapore Bond vs Swap play and Repo funding: [[Principles_of_Financial_Engineering_Neftci.md#page=162]]
- Analysis of Repo-SIBOR spread risks: [[Principles_of_Financial_Engineering_Neftci.md#page=163]]
- Formula for Par-Par ASW upfront and spread: [[Corb_Swaps#page=398]]
- Modern Yield-Yield (Market Value) ASW definition: [[Corb_Swaps#page=400]]
- Asset swap as a tool for relative value trading: [[Tuckman_Serrat#page=377]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — Đường cong chiết khấu.
- [[I_Spread_Vs_ASW]] — So sánh độ chính xác và tính thanh khoản với phương pháp nội suy.
- [[Discount_Margin_Mechanism]] — Metric tương đương cho FRN tự nhiên.
- [[Z_Spread_Vs_I_Spread_Mechanics]] — Các cách đo lường spread thay thế.
