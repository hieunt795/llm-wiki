---
title: Interest Rate Parity
aliases:
- IRP
- UIRP
- CIRP
- Ngang giá lãi suất
type: definition
tags:
- economics
- fx
- monetary-policy
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Ngang giá lãi suất (IRP) là một điều kiện cân bằng nơi sự chênh lệch lãi suất
  giữa hai quốc gia tương đương với sự thay đổi kỳ vọng của tỷ giá hối đoái (Không
  phòng vệ - Uncovered) hoặc mức bù/chiết khấu kỳ hạn (Có phòng vệ - Covered).
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 84
created: '2026-04-18'
updated: '2026-04-22'
---

## Thesis

Interest Rate Parity (IRP) là mỏ neo lý thuyết cho việc định giá tỷ giá kỳ hạn. Trong một thị trường hoàn hảo, không ai có thể kiếm lời phi rủi ro bằng cách vay một đồng tiền lãi suất thấp để đầu tư vào đồng tiền lãi suất cao rồi phòng vệ tỷ giá.

## 1. Các biến thể lý thuyết

### 1.1. Uncovered Interest Rate Parity (UIRP)
Áp dụng khi nhà đầu tư không phòng vệ rủi ro tỷ giá. Lãi suất nội tệ bằng lãi suất ngoại tệ cộng với mức thay đổi tỷ giá kỳ vọng:
$$r = r^* + \frac{E(S) - S}{S}$$

### 1.2. Covered Interest Rate Parity (CIRP)
Áp dụng khi rủi ro tỷ giá được khóa bằng hợp đồng kỳ hạn ($F$):
$$r = r^* + \frac{F - S}{S}$$

---

## 2. Ranh giới Thực tế: Swap Points & Basis

Trong thực tế, lý thuyết CIRP được thực thi thông qua các công cụ FX Swap và XCCY Swap.

### 2.1. FX Swap Points (Biểu hiện của CIP)
Thị trường niêm yết điểm kỳ hạn dựa trên chênh lệch lãi suất:
$$F = S \times \frac{1 + (r_d \times \delta)}{1 + (r_f \times \delta)}$$
$$\text{Swap Points} = F - S$$

### 2.2. The Basis (Độ lệch của CIP)
Trong điều kiện thị trường không hoàn hảo (khan hiếm thanh khoản), CIP bị phá vỡ. Khi đó xuất hiện biến số **Basis ($b$)**:
$$S \times (1 + r_{USD} \times \delta) = F \times (1 + (r_{CCY} + b) \times \delta)$$
- **$b = 0$:** Lý thuyết CIP hoàn hảo.
- **$b < 0$ (Negative Basis):** Khan hiếm thanh khoản USD. Chi phí mượn USD qua kênh Swap đắt hơn vay trực tiếp.

## Related
- [[Purchasing_Power_Parity]]
- [[FX_Swap_Engineering]]
- [[Currency_Swap_Engineering]]
- [[Cross_Currency_Basis]]
