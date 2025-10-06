import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

MODEL = "ibm-granite/granite-4.0-h-micro"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

data = {
    "inputs": "Привіт! Як у тебе справи?"  # рядок, а не список словників
}

response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL}", headers=headers, json=data)

try:
    result = response.json()
    print("✅ Відповідь від моделі:")
    if isinstance(result, list) and "generated_text" in result[0]:
        print(result[0]["generated_text"])
    else:
        print(result)
except Exception as e:
    print("❌ Помилка при отриманні відповіді!")
    print("HTTP статус:", response.status_code)
    print("Текст відповіді:", response.text)

