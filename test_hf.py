import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}
data = {"inputs": "Привіт! Як справи?"}

response = requests.post(MODEL_URL, headers=headers, json=data)
print("🔹 Відповідь сервера:")
print(response.json())
