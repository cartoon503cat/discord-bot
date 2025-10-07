import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

MODEL = "gpt2"  # англомовна модель, але працює через API
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_model_response(prompt, max_new_tokens=50):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": 0.7,
            "do_sample": True,
        }
    }
    resp = requests.post(HF_API_URL, headers=headers, json=payload)
    if resp.status_code == 200:
        j = resp.json()
        if isinstance(j, list) and "generated_text" in j[0]:
            return j[0]["generated_text"]
        if isinstance(j, dict) and "generated_text" in j:
            return j["generated_text"]
        return j
    else:
        return {"error": f"❌ Помилка: {resp.status_code}", "text": resp.text}

if __name__ == "__main__":
    prompt = "Привіт. Розкажи цікаву історію українською:"
    result = get_model_response(prompt, max_new_tokens=100)
    print("Відповідь:", result)

