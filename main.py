import os
import threading
from flask import Flask
from discord.ext import commands

# --- Простий healthcheck web-сервер ---
app = Flask("health")

@app.route("/")
def home():
    return "OK", 200

def run_web():
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)

# --- Discord bot ---
intents = commands.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот увімкнений: {bot.user} — ready.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().strip() == "яке айпі":
        await message.reply("Айпі сервера: `play.pryklad.com`")  # <- заміни на свій IP/хост
    await bot.process_commands(message)

if __name__ == "__main__":
    # запускаємо web-сервер в окремому потоці (Render очікує процес, що слухає порт)
    t = threading.Thread(target=run_web)
    t.start()

    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        print("⛔ ERROR: TOKEN не знайдено в ENV")
    else:
        bot.run(TOKEN)
