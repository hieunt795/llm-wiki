# Wiki Link — Librarian Modularization (As-Built)

> Tài liệu này mô tả phần module hóa **đã triển khai thực tế** cho `librarian.py` trong repo hiện tại.

---

## 1. Mục tiêu

Tách `librarian.py` monolith thành các module có ranh giới rõ ràng nhưng vẫn giữ nguyên contract chạy:

```text
python librarian.py <command> ...
```

Không thay đổi SOP của repo. Không đổi tên command. Không ép sửa các script engine trong `05_scripts/`.

---

## 2. Cấu trúc mới

```text
librarian.py                  # thin wrapper entrypoint
librarian_pkg/
  __init__.py
  cli.py                      # argparse + dispatch
  shared.py                   # paths, ANSI UI, run_script, StepRunner
  steps.py                    # step implementations + quick counters
  validation.py               # schema/wikilink/source_ref validation + writeback
  help_data.py                # PIPELINE_HELP registry
  pipelines.py                # pipeline orchestration + status/help
```

---

## 3. Mapping trách nhiệm

### 3.1 `librarian.py`

- Chỉ còn vai trò wrapper:
  - import `main` từ `librarian_pkg.cli`
  - giữ nguyên entrypoint cho user và agent

### 3.2 `librarian_pkg/shared.py`

- Chứa hạ tầng dùng chung:
  - `bootstrap_stdout()`
  - constants đường dẫn
  - ANSI/UI helpers
  - `run_script()`
  - `StepRunner`

### 3.3 `librarian_pkg/steps.py`

- Chứa các step có thể tái sử dụng giữa nhiều pipeline:
  - graph/index/embed
  - bridge/orphan/thesis
  - inbox
  - quick counts cho status

### 3.4 `librarian_pkg/validation.py`

- Chứa logic kiểm tra và writeback:
  - frontmatter validation
  - broken wikilink check
  - source ref check
  - writeback queue processing

### 3.5 `librarian_pkg/help_data.py`

- Tách registry help khỏi code orchestration để:
  - đọc dễ hơn
  - update help text không chạm dispatch

### 3.6 `librarian_pkg/pipelines.py`

- Chứa orchestration cấp pipeline:
  - `pipeline_sync`, `pipeline_health`, `pipeline_search`, ...
  - `pipeline_status`
  - `pipeline_help`
  - `pipeline_batch`

### 3.7 `librarian_pkg/cli.py`

- Chứa:
  - parser builder
  - `make_runner_factory`
  - `dispatch(args)`
  - `main()`

---

## 4. Lợi ích đã đạt

- `librarian.py` không còn là file điều phối khổng lồ.
- Shared runtime và pipeline orchestration đã được tách lớp.
- Help data không còn lẫn trong dispatch.
- Validation và step logic có thể test/tách tiếp độc lập.
- Việc mở rộng thêm command mới giờ chỉ cần chạm đúng module liên quan.

---

## 5. Giới hạn hiện tại

- Các script engine trong `05_scripts/` vẫn là flat layout.
- `pipelines.py` hiện vẫn là module lớn nhất trong package mới.
- `help_data.py` vẫn là dict tĩnh; chưa chuyển sang config file.
- Chưa có test automation cho `librarian_pkg`.

---

## 6. Bước tiếp theo hợp lý

1. Tách tiếp `pipelines.py` thành:
   - `pipelines/core.py`
   - `pipelines/search.py`
   - `pipelines/ingest.py`
   - `pipelines/maintenance.py`
2. Tách `05_scripts/` theo namespace vật lý:
   - `05_scripts/retrieval/`
   - `05_scripts/ingestion/`
   - `05_scripts/governance/`
   - `05_scripts/synthesis/`
3. Bổ sung smoke test cho các command chính:
   - `status`
   - `help`
   - `health --only missing_thesis`
   - `search <query>`
4. Chuẩn hóa import path giữa `librarian_pkg` và `05_scripts` nếu sau này muốn gọi logic nội bộ thay vì subprocess.

---

## 7. Kết luận

Lượt module hóa này giải quyết phần monolith ở tầng CLI/orchestrator trước, theo nguyên tắc:

```text
entrypoint ổn định
-> orchestration tách lớp
-> shared/runtime gom lại
-> validation tách riêng
-> engine scripts giữ nguyên
```

Đây là điểm dừng an toàn để tiếp tục module hóa sâu hơn mà không phá workflow hiện tại của repo.
