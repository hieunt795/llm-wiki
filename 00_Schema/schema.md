# WIKI SCHEMA v2

## Nguyên tắc bất biến
1. Raw sources là source of truth. Wiki là derived artifact.
2. Mọi claim phải có citation trỏ về source cụ thể.
3. Không xóa góc nhìn trái chiều — ghi lại dưới tag `[ambiguous]`.
4. Trước khi tạo node mới, check `alias_registry.md`.

## Taxonomy: 6 loại Node

### TYPE 1 — Definition Node
- **Dùng khi:** "X là gì"
- **Template frontmatter:**
  ```yaml
  type: definition
  aliases: []
  sources: []
  confidence: high | medium | low
  provenance: extracted | inferred | ambiguous
  ```
- **Heading bắt buộc:** `## Định nghĩa`, `## Phân biệt với`, `## Nguồn`

### TYPE 2 — Mechanism Node
- **Dùng khi:** "X hoạt động như thế nào / tại sao Y xảy ra"
- **Template frontmatter:**
  ```yaml
  type: mechanism
  trigger: ""         # Điều kiện kích hoạt
  output: ""          # Kết quả
  constraints: []     # Giả định / điều kiện biên
  ```
- **Heading bắt buộc:** `## Cơ chế`, `## Điều kiện`, `## Ví dụ số`

### TYPE 3 — Relationship Node
- **Dùng khi:** "X tác động đến Y qua Z"
- **Template frontmatter:**
  ```yaml
  type: relationship
  from: "[[X]]"
  to: "[[Y]]"
  via: "[[Z]]"
  direction: unidirectional | bidirectional
  ```

### TYPE 4 — Evidence Node
- **Dùng khi:** Dữ liệu thực nghiệm, số liệu, case study
- **KHÔNG phải Concept Node** — không đưa vào `03_Wiki/concepts/`
- **Lưu trong:** `03_Wiki/evidence/`
- **Frontmatter:**
  ```yaml
  type: evidence
  date_observed: ""
  source_page: ""
  ```

### TYPE 5 — Perspective Node
- **Dùng khi:** Quan điểm riêng của một tác giả, không phải consensus
- **Frontmatter:**
  ```yaml
  type: perspective
  author: "[[Author_Name]]"
  stance: "agrees_with | contradicts | extends"
  ref_node: "[[Concept_Node]]"
  ```

### TYPE 6 — Contradiction Node
- **Dùng khi:** Hai sources nói ngược nhau về cùng một vấn đề
- **Bắt buộc có:** Ít nhất 2 citation từ 2 sources khác nhau
- **Heading bắt buộc:** `## Góc nhìn A`, `## Góc nhìn B`, `## Điểm mâu thuẫn`
- **Tag:** `#contradiction`

## Provenance Tags (dùng inline trong body)
- `[extracted]` — trích thẳng từ source, có page cite
- `[inferred]` — LLM synthesis từ nhiều sources
- `[ambiguous]` — sources không đồng ý nhau

## Citation format
`[[Book_Title.pdf#page=X]]` — trỏ thẳng trang PDF gốc
