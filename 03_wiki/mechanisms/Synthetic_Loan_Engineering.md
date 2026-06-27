---
title: Synthetic Loan Engineering
aliases:
- Synthetic USD Loan
- Japanese Premium Hedge
- Khoản vay giả lập
type: mechanism
tags:
- financial-engineering
- fx-forwards
- funding
- arbitrage
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Synthetic loan engineering is the process of replicating a loan in currency
  A by borrowing in currency B and using FX spot and forward contracts to fix the
  entry and exit exchange rates, often used to bypass credit limits or high funding
  premiums.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 187
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

[RAW] Salih Neftci minh họa rằng khi một thị trường vốn bị tắc nghẽn hoặc quá đắt đỏ (như trường hợp "Japanese Premium" năm 1997), các kỹ sư tài chính có thể sử dụng phương trình hợp đồng (contractual equation) để "nhập khẩu" thanh khoản từ một đồng tiền khác. Một khoản vay USD có thể được tái lập hoàn hảo bằng cách vay JPY và sử dụng các chân giao dịch FX để triệt tiêu rủi ro tỷ giá. [[Principles_of_Financial_Engineering_Neftci.md#page=187]]

---

## 1. The Contractual Equation for Synthetic Loans

Để tạo ra một khoản vay giả lập bằng đồng USD ($USD_{loan}$) từ đồng Yên ($JPY$), ta sử dụng tổ hợp sau:

$$ \text{Synthetic USD Loan} = \text{Borrow JPY} + \text{Spot Buy USD/Sell JPY} + \text{Forward Sell USD/Buy JPY} $$

### Step-by-Step Mechanics:
1.  **Borrow JPY (t=0):** Vay một lượng Yên Nhật tại thị trường nội địa với lãi suất $r_{JPY}$.
2.  **Spot Exchange (t=0):** Đổi ngay lượng Yên vừa vay lấy USD tại tỷ giá Spot $e_{t0}$. Lúc này, nhà đầu tư có USD mặt để sử dụng.
3.  **Forward Hedge (t=0 for t=1):** Ký hợp đồng bán USD mua lại JPY tại thời điểm đáo hạn $t_1$ với tỷ giá kỳ hạn $F_{t0}$. Điều này đảm bảo nhà đầu tư biết chính xác cần bao nhiêu USD để trả khoản nợ JPY gốc.

---

## 2. Case Study: The "Japanese Premium" (1997)

[RAW] Sau sự sụp đổ của Ngân hàng Hokkaido Takushoku, các ngân hàng Nhật Bản phải đối mặt với mức phí cộng thêm (Premium) lên tới 40 bps khi vay Eurodollar trực tiếp so với các ngân hàng Mỹ.

*   **Problem:** Vay USD trực tiếp quá đắt hoặc không khả thi do giới hạn tín dụng (Credit lines).
*   **Solution:** Các ngân hàng Nhật quay về thị trường nội địa vay JPY (vốn dĩ rẻ và sẵn có), sau đó thực hiện chân giao dịch Spot và Forward như trên để có USD.
*   **Market Impact:** Hành động này đẩy nhu cầu mua Forward JPY (bán Forward USD) tăng vọt, làm tỷ giá Forward JPY trở nên đắt đỏ (richen dramatically), chứng minh rằng rủi ro tín dụng tại một thị trường có thể truyền dẫn sang giá cả của thị trường phái sinh FX. [[Principles_of_Financial_Engineering_Neftci.md#page=188]]

---

## 3. Applications and Limits

- **Credit Line Optimization:** Khi hạn mức vay USD của một công ty đã hết, họ có thể dùng hạn mức vay EUR còn trống để tạo Synthetic USD loan.
- **Capital Controls Bypass:** Trong các thị trường bị kiểm soát vốn (e.g., Brazil), các doanh nghiệp sử dụng "Parallel Loans" (tiền thân của synthetic loans) để có ngoại tệ.
- **Cost Analysis:** Chi phí của khoản vay giả lập bằng: $r_{foreign} + (F_{t0} - e_{t0})/e_{t0}$. Theo CIRP, chi phí này sẽ xấp xỉ lãi suất vay nội địa trừ khi có các rào cản trọng tài (Limits of Arbitrage).

---

## Evidence / Source Anchors

- The contractual equation for synthetic USD loans: [[Principles_of_Financial_Engineering_Neftci.md#page=188]]
- Historical context of the Japanese Premium (1997): [[Principles_of_Financial_Engineering_Neftci.md#page=187]]
- Use of parallel loans to bypass capital controls: [[Principles_of_Financial_Engineering_Neftci.md#page=189]]

## Related

- [[FX_Forward_Engineering]] — Nền tảng phân rã dòng tiền.
- [[Covered_Interest_Parity]] — Cơ sở định giá của cấu trúc này.
- [[Currency_Forward_Synthetics]] — Các ứng dụng giả lập khác.
