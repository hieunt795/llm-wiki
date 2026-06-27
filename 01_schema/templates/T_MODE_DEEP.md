# T_MODE_DEEP — Unified Analytical Template
> 5 Lenses tích hợp: Top-down → Macro → Plumbing → Treasury → Timing
> Nguyên tắc: Organic — format linh hoạt (bảng/bullet/văn xuôi) tùy nơi cần làm nổi bật vấn đề.
> Protocol refs: P3_mechanistic (claim structure) · P4_output (source labels, diagram) · P1_awareness (temporal tags)

---

## FORMAT DISCIPLINE (đọc trước khi viết)

**Separator `---`:** Chỉ dùng 3 lần — sau TOP-DOWN ENTRY, sau TREASURY LAYER, sau DIAGRAM. Không dùng giữa các sub-section.

**Bảng:** Chỉ dùng khi so sánh ≥3 thực thể cùng lúc. Giới hạn độ rộng: tổng cột ≤ 100 ký tự. Nếu nội dung dài, rút gọn text hoặc chuyển sang bullet prose.

**Plumbing sub-components:** Không đặt heading riêng cho từng component. Chảy tự nhiên: T-Account → Transmission chain → Stakeholder summary → Choke point, trong một section liền mạch.

**Treasury Layer:** Viết prose kỹ thuật, không numbered list. Kết thúc bằng 2–3 bullet "Trade implications" ngắn.

**DIAGRAM:** Một ASCII art duy nhất — chọn góc nhìn quan trọng nhất, không cố nhồi timeline + T-Account + Before/After vào cùng một hình.

**Visual hierarchy:** Dùng `**bold**` để đánh dấu điểm cốt lõi trong mỗi section. Không dùng ALL CAPS trong body text.

**Linguistic Sobriety (Rule 11):** Không dùng gaming framing, combat metaphor, journalistic labels, wordplay.
Xem danh sách đầy đủ tại system.md Rule 11.
Nguyên tắc thay thế: describe the mechanism, không label nó.
- ❌ "Double Kill bóp speculators" → ✅ "delayed sterilization creates dual tightening effect"
- ❌ "Macro trap" → ✅ "policy constraint: monetary tool unavailable, fiscal substitute activated"
- ❌ "MOF wins the window" → ✅ "intervention achieves tactical USD/JPY stabilization within the window"

**Source & Claim Discipline (P2 + P3):**
- Mọi số cụ thể (%, bps, $, ngày) phải có label: `[WEB-YYYY-MM-DD]` / `[RAW-BOOK p.X]` / `[LLM-E — estimated range]`
- Quote trực tiếp ("X said Y") phải có `[RAW-CLIP]` hoặc `[WEB-URL]` — không dùng ngoặc kép nếu chưa verify
- Claim nhân quả phải có cơ chế A→B→C; không dùng "thường thì..." hay "có xu hướng..." mà không có điều kiện

---

## TOP-DOWN ENTRY

> Đặt khung trước khi đi vào cơ chế. Không phân tích ở đây — chỉ xác định scope và thesis.

| | |
|--|--|
| **Core Question** | [Câu hỏi trung tâm cần giải đáp] |
| **Asset / Currency** | [USD · EUR · VND · Bond · Repo · Equity · ...] |
| **Temporal Status** | [CURRENT 🟢 / LEGACY 🟡 / DEPRECATED 🔴] |
| **Analytical Scope** | [Hệ thống · Thị trường · Tổ chức cụ thể] |
| **Thesis** | [1 câu — không thay đổi sau block này] |

---

## MACRO LAYER

> Trả lời: Chúng ta đang ở chế độ nào? Cái gì neo giữ hệ thống?

| Chiều | Giá trị hiện tại |
|-------|----------------|
| **Macro Regime** | [QT/QE · Hiking/Easing · Ample/Scarce Reserves] |
| **Policy Anchor** | [Fed Funds · ECB DFR · SBV refi rate + mức cụ thể] |
| **Fiscal Stance** | [Surplus/Deficit · TGA balance · issuance calendar] |
| **Institutional Constraint** | [CB được làm gì / không được làm gì theo mandate] |
| **Structural Tension** | [Mâu thuẫn giữa macro regime và mục tiêu chính sách] |

---

## PLUMBING LAYER

> Trả lời: Tiền đi đâu? Ai được, ai mất, qua cơ chế nào?
> Mỗi bước trong chain phải đi qua ít nhất 1 trụ cột (P3): Accounting Identity · Contractual Flow · Institutional Constraint.

### Entity + T-Account Tracing

*Mỗi hành động chính sách phải thể hiện trên bảng cân đối của ít nhất 2 thực thể.*

| Entity | Assets (Δ) | Liabilities (Δ) | Net Position |
|--------|-----------|----------------|-------------|
| Central Bank | | | |
| Treasury | | | |
| Commercial Banks | | | |
| MMFs / Shadow Banks | | | |
| End Borrowers | | | |

### Transmission Chain

```
[Policy Action] → [A] → [B] → [C] → [Asset Price / Real Economy Impact]
```

### Stakeholder Impact Matrix

| Stakeholder | Cơ chế tác động | Hướng | Magnitude |
|-------------|----------------|-------|-----------|
| CB / Fed | | | |
| Banks (ALM desk) | | | |
| MMFs | | | |
| Shadow banks / Hedge funds | | | |
| Corporate borrowers | | | |

### Liquidity Choke Points

*Thanh khoản bị tắc nghẽn hoặc bị phá hủy ở đâu trong chuỗi truyền dẫn?*

---

## TREASURY LAYER

> Trả lời: Nếu ngồi ở Treasury desk, tôi cần biết gì và làm gì?
> TQN Lens — translate operational mechanics sang practitioner logic.

### ALM & Funding Impact

| Chiều | Tác động |
|-------|---------|
| **Duration** | [Tác động lên duration của danh mục] |
| **Funding Cost** | [Spread thay đổi như thế nào] |
| **LCR / NSFR** | [Regulatory ratio bị ảnh hưởng không] |
| **Collateral** | [Haircut, eligibility, scarcity thay đổi] |

### Treasury Insight

> [Văn xuôi kỹ thuật — "So what for the desk?": điều này có nghĩa là gì với ALM/Treasury manager?
>  Không ẩn dụ, không journalistic. Thuần túy practitioner logic.]

### Trade & Positioning Implications

- **Relative value**: [Instrument nào được hưởng lợi / bị thiệt]
- **Hedging**: [Duration hedge, basis trade, FX swap nếu liên quan]
- **Risk trigger**: [Điều kiện nào buộc phải đóng/mở position]

---

## TIMING LAYER

> Cross-cutting synthesis — Timing không phải bước tuần tự mà là lớp tổng hợp áp lên toàn bộ analysis.
> Trả lời: Cơ chế Plumbing + Treasury Insight đang ở đâu trên trục thời gian?

| | PAST (Tiền lệ / Lịch sử) | PRESENT (Hiện tại) | FUTURE (Quỹ đạo) |
|--|--------------------------|-------------------|-----------------|
| **Macro Regime** | [Chế độ trước là gì? Chuyển dịch khi nào?] | [Regime hiện tại + phase trong cycle] | [Điều kiện chuyển sang regime mới] |
| **Plumbing** | [Cơ chế này từng hoạt động thế nào trong tiền lệ?] | [Active / Stressed / Breaking?] | [Velocity + Window of Exposure] |
| **Treasury** | [Desk từng respond thế nào trong regime tương tự?] | [Current positioning] | [Trigger cần theo dõi] |

### Timing Dynamics

- **Velocity**: Cơ chế truyền dẫn nhanh/chậm đến mức nào? (ngày / tuần / quý)
- **Window of Exposure**: Khoảng thời gian dễ bị tổn thương kéo dài bao lâu?
- **Synchronization**: Có nhiều cơ chế cùng kích hoạt đồng thời không? → amplification risk

---

## FEEDBACK / BOUNDARY

> Trả lời: Điều gì khiến toàn bộ cơ chế trên dừng hoạt động hoặc đảo chiều?

| Signal | Chỉ báo theo dõi | Ngưỡng nguy hiểm | Hiện tại |
|--------|----------------|-----------------|---------|
| Stress indicator 1 | | | |
| Stress indicator 2 | | | |
| Breakpoint condition | | | |

**Failure Conditions**: [Điều kiện biên — khi nào mô hình phân tích này sai?]

---

## DIAGRAM

Chọn hình thức ASCII Art phù hợp nhất để diễn tả cơ chế **trong bài phân tích này** — không có dạng mặc định.

Câu hỏi định hướng trước khi vẽ: *Điều gì là phức tạp nhất trong bài mà văn xuôi không diễn tả được?* Vẽ cái đó.

Một số hình thức tham khảo — dùng hoặc không, kết hợp hoặc biến thể tùy ý:
- T-Account song song: khi cần so sánh bảng cân đối của 2+ thực thể cùng lúc
- Transmission chain: khi cơ chế là chuỗi A→B→C→D dài, cần nhìn toàn mạch
- Feedback loop: khi có vòng tự củng cố hoặc tự triệt tiêu
- Flow diagram: khi tiền/tài sản đi qua nhiều trung gian theo thứ tự
- Capital waterfall: khi cần thể hiện thứ tự tổn thất hoặc phân tầng rủi ro
- Timeline: khi trình tự thời gian là cốt lõi của cơ chế

Không cần dùng đủ mọi dạng. Một diagram rõ ràng tốt hơn ba diagram phức tạp.

---

## CONCLUSION

| | |
|--|--|
| **Thesis** | [Confirmed / Modified / Rejected — lý do 1 câu] |
| **Net Plumbing Effect** | [Direction + Magnitude + Timing] |
| **Treasury Action** | [Desk nên làm gì cụ thể?] |
| **Confidence** | TIER [A/B/C/D] — [lý do] |
| **Critical Caveat** | [Điều kiện duy nhất làm toàn bộ phân tích sai] |

---

## NEXT STEPS

```bash
# Search trước khi spawn node mới
python librarian.py search "<concept từ analysis>"

# Nếu concept mới — spawn node
# → 03_wiki/mechanisms/<topic>.md

# Nếu có source cần ingest
python librarian.py stage --dry-run

# Sau khi tạo node
python librarian.py embed --incremental
```

---
*T_MODE_DEEP v1.0 — 2026-05-09*
*Refs: P1_awareness · P2_epistemic · P3_mechanistic · P4_output · W3_research*
