# CLAUDE.md — Wiki Link System Prompt
> Agent: Claude (claude-sonnet-4-6 / claude-opus-4-6)
> Load order: CLAUDE.md → 01_schema/hot.md → 01_schema/memory.md → system.md → protocols on-demand
> Core SOP: defined in `system.md` — rules, output modes, checklist, pointer map all live there.
> Analytical discipline: **5 Lenses** — Top-down · Macro · Plumbing · Treasury · Timing

## Claude-Specific Notes

**MANDATE: Top-down → Macro → Plumbing → Treasury → Timing**
- Every MODE DEEP analysis must integrate all 5 lenses in sequence.
- Top-down sets the frame. Macro locks the regime. Plumbing grounds the mechanism. Treasury translates to practitioner logic. Timing synthesizes Past/Present/Future across all layers.
- **Plumbing 4-Component Discipline (within Plumbing Layer):** (1) Entity + Flow Tracing | (2) Stakeholder Impact Matrix | (3) Liquidity Narrative Discovery | (4) Asset Price Mechanical Linkage
- **MODE DEEP structure:** Top-Down Entry → Macro Layer → Plumbing Layer → Treasury Layer → Timing Layer (Past/Present/Future) → Feedback/Boundary → Diagram → Conclusion → Next Steps
- Template: `01_schema/templates/T_MODE_DEEP.md`

**Search escalation (no Graphify CLI):**
- Fast lookup: `wiki_search` (BM25 boost)
- Deep synthesis: `hybrid_search` (raw heatmap) → `deepdive_search` (thin detection → drill)
- CLI alternative: `python librarian.py search "<query>" --deep`

**Read Discipline — Two-Pass Pattern (token efficiency):**
- Pass 1 — Locate: chạy search phù hợp, chỉ đọc output tóm tắt để quyết định có cần đọc tiếp không.
  - Keyword/BM25: `librarian.py search` hoặc `Grep` → file path + line number + thesis line
  - Semantic: `librarian.py search --semantic` → ranked node list với title + thesis + similarity score
  - Đủ để quyết định node nào liên quan — không đọc full content ở bước này.
- Pass 2 — Expand (chỉ khi Pass 1 xác nhận cần):
  - Giới hạn cứng: đọc tối đa 2 nodes mỗi query cycle. Ưu tiên: score cao nhất + type=WIKI trước.
  - Nếu thesis line từ Pass 1 đã đủ rõ để trả lời → dừng lại, không cần đọc file.
  - Keyword hit → wiki node (03_wiki/): `Read(file, offset=line-3, limit=40)` → đọc section xung quanh match
  - Keyword hit → raw node (02_sources/): `Read(file, offset=line-3, limit=40)` → đọc đoạn xung quanh match, không đọc cả chapter
  - Semantic hit → wiki node: `Read(file, limit=60)` → đọc từ đầu node (frontmatter + thesis + mechanism)
  - Semantic hit → raw node: `Read(file, offset=match_area, limit=60)` → đọc đoạn gần nhất với query, không đọc từ đầu file
- Không dùng `Read` trên toàn file trừ khi Pass 1 xác nhận toàn bộ file đều cần thiết.
- Mục tiêu: lấy đúng signal, không load boilerplate.

**CLAUDE.md is intentionally minimal.** Load `system.md` for full SOP (BLOCK 0–4).

---

<!-- FULL SOP: READ system.md -->
<!-- system.md contains: BLOCK 0 Hard Rules | BLOCK 1 Identity | BLOCK 2 Output Modes | BLOCK 3 Session Checklist | BLOCK 4 Pointer Map -->
