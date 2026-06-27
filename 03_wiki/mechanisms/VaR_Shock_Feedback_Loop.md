---
title: VaR Shock Feedback Loop
aliases:
- VaR Shock
- JGB VaR Shock 2003
- Stop-Loss Cascade
- One-Way Market Feedback Loop
type: mechanism
tags:
- fixed-income
- market-risk
- japan
- quantitative-easing
- VaR
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: 'A market where prolonged central bank intervention suppresses volatility
  and directionality generates a structural fragility: short sellers, who would normally
  provide natural support by covering positions during a sell-off, are progressively
  eliminated because they sustain losses in a persistently'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
---

## Thesis

A market where prolonged central bank intervention suppresses volatility and directionality generates a structural fragility: short sellers, who would normally provide natural support by covering positions during a sell-off, are progressively eliminated because they sustain losses in a persistently trending market. The resulting one-way positioning creates a market with no stabilising buyers when the trend reverses — making a forced sell-off self-amplifying.

## Mechanism

### Phase 1: Accumulation of Fragility (Years)

1. Central bank suppresses yields and volatility through extended monetary easing (QE, yield management)
2. Declining volatility reduces VaR charges → higher leverage becomes optimal for a given risk budget
3. All participants become uniformly long; short sellers sustain repeated losses → exit the market
4. Market-maker balance sheets shrink as volatility trading becomes unprofitable → reduced absorption capacity
5. The market superficially appears stable but has become structurally brittle

### Phase 2: The Shock (Days)

1. An external shock reverses the price trend (e.g., foreign central bank signals, economic data)
2. Uniformly long positions begin losing value
3. VaR limits are breached simultaneously across participants → forced stop-loss selling triggered

### Phase 3: The Feedback Loop (Weeks)

1. Stop-loss selling depresses prices further
2. Further price decline triggers additional VaR breaches at other institutions
3. Market makers, with depleted balance sheets, cannot absorb the flow (no buyers)
4. **Critical absence:** No short sellers exist to cover their positions (natural buyers in a declining market), so there is no mean-reverting force
5. Positive feedback: price fall → more VaR breaches → more selling → further price fall

### Second-Wave Mechanism

In the JGB 2003 episode, the initial wave (June 2003) triggered by US yield backup was followed by a **second wave** in August 2003. This occurred because:
- The first wave did not clear all stressed positions
- Remaining long positions with slightly higher VaR thresholds were eventually breached as yields stayed elevated
- The delay between waves reflects the sequential exhaustion of remaining stability buffers in different institutions

### Historical case: JGB VaR Shock, Summer 2003

**Context:** During BoJ's first QE programme (2001–2006), Japanese yields had declined for several years. Short sellers had been progressively weeded out.

**Trigger:** US bond yields backed up substantially on apparent signals of a Fed policy change. JGB yields rapidly increased from June 2003 onward.

**Mechanism in practice:**
- Existing long positions at dealers came under VaR pressure simultaneously
- Stop-loss selling created a positive feedback loop
- First wave (June 2003): initial spike
- Second wave (August 2003): continuation as remaining long positions were similarly forced
- The episode occurred *during* BoJ QE (not after), demonstrating that QE does not prevent VaR shocks; it creates the conditions for them

**Contrast with 2007/2008:**
A second municipal stress episode in Japan around year-end 2007 — after excess reserves had stabilised — was significantly more limited and localised. This suggests that QE liquidity removal (2006) and then stabilisation created a more resilient base of value investors willing to pick up cheap assets, compared to the 2003 episode during peak QE fragility.

### Boundaries / Conditions

- Requires: (1) extended one-directional price trend, (2) capacity for leverage, (3) large institutional participation with VaR-based risk management, (4) some external market linked to the domestic market that can transmit shocks (FX, global yield spillover)
- **Does not require:** central bank withdrawal of liquidity. The 2003 VaR shock occurred *during* QE, not after.
- Exit strategies from QE must manage this risk: rapid liquidity withdrawal can destroy value investors' confidence in abundant funding, amplifying credit spread widening. Extended exit timelines (e.g., BoJ 2006: faster withdrawal than injection) can mitigate but not eliminate this risk.
- More relevant for markets with: (a) low natural short-seller presence, (b) concentrated institutional positioning, (c) limited market depth

## Evidence / Source Anchors

- JGB VaR Shock 2003 (June–August, two waves): [[Fixed_Income_Alexander_During_Ch09.md#page=17]]
- Phase: "traders who would take active short positions had gradually been weeded out": [[Fixed_Income_Alexander_During_Ch09.md#page=17]]
- Stop-loss selling, positive feedback loop, second wave August 2003: [[Fixed_Income_Alexander_During_Ch09.md#page=17]]
- Contrast: 2007/2008 second municipal episode was more limited: [[Fixed_Income_Alexander_During_Ch09.md#page=17]]
- End of BoJ QE 2006: yield increase from ~1.5% to 2%, Yubari shock June 20 2006: [[Fixed_Income_Alexander_During_Ch09.md#page=17]]

## Related

- [[BoJ_QE_2013_Case_Study]] — 2013 episode echoes 2003 VaR dynamics
- [[QE_Liquidity_Distortion]] — parent: QE suppresses market volatility structurally
- [[Quantitative_Easing]] — policy context for the 2001–2006 and 2013+ BoJ programmes
- [[QE_Empirical_Evidence]] — broader QE empirical record
- [[Negative_Interest_Rate_Mechanics]] — next policy step after QE in Japan (2016)













---
# [[VaR_Shock_Feedback_Loop]]

## Mechanism

Điều rùng rợn của một chu kỳ êm ả lặp đi lặp lại (do Trung ương ghim giá ổn định) là các công cụ Quản trị rủi ro ([[Role_Of_Market_Volatility]]) bị thui chột. **VaR Shock (Cú sốc VaR)** là minh hoạ đẫm máu cho lý thuyết Minsky. [extracted] [[Fixed_Income_Alexander_During_Ch10.md#page=16]]

### Đồ thị thời gian
1. Trong nhiều năm điệp khúc giảm lợi suất, các nhà đầu cơ Short (bán khống) thua lỗ và bị thanh trừng sạch sẽ khỏi thị trường. Toàn bộ người chơi đều đang Long (ôm hàng) với mức đòn bẩy khổng lồ (bởi vì volatility đang thấp, Value-at-Risk cho phép vay bão táp). [extracted] [[Fixed_Income_Alexander_During_Ch10.md#page=16]]
2. Bất ngờ, một cú shock ngược hướng vĩ mô ập đến (Ví dụ mùa hè 2003, lợi suất Mỹ và Nhật bung mạnh do Fed úp mở đổi giọng).
3. Những ai đang Long bắt buộc phải dừng lỗ ngay tắp lự ([[Trading_Strategy_And_Principles|stop-loss]]) theo luật **VaR limits**.
4. **Tuyệt cảnh:** Thị trường không còn bất kỳ Short-seller nào (những người vốn dĩ sẽ "mua đóng lệnh" - cover shorts để đỡ giá rơi). Lệnh bán tháo giẫm đạp vào hư không, đục lủng thanh khoản, tạo ra Feedback Loop đè giá rớt tự do khiến đợt VaR call thứ hai bị vỡ. [extracted] [[Fixed_Income_Alexander_During_Ch10.md#page=16-17]]

Cú sốc VaR 2003 ở thị trường Nhật JGB chính là bằng chứng đanh thép chối từ khái niệm bình yên cưỡng bức của trung ương.

### Nguồn

- [[Fixed_Income_Alexander_During_Ch10.md#page=16-17]] — Cú sốc VaR Nhật bản 2003, positive feedback loop.
