#!/usr/bin/env python3
"""
normalize_ocr_md.py — Hậu xử lý OCR cho file .md sinh từ Marker/docling.

Vá các lỗi OCR thay-ký-tự hệ thống (vd: "GOP" -> "GDP") để chuẩn hoá entity
TRƯỚC khi chunk + trích triple cho KG2RAG. Entity-resolution rất nhạy với biến
thể chính tả: "GOP" và "GDP" sẽ bị coi là 2 entity khác nhau nếu không sửa.

An toàn:
  - Mặc định DRY-RUN: chỉ báo cáo số lần thay + ngữ cảnh mẫu, KHÔNG ghi file.
  - --apply: ghi đè, tạo backup <file>.bak trước khi sửa.
  - TIER1/TIER2 (non-word, near-zero risk) được áp dụng.
  - TIER3 (đụng từ tiếng Anh hợp lệ) CHỈ báo cáo, KHÔNG tự sửa.
  - --scan: quét token khả nghi (heuristic) để mở rộng danh sách thủ công.

Cách dùng:
  python 05_scripts/normalize_ocr_md.py "<file.md>"            # dry-run
  python 05_scripts/normalize_ocr_md.py "<file.md>" --scan     # dry-run + quét token lạ
  python 05_scripts/normalize_ocr_md.py "<file.md>" --apply    # ghi + backup
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

# Console Windows mặc định cp1252 -> ép UTF-8 cho output có box-char/tiếng Việt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── TIER 1: garble KHÔNG phải từ tiếng Anh → thay an toàn (không thể đụng từ thật) ──
TIER1 = {
    r"\bGOP\b":        "GDP",          # lỗi nổi bật nhất trong IMF Macro Accounting
    r"\blMF\b":        "IMF",          # l->I, tài liệu do chính IMF xuất bản
    r"\bfore1gn\b":    "foreign",      # 1->i
    r"\baccoums\b":    "accounts",
    r"\bmcome\b":      "income",
    r"\bmcomc\b":      "income",
    r"\bExporrs\b":    "Exports",
    r"\blmporcs\b":    "Imports",
    r"\btlemand\b":    "demand",
    r"\bmventones\b":  "inventories",
    r"\bdefimnon\b":   "definition",
    r"\bProdud\b":     "Product",
    r"\bSedoral\b":    "Sectoral",
    r"\bBasrc\b":      "Basic",
    r"\bdomesuc\b":    "domestic",
    r"dispo:\.able":   "disposable",   # garble cụ thể "dispo:.able"
}

# ── TIER 2: non-word, rủi ro rất thấp nhưng nên liếc dry-run trước (c↔t confusion) ──
TIER2 = {
    r"\bche\b":      "the",
    r"\bchis\b":     "this",
    r"\bresc\b":     "rest",
    r"\bcurrenr\b":  "current",
    r"\boffser\b":   "offset",
}

# ── TIER 3: đụng TỪ TIẾNG ANH HỢP LỆ → chỉ báo cáo, KHÔNG auto-fix (tránh phá nội dung) ──
TIER3_REVIEW = {
    r"\bnor\b":   "not?  (nhưng 'nor' là từ thật — kiểm tay)",
    r"\bmuse\b":  "must? ('muse' là từ thật)",
    r"\bchat\b":  "that? ('chat' là từ thật)",
}


def count_and_samples(text, pattern, max_samples=2):
    """Đếm số match + lấy vài dòng ngữ cảnh."""
    matches = list(re.finditer(pattern, text))
    samples = []
    for m in matches[:max_samples]:
        start = text.rfind("\n", 0, m.start()) + 1
        end = text.find("\n", m.end())
        if end == -1:
            end = len(text)
        line = text[start:end].strip()
        if len(line) > 110:
            # cắt quanh match cho gọn
            rel = m.start() - start
            a = max(0, rel - 45)
            line = "…" + line[a:rel + 55] + "…"
        samples.append(line)
    return len(matches), samples


def apply_tier(text, mapping):
    total = 0
    per_rule = []
    for pat, repl in mapping.items():
        n, samples = count_and_samples(text, pat)
        if n:
            text = re.sub(pat, repl, text)
            total += n
            per_rule.append((pat, repl, n, samples))
    return text, total, per_rule


def scan_suspicious(text, top=40):
    """Heuristic phát hiện token OCR lạ để mở rộng danh sách thủ công."""
    from collections import Counter
    flags = Counter()
    # 1) chữ + số lẫn lộn (vd "1Jpkal"), bỏ token toàn số
    for tok in re.findall(r"\b(?=\w*[A-Za-z])(?=\w*\d)\w{2,}\b", text):
        if not tok.isdigit():
            flags[tok] += 1
    # 2) cùng 1 chữ cái lặp >=3 (vd "Blllance")
    for tok in re.findall(r"\b\w*([A-Za-z])\1\1\w*\b", text):
        pass  # group trả về ký tự; cần findall nguyên token bên dưới
    for m in re.finditer(r"\b\w*(?:([A-Za-z])\1\1)\w*\b", text):
        flags[m.group(0)] += 1
    # 3) chữ thường rồi HOA giữa từ (vd "GNDlp" -> không; "tHe" -> có)
    for tok in re.findall(r"\b[a-z]+[A-Z]\w*\b", text):
        flags[tok] += 1
    # 4) ký tự non-ascii giữa chữ (vd "Neutr·llty")
    for tok in re.findall(r"\b\w*[^\x00-\x7f]\w*\b", text):
        flags[tok] += 1
    return flags.most_common(top)


def main():
    ap = argparse.ArgumentParser(description="Hậu xử lý OCR cho file .md (KG2RAG-ready).")
    ap.add_argument("file", help="Đường dẫn file .md")
    ap.add_argument("--apply", action="store_true", help="Ghi đè (mặc định dry-run)")
    ap.add_argument("--scan", action="store_true", help="Quét token khả nghi (heuristic)")
    ap.add_argument("--no-tier2", action="store_true", help="Bỏ qua TIER2 (c↔t confusion)")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"ERR: không thấy file: {path}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    orig_len = len(text)

    print(f"=== normalize_ocr_md — {path.name} ===")
    print(f"Mode: {'APPLY (sẽ ghi + backup)' if args.apply else 'DRY-RUN (không ghi)'}\n")

    grand_total = 0

    # TIER 1
    text, t1, rules1 = apply_tier(text, TIER1)
    print(f"── TIER 1 (non-word, an toàn) — {t1} thay thế ──")
    for pat, repl, n, samples in rules1:
        print(f"  {pat:>16} -> {repl:<14} ×{n}")
        for s in samples:
            print(f"        | {s}")
    grand_total += t1

    # TIER 2
    if not args.no_tier2:
        text, t2, rules2 = apply_tier(text, TIER2)
        print(f"\n── TIER 2 (non-word, liếc trước) — {t2} thay thế ──")
        for pat, repl, n, samples in rules2:
            print(f"  {pat:>16} -> {repl:<14} ×{n}")
            for s in samples:
                print(f"        | {s}")
        grand_total += t2

    # TIER 3 — chỉ báo cáo
    print(f"\n── TIER 3 (đụng từ thật — CHỈ BÁO CÁO, không sửa) ──")
    any3 = False
    for pat, note in TIER3_REVIEW.items():
        n, samples = count_and_samples(text, pat)
        if n:
            any3 = True
            print(f"  {pat:>16} ?  {note}  ×{n}")
            for s in samples:
                print(f"        | {s}")
    if not any3:
        print("  (không phát hiện)")

    # SCAN
    if args.scan:
        print(f"\n── SCAN token khả nghi (heuristic, top 40) ──")
        for tok, n in scan_suspicious(text):
            print(f"  {n:>4}×  {tok}")

    print(f"\n=== TỔNG cộng sẽ thay: {grand_total} ===")

    if args.apply:
        if grand_total == 0:
            print("Không có gì để thay — bỏ qua ghi.")
            return
        bak = path.with_suffix(path.suffix + ".bak")
        shutil.copy2(path, bak)
        path.write_text(text, encoding="utf-8")
        print(f"Đã ghi {path.name}  (backup: {bak.name})")
        print(f"Độ dài: {orig_len} -> {len(text)} ký tự")
    else:
        print("Dry-run: KHÔNG ghi. Thêm --apply để áp dụng (sẽ tạo .bak).")


if __name__ == "__main__":
    main()
