---
title: New Keynesian Phillips Curve (NKPC)
aliases:
- NKPC
- Baseline ITF Model
- Modern Macro Supply Equation
- Kỳ vọng lạm phát New Keynesian
type: mechanism
tags:
- macroeconomics
- monetary-policy
- expectations
- inflation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The New Keynesian Phillips Curve (NKPC) posits that current inflation is determined
  by the expectations of future inflation and the current output gap, serving as the
  foundational supply-side equation for the Inflation Targeting Framework (ITF).
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 230
- file: Perry_Central_Bank_Policy_P4.md
  page: 231
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

NKPC là "trái tim" của kinh tế học vĩ mô hiện đại. Perry Warjiyo giải mã cơ chế tại sao **Kỳ vọng tương lai** lại quan trọng hơn dữ liệu quá khứ: trong một thế giới nơi các doanh nghiệp đặt giá gối đầu (staggered pricing), họ không chỉ nhìn vào chi phí hôm nay mà còn dự tính lạm phát ngày mai để điều chỉnh giá ngay lập tức. Đây là lý do tại sao ITF tập trung vào việc quản trị kỳ vọng. [[Perry_Central_Bank_Policy_P4.md#page=230]]

---

## 1. The Mathematical Foundation

Hệ thống Baseline ITF bao gồm 3 phương trình, trong đó NKPC đóng vai trò là phương trình Cung (Supply side):

### A. The Supply Equation (NKPC)
$$\pi_t = E[\pi_{t+1}] + \alpha x_t + \epsilon_t$$
- **$\pi_t$:** Lạm phát hiện tại.
- **$E[\pi_{t+1}]$:** Kỳ vọng lạm phát giai đoạn tới (mỏ neo của ITF).
- **$x_t$:** Khoảng cách sản lượng (Output Gap).
- **$\alpha$:** Độ nhạy của lạm phát với sản lượng. [[Perry_Central_Bank_Policy_P4.md#page=230]]

### B. The Demand Curve (Dynamic IS)
$$x_t = E[x_{t+1}] - \delta(i_t - E[\pi_{t+1}]) + u_t$$
- Phương trình này kết nối lãi suất danh nghĩa ($i_t$) của NHTW với cầu thực tế thông qua lãi suất thực dự tính. [[Perry_Central_Bank_Policy_P4.md#page=231]]

### C. The Policy Rule
$$i_t = \phi_\pi \pi_t + \phi_x x_t + \phi_i i_{t-1} + \upsilon_t$$
- Phản ứng của NHTW đối với các biến số kinh tế (thường là một biến thể của Taylor Rule). [[Perry_Central_Bank_Policy_P4.md#page=231]]

---

## 2. Strategic Implications: Anchoring

Perry Warjiyo nhấn mạnh rằng NKPC thay đổi hoàn toàn cách NHTW vận hành:
- **Forward-looking:** Vì $\pi_t$ bị dẫn dắt bởi $E[\pi_{t+1}]$, NHTW không cần phải chờ lạm phát tăng mới hành động. Chỉ cần kỳ vọng tăng, lạm phát thực sẽ tăng ngay lập tức.
- **Credibility Trap:** Nếu NHTW mất uy tín, kỳ vọng sẽ rời xa mục tiêu, làm cho tham số $\alpha$ trở nên bất ổn và chính sách tiền tệ mất hiệu lực.
- **The Output-Inflation Trade-off:** Tham số $\alpha$ phản ánh độ dốc của đường Phillips. Một $\alpha$ nhỏ (đường phẳng) nghĩa là NHTW phải chấp nhận một đợt suy thoái lớn để giảm một chút lạm phát ([[Sacrifice_Ratio_Mechanism|Sacrifice Ratio]]). [[Perry_Central_Bank_Policy_P4.md#page=231]]

---

## Evidence / Source Anchors

- Formulation of the supply-side equilibrium equation (Equation 1): [[Perry_Central_Bank_Policy_P4.md#page=230]]
- Identification of New Keynesian and New Neoclassical Synthesis as the foundation of ITF: [[Perry_Central_Bank_Policy_P4.md#page=230]]
- Analysis of microfoundations derived from optimal agent behavior: [[Perry_Central_Bank_Policy_P4.md#page=231]]
- Description of the relationship between future expectations and current pricing: [[Perry_Central_Bank_Policy_P4.md#page=230]]

## Related

- [[Inflation_Targeting_Framework_ITF]] — The regime that uses NKPC as its roadmap.
- [[Taylor_Rule_Monetary_Policy]] — The corresponding policy response function.
- [[Nominal_Rigidity_Models_Fischer_Taylor]] — The micro-foundation of the output gap link.
- [[Sacrifice_Ratio_Mechanism]] — The cost implied by the NKPC slope.
