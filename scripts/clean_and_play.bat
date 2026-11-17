@echo off
title MTA:SA Fast Clean & Launch
echo ===================================================
echo   MTA:SA - Очистка логов и оптимизированный запуск
echo ===================================================
echo.

:: 1. Очистка спама в логах (убирает микрофризы диска)
echo [*] Очистка файлов логов перед входом...
if exist "MTA\logs\clientscript.log" type nul > "MTA\logs\clientscript.log"
if exist "MTA\logs\logfile.txt" type nul > "MTA\logs\logfile.txt"
if exist "MTA\logs\console.log" type nul > "MTA\logs\console.log"
if exist "MTA\logs\CEGUI.log" type nul > "MTA\logs\CEGUI.log"
if exist "MTA\cef\cefdebug.txt" type nul > "MTA\cef\cefdebug.txt"
if exist "D:\CCD\MTA\logs\clientscript.log" type nul > "D:\CCD\MTA\logs\clientscript.log"
if exist "D:\CCD\MTA\logs\logfile.txt" type nul > "D:\CCD\MTA\logs\logfile.txt"
if exist "D:\CCD\MTA\logs\console.log" type nul > "D:\CCD\MTA\logs\console.log"
if exist "D:\CCD\MTA\logs\CEGUI.log" type nul > "D:\CCD\MTA\logs\CEGUI.log"
if exist "D:\CCD\MTA\cef\cefdebug.txt" type nul > "D:\CCD\MTA\cef\cefdebug.txt"
if exist "%ProgramData%\MTA CCDPlanet All\1.6\report.log" type nul > "%ProgramData%\MTA CCDPlanet All\1.6\report.log"
echo [+] Логи успешно очищены.

:: 2. Запуск игры с повышенным приоритетом
echo.
echo [*] Запуск игры с приоритетом AboveNormal...
if exist "CCDPlanet.exe" (
    start /AboveNormal "" "CCDPlanet.exe"
    echo [+] CCDPlanet запущен!
) else if exist "D:\CCD\CCDPlanet.exe" (
    start /AboveNormal "" "D:\CCD\CCDPlanet.exe"
    echo [+] CCDPlanet запущен!
) else if exist "MTA\Multi Theft Auto.exe" (
    start /AboveNormal "" "MTA\Multi Theft Auto.exe"
    echo [+] MTA запущен!
) else (
    echo [!] Исполняемый файл игры не найден в текущей папке.
)

timeout /t 2 >nul
exit /b 0
