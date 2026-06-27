# W2 — SURGICAL INGEST
> Load khi: ingest tài liệu mới vào wiki.

## Phase 0 — SOURCE ROUTING (chạy TRƯỚC Phase A)

```
Xác định source type → gán nhãn → route đúng pipeline

IF source nằm trong books/
  → label: [RAW-BOOK]
  → proceed bình thường (Phase A–D dưới đây)

ELSE IF source nằm trong official_reports/
  → label: [RAW-OFFICIAL]
  → proceed bình thường (Phase A–D)

ELSE IF source nằm trong academic/
  → label: [RAW-ACADEMIC]
  → proceed bình thường (Phase A–D)

ELSE IF source nằm trong Clipping/ HOẶC deep-research/
  → label: [RAW-CLIP] hoặc [RAW-DR-LLM] (xem bảng dưới)
  → REDIRECT → W5_secondary_ingest.md

ELSE IF source nằm trong Inbox/
  → REDIRECT → W5_secondary_ingest.md, Phase 0-T (Triage)
  → AI phân loại xong mới ingest

ELSE (không rõ nguồn gốc)
  → label: [UNVERIFIED]
  → Move vào Inbox/ trước, chạy Triage
```

**Phân biệt [RAW-CLIP] vs [RAW-DR-LLM]:**

| Dấu hiệu | Label |
|----------|-------|
| File do Obsidian Clipper tạo (có `source:` URL, author rõ ràng) | `[RAW-CLIP]` |
| Output từ Gemini Deep Research / ChatGPT research mode | `[RAW-DR-LLM]` |
| Substack / blog / financial press | `[RAW-CLIP]` |
| File không có URL rõ ràng, viết theo style LLM tổng hợp | `[RAW-DR-LLM]` |

> **Note:** Thư mục `deep-research/` hiện có thể chứa cả Clipping lẫn LLM output — phân loại theo nội dung file, không theo tên thư mục.

---

## 4 Phases (áp dụng cho [RAW-BOOK], [RAW-OFFICIAL], [RAW-ACADEMIC])

### Phase A — Pre-flight (Concept Mapping)
- Convert source → `.md` vào `02_sources/`
- Tạo concept map tại `04_outputs/[source]_concept_map.md`
- Liệt kê các khái niệm chính, mối liên hệ, gaps so với wiki hiện có

### Phase B — Extraction (Surgical Merge)
- **Step 1: Raw Extraction**: Sử dụng `exact_extractor.py` để trích xuất văn bản gốc từ thư mục sách.
  ```powershell
  python 05_scripts/exact_extractor.py --dir "path/to/book" --heading "X.X" --out "staged_nodes/raw/..."
  ```
- **Step 2: Wiki Audit**: Chạy `python librarian.py search "<concept>"` cho từng khái niệm chính.
- **Step 3: Refinement**: Gọi Sub-agent (Generalist) để tinh chỉnh bản Raw thành chuẩn **Mode B** (P4_output).
- **IF** node tồn tại → **BẮT BUỘC AUDIT**: Đọc toàn bộ nội dung cũ.
  - Nội dung cũ ĐÚNG → **UPDATE** (bổ sung góc nhìn/ví dụ/toán học — KHÔNG thay thế nội dung cũ).
    - Append entry vào `source_refs[]`
    - Tăng `confidence` nếu source là [RAW-BOOK/OFFICIAL/ACADEMIC] và independent
    - Cập nhật `updated:` và ghi log
  - Nội dung cũ SAI/OUTDATED → **REPLACE** (ghi rõ lý do replace, ghi `superseded_by` nếu archive node cũ).
    - Confidence reset về source mới
  - Nội dung trùng hoàn toàn → **skip**
  - Nguồn mới mâu thuẫn với node hiện có → **CONTRADICTION**
    - KHÔNG merge vào body — tạo node riêng `type: contradiction` tại `03_wiki/contradictions/`
    - Link 2 chiều giữa 2 nodes
    - Xác định trục mâu thuẫn: số liệu / cơ chế / kết luận
  - Tìm thấy link còn thiếu giữa 2 node liên quan → **BRIDGE**
    - Confirm cả 2 node tồn tại, thêm wikilink 2 chiều
- **IF** node không tồn tại → **SPAWN**
  - Dùng template Mode B từ P4_output.md
  - `confidence: 1`, `status: draft` cho đến khi có ≥2 nguồn

### Phase C — Merge (Write & Log)
- Tạo/cập nhật node theo `schema.md`
- Cập nhật `01_schema/log.md` theo format chuẩn (xem W4_memory.md § log.md):
  ```
  [YYYY-MM-DD] SPAWN       — NodeName — source [RAW-TYPE]
  [YYYY-MM-DD] UPDATE      — NodeName — what added — source
  [YYYY-MM-DD] REPLACE     — NodeName — reason — old claim → new claim
  [YYYY-MM-DD] BRIDGE      — NodeA ↔ NodeB — rationale
  [YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis (data/mechanism/conclusion)
  ```
- Thêm wikilinks 2 chiều vào Related nodes

### Phase D — Sync
```bash
python librarian.py ingest
```

> `librarian.py ingest` tương đương post-ingest sync: `build_graph → gen_index → auto_bridge → staleness`.
> Nếu muốn chạy tay từng bước:
```bash
python 05_scripts/_build_wiki_graph.py
python 05_scripts/gen_index.py
python 05_scripts/auto_bridge.py --force --backup
python 05_scripts/auto_synthesis.py --check --stale-only
```

> Nếu `--check` báo có tag STALE → chạy `auto_synthesis.py "<tag>" --no-llm` để refresh report trước session tiếp theo. Không bắt buộc chạy ngay — lazy refresh được chấp nhận nếu session tiếp theo không dùng tag đó.

## Giới hạn: Tối đa 3 writebacks/session để tránh drift.
