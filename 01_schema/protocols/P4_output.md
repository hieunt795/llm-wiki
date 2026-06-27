# P4 — OUTPUT STANDARD
> Load khi: cần chi tiết format response, diagram, source labels.

## 6-Step Masterclass Structure (Mode A)

| Bước | Nội dung | Ghi chú |
|------|---------|---------|
| 1. CORE THESIS | 1 đoạn, thuật ngữ kỹ thuật, bản chất vấn đề | Không ẩn dụ |
| 2. INTEGRATED PROSE | 3–4 đoạn chuỗi nhân quả, biến số tăng/giảm/dịch chuyển | Trung tính, không giật gân |
| 3. VISUAL/DIAGRAM | Chỉ khi cơ chế phức tạp hoặc có yêu cầu | Optional |
| 4. EXPERT SYNTHESIS | ≥3 lenses từ 13 Master Models, cite `[RAW] File:page` | Bắt buộc |
| 5. WORKED EXAMPLE | Lượng hóa bằng số thực tế | Gắn nhãn [LLM] nếu số chưa verify |
| 6. FAILURE CONDITIONS | Điều kiện biên — khi nào mô hình thất bại | Bắt buộc |

Kết thúc mọi response Mode A: **WRITEBACK** + **NEXT IDEA**.

## Source Labels
```
[RAW]        — Trích dẫn trực tiếp từ tài liệu gốc (file:page)
[WIKI]       — Node đã tổng hợp (node_name / YYYY-MM-DD)
[WEB]        — Nguồn web đã fetch (URL / ngày)
[LLM]        — Suy luận nội sinh, chưa citation
[UNVERIFIED] — Chưa đối chiếu bất kỳ nguồn nào
[extracted]  — Rút trực tiếp từ raw, chưa diễn giải
```

## Multi-Source Citation Rules

**Nguyên tắc:** Mỗi claim phải mang tất cả nguồn xác nhận nó — không chỉ nguồn đầu tiên.

### Inline citation — cùng đoạn văn
Khi ≥2 nguồn đồng quan điểm về cùng một claim, cite tất cả ngay cuối câu đó:
```markdown
[WIKI] Fiscal dominance xảy ra khi CB bị kẹt bởi danh mục trái phiếu quá lớn,
buộc phải ưu tiên ổn định tài khóa hơn chống lạm phát.
[[Fixed_Income_During_Ch10.md#page=9]] [[Perry_Warjiyo_CB_Policy.md#page=142]]
```

### Evidence / Source Anchors section — liệt kê đầy đủ
```markdown
## Evidence / Source Anchors

- [[During_Ch10.md#page=9]]     — định nghĩa mất độc lập do danh mục trái phiếu lớn
- [[Perry_CB_Policy.md#page=142]] — cơ chế fiscal dominance trong context EMEs
- [[Tuckman_Serrat.md#page=88]]  — yield impact khi CB buộc hold to maturity
```

### Confidence scaling
| Số nguồn độc lập đồng thuận | `confidence` |
|-----------------------------|-------------|
| 1 nguồn                     | 1–2         |
| 2 nguồn                     | 3           |
| 3+ nguồn                    | 4–5         |
| Nguồn mâu thuẫn nhau        | Tạo `type: contradiction` node riêng |

### Khi 2 nguồn đồng quan điểm nhưng diễn đạt khác nhau
Giữ cả 2 góc nhìn trong body, không gộp thành 1 câu:
```markdown
[RAW] During (Ch.10): "CB loses independence when sovereign bond portfolio exceeds..."
[[During_Ch10.md#page=9]]

[RAW] Perry (p.142): "Fiscal dominance emerges when debt monetization becomes
the path of least resistance for the treasury..."
[[Perry_CB_Policy.md#page=142]]
```
Sau đó tổng hợp thành `[WIKI]` ở đoạn kết section, cite cả 2.

## Diagram Types (ASCII Art)

| Tên chuẩn | Dùng khi |
|-----------|---------|
| Transmission Flow | Chuỗi nhân quả đa bước |
| Accounting T-Account | Tác động kế toán kép |
| Capital Waterfall | Phân tầng rủi ro |
| Feedback Spiral | Cơ chế tự củng cố |

## Mode B — Wiki Node Format

### Frontmatter (chuẩn thực tế)
```yaml
---
title: "Human-readable title"
aliases:
- Tên tiếng Việt
- Tên viết tắt
type: concept|definition|mechanism|relationship|convention|perspective|evidence|domain|glossary|contradiction|synthesis
tags:
- tag1
- tag2
status: draft|reviewed|verified|stale|archived|conflict
confidence: 1-5
expert_lens: "Author1 | Author2"
thesis: "ONE sentence: core transmission claim"
provenance: extracted|expanded|LLM|synthesized
chapter: N                      # số chương trong sách gốc (nếu có)
source_refs:
  - file: "Filename.md"
    page: X
  - file: "Filename2.md"        # thêm entry khi có nguồn thứ 2+
    page: Y
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Body (linh hoạt theo type)
```markdown
# [[Node_Title]]

## Thesis
[WIKI/LLM] 1–2 câu core claim.

## Definition          ← dùng nếu type: definition
## Mechanism           ← dùng nếu type: mechanism
### Sub-section        ← thoải mái mở rộng theo topic

## Worked Example
[LLM/RAW] Ví dụ lượng hóa bằng số thực tế.

## Evidence / Source Anchors
- [[File.md#page=X]] — mô tả ngắn nội dung trích dẫn.

## [Topic-specific sections]   ← tự do thêm khi cần
## Related
- [[Node_A]]
- [[Node_B]] — ghi chú quan hệ nếu cần
```

### Rules
- **Trường cứng:** `title`, `type`, `status`, `confidence`, `thesis`, `source_refs`, `created`, `updated`
- **Trường mềm:** `chapter`, `provenance`, `aliases` — thêm khi có thông tin
- **Multi-source:** `source_refs` là array — **append**, không overwrite. Tăng `confidence` khi ≥2 nguồn độc lập xác nhận.
- **Inline citation:** dùng `[[File.md#page=X]]` ngay sau câu cần cite, không để cuối section.
- **Labels bắt buộc trên mỗi đoạn:** `[WIKI]` / `[LLM]` / `[RAW]` / `[extracted]` — không để đoạn nào không có label.
- **Body không cứng 4 sections** — chỉ `## Thesis` và `## Related` là bắt buộc. Các sections còn lại mở rộng theo nhu cầu của topic.
