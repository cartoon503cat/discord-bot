import os
import threading
import discord
from flask import Flask
from discord.ext import commands

app = Flask("health")

@app.route("/")
def home():
    return "OK", 200

def run_web():
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот увімкнений: {bot.user} — ready.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()

    
    if content == "<:emoji_36:1390751091355942922>":
        await message.reply("Шо вилупився 😑")
    if content == "жах":
        await message.reply("який жах, який жах а що не жах, жах я ж кажу, який жах 😱")
    if "ррр" in content:
        await message.reply("Ричалочка ти 🥰")
    if any(phrase in content for phrase in ["яке айпі", "яке айпі?"]):
        await message.reply("Айпі сервера:`dragonseven.top`")
phrases = ["добраніч", "солодких снів", "надобраніч", "я спати", "солодесеньких снів"]
    if any(phrase in content for phrase in phrases):
    await message.reply("Солодесеньких снів 🥰😴")
    # Тут можна додавати інші фрази...

    await bot.process_commands(message)

if __name__ == "__main__":
    t = threading.Thread(target=run_web)
    t.start()

    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        print("⛔ ERROR: TOKEN не знайдено в ENV")
    else:
        bot.run(TOKEN)






