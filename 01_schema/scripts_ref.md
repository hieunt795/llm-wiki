# SCRIPTS REFERENCE — Wiki Link Operations
> Load khi: cần biết cách vận hành các công cụ tự động.

---

## 0. LIBRARIAN (Single Entry Point)

### `librarian.py` — Wiki Link Librarian v1.0
**Dùng Librarian thay vì gọi scripts trực tiếp cho mọi pipeline cơ học.**

```powershell
python librarian.py status                          # System overview
python librarian.py sync                            # Phase D: build_graph + gen_index + staleness
python librarian.py ingest                          # Post-ingest: sync + auto_bridge + staleness
python librarian.py health                          # orphans + missing_thesis + staleness + bounties
python librarian.py daily                           # Daily workflow: suggest + orphans + staleness
python librarian.py wisdom <tag> [--no-llm]         # Wisdom synthesis cho một tag
python librarian.py audit <file>                    # Claim audit
python librarian.py search "<query>" [--deep]       # Search (--deep = hybrid_search)
python librarian.py deepdive "<query>"              # Detect thin nodes -> drill RAW -> draft expansion
python librarian.py rename OldName NewName          # Safe rename + sync
python librarian.py staleness [--auto-mark]         # Report or mark stale nodes
python librarian.py stage --dry-run                 # auto_ingest wrapper
python librarian.py extract --book perry --skip-existing
python librarian.py scout --mode lines --n 10
python librarian.py section --dir ... --heading ... --out ...

# Cơ chế bỏ qua / chỉ chạy một bước:
python librarian.py sync --skip gen_index
python librarian.py health --only staleness,find_orphans
python librarian.py sync --only staleness
```

> **Expand:** Thêm pipeline mới = thêm 1 function `pipeline_X(runner)` + 1 entry trong `parser.add_argument choices` trong `librarian.py`.

---

## 1. INGESTION & EXTRACTION

### `exact_extractor.py` (Surgical Extraction)
Công cụ trích xuất văn bản gốc chính xác từ sách dựa trên đề mục.
- **Mục đích:** Đảm bảo LLM có đầy đủ ngữ cảnh gốc, tránh tóm tắt sơ sài.
- **Cách dùng:**
  ```powershell
  python 05_scripts/exact_extractor.py --dir "02_sources/books/slug" --heading "10.1." --out "output_path.md"
  ```
- **Canonical entry point:** `python librarian.py section --dir ... --heading ... --out ...`
- **Flags:**
  - `--dir`: Thư mục chứa các file .md của sách.
  - `--heading`: Tên đề mục (ví dụ: "Chapter 8" hoặc "10.1.").
  - `--out`: Đường dẫn file kết quả.

---

## 2. GRAPH & SEMANTIC BRIDGING

### `auto_bridge.py` (Semantic Linking)
Tự động kết nối các node mồ côi (orphans) dựa trên bí danh và từ khóa.
- **Giao thức mới:** Đã loại bỏ các liên kết đến Raw Source khi tính toán độ cô lập ngữ nghĩa.
- **Cách dùng:**
  ```powershell
  python 05_scripts/auto_bridge.py --report     # Xem thống kê sức khỏe đồ thị
  python 05_scripts/auto_bridge.py --dry-run    # Xem trước gợi ý liên kết
  python 05_scripts/auto_bridge.py --force --backup  # Áp dụng + Sao lưu
  ```

### `_build_wiki_graph.py` (Graph Sync)
Cập nhật metadata và các cạnh (edges) vào file `graph.json`.
- **Cách dùng:**
  ```powershell
  python 05_scripts/_build_wiki_graph.py
  ```

---

## 3. INDEXING

### `gen_index.py` (Master Index Generator)
Tái cấu trúc và tạo mới file `index.md` cùng các sub-indexes theo loại node.
- **Cách dùng:**
  ```powershell
  python 05_scripts/gen_index.py
  ```

---

## 4. UTILITIES

---

## 5. SEARCH & AUDIT DEEP DIVE

> **Search Escalation Order:** `semantic_search` (meaning-based, cross-language) → `wiki_search` (fast, BM25+keyword) → `hybrid_search` (deep: Graphify + BM25 + Heatmap) → `deepdive_search` (detect thin → drill RAW → draft)
> **Canonical entry point:** `python librarian.py search "<query>"` hoặc `--deep` để dùng hybrid.
> **Semantic entry point:** `python 05_scripts/semantic_search.py "<query>"` — dùng khi keyword search miss hoặc query tiếng Việt tìm concept tiếng Anh.

### `wiki_search.py` (BM25 + Recency — v3.3)
Tìm kiếm nhanh trong wiki + raw sources theo BM25 với recency decay (half_life_years).
- **Indexes:** `03_wiki/` (wiki) + `02_sources/` (raw) — cả hai trong một cache build.
- **Scoring:** BM25 × exp(-ln2 × age / half_life) + source_refs boost ×1.5 + [LLM] penalty ×0.5.
- **Cache:** `.cache/wiki_search_cache.pkl` (TTL 600s, format version 3 — invalidates stale-raw builds).
- **Cách dùng:**
  ```powershell
  python 05_scripts/wiki_search.py "private credit" --top 10
  python 05_scripts/wiki_search.py "fiscal dominance" --no-raw      # wiki only
  python 05_scripts/wiki_search.py "LCR" --no-wiki --top 5          # raw only
  python 05_scripts/wiki_search.py "bond price" --json              # JSON output for piping
  python 05_scripts/wiki_search.py "inflation" --min-confidence 3   # confidence filter
  ```
- **Bugs fixed 2026-05-02:** sys.path self-registration (fixes subprocess invocation from WIKI_ROOT); cache dirs_key always includes raw_dir; CACHE_FORMAT_VERSION bumped to 3.
- **Semantic flag (v3.4):** `--semantic` để hybrid keyword + embedding search cùng lúc (yêu cầu embed index đã build).

### `semantic_search.py` + `embed_index.py` (Embedding — v2.1)
Semantic search dựa trên sentence embeddings. Tìm được concept theo nghĩa, không cần đúng keyword. Cross-language (Việt ↔ English).
- **Model:** `paraphrase-multilingual-MiniLM-L12-v2` (~420MB, CPU encoder, 50+ ngôn ngữ).
  - Lý do giữ MiniLM: decoder-based models (Qwen3, BGE-M3) quá chậm trên CPU không GPU (~20h build).
  - Nâng cấp: dùng Colab GPU để rebuild với BGE-M3 (8192 token context) khi cần.
- **Chunking:** Wiki nodes → 1 vector/file. Raw sources → 1 vector/page (`<!-- Page N -->`), CHUNK_SIZE=1500 chars (~375 tokens).
- **Index:** `.cache/wiki_embed.index` (FAISS) + `.cache/wiki_embed.meta.json`. ~13,717 vectors.
- **Search bias:** `wiki_search` thiên wiki (title×5, thesis×4, aliases×3 boost). `semantic_search` thiên raw (12,901 raw chunks vs 816 wiki nodes). `--deep` kết hợp cả hai → cân bằng nhất.
- **Install (một lần):**
  ```powershell
  pip install sentence-transformers faiss-cpu watchdog --break-system-packages
  ```
- **Build/rebuild index:**
  ```powershell
  python 05_scripts/embed_index.py --build        # build lần đầu hoặc rebuild
  python 05_scripts/embed_index.py --stats        # xem số vectors + build time
  python 05_scripts/embed_index.py --build --watch  # auto-reindex khi file thay đổi
  ```
- **Search:**
  ```powershell
  python 05_scripts/semantic_search.py "chính phủ kiểm soát ngân hàng trung ương"
  python 05_scripts/semantic_search.py "collateral reuse" --top 5 --threshold 0.55
  python 05_scripts/semantic_search.py "yield curve control" --wiki-only
  python 05_scripts/semantic_search.py "BOJ intervention" --raw-only
  python 05_scripts/wiki_search.py "fiscal dominance" --semantic   # hybrid mode
  ```
- **Output:** Score (cosine 0–1) + file path + **page number** cho raw chunks + snippet text thực tế của trang.
- **Rebuild khi nào:** Sau khi thêm sách mới hoặc extract PDF mới vào `02_sources/`.

### `hybrid_search.py` (Graphify + BM25 + Heatmap — v3.2)
Ba lớp tìm kiếm kết hợp: structural neighbors từ graph + BM25 scores + fuzzy context windows.
- **STEP 1 — Graphify:** Query `graphify-out/graph.json` trực tiếp (không cần CLI). Trả về primary match, thesis, links TO/FROM.
- **STEP 2 — BM25:** Direct Python import `wiki_search` (không subprocess). Wiki + RAW cùng một lần.
- **STEP 3 — Heatmap:** 5 context windows rải đều 0%→100% file cho mỗi kết quả.
- **Cách dùng:**
  ```powershell
  python 05_scripts/hybrid_search.py "fiscal dominance"
  python 05_scripts/hybrid_search.py "interest rate transmission" --top 3
  python 05_scripts/hybrid_search.py "LCR" --raw-only               # RAW heatmap chỉ
  python 05_scripts/hybrid_search.py "private credit" --json        # JSON output
  python librarian.py search "fiscal dominance" --deep              # canonical
  ```
- **Bugs fixed 2026-05-02:** Graphify đọc graph.json trực tiếp (không gọi CLI); wiki_search qua import API (không subprocess → không python/python3 mismatch); file path resolution từ WIKI_ROOT.

### `deepdive_search.py` (Detect → Drill → Draft — v2.0)
Pipeline 3 giai đoạn cho thin-node research: phát hiện wiki coverage gaps → drill RAW → tạo expansion draft.
- **Thin node criteria:** confidence ≤ threshold (default 2) OR body chứa `[LLM]` OR không có `source_refs`.
- **Output:** `04_outputs/drafts/YYYY-MM-DD_<query>_deepdive.md` với RAW citations sẵn sàng review.
- **Cách dùng:**
  ```powershell
  python librarian.py deepdive "taralac facility"
  python librarian.py deepdive "interest rate corridor" --threshold 3
  python 05_scripts/deepdive_search.py "LCR mechanics"
  ```
- **Rewrite 2026-05-02:** Loại bỏ hoàn toàn ollama dependency; dùng wiki_search + hybrid_search Python API; output structured draft thực sự (không mock).

### `claim_auditor.py` (F.I.T.S.E.R.B.V.L Gatekeeper)
Kiểm chứng tính đúng đắn của một claim/file nháp so với toàn bộ Wiki.
- **Cách dùng:** `python 05_scripts/claim_auditor.py "path/to/draft.md"`
- **Quy trình:** Tự động tìm mâu thuẫn (Inconsistency) và xác định độ tin cậy.

### `raw_scout.py` (Random Discovery)
Lấy ngẫu nhiên từ khóa hoặc câu văn từ Raw Sources để tìm ý tưởng.
- **Cách dùng:** `python 05_scripts/raw_scout.py --mode lines --n 10`
- **Canonical entry point:** `python librarian.py scout --mode lines --n 10`

### `extract_pdf.py` (PDF -> Markdown)
Chuẩn hóa PDF raw source sang `.md` để search/ingest dùng được.
- **Cách dùng:** `python 05_scripts/extract_pdf.py --book perry --skip-existing`
- **Canonical entry point:** `python librarian.py extract --book perry --skip-existing`

### `auto_ingest.py` (Staging Workflow)
Scan books -> tìm uncovered sections -> stage draft nodes -> accept reviewed nodes vào wiki.
- **Cách dùng:** `python 05_scripts/auto_ingest.py --dry-run`
- **Canonical entry point:** `python librarian.py stage --dry-run`

---

## 6. NEW PIPELINES (Sprint 1–5, 2026-04-26)

### `deepdive_search.py` (Deep Research: Detect → Drill → Draft)
Phát hiện wiki nodes thin → escalate hybrid_search RAW → tạo expansion draft.
- **Trigger:** confidence≤2 OR [LLM]>0 OR no source_refs trong top wiki results
- **Output:** `04_outputs/drafts/YYYY-MM-DD_<query>_deepdive.md`
- **Cách dùng:** `python librarian.py deepdive "taralac facility"`

### `rename_node.py` (Safe Node Renamer)
Đổi tên node an toàn: heal toàn bộ [[OldName]] → [[NewName]] rồi rename file + sync.
- **Cách dùng:** `python librarian.py rename OldName NewName`
- **Tên có khoảng trắng:** `python librarian.py rename "Old Name" "New Name"`
- **Dry-run:** `python librarian.py rename OldName NewName --no-llm`

### Schema fields mới (Sprint 1)
Frontmatter additions — xem `01_schema/schema.md` để biết full spec:
- `status`: draft | reviewed | verified | stale | archived | conflict  (legacy: active→verified)
- `superseded_by` + `superseded_date`: version chain khi node bị replace
- `half_life_years`: 10 (mechanism) | 1 (regulation) | 0.1 (market-data) | 0.5 (synthesis)

### Recency weighting trong `wiki_search.py` (Sprint 2)
BM25 score × exp(-ln2 × age_years / half_life_years). Nodes với half_life_years ngắn tự fade khi outdated.

### Synthesis archiving trong `auto_synthesis.py` (Sprint 3)
Mỗi wisdom run tự động tạo node trong `03_wiki/syntheses/` với frontmatter chuẩn — vào graph, searchable.

### Web Search rules (Sprint 5) — xem W1_query.md Giai đoạn 3
- TIER 1 Ephemeral: `[WEB-YYYY-MM-DD:source]` inline, không persist
- TIER 2 Ingest-flagged: thêm `[INGEST CANDIDATE]` cuối response

### `_build_wiki_graph.py` (Graphify Post-processor, fixed 2026-04-27)
Inject wiki nodes + provenance edges vào `graphify-out/graph.json` sau khi graphify CLI chạy xong.
- **Workflow:** Chạy `graphify` trước → sau đó `python 05_scripts/_build_wiki_graph.py`
- **Bugs fixed 2026-04-27:**
  - Skip `_index.md` files (tránh duplicate IDs từ Sprint 2)
  - Fix indentation: Raw Sources loop — `if source_id not in existing_node_ids` vào đúng scope
  - Fix `source_refs` loop nested sai trong `for link` → chạy 1 lần/node thay vì 1 lần/link
  - Filter page anchors (`#page=N`, `.md#`) khỏi wikilinks → giảm dangling links ~50%

### Currently Layer (2026-04-27) — xem W1_query.md Giai đoạn 0
Currency Gate chạy ĐẦU TIÊN trước mọi query time-sensitive:
- Trigger: monetary policy, regulatory, market-data, macro, hoặc query chứa "hiện tại/latest/2026"
- Agent tự construct search query từ nguyên tắc (không hardcode template)
- `half_life_years` làm on/off switch: ≥10 skip, <10 trigger
- Validate source: discard nếu cũ hơn 6 tháng
- Response 3 lớp: `[WIKI LAYER]` → `[CURRENTLY — YYYY-MM-DD]` → `[SYNTHESIS]`
- Auto-flag `⚠️ STALE SIGNAL` + `[INGEST CANDIDATE]` khi news mâu thuẫn wiki node
