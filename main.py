import os
import threading
import discord
from flask import Flask
from discord.ext import commands
import random
import re  # для пошуку посилань
import requests

# ===== Hugging Face AI =====
import os
HF_API_KEY = os.getenv("HF_API_KEY")  # токен підхоплюється із змінної середовища
HF_MODEL = "google/flan-t5-base"  # або іншу модель, яку вибрав

def ask_huggingface(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(
        f"https://api-inference.huggingface.co/models/{HF_MODEL}",
        headers=headers,
        json=payload
    )
    data = response.json()
    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    elif isinstance(data, dict) and "error" in data:
        return f"Помилка: {data['error']}"
    else:
        return "Помилка: AI не зміг відповісти."


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

# Лічильник GIF
user_gif_count = {}

@bot.event
async def on_ready():
    print(f"✅ Бот увімкнений: {bot.user} — ready.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower().strip()
    responded = False  # прапорець, чи вже відповіли

    # AI через Hugging Face
    if content.startswith("!ai"):
        user_input = message.content[len("!ai "):].strip()
        if user_input:
            await message.channel.send("Думаю... 🤖")
            try:
                answer = ask_huggingface(user_input)
            except Exception as e:
                answer = f"Помилка: {e}"
            await message.channel.send(answer[:1900])

    
    # === ЛІЧИЛЬНИК GIF ===
    gif_domains = ["tenor.com", "giphy.com", ".gif"]

    user_id = message.author.id
    gif_found = False

    # Перевірка вкладень
    if message.attachments:
        gif_attachments = [a for a in message.attachments if a.filename.lower().endswith(".gif")]
        if gif_attachments:
            gif_found = True

    # Перевірка посилань у тексті
    urls = re.findall(r'(https?://\S+)', message.content.lower())
    if any(any(domain in url for domain in gif_domains) for url in urls):
        gif_found = True

    # Якщо знайдено GIF
    if gif_found:
        user_gif_count[user_id] = user_gif_count.get(user_id, 0) + 1
        if user_gif_count[user_id] == 3:
            await message.reply("Шо ти ото гіфочками засипаєш...))")
            user_gif_count[user_id] = 0

    # === Рандом ===
    triggers = ["!рандом", "випадкове число", "random", "дай число", "кинь багатограник", "кинь кубик"]

    if not responded and any(content.startswith(t) for t in triggers):
        parts = content.split()

        # Якщо перший тригер складається з двох слів
        if len(parts) >= 4 and parts[0] + " " + parts[1] in triggers:
            try:
                start = int(parts[2])
                end = int(parts[3])
                number = random.randint(start, end)
                await message.reply(f"🎲 Випадкове число між {start} і {end}: {number}")
            except ValueError:
                await message.reply("Вкажіть числа у правильному форматі, наприклад: Випадкове число 1 100")

        elif len(parts) == 3:  # Для тригерів з одним словом
            try:
                start = int(parts[1])
                end = int(parts[2])
                number = random.randint(start, end)
                await message.reply(f"🎲 Випадкове число між {start} і {end}: {number}")
            except ValueError:
                await message.reply("Вкажіть числа у правильному форматі, наприклад: Випадкове число 1 100")

        else:
            number = random.randint(1, 100)
            await message.reply(f"🎲 Випадкове число від 1 до 100: {number}")

        responded = True




    if content == "<:emoji_36:1390751091355942922>": 
        await message.reply("Шо вилупився 😑")

    if not responded and "мур" in content:
        await message.reply("ти ж мій котик))🥹🥰")
        responded = True
        
    if not responded and "ррр" in content:
        await message.reply("Ричалочка ти)) 🥰")
        responded = True

    if not responded and "🖕" in content:
        await message.reply("Жах отаке показувати 😱")
        responded = True
        
    if not responded and ":skitl_chan:" in content:
        await message.reply("Сам ти тяночка) 😝")
        responded = True

    if not responded and "🩰" in content:
        await message.reply("Шо ти ото ті тапки постійно кидаєш...))")
        responded = True

    if content == "🥰": 
        await message.reply("Хто це у нас тут у сердечках купається))")

    if not responded and "жах" in content:
        await message.reply("який жах, який жах а що не жах, жах я ж кажу, який жах 😱")
        responded = True

    if not responded and "ужас" in content:
        await message.reply("який жах, який жах а що не жах, жах я ж кажу, який жах 😱")
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
       
    if not responded and content == "правило 3.1":
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
        "**Ферма золота**\n\n"
        "Світ: Звичайний, Незер\n\n"
        "Частина незерська: `369 128 122` (стеля незеру)\n"
        "Частина в звичайному світі: `2968 68 982`"
        )
        responded = True
        
    if not responded and content == "ферма їжі":
        await message.reply(
        "**Ферма їжі (смажена свинина)**\n\n"
        "Світ: Незер\n\n"
        "Координати: `269 128 37` (стеля незеру)"
        )
        responded = True
        
    if not responded and content == "ферма жаб’ячого світла":
        await message.reply(
        "**Ферма жаб’ячого світла**\n\n"
        "Світ: Незер\n\n"
        "Координати: `486 128 2` (стеля незеру)"
        )
        responded = True
        
    if not responded and content == "ферма шалкерів":
        await message.reply(
        "**Ферма шалкерів**\n\n"
        "Світ: Звичайний\n\n"
        "Координати: `2759 90 763`"
        )
        responded = True

    if not responded and content == "ферма пороху":
        await message.reply(
        "**Ферма пороху**\n\n"
        "Світ: Звичайний\n\n"
        "Координати: `2792 91 938`"
        )
        responded = True

    if not responded and content == "ферма заліза":
        await message.reply(
        "**Ферма заліза**\n\n"
        "Світ: Звичайний\n\n"
        "Тех. частина: `2546 71 714`\n"
        "Готовий продукт: `2452 75 661`"
        )
        responded = True

    if not responded and content == "ферма ламінарії":
        await message.reply(
        "**Ферма блоків ламінарії**\n\n"
        "Світ: Звичайний\n\n"
        "Координати: `2471 70 779`"
        )
        responded = True

    if not responded and content == "ферма тростини":
        await message.reply(
        "**Ферма тростини**\n\n"
        "Світ: Звичайний\n\n"
        "Координати: `2612 63 736`"
        )
        responded = True

    if not responded and content == "ферма скелетів":
        await message.reply(
        "**Ферми скелетів (на спавнері)**\n\n"
        "Світ: Звичайний\n\n"
        "Координати першої: `2589 63 394`\n"
        "Координати другої: `2606 63 727`"
        )
        responded = True

    if not responded and content == "ферма вовни":
        await message.reply(
        "**Ферма вовни**\n\n"
        "Світ: Звичайний\n\n"
        "Координати: `2591 63 750`"
        )
        responded = True

    if not responded and content == "ферма ключів":
        await message.reply(
        "**Ферми ключів**\n\n"
        "Світ: Звичайний\n\n"
        "Головний острів: `2494 80 621`\n"
        "Головний острів: `2428 73 614`\n"
        "Сусідній острів: `2898 72 593`"
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


































