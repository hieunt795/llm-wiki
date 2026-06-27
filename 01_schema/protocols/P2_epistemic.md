# P2 — EPISTEMIC INTEGRITY
> Load khi: kiểm tra độ tin cậy nguồn, phát hiện claim sai, xử lý mâu thuẫn.

## Thang Tin cậy (context-dependent)

### Tier 1 — RAW Sources (phân tầng theo loại)

| Nhãn | Mức tin | Định nghĩa | Folder |
|------|---------|-----------|--------|
| `[RAW-BOOK]` | ⭐⭐⭐⭐⭐ | Sách học thuật / practitioner có publisher | `books/` |
| `[RAW-OFFICIAL]` | ⭐⭐⭐⭐½ | CB, IMF, BIS, FSB, World Bank official reports | `official_reports/` |
| `[RAW-ACADEMIC]` | ⭐⭐⭐⭐ | Working papers, journal articles (có abstract + citations) | `academic/` |
| `[RAW-CLIP]` | ⭐⭐⭐ | Clipping: independent analyst, financial press, Substack | `Clipping/` |
| `[RAW-DR-LLM]` | ⭐⭐ | Deep-research output từ Gemini/ChatGPT (LLM synthesis) | `deep-research/` |
| `[RAW-OPINION]` | ⭐⭐ | Blog, op-ed, commentary không có citation rõ ràng | `Clipping/` hoặc riêng |

> **Backward-compat:** `[RAW]` không có suffix = mặc định treat như `[RAW-BOOK]`. Khi gặp node cũ dùng `[RAW]` thuần → không cần migrate ngay, chỉ update khi audit.

### Tier 2 — Derived & Synthesized

| Nhãn | Mức tin | Yêu cầu |
|------|---------|---------|
| `[WIKI]` | ⭐⭐⭐⭐ | Node + ngày updated |
| `[WEB]` | ⭐⭐⭐ | URL + ngày truy cập |
| `[LLM-D]` | ⭐⭐⭐ | **Deduction** — chain từ [RAW] facts đã verify |
| `[LLM-E]` | ⭐⭐ | **Extrapolation** — apply pattern vượt scope source |
| `[LLM-S]` | ⭐ | **Speculation** — pure inference, no source backing |
| `[UNVERIFIED]` | ⭐ | Không dùng làm luận điểm chính |

## Red Flags — Dừng lại khi thấy

| Pattern | Rủi ro | Hành động |
|---------|--------|-----------|
| `[LLM]` + số cụ thể (%, bps, $) | Hallucination số | Verify bằng [RAW]/[WEB]; nếu không có → dùng range + `[LLM — unverified figure]` |
| `[LLM]` + nhân quả mạnh ("X gây Y") | False causality | Truy cơ chế trung gian; nếu không rõ → "có thể" / "có xu hướng" |
| `[RAW-DR-LLM]` + số cụ thể | Hallucination từ LLM synthesis | MUST cross-verify với [RAW-BOOK]/[RAW-OFFICIAL] trước khi cite |
| `[RAW-CLIP]` + claim causal mạnh | Author bias / opinion | Check: có citations không? Nếu không → downgrade sang [RAW-OPINION] |
| `[RAW-CLIP]` confirm wiki node | Không phải independent verify | KHÔNG tăng `confidence` — clip có thể cite cùng nguồn gốc với book |
| Node `confidence: 1–2` | Bằng chứng yếu | Gắn `[LOW CONFIDENCE]`; không làm luận điểm trụ cột |
| Một nguồn duy nhất | Single-source risk | Ghi rõ; note chưa cross-validate |
| Số liệu không có ngày | Stale data | Gắn `[DATA: DATE UNKNOWN]` |
| Số cụ thể trong MODE DEEP | Stale data risk | MUST satisfy 1 trong 3: (A) `[WEB-YYYY-MM-DD]` verified ≤12 tháng; (B) `[RAW-YYYY]` + caveat regime check; (C) `[LLM-E]` + estimated range |

### Confidence Increment Rules (theo source type)

| Source thêm vào | Tăng confidence? | Điều kiện |
|-----------------|-----------------|-----------|
| `[RAW-BOOK]` | ✅ +1 (nếu independent) | Tác giả khác, không cite nhau |
| `[RAW-OFFICIAL]` | ✅ +1 | Luôn tính là independent |
| `[RAW-ACADEMIC]` | ✅ +1 | Nếu peer-reviewed |
| `[RAW-CLIP]` | ❌ không tăng | Có thể derive từ cùng nguồn gốc |
| `[RAW-DR-LLM]` | ❌ không tăng | LLM synthesis, không phải primary source |
| `[RAW-OPINION]` | ❌ không tăng | Commentary, không phải evidence |

## RAW Source Fallibility

RAW không phải ground truth tuyệt đối:

| Loại lỗi | Nhãn |
|----------|------|
| Sách cũ, cấu trúc thị trường đã thay đổi | `[RAW — may be superseded]` |
| Hai RAW mâu thuẫn nhau | → Contradiction Protocol (xem dưới) |
| Bị bác bỏ thực nghiệm sau này | `[RAW — empirically contested]` |
| Author bias rõ ràng (trường phái) | Gắn nhãn trường phái; đặt cạnh quan điểm đối lập |

## Contradiction Protocol

```
Khi hai nguồn mâu thuẫn:
  → KHÔNG chọn một bên và im lặng bên kia
  → Trình bày: [Quan điểm A — Nguồn X] + [Quan điểm B — Nguồn Y]
  → Xác định: điều kiện mà A đúng / B đúng
  → Nếu chưa có node → SPAWN 03_wiki/contradictions/
```

## Self-Correction
```
Nếu bị phản bác → không defensive → kiểm tra nguồn gốc claim
[LLM] bị sai → thừa nhận, tìm [RAW]/[WEB] ngay
[RAW/WIKI] bị nghi sai → đọc lại context, cross-validate
Phát hiện sai → update node + log vào 01_schema/log.md
```

## LLM Tier Reference

| Tag | Tên | Khi nào dùng |
|-----|-----|--------------|
| `[LLM-D]` | Deduction | Suy luận logic từ RAW/WIKI đã verify — chuỗi A→B→C rõ ràng |
| `[LLM-E]` | Extrapolation | Áp dụng pattern học được ra ngoài scope source; cần caveat |
| `[LLM-S]` | Speculation | Không có source backing; PHẢI explicit label; không làm luận điểm chính |

Rule: `[LLM-S]` + số cụ thể = hard block. Phải convert sang [LLM-E] + estimated range hoặc skip.
