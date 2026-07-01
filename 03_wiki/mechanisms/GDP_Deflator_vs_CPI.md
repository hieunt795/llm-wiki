---
title: GDP Deflator vs CPI
aliases:
  - GDP Deflator
  - CPI vs GDP Deflator
  - Laspeyres vs Paasche Price Index
  - Consumer Price Index
  - Paasche Index
  - Laspeyres Index
  - Price Index Formulas
type: mechanism
tags:
  - macro
  - inflation
  - national-accounts
  - price-measurement
  - statistics
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Ouanes | Thakur | IMF"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.2"
thesis: The GDP deflator (Paasche, current-period weights) and the CPI (Laspeyres, base-period weights) diverge in three dimensions — coverage (all domestic output vs. consumer basket), treatment of imports (excluded from deflator, included in CPI), and weighting methodology (fixed vs. flexible) — with the Laspeyres index systematically overstating inflation by ignoring substitution effects and the Paasche index understating it.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 22
created: "2026-07-01"
updated: "2026-07-01"
---

# [[GDP_Deflator_vs_CPI]]

## Thesis

[RAW] A commonly used measure of inflation, the consumer price index (CPI) measures the prices of a representative basket of goods and services purchased by the average consumer. There are three main differences between the GDP deflator and the CPI.

## 1. Three Dimensions of Divergence

### Dimension 1: Coverage of Goods and Services

[RAW] The CPI takes into account only a subset of all goods and services in the economy — those bought by consumers. An increase in the price of goods and services bought by firms or the government (such as machinery) shows up in the GDP deflator but not in the CPI.

### Dimension 2: Treatment of Imports

[RAW] The GDP deflator includes only domestically produced goods. Imported final goods are not covered, and therefore a change in the prices of imported goods does not have a direct impact on the GDP deflator in the short run. The CPI, however, is affected by changes in the prices of imported goods to the extent that those goods are part of the CPI basket.

### Dimension 3: Weighting Methodology

[RAW] The CPI is based on a set basket of goods and services assigned **fixed weights** (Laspeyres price index). The GDP deflator basket changes over time as the composition of GDP changes (Paasche price index). The CPI uses base-year quantities as weights; the GDP deflator uses current-year quantities.

**Example:** If a drought destroys the corn crop:
- Corn output falls to zero; corn price rises sharply.
- Corn drops out of the GDP deflator (not produced).
- Corn remains in the CPI, contributing to a substantial rise in the CPI.

## 2. Price Index Formulas

[RAW] Formal notation:

**Laspeyres Index (CPI / WPI):**
$$\text{CPI} = \frac{\sum p_1^i q_0^i}{\sum p_0^i q_0^i} \times 100$$

where $q_0^i$ = base-year quantities, $p_1^i$ = current prices, $p_0^i$ = base-year prices.

**Paasche Index (GDP Deflator):**
$$\text{GDP Deflator} = \frac{\sum p_1^i q_1^i}{\sum p_0^i q_1^i} \times 100 = \frac{\text{GDP at current prices}}{\text{GDP at base-year prices}} \times 100$$

The two formulas differ only in whether base-year quantities ($q_0^i$, Laspeyres) or current-year quantities ($q_1^i$, Paasche) appear in both numerator and denominator.

## 3. Systematic Biases

[RAW] The difference between the two indexes is not large if inflation is low and stable, but can be substantial in the presence of large relative price changes and movements in import prices.

| Index | Bias direction | Mechanism |
|---|---|---|
| Laspeyres (CPI, WPI, PPI) | **Overstates** inflation | Ignores substitution effects — consumers shift away from relatively more expensive goods, but fixed-weight index assumes unchanged consumption basket |
| Paasche (GDP Deflator) | **Understates** inflation | Uses current-period weights which overrepresent goods whose relative price has fallen (hence quantities purchased increased) |

**Practical implication:** In transition economies with high inflation and large relative price changes, the CPI may significantly overstate the true cost-of-living increase.

## 4. Special Case: Transition Economies

[RAW] In transition economies experiencing high inflation, a third index (the **Sauerbeck index**) is sometimes used. Although it uses base-period weights like the Laspeyres index, it compares current prices with those in the previous month (not a fixed base year). This provides a more timely measure during rapid price change.

[RAW] Because of rapid changes in production and consumption patterns and the lack of reliable price indicators in transition economies, it is often preferable to derive real GDP data using **volume or quantity indicators** rather than using a GDP deflator to deflate nominal GDP.

## 5. Underlying vs. Measured Inflation

[RAW] An important distinction must be made between:
- **Measured inflation** — total recorded change in CPI or deflator.
- **Underlying (core) inflation** — basic change in the overall price level, abstracting from unusual one-time increases caused by administered price adjustments, excise tax changes, or discrete exchange rate devaluations.

[RAW] Especially in transition economies, analysts should focus on the underlying rate of inflation rather than the measured rate because structural changes and reforms inevitably result in discrete adjustments in many administered prices.

## 6. WPI and PPI

[RAW] The wholesale price index (WPI) and producer price index (PPI) measure prices at the wholesale and producer levels, respectively. Like the CPI, both use fixed-weight (Laspeyres) methodology and therefore tend to overstate inflation.

## 7. Treasury Insight

[LLM] For macro practitioners, the CPI vs GDP deflator divergence matters most in three contexts:

1. **BOP/terms of trade analysis** — the deflator excludes import prices while CPI includes them, so divergence between the two signals that imported inflation is transmitting into consumer prices even when domestic production costs are stable.

2. **Real GDP construction** — using the wrong deflator inflates or deflates real growth estimates, particularly significant in transition economies where the pre-reform price structure was heavily distorted. Volume-based methods sidestep this problem.

3. **Wage negotiation and incomes policy** — CPI overstatement due to Laspeyres bias means that full CPI indexation of wages builds excess inflation into wage contracts. Partial forward-looking indexation (using projected rather than past inflation) is theoretically superior. See [[Incomes_Policy_Wage_Controls]].
