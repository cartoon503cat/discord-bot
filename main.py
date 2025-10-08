import os
import discord
import asyncio
import aiohttp

TOKEN = os.environ["DISCORD_TOKEN"]
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # API ключ Google, якщо потрібен

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def query_gemini(prompt: str) -> str:
    # URL API Gemini для генерації тексту
    url = "https://api.generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GOOGLE_API_KEY}"
    }
    body = {
        "prompt": {
            "text": prompt
        },
        "temperature": 0.7,
        "candidateCount": 1
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as resp:
            if resp.status != 200:
                text = await resp.text()
                return f"⚠️ Помилка API: {resp.status} — {text}"
            data = await resp.json()
            # Google Gemini повертає в полі `candidates`
            candidates = data.get("candidates", [])
            if not candidates:
                return "Немає відповіді від Gemini"
            return candidates[0].get("output", "")

@client.event
async def on_ready():
    print(f"Увійшов як {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!gen "):
        prompt = message.content[len("!gen "):]
        await message.channel.send("🔍 Запитую Gemini...")
        resp = await query_gemini(prompt)
        await message.channel.send(resp)

client.run(TOKEN)

