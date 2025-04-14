import ftplib
import aiogram.types
from aiogram import Bot,Dispatcher,Router,F
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from os import getenv
from dotenv import load_dotenv
import sys
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
load_dotenv()
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Uzbekistan", callback_data="uz")
    inline.button(text="Rassia", callback_data="ru")
    inline.button(text="Qozog'iston", callback_data="kz")
    inline.button(text="Qirg'iziston", callback_data="kg")
    inline.button(text="Afg'oniston", callback_data="afg")
    inline.button(text="Tojikiston", callback_data="tjk")
    # inline.button(text="Ha",callback_data="Ha")
    # inline.button(text="Yoq",callback_data="Yoq")
    inline.adjust(2)
    return inline.as_markup()

def get_ha_yoq() ->ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    kb.button(text="HA")
    kb.button(text="YOQ")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
def tozalash()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder
    inline.button(text="Ha", callback_data="Ha")
    inline.button(text="yoq", callback_data="yoq")
    return inline.as_markup()
dd=Dispatcher()
tokinim=getenv("BOT_TOKEN")
# @dd.startup()

my_router=Router()
dd.include_router(my_router)
async def bot_ishlaganda(b:Bot):
    await b.send_message(chat_id=getenv("MY_ID"),text="Bot ishladi")
# @dd.message(Command('start'))
@my_router.message(Command('start'))
# Router yordamida xabar berish

async def start_bosilganda(m:Message):
    await m.answer("Xush kelibsiz",)
    await m.answer("Siz qaysi davlatni tanlamoqchisiz?:" \
                   , reply_markup=get_inline())

@my_router.callback_query(F.data == "kz")
async def tm_tanlanda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Qozog'istoni tanladingizmi")
    await call.message.answer("Tojikistoni tanladangiz")

@my_router.callback_query(F.data=="ha")
async def ha_tanlanganda(call:CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.answer(f"{matn}ni tanladingiz")
    r=getenv("ADMINS")
    for i in r:
        await call.bot.send_message(chat_id=getenv("ADMNINS1"),\
        text=f"{call.from_user.full_name} {matn}ni tanladi")
@my_router.callback_query(F.data == "Yoq`")
async def ha_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Biror bir Davlatni tanlang")
    await call.message.edit_reply_markup(reply_markup=get_inline())
# async def ha_tanlanganda(call:CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=tozalash())
#     await call.answer("Ooo buyuk vatanparvar?!",
# async def ha_tanlanganda(call:CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=tozalash())
#     await call.answer("Ooo buyuk vatanparvar?!",
# @my_router.callback_query(F.data=="ha")
#     async def ha_tanlanganda(call:CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=tozalash())
#     await call.answer("Ooo buyuk vatanparvar?!",\
#                    reply_markup=aiogram.types.ReplyKeyboardRemove())
# @my_router.callback_query(F.data=="yoq")
# async def Yoq_tanlanganda(m:Message):
#     await call.message.edit_reply_markup(reply_markup=tozalash())
#     await m.answer("Yaxshi ish?!",\
#                    reply_markup=aiogram.types.ReplyKeyboardRemove())
# @my_router.message()
# async def xaba_kelganda(m:Message,bot:Bot):
#     await m.copy_to(chat_id=m.from_user.id)
#     await m.copy_to(chat_id=" 5005110302")
#     await m.answer(chat_id=" 5005110302",\
#                    text=f"{m.from_user.full_name} \
#     sizning botingizga '{m.text}' deb yozdi",)
async def start():
        botim=Bot(token=tokinim,\
    default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        # dd.startup.register(bot_ishlaganda)
        await dd.start_polling(botim)
if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,\
   format="%(asctime)s -%(name)s -%(levelname)s - %(message)s"\
   ,handlers=[
              logging.FileHandler("bot.log"),
              logging.StreamHandler(sys.stdout)
        ])
    run(start())
