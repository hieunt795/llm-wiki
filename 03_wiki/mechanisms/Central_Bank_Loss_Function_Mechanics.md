---
title: Central Bank Loss Function Mechanics
aliases:
- Policy Loss Function
- Social Welfare Function (Monetary)
- Inflation-Output Trade-off
- Hàm tổn thất NHTW
type: mechanism
tags:
- monetary-policy
- central-banking
- economics
- optimization
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The central bank loss function is a mathematical tool used to evaluate policy
  performance, where the bank seeks to minimize a weighted sum of squared deviations
  of inflation and output from their respective targets.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 231
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Làm sao để biết một chính sách là "tốt"? Perry Warjiyo bóc tách ranh giới của sự tối ưu: NHTW không chỉ nhìn vào một biến số duy nhất. **Hàm Tổn thất (Loss Function)** là thước đo sự "đau đớn" của xã hội do những bất ổn kinh tế gây ra. Bằng cách tối thiểu hóa hàm này, NHTW tìm ra điểm cân bằng tối ưu giữa việc kiềm chế lạm phát và bảo vệ tăng trưởng sản lượng. [[Perry_Central_Bank_Policy_P4.md#page=231]]

---

## 1. The Mathematical Structure

Hàm tổn thất tiêu chuẩn được biểu diễn dưới dạng bậc hai (quadratic):
$$L_t = E_t \sum_{j=0}^{\infty} \delta^j [(\pi_{t+j} - \pi^*)^2 + \lambda x^2_{t+j}]$$

### A. The Components
- **$(\pi - \pi^*)^2$:** Độ lệch lạm phát thực so với mục tiêu. Bình phương nghĩa là NHTW ghét lạm phát quá cao cũng như quá thấp (tính đối xứng).
- **$x^2$:** Khoảng cách sản lượng ($y - y^*$).
- **$\lambda$ (The Weight):** Trọng số thể hiện ưu tiên của NHTW. Nếu $\lambda = 0$, NHTW là một "Inflation Nutter" (chỉ quan tâm lạm phát). Nếu $\lambda > 0$, NHTW thực hiện **Flexible ITF**. [[Perry_Central_Bank_Policy_P4.md#page=231]]

### B. The Targeting Rule
Khi giải bài toán tối thiểu hóa hàm tổn thất kết hợp với ràng buộc của [[New_Keynesian_Phillips_Curve_NKPC|NKPC]], ta thu được quy tắc mục tiêu tối ưu:
$$\pi_t + \frac{\lambda}{\alpha} x_t = 0$$
- **Ý nghĩa:** Nếu có một cú shock làm lạm phát tăng ($\pi > 0$), NHTW phải chấp nhận một khoảng cách sản lượng âm ($x < 0$) để đưa hệ thống về cân bằng. Tỷ lệ đánh đổi phụ thuộc vào trọng số ưu tiên ($\lambda$) và độ dốc của đường Phillips ($\alpha$). [[Perry_Central_Bank_Policy_P4.md#page=231]]

---

## 2. Strategic Implications: Credibility & Welfare

Perry Warjiyo nhấn mạnh rằng hàm tổn thất này dựa trên **Microfoundations**:
- **Social Welfare:** Tối thiểu hóa $L_t$ tương đương với việc tối đa hóa phúc lợi của hộ gia đình đại diện trong nền kinh tế.
- **Dynamic Consistency:** NHTW phải tính đến giá trị hiện tại của các tổn thất trong tương lai thông qua hệ số chiết khấu $\delta$.
- **Certainty Equivalence:** Trong mô hình tuyến tính, NHTW hành động dựa trên các giá trị kỳ vọng như thể chúng là chắc chắn, nhưng phải cực kỳ thận trọng với các sai số stochastic ($\epsilon, u, \upsilon$). [[Perry_Central_Bank_Policy_P4.md#page=231]]

---

## Evidence / Source Anchors

- Formulation of the quadratic loss function (Equation 4): [[Perry_Central_Bank_Policy_P4.md#page=231]]
- Derivation of the optimal targeting rule linking inflation and output gap (Equation 5): [[Perry_Central_Bank_Policy_P4.md#page=231]]
- Analysis of weights ($\lambda$) in determining the policy stance (Strict vs. Flexible): [[Perry_Central_Bank_Policy_P4.md#page=231]]
- Identification of welfare maximization as the underlying objective of the loss function: [[Perry_Central_Bank_Policy_P4.md#page=231]]

## Related

- [[Inflation_Targeting_Framework_ITF]] — The strategic framework using this function.
- [[New_Keynesian_Phillips_Curve_NKPC]] — The structural constraint of the loss function.
- [[Sacrifice_Ratio_Mechanism]] — The empirical cost derived from this trade-off.
- [[Strict_vs_Flexible_Inflation_Targeting]] — The classification based on $\lambda$.
- [[Central_Bank_Quadratic_Loss_Function]]
- [[Loss_Function_Central_Bank]]
- [[Rules_Vs_Discretion_Debate]]
- [[Central_Bank_Coordination_Framework]]
- [[Principles_of_Central_Bank_Reputation_and_Effectiveness]]
- [[Central_Bank_Definition]]
- [[Central_Bank_Definition_And_Mandates]]
- [[Central_Bank_Evolutionary_Episodes]]
- [[Central_Bank_Independence_Framework]]
- [[Central_Bank_Operational_Frameworks]]
- [[Central_Bank_Operational_Framework_Design]]
- [[Operational_Targeting_Price_Vs_Quantity]]
