# W5 — SECONDARY SOURCE INGEST
> Load khi: ingest Clipping, Deep-research LLM output, hoặc source không rõ nguồn gốc.
> Khác W2: có thêm **Adversarial Audit** — kiểm tra xung đột với books trước khi merge.

---

## Source Labels trong workflow này

| Label | Mô tả | Trust |
|-------|-------|-------|
| `[RAW-CLIP]` | Clipping từ web: Substack, financial press, independent analyst | ⭐⭐⭐ |
| `[RAW-DR-LLM]` | Deep-research output từ Gemini/ChatGPT (LLM synthesis) | ⭐⭐ |
| `[RAW-OPINION]` | Blog, op-ed, commentary không có citations | ⭐⭐ |

> Xem P2_epistemic.md để biết đầy đủ quy tắc confidence increment.

---

## Phase 0-T — INBOX TRIAGE (chỉ dùng khi file từ Inbox/)

> Trigger: User nói "Triage Inbox", "Phân loại Inbox", hoặc file source nằm trong `02_sources/Inbox/`.

**Với mỗi file trong Inbox/, thực hiện:**

```
STEP 1 — Đọc frontmatter + 50 dòng đầu của file

STEP 2 — Xác định label theo checklist:
  [ ] Có `source:` URL không?
  [ ] Có `author:` cụ thể không?
  [ ] Nội dung có citations/footnotes không?
  [ ] Style viết: prose có luận điểm hay tổng hợp nhiều nguồn?
  [ ] Published date có không?

STEP 3 — Gán label đề xuất:
  Sách / textbook rõ ràng        → [RAW-BOOK]     → books/
  CB, IMF, BIS official doc      → [RAW-OFFICIAL] → official_reports/
  Working paper / journal        → [RAW-ACADEMIC] → academic/
  Web article, Substack, press   → [RAW-CLIP]     → Clipping/
  LLM synthesis (no clear author)→ [RAW-DR-LLM]  → deep-research/
  Blog / op-ed / no citation     → [RAW-OPINION]  → Clipping/
  Không xác định được            → [UNVERIFIED]   → giữ ở Inbox

STEP 4 — Báo cáo cho user:
  Format: "File [X]: đề xuất [LABEL] → move vào [folder]. Lý do: [1 câu]."
  Hỏi confirm trước khi move.

STEP 5 — Sau khi user confirm:
  → Move file ra khỏi Inbox vào folder đúng
  → Proceed sang Phase A của W5 (hoặc W2 nếu là RAW-BOOK/OFFICIAL/ACADEMIC)
```

**Rule quan trọng:** File trong Inbox **KHÔNG được cite** trong wiki nodes cho đến khi đã move ra folder đúng và qua Phase A–D.

---

## Phase A — Pre-flight & Classification

**A1. Xác nhận label:**
```
Đọc frontmatter của file clipping:
  → Có `source:` URL + `author:` rõ ràng → [RAW-CLIP]
  → Không có URL / style tổng hợp nhiều nguồn / không có tác giả cụ thể → [RAW-DR-LLM]
  → Có URL nhưng không có citation gì trong nội dung → [RAW-OPINION]
```

**A2. Concept Map — giống W2 nhưng thêm cột "Risk":**

Tạo concept map tại `04_outputs/temp/[source_name]_concept_map.md`, format:

```markdown
## Concept Map: [Source Title]
Label: [RAW-CLIP] / [RAW-DR-LLM] / [RAW-OPINION]
Author: ...  |  Published: ...  |  Source: ...

| Claim | Loại | Có citation? | Risk Flag |
|-------|------|-------------|-----------|
| "X causes Y via Z" | Causal | Yes/No | CHECK-CONFLICT / OK |
| "Rate is X%" | Data | Yes/No | VERIFY-NUMBER |
| "Framework A means B" | Mechanism | Yes/No | CHECK-AGREE |
```

**Risk flags:**
- `CHECK-CONFLICT` — claim causal mạnh, cần check với books
- `VERIFY-NUMBER` — số cụ thể từ non-book source, PHẢI verify
- `CHECK-AGREE` — mechanism claim, check có đồng thuận với wiki không
- `OK` — factual/contextual, không phải luận điểm cứng

---

## Phase B — Adversarial Audit (KHÁC BIỆT SO VỚI W2)

> Mục đích: phát hiện xung đột với knowledge base sách trước khi bất kỳ thứ gì được ingest.

**B1. Với mỗi claim có Risk Flag:**

```
→ python librarian.py search "<claim keyword>"
→ Đọc top-3 kết quả wiki

IF wiki node tồn tại + claim ĐỒNG THUẬN với node:
  → Đánh dấu: AGREE
  → Ghi chú: source có thể cite cùng nguồn gốc với book
  → Khi ingest: EXPAND source_refs[], KHÔNG tăng confidence

IF wiki node tồn tại + claim MÂU THUẪN với node:
  → Đánh dấu: CONFLICT
  → KHÔNG merge vào node cũ
  → Xác định: mâu thuẫn về (a) số liệu, (b) cơ chế, hay (c) kết luận?
  → Route sang Phase C-CONFLICT

IF wiki node KHÔNG tồn tại:
  → Đánh dấu: NEW-TERRITORY
  → Route sang Phase C-NEW, với confidence thấp hơn W2

IF claim là opinion/perspective (không phải mechanism):
  → Route sang Phase C-PERSPECTIVE
```

**B2. Screen đặc biệt cho [RAW-DR-LLM]:**

```
Trước khi dùng BẤT KỲ số liệu nào từ DR-LLM output:
  → Tìm citation gốc trong text (nếu Gemini Deep Research thường cite nguồn)
  → Nếu có citation → treat citation đó như [WEB], verify URL còn hoạt động không
  → Nếu không có citation → label số đó là [LLM-E — unverified], KHÔNG cite trực tiếp
  → Mechanism descriptions (không có số) → có thể dùng như [LLM-E] với caveat
```

---

## Phase C — Merge (3 nhánh)

### C-AGREE: Clip confirm wiki (không conflict)

```
Writeback type: UPDATE
→ UPDATE source_refs[] trong node hiện có (bổ sung, KHÔNG thay thế)
→ Thêm entry: { file: "[clip_filename].md", label: "[RAW-CLIP]", note: "confirms — no confidence bump" }
→ KHÔNG tăng confidence (CLIP/DR-LLM không đủ điều kiện tăng confidence)
→ Nếu clip có góc nhìn / analogy thú vị → thêm vào ## Worked Example với label [RAW-CLIP]
→ Cập nhật updated: và ghi log: "[YYYY-MM-DD] UPDATE — NodeName — added clip source — [RAW-CLIP]"
```

### C-CONFLICT: Clip mâu thuẫn với wiki

```
Writeback type: CONTRADICTION
IF mâu thuẫn về số liệu:
  → Kiểm tra ngày: clip mới hơn book?
    YES → gắn ⚠️ [STALE SIGNAL] vào node cũ + [INGEST CANDIDATE]
    NO  → ghi note trong node: "Contradicted by [clip] — older/unverified source"
  → KHÔNG replace số liệu cũ bằng số từ clip

IF mâu thuẫn về cơ chế / kết luận:
  → CONTRADICTION: SPAWN node mới tại 03_wiki/contradictions/
  → Node format: type: contradiction, status: conflict, confidence: 1
  → Body: [Quan điểm A — RAW-BOOK source] vs [Quan điểm B — RAW-CLIP source]
  → Thêm điều kiện: "A đúng khi X, B đúng khi Y" (nếu có thể xác định trục)
  → Link 2 chiều: node gốc ←→ contradiction node (BRIDGE tự động)
  → Log: "[YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis (data/mechanism/conclusion)"
```

### C-NEW: Clip mở ra territory chưa có trong wiki

```
Writeback type: SPAWN
→ SPAWN node mới tại folder phù hợp (mechanisms/ / definitions/ tùy loại)
→ confidence: 1 (single non-book source)
→ status: draft
→ source_refs: [{ file: "[clip].md", label: "[RAW-CLIP]" }]
→ Thesis phải mark: [RAW-CLIP — not yet verified against books]
→ Ghi vào Active Debt trong memory.md: "Verify [[NodeName]] against RAW-BOOK"
→ Log: "[YYYY-MM-DD] SPAWN — NodeName — source [RAW-CLIP]"
```

### C-PERSPECTIVE: Opinion / Analyst view

```
Writeback type: PERSPECTIVE
→ PERSPECTIVE: SPAWN node tại 03_wiki/perspectives/
→ type: perspective
→ school: [label theo P2 taxonomy nếu applicable]
→ confidence: 2 (analyst view, không phải mechanism claim)
→ Thesis dùng ngôn ngữ attributed: "Theo [Author], X vì Y"
→ Link tới node mechanism liên quan nếu có
→ Log: "[YYYY-MM-DD] PERSPECTIVE — NodeName — author/school"
```

---

## Phase D — Sync (giống W2)

```bash
python librarian.py ingest
```

> Nếu cần manual control:
```bash
python 05_scripts/_build_wiki_graph.py
python 05_scripts/gen_index.py
python 05_scripts/auto_bridge.py --force --backup
python 05_scripts/auto_synthesis.py --check --stale-only
```

---

## Quick Reference: W5 vs W2

| Điểm khác biệt | W2 (Books) | W5 (Clip/DR) |
|----------------|-----------|-------------|
| Confidence tăng khi confirm? | ✅ Có | ❌ Không |
| Số liệu từ source → cite trực tiếp? | ✅ Có | ❌ Phải verify |
| Conflict → merge vào node? | ❌ Tạo contradiction | ❌ Tạo contradiction |
| New territory → confidence khởi đầu | 1 (tăng khi có RAW) | 1 (phải verify bằng book) |
| Mechanism claims → trust? | High | Medium (cần corroborate) |
| Adversarial Audit bắt buộc? | ❌ Không | ✅ Bắt buộc |

---

## Giới hạn: Tối đa 3 writebacks/session (giống W2).
