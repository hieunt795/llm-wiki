---
title: Discount Margin Mechanism
aliases:
- Discount Margin
- DM
- FRN Valuation
- Par Value Mechanism
- Spread over Benchmark
type: mechanism
tags:
- fixed-income
- valuation
- credit-risk
- frn
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income (2021)
thesis: The discount margin (DM) is the effective spread over the benchmark rate that
  an investor earns on a Floating Rate Note (FRN), functioning as the primary metric
  for credit risk valuation in variable-coupon instruments.
source_refs:
- file: During_Fixed_Income_Ch18.md
  page: 172
- file: During_Fixed_Income_Ch18.md
  page: 175
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Tại sao giá của FRN thường ổn định hơn trái phiếu cố định? Alexander Düring bóc tách ranh giới của cơ chế tái định giá (Reset): vì coupon của FRN tự động điều chỉnh theo lãi suất thị trường, nó triệt tiêu hầu hết rủi ro lãi suất. Sự biến động giá của FRN do đó trở thành mỏ neo thuần túy cho **Rủi ro tín dụng** (Credit Risk), và **Discount Margin (DM)** chính là thước đo chính xác nhất cho rủi ro này. [[During_Fixed_Income_Ch18.md#page=172]]

---

## 1. The Anchor: Par Value Mechanism

Düring giải mã tại sao FRN lại là công cụ bảo vệ vốn tuyệt vời:
- **The Logic:** Vào ngày reset coupon (thường là 3 tháng một lần), lãi suất coupon mới được thiết lập bằng đúng lãi suất thị trường hiện tại cộng với một biên độ cố định (Quoted Margin).
- **The Equilibrium:** Nếu rủi ro tín dụng của người phát hành không thay đổi, giá của FRN **bắt buộc** phải quay về mức 100% (Par) vào ngày reset.
- **The Pull-to-Par:** Bất kỳ sự lệch giá nào giữa hai kỳ reset đều chỉ là tạm thời, phản ánh rủi ro lãi suất tích lũy trong vài ngày còn lại của kỳ coupon đó. [[During_Fixed_Income_Ch18.md#page=175]]

---

## 2. Mechanism: Discount Margin (DM) Calculation

Khi rủi ro tín dụng của doanh nghiệp tăng lên, nhà đầu tư yêu cầu một mức lợi nhuận cao hơn Quoted Margin (QM) ban đầu. Điều này khiến giá trái phiếu ($P$) giảm xuống dưới 100.
- **DM Definition:** Là mức chênh lệch (spread) duy nhất khi cộng vào lãi suất benchmark sẽ làm cho giá trị hiện tại của toàn bộ dòng tiền dự kiến của FRN bằng đúng giá thị trường hiện tại.
- **Toán học:**
$$P = \sum \frac{\text{Coupon}_i}{(1 + (R_i + DM) \times DCF_i)} + \frac{100}{(1 + (R_n + DM) \times DCF_n)}$$
- **Interpretation:** Nếu $DM > QM$, trái phiếu đang giao dịch dưới mệnh giá (discount). Nếu $DM < QM$, trái phiếu đang giao dịch trên mệnh giá (premium). [[During_Fixed_Income_Ch18.md#page=172]]

---

## 3. Strategic Implications: Credit Discovery

- **Isolating Credit:** Vì FRN loại bỏ nhiễu từ biến động đường cong lợi suất, biến động của DM là tín hiệu "sạch" nhất về sức khỏe tài chính của người phát hành.
- **The Floor Trap:** Düring cảnh báo ranh giới kỹ thuật — trong môi trường lãi suất âm, nhiều FRN có cơ chế **Implicit Floor** (sàn 0%). Nếu benchmark xuống âm, coupon không đổi, dẫn đến việc giá FRN tăng vọt cơ học, làm méo mó việc tính toán DM thực tế. [[During_Fixed_Income_Ch18.md#page=176]]

---

## Evidence / Source Anchors

- Analysis of the pull-to-par effect on coupon reset dates: [[During_Fixed_Income_Ch18.md#page=175]]
- Mathematical definition of Discount Margin relative to Quoted Margin: [[During_Fixed_Income_Ch18.md#page=172]]
- Identification of DM as the primary credit risk indicator for floaters: [[During_Fixed_Income_Ch18.md#page=172]]
- Description of the 0% coupon floor impact on FRN valuation: [[During_Fixed_Income_Ch18.md#page=176]]

## Related

- [[Bond_Valuation_Principles]] — The general framework for PV calculations.
- [[Yield_Calculations_Variants]] — DM vs. Yield-to-maturity.
- [[Counterparty_Credit_Risk]] — The driver behind DM fluctuations.
- [[Inverse_Floater_Structure]] — The complex variant where duration is amplified.
