# Wiki Link — Luồng hiện tại, vận hành, và cleanup repo

> Mục tiêu của tài liệu này: mô tả **trạng thái hiện tại đang chạy thực tế** của repo, chỉ ra các điểm chưa tối ưu, xác định artefact/rác, và chốt cách vận hành ngắn gọn. Tài liệu này bổ sung cho các file trong `00_design/` đang mô tả kiến trúc đích và plan nâng cấp.

---

## 1. Ảnh chụp hệ thống hiện tại

- Workspace hiện có các lớp chính:
  - `01_schema/`: luật vận hành, protocol, workflow, schema.
  - `02_sources/`: nguồn thô Markdown sau extract.
  - `03_wiki/`: node tri thức nguyên tử.
  - `04_outputs/`: node staged, research, audit, temp.
  - `05_scripts/`: engine script.
  - `06_publish/`: output đã polish.
  - `.cache/` và `graphify-out/`: artefact phái sinh, tái sinh được.
- Entry point duy nhất đang dùng là `librarian.py`.
- Trạng thái đo được khi rà repo:
  - `python librarian.py status`: `888` wiki nodes, `34` scripts, `11` wisdom reports, `0` staged, `0` stale, `99` orphans.
  - `python librarian.py health`: `18` node thiếu thesis, `3` stale theo quét staleness, `270` node cần raw-source verification.
- Git đang có thay đổi người dùng chưa commit, nên cleanup chỉ đụng artefact tái sinh được và code hạ tầng an toàn.

---

## 2. Luồng vận hành hiện tại

### 2.1 Luồng ingest

```text
PDF / clipping / inbox
  -> extract_pdf(.py / _docling.py)
  -> 02_sources/*.md
  -> stage / review / audit
  -> 04_outputs/staged_nodes
  -> accept
  -> 03_wiki/*.md
  -> librarian sync / ingest
  -> graphify-out/graph.json
  -> 01_schema/index/*
  -> git push source markdown
  -> Colab build BGE-M3
  -> pull .cache/wiki_embed.*
```

### 2.2 Luồng search và research

```text
Query
  -> librarian search
  -> wiki_search / semantic_search / hybrid_search
  -> graphify-out/graph.json + .cache/wiki_index.db + pulled FAISS artifact
  -> deepdive nếu coverage mỏng
  -> audit / synthesis
  -> 04_outputs/research hoặc 06_publish
```

### 2.3 Luồng sync hệ thống

```text
03_wiki thay đổi
  -> _build_wiki_graph.py
  -> gen_index.py
  -> auto_bridge.py (nếu ingest)
  -> staleness / health / suggest_ideas
  -> nếu cần semantic mới: push source -> rebuild trên Colab -> pull artifact
```

---

## 3. Vai trò từng lớp

### 3.1 Source-of-truth

- `01_schema/`: luật, template, protocol.
- `02_sources/`: raw evidence đã extract.
- `03_wiki/`: knowledge layer chính.
- `06_publish/`: nội dung phát hành cuối.

### 3.2 Tầng trung gian

- `04_outputs/staged_nodes/`: draft chờ review.
- `04_outputs/research/`: synthesis và note nghiên cứu.
- `04_outputs/temp/`: scratch space, không nên coi là dữ liệu bền.

### 3.3 Artefact phái sinh

- `.cache/`: FAISS, SQLite FTS5, manifest, search cache.
- `graphify-out/graph.json`, `graph.html`, `GRAPH_REPORT.md`: output đồ thị.
- `graphify-out/cache/` và các file `.graphify_*`: cache/debug trung gian của graphify.
- `__pycache__/`, `05_scripts/extract_log.txt`: artefact runtime.

---

## 4. Thành phần chưa tối ưu

### 4.1 Orchestrator phình to

- `librarian.py` đang ôm quá nhiều trách nhiệm:
  - dispatch CLI
  - runner
  - validate
  - help registry
  - status counting
  - writeback/log helpers
- Hệ quả:
  - khó test theo module
  - khó đọc quan hệ pipeline
  - thay đổi nhỏ dễ va chạm chéo

### 4.2 Code trùng trong orchestrator

- `librarian.py` có định nghĩa trùng `step_embed_build()` và `step_embed_stats()`.
- Đây là tín hiệu file đã lớn hơn mức nên quản lý thủ công an toàn.

### 4.3 Sync graph chưa tự vệ với dữ liệu trùng

- `_build_wiki_graph.py` trước khi sửa chỉ `extend()` node/edge mới vào `graph.json`.
- Nếu graph đã có dữ liệu cũ cùng khóa, file đồ thị có thể phình dần theo số lần sync.
- Ngoài ra logic provenance source hiện vẫn hardcode cho một vài pattern source (`Alexander During`, `Perry`), chưa phải mapping tổng quát.

### 4.4 Artefact lẫn với code và design

- `graphify-out/` chứa cả output chính lẫn cache/debug trung gian.
- `05_scripts/` còn log file và notebook ad hoc.
- Root repo còn các báo cáo phân tích đơn lẻ nằm ngoài `06_publish/` hoặc `00_design/`.

### 4.5 Sức khỏe tri thức còn nợ

- `99` orphan nodes.
- `18` nodes thiếu `thesis`.
- `270` nodes cần raw-source verification.
- Đây không phải "rác file", nhưng là "rác cấu trúc tri thức" cần xử lý dần bằng workflow.

---

## 5. Thành phần rác hoặc nên coi là artefact

### 5.1 Có thể xóa và tái sinh

- `__pycache__/`
- `05_scripts/__pycache__/`
- `05_scripts/.cache/wiki_search_cache.pkl`
- `05_scripts/extract_log.txt`
- `graphify-out/cache/`
- `graphify-out/.graphify_*`

### 5.2 Nên giữ nhưng phải coi là output, không phải nguồn

- `.cache/wiki_embed.index`
- `.cache/wiki_index.db`
- `graphify-out/graph.json`
- `graphify-out/graph.html`
- `graphify-out/GRAPH_REPORT.md`

### 5.3 Không tự động xóa trong lượt này

- File untracked do người dùng vừa tạo:
  - `00_design/*`
  - `02_sources/WikiLink_System_Architecture_2026-06-27.md`
  - `05_scripts/normalize_ocr_md.py`
  - `05_scripts/to_MD.ipynb`
  - `05_scripts/to_MD_chunkr.ipynb`
  - `06_publish/2026-06-27_fed-treasury-balance-sheet-h1-2026_note.md`
  - `Fed_Treasury_Balance_Sheet_H1_2026_MODE_DEEP_v2.md`
- Lý do: đây có thể là nội dung làm việc thực tế hoặc đang được người dùng soạn, không phải artefact runtime chắc chắn.

---

## 6. Cleanup đã thực hiện

- Bổ sung `.gitignore` để chặn:
  - `05_scripts/extract_log.txt`
  - `graphify-out/cache/`
  - `graphify-out/.graphify*`
- Bỏ định nghĩa trùng trong `librarian.py`.
- Thêm dedupe node/edge trong `_build_wiki_graph.py` để tránh graph sync tiếp tục cộng dồn trùng lặp.
- Dọn artefact runtime tái sinh được:
  - `__pycache__/`
  - `05_scripts/__pycache__/`
  - `05_scripts/.cache/wiki_search_cache.pkl`
  - `05_scripts/extract_log.txt`
  - `graphify-out/cache/`
  - `graphify-out/.graphify_*`

---

## 7. Vận hành khuyến nghị

### 7.1 Đầu session

```text
1. Đọc CLAUDE.md -> 01_schema/hot.md -> 01_schema/memory.md -> system.md
2. python librarian.py status
3. python librarian.py help
4. Nếu làm trên node/wiki: search trước rồi mới tạo/sửa
```

### 7.2 Sau khi sửa node hoặc ingest

```text
1. python librarian.py sync
2. python librarian.py health
3. Nếu cần semantic artifact mới: push source -> rebuild trên Colab -> pull artifact
```

### 7.3 Khi làm research

```text
1. python librarian.py search "<query>"
2. Nếu mỏng: python librarian.py deepdive "<query>"
3. Nếu cần landscape: python librarian.py wisdom "<tag>" --no-llm
4. Khi chuẩn bị merge: python librarian.py audit <file>
```

### 7.4 Quy tắc tách lớp

- `00_design/`: tài liệu kiến trúc, luồng, quyết định kỹ thuật.
- `06_publish/`: note và bài đã polish.
- Root repo: chỉ giữ entrypoint, luật hệ thống, và file điều phối thật sự cần ở root.
- Artifact chạy máy phải nằm trong `.cache/`, `graphify-out/`, hoặc `04_outputs/temp/`.

---

## 8. Backlog tối ưu tiếp theo

1. Tách `librarian.py` thành:
   - `cli/dispatch`
   - `pipelines/*`
   - `validators/*`
   - `status/*`
2. Tách `05_scripts/` theo module vật lý giống hướng trong `00_design/WikiLink_KG2RAG_System_Architecture.md`.
3. Chuẩn hóa chỗ chứa notebook và script ad hoc:
   - notebook research/extract vào thư mục riêng như `05_scripts/notebooks/`
   - log/cache vào `04_outputs/temp/` hoặc thư mục cache rõ ràng
4. Sửa `_build_wiki_graph.py` để provenance source không còn hardcode theo từng bộ sách.
5. Giảm orphan count bằng workflow:
   - chạy `python librarian.py ingest`
   - review output của `auto_bridge`
   - audit lại các hub node thiếu liên kết
6. Xử lý `18` node thiếu thesis trước khi mở rộng ingest thêm.

---

## 9. Kết luận vận hành

Repo hiện vận hành được, cấu trúc tổng thể đúng hướng, nhưng đang có ba loại nợ khác nhau:

- **nợ code**: orchestrator monolith, một số helper trùng, script sync graph còn thô;
- **nợ repo hygiene**: cache/debug/log artefact còn lẫn vào workspace;
- **nợ tri thức**: orphan nodes, missing thesis, low-verification nodes.

Việc cleanup nên tiếp tục theo thứ tự:

```text
artifact runtime -> orchestrator hygiene -> graph/provenance correctness -> knowledge health
```
