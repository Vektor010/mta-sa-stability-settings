@echo off
title MTA:SA & GTA_SA System Optimizer
echo ========================================================
echo   Оптимизация gta_sa.exe и Windows 11 для MTA:SA
echo ========================================================
echo.

:: 1. Отключение DWM MPO (Multi-Plane Overlay) для безрамочного режима
echo [*] Применение твика отключения DWM MPO...
reg import "%~dp0registry\disable_mpo_windowed.reg" >nul 2>&1
if %errorlevel% equ 0 (
    echo [+] DWM MPO твик успешно применен.
) else (
    echo [!] Требуются права администратора для записи в HKLM. Запустите от имени Администратора.
)

:: 2. Применение флага DISABLEDXMAXIMIZEDWINDOWEDMODE для gta_sa.exe
echo.
echo [*] Применение флага совместимости для gta_sa.exe...
reg import "%~dp0registry\gta_sa_compat_flags.reg" >nul 2>&1
if %errorlevel% equ 0 (
    echo [+] Флаг DISABLEDXMAXIMIZEDWINDOWEDMODE применен.
) else (
    echo [!] Ошибка применения флага совместимости.
)

echo.
echo ========================================================
echo [+] Системные оптимизации применены!
echo [*] Для вступления в силу изменений MPO рекомендуется перезагрузить ПК.
echo ========================================================
pause
