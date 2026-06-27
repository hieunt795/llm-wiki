---
title: Credit Ratings and Migration
aliases:
- Credit Rating
- Rating Migration
- Transition Matrix
- Markov Process in Finance
- Selective Default
- Xếp hạng tín nhiệm
type: definition
tags:
- credit-risk
- quantitative-finance
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch25.md
thesis: Credit ratings are ordinal measures of default probability that evolve through
  time according to a transition matrix, where the multi-period risk of a security
  is a non-linear function of its rating migration path.
source_refs:
- file: During_Fixed_Income_Ch25.md
  page: 264
- file: During_Fixed_Income_Ch25.md
  page: 266
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 501-510
  section: "Chapter 1.4: Credit fundamentals and ratings"
- file: During_Fixed_Income_Ch25.md
  page: 267
- file: During_Fixed_Income_Ch25.md
  page: 268
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Credit ratings provide a standardized, public opinion on the likelihood of full and timely payment of principal and interest. Alexander Düring bóc tách bản chất của hệ thống này: nó là một thang đo **thứ tự (ordinal)** chứ không phải **định lượng (cardinal)**. Một xếp hạng AAA có nghĩa là rủi ro thấp hơn AA, nhưng nó không chỉ ra chính xác một mức xác suất vỡ nợ cố định. Rủi ro thực sự nằm ở sự **Dịch chuyển (Migration)**—khả năng một trái phiếu bị hạ hạng trước khi nó thực sự sụp đổ. [[During_Fixed_Income_Ch25.md#page=264-266]]

## Mechanism: The Markov Transition Matrix

The evolution of ratings is modeled as a **Markov Process**—a stochastic process where the future state depends only on the current state, not the past history (no memory).

### 1. The 1-Year Matrix
Agencies (S&P, Moody's, Fitch) publish annual transition tables showing the probability of moving from one rating band to another (e.g., A to BBB, or A to Default). [[During_Fixed_Income_Ch25.md#page=267]]

### 2. Multi-Period Probability Paradox
A common error is to assume the 2-year default probability ($p_2$) is simply twice the 1-year probability ($2p_1$).
- **The Correct Logic:** One must sum the probabilities of defaulting in year 1 AND surviving year 1 but migrating to a different rating band, then defaulting from that new band in year 2.
- **Formula:** $p_{2,i,D} = p_{i,D} + (1 - p_{i,D}) \sum_{k} p_{i,k} p_{k,D}$
- **Inference:** Over extremely long horizons (50+ years), the initial rating becomes irrelevant for corporate issuers as they either default or reach a steady-state average (irrelevance of initial state). [[During_Fixed_Income_Ch25.md#page=267-269]]

## Strategic Implications: Institutional Conflict

### 1. Solicited vs. Unsolicited Ratings
- **Solicited:** Paid for by the issuer. Provides the agency with privileged access to internal data but creates a "he who pays the piper calls the tune" conflict of interest.
- **Unsolicited:** Performed by the agency independently. Common for developed sovereigns (who don't need to pay to attract investors). Some regulators insist on clear labeling to warn of potential data gaps. [[During_Fixed_Income_Ch25.md#page=265-266]]

### 2. Rating "Through the Cycle"
Ratings are meant to ignore temporary business cycle fluctuations. However, because cycles are not fully predictable, rating transitions still exhibit cyclical clusters, leading to correlated selling by investors bound by **Investment Grade** mandates. [[During_Fixed_Income_Ch25.md#page=267]]

## Evidence / Source Anchors

- Definition of credit ratings as ordinal rather than cardinal scales: [[During_Fixed_Income_Ch25.md#page=264]]
- Analysis of the Markov assumption in the Jarrow-Lando-Turnbull model: [[During_Fixed_Income_Ch25.md#page=268]]
- Mathematical proof of the multi-period default probability calculation: [[During_Fixed_Income_Ch25.md#page=267]]
- Contrast between 50-year risk evolution for Corporate vs. Sovereign issuers: [[During_Fixed_Income_Ch25.md#page=269]]
- Identification of "Selective Default" as a specific issuer-level rating state: [[During_Fixed_Income_Ch25.md#page=264]]

## Related

- [[Credit_Risk_Taxonomy]] — The events (Default/Insolvency) that ratings attempt to predict.
- [[Sovereign_Debt_Risk_Dynamics]] — Why sovereign ratings are rarely solicited but highly stable.
- [[Managed_Default_Vs_Liquidation]] — The resolution process for rated debt in distress.
- [[Securitization_And_Asset_Based_Finance_ABF]] — Where rating models famously failed during the 2008 crisis.
- [[Credit_Risk_Transfer_CRT]]
- [[Credit_Default_Swaps_CDS]]
