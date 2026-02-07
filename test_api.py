import requests

response = requests.post(
    "http://127.0.0.1:8001/generate",
    json={"prompt": "Machine learning is", "max_length": 50}
)

print("Status Code:", response.status_code)
print("Response:", response.json())
