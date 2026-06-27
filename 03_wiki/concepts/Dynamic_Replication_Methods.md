---
title: Dynamic Replication Methods
aliases:
- Dynamic Replication
- Portfolio Rebalancing
- Dynamic Hedging
type: concept
tags:
- financial-engineering
- replication
- risk-management
- hedging
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Dynamic replication is the extension of synthetic engineering to environments
  where static matching is impossible due to market gaps, illiquidity, or instrument
  nonlinearity, necessitating periodic portfolio rebalancing to maintain equivalence
  with a target asset.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 238
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 261-263
created: '2026-05-22'
updated: '2026-04-22'
---

## Thesis
[RAW] Dynamic replication là sự tổng quát hóa của [[Synthetics_Replicating_Portfolios|static replication]] (mô phỏng tĩnh). Nó là công cụ thiết yếu khi các "phương trình hợp đồng" (contractual equations) không thể được áp dụng một cách tĩnh do thiếu hụt thị trường, tính thanh khoản kém, hoặc tính phi tuyến của công cụ mục tiêu. Cơ chế cốt lõi là việc tái cân bằng (rebalancing) liên tục danh mục các tài sản thanh khoản để duy trì giá trị và rủi ro tương đương với tài sản mục tiêu.

## 1. Motivation: Why Static Replication Fails
[RAW] Neftci xác định 4 lý do chính khiến mô phỏng tĩnh thất bại và yêu cầu phương pháp động:

1.  **Nonexistence of Assets (Thiếu hụt tài sản):** Không có đủ các công cụ ở "vế phải" của phương trình hợp đồng để khớp chính xác dòng tiền.
2.  **Illiquidity (Kém thanh khoản):** Các thành phần lý thuyết có thể tồn tại nhưng không giao dịch tích cực. Giá của synthetic không đơn giản là tổng giá các thành phần nếu chúng không có giá thị trường sẵn dùng. Cần dùng các tài sản "tương tự" và điều chỉnh định kỳ.
3.  **Nonlinearity & Convexity (Tính phi tuyến và Độ lồi):** Các công cụ như options có tính chất phi tuyến. Việc dùng các công cụ tuyến tính để mô phỏng chúng yêu cầu phải tái cân bằng liên tục để duy trì sự xấp xỉ (e.g., Delta hedging).
- **Parameter Changes (Thay đổi tham số):** Các tham số định giá (lãi suất, volatility) thay đổi theo thời gian, yêu cầu điều chỉnh tỷ trọng danh mục.

5.  **Practitioner Strategy (The Dealer's Approach):** [RAW] Các tổ chức lớn thường chọn "tự sản xuất" (manufacture) quyền chọn bằng dynamic replication thay vì mua từ thị trường (Dealer). Điều này giúp tiết kiệm spread và phí bảo hiểm, đồng thời cho phép tạo ra các sản phẩm tùy chỉnh như **Synthetic Bond Options**. [[Principles_of_Financial_Engineering_Neftci.md#page=238]]

## 2. Theoretical vs. Practical Framework
[RAW]
- **Continuous Time (Exact):** Trong lý thuyết thời gian liên tục, việc tái cân bằng diễn ra vô hạn lần và tức thời, cho phép mô phỏng "hoàn hảo".
- **Discrete Time (Approximation):** Trong thực tế, tái cân bằng diễn ra tại các khoảng thời gian hữu hạn ($\delta$). Đây là một sự xấp xỉ. Độ chính xác bị ảnh hưởng bởi chi phí giao dịch (transaction costs), bước nhảy giá (jumps), và độ trễ.

## 3. Section 8.5: Principles & Mechanics (The Binomial Approach)
[RAW] Neftci thiết lập 3 nguyên tắc nền tảng để đảm bảo việc "chế tạo" (manufacturing) một synthetic thành công qua dynamic replication:
1.  **No Payouts:** Không có cổ tức hoặc các dòng tiền chi trả trung gian trong suốt vòng đời của chứng khoán mục tiêu. Danh mục mô phỏng phải khớp chính xác dòng tiền cuối cùng.
2.  **Self-Financing:** Không có các khoản bơm tiền hoặc rút tiền ròng sau khi thiết lập ban đầu. Chi phí ban đầu tại $t_0$ phải bằng đúng chi phí thực tế của toàn bộ chiến lược.
3.  **Credit Risk Parity:** Rủi ro tín dụng của synthetic và công cụ mục tiêu phải giống hệt nhau.

### 3.1 Binomial Tree Mechanics
[RAW] Để thực hiện mô phỏng động, ta cần một mô hình cho các biến số ngẫu nhiên (như lãi suất hoặc giá cổ phiếu) qua thời gian. [[Binomial_Trees|Cây nhị thức]] là mô hình phổ biến nhất cho mục đích này:
- **Discrete Time ($\Delta$):** Chia thời gian [t, T] thành các khoảng hữu hạn.
- **Up/Down States:** Tại mỗi nút (node), chỉ có hai trạng thái có thể xảy ra.
- **Non-recombining Paths:** Một cây không tái kết hợp (non-recombining) có nghĩa là một đợt giảm lãi suất sau một đợt tăng sẽ không dẫn đến cùng một mức giá/lãi suất như một đợt tăng sau một đợt giảm. Điều này quan trọng trong mô hình hóa lãi suất vì "con đường" (path) đi đến một nút có ý nghĩa kinh tế. [[Principles_of_Financial_Engineering_Neftci.md#page=251]]

### 3.2 The Replication Process (Backward Induction)
[RAW] Quá trình mô phỏng bắt đầu từ tương lai (đáo hạn) và lùi dần về hiện tại:
1.  **Terminal Payoff:** Xác định giá trị mục tiêu tại thời điểm đáo hạn (e.g., $100 cho trái phiếu 0 coupon).
2.  **Solving for Weights ($\theta$):** Tại mỗi nút trước đó, lập hệ hai phương trình với hai ẩn số là trọng số của "tài sản cho vay" ($\theta^{lend}$) và "tài sản rủi ro" ($\theta^{bond}$) để khớp với các giá trị tiềm năng tại nút tiếp theo.
3.  **Backward Step:** Tính toán chi phí thiết lập tại nút hiện tại (Fair value) và tiếp tục lùi về $t_0$.

## 4. Case Study: Bond Option Replication (Section 8.2)
[RAW] Một ví dụ thực tế về việc một quỹ quản lý tài sản tại San Francisco sử dụng dynamic replication để tạo ra chiến lược "Principal Preservation" (bảo toàn vốn):
- **Target:** Một call option trên trái phiếu nhằm cho phép nhà đầu tư hưởng lợi từ đà tăng (unlimited upside) nhưng không chịu rủi ro giảm giá (no downside).
- **Mechanism:** Sử dụng mô hình tính toán **Hedge Ratio (Delta)** hàng ngày để điều chỉnh tỷ trọng giữa trái phiếu và tiền mặt/lending.
- **Goal:** Mô phỏng biến động giá của option hàng ngày cho đến khi đáo hạn.
- **Expert Perspective:** Đây là cách tiếp cận của một "Dealer" hơn là một "Asset Manager" truyền thống vì họ tự tạo ra công cụ thay vì mua nó từ Street.

## 4. Core Mechanism: Self-Financing Requirement

[RAW] Để một chiến lược dynamic replication có giá trị trong định giá và phòng hộ, nó phải hướng tới tính **Self-financing** (tự tài trợ).
- Một chiến lược rollover đơn thuần (như vay ngắn hạn để tạo trái phiếu dài hạn) có thể thất bại nếu nó yêu cầu các khoản bơm tiền (cash injections) hoặc rút tiền (withdrawals) không biết trước tại các thời điểm tái cân bằng do biến động lãi suất/giá.
- [[Principles_of_Financial_Engineering_Neftci.md#page=243]]

## 5. Some Important Conditions (Neftci Section 8.6)
[RAW] Để phương pháp dynamic replication hoạt động chính xác, cần thỏa mãn hai điều kiện nền tảng:

### 5.1. Arbitrage-Free Initial Conditions
[RAW] Các phương pháp mô phỏng (dynamic methods) chỉ hoạt động nếu bắt đầu từ các động thái (dynamics) loại trừ cơ hội arbitrage ngay từ đầu. Nếu không, các kết quả tính toán sẽ bị sai lệch (e.g., giá trái phiếu hoặc option có thể bị âm).
- **Condition:** Tại mọi nút (node) trong cây nhị thức, lãi suất phi rủi ro ($L_j$) phải nằm giữa hai mức sinh lời tiềm năng ($R_{down}$ và $R_{up}$) của tài sản rủi ro:
  $$R_{down} \le L_j \le R_{up}$$
- **Bond Specifics:** Đối với trái phiếu, trước khi đáo hạn, điều kiện này yêu cầu $R_{down} = L_j = R_{up}$ do tính chất arbitrage của thị trường nợ. [[Principles_of_Financial_Engineering_Neftci.md#page=261]]
- **Martingale Dynamics:** Cấu trúc cây phải tuân thủ các đặc tính Martingale để đảm bảo tính không-arbitrage (chi tiết tại Chương 11).

### 5.2. Role of Binomial Structure (One-Factor Model)
[RAW] Cấu trúc cây nhị thức dựa trên một giả định mạnh về mối tương quan:
- **Perfect Correlation:** Giả định rằng lợi suất trái phiếu dài hạn và lãi suất ngắn hạn biến động cùng hướng (perfectly correlated). Khi lãi suất ngắn hạn giảm, giá trái phiếu (hoặc lợi suất dài hạn) cũng biến động một cách hệ thống tương ứng.
- **One-Factor Model:** Giả định chỉ có một biến ngẫu nhiên duy nhất (single random variable) quyết định giá trị tương lai của mọi tài sản tại mỗi nút.
- **Limitations:** Trong thực tế, nhiều yếu tố ngẫu nhiên khác có thể tác động khiến giá trái phiếu đi ngược hướng lãi suất ngắn hạn. Điều này yêu cầu các mô hình phức tạp hơn (trinomial trees hoặc multi-factor models) và cần nhiều tài sản cơ sở (base assets) hơn để tạo ra một synthetic hoàn hảo. [[Principles_of_Financial_Engineering_Neftci.md#page=262]]

## 6. Real-Life Complications (Section 8.7)
[RAW] Mô phỏng động trong thực tế "mong manh" (fragile) hơn mô phỏng tĩnh do các yếu tố ma sát thị trường:
1. **Bid-Ask Spreads & Liquidity:** Việc tái cân bằng thường xuyên làm tăng chi phí spread. Khác với mô phỏng tĩnh, chi phí thanh khoản tương lai không thể biết trước tại $t_0$, tạo thêm rủi ro cho synthetic.
2. **Model Risk & Jumps:** Các mô hình dựa trên thời gian rời rạc là sự xấp xỉ. Các "bước nhảy" (jumps) giá bất ngờ có thể phá vỡ tính liên tục cần thiết cho việc phòng hộ hoàn hảo. Chi tiết tại [[Model_Risk_And_Jumps]].
3. **Operational Costs:** Đòi hỏi hệ thống phần mềm quản lý vị thế và nhân sự kỹ thuật cao, dẫn đến chi phí vận hành lớn.
4. **Volatility Sensitivity:** Các công cụ phi tuyến (nonlinear) như options cực kỳ nhạy cảm với biến động của volatility. Nếu volatility thay đổi không dự tính được (volatility shocks), chiến lược phòng hộ delta sẽ trở nên không chính xác.

## 7. Conclusions: The Sequence of Weights (Section 8.8)
[RAW] Neftci kết luận rằng sự khác biệt cốt lõi giữa mô phỏng tĩnh và động nằm ở bản chất của "phương trình":
- **Static:** Trọng số (weights) cố định, phương trình mang tính hợp đồng (contractual).
- **Dynamic:** Trọng số $\theta_t$ thay đổi theo thời gian, phương trình mang tính đại số (algebraic) và cần máy tính xử lý.
- **Sequence of Weights:** Một dynamic synthetic thực chất là một chuỗi các trọng số $\{\theta_1, \theta_2, \dots, \theta_n\}$ được thiết kế để duy trì tính [[Self_Financing_Portfolio|self-financing]]. Đây là một "thuật toán" (algorithm) hơn là một danh mục tài sản cố định.

## Strategic Dynamics
[LLM] Dynamic replication chuyển rủi ro từ "Market Risk" (biến động giá) sang "Model Risk" và "Execution Risk".
- Thay vì lo lắng về việc giá tài sản mục tiêu đi đâu, nhà kỹ thuật tài chính lo lắng về việc mô hình tái cân bằng (Hedge ratio) có chính xác không và chi phí giao dịch có ăn mòn lợi nhuận không.
- **Market Impact:** Khi nhiều nhà đầu tư cùng thực hiện delta hedging (ví dụ: bán tài sản cơ sở khi thị trường giảm để giữ vị thế trung lập cho put option), họ có thể tạo ra áp lực bán tháo, làm trầm trọng thêm các đợt điều chỉnh thị trường (feedback loop).
- **Volatility Smile:** Sự phụ thuộc của Delta vào volatility có nghĩa là nếu thị trường xuất hiện "nụ cười biến động" (volatility smile), các phương pháp mô phỏng nhị thức đơn giản sẽ thất bại trong việc khớp giá trị thực tế.

## Related
- [[Synthetics_Replicating_Portfolios]] — Khung lý thuyết cơ bản.
- [[Convexity]] — Lý do chính đòi hỏi sự tái cân bằng.
- [[Self_Financing_Portfolio]] — Điều kiện bắt buộc cho tính hợp lệ của mô phỏng.
- [[Binomial_Trees]] — Công cụ triển khai mô hình 1-factor.
- [[Model_Risk_And_Jumps]] — Rủi ro phát sinh từ các giả định mô hình và bước nhảy giá.
