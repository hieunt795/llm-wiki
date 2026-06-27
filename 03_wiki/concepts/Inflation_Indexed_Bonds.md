---
title: Inflation-Indexed Bonds
aliases:
- Linkers
- Real Bonds
- Inflation-Linked Debt
- Capital-Indexed Bonds
- Trái phiếu chống lạm phát
type: definition
tags:
- fixed-income
- inflation
- macroeconomics
- sovereign-debt
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch24.md
thesis: Trái phiếu chống lạm phát (Linkers) là công cụ nợ có dòng tiền được liên kết
  trực tiếp với một chỉ số giá tiêu dùng, giúp bảo vệ sức mua của nhà đầu tư và đóng
  vai trò như một công cụ phòng vệ của Chính phủ đối với hiện tượng 'tax creep'.
source_refs:
- file: During_Fixed_Income_Ch24.md
  page: 227
- file: During_Fixed_Income_Ch24.md
  page: 229
- file: During_Fixed_Income_Ch24.md
  page: 230
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

While nominal bonds provide a fixed income in currency terms, investors are ultimately interested in **consumption**. Alexander Düring explains that Linkers solve the uncertainty of future price developments by committing to compensate the lender for any loss in purchasing power. Historically and mathematically, they can be viewed as foreign currency bonds where the "currency" is a hypothetical unit of constant purchasing power. [[During_Fixed_Income_Ch24.md#page=227-230]]

## Definition: Real vs. Nominal Income

- **Nominal Bonds:** Provide a steady stream of currency units. In high-inflation environments, the real value of these units evaporates.
- **Inflation-indexed Bonds:** Provide a steady stream of **goods/consumption**. Coupons and principal are adjusted by an inflation index (CPI), ensuring the investor can purchase the same basket of goods regardless of price levels. [[During_Fixed_Income_Ch24.md#page=227]]

### Historical Origin: Massachusetts 1780
The first known inflation-linked bond was issued by the State of Massachusetts during the War of Independence.
- **The Basket:** Paid in "Five Bushels of CORN, sixty-eight Pounds of BEEF, Ten Pounds of SHEEPS WOOL, and Sixteen Pounds of SOLE LEATHER."
- **The Context:** At the time, inflation was running at 220% annually, making nominal payments worthless to soldiers. [[During_Fixed_Income_Ch24.md#page=227-228]]

## Issuance Dynamics

### 1. The Sovereign Incentive: Tax Creep
Governments with progressive income tax systems have a natural "long position" in inflation.
- **Mechanism:** Inflation pushes citizens into higher tax brackets without any increase in real income (Tax Creep). This increases the government's tax take as a share of GDP.
- **The Hedge:** Governments issue inflation-indexed bonds to create an offsetting "short position" in inflation, hedging their exposure to tax creep. [[During_Fixed_Income_Ch24.md#page=229]]

### 2. The Investor Incentive: Liability Matching
Institutions like pension funds and life insurance companies have explicit inflation-linked promises to their clients. Linkers are the only high-quality assets that perfectly match the duration and inflation-sensitivity of these liabilities. [[During_Fixed_Income_Ch24.md#page=230]]

---

## 3. Worked Example: Calculating the Index Ratio

Giả sử bạn mua một trái phiếu TIPS với các thông số sau:
- **Mệnh giá gốc ban đầu ($P_0$):** 1,000 USD
- **Lãi suất Coupon thực (Real Coupon):** 2% / năm
- **Chỉ số CPI tại ngày phát hành ($CPI_{base}$):** 100

### Step 1: Tính Index Ratio sau 1 năm
Giả sử sau 1 năm, lạm phát tăng 5%, chỉ số CPI lúc này ($CPI_{current}$) là 105.
$$\text{Index Ratio} = \frac{CPI_{current}}{CPI_{base}} = \frac{105}{100} = 1.05$$

### Step 2: Điều chỉnh Mệnh giá gốc (Adjusted Principal)
Mệnh giá gốc mới dùng để tính lãi và trả nợ sẽ là:
$$P_{adj} = P_0 \times \text{Index Ratio} = 1,000 \times 1.05 = 1,050 \text{ USD}$$

### Step 3: Tính toán tiền lãi thực nhận (Coupon Payment)
Số tiền lãi thực nhận cuối kỳ 1:
$$\text{Coupon}_{adj} = P_{adj} \times \text{Real Coupon} = 1,050 \times 2\% = 21 \text{ USD}$$

---

## The FX Analogy

Düring provides a powerful mathematical lăng kính:
- An inflation index $I_t$ behaves exactly like an **FX Rate**.
- The inflation-linked bond is a bond denominated in a hypothetical foreign currency.
- The **Real Yield** is the yield of the bond in its home currency (the purchasing power unit).
- The **Nominal Yield** (on nominal bonds) is the best estimate of the return when converted back into the "local" currency (inflated cash). [[During_Fixed_Income_Ch24.md#page=230]]

## Evidence / Source Anchors

- Analysis of inflation-indexed debt as a steady stream of goods vs. currency: [[During_Fixed_Income_Ch24.md#page=227]]
- Detailed breakdown of the 1780 Massachusetts basket bond structure: [[During_Fixed_Income_Ch24.md#page=228-229]]
- Definition of Tax Creep as a driver for government linker issuance: [[During_Fixed_Income_Ch24.md#page=229]]
- Establishment of the FX Analogy for modeling linker risk and return: [[During_Fixed_Income_Ch24.md#page=230]]

## Related

- [[TIPS_Bond_Structure]] — The dominant implementation (Capital-indexed).
- [[Interest_Indexed_Bonds]] — The floating-rate alternative (Pay-as-you-go).
- [[Breakeven_Inflation_Metrics]] — How the market prices these instruments.
- [[Inflation_Seasonality_And_Pricing]] — The primary "noise" in linker valuations.
- [[Real_Yield_Definition]] — The return metric used in the purchasing power unit.
