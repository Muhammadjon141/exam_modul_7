import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Telegram bot tokenini o'rnating
TELEGRAM_TOKEN = '7385548735:AAGF6oj1S65hDMoPqmCHI5fuMnbeKACekA8'

# Bot va Dispatcher ni yaratish
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Salom! O'quv markaz botiga xush kelibsiz! Artistlar haqida ma'lumot olish uchun 
                        /get_courses - Kurslar ro'yhati
                        /get_teachers - O'qituvchilar ro'yhati
                        /get_students - Talabalar ro'yhati
                        buyrug‘ini yuboring.""")

@dp.message_handler(commands=['get_courses'])
async def get_artists(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/course/')
    if response.status_code == 200:
        artists = response.json()
        if artists:
            for artist,i in zip(artists, range(1, (len(artists)+1))):
                artists_list = artist['title']
                await message.reply(f"Kurslar ro'yhati:\n{i}. {artists_list}")
        else:
            await message.reply("Kurslar topilmadi.")
    else:
        await message.reply("Kurslarni olishda xatolik yuz berdi.")


@dp.message_handler(commands=['get_teachers'])
async def get_alboms(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/teacher/')
    if response.status_code == 200:
        alboms = response.json()
        if alboms:
            for albom,i in zip(alboms, range(1, (len(alboms)+1))):
                alboms_list = f"{albom['first_name']} {albom['last_name']}"
                await message.reply(f"O'qituvchilar ismi:\n{i}. {alboms_list}")
        else:
            await message.reply("O'qituvchilar topilmadi.")
    else:
        await message.reply("O'qituvchilarni olishda xatolik yuz berdi.")

@dp.message_handler(commands=['get_students'])
async def get_songs(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/student/')
    if response.status_code == 200:
        songs = response.json()
        if songs:
            for song,i in zip(songs, range(1, (len(songs)+1))):
                songs_list = f"{song['first_name']} {song['last_name']}"
                await message.reply(f"Student ismi:\n{i}. {songs_list}")
        else:
            await message.reply("Studentlar topilmadi.")
    else:
        await message.reply("Studentlarni olishda xatolik yuz berdi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
