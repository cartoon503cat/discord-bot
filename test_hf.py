import requests
import json

print("🤖 Тест безкоштовної AI-моделі — альтернативний endpoint")

# Альтернативний безкоштовний endpoint
MODEL_URL = "https://free.llm.garden/llm"

prompt = "Привіт! Розкажи про себе коротко українською."

payload = {
    "model": "gpt2-xl",  # модель, можливо легша — “gpt2-xl”, “gpt2-large” тощо
    "prompt": prompt,
    "max_new_tokens": 100,
    "temperature": 0.7
}

try:
    print("⏳ Відправляю запит...")
    response = requests.post(MODEL_URL, json=payload, timeout=60)

    if response.status_code == 200:
        data = response.json()
        # Залежно від формату відповіді
        text = data.get("text") or data.get("response") or json.dumps(data)
        print("\n✅ Відповідь AI:")
        print(text.strip())
    else:
        print(f"\n❌ Помилка: {response.status_code} — {response.text}")

except Exception as e:
    print(f"\n🚨 Виникла помилка: {e}")
