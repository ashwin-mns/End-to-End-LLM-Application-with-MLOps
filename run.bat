@echo off
setlocal
echo ===================================================
echo   END-TO-END LLM APP - FRESH START
echo ===================================================

echo [1/3] CLEANUP: Killing old Python processes...
taskkill /F /IM python.exe /T >NUL 2>&1
taskkill /F /IM mlflow.exe /T >NUL 2>&1
timeout /t 2 /nobreak > NUL

echo [2/3] INFRASTRUCTURE: Checking Environment...
if exist "venv\Scripts\python.exe" (
    echo    - Virtual Environment found.
) else (
    echo    - ERROR: venv not found! Please run 'python -m venv venv' first.
    pause
    exit /b
)

echo [3/3] EXECUTION: Starting Servers...
echo.
echo    - Starting MLflow UI (Port 5001)...
start "MLflow Server" cmd /k ".\venv\Scripts\python.exe -m mlflow ui --port 5001 --backend-store-uri ./mlflow_runs"

echo    - Waiting for MLflow...
timeout /t 5 /nobreak > NUL

echo    - Starting API Server (Port 5000)...
start "LLM API Server" cmd /k ".\venv\Scripts\python.exe -u debug_run.py"

echo.
echo ===================================================
echo   SUCCESS! Services are launching.
echo ===================================================
echo.
echo   API Docs:      http://127.0.0.1:5000/docs
echo   MLflow UI:     http://127.0.0.1:5001
echo.
echo ===================================================
pause
