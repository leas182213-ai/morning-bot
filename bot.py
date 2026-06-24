import os
import asyncio
from datetime import time
from telegram import Bot
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CONTACTS = [
    {"id": 304029100, "name": "Мая", "greeting": "Доброе утро, Маечка! Пусть этот день принесёт тебе только радость и тепло. Люблю тебя ☀️"},
    {"id": 5579813852, "name": "Соня", "greeting": "Доброе утро, Сонечка! Желаю лёгкого и светлого дня, пусть всё складывается хорошо 🌸"},
    {"id": 513987887, "name": "Доча", "greeting": "Доброе утро, моя родная! Целую тебя крепко, пусть день будет добрым ❤️"},
    {"id": 15618241, "name": "Марина", "greeting": "Доброе утро, Марина! Желаю прекрасного и продуктивного дня 🌺"},
    {"id": 6675950007, "name": "Шухрат", "greeting": "Доброе утро, Шухрат! Желаю отличного дня и успехов во всём ☀️"},
]

SEND_DAYS = [0, 2, 4]

async def send_greetings(context):
    from datetime import datetime
    today = datetime.now().weekday()
    if today in SEND_DAYS:
        for contact in CONTACTS:
            try:
                await context.bot.send_message(chat_id=contact["id"], text=contact["greeting"])
                print(f"✅ Отправлено: {contact['name']}")
            except Exception as e:
                print(f"❌ Ошибка {contact['name']}: {e}")

async def start(update, context):
    await update.message.reply_text("Бот утренних приветствий работает! 🌅")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.job_queue.run_daily(send_greetings, time=time(8, 0))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
