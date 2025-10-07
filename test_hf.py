import requests

def ask_free_ai(prompt: str) -> str:
    """
    Відправляє запит до безкоштовної AI API (LiteLLM proxy).
    Повертає відповідь, подібну до OpenAI ChatGPT.
    """
    try:
        response = requests.post(
            "https://api.litellm.ai/chat/completions",
            json={
                "model": "mistral",  # також доступні: "gpt-3.5-turbo", "phi-3-mini", "llama-3"
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            },
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"⚠️ Помилка: {response.status_code} — {response.text}"

    except Exception as e:
        return f"❌ Виникла помилка: {e}"


if __name__ == "__main__":
    print("🤖 Тест безкоштовного AI")
    while True:
        user_input = input("\nВведи запит (або 'вихід'): ").strip()
        if user_input.lower() in ["вихід", "exit", "quit"]:
            print("👋 Завершення роботи.")
            break

        print("\nДумаю...\n")
        answer = ask_free_ai(user_input)
        print("💬 Відповідь:\n", answer)



