---
type: mechanism
trigger: "Sự tồn tại của coin với giá trị kim loại nội tại + chi phí đúc + seigniorage"
output: "Corridor giá trị mà coin có thể giao dịch"
constraints: ["Coin phải có thể melted hoặc minted", "Seigniorage do sovereign kiểm soát"]
sources: ["Fixed Income - Alexander During-3.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 2
---

# Coin Value Corridor

## Cơ chế

Giá trị $V$ của một đồng tiền xu (coin) bị ràng buộc trong một **corridor** xác định bởi: [extracted] [[Fixed Income - Alexander During-3.pdf#page=4]]

$$V_i - V_m \leq V \leq V_i + V_M + S$$

Trong đó:
- $V_i$ = Giá trị kim loại nội tại (inherent metal value)
- $V_m$ = Chi phí nấu chảy (melting cost)
- $V_M$ = Chi phí đúc (minting cost)
- $S$ = [[Seigniorage]]

### Arbitrage mechanism

- Nếu coin **giao dịch dưới** cận dưới ($V_i - V_m$): thương lái kim loại phế liệu sẽ **nấu chảy** coin → thu lợi
- Nếu coin **giao dịch trên** cận trên ($V_i + V_M + S$): sẽ hấp dẫn để **đúc tiền mới** từ kim loại

[extracted] [[Fixed Income - Alexander During-3.pdf#page=4-5]]

### Kỹ thuật phá corridor (qua debasement)

- **Sovereign:** Cố tình đưa coin độ tinh khiết thấp hơn → **debasement** → thường dẫn đến inflation
- **Private forgers:** Clipping (cắt rìa coin), giảm trọng lượng coin so với mệnh giá
- **Phòng thủ:** Sir Isaac Newton phát minh **rolling coins** (cạnh có rãnh) để chống clipping

[extracted] [[Fixed Income - Alexander During-3.pdf#page=5]]

## Điều kiện

- Coin phải có thể nấu chảy thành kim loại và đúc lại
- Seigniorage phải do sovereign kiểm soát
- Equation (2.1) trong sách gốc

## Ví dụ số

Xem Equation 2.1 trong sách. [extracted] [[Fixed Income - Alexander During-3.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-3.pdf#page=4]] — Equation 2.1 + arbitrage
- [[Fixed Income - Alexander During-3.pdf#page=5]] — Debasement, clipping, Newton
