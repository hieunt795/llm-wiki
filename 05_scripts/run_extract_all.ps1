# run_extract_all.ps1
# Pipeline docling extract toan bo books - chay tuan tu nhe -> nang
# USAGE: powershell -ExecutionPolicy Bypass -File "E:\Wiki Link\05_scripts\run_extract_all.ps1"

$WikiRoot = "E:\Wiki Link"
$Script   = "05_scripts\extract_pdf_docling.py"
$LogFile  = "$WikiRoot\05_scripts\extract_log.txt"

$Books = @(
    @{ book = "singh_collateral_plumbing";       pages = 115  },
    @{ book = "imf_macro_accounting";            pages = 196  },
    @{ book = "tata_bank_alm";                   pages = 200  },
    @{ book = "schofield_fixed_income";          pages = 301  },
    @{ book = "lipschitz_schadler_macro";        pages = 312  },
    @{ book = "weithers_fx_guide";               pages = 323  },
    @{ book = "homer_leibowitz_yield_book";      pages = 351  },
    @{ book = "huggins_schaller_relative_value"; pages = 430  },
    @{ book = "imf_wb_govt_bond_markets";        pages = 436  },
    @{ book = "tuckman_serrat_fixed_income";     pages = 538  },
    @{ book = "howard_corb_swaps";               pages = 623  },
    @{ book = "neftci_principles";               pages = 893  },
    @{ book = "watts_wray_mmt_macro";            pages = 1188 },
    @{ book = "wilmott_quant_finance";           pages = 1401 }
)

function Get-ChunkSize($pages) {
    if ($pages -le 200) { return 10 }
    if ($pages -le 500) { return 7  }
    return 5
}

function Log($msg) {
    $ts   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
}

Set-Location $WikiRoot

Log "========================================================"
Log "START extract_all pipeline | Books: $($Books.Count)"
Log "========================================================"

$total_start = Get-Date
$done    = 0
$failed  = 0
$skipped = 0

foreach ($entry in $Books) {
    $book  = $entry.book
    $pages = $entry.pages
    $chunk = Get-ChunkSize $pages
    $chunks_dir = "$WikiRoot\02_sources\books\$book\_chunks"

    if (Test-Path $chunks_dir) {
        Log "SKIP : $book (_chunks exists - dang chay do?)"
        $skipped++
        continue
    }

    Log "BEGIN: $book  pages=$pages chunk=$chunk refresh=5"
    $t0 = Get-Date

    python $Script --book $book --force --chunk-size $chunk --refresh-every 5
    $exit_code = $LASTEXITCODE

    $elapsed = [math]::Round(((Get-Date) - $t0).TotalMinutes, 1)
    $elapsed_str = "$elapsed min"

    if ($exit_code -eq 0) {
        $done++
        Log "DONE : $book ($elapsed_str)"
    } else {
        $failed++
        Log "FAIL : $book exit=$exit_code ($elapsed_str)"
    }
}

$total = [math]::Round(((Get-Date) - $total_start).TotalMinutes, 1)
$total_str = "$total min"
Log "========================================================"
Log "FINISH: done=$done failed=$failed skipped=$skipped total=$total_str"
Log "========================================================"
