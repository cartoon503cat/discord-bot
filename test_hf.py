import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

MODEL = "INSAIT-Institute/MamayLM-Gemma-2-9B-IT-v0.1"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_model_response(prompt):
    data = {"inputs": prompt}
    response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL}", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"❌ Помилка при отриманні відповіді: {response.status_code}"}

# Приклад використання
prompt = "Привіт! Як у тебе справи?"
result = get_model_response(prompt)
print(result)
