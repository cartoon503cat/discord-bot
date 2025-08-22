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

    
    # ПРАВИЛА

    
    if not responded and content == "правило 1":
        await message.reply("**1. Усі рішення приймає виключно головна сторона (Аня – у місті, Цукерка – у селі).**")
        responded = True

    if not responded and content == "1":
        await message.reply("**1. Усі рішення приймає виключно головна сторона (Аня – у місті, Цукерка – у селі).**")
        responded = True
       
    if not responded and content == "правило 2.1":
        await message.reply("2.1 Щоб обрати місце для будівництва, напишіть у чат <#1331393063767117874>  , і Аня покаже вам доступні райони для забудови.")
        responded = True
       
    if not responded and content == "2.1":
        await message.reply("2.1 Щоб обрати місце для будівництва, напишіть у чат <#1331393063767117874>  , і Аня покаже вам доступні райони для забудови.")
        responded = True
       
    if not responded and content == "правило 3.1" in content:
        await message.reply("3.1 Нзеценурна лайка.")
        responded = True
    
    if not responded and content == "3.1":
        await message.reply("3.1 Нзеценурна лайка.")
        responded = True

    if not responded and content == "правило 3.2":
        await message.reply("3.2 Поширення фото/відео 18+.")
        responded = True
         
    if not responded and content == "3.2":
        await message.reply("3.2 Поширення фото/відео 18+.")
        responded = True
       
    if not responded and content == "правило 3.3":
        await message.reply("3.3 Спори на тему релігії, політики або особистих уподобань.")
        responded = True

    if not responded and content == "3.3":
        await message.reply("3.3 Спори на тему релігії, політики або особистих уподобань.")
        responded = True

    if not responded and content == "правило 3.4":
        await message.reply("3.4 Забороняється ображати інших мешканців острова або висловлюватися негативно про них.")
        responded = True

    if not responded and content == "3.4":
        await message.reply("3.4 Забороняється ображати інших мешканців острова або висловлюватися негативно про них.")
        responded = True

    if not responded and content == "правило 3.5":
        await message.reply("3.5 Заборонені спам, флуд та інше, що заважає гармонії острова.")
        responded = True

    if not responded and content == "3.5":
        await message.reply("3.5 Заборонені спам, флуд та інше, що заважає гармонії острова.")
        responded = True

    if not responded and content == "правило 3.6":
        await message.reply("3.6 Проявляйте повагу до кожного мешканця острова.")
        responded = True

    if not responded and content == "3.6":
        await message.reply("3.6 Проявляйте повагу до кожного мешканця острова.")
        responded = True

    if not responded and content == "правило 3.7":
        await message.reply("3.7 Жарти, що ображають почуття, неприпустимі! Якщо вас просять зупинитися, так і зробіть.")
        responded = True

    if not responded and content == "3.7":
        await message.reply("3.7 Жарти, що ображають почуття, неприпустимі! Якщо вас просять зупинитися, так і зробіть.")
        responded = True

    if not responded and content == "правило 3.8":
        await message.reply("3.8 Забороняється будь які образи, негативні висказування, негативні реакції у адрес адміністрації та жителів міста.")
        responded = True

    if not responded and content == "3.8":
        await message.reply("3.8 Забороняється будь які образи, негативні висказування, негативні реакції у адрес адміністрації та жителів міста.")
        responded = True

    if not responded and content == "правило 3.9":
        await message.reply("3.10 Нік учасника обов'язково має мати букви у своєму складі, щоб утворюворювалося хоч якесь сенсове слово... Не дозволяються ніки лише з символів типу крапок, дужок, рисок, тире і так далі...")
        responded = True

    if not responded and content == "3.9":
        await message.reply("3.10 Нік учасника обов'язково має мати букви у своєму складі, щоб утворюворювалося хоч якесь сенсове слово... Не дозволяються ніки лише з символів типу крапок, дужок, рисок, тире і так далі...")
        responded = True

    if not responded and content == "правило 4.1":
        await message.reply("4.1 Якщо вона вам не подобається, скажіть про це спокійно, і ми разом владнаємо конфлікт.")
        responded = True

    if not responded and content == "4.1":
        await message.reply("4.1 Якщо вона вам не подобається, скажіть про це спокійно, і ми разом владнаємо конфлікт.")
        responded = True

    if not responded and content == "правило 4.2":
        await message.reply("4.2 Якщо ж ваше обурення – лише для сварки, на вас чекає миттєвий бан.")
        responded = True

    if not responded and content == "4.2":
        await message.reply("4.2 Якщо ж ваше обурення – лише для сварки, на вас чекає миттєвий бан.")
        responded = True

    
    #ІНФОРМАЦІЯ

    
    if not responded and content == "ферма золота":
        await message.reply(
        "**Ферма золота:**\n\n"
        "Світ: Звичайний, Незер\n\n"
        "Частина незерська: `369 128 122` (стеля незеру)\n"
        "Частина в звичайному світі: `2968 68 982`"
        )
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





















