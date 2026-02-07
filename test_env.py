print("Hello from Python")
import sys
print("Version:", sys.version)
try:
    import fastapi
    print("FastAPI:", fastapi.__version__)
    import uvicorn
    print("Uvicorn:", uvicorn.__version__)
    import mlflow
    print("MLflow:", mlflow.__version__)
except ImportError as e:
    print("Import Error:", e)
