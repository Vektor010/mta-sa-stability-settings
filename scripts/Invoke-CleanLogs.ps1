<#
.SYNOPSIS
    Invoke-CleanLogs.ps1 - Zero-Spam Log Maintenance & Safe Archival for MTA:SA
.DESCRIPTION
    Safely backs up and truncates runtime logs (clientscript.log, logfile.txt,
    CEGUI.log, cefdebug.txt, report.log) to prevent disk I/O micro-stutters.
#>

[CmdletBinding()]
param(
    [string]$GameRoot = "D:\CCD",
    [string]$BackupDir = "D:\CCD\_backup"
)

$ErrorActionPreference = "Continue"

$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$destinationBackup = Join-Path -Path $BackupDir -ChildPath "${timestamp}_log_backup"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " ZeroStutter-MTA | Automated Log Maintenance & Archival  " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Ensure backup directory exists
if (-not (Test-Path $destinationBackup)) {
    New-Item -ItemType Directory -Path $destinationBackup -Force | Out-Null
    Write-Host "[+] Created archival directory: $destinationBackup" -ForegroundColor Green
}

# Target runtime logs
$targetLogs = @(
    (Join-Path $GameRoot "MTA\logs\clientscript.log"),
    (Join-Path $GameRoot "MTA\logs\console.log"),
    (Join-Path $GameRoot "MTA\logs\logfile.txt"),
    (Join-Path $GameRoot "MTA\logs\logfile.txt.1"),
    (Join-Path $GameRoot "MTA\logs\CEGUI.log"),
    (Join-Path $GameRoot "MTA\cef\cefdebug.txt"),
    (Join-Path $GameRoot "MTA\core.log"),
    "C:\ProgramData\MTA CCDPlanet All\1.6\report.log"
)

$archivedCount = 0
$cleanedCount = 0

foreach ($logFile in $targetLogs) {
    if (Test-Path $logFile) {
        $fileName = [System.IO.Path]::GetFileName($logFile)
        $backupDest = Join-Path $destinationBackup $fileName

        try {
            # Copy with shared read/write access
            Copy-Item -Path $logFile -Destination $backupDest -Force
            $archivedCount++
            Write-Host "  -> Archived: $fileName" -ForegroundColor Gray

            # Truncate content without deleting locked handles
            [System.IO.File]::WriteAllText($logFile, [string]::Empty)
            $cleanedCount++
            Write-Host "  [OK] Truncated: $fileName" -ForegroundColor Green
        }
        catch {
            Write-Host "  [!] Locked by process (skipped truncation): $fileName" -ForegroundColor Yellow
        }
    }
}

Write-Host "----------------------------------------------------------" -ForegroundColor Cyan
Write-Host "[*] Summary: Archived: $archivedCount files | Truncated: $cleanedCount files" -ForegroundColor White
Write-Host "[+] Zero-Spam maintenance complete. Ready for clean session." -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
