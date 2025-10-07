import requests
import json

print("🤖 Тест безкоштовної AI-моделі через mlvoca.com")

# Безкоштовний публічний endpoint
MODEL_URL = "https://mlvoca.com/api/generate"

# Твій запит до моделі
prompt = "Привіт! Розкажи коротко про себе українською мовою."

# Дані, які відправляються у запиті
payload = {
    "model": "tinyllama",   # Можна спробувати: "deepseek-r1:1.5b", "mistral", "phi3"
    "prompt": prompt,
    "stream": False          # False — щоб отримати весь текст одразу
}

# Відправлення запиту
try:
    print("⏳ Відправляю запит...")
    response = requests.post(MODEL_URL, json=payload, timeout=60)

    if response.status_code == 200:
        try:
            data = response.json()
            text = data.get("response") or data.get("text") or str(data)
        except json.JSONDecodeError:
            text = response.text

        print("\n✅ Відповідь AI:")
        print(text.strip())
    else:
        print(f"\n❌ Помилка: {response.status_code} {response.text}")

except Exception as e:
    print(f"\n🚨 Виникла помилка: {e}")
