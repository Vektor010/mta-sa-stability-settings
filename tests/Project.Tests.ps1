# Project.Tests.ps1 - Automated Verification Suite

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$failed = 0

Write-Host "Running Verification Suite in: $repoRoot" -ForegroundColor Cyan

# 1. PowerShell AST Syntax Validation
$scripts = Get-ChildItem -Path "$repoRoot\scripts" -Filter "*.ps1" -ErrorAction SilentlyContinue
foreach ($s in $scripts) {
    $errs = $null
    $tokens = $null
    [System.Management.Automation.Language.Parser]::ParseFile($s.FullName, [ref]$tokens, [ref]$errs) | Out-Null
    if ($errs.Count -eq 0) {
        Write-Host "  [PASS] AST Syntax: $($s.Name)" -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] AST Error in $($s.Name)" -ForegroundColor Red
        $failed++
    }
}

# 2. XML Configuration Validation
$xmlFiles = Get-ChildItem -Path "$repoRoot" -Filter "*.xml" -Recurse
foreach ($xf in $xmlFiles) {
    try {
        [xml]$parsed = Get-Content $xf.FullName -Raw
        Write-Host "  [PASS] XML Valid: $($xf.Name)" -ForegroundColor Green
    } catch {
        Write-Host "  [FAIL] XML Malformed: $($xf.Name)" -ForegroundColor Red
        $failed++
    }
}

# 3. Registry Rollback Parity
$regFiles = Get-ChildItem -Path "$repoRoot\registry" -Filter "*.reg" | Where-Object { $_.Name -notmatch "^restore_" }
foreach ($rf in $regFiles) {
    $restore = "restore_" + $rf.Name
    $target = Join-Path "$repoRoot\registry" $restore
    if (Test-Path $target) {
        Write-Host "  [PASS] Rollback Pair: $($rf.Name) -> $restore" -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] Missing Rollback: $($rf.Name)" -ForegroundColor Red
        $failed++
    }
}

# 4. RTSS Profile Flag
$rtssFiles = @(
    (Join-Path $repoRoot "gta_sa.exe.cfg"),
    (Join-Path $repoRoot "configs\rtss\gta_sa.exe.cfg")
)
foreach ($rf in $rtssFiles) {
    if (Test-Path $rf) {
        $content = Get-Content $rf -Raw
        if ($content -match "EnableHooking=0") {
            Write-Host "  [PASS] RTSS Hooking Flag: $rf" -ForegroundColor Green
        } else {
            Write-Host "  [FAIL] RTSS Flag Missing in $rf" -ForegroundColor Red
            $failed++
        }
    }
}

Write-Host "--------------------------------------------------------" -ForegroundColor Cyan
if ($failed -eq 0) {
    Write-Host "All project tests PASSED successfully." -ForegroundColor Green
    exit 0
} else {
    Write-Host "$failed test assertion(s) FAILED." -ForegroundColor Red
    exit 1
}
