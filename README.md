# 🤖 TG GPT Chat Bot

Telegram бот с ChatGPT — просто общайся с AI.

## Возможности

- 💬 Чат с GPT-4o-mini
- 📷 Анализ фото (описание картинок)
- 📝 История контекста
- 🗑️ Очистка истории
- ⚡ Быстрые ответы

## Установка

```bash
pip install -r requirements.txt
cp .env.example .env
# Заполни BOT_TOKEN и OPENAI_API_KEY
python -m bot.main
```

## Команды

- `/start` — начать заново
- `/clear` — очистить историю
- `/help` — помощь

## Кнопки

- 🗑️ Очистить историю — сброс контекста
- ❓ Помощь — инструкция
