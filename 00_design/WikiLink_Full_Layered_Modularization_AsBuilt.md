# Wiki Link — Full Layered Modularization (As-Built)

> Tài liệu này chốt trạng thái module hóa **thực tế đã áp dụng** cho repo hiện tại, vượt ra ngoài `librarian.py` và bao gồm cả tầng `05_scripts/`.

---

## 1. Kết quả đạt được

Repo hiện đã được module hóa theo hai lớp:

### 1.1 Lớp CLI / orchestrator

```text
librarian.py
-> librarian_pkg/
   -> cli
   -> shared
   -> steps
   -> validation
   -> help_data
   -> pipelines/
      -> maintenance
      -> content
      -> research
```

### 1.2 Lớp engine scripts

```text
05_scripts/
-> retrieval/
-> ingestion/
-> governance/
-> synthesis/
-> graph/
-> ops/
-> common/
-> root wrappers (compatibility layer)
```

---

## 2. Nguyên tắc module hóa đã dùng

1. Không phá entrypoint cũ.
2. Tách orchestration trước, engine sau.
3. Tách vật lý theo domain nhưng giữ wrapper tương thích để không gãy SOP.
4. Code mới phải import từ layer thật; wrapper root chỉ để tương thích ngược.

---

## 3. Tầng hiện tại của repo

### 3.1 Control layer

- `librarian.py`
- `librarian_pkg/*`

Đây là lớp điều phối, không chứa business logic nặng của retrieval/ingest ngoài orchestration.

### 3.2 Engine layer

- `05_scripts/retrieval/*`
- `05_scripts/ingestion/*`
- `05_scripts/governance/*`
- `05_scripts/synthesis/*`
- `05_scripts/graph/*`
- `05_scripts/ops/*`

Đây là lớp thực thi pipeline.

### 3.3 Compatibility layer

- `05_scripts/*.py` ở root

Các file này giờ là wrapper mỏng trỏ vào implementation mới trong subfolder tương ứng.

### 3.4 Data and source-of-truth layer

- `01_schema/`
- `02_sources/`
- `03_wiki/`
- `04_outputs/`
- `06_publish/`

---

## 4. Ưu điểm của trạng thái mới

- `librarian.py` không còn là monolith.
- `pipelines` đã tách theo nhóm trách nhiệm.
- `05_scripts` không còn flat layout.
- Retrieval, ingest, governance, synthesis, graph và ops đã có ranh giới vật lý rõ hơn.
- Các path cũ như `python 05_scripts/wiki_search.py` vẫn dùng được.

---

## 5. Chi phí đánh đổi hiện tại

- Có song song hai bề mặt:
  - implementation thật trong subfolders
  - wrapper compatibility ở root
- `status` hiện đếm cả wrapper lẫn implementation thật, nên số script tăng lên.
- Một số script vẫn dùng subprocess qua wrapper cũ, chưa chuyển sang import nội bộ hoàn toàn.

---

## 6. Điểm còn chưa “tối đa”

Module hóa hiện tại đã sâu hơn rõ rệt, nhưng chưa phải trạng thái cuối:

1. `retrieval/`, `ingestion/`, `governance/` vẫn còn là các script lớn, chưa tách tiếp thành helper module nhỏ hơn.
2. `embed_index.py` vẫn chưa được đẩy vào namespace riêng như `embedding/`.
3. Notebook và PowerShell helper vẫn chưa được gom thành nhóm hỗ trợ riêng.
4. Chưa có test package hóa tự động cho từng layer.

---

## 7. Hướng đi tiếp để đạt “tối đa” hơn nữa

### 7.1 Tách sâu trong từng layer

Ví dụ:

```text
retrieval/
  core/
  bm25/
  semantic/
  fusion/
  cli/
```

```text
ingestion/
  extract/
  staging/
  coverage/
  drafting/
  cli/
```

### 7.2 Tách embedding thành layer riêng

```text
05_scripts/embedding/
  embed_index.py
  manifest.py
  stats.py
```

### 7.3 Loại dần wrapper root

Khi SOP và các lệnh nội bộ đã migrate hoàn toàn, wrapper root có thể giảm dần hoặc chuyển sang deprecation mode.

---

## 8. Kết luận

Repo hiện đã đạt module hóa theo tầng ở mức thực dụng và an toàn:

```text
entrypoint stable
-> orchestrator layered
-> engine scripts layered
-> compatibility preserved
```

Đây là trạng thái tốt để tiếp tục refactor sâu hơn mà không làm gãy workflow đang dùng hàng ngày.
