---
title: Cash and Carry Arbitrage
aliases:
- Cash-and-carry arbitrage
- Basis trade
- Trading the basis
- Spot-Futures Arbitrage
- Synthetic Futures Construction
type: mechanism
tags:
- trading-strategies
- arbitrage
- repo
- futures
- contango
- commodities
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens:
- "Alexander Düring"
- "Salih Neftci"
provenance:
- "Alexander Düring - Fixed Income Trading and Risk Management (2021)"
- "Salih Neftci - Principles of Financial Engineering"
thesis: Cash and Carry Arbitrage là chiến lược mua tài sản giao ngay (spot) và đồng
  thời bán khống hợp đồng tương lai (futures) để khóa lợi nhuận phi rủi ro từ chênh
  lệch giá. Düring nhấn mạnh vai trò của Repo Rate trong Fixed Income; Neftci nhấn
  mạnh cost of carry là trần giá Futures trong thị trường Contango hàng hóa — cả
  hai hội tụ ở cùng một logic: arbitrage tự điều chỉnh giá về cân bằng.
source_refs:
- file: Fixed_Income_Alexander_During_Ch29.md
  page: 16
- file: Neftci_Principles.md
  page: 219
created: '2026-04-13'
updated: '2026-05-04'
---

# Cash And Carry Arbitrage

## Định nghĩa tổng quát

Cash and Carry Arbitrage là chiến lược bắt lợi nhuận phi rủi ro từ chênh lệch giữa giá giao ngay (spot) và giá kỳ hạn (futures). Chiến lược xuất hiện ở cả thị trường **trái phiếu** (Düring) và thị trường **hàng hóa** (Neftci) — cùng logic arbitrage, khác nhau ở cơ chế thực thi.

---

## Düring: Fixed Income & Repo Market

> *[[Fixed_Income_Alexander_During_Ch29.md#page=16-17]]*

Ý tưởng liên kết Futures với rổ Trái phiếu nằm ở cash-and-carry arbitrage — giả định chênh lệch chi phí cầm cố nợ vay ([[Repurchase_Agreement|repo]]).

### Cơ chế thực hiện
1. Mua trái phiếu rẻ giao nhất (**CTD**) bằng tiền vay qua đêm theo Repo Rate.
2. Ngay lập tức **Short** Futures tương đương.
3. Mỗi ngày chịu chi phí lãi vay ròng (cost of carry).
4. Tại ngày đáo hạn Futures, giao đúng trái phiếu đó cho sàn.

Hoạt động gộp này gọi là **Mua/Bán Basis (Trading the basis)**.
- **Break-even:** khi [[Futures_Basis_And_Implied_Repo_Rate|net basis]] = 0.
- **Fair Value:** tính từ converted forward price của CTD.
- Lực mua mạnh đẩy CTD lên, Short Futures kéo $F$ xuống → [[Futures_Basis_And_Implied_Repo_Rate|implied repo rate]] (IRR) bám sát Repo Rate thị trường.

### Rủi ro: Term Repo Risk
Khi hợp đồng Repo vay dài hạn không khớp đúng ngày giao Futures, Trader bị đòi lại Trái phiếu đúng ngày phải giao → **fail to exchange** (thất hẹn thanh toán).

---

## Neftci: Commodity Futures & Cost of Carry

> *[[Neftci_Principles.md#page=219-221]]*

Trong hàng hóa, Cash and Carry đặt **trần giá Futures** tại thị trường Contango:

$$F_{t,0} \leq S_{t,0}(1+r) + \text{Costs} - \text{Convenience Yield}$$

Điều kiện kích hoạt arbitrage: $F > S(1+r) + q$

### Chuỗi thực hiện
1. Phát hiện Contango: $F_{t_0} > S_{t_0}(1+r) + \text{Storage} + \text{Insurance}$
2. Short Futures tại $F$
3. Vay tiền, mua Spot $S_{t_0}$
4. Thuê kho/tàu dầu lưu trữ hàng qua kỳ $(t_0, T)$
5. Giao hàng tại $T$, khóa lợi nhuận phi rủi ro

### Hệ quả tự điều chỉnh

```
[Cash and Carry] ───> [↑ Spot Demand] ───> [↑ Spot Price]
        │                                       │
        └────────────> [↓ Futures Price] <──────┘
                               │
                               v
                     [Narrowing Contango → Equilibrium]
```

### Ví dụ: JPMorgan & Siêu tàu Front Queen (2009)

Heating Oil rơi vào Contango cực mạnh — Spot $553/tấn, Futures tháng 8 $580/tấn. JPMorgan thuê siêu tàu *Front Queen* (273,000 tấn) làm kho nổi.

| Chi phí | Tính toán | ($M) |
|:---|:---|:---|
| Mua Spot | 273k tấn × $553 | 150.969 |
| Lãi vay (1%) | | 1.510 |
| Bảo hiểm (0.25%) | | 0.377 |
| Vận chuyển | Singapore → Europe | 1.600 |
| Lưu kho | $3.85/tấn | 1.051 |
| **TỔNG** | | **155.507** |

**Doanh thu:** $158.34M → **Lợi nhuận arbitrage: ~$2.833M**

### Điều kiện đứt gãy
- **Không thể lưu trữ:** Điện, dịch vụ — không áp dụng được.
- **Kho đầy 100%:** Chi phí $q$ → ∞, Futures thoát anchor Spot.
- **Counterparty Risk:** Sàn hoặc bên mua Futures vỡ nợ.

---

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch29.md#page=16-17]] — Cơ chế Cash and Carry trong Fixed Income qua Repo (Düring)
- [[Neftci_Principles.md#page=219-221]] — Cơ chế trong hàng hóa, pricing ceiling, case study JPMorgan (Neftci)

#
