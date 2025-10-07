import os
import discord
import aiohttp
import asyncio
from flask import Flask
from threading import Thread

DISCORD_TOKEN = os.environ["TOKEN"]
HF_TOKEN = os.environ["HF_TOKEN"]
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Discord bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# --- Discord Bot ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

async def generate_response(prompt):
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    data = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()
            try:
                text = result[0]["generated_text"]
                return text
            except Exception:
                return "😕 Модель зараз не відповідає або перевантажена."

@client.event
async def on_ready():
    print(f"✅ Увійшов як {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!ai"):
        prompt = message.content[len("!ai "):].strip()
        if not prompt:
            await message.channel.send("Напиши щось після `!ai`")
            return
        await message.channel.send("🧠 Думаю...")
        reply = await generate_response(prompt)
        await message.channel.send(reply[:1800])

# Запускаємо Flask у фоні, Discord — основний
Thread(target=run_flask).start()
client.run(DISCORD_TOKEN)
