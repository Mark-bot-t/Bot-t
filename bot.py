import asyncio
import json
import subprocess
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Получаем токен из переменных окружения (Railway Variables)
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я Линкорез — пришли ссылку на YouTube плейлист, и я нарежу его на отдельные видео.")

@dp.message()
async def handle_playlist(message: types.Message):
    playlist_url = message.text.strip()
    if "youtube.com/playlist" not in playlist_url:
        await message.answer("❌ Это не похоже на ссылку на плейлист YouTube.")
        return

    await message.answer("🔍 Получаю список видео...")

    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--dump-json", playlist_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        video_count = 0
        for line in result.stdout.splitlines():
            data = json.loads(line)
            if "id" in data:
                video_url = f"https://www.youtube.com/watch?v={data['id']}"
                await message.answer(video_url)
                await message.answer("———————————")
                video_count += 1

        if video_count == 0:
            await message.answer("❌ Видео в плейлисте не найдено.")

    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
