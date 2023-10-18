import os
import logging

from aiogram import Bot, Dispatcher, executor, types
#from config import TOKEN

logging.basicConfig(filename='logs.txt', 
                    filemode='a',
                    level=logging.DEBUG)

TOKEN = os.getenv('TOKEN')

dic = {
    'А': 'A',
    'а': 'a',
    'Б': 'B',
    'б': 'b',
    'В': 'V',
    'в': 'v',
    'Г': 'G',
    'г': 'g',
    'Д': 'D',
    'д': 'd',
    'Е': 'E',
    'е': 'e',
    'Ё': 'E',
    'ё': 'e',
    'Ж': 'Zh',
    'ж': 'zh',
    'З': 'Z',
    'з': 'z',
    'И': 'I',
    'и': 'i',
    'Й': 'I',
    'й': 'i',
    'К': 'K',
    'к': 'k',
    'Л': 'L',
    'л': 'l',
    'М': 'M',
    'м': 'm',
    'Н': 'N',
    'н': 'n',
    'О': 'O',
    'о': 'o',
    'П': 'P',
    'п': 'p',
    'Р': 'R',
    'р': 'r',
    'С': 'S',
    'с': 's',
    'Т': 'T',
    'т': 't',
    'У': 'U',
    'у': 'u',
    'Ф': 'F',
    'ф': 'f',
    'Х': 'Kh',
    'х': 'kh',
    'Ц': 'Ts',
    'ц': 'ts',
    'Ч': 'Ch',
    'ч': 'ch',
    'Ш': 'Sh',
    'ш': 'sh',
    'Щ': 'Shch',
    'щ': 'shch',
    'Ъ': 'Ie',
    'ъ': 'ie',
    'Ы': 'Y',
    'ы': 'y',
    'Ь': "",
    'ь': "",
    'Э': 'E',
    'э': 'e',
    'Ю': 'Iu',
    'ю': 'iu',
    'Я': 'Ia',
    'я': 'ia',
    ' ': ' '
    }

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Здравствуйте, {user_name}! Введите, пожалуйста, Ваше полное ФИО"
    logging.info(f"{user_name=} {user_id=} send message {message.text}")
    await message.reply(text)

@dp.message_handler()
async def transformation_alphabet(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    result = '' 
    for letter in text:
        result += dic[letter]
    logging.info(f"{user_name=} {user_id=} send message {result}")
    await bot.send_message(user_id, result)  


if __name__ == '__main__':
    executor.start_polling(dp)