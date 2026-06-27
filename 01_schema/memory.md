# WIKI LINK — Operational Memory (v4.7)
> **Lazy Loading Architecture:** system.md (TIER 0, ~100 lines) → hot.md + memory.md (session start) → protocols/workflows (on-demand via Pointer Map).
> Cập nhật file này qua W4_memory.md protocol.


## 1. User Preferences
- **Response Standard:** 3-mode adaptive framework (system.md BLOCK 2):
  - **MODE FLASH** — factual/definition: BLUF + Evidence + Number. Ngắn gọn.
  - **MODE DEEP** — mechanism/transmission: **RCL skeleton** (Regime Lock → Causal Chain [inline conditions] → Feedback Topology → Channel Interaction → Quantified Anchor → Boundary Conditions). SCQA logic trong prose. ≥3 expert lenses.
  - **MODE SCAN** — landscape/thematic: wisdom output + pattern annotation + gaps.
- **Tone:** Trung lập, kỹ thuật, phân tích. Tuyệt đối không sử dụng ngôn ngữ báo chí, từ ngữ giật gân, hoặc các tính từ cảm xúc/quảng cáo. **CẤM TUYỆT ĐỐI** các cụm từ mang tính "kêu" hoặc "giật tít" như: "thực chiến", "phản ứng sinh tồn", "vũ khí sắc bén", "cú đấm thép", "nhiệt kế", "ống dẫn" (trừ khi là thuật ngữ kỹ thuật chuyên ngành), "sức hút", "câu kéo", hoặc bất kỳ thuật ngữ nào mang tính ẩn dụ báo chí. Ngôn ngữ phải thuần túy mô tả cơ chế kỹ thuật và định lượng.
- **Sourcing Ratio (Priority):** 70% RAW Source / 30% WIKI. Ưu tiên đào sâu vào `02_sources/` vì wiki hiện tại mức độ ingest chưa cao.
- **Causal Chain format:** `X →[điều kiện A]→ Y →[điều kiện B]→ Z` với confounders explicit tại mỗi arrow.
- **Expert Lenses Extension:** 
  - **Trần Quang Nghĩa (TQN):** Lăng kính Practitioner TỐI THƯỢNG cho Operational Mechanics.
  - **MANDATORY OPERATIONAL CHECKLIST (for MODE DEEP Synthesis):**
    1. **Institutional Mapping (The Plumbing):** Xác định các thực thể và trace dòng tiền. Phải làm rõ **tác động cụ thể lên từng bên** (ai được, ai mất?).
    2. **Balance Sheet Tracing (T-Account):** Sử dụng bảng T-Account để giải thích biến động Asset/Liab.
    3. **Narrative Discovery (The Story):** Dựa trên dòng chảy thực tế (MB delta, RO lag) để xác định "câu chuyện" thực sự đằng sau giá cả.
    4. **Asset Price Linkage:** Kết nối trực tiếp sự thay đổi thanh khoản với biến động giá tài sản (Price Prediction).
- **Visuals:** Chỉ sử dụng sơ đồ (Transmission Flow, T-Account) khi thực sự phức tạp hoặc có yêu cầu.
- **Search Logic:** Sử dụng **Hybrid Search v2.5** (Fuzzy + Heatmap + Parallel Scouting) làm chuẩn.
- **Thematic Query:** Với câu hỏi dạng landscape/thematic → chạy `auto_synthesis.py "<tag>" --no-llm` trước để lấy Hub Map + Tension Pairs, rồi mới drill chi tiết bằng hybrid_search.
- **CURRENTLY LAYER (bắt buộc):** Trước mọi query về monetary policy / regulatory / market data / macro — chạy web search để check breaking news. Nếu có update → inject `[CURRENTLY — YYYY-MM-DD]` section vào response trước SYNTHESIS. Nếu news mâu thuẫn wiki → flag `⚠️ [STALE SIGNAL]` + `[INGEST CANDIDATE]`. Xem W1_query.md Giai đoạn 0 để biết đầy đủ trigger conditions.
- **NEXT STEPS (bắt buộc cuối mỗi response):** Luôn kết thúc bằng 2 phần: (A) 2–3 Deep Dive Ideas — node/tension cụ thể từ wiki graph đáng phân tích tiếp, có lý do rõ ràng; (B) 1–2 System Actions — lệnh cụ thể có thể chạy ngay (ingest/search/synthesis/bridge/audit). Không viết chung chung — phải dẫn tên node thực tế và lệnh thực tế.

## 2. Technical Fixes (Windows/CLI)
- **Search Tool:** Sử dụng `findstr /I /N` thay vì `grep` trên Windows để lấy Line Numbers chính xác.
- **Encoding:** Cẩn thận với các file UTF-16; luôn dùng cơ chế `read_file_safe` trong các script Python.
- **Text Merging:** Lỗi dính chữ từ PDF được xử lý bằng cơ chế **Sub-string Detection** trong `hybrid_search.py`.
- **Source Diversity:** Đã tích hợp **Source Clustering** vào `wiki_search.py` để tránh một bộ sách chiếm sóng kết quả.

## 3. Analytical Truths (Validated Logics)
- **Vietnam Node:** LDR (85%) và SML (30%) là các "vách ngăn" thanh khoản quan trọng nhất giữa Market 1 & 2.
- **Modern Era:** Hệ thống đang chuyển dịch sang **Multi-curve framework** (OIS Discounting) và Basel III (CAR 10.5%).
- **Shadow Banking:** Private Credit tại VN đang trở thành ranh giới mới của rủi ro truyền dẫn qua cơ chế PIK và SRT.

## 4. Active Debt
- [ ] Ingest nốt Batch 3 về "Price Discovery" của báo cáo Private Credit.
- [ ] Cập nhật số liệu 2026 (Import Cover < 3M, CAR 10.5%
- [ ] Fix missing thesis: `VaR_Shock_Feedback_Loop` (tag: fixed-income, detected 2026-04-26)
- [ ] Fix missing thesis: `Financial_Repression` (tag: monetary-policy, detected 2026-04-26)
- [ ] Fix missing thesis: `Search_For_Yield_Channel` (tag: monetary-policy, detected 2026-04-26)
- [ ] Fix missing thesis: `Global_Drivers_Of_Private_Credit` (tag: monetary-policy, detected 2026-04-26)

## 4b. Raw Source Ingestion Plan (Added 2026-05-06)
**Status:** 341/3,123 sections ingested (10.9% complete). See [[04_outputs/temp/raw_sources_ingest_planning.md]].

**Coverage by book:**
- **HIGH (20%+):** Perry Warjiyo (28.5%), Howard Corb (24.1%), Düring (22.2%), Schofield (20.9%)
  - **Phase 1 Action:** Complete these 4 → +121 nodes → 18.8% total (2–4 weeks)
- **MEDIUM (5–20%):** Choudhry (12.3%), Tuckman (11.5%), Bondistan (15.3%), CBbalance (18.6%)
  - **Phase 2 Action:** Expand Choudhry (278 uncovered) + Tuckman (54) → +332 nodes → 29.4% total (4–8 weeks)
- **LOW (<5%):** Wilmott (173), Singh (158), Homer-Leibowitz (93), ACI (489), Neftci (70), others
  - **Phase 3 Action:** Specialized depth (8+ weeks)

**Scout command:** `python librarian.py scout --mode lines --n 10` (random uncovered sections)
**Coverage report:** `python librarian.py stage --list-coverage`
**Next ingest priority:** Perry Warjiyo (28.5% done, 181 remain) or Choudhry (278 large unexplored source)

## 5. Upgrade Roadmap (drafted 2026-04-26)

### SPRINT 1 — Schema Refactor (ưu tiên cao, ~2–3 giờ)
- [ ] Thêm `status` (5-state: draft→reviewed→verified→stale→archived) vào frontmatter schema
- [ ] Thêm `superseded_by` + `superseded_date` vào frontmatter schema
- [ ] Thêm `half_life_years` vào frontmatter (mechanism: 10, regulation: 1, market-data: 0.1)
- [ ] Cập nhật `01_schema/schema.md` với 3 fields mới
- [ ] Cập nhật `claim_auditor.py`: check status + superseded_by trong step S và V

### SPRINT 2 — Search Upgrade (~2 giờ)
- [ ] Recency weighting trong `wiki_search.py`: `score × exp(-λ × days/365)`, λ lấy từ `half_life_years`
- [ ] Extend `gen_index.py` để sinh thêm `_index.md` per category directory (mechanisms/, concepts/, etc.)

### SPRINT 3 — Knowledge Compounding (~2 giờ)
- [ ] Synthesis archiving: sửa `auto_synthesis.py` writeback để tạo node trong `03_wiki/syntheses/`
      với frontmatter: type:synthesis, tags, related_hubs — để vào graph, searchable
- [ ] Viết `rename_node.py`: đổi tên file → search-replace [[OldName]] → librarian sync
      Tích hợp vào Librarian: `python librarian.py rename OldName NewName`

### SPRINT 4 — Deep Research Pipeline (ưu tiên cao, ~3 giờ)
- [ ] Thêm pipeline `deepdive` vào `librarian.py`
      Flow: wiki_search → quality gate (confidence≤2 OR [LLM]>0 OR no source_refs)
            → hybrid_search raw → exact_extractor passages → in draft expansion proposal
      Usage: `python librarian.py deepdive "taralac facility"`
- [ ] Cập nhật `scripts_ref.md` + `help` data trong librarian.py

### SPRINT 5 — Web Search Integration (ưu tiên trung bình, ~2 giờ)
- [ ] Ephemeral tier: cite web inline as `[WEB-YYYY-MM-DD:url]`, không persist vào wiki
- [ ] Ingest-flagged tier: khi web result có giá trị dài hạn → append `[INGEST CANDIDATE: url]`
      cuối response để queue vào W2 workflow
- [ ] Trigger condition: query chứa market data/regulatory threshold HIỆN HÀNH
      HOẶC wiki top-3 results đều có confidence ≤ 2
- [ ] Cập nhật W1_query.md: thêm nhánh web-search fallback sau deepdive

### FUTURE (sau Topic 06)
- [ ] 4-factor confidence scoring: source_count(0.3)+source_quality(0.3)+recency(0.2)+cross_refs(0.2)
      Cần định nghĩa source quality taxonomy trước: [RAW-CB]>[RAW-academic]>[RAW-practitioner]>[WEB]
- [ ] Vector search layer (FAISS local) thêm vào wiki_search.py làm semantic tiebreaker
- [ ] Watch mode: Python watchdog auto-trigger `librarian sync` khi wiki file thay đổi

- [ ] Fix missing thesis: `Policy_Response_to_Shocks` (tag: monetary-policy, detected 2026-04-29)