import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6821567224:AAH6opjmnGHTXTPZVOAatXN8O1c61OQCbFg'


# Configure Logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot (token=API_TOKEN)
dp = Dispatcher(bot)
@dp. message_handler(commands=['start', 'help' ])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Abdulaziz")],
        [types.KeyboardButton(text="Dasturchilar")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
async def send_welcome (message: types.Message):

#This handler will be called when user sends "/start or/help" command
    await message.reply("Salom")
@dp. message_handler()
async def send (message: types.Message):
    try:
        respond = 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


