# WIKI LINK SYSTEM COMMANDS (--Help)

Sử dụng các lệnh và từ khóa sau để kích hoạt các quy trình tự động của Agent:

## 1. Quy trình Ingestion & Audit
- **"Audit [file]"**: Thực hiện quy trình đối soát 10 bước F.I.T.S.E.R.B.V.L.
- **"Ingest [file]"**: Sau khi Audit, thực hiện nạp dữ liệu, tạo node và build lại graph.
- **"Systemic Audit"**: Yêu cầu Agent truy hồi toàn bộ Wiki + Raw để đánh giá một luận điểm phức tạp.

## 2. Các Framework Tư duy (Keywords)
- **"F.I.T.S.E.R"**: Trục logic cơ bản (Fit, Inconsistency, Tension, Synthesis, Edge, Risk).
- **"Institutional Divergence"**: Phân tích đặc thù cấu trúc ("Nhà tôi khác nhà ông").
- **"Temporal Variance"**: Phân tích đặc thù thời điểm ("Nay khác xưa").
- **"3-Tier Thinking"**: Yêu cầu bóc tách theo tầng Data -> Structure -> Philosophy.

## 3. Các bước chốt chặn (Guardrails)
- **"Validation Post"**: Thiết lập mốc số liệu kiểm chứng tương lai.
- **"Bias Check"**: Kiểm định thiên kiến và agenda của nguồn tin.
- **"Link Healing"**: Tự động rà soát các node liên quan để cập nhật sự thay đổi.

## 4. Scripts hỗ trợ (Dành cho Terminal)
- `python librarian.py help`: Hiển thị toàn bộ pipelines hiện có.
- `python librarian.py stage --dry-run`: sample uncovered sections để ingest.
- `python librarian.py extract --book perry --skip-existing`: extract PDF -> Markdown.
- `python librarian.py scout --mode lines --n 10`: random raw discovery.
- `python librarian.py section --dir ... --heading ... --out ...`: surgical extraction.
- `python 05_scripts/system_tools.py --help-cmd`: Hiển thị bảng lệnh hệ thống.
- `python 05_scripts/wiki_search.py "[query]"`: Tìm kiếm semantic nhanh.
- `python 05_scripts/_build_wiki_graph.py`: Cập nhật lại toàn bộ liên kết Wiki.

---
**Lưu ý:** Nếu bạn quên bất kỳ bước nào, chỉ cần gõ `--Help`, tôi sẽ hiển thị lại bảng này.
