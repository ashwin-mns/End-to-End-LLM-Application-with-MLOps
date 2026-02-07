import mlflow
import mlflow.sklearn
import logging
import time
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MLflow experiment
EXPERIMENT_NAME = "llm-inference-experiments"
mlflow.set_experiment(EXPERIMENT_NAME)

def log_experiment(model_name, temperature, max_length):
    """
    Simulate an experiment run where we log parameters and metrics.
    In a real scenario, this would involve training or evaluating the model.
    """
    with mlflow.start_run():
        logger.info(f"Starting run for model: {model_name}")
        
        # Log Parameters
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("temperature", temperature)
        mlflow.log_param("max_length", max_length)
        
        # Simulate some processing/validation
        time.sleep(1) 
        
        # Mock Metrics (e.g., latency, perplexity)
        # In a real app, calculate these based on validation set
        mock_latency = random.uniform(0.1, 0.5)
        mock_perplexity = random.uniform(10.0, 30.0)
        
        mlflow.log_metric("latency_seconds", mock_latency)
        mlflow.log_metric("perplexity", mock_perplexity)
        
        logger.info(f"Run complete. Latency: {mock_latency:.4f}s, Perplexity: {mock_perplexity:.4f}")
        logger.info(f"Experiment logged to MLflow under: {EXPERIMENT_NAME}")

if __name__ == "__main__":
    # Example experiment runs
    print("Running experiments...")
    log_experiment("distilgpt2", 0.7, 50)
    log_experiment("distilgpt2", 0.9, 100)
    log_experiment("gpt2-medium", 0.8, 50)
    print("Experiments completed. Run 'mlflow ui' to view results.")
