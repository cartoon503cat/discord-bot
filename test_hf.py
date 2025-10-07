import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

MODEL = "d0p3/ukr-t5-small"  # назва моделі на Hugging Face
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_model_response(prompt):
    data = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return result
    else:
        return {"error": f"❌ Помилка: {response.status_code}", "text": response.text}

# Приклад
if __name__ == "__main__":
    prompt = "Привіт! Як у тебе справи?"
    print(get_model_response(prompt))


