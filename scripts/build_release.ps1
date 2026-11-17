$zipPath = "D:\CCD\mta-settings-pack\MTA_Stability_Pack_v1.0.0.zip"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

$tempDir = "D:\CCD\mta-settings-pack\_release_temp"
if (Test-Path $tempDir) { Remove-Item $tempDir -Recurse -Force }
New-Item -ItemType Directory -Path "$tempDir\registry" -Force | Out-Null

Copy-Item "D:\CCD\mta-settings-pack\coreconfig.xml" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\server_settings.json" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\handling.cfg" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\chatboxpresets.xml" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\clean_and_play.bat" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\apply_gta_optimizations.bat" $tempDir -Force
Copy-Item "D:\CCD\mta-settings-pack\registry\*" "$tempDir\registry" -Force

Compress-Archive -Path "$tempDir\*" -DestinationPath $zipPath -CompressionLevel Optimal
Remove-Item $tempDir -Recurse -Force

$hash = (Get-FileHash -Algorithm SHA256 $zipPath).Hash
Write-Host "Archive created: $zipPath" -ForegroundColor Green
Write-Host "SHA256: $hash" -ForegroundColor Cyan
