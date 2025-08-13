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
    responded = False  # прапорець, чи вже відповіли

    if not responded and content == "<:emoji_36:1390751091355942922>":
        await message.reply("Шо вилупився 😑")
        responded = True
    if not responded and content == "жах":
        await message.reply("який жах, який жах а що не жах, жах я ж кажу, який жах 😱")
        responded = True
    if not responded and "ррр" in content:
        await message.reply("Ричалочка ти 🥰")
        responded = True

    # Група фраз для снів
    phrases = ["добраніч", "солодких снів", "надобраніч", "я спати", "солодесеньких снів"]
    if not responded and any(phrase in content for phrase in phrases):
        await message.reply("Солодесеньких снів 🥰😴")
        responded = True

    # Реакція на айпі (кілька варіантів)
    ip_phrases = ["яке айпі?", "яке айпі", "айпі", "ip"]
    if not responded and any(phrase in content for phrase in ip_phrases):
        await message.reply("Айпі сервера: `dragonseven.top`")
        responded = True
        
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















