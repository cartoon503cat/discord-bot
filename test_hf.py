import requests
import json
import os

def ask_openrouter(prompt: str) -> str:
    """
    Відправляє запит до OpenRouter API з українським prompt.
    Повертає текст відповіді або повідомлення про помилку.
    Потрібно встановити змінну оточення OPENROUTER_API_KEY = твій_ключ
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "❌ Помилка: API ключ не встановлений у змінній OPENROUTER_API_KEY"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-r1:free",  # приклад моделі, яка має free версію в OpenRouter :contentReference[oaicite:1]{index=1}
        "messages": [
            {"role": "system", "content": "Ти корисний асистент, говориш українською."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            # Витяг відповіді
            text = (
                data.get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
                or data.get("output", "")
                or ""
            )
            return text.strip()
        else:
            return f"❌ Помилка HTTP {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"❌ Помилка запиту: {e}"


if __name__ == "__main__":
    print("🤖 Тест OpenRouter AI")
    test_prompt = "Привіт! Розкажи про себе українською мовою."
    print("Prompt:", test_prompt)
    response = ask_openrouter(test_prompt)
    print("Відповідь:", response)

