---
title: Barro-Gordon Model (Inflation Bias)
aliases:
- Barro-Gordon 1983
- Inflation Bias Mechanism
- Time Inconsistency Model
- Conservative Central Banker
- Optimal Contract for Central Banks
- Mô hình Barro-Gordon
- Barro-Gordon Time Inconsistency Model
- Barro-Gordon Model of Policy Credibility
type: mechanism
tags:
- monetary-theory
- credibility
- game-theory
- central-banking
- macroeconomics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (Warjiyo & During)
thesis: The Barro-Gordon model formalizes the time inconsistency problem, demonstrating
  that without institutional commitment or independence, a central bank's incentive
  to create surprise inflation leads to a sub-optimal 'Inflation Bias' without reducing
  unemployment.
source_refs:
- file: Perry_Central_Bank_Policy_P5.md
  page: 301
- file: Perry_Central_Bank_Policy_P5.md
  page: 302
- file: Perry_Central_Bank_Policy_P5.md
  page: 303
- file: During_Fixed_Income_Ch05.md
  page: 34
- file: Perry_Central_Bank_Policy_P4.md
  page: 301
created: '2026-04-18'
updated: '2026-04-26'
chapter: 10
---

# [[Barro_Gordon_Model]]

## Thesis
[WIKI/LLM] NHTW nên được thiết kế như thế nào để thoát khỏi "Cái bẫy chính trị"? Mô hình Barro-Gordon (1983) sử dụng lý thuyết trò chơi để chứng minh rằng dưới cơ chế tự ý (discretion), kỳ vọng của công chúng sẽ điều chỉnh theo sự không nhất quán của NHTW, dẫn đến thiên kiến lạm phát (inflation bias) mà không cải thiện được sản lượng. Một quy tắc cam kết (rule-based) giúp đạt mục tiêu lạm phát với chi phí xã hội thấp nhất. [[Perry_Central_Bank_Policy_P5.md#page=301]] [[During_Fixed_Income_Ch05.md#page=34]]

## Mechanism

### 1. Social Loss Function and Constraints
[RAW] The central bank aims to minimize a social loss function $L$ representing social costs:
$L = b(U - U^*)^2 + \pi^2$ [[Perry_Central_Bank_Policy_P4.md#page=301]]
Where:
- $b > 0$: weight assigned to unemployment relative to inflation.
- $U, U^*$: actual and targeted unemployment ($U^* = k U_n$, $0 < k < 1$).
- $\pi$: actual inflation.

[RAW] The relationship follows the Expectations-Augmented Phillips Curve (EAPC):
$U = U_n - a(\pi - \pi^e)$ [[Perry_Central_Bank_Policy_P4.md#page=301]]

### 2. The Inflation Bias Trap (Nash Equilibrium)
[RAW] Under discretion, the central bank minimizes social costs, resulting in an optimal inflation rate $\pi^{**}$ influenced by expectations:
$\pi^{**} = \frac{ab(1-k)U_n}{1 + a^2b} + \frac{a^2b\pi^e}{1 + a^2b}$ [[Perry_Central_Bank_Policy_P4.md#page=302]]

[WIKI] Cơ chế này vận hành như một trò chơi:
1.  **The Temptation:** NHTW muốn tạo "lạm phát bất ngờ" để đẩy $U < U_n$.
2.  **The Anticipation:** Công chúng (rational agents) biết được ý đồ này và tăng kỳ vọng lạm phát $\pi^e$ ngay lập tức.
3.  **Outcome:** Điểm cân bằng Nash dẫn đến $\pi_{REH} = ab(1-k)U_n$. Lạm phát dương nhưng thất nghiệp vẫn ở mức tự nhiên. Xã hội gánh chịu tổn thất tối đa (**Stagflation**).

### 3. Comparison of Policy Regimes
[RAW] Warjiyo (citing Bofinger, 2000) compares:
1. **Surprise Inflation ($L_S$):** Lowest social cost (unsustainable).
2. **Inflation Rule ($L_{RULE}$):** Bank commits to $\pi=0$. Moderate cost, high credibility.
3. **Inflation Bias ($L_{REH}$):** Highest social cost, zero credibility.
[RAW] Hierarchy of social costs: $L_S < L_{RULE} < L_{REH}$. [[Perry_Central_Bank_Policy_P4.md#page=303]]

---

## Theoretical Solutions (Warjiyo's Lens)

### A. The Rogoff Solution: Conservative Central Banker (1985)
- [WIKI] Xã hội nên thuê một Thống đốc có mức độ "ghét" lạm phát cao hơn mức trung bình của xã hội (tham số $b$ nhỏ). Điều này làm giảm độ dốc của phản ứng lạm phát. [[Perry_Central_Bank_Policy_P5.md#page=296]]

### B. The Walsh Solution: Optimal Contract (1995)
- [WIKI] Ký hợp đồng thưởng/phạt Thống đốc dựa trên kết quả lạm phát thực tế để triệt tiêu động lực "gian lận" kỳ vọng. [[Perry_Central_Bank_Policy_P5.md#page=297]]

### C. Connection to Trilemma
[WIKI/LLM] Đối với các nền kinh tế mới nổi (EMEs), uy tín thường được "vay mượn" thông qua [[Policy_Trilemma.md]]. Việc cố định tỷ giá hối đoái vào một đồng tiền có uy tín cao (như USD) đóng vai trò như một quy tắc cam kết ngoại vi để giải quyết bài toán Barro-Gordon, mặc dù buộc phải đánh đổi sự độc lập của chính sách tiền tệ nếu dòng vốn tự do lưu chuyển.

---

## Market Verification (Düring's Lens)

[WIKI] Sự độc lập không chỉ là lý thuyết; nó có biểu hiện vật lý trên thị trường tài chính:
- **Inflation Premium:** Nếu NHTW không độc lập, nhà đầu tư sẽ yêu cầu mức lợi suất (yield) cao hơn cho trái phiếu dài hạn để bù đắp rủi ro lạm phát chính trị.
- **Yield Curve Anchor:** NHTW độc lập giúp "ghim" phần đầu của đường cong lợi suất, giảm chi phí vốn thực tế bằng cách loại bỏ biến số bất định từ chính sách tùy nghi. [[During_Fixed_Income_Ch05.md#page=34]]

---

## Evidence / Source Anchors
- [[Perry_Central_Bank_Policy_P4.md#page=301]] — Definition of the social loss function and EAPC.
- [[Perry_Central_Bank_Policy_P4.md#page=302]] — Mathematical derivation of optimal inflation.
- [[During_Fixed_Income_Ch05.md#page=34]] — Market signaling role of independence in yield curves.
- [[Perry_Central_Bank_Policy_P4.md#page=303]] — Comparison of social costs $L_S$, $L_{RULE}$, and $L_{REH}$.

## Related
- [[Time_Inconsistency_Problem]]
- [[Expectations-Augmented_Phillips_Curve]]
- [[Inflation_Bias]]
- [[Policy_Trilemma.md]]
- [[Central_Bank_Independence.md]]
- [[Inflation_Targeting_Framework.md]]
- [[Yield_Curve_Mechanics]]
