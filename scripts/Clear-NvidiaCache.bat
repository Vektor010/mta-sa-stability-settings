@echo off
setlocal
echo ========================================================
echo  ZeroStutter-MTA: NVIDIA DirectX Shader Cache Cleaner
echo ========================================================
echo.

set "NV_CACHE=%LOCALAPPDATA%\NVIDIA\DXCache"

if not exist "%NV_CACHE%" (
    echo [!] NVIDIA DXCache directory not found at: %NV_CACHE%
    goto :done
)

echo [*] Target directory: %NV_CACHE%
echo [*] Purging compiled shader blobs (*.bin, *.toc)...

del /q /f "%NV_CACHE%\*.bin" 2>nul
del /q /f "%NV_CACHE%\*.toc" 2>nul

echo [+] Shader cache purged successfully.
echo [*] Note: Next game launch will recompile shaders on-demand without stale index conflicts.

:done
echo.
echo ========================================================
pause
