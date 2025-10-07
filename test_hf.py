import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

HF_API_URL = "https://api-inference.huggingface.co/models/INSAIT-Institute/MamayLM-Gemma-2-9B-IT-v0.1"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_model_response(prompt):
    data = {"inputs": prompt}
    response = requests.post(HF_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return result
    else:
        return {"error": f"❌ Помилка при отриманні відповіді: {response.status_code}", "text": response.text}

# Приклад використання
prompt = "Привіт! Як у тебе справи?"
result = get_model_response(prompt)
print(result)
