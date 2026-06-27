# migrate_frontmatter_v3.ps1
# Migrates all 03_Wiki nodes to Schema v3 frontmatter
# Adds: status: active, thesis: "", updated: TODAY
# Renames: source: -> source_refs: (with basic conversion)
# Does NOT touch body content

$today = Get-Date -Format "yyyy-MM-dd"
$wikiPath = "03_Wiki"
$count = 0
$touched = @()

Get-ChildItem -Recurse $wikiPath -Filter "*.md" | ForEach-Object {
    $file = $_.FullName
    $content = Get-Content $file -Raw -Encoding UTF8

    # Skip if already fully migrated (has source_refs: and status:)
    if ($content -match "^source_refs:" -and $content -match "^status:") {
        return
    }

    $changed = $false

    # 1. Add status: active if missing
    if ($content -notmatch "^status:") {
        $content = $content -replace "(?m)^(created:.*)", "status: active`n`$1"
        $changed = $true
    }

    # 2. Add updated: today if missing  
    if ($content -notmatch "^updated:") {
        $content = $content -replace "(?m)^(created:.*)", "`$1`nupdated: $today"
        $changed = $true
    }

    # 3. Add thesis placeholder if missing
    if ($content -notmatch "^thesis:") {
        $content = $content -replace "(?m)^(type:.*)", "`$1`nthesis: `"`"`""
        $changed = $true  
    }

    # 4. Convert simple source: field to source_refs: if present and not already converted
    if ($content -match "^source:" -and $content -notmatch "^source_refs:") {
        # Extract the old source value
        $sourceMatch = [regex]::Match($content, '(?m)^source:\s*"?([^"\n]+)"?\s*$')
        if ($sourceMatch.Success) {
            $sourceVal = $sourceMatch.Groups[1].Value.Trim()
            $sourceRefsBlock = "source_refs:`n  - file: `"$sourceVal`"`n    page: 1  # TODO: verify page"
            $content = $content -replace "(?m)^source:\s*`"?[^`"\n]+`"?\s*\n", "$sourceRefsBlock`n"
            $changed = $true
        }
    }

    # 5. Add source_refs placeholder if no source at all
    if ($content -notmatch "^source_refs:" -and $content -notmatch "^source:") {
        $content = $content -replace "(?m)^(created:.*)", "source_refs: []  # TODO: add citations`n`$1"
        $changed = $true
    }

    if ($changed) {
        Set-Content $file -Value $content -Encoding UTF8 -NoNewline
        $count++
        $touched += $_.Name
    }
}

Write-Host "✅ Migrated $count nodes to Schema v3 frontmatter"
Write-Host ""
Write-Host "Files touched:"
$touched | ForEach-Object { Write-Host "  - $_" }
