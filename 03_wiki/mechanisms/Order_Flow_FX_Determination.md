---
title: Order Flow FX Determination
aliases:
- FX Market Microstructure
- Order Flow Model
- Evans-Lyons Model
- Trading Flow Information
type: mechanism
tags:
- fx
- market-infrastructure
- information-asymmetry
- trading
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The order flow model of exchange rate determination asserts that trading flows
  are the primary medium for transmitting private information to market prices, explaining
  short-term FX volatility that fundamental models (random walk) fail to capture.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 93
- file: Perry_Central_Bank_Policy_P3.md
  page: 94
- file: Perry_Central_Bank_Policy_P3.md
  page: 95
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Traditional macroeconomic models (PPP, IRP) fail to predict short-term FX movements, a phenomenon known as the **Exchange Rate Puzzle**. Perry Warjiyo (trích dẫn Evans & Lyons, 2002) giải mã cơ chế bế tắc này: tỷ giá không chỉ nhảy theo tin tức công khai mà còn chạy theo **Order Flows** (hiệu số giữa lệnh mua và lệnh bán). Luồng lệnh chính là "vật mang" các mẩu thông tin riêng tư chưa được phản ánh vào giá. [[Perry_Central_Bank_Policy_P3.md#page=93]]

---

## Mechanism: The Microstructure Channel

The relationship is expressed as:
$$\Delta S_{t+1} = \beta_i(r - r^*) + \beta_z O_t$$
- **$O_t$ (Order Flow):** An indicator of net buying/selling pressure.
- **$(r - r^*)$:** Macro fundamentals (interest rate disparity). [[Perry_Central_Bank_Policy_P3.md#page=94]]

### 1. Private Information Transmission
Market players (notably large commercial banks) possess private information from their vast customer networks.
- **The Process:** This information is only revealed to the market when the bank executes a trade.
- **The Signal:** Each transaction acts as a signal. Evans and Lyons (2002) found that an aggressive increase in purchases of **$1 billion** causes a **0.5% appreciation** in the USD/DEM pair. [[Perry_Central_Bank_Policy_P3.md#page=95]]

### 2. The Multi-Segment Market
The FX market consists of two layers that process information differently:
- **Customer-to-Dealer:** Quote-driven transactions based on commercial needs (exports/imports).
- **Interdealer:** Order-driven transactions where banks manage their own risk and speculate on private information. This segment provides **70%** of the explanatory power for short-term volatility. [[Perry_Central_Bank_Policy_P3.md#page=93-94]]

---

## Strategic Implications: The News Filter

The model explains why exchange rates can move even without public "news."
- **Bayesian Extraction:** Market players attempt to extract the "relative demand signal" from the "order flow noise."
- **Perception Bias:** Because players have heterogeneous information, their reactions to the same order flow vary, creating the high volatility observed in the **Dornbusch Overshooting** phase. [[Perry_Central_Bank_Policy_P3.md#page=96]]

## Evidence / Source Anchors

- Analysis of the failure of macro models vs. random walk (Meese & Rogoff puzzle): [[Perry_Central_Bank_Policy_P3.md#page=93]]
- Statistical proof that order flows explain 70% of daily FX fluctuations: [[Perry_Central_Bank_Policy_P3.md#page=95]]
- Identification of large banks as holders of excess information due to network effects: [[Perry_Central_Bank_Policy_P3.md#page=94]]
- Mathematical derivation of the market microstructure FX equation: [[Perry_Central_Bank_Policy_P3.md#page=94]]

## Related

- [[Exchange_Rate_Determination_Theories]] — The broader theoretical umbrella.
- [[Dornbusch_Overshooting_Model]] — Why microstructure noise leads to overshooting.
- [[OTC_Trade_Lifecycle]] — The operational process that generates order flow.
- [[Information_Leakage_In_Trading]] — The risk inherent in large order flow execution.
- [[Order_Flow_Mechanism]]
- [[FX_Spot_Trading_Mechanics]]
