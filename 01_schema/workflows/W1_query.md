# W1 — QUERY PROTOCOL (IF-ELSE v4.1)
> Load khi: nhận query phức tạp cần tìm kiếm có cấu trúc.
> Mỗi nhánh IF-ELSE map sang một **Response Mode** trong system.md BLOCK 2.

---

## Giai đoạn 0 — CURRENCY GATE (chạy ĐẦU TIÊN, trước mọi thứ)

> **Mục đích:** Phát hiện breaking news / recent update trước khi synthesis.
> Agent dùng built-in web search — KHÔNG cần script Python.

### STEP 0A — Xác định node type cần check

```
Không trigger (skip Currency Gate) nếu:
  • half_life_years ≥ 10 (mechanisms, pure theory)
  • Query là định nghĩa khái niệm bất biến ("repo là gì", "duration formula")

Trigger bắt buộc nếu thuộc bất kỳ loại nào:
  • Monetary policy / central bank decisions
  • Regulatory thresholds (CAR, LDR, Basel, Thông tư)
  • Market data (yields, spreads, tỷ giá, CDS)
  • Macro indicators (CPI, GDP, trade balance, FX reserves)
  • Private credit / shadow banking
  • Query chứa: "hiện tại", "mới nhất", "2025", "2026", "gần đây",
               "latest", "current", "recent", "update"
```

### STEP 0B — Construct web search query

```
Agent tự xây query dựa trên nguyên tắc — KHÔNG dùng template cứng:
  1. Giữ entity/concept cốt lõi từ query gốc
  2. Thêm temporal context (năm/tháng hiện tại)
  3. Thêm institutional scope nếu relevant (Vietnam, SBV, NHNN, IMF, BIS...)
  4. Focus vào phần most likely to change của topic đó

half_life_years chỉ dùng để quyết định CÓ trigger không:
  ≥ 10  →  skip (mechanism thuần túy, không thay đổi)
  < 10  →  trigger, agent tự construct query phù hợp
```

### STEP 0C — Validate kết quả web search

```
SAU KHI có kết quả web:
  → Kiểm tra ngày publish của từng source
  → Nếu source cũ hơn 6 tháng → DISCARD, không tính là "currently"
  → Chỉ giữ lại sources trong 6 tháng gần nhất

ĐÁNH GIÁ:
  IF (có source mới hơn wiki knowledge, trong 6 tháng)
    → SET FLAG: CURRENTLY_ACTIVE = true
    → Ghi nhớ snippets + sources để inject vào response
    → IF news MÂU THUẪN wiki node → SET FLAG: STALE_SIGNAL = true
  ELSE
    → SET FLAG: CURRENTLY_ACTIVE = false → tiếp tục bình thường
```

---

## Giai đoạn 0.5 — PREMISE AUDIT (sau Currency Gate, trước Mode Select)

```
Extract premises từ user query → kiểm tra từng cái:

  IF premise factually correct (đã verify qua Currency Gate hoặc wiki)
    → proceed

  ELSE IF premise outdated / wrong
    → Pivot: "Premise của bạn cần update — actually [X] happened on [Y]"
    → KHÔNG build response trên premise sai ("castle on sand")

  ELSE IF premise ambiguous
    → 1 câu clarify trước khi proceed

Scope của Premise Audit:
  ✓ Factual claims: số liệu, trạng thái policy, regulatory threshold
  ✓ Causal assumptions: "vì A nên B" — check mechanism
  ✗ Conceptual/definitional premises → không audit (user có thể dùng khác định nghĩa)
```

---

## Giai đoạn 1 — ĐỊNH VỊ + MODE SELECT

```
IF (câu hỏi thematic/landscape: "tất cả X", "landscape Y", "map domain Z")
  → MODE SCAN
  → python librarian.py wisdom "<tag>" --no-llm
  → Đọc Hub Map + Tension Pairs → annotate pattern + gaps

ELSE IF (câu hỏi cơ chế / transmission / "tại sao" / "vận hành thế nào")
  → MODE DEEP (RCL skeleton)
  → Chuyển sang Giai đoạn 2
  → Apply: Top-Down Entry → Macro Layer → Plumbing Layer → Treasury Layer → Timing Layer → Feedback/Boundary
  → Template: 01_schema/templates/T_MODE_DEEP.md

ELSE IF (định nghĩa / số liệu cụ thể / "X là gì" / regulatory threshold)
  → MODE FLASH
  → python librarian.py search "<query>"
  → BLUF 1 câu + Evidence 2-3 dòng + Number anchor

ELSE
  → MODE DEEP (default)
  → Chuyển sang Giai đoạn 2
```

---

## Giai đoạn 2 — SOI CHI TIẾT (Microscope Mode)
> Chỉ chạy cho MODE DEEP. MODE FLASH dùng wiki_search nhanh. MODE SCAN dùng wisdom.

```
IF (cần định nghĩa / thesis nhanh)
  → python librarian.py search "<query>"
ELSE IF (cần cơ chế / context window từ RAW)
  → python librarian.py search "<query>" --deep
ELSE IF (wiki coverage thin / confidence thấp)
  → python librarian.py deepdive "<query>"
```

```
IF (node tồn tại, confidence ≥ 3)
  → Đọc node → trích source_refs → grep [RAW] → apply RCL skeleton
ELSE IF (node thin: confidence ≤ 2 OR [LLM] > 0 OR no source_refs)
  → python librarian.py deepdive "<query>" → đọc draft → apply RCL từ RAW evidence
ELSE
  → TYPE 2: SPAWN node mới theo schema.md
```

---

## Giai đoạn 3 — SYNTHESIS WITH CURRENTLY LAYER

```
IF (CURRENTLY_ACTIVE = true)
  → Cấu trúc response 3 lớp:

  ━━━ [WIKI LAYER] ━━━
  Kiến thức cấu trúc từ wiki nodes — [RAW] citations
  Dùng RCL / FLASH / SCAN tùy mode

  ━━━ [CURRENTLY — YYYY-MM-DD] ━━━
  [WEB: tên nguồn] → tóm tắt điều gì thay đổi / xác nhận / mâu thuẫn

  ━━━ [SYNTHESIS] ━━━
  "Theo [[Wiki_Node]], cơ chế X... Tuy nhiên, cập nhật [date]
   cho thấy Y đã thay đổi vì Z → implication cho A, B, C."

  IF (STALE_SIGNAL = true)
    → Thêm cuối response:
      ⚠️ [STALE SIGNAL] [[Node_Name]] có thể outdated.
      [INGEST CANDIDATE] url — lý do cần update wiki

ELSE (CURRENTLY_ACTIVE = false)
  → Response bình thường theo mode
  → Không có CURRENTLY section
```

**Epistemic hierarchy:**
```
[RAW] > [WIKI] > [WEB-CURRENT] > [LLM]
Web current bổ sung lớp thời gian thực — KHÔNG thay thế RAW.
```

---

## Giai đoạn 4 — WEB SEARCH FALLBACK (Telescope Mode)
> Chỉ kích hoạt khi wiki thin — khác với Currency Gate ở Giai đoạn 0.

```
TRIGGER (ít nhất 1):
  (A) deepdive: wiki top-3 confidence ≤ 2 VÀ hybrid_search không có RAW
  (B) User explicit: "tìm web", "tìm thêm"

NẾU TRIGGER:
  TIER 1 — EPHEMERAL: số liệu tức thời → [WEB-YYYY-MM-DD: nguồn], không persist
  TIER 2 — INGEST-FLAGGED: framework/regulation mới → [INGEST CANDIDATE] cuối response
```

---

## Node Operations

| Type | Khi nào | Hành động |
|------|---------|-----------|
| TYPE 1: UPDATE | Node tồn tại, có thêm thông tin mới | Thêm section mới, giữ nội dung cũ |
| TYPE 2: SPAWN | Khái niệm chưa có node | Tạo node mới theo schema.md |
| TYPE 3: BRIDGE | Hai node liên quan chưa linked | Thêm wikilink 2 chiều |
| TYPE 4: CONTRADICTION | Phát hiện mâu thuẫn | SPAWN node tại `contradictions/` |
