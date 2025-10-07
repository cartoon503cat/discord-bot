import requests

print("🤖 Тест безкоштовного AI")

# URL до безкоштовної моделі (без Hugging Face API)
MODEL_URL = "https://textgenapi-production.up.railway.app/generate"

# Текст для тесту
prompt = "Привіт! Розкажи коротко про себе."

data = {"prompt": prompt}

try:
    response = requests.post(MODEL_URL, json=data, timeout=30)
    if response.status_code == 200:
        result = response.json().get("response", "⚠️ Немає відповіді від моделі.")
        print("\n✅ Відповідь AI:")
        print(result)
    else:
        print(f"\n❌ Помилка: {response.status_code} {response.text}")
except Exception as e:
    print(f"\n🚨 Виникла помилка: {e}")
