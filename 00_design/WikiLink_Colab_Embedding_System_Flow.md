# Wiki Link — Luồng hệ thống embedding chạy hoàn toàn trên Colab

> Trạng thái mục tiêu của tài liệu này: **local không build embedding**, **Colab là nơi duy nhất build/rebuild vector index**, và local chỉ tiêu thụ artifact embedding đã kéo về.

---

## 1. Quyết định hệ thống

- Engine embedding chuẩn: `BAAI/bge-m3`
- Nơi build embedding duy nhất: **Google Colab (T4/GPU)**
- Artifact embedding chuẩn:
  - `.cache/wiki_embed.index`
  - `.cache/wiki_embed.meta.json`
  - `.cache/wiki_embed.manifest.json`
- Source-of-truth để build embedding:
  - `03_wiki/**/*.md`
  - `02_sources/**/*.md`
- Local machine:
  - được phép `sync`, `search`, `research`, `audit`
  - **không còn là nơi chuẩn để chạy `embed_index.py --build`**

---

## 2. Mục tiêu của thiết kế này

- Loại bỏ phụ thuộc vào CPU local cho workload nặng.
- Cố định một môi trường build embedding duy nhất để tránh drift.
- Giữ repo theo mô hình:
  - dữ liệu tri thức đi qua Git
  - vector index là artifact phái sinh
- Làm cho vận hành rõ ràng:
  - local viết tri thức
  - Colab build vector
  - local chỉ pull artifact và dùng lại

---

## 3. Phân vai hệ thống

### 3.1 Local workspace

- Chỉnh sửa `02_sources/` và `03_wiki/`
- Chạy `librarian.py sync`
- Chạy graph/index text/local audit
- Commit + push source markdown
- Kéo artifact embedding từ Colab về `.cache/`

### 3.2 GitHub private repo

- Kênh trung chuyển source-of-truth giữa local và Colab
- Chỉ chứa `.md`, code, schema, design
- Không là nơi lưu artifact embedding

### 3.3 Colab runtime

- Clone repo mới nhất
- Cài `sentence-transformers`, `faiss-cpu`
- Load `BAAI/bge-m3`
- Chạy full build embedding
- Nén artifact `.cache/wiki_embed.*`
- Xuất zip về local

---

## 4. Luồng hệ thống tổng thể

```text
LOCAL AUTHORING
  02_sources/*.md, 03_wiki/*.md
    -> librarian.py sync
    -> git add/commit/push

GIT REMOTE
  private repo
    -> Colab clone/pull latest

COLAB EMBEDDING
  pip install deps
    -> python 05_scripts/embed_index.py --build
    -> zip .cache/wiki_embed.*
    -> download artifact

LOCAL CONSUMPTION
  pull_embed_index.ps1
    -> .cache/wiki_embed.*
    -> semantic_search / hybrid_search / deepdive / wiki_search
```

---

## 5. Luồng chi tiết theo pha

### 5.1 Pha A — tạo hoặc cập nhật tri thức trên local

```text
PDF / note / clipping
  -> extract / normalize
  -> 02_sources/*.md
  -> stage / review
  -> 03_wiki/*.md
  -> python librarian.py sync
  -> graph + text index local được cập nhật
```

Kết quả của pha này:
- source markdown mới nhất đã sẵn sàng
- graph/search text local đã đúng
- embedding artifact có thể vẫn cũ

### 5.2 Pha B — xuất source-of-truth lên remote

```text
local markdown changes
  -> git add 02_sources 03_wiki
  -> git commit
  -> git push
```

Nguyên tắc:
- chỉ push phần source cần thiết
- không push `.cache/wiki_embed.*`
- repo phải private

### 5.3 Pha C — build embedding trên Colab

```text
Colab runtime start
  -> git clone / git pull
  -> install dependencies
  -> python 05_scripts/embed_index.py --build
  -> zip .cache/wiki_embed.index/meta/manifest
  -> download zip
```

Nguyên tắc:
- chỉ dùng `--build`
- không dùng `--incremental` cross-machine
- Colab là môi trường chuẩn để tải `BAAI/bge-m3`

### 5.4 Pha D — nhập artifact về local

```text
wiki_embed_artifacts.zip
  -> Downloads
  -> powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1
  -> .cache/wiki_embed.*
```

Kết quả:
- local có index đúng theo source mới nhất đã push
- semantic search dùng artifact mới

### 5.5 Pha E — tiêu thụ embedding trên local

```text
query
  -> semantic_search.py
  -> hybrid_search.py
  -> deepdive_search.py
  -> librarian search / deepdive
```

Local ở pha này:
- chỉ load model nếu cần query embedding
- không chịu trách nhiệm build lại index chuẩn

---

## 6. Chuỗi vận hành chuẩn

### 6.1 Khi chỉ sửa tri thức

1. Sửa `02_sources/` hoặc `03_wiki/`
2. Chạy `python librarian.py sync`
3. Chạy health/audit nếu cần
4. Commit + push
5. Chưa cần semantic artifact mới nếu chưa làm semantic research

### 6.2 Khi cần semantic search đúng dữ liệu mới nhất

1. Hoàn tất chỉnh sửa source
2. Push source mới nhất lên remote
3. Rebuild embedding trên Colab
4. Kéo artifact về local
5. Chạy semantic/hybrid/deepdive

### 6.3 Khi chỉ làm graph hoặc text search

- Không cần Colab
- Không cần rebuild embedding
- Chỉ cần `librarian.py sync` là đủ

---

## 7. Trạng thái nhất quán của hệ thống

### 7.1 Hệ thống nhất quán hoàn toàn khi

- `02_sources/` và `03_wiki/` local đã commit/push
- Colab rebuild từ đúng commit mới nhất
- `.cache/wiki_embed.*` local được pull từ build đó

### 7.2 Hệ thống nhất quán một phần khi

- graph/text index local đã mới
- embedding artifact vẫn cũ

Trường hợp này:
- keyword search vẫn dùng được
- graph sync vẫn đúng
- semantic result có thể lệch so với markdown mới nhất

---

## 8. Failure modes cần hiểu rõ

### 8.1 Local sửa source nhưng quên rebuild Colab

Hệ quả:
- semantic search không phản ánh node/source mới

Dấu hiệu:
- `librarian.py sync` thấy node mới
- nhưng `semantic_search` không thấy nội dung mới

### 8.2 Colab build từ commit cũ

Hệ quả:
- artifact hợp lệ về kỹ thuật nhưng sai về dữ liệu

Kiểm soát:
- luôn `git pull` hoặc clone mới trước khi build

### 8.3 Local giữ artifact cũ

Hệ quả:
- query semantic chạy được nhưng drift so với remote/source hiện hành

Kiểm soát:
- sau mỗi đợt rebuild Colab, luôn import lại zip vào `.cache/`

### 8.4 Chạy incremental cross-machine

Hệ quả:
- manifest/mtime không còn tin cậy
- dễ sinh index thiếu hoặc sai

Kết luận:
- **cấm dùng incremental trên Colab flow chuẩn**

---

## 9. Quy tắc vận hành mới

- `librarian.py sync` là lệnh local chuẩn sau khi sửa tri thức
- `embed_index.py --build` là lệnh Colab chuẩn
- `embed_index.py --incremental` không còn là đường vận hành chính
- `.cache/wiki_embed.*` là artifact, không commit
- mọi semantic regression trước tiên phải kiểm tra:
  - source đã push chưa
  - Colab đã rebuild chưa
  - local đã pull artifact mới chưa

---

## 10. Checklist ngắn

### 10.1 Local authoring

```powershell
python librarian.py sync
git add 02_sources 03_wiki
git commit -m "feat: update knowledge"
git push
```

### 10.2 Colab build

```powershell
python 05_scripts/embed_index.py --build
```

### 10.3 Local import artifact

```powershell
powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1
python 05_scripts\embed_index.py --stats
```

---

## 11. Kết luận

Luồng mới của repo nên được hiểu ngắn gọn như sau:

```text
local viết tri thức
  -> git đẩy source
  -> Colab build BGE-M3
  -> local kéo artifact
  -> local dùng semantic search
```

Đây là điểm cắt hệ thống rõ ràng nhất:

- **Markdown là dữ liệu gốc**
- **Colab là xưởng build embedding**
- **Local là nơi authoring + tiêu thụ**
