from aiogram import Bot, Dispatcher, executor, types 
from aiogram.dispatcher.filters import Text 

Token = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAA" 
bot = Bot(token=Token) 
dp = Dispatcher(bot=bot) 

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message): 
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    buttons = ["Получить новости"] 
    keyboard.add(*buttons) 
    us_name = message.from_user.full_name 
    await message.answer(f"{us_name}, , привет, нужны новости?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Получить новости"))
async def cmd_start(message: types.Message): 
    await message.reply_document(open('news.txt', 'rb'))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)