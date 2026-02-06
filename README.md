# End-to-End LLM Application with MLOps

## 📌 Project Overview
We are building a production-grade **LLM Application** that demonstrates the full lifecycle of a Machine Learning model. This project moves beyond simple Jupyter notebooks to a real-world system architecture used by top tech companies.

### Key Features
- **LLM Inference API**: A FastAPI-based REST API to serve model predictions.
- **Experiment Tracking**: Integrated with **MLflow** to track parameters, metrics, and model versions.
- **Containerization**: Fully Dockerized application for consistent environments.
- **Cloud Deployment**: Deployed on **AWS SageMaker** for scalable inference.
- **CI/CD Pipeline**: Automated deployment using **GitHub Actions**.
- **Monitoring**: Real-time performance monitoring.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User[User] -->|Request| API[FastAPI Interface]
    API -->|Input| Model[LLM Inference Service]
    Model -->|Log| MLflow[MLflow Tracking]
    Model -->|Output| API
    API -->|Response| User
    
    subgraph MLOps Infrastructure
        Docker[Docker Container]
        SageMaker[AWS SageMaker Endpoint]
        GitHub[GitHub Actions CI/CD]
    end
    
    API -.-> Docker
    Docker -.-> SageMaker
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker
- AWS Account (optional for local dev, required for deployment)

### Installation
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd "End-to-End LLM Application with MLOps"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
1. **Start the API**
   ```bash
   uvicorn app.main:app --reload
   ```
   Visit `http://localhost:8000/docs` to see the Swagger UI.

2. **Run MLflow UI**
   ```bash
   mlflow ui
   ```
   Visit `http://localhost:5000` to view experiments.

## ☁️ Deployment to AWS SageMaker (Status: Pending Verification)

> **Note**: The deployment scripts are ready, but actual deployment is currently paused pending AWS Account Identity Verification.

### Deployment Preview
Once the account is active, the following results are expected:

**1. Terminal Output Success:**
![Terminal Success](docs/images/terminal_success.png)

**2. AWS SageMaker Console (Active Endpoint):**
![SageMaker Console](docs/images/aws_sagemaker.png)

### Steps to Finalize Deployment
1.  **Complete AWS Registration**: Verify phone number and payment method on AWS Console.
2.  **Configure AWS Credentials**:
    ```bash
    aws configure
    ```
3.  **Build and Push Docker Image**:
    ```bash
    # Login to ECR
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

    # Build and Tag
    docker build -t llm-app .
    docker tag llm-app:latest <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/llm-app:latest

    # Push
    docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/llm-app:latest
    ```
4.  **Deploy**:
    ```bash
    python deploy.py
    ```

## 🛠️ Tech Stack
| Component | Tool Used | Description |
|-----------|-----------|-------------|
| **Model** | Hugging Face Transformers | Pre-trained LLM (GPT-2/DistilGPT2) |
| **API** | FastAPI | High-performance API framework |
| **Tracking** | MLflow | Experiment tracking & model registry |
| **Container** | Docker | Application packaging |
| **Cloud** | AWS SageMaker | Scalable model deployment |
| **CI/CD** | GitHub Actions | Automated specific workflows |

## 📝 Project Methodology
1. **Select Model**: Choose a lightweight LLM for cost-effective demonstration.
2. **Build API**: Wrap the model in a FastAPI service.
3. **Track Experiments**: Log every run with MLflow to ensure reproducibility.
4. **Dockerize**: Package the app and dependencies.
5. **Deploy**: Push to AWS SageMaker for production availability.
6. **Monitor**: Track system health and model performance.

---
**Author**: Ashwin
**Goal**: Mastery of End-to-End MLOps for LLMs.

<img width="1919" height="864" alt="Screenshot 2026-02-06 153202" src="https://github.com/user-attachments/assets/72ff040c-c900-490e-b19a-8da1de6967ec" />

<img width="1919" height="916" alt="Screenshot 2026-02-06 153238" src="https://github.com/user-attachments/assets/8db35443-42e3-4d45-9892-20710c616735" />

<img width="1893" height="866" alt="Screenshot 2026-02-06 153309" src="https://github.com/user-attachments/assets/b2b6f70c-e6f6-4e2a-9c9d-491093f70035" />

<img width="1919" height="862" alt="Screenshot 2026-02-06 180840" src="https://github.com/user-attachments/assets/dcee5f38-1417-4724-b97a-f6c9759fa94d" />








