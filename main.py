import os
import discord
import asyncio
from gpt4all import GPT4All

# Завантаження моделі
model = GPT4All("gpt4all-lora-quantized")

# Ініціалізація бота
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ai "):
        prompt = message.content[4:]
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, lambda: model.generate(prompt))
        await message.channel.send(response)

client.run(TOKEN)

