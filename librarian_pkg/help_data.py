PIPELINE_HELP = {
    "sync": {
        "desc": "Đồng bộ graph + index sau bất kỳ thay đổi nào trong wiki.",
        "when": "Sau khi sửa node, đổi tên file, hoặc thêm wikilink thủ công.",
        "steps": [
            ("build_graph", "Inject wiki nodes & edges vào graph.json"),
            ("gen_index", "Tái tạo index.md và các sub-index theo loại node"),
            ("sync_registry", "Làm mới registry đồng bộ"),
            ("staleness", "Kiểm tra wisdom reports nào đã bị lỗi thời"),
        ],
        "examples": [
            "python librarian.py sync",
            "python librarian.py sync --skip gen_index",
            "python librarian.py sync --only staleness",
        ],
    },
    "ingest": {
        "desc": "Post-ingest sync sau khi hoàn tất Phase A-C của W2.",
        "when": "Sau khi SPAWN/EXPAND node mới từ raw source.",
        "steps": [
            ("build_graph", "Inject nodes & edges mới vào graph.json"),
            ("gen_index", "Tái tạo index"),
            ("auto_bridge", "Tự động link orphan nodes vào graph (--force --backup)"),
            ("staleness", "Báo cáo tags bị stale cần re-run wisdom"),
        ],
        "examples": [
            "python librarian.py ingest",
            "python librarian.py ingest --skip auto_bridge",
        ],
    },
    "health": {
        "desc": "Kiểm tra toàn bộ sức khỏe của wiki graph.",
        "when": "Định kỳ hoặc trước khi bắt đầu ingest topic mới.",
        "steps": [
            ("find_orphans", "Tìm nodes không có incoming link nào"),
            ("missing_thesis", "Tìm nodes thiếu thesis trong frontmatter"),
            ("staleness", "Wisdom reports nào đã lỗi thời"),
            ("suggest_ideas", "Bounty nodes + synthesis alerts + random walk"),
        ],
        "examples": [
            "python librarian.py health",
            "python librarian.py health --only missing_thesis,staleness",
            "python librarian.py health --skip suggest_ideas",
        ],
    },
    "daily": {
        "desc": "Workflow hằng ngày: gợi ý việc cần làm hôm nay.",
        "when": "Đầu mỗi session làm việc với wiki.",
        "steps": [
            ("suggest_ideas", "Bounty nodes, synthesis alerts, random walk"),
            ("find_orphans", "Orphan nodes cần được bridge"),
            ("staleness", "Wisdom reports cần refresh"),
            ("missing_thesis", "Nodes cần bổ sung thesis"),
        ],
        "examples": [
            "python librarian.py daily",
            "python librarian.py daily --only suggest_ideas",
        ],
    },
    "wisdom": {
        "desc": "Chạy Wisdom Synthesis cho một tag — Hub Map + Tension Pairs + LLM essay.",
        "when": "Trước khi ingest topic mới hoặc sau khi ingest để so sánh.",
        "steps": [
            ("staleness_check", "Kiểm tra report cũ còn fresh hay không"),
            ("auto_synthesis", "Collect -> subgraph -> hubs -> collisions -> clusters -> report"),
        ],
        "examples": [
            "python librarian.py wisdom monetary-policy --no-llm",
            "python librarian.py wisdom fixed-income",
            "python librarian.py wisdom central-banking --model claude-sonnet-4-6",
        ],
    },
    "audit": {
        "desc": "Chạy F.I.T.S.E.R.B.V.L audit trên một wiki node hoặc draft.",
        "when": "Trước khi merge node mới hoặc khi nghi ngờ chất lượng node.",
        "steps": [
            ("claim_audit", "F-I-T-S-E-R-B-V-L: 9 bước kiểm tra chất lượng node"),
        ],
        "examples": [
            "python librarian.py audit 03_wiki/mechanisms/Fiscal_Dominance.md",
            "python librarian.py audit 03_wiki/concepts/Barro_Gordon_Model.md",
        ],
    },
    "search": {
        "desc": "Tìm kiếm trong wiki + raw sources.",
        "when": "Khi cần tìm khái niệm trước khi SPAWN node hoặc trong khi viết.",
        "steps": [
            ("search", "wiki_search RRF mặc định; semantic-only hoặc hybrid heatmap khi cần"),
        ],
        "examples": [
            "python librarian.py search 'fiscal dominance' --top 8",
            "python librarian.py search 'interest rate transmission' --semantic --no-raw",
            "python librarian.py search 'repo market liquidity stress' --deep --raw-only --top 3",
            "python librarian.py search 'monetary policy' --export 04_outputs/temp/mp_search.md",
        ],
    },
    "deepdive": {
        "desc": "Deep Research: Detect thin wiki nodes -> Drill raw sources -> Draft expansion proposal.",
        "when": "Khi wiki node có confidence thấp, [LLM] placeholders, hoặc thiếu source_refs.",
        "steps": [
            ("detect", "wiki_search -> đánh giá confidence/[LLM]/source_refs của top results"),
            ("drill", "hybrid_search trên Raw Sources nếu wiki coverage thin"),
            ("draft", "Tạo expansion proposal với RAW citations vào 04_outputs/drafts/"),
        ],
        "examples": [
            "python librarian.py deepdive 'taralac facility mechanics'",
            "python librarian.py deepdive 'interest rate corridor' --threshold 3",
        ],
    },
    "staleness": {
        "desc": "Auto-detect nodes quá half_life -> report hoặc mark status:stale",
        "when": "Khi cần rà soát node đã quá hạn tri thức hoặc muốn tự động gắn cờ stale.",
        "steps": [("staleness_scan", "Quét toàn bộ 03_wiki theo half_life_years")],
        "examples": [
            "python librarian.py staleness",
            "python librarian.py staleness --auto-mark",
            "python librarian.py staleness --threshold 1.0",
        ],
    },
    "rename": {
        "desc": "Đổi tên wiki node an toàn: heal [[OldName]] -> [[NewName]] rồi rename file + sync.",
        "when": "Khi cần rename node sau ingest, tránh broken wikilinks.",
        "steps": [
            ("rename_node", "Search-replace wikilinks + rename file + update frontmatter title"),
            ("sync_graph", "Rebuild graph.json với tên mới"),
            ("sync_index", "Rebuild index.md + _index.md"),
        ],
        "examples": [
            "python librarian.py rename OldName NewName",
            "python librarian.py rename 'Old Name' 'New Name'",
            "python librarian.py rename OldName NewName --dry-run",
        ],
    },
    "status": {
        "desc": "System overview: node count, staged nodes, stale flags, orphan count, scripts, reports.",
        "when": "Đầu session hoặc khi cần nắm nhanh trạng thái hệ thống.",
        "steps": [("status", "In thống kê hệ thống + danh sách pipelines")],
        "examples": [
            "python librarian.py status",
            "python librarian.py",
        ],
    },
    "stage": {
        "desc": "Staging ingest từ raw books: sample uncovered sections, review staged nodes, accept vào wiki.",
        "when": "Khi muốn bán tự động hóa W2 ingest thay vì làm thủ công từng section.",
        "steps": [("auto_ingest", "scan books -> coverage -> stage drafts -> optionally accept reviewed drafts")],
        "examples": [
            "python librarian.py stage --dry-run",
            "python librarian.py stage --list-coverage",
            "python librarian.py stage --staged",
            "python librarian.py stage --accept Bindseil__Some_Heading",
        ],
    },
    "review": {
        "desc": "Xem và accept staged nodes — UI rõ ràng hơn stage --staged/--accept.",
        "when": "Sau khi chạy stage, trước khi merge nodes vào 03_wiki chính thức.",
        "steps": [
            ("list_staged", "Liệt kê staged nodes với frontmatter tóm tắt"),
            ("accept_node", "Accept node cụ thể -> 03_wiki + sync"),
            ("accept_all", "Accept tất cả nodes -> 03_wiki + sync"),
        ],
        "examples": [
            "python librarian.py review",
            "python librarian.py review accept Bindseil__Some_Heading",
            "python librarian.py review accept-all",
        ],
    },
    "extract": {
        "desc": "Extract PDF sang Markdown trong 02_sources/books.",
        "when": "Khi vừa thêm PDF raw source mới hoặc cần backfill file .md cho pipeline ingest/search.",
        "steps": [("extract_pdf", "pdf -> markdown alongside source files")],
        "examples": [
            "python librarian.py extract --book perry --skip-existing",
            "python librarian.py extract --file 02_sources/books/foo/bar.pdf --dry-run",
            "python librarian.py extract --all --dry-run",
        ],
    },
    "scout": {
        "desc": "Random discovery trên raw sources để tìm idea hoặc spot coverage gaps.",
        "when": "Khi cần seed ý tưởng nghiên cứu hoặc random walk ngoài wiki graph.",
        "steps": [("raw_scout", "sample lines or terms from clustered raw sources")],
        "examples": [
            "python librarian.py scout --mode lines --n 10",
            "python librarian.py scout --mode words --n 20",
        ],
    },
    "section": {
        "desc": "Surgical extraction một section cụ thể từ book markdown.",
        "when": "Khi cần raw passage đầy đủ để viết node hoặc audit claim sâu hơn.",
        "steps": [("exact_extractor", "extract matching chapter/section block into output file")],
        "examples": [
            'python librarian.py section --dir 02_sources/books/bindseil_monetary_policy --heading "1.1 Key Concepts" --out 04_outputs/temp/bindseil_1_1.md',
        ],
    },
    "organize": {
        "desc": "Dọn dẹp và sắp xếp node trong thư mục: report schema gaps, misplaced types, duplicates, whitespace.",
        "when": "Khi một folder wiki lộn xộn, node nằm sai taxonomy folder, hoặc cần review trước khi sync/ingest tiếp.",
        "steps": [
            ("organize_nodes", "scan folder -> propose moves/fixes; default dry-run"),
            ("sync_graph", "rebuild graph after applied moves"),
            ("sync_index", "rebuild generated indexes after applied moves"),
        ],
        "examples": [
            "python librarian.py organize --dir 03_wiki/concepts",
            "python librarian.py organize --dir 03_wiki --limit 40",
            "python librarian.py organize --dir 03_wiki/concepts --apply",
        ],
    },
    "cleanup": {
        "desc": "Dọn whitespace cơ học trong folder (trailing spaces, blank lines, final newline). Không move node.",
        "when": "Sau khi ingest hàng loạt hoặc khi node có trailing whitespace nhìn xấu trong diff.",
        "steps": [("organize_nodes", "scan + fix whitespace only (no moves)")],
        "examples": [
            "python librarian.py cleanup --dir 03_wiki/mechanisms",
            "python librarian.py cleanup --dir 03_wiki/concepts --apply",
            "python librarian.py cleanup --dir 03_wiki --apply --limit 50",
        ],
    },
    "batch": {
        "desc": "Chạy nhiều pipelines liên tiếp trong một lệnh.",
        "when": "Khi muốn kết hợp nhiều bước mà không cần mở nhiều terminal.",
        "steps": [("pipeline_N", "Mỗi pipeline trong list chạy tuần tự với StepRunner riêng")],
        "examples": [
            "python librarian.py batch sync,health",
            "python librarian.py batch daily,wisdom monetary-policy",
            "python librarian.py batch ingest,staleness",
            "python librarian.py batch organize,sync --dir 03_wiki/concepts --apply",
        ],
    },
    "inbox": {
        "desc": "Process inbox: scan files -> user manually selects folder -> extract + move.",
        "when": "Khi add tài liệu mới vào 02_sources/inbox/, cần extract + organize cho ingest.",
        "steps": [
            ("scan_inbox", "Scan inbox files (no auto-classify, user chooses folder)"),
            ("process", "Extract + move inbox files to specified book folder"),
            ("sync_graph", "Rebuild graph after moving files"),
            ("sync_index", "Rebuild indexes after moving files"),
        ],
        "examples": [
            "python librarian.py inbox",
            "python librarian.py inbox --list-books",
            "python librarian.py inbox --process bindseil",
            "python librarian.py inbox --process clipping",
        ],
    },
}
