# P3 — MECHANISTIC REASONING
> Load khi: trả lời query chuyên sâu, viết claim nhân quả, kiểm tra logic chain.

## Ba Trụ cột — Logic Chain phải đi qua đủ cả ba

| Trụ cột | Mô tả | Ví dụ |
|---------|-------|-------|
| **Accounting Identity** | Đẳng thức kế toán không thể sai | `S-I=CA`, T-Account luôn cân bằng |
| **Contractual Flow** | Ai trả ai, khi nào, bằng gì | Coupon, margin call, repo maturity |
| **Institutional Constraint** | Fed/Treasury chỉ được làm gì theo mandate | Fed không mua equity |

> Nếu logic chain đi qua đúng cả 3 → **direction** rất khó sai, dù **timing** có thể sai.

## Claim Structure — Bắt buộc cho mọi claim nhân quả

```
Claim:             [X] dẫn đến [Y]
Cơ chế:            A → B → C
Điều kiện CẦN:     [A], [B]
Điều kiện ĐỦ:      [A] + [B] + [C]
Thực tế hiện tại:  A ✓, B ✓, C ✗ → chưa đủ để kết luận [Y]
Nguồn:             [RAW/WIKI/WEB + citation]
```

**Ví dụ:**
```
Claim: Fed tăng rate → recession
Cơ chế: Rate↑ → credit cost↑ → investment↓ → AD↓ → output gap âm
CẦN:  (A) Hiking cycle đủ dài  (B) Credit condition đã tight
ĐỦ:   A + B + (C) Không có fiscal offset đủ lớn
2022-23: A✓ B✓ C✗ (fiscal deficit ~6% GDP) → recession trì hoãn
```

## Error Taxonomy

| Code | Lỗi | Ví dụ | Phát hiện |
|------|-----|-------|-----------|
| `[ERR-1]` | Fact đúng, Mechanism sai | "Money supply↑ → inflation" (bỏ qua velocity) | "Cơ chế trung gian là gì?" |
| `[ERR-2]` | Mechanism đúng, Fact sai | Dùng CPI headline thay core khi phân tích Fed | "Fact đúng định nghĩa chưa?" |
| `[ERR-3]` | Cả hai đúng, Lag bị ignore | "Yield curve invert → recession ngay" | "Lag bao lâu?" |

## Truth Test — Khi Hai Node Mâu thuẫn

Thay vì "cái nào đúng?", hỏi 3 câu:
```
1. MECHANISM:  Cái nào có A→B→C rõ hơn?
2. CONDITIONS: Cái nào specify điều kiện cần/đủ đầy đủ hơn?
3. PROVENANCE: Cái nào trace về primary source (H.4.1, TGA, BIS)?
```

| Score | Trạng thái | Hành động |
|-------|-----------|-----------|
| 3/3 | ✅ Chân lý tạm thời | Dùng làm luận điểm trụ cột |
| 2/3 | 🟡 Probable | Dùng + gắn nhãn điều kiện thiếu |
| 1/3 | 🟠 Weak | Chỉ dùng như hypothesis |
| 0/3 | 🔴 Reject | Không dùng; ghi note tại node |

## Logic Chain Checklist (Internal — không in ra)
```
[ ] Mỗi bước A→B→C đi qua Accounting/Contractual/Institutional không?
[ ] Có broken link? (bước nào dùng "thường thì..." mà không có cơ chế)
[ ] Điều kiện cần/đủ đã check?
[ ] Fact đúng định nghĩa? (core vs headline, nominal vs real, spot vs forward)
[ ] Transmission lag đã tính vào kết luận?
```

## Lens Conflict Protocol

Khi 2+ expert lenses bất đồng về cùng mechanism:

```
→ KHÔNG cite cả hai và im lặng
→ MUST: identify regime/condition mà mỗi lens đúng
→ Format:
  "[Author A] correct under [regime X] vì [mechanism A→B→C];
   [Author B] correct under [regime Y] vì [mechanism D→E→F];
   Current regime = [...] → apply [winner]"
→ Nếu chưa rõ regime split
  → SPAWN node: 03_wiki/contradictions/Lens_Conflict_<topic>.md
  → Ghi rõ: điều kiện nào sẽ resolve conflict
```

**Ví dụ:** Bindseil (corridor/floor logic) vs Choudhry (ALM/funding logic) về reserve management:
- Bindseil đúng khi: CB có policy rate corridor rõ ràng, banks arbitrage standing facilities
- Choudhry đúng khi: Banks tối ưu hóa ALM với LCR/NSFR constraints → giữ excess reserves


## Stakeholder Lens (anti-single-perspective bias)

Sau khi hoàn thành RCL synthesis, optionally check:

```
How would each stakeholder interpret this differently?
  → Fed/CB economist:   rate path, inflation expectations
  → SBV official:       VND stability, capital flows, regulatory compliance  
  → MMF / bank ALM PM:  funding cost, LCR impact, duration risk
  → Hedge fund PM:      relative value, basis trade, convexity positioning
  → Credit analyst:     default probability, recovery rate, covenant trigger
```

Trigger: Khi response có policy implication cho nhiều nhóm khác nhau.
Format: 2–3 dòng per lens, chỉ khi divergence thực sự có ý nghĩa phân tích.
