@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs
    exit /b
)

cd /d "%~dp0"
python game_afker.py
pause
