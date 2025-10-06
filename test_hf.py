import requests
import os

# 🔑 Твій API токен (заміни на свій з Hugging Face)
HF_TOKEN = os.getenv("HF_TOKEN") or "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"  

# 🔧 Використовуємо Granite-4.0-H-Micro
MODEL = "ibm-granite/granite-4.0-h-micro"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

data = {
    "inputs": "Привіт! Як у тебе справи?",
}

response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL}", headers=headers, json=data)

# Перевіримо, чи повертає сервер JSON
try:
    result = response.json()
    print("✅ Відповідь від моделі:")
    print(result)
except Exception as e:
    print("❌ Помилка при отриманні відповіді!")
    print("HTTP статус:", response.status_code)
    print("Текст відповіді:", response.text)

