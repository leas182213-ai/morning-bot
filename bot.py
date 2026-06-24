import os
import asyncio
from datetime import datetime
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CONTACTS = [
    {"id": 304029100, "name": "Мая", "greeting": "Доброе утро, Маечка! Пусть этот день принесёт тебе только радость и тепло. Люблю тебя ☀️"},
    {"id": 5579813852, "name": "Соня", "greeting": "Доброе утро, Сонечка! Желаю лёгкого и светлого дня, пусть всё складывается хорошо 🌸"},
    {"id": 513987887, "name": "Доча", "greeting": "Доброе утро, моя родная! Целую тебя крепко, пусть день будет добрым ❤️"},
    {"id": 15618241, "name": "Марина", "greeting": "Доброе утро, Марина! Желаю прекрасного и продуктивного дня 🌺"},
    {"id": 6675950007, "name": "Шухрат", "greeting": "Доброе утро, Шухрат! Желаю отличного дня и успехов во всём ☀️"},
]

SEND_DAYS = [0, 2, 4]
SEND_HOUR = 8

async def send_greetings():
    bot = Bot(token=BOT_TOKEN)
    for contact in CONTACTS:
        try:
            await bot.send_message(chat_id=contact["id"], text=contact["greeting"])
            print(f"✅ Отправлено: {contact['name']}")
        except Exception as e:
            print(f"❌ Ошибка {contact['name']}: {e}")

async def main():
    while True:
        now = datetime.now()
        if now.weekday() in SEND_DAYS and now.hour == SEND_HOUR and now.minute == 0:
            print("Отправляю приветствия...")
            await send_greetings()
            await asyncio.sleep(61)
        else:
            await asyncio.sleep(30)

if __name__ == "__main__":
    print("Бот запущен!")
    asyncio.run(main())
