# 🚀 End-to-End LLM Application with MLOps: Project Overview

This project is a production-grade machine learning application that demonstrates the full lifecycle of a Large Language Model (LLM)—from inference to tracking and deployment.

## 🌟 Core Architecture
The system is built on three main pillars:
1.  **FastAPI Inference Service**: A high-performance REST API that serves a language model (e.g., `distilgpt2`) for real-time text generation.
2.  **MLflow Tracking Dashboard**: Every request is logged as an "experiment run," tracking parameters (like `max_length`), metrics (like `latency`), and model versions for full observability.
3.  **Scalable Infrastructure**: The app is **Dockerized** for consistency and prepared for deployment to **AWS SageMaker** via automated CI/CD pipelines.

## 🐳 Why Docker?
In a professional MLOps pipeline, Docker is essential for several reasons:
-   **Environment Consistency**: It ensures the app runs the same on your laptop, a colleague's machine, or in the AWS cloud.
-   **Dependency Isolation**: LLMs require heavy libraries (like PyTorch). Docker prevents version conflicts with other projects.
-   **Seamless Deployment**: AWS SageMaker uses Docker containers to serve models.
-   **Scalability**: Containers can be spun up or down in seconds to handle varying traffic.

## 🎯 How It Works
1.  **Request**: A user sends a prompt to the FastAPI `/generate` endpoint.
2.  **Inference**: The model generates text while MLflow logs the performance metrics.
3.  **Response**: The system returns the generated text and updates the tracking dashboard.

## 🚀 Quick Start
```bash
.\run.bat
```
Access the API at `http://127.0.0.1:5000/docs` and MLflow at `http://127.0.0.1:5001`.
