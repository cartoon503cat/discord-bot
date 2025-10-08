import os
import discord
import asyncio
import aiohttp
from flask import Flask
import threading

# ==========================
# Discord бот
# ==========================
TOKEN = os.environ["TOKEN"]
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # API ключ Google, якщо потрібен

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def query_gemini(prompt: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/text-bison-001:generateText"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GOOGLE_API_KEY}"
    }
    body = {
        "prompt": {"text": prompt},
        "temperature": 0.7,
        "candidateCount": 1
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as resp:
            if resp.status != 200:
                text = await resp.text()
                return f"⚠️ Помилка API: {resp.status} — {text}"
            data = await resp.json()
            candidates = data.get("candidates", [])
            if not candidates:
                return "Немає відповіді від Gemini"
            return candidates[0].get("output", "")

@client.event
async def on_ready():
    print(f"✅ Увійшов як {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!gen "):
        prompt = message.content[len("!gen "):]
        await message.channel.send("🔍 Запитую Gemini...")
        resp = await query_gemini(prompt)
        await message.channel.send(resp)

# ==========================
# Flask-сервер для Render
# ==========================
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Discord бот працює!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ==========================
# Запуск Flask + Discord
# ==========================
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()  # Flask у окремому потоці
    client.run(TOKEN)


