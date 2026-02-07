@echo off
echo ===================================================
echo CLEANUP AND START (Direct Venv Paths)
echo ===================================================

echo Switching to alternate ports to avoid stuck processes...
timeout /t 2 /nobreak > NUL

echo ===================================================
echo Starting End-to-End LLM Application Servers
echo ===================================================

echo 1. Starting MLflow UI on port 5001...
start "MLflow Server" cmd /k ".\venv\Scripts\mlflow.exe ui --port 5001 --backend-store-uri ./mlflow_runs"

echo Waiting 5 seconds for MLflow to initialize...
timeout /t 5 /nobreak > NUL

echo 2. Starting FastAPI Server on port 5000...
start "LLM API Server" cmd /k ".\venv\Scripts\python.exe debug_run.py"

echo ===================================================
echo Servers are starting in new windows.
echo API Docs: http://127.0.0.1:5000/docs
echo MLflow UI: http://127.0.0.1:5001
echo ===================================================
pause
