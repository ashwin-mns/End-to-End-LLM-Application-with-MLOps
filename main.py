from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import llm_service
# import mlflow # REMOVED: Causes startup hang on import
import time
import logging
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mlflow_tracking_uri = "http://127.0.0.1:5001"

app = FastAPI(
    title="End-to-End LLM API",
    description="A production-ready API for LLM inference with MLOps practices.",
    version="1.0.0"
)

# Add CORS Middleware to fix "Failed to fetch" in Swagger UI
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mlflow_initialised = False
mlflow = None # Global placeholder

def ensure_mlflow():
    global mlflow_initialised, mlflow
    if not mlflow_initialised:
        try:
            logging.info("Lazy-initializing MLflow...")
            import mlflow as m # Lazy import
            mlflow = m
            mlflow.set_tracking_uri("http://127.0.0.1:5001")
            mlflow.set_experiment("llm-inference-experiments")
            mlflow_initialised = True
            logging.info("MLflow initialized.")
        except Exception as e:
            logging.error(f"MLflow init failed: {e}")

class QueryRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "LLM Inference API"}


@app.post("/generate")
def generate_text(request: QueryRequest):
    """
    Endpoint to generate text from the LLM.
    """
    ensure_mlflow()
    with mlflow.start_run():
        try:
            start_time = time.time()
            
            # Log Parameters
            mlflow.log_param("prompt", request.prompt)
            mlflow.log_param("max_length", request.max_length)
            mlflow.log_param("temperature", request.temperature)
            
            if not request.prompt:
                raise HTTPException(status_code=400, detail="Prompt cannot be empty")
            
            generated_text = llm_service.generate_text(
                request.prompt, 
                request.max_length, 
                request.temperature
            )
            
            # Calculate and Log Metrics
            latency = time.time() - start_time
            mlflow.log_metric("latency", latency)
            mlflow.log_param("status", "success")
            
            return {
                "input_prompt": request.prompt,
                "generated_text": generated_text,
                "model": "distilgpt2",
                "latency": latency
            }
        except Exception as e:
            mlflow.log_param("status", "failed")
            mlflow.log_param("error", str(e))
            raise HTTPException(status_code=500, detail=str(e))
