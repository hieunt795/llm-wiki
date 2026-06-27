# system.md — Wiki Link Operational System

MANDATORY: All agents MUST read this file before starting work.
Load order: CLAUDE.md → hot.md → memory.md → system.md → domain protocols
This document contains hard rules (BLOCK 0), identity (BLOCK 1), output modes (BLOCK 2), session checklist (BLOCK 3), pointer map (BLOCK 4).

---

## BLOCK 0: Hard Rules (Non-Negotiable)

1. Read system.md first — before any session starts, agents must load this file + hot.md
2. Librarian.py is the SOP — all wiki/graph/search operations go through it, never direct file manipulation
3. Rule 0 (Pre-ingest) — always wiki_search before creating nodes (prevent duplicates, see memory/rule_0_pre_check.md)
4. Incremental embedding — always use python librarian.py embed --incremental (never full rebuild unless necessary)
5. Triad Discipline (MPT) — Mọi phân tích phải đi qua bộ lọc 3 tầng:
   - Macro: Xác định chế độ (Regime) và neo chính sách (Policy Anchor).
   - Plumbing: Truy vết T-account và các ràng buộc kỹ thuật (Operational Mechanics).
   - Treasury: Trích xuất tác động vận hành và logic thực thi cho thực tế (Practitioner Logic).
6. Node quality gates — thesis field is required; confidence must be labeled per memory/strict_ingest_rules.md
7. No destructive shortcuts — never force-delete files, use librarian.py rename or validate to heal links first
8. Git commits require context — include why in commit message, not just what

9. Treasury Insight Requirement — Every analytical output or wiki node expansion must include a "Treasury Insight" section, translating mechanical plumbing into practitioner logic (e.g., "So what for the Treasury desk?").
10. TQN Lens Priority — Prioritize the "Trần Quang Nghĩa (TQN)" practitioner lens for all operational mechanics, focusing on T-Account tracing and liquidity narratives.
11. Linguistic Sobriety — Strictly forbid journalistic, marketing, or metaphorical language. Sử dụng văn phong thuần túy kỹ thuật, phân tích và khô khan.

    Prohibited — General: "thực chiến", "phản ứng sinh tồn", "nhiệt kế", "vũ khí", "giật tít", "bottom line", "in real time", và bất kỳ tính từ biểu cảm nào.

    Prohibited — FX/Macro domain (common violations):
    - Gaming framing: "Kill", "Double Kill", "Kill 1/2", "wins/loses the window"
    - Combat metaphor: "arms race", "vũ khí tài chính", "bóp speculative positions"
    - Journalistic labels: "Macro trap", "deferred reckoning", "tipping point"
    - Wordplay: "buy time / buy credibility", "loop tightens"
    - Filler phrases: "in real time", "bottom line", "at the end of the day"

    Substitution principle: replace emotive framing with mechanism description.
    ❌ "Double Kill bóp speculators"
    ✅ "delayed sterilization creates dual tightening: spot FX effect + reserve drain effect"

---

## BLOCK 1: Identity & Context

System Role: Wiki Link is a dual-mode knowledge system:
- Mode SYNTHESIS: Ingest raw academic sources (books, papers) → wiki nodes (concepts, mechanisms, rationales)
- Mode DEEP: Analyze financial systems using "Treasury-First" plumbing logic (who moves, why, what breaks).

Current Phase: Ingest Phase 2 (Choudhry, Tuckman core expansion) — 11% coverage → 42% target in 12 weeks (see memory/ingest_plan_2026.md)

---

## BLOCK 2: Output Modes

MODE SYNC (lightweight, operational)
- Command: python librarian.py sync

MODE SEARCH (query-response)
- Commands: python librarian.py search <query> [--deep | --semantic]

MODE INGEST (workflow orchestration)
- Commands: python librarian.py stage --dry-run / review / ingest

MODE DEEP (Plumbing-First Synthesis)
- Template: 01_schema/templates/T_MODE_DEEP.md
- 5 Lenses (bắt buộc đủ): Top-down → Macro → Plumbing → Treasury → Timing
- 8 Blocks: Top-Down Entry → Macro Layer → Plumbing Layer → Treasury Layer → Timing Layer (Past/Present/Future) → Feedback/Boundary → Diagram → Conclusion → Next Steps
- Timing là cross-cutting layer — tổng hợp qua toàn bộ analysis, không phải bước tuần tự.
- Diagram: ASCII Art linh hoạt — chọn dạng phù hợp với cơ chế (T-Account, Transmission chain, Feedback loop, Flow diagram, Capital waterfall), không cố định.
- Lens chuyên môn (TQN, Tuckman, Choudhry, v.v.) dùng linh hoạt theo ngữ cảnh trong từng layer.
- Protocol refs: P3_mechanistic · P4_output · P1_awareness

---

## BLOCK 3: Session Checklist (Start Every Session)

[ ] Read system.md (this file) + hot.md (current context)
[ ] Load memory (01_schema/memory.md + memory/ directory for persistent state)
[ ] Check ingest status: python librarian.py status (staged count, stale count, orphans)
[ ] Load relevant domain protocol (if analysis task): SPEC_SEARCH_V1.md, Audit_Protocol.md, VIS_Protocol.md
[ ] Verify librarian.py is in path: python librarian.py help
[ ] If embedding work: confirm manifest exists: ls .cache/wiki_embed.manifest.json

---

## BLOCK 4: Pointer Map (Where Things Live)

CRITICAL FILES (Agents Must Read):
- 01_schema/hot.md — current session context + active tag (read every session)
- 01_schema/memory.md — persistent state index (check for relevant memories)
- 01_schema/schema.md — node frontmatter spec (read when creating nodes)
- memory/rule_0_pre_check.md — mandatory pre-ingest search check
- memory/workflow_triad_analysis.md — triad analytical discipline (Macro-Plumbing-Treasury)
- memory/workflow_plumbing_analysis.md — plumbing-first analytical discipline
- memory/ingest_plan_2026.md — ingest roadmap (Phase 1-3 coverage targets)

LIBRARIAN.PY CORE COMMANDS:
- status: quick overview (start of session)
- sync: after file edits, before git commit
- search <query>: before SPAWN node, verify concept doesn't exist
- search --deep: deep research, thin coverage detection
- embed --incremental: after node creation (ALWAYS incremental, never full rebuild)
- embed --stats: check vector index size + model
- wisdom <tag>: synthesis after ingesting a chapter
- audit <file>: before merge, F.I.T.S.E.R.B.V.L 9-point check
- ingest: post-ingest sync (graph + index + bridge + staleness)
- health: periodic check (orphans + stale + missing thesis)
- batch sync,embed: chain multiple pipelines

DIRECTORIES:
- 03_wiki/ — wiki nodes (concepts, mechanisms, rationales)
- 02_sources/ — raw PDF markdown extracts
- 04_outputs/staged_nodes/ — candidates before merge to 03_wiki
- 04_outputs/research/ — wisdom synthesis reports
- .cache/ — FAISS index + manifest (auto-managed by embed --incremental)
- 05_scripts/ — Python pipeline scripts

---

## BLOCK 5: Key Decision: Why Incremental Embed?

Librarian tracks file mtime in .cache/wiki_embed.manifest.json:
- First run: full build (encode all files) + create manifest
- Subsequent runs: only encode changed/new files
- Result: saves 80% time when adding/editing a few nodes vs. hundreds

Always use: python librarian.py embed --incremental
Never use: python librarian.py embed --build (full rebuild only if manifest corrupted)

---

## Version

- system.md v1.0 — May 8, 2026
- librarian.py v2.1 — incremental embed support, batch orchestration
- Next review: June 8, 2026 (post-Phase 2 Choudhry ingest)

---

END OF SYSTEM.MD

Agents: Load this file FIRST before starting work. Then load hot.md + memory/ directory for context.
