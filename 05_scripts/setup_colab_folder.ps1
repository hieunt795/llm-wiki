# setup_colab_folder.ps1
# Tạo folder docling_extract trên Desktop, copy tất cả PDF + scripts
# USAGE: Right-click -> Run with PowerShell
#        hoặc: powershell -ExecutionPolicy Bypass -File "E:\Wiki Link\05_scripts\setup_colab_folder.ps1"

$Desktop    = [Environment]::GetFolderPath("Desktop")
$TargetDir  = Join-Path $Desktop "docling_extract"
$WikiRoot   = "E:\Wiki Link"
$BooksDir   = Join-Path $WikiRoot "02_sources\books"
$ScriptsDir = Join-Path $WikiRoot "05_scripts"

Write-Host "=== Setup Colab Extract Folder ===" -ForegroundColor Cyan
Write-Host "Target: $TargetDir"

# ── Tạo folder structure ───────────────────────────────────────────────────────
New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
New-Item -ItemType Directory -Force -Path "$TargetDir\books" | Out-Null

# ── Copy scripts ───────────────────────────────────────────────────────────────
Write-Host "`nCopying scripts..." -ForegroundColor Yellow
Copy-Item "$ScriptsDir\extract_pdf_docling.py"   "$TargetDir\" -Force
Copy-Item "$ScriptsDir\colab_extract_docling.ipynb" "$TargetDir\" -Force
Write-Host "  [OK] extract_pdf_docling.py"
Write-Host "  [OK] colab_extract_docling.ipynb"

# ── Copy tất cả PDF (giữ nguyên folder structure) ─────────────────────────────
Write-Host "`nCopying PDFs..." -ForegroundColor Yellow
$pdfs = Get-ChildItem -Path $BooksDir -Recurse -Filter "*.pdf"
$count = 0
foreach ($pdf in $pdfs) {
    $rel     = $pdf.FullName.Substring($BooksDir.Length + 1)
    $destDir = Join-Path "$TargetDir\books" (Split-Path $rel -Parent)
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    Copy-Item $pdf.FullName (Join-Path $destDir $pdf.Name) -Force
    Write-Host "  [OK] $rel"
    $count++
}
Write-Host "`n  Total: $count PDFs copied"

# ── Tạo requirements.txt ───────────────────────────────────────────────────────
Write-Host "`nCreating requirements.txt..." -ForegroundColor Yellow
@"
# Requirements for docling PDF extraction
# Install: pip install -r requirements.txt

docling>=2.0.0
pymupdf>=1.24.0
"@ | Out-File -FilePath "$TargetDir\requirements.txt" -Encoding UTF8
Write-Host "  [OK] requirements.txt"

# ── Tạo README ────────────────────────────────────────────────────────────────
Write-Host "`nCreating README.md..." -ForegroundColor Yellow
@"
# Docling PDF Extractor

Extract tất cả PDF trong books/ thành Markdown chuẩn dùng Docling.

## Setup

### Local (Windows)
\`\`\`powershell
pip install -r requirements.txt
python extract_pdf_docling.py --all --skip-existing --chunk-size 10
\`\`\`

### Google Colab (Recommended — ~107 phút vs ~12 tiếng local)
1. Upload toàn bộ folder \`books/\` lên Google Drive:
   \`My Drive/Wiki Link/02_sources/books/\`
2. Mở \`colab_extract_docling.ipynb\` trên Colab
3. Runtime → Change runtime type → **T4 GPU**
4. Chạy từng cell theo thứ tự
5. Output \`.md\` sẽ được ghi thẳng vào Drive
6. Sau khi xong, sync Drive về local \`E:\Wiki Link\02_sources\books\`

## Commands

\`\`\`powershell
# Extract 1 book cụ thể
python extract_pdf_docling.py --book central_bank_balance_sheet --force --chunk-size 10

# Extract tất cả, bỏ qua file đã có
python extract_pdf_docling.py --all --skip-existing --chunk-size 10

# Force re-extract tất cả
python extract_pdf_docling.py --all --force --chunk-size 10

# Nếu bad_alloc → giảm chunk size
python extract_pdf_docling.py --all --skip-existing --chunk-size 5
\`\`\`

## Ước tính thời gian
- Total: 74 PDFs, 12,952 pages
- Local CPU: ~12 tiếng
- Colab T4 GPU: ~107 phút
"@ | Out-File -FilePath "$TargetDir\README.md" -Encoding UTF8
Write-Host "  [OK] README.md"

# ── Summary ───────────────────────────────────────────────────────────────────
Write-Host "`n=== Done ===" -ForegroundColor Green
Write-Host "Folder: $TargetDir"
Write-Host "Contents:"
Get-ChildItem $TargetDir | Format-Table Name, LastWriteTime -AutoSize
Write-Host "`nNext step: Upload books/ folder to Google Drive then open colab_extract_docling.ipynb"
