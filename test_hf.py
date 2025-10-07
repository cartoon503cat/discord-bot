import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ HF_TOKEN не встановлено у змінних середовища!")

MODEL = "malteos/gpt2-uk"
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_model_response(prompt, max_length=100):
    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_length,
            "temperature": 0.7,
            "do_sample": True
        }
    }
    response = requests.post(HF_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        # результат може бути або рядком або списком з {"generated_text": ...}
        if isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return result
    else:
        return {"error": f"❌ Помилка при отриманні відповіді: {response.status_code}", "text": response.text}

if __name__ == "__main__":
    prompt = "Привіт, як твої справи?"
    resp = get_model_response(prompt)
    print("Відповідь моделі:", resp)
