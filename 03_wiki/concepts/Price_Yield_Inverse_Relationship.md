---
title: Price-Yield Inverse Relationship
aliases:
- Inverse Relationship
- Bond Price vs Yield
- Mối quan hệ nghịch đảo Giá-Lãi suất
type: concept
tags:
- fixed-income
- valuation
- foundations
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Moorad Choudhry"
provenance: Homer_Leibowitz_Yield_Book.md
thesis: Mối quan hệ nghịch đảo giữa giá và lãi suất trái phiếu (Price-Yield Inverse
  Relationship) là một hệ quả cơ học tất yếu của việc định giá dòng tiền cố định trong
  tương lai dựa trên chi phí cơ hội hiện tại của vốn.
source_refs:
- file: Homer_Leibowitz_Yield_Book.md
- file: Choudhry_Fixed_Income_Markets.md
created: '2026-04-24'
updated: '2026-04-24'
---

## Thesis

Trong thị trường thu nhập cố định (Fixed Income), khi lãi suất thị trường tăng, giá trái phiếu hiện hữu sẽ giảm và ngược lại. Đây không phải là một quan sát tâm lý mà là một phép toán cơ học dựa trên giá trị thời gian của tiền (Time Value of Money). [RAW]

## 1. Cơ chế 1: Cỗ máy chiết khấu (The Discounting Engine)

Về mặt toán học, giá của một trái phiếu ($P$) là tổng giá trị hiện tại (Present Value) của tất cả các dòng tiền (Coupons $C$ và Mệnh giá $M$) trong tương lai.

$$P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{M}{(1+r)^n}$$

- **Biến số $r$ (Lãi suất chiết khấu):** Nằm ở mẫu số. Khi lãi suất thị trường tăng, mẫu số lớn lên, làm giảm giá trị hiện tại của từng dòng tiền tương lai.
- **Tác động lũy kế:** Vì các dòng tiền nằm ở các thời điểm xa (n lớn), tác động của việc thay đổi $r$ ở mẫu số sẽ được khuếch đại (compounding effect).

## 2. Cơ chế 2: Chi phí cơ hội (Opportunity Cost)

Dưới góc độ kinh tế học, mối quan hệ này phản ánh sự cạnh tranh giữa các tài sản trên thị trường.

- **Khi lãi suất giảm:** Các trái phiếu mới phát hành sẽ có mức Coupon thấp hơn. Trái phiếu cũ (với Coupon cao hơn) trở nên hấp dẫn vượt trội. Nhà đầu tư sẵn sàng trả một mức giá cao hơn mệnh giá (Premium) để sở hữu dòng thu nhập cao này.
- **Khi lãi suất tăng:** Trái phiếu cũ trở nên "lạc hậu" vì trả lãi thấp hơn thị trường. Để bán được trái phiếu này, người bán buộc phải giảm giá xuống dưới mệnh giá (Discount) để người mua mới đạt được mức tỷ suất sinh lời (Yield) tương đương với thị trường.

## 3. Ví dụ minh họa (Worked Example)

Xét một trái phiếu mệnh giá $1,000, Coupon 10% ($100/năm), kỳ hạn 1 năm.

| Kịch bản | Lãi suất thị trường | Giá trái phiếu tính toán | Trạng thái |
| :--- | :--- | :--- | :--- |
| **Gốc** | **10%** | $(100 + 1,000) / 1.10 = \$1,000$ | **Par** |
| **Lãi suất giảm** | **5%** | $(100 + 1,000) / 1.05 = \$1,047.6$ | **Premium** |
| **Lãi suất tăng** | **15%** | $(100 + 1,000) / 1.15 = \$956.5$ | **Discount** |

## 4. Sơ đồ truyền dẫn (Transmission Flow)

```ascii
LÃI SUẤT THỊ TRƯỜNG GIẢM (▼ r)
          │
          ▼
TĂNG GIÁ TRỊ HIỆN TẠI (PV) CỦA DÒNG TIỀN CỐ ĐỊNH
          │
          ▼
CẦU TRÁI PHIẾU "LÃI SUẤT CAO" CŨ TĂNG (▲ Demand)
          │
          ▼
GIÁ TRÁI PHIẾU TĂNG TRÊN MỆNH GIÁ (▲ Price > Par)
          │
          ▼
YIELD (TỶ SUẤT SINH LỜI) CỦA TRÁI PHIẾU GIẢM XUỐNG MỨC CÂN BẰNG MỚI
```

## 5. Các đặc tính biên

- **Convexity (Độ lồi):** Mối quan hệ Price-Yield không phải là đường thẳng mà là một đường cong lồi về phía gốc tọa độ. Điều này có nghĩa là khi lãi suất giảm, giá tăng mạnh hơn so với mức giảm giá khi lãi suất tăng cùng một biên độ. [[Convexity]]
- **Duration (Độ nhạy):** Thời gian đáo hạn càng dài, độ nhạy của giá đối với lãi suất càng lớn. [[Macaulay_Duration]]

## Related

- [[Bond_Relative_Value_Valuation]] — Cách định giá dựa trên chênh lệch Yield.
- [[Convexity]] — Sự bất đối xứng trong thay đổi giá.
- [[Interest_Rate_Risk]] — Rủi ro hệ thống từ biến động lãi suất.
