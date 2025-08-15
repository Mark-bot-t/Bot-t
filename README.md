# Линкорез — Telegram бот для разрезания YouTube плейлистов на ссылки

## Запуск локально
1. Установи зависимости:
   ```
   pip install -r requirements.txt
   ```
2. Запусти бота:
   ```
   TOKEN=твой_токен python bot.py
   ```

## Деплой на Railway
1. Зайди на https://railway.app
2. Создай новый проект и привяжи GitHub репозиторий с этим кодом.
3. В разделе Variables добавь:
   - KEY: TOKEN
   - VALUE: твой токен от BotFather
4. Railway автоматически запустит бота.
