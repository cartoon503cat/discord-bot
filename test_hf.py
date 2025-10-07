import os
import discord
import aiohttp
import asyncio

# Токени з секретів Replit
DISCORD_TOKEN = os.environ["TOKEN"]
HF_TOKEN = os.environ["HF_TOKEN"]

# Hugging Face модель — безкоштовна, текстова, легка
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

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
                return "😕 Вибач, але модель не відповіла або перевантажена."

@client.event
async def on_ready():
    print(f"✅ Увійшов як {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Якщо користувач написав команду з префіксом !
    if message.content.startswith("!ai"):
        prompt = message.content[len("!ai "):].strip()
        if not prompt:
            await message.channel.send("Напиши щось після `!ai`, наприклад: `!ai Привіт, хто ти?`")
            return

