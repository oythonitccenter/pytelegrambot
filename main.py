from aiogram import Bot,Dispatcher
from asyncio import run
from aiogram.filters import Command,CommandStart
from aiogram.types import Message
t="7944803359:AAFOIAeULJqZflXW9n_zzI6ni6qqwxXEoz8"
dp=Dispatcher()
#Dekorat bilan Dispatcher vazifasini yaratish
@dp.message(Command("start"))
# Javob beragigan dekoratr Command("start") Start buyrug'i
async def start_bosilganda(x:Message,bot:Bot):
    await x.answer(f"Xush kelibsiz")
    await bot.send_message("7956914567","Xush kelibsiz ")

async def main():
    bot=Bot(token=t)
    dp.message.register(start_bosilganda,CommandStart)
    await dp.start_polling(bot)
run(main())


