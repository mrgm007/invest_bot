from aiogram import types
from dispatcher import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

invest_menu = InlineKeyboardMarkup(row_width=1)
invest_btn = InlineKeyboardButton(text="Инвестировать💰", url="https://t.me/adillet_ico")
invest_menu.add(invest_btn)

@dp.message_handler(commands="start")
async def cmd_ping_bot(message: types.Message):
    chat_id = message.chat.id
    text = "Ассаламуалейкум, меня зовут <b>Әділет Қабдолов</b>, я \nпрофессионал в области <b>ICO</b>, занимаюсь привлечением \nинвесторов 💰 \nМои показатели самые высокие на всем СНГ, моя деятельность \nХаляль, разрешенная шариатом, я получаю заработок в виде \nдивидендов на бирже, ваш заработок — он только ваш. Ин Ша \nАллах, а теперь расскажите о себе по кнопке ниже 👇"

    photo_path = os.path.join(os.path.dirname(__file__), 'photo.jpg')
    with open(photo_path, 'rb') as photo_file:
        photo = types.InputFile(photo_file)
        await bot.send_photo(chat_id=chat_id, photo=photo, caption=text, reply_markup=invest_menu)

