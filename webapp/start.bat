@echo off
rem Starts the GATE study planner and opens it in your browser.
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found on PATH. Install Python 3.9+ from https://www.python.org and try again.
  pause
  exit /b 1
)
python server.py
pause
