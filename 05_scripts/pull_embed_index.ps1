# pull_embed_index.ps1
# Giải nén artifact embed (tải từ Colab) vào .cache/ ở local.
# USAGE:
#   powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1
#   powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1 -Zip "C:\path\wiki_embed_artifacts.zip"
#
# Mặc định tìm wiki_embed_artifacts.zip trong Downloads.

param(
    [string]$Zip = ""
)

$ErrorActionPreference = "Stop"
$WikiRoot = Split-Path $PSScriptRoot -Parent
$Cache    = Join-Path $WikiRoot ".cache"

if (-not $Zip) {
    $dl = Join-Path ([Environment]::GetFolderPath("UserProfile")) "Downloads\wiki_embed_artifacts.zip"
    if (Test-Path $dl) { $Zip = $dl }
    else { Write-Host "Khong tim thay zip trong Downloads. Truyen -Zip <path>." -ForegroundColor Red; exit 1 }
}

if (-not (Test-Path $Zip)) { Write-Host "Khong thay file: $Zip" -ForegroundColor Red; exit 1 }

New-Item -ItemType Directory -Force -Path $Cache | Out-Null

# Backup bo artifact cu (phong khi can rollback)
$artifactNames = @(
    "wiki_embed.index",
    "wiki_embed.meta.json",
    "wiki_embed.manifest.json"
)

foreach ($name in $artifactNames) {
    $src = Join-Path $Cache $name
    if (Test-Path $src) {
        $bak = Join-Path $Cache ($name + ".bak")
        Copy-Item $src $bak -Force
        Write-Host "Backup $name -> $($name).bak" -ForegroundColor DarkGray
    }
}

Write-Host "Giai nen $Zip -> $Cache" -ForegroundColor Cyan
Expand-Archive -Path $Zip -DestinationPath $Cache -Force

Write-Host "`nDone. Index hien tai:" -ForegroundColor Green
Get-ChildItem $Cache -Filter "wiki_embed.*" | Format-Table Name, @{N="MB";E={[math]::Round($_.Length/1MB,1)}}, LastWriteTime -AutoSize

Write-Host "Kiem tra:  python 05_scripts\embed_index.py --stats" -ForegroundColor Yellow
