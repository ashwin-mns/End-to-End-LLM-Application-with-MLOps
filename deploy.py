import sagemaker
from sagemaker.model import Model
import boto3
import time

"""
AWS SAGEMAKER DEPLOYMENT SCRIPT
--------------------------------
This script automates the deployment of the Docker container to AWS SageMaker.

PREREQUISITES:
1. AWS CLI configured with `aws configure`.
2. Docker image built and pushed to AWS ECR.
3. IAM Role with SageMaker permissions.
"""

# --- CONFIGURATION (UPDATE THESE) ---
# The IAM Role ARN that SageMaker assumes to run the model
# Example: "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole-20240101"
ROLE_ARN = "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_ROLE"

# The URI of your Docker image in AWS ECR
# Example: "123456789012.dkr.ecr.us-east-1.amazonaws.com/llm-app:latest"
ECR_IMAGE_URI = "YOUR_ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/llm-app:latest"

# Instance type for the endpoint (ml.m5.large is good for small CPU tests)
INSTANCE_TYPE = "ml.m5.large" 
ENDPOINT_NAME = f"llm-inference-endpoint-{int(time.time())}"

def deploy_to_sagemaker():
    print(f"Starting deployment to SageMaker...")
    print(f"Image: {ECR_IMAGE_URI}")
    print(f"Role: {ROLE_ARN}")
    
    try:
        # Initialize SageMaker Session
        sess = sagemaker.Session()
        
        # Create Model Object
        model = Model(
            image_uri=ECR_IMAGE_URI,
            role=ROLE_ARN,
            sagemaker_session=sess,
            name=f"llm-model-{int(time.time())}"
        )
        
        print("Deploying model to endpoint... (Usage: ml.m5.large)")
        # Deploy the endpoint
        predictor = model.deploy(
            initial_instance_count=1,
            instance_type=INSTANCE_TYPE,
            endpoint_name=ENDPOINT_NAME
        )
        
        print(f"✅ Deployment Complete!")
        print(f"Endpoint Name: {ENDPOINT_NAME}")
        
    except Exception as e:
        print(f"❌ Deployment Failed: {e}")
        print("Ensure you have set ROLE_ARN and ECR_IMAGE_URI correctly.")

if __name__ == "__main__":
    deploy_to_sagemaker()
