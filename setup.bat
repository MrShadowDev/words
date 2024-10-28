@echo off
setlocal enabledelayedexpansion

python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b 1
)

echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install requirements.
    pause
    exit /b 1
)

echo Running run.py...
python run.py
if %errorlevel% neq 0 (
    echo Error: Failed to run run.py.
    pause
)

pause