# W3 — DEEP RESEARCH FLOW
> Load khi: viết research report, whitepaper, hoặc deep-dive analysis.

## Phase R0 — Thesis Lock
- **R0.1 Parsing:** Extract Framework, Output Format, Writing Style, Data Requirements từ prompt.
- **R0.2 Thesis Lock:** Chốt Core Thesis (1 câu) + Null Hypothesis. **Thesis KHÔNG thay đổi sau bước này.**

## Phase R1 — Internal Research (Wiki + Raw)
```
[R1.0 — WISDOM PRE-SCAN] Nếu query có tag rõ ràng:
  → python 05_scripts/auto_synthesis.py "<tag>" --no-llm
  → Đọc: Hub Map (God Nodes) + Tension Pairs
  → Mục đích: biết trước structural skeleton trước khi drill chi tiết
  → Ghi nhận: top 3 hubs → dùng làm anchor trong synthesis

[R1.1 — DETAIL DRILL]
Scan 01_schema/index.md → tìm nodes liên quan
Chạy hybrid_search.py "<thesis keywords>"
Map nodes vào framework
Lập GAP LIST: những dữ liệu/phân tích wiki không cung cấp được
```

> **Khi nào bỏ qua R1.0:** Query về một node cụ thể (không phải thematic). Ví dụ "giải thích Barro-Gordon" → bỏ qua, dùng hybrid_search thẳng.

## Phase R2 — External Research (Web)
- Chỉ tìm để lấp GAP LIST — không expand scope
- Ưu tiên nguồn: Central Bank > IMF/BIS/World Bank > Academic > Financial Press
- **Bắt buộc:** cite đầy đủ tên nguồn + ngày + URL

## Phase R3 — Synthesis & Output
- Enforce Writing Style và Constraints từ R0
- Gắn **CONFIDENCE TIER** cho toàn báo cáo:
  ```
  TIER A: ≥3 RAW sources cross-validated
  TIER B: 1-2 RAW + WIKI
  TIER C: WIKI + WEB
  TIER D: LLM-dominant — cần review
  ```

## Phase R4 — Post-Report Writeback
- Xử lý Writeback Queue vào Wiki/Schema
- Cập nhật `01_schema/log.md`
- Giới hạn: 3 writebacks/session
