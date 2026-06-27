# GEMINI.md — Wiki Link System Prompt
> Agent: Gemini (gemini-2.0-flash / gemini-2.5-pro)
> Load order: GEMINI.md → 01_schema/hot.md → 01_schema/memory.md → system.md → protocols on-demand
> Core SOP: defined in `system.md` — rules, output modes, checklist, pointer map all live there.
> Analytical discipline: **5 Lenses** — Top-down · Macro · Plumbing · Treasury · Timing

## Gemini-Specific Notes

**MANDATE: Top-down → Macro → Plumbing → Treasury → Timing**
- Every MODE DEEP analysis must integrate all 5 lenses in sequence.
- Top-down sets the frame. Macro locks the regime. Plumbing grounds the mechanism. Treasury translates to practitioner logic. Timing synthesizes Past/Present/Future across all layers.
- **Plumbing 4-Component Discipline (within Plumbing Layer):** (1) Entity + Flow Tracing | (2) Stakeholder Impact Matrix | (3) Liquidity Narrative Discovery | (4) Asset Price Mechanical Linkage
- **MODE DEEP structure:** Top-Down Entry → Macro Layer → Plumbing Layer → Treasury Layer → Timing Layer (Past/Present/Future) → Feedback/Boundary → Diagram → Conclusion → Next Steps
- Template: `01_schema/templates/T_MODE_DEEP.md`

**Knowledge graph + structural search:**
- Read `graphify-out/GRAPH_REPORT.md` before answering architecture/codebase questions.
- Navigate via `graphify-out/wiki/index.md` if available (prefer over raw files).
- After code edits: `graphify update .` to sync graph (AST-only, no cost).
- Structural queries: `graphify query "<query>" --budget 800` → semantic → wiki_search → hybrid_search

**Search bias:** `wiki_search` favors wiki (BM25 ×4–5), `semantic_search` favors raw (volume). Use `--deep` to balance both.

**Read Discipline — Two-Pass Pattern (token efficiency):**
- Pass 1 — Locate: chạy search phù hợp, chỉ đọc output tóm tắt để quyết định có cần đọc tiếp không.
  - Keyword/BM25: `librarian.py search` hoặc `Grep` → file path + line number + thesis line
  - Semantic: `librarian.py search --semantic` → ranked node list với title + thesis + similarity score
  - Nếu thesis line từ Pass 1 đã đủ rõ để trả lời → dừng lại, không cần đọc file.
  - Đủ để quyết định node nào liên quan — không đọc full content ở bước này.
- Pass 2 — Expand (chỉ khi Pass 1 xác nhận cần):
  - Giới hạn cứng: đọc tối đa 2 nodes mỗi query cycle. Ưu tiên: score cao nhất + type=WIKI trước.
  - Nếu ReadFile tool không hỗ trợ offset/limit → dùng Grep trước để locate section, rồi mới ReadFile.
  - Keyword hit → wiki node (03_wiki/): Grep section heading → ReadFile giới hạn vùng liên quan
  - Keyword hit → raw node (02_sources/): Grep match line → ReadFile đoạn xung quanh, không đọc cả chapter
  - Semantic hit → wiki node: ReadFile node đó (wiki node thường ngắn, chấp nhận được)
  - Semantic hit → raw node: Grep keyword trong file trước → chỉ đọc đoạn match, không đọc từ đầu file
- Không đọc toàn file raw node trừ khi Pass 1 xác nhận toàn bộ file đều cần thiết.
- Mục tiêu: lấy đúng signal, không load boilerplate.

**GEMINI.md is intentionally minimal.** Load `system.md` for full SOP (BLOCK 0–4).

---

<!-- FULL SOP: READ system.md -->
<!-- system.md contains: BLOCK 0 Hard Rules | BLOCK 1 Identity | BLOCK 2 Output Modes | BLOCK 3 Session Checklist | BLOCK 4 Pointer Map -->
