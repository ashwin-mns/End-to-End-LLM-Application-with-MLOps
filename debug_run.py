from app.main import app
import uvicorn
import logging

if __name__ == "__main__":
    try:
        print("Starting LLM API Server...", flush=True)
        # Use simple run configuration
        config = uvicorn.Config(app=app, host="127.0.0.1", port=5000, log_level="info")
        server = uvicorn.Server(config)
        server.run()
    except Exception as e:
        print(f"CRITICAL ERROR: {e}", flush=True)
