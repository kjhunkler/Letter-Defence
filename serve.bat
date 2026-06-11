@echo off
title Letter Castle server
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install it from https://www.python.org/downloads/
  echo and check "Add python.exe to PATH" during setup.
  pause
  exit /b 1
)

set LANIP=
for /f "tokens=*" %%i in ('powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notmatch '^(127\.|169\.254)'} | Select-Object -First 1).IPAddress"') do set LANIP=%%i

echo.
echo  ================================================
echo   Letter Castle is being served!
echo.
echo   On this computer:   http://localhost:8000
if defined LANIP echo   On a phone/tablet:  http://%LANIP%:8000
if defined LANIP echo   (must be on the same Wi-Fi as this computer)
echo.
echo   Keep this window open while playing.
echo   Press Ctrl+C or close this window to stop.
echo  ================================================
echo.

start "" http://localhost:8000
python -m http.server 8000
pause
