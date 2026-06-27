# Embedding split: Local (CPU) ↔ Colab T4 (GPU)

Tách compute: **local sinh node `.md`**, **Colab T4 chạy embed/FAISS**. Transport = **Git/GitHub** cho `.md`, kênh riêng (browser download / Drive) cho artifact index 90MB.

```
┌─ LOCAL (Claude Code, CPU) ────────────┐      ┌─ COLAB T4 (GPU) ──────────────┐
│ đọc 02_sources → sinh/sửa .md          │      │ git clone --depth 1            │
│ librarian.py sync   (graph/link only)  │ ─push► pip install st + faiss        │
│ KHÔNG chạy embed local                 │ .md  │ embed_index.py --build (GPU)   │
│ pull_embed_index.ps1 → .cache/         │ ◄zip─ │ zip .cache/wiki_embed.* → tải │
└────────────────────────────────────────┘      └────────────────────────────────┘
```

## Nguyên tắc

- **Source of truth = `.md`** (03_wiki + 02_sources). Đi qua git, diffable.
- **`.cache/wiki_embed.*` = artifact phái sinh.** KHÔNG commit (đã thêm vào `.gitignore`). Regenerable từ `.md`.
- **Trên Colab dùng `--build` (full), KHÔNG `--incremental`** — `mtime` đổi sau git clone nên incremental cross-machine sai. Full build e5-base ~24k vectors trên T4 chỉ vài phút.
- **Local chỉ chạy `librarian.py sync`** (nhẹ, không load model). Không chạy `embed`/`batch ...,embed` ở local.
- ⚠️ **Repo GitHub PHẢI private** — `02_sources` chứa full-text sách bản quyền.

## Setup một lần: tạo remote + push

`gh` chưa cài. Hai cách:

**Cách A — tạo repo trên web github.com (private), rồi:**
```powershell
cd "D:\AI\Wiki Link"
git remote add origin https://github.com/<USER>/<REPO>.git
git push -u origin master
```

**Cách B — cài gh rồi tạo bằng CLI:**
```powershell
winget install GitHub.cli
gh auth login
gh repo create <REPO> --private --source=. --remote=origin --push
```

> Lần push đầu ~383MB (raw sources). Sau đó chỉ push delta của `.md` đã sửa.

## Chu trình thường ngày

1. **Local:** đọc tài liệu → sinh/sửa node `.md` → `python librarian.py sync`.
2. **Local:** commit + push `.md`:
   ```powershell
   git add 03_wiki 02_sources ; git commit -m "feat: <mô tả node>" ; git push
   ```
3. **Colab:** mở `colab_embed_index.ipynb` → Runtime = T4 GPU → chạy hết cell (clone → install → `--build` → tải `wiki_embed_artifacts.zip`).
4. **Local:** đưa index về:
   ```powershell
   powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1
   ```
   (tự tìm zip trong Downloads; hoặc `-Zip <path>`)
5. **Local:** verify:
   ```powershell
   python 05_scripts\embed_index.py --stats
   ```

## Kênh trả về index (chọn 1)

- **Browser download** (mặc định trong notebook): `files.download()` zip ~90MB. Đơn giản nhất.
- **Google Drive**: bỏ comment cell cuối notebook → copy artifact vào `MyDrive/WikiLink_index/`, rồi tải/sync về local.

## Lưu ý kỹ thuật

- Model: `intfloat/multilingual-e5-base` (768-dim, đa ngôn ngữ VI+EN). Không đổi giữa local/Colab → index tương thích.
- FAISS `IndexFlatIP` (cosine qua normalized dot product).
- `embed_index.py` không cần sửa: `sentence-transformers` tự bắt CUDA trên T4.
- Sau khi pull, `semantic_search.py` / `hybrid_search.py` / `deepdive_search.py` ở local đọc `.cache/wiki_embed.*` như bình thường.
