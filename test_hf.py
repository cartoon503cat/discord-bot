# bot.py
import os
import discord
import requests

from discord.ext import commands

# Витягуємо токени з Environment Variables
DISCORD_TOKEN = os.environ["TOKEN"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

# Створюємо бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Функція для звернення до OpenRouter API
def ask_openrouter(prompt: str) -> str:
    url = "https://api.openrouter.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",  # Легка, безкоштовна модель
        "messages": [
            {"role": "system", "content": "Ви допомагаєте користувачу українською."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Помилка при зверненні до OpenRouter: {e}"

# Команда для чату з AI
@bot.command(name="ai")
async def ai_chat(ctx, *, question: str):
    await ctx.send("🤖 Думка AI...")
    answer = ask_openrouter(question)
    await ctx.send(answer)

# Старт бота
bot.run(DISCORD_TOKEN)

