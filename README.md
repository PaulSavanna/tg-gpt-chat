# TG GPT Chat Bot

Telegram bot with ChatGPT — just chat with AI.

## Features

- Chat with GPT-4o-mini
- Photo analysis (describe images)
- Context history
- Clear history
- Fast responses

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill in BOT_TOKEN and OPENAI_API_KEY
python -m bot.main
```

### Environment Variables

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Telegram Bot API token from [@BotFather](https://t.me/BotFather) |
| `OPENAI_API_KEY` | OpenAI API key for GPT and DALL-E access |

## Commands

- `/start` — restart the bot
- `/clear` — clear history
- `/help` — show help

## Buttons

- Clear History — reset context
- Help — instructions
