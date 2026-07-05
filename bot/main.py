import asyncio
from aiogram import Bot, Dispatcher

from bot.config import settings
from bot.services.database import Database
from bot.handlers import setup_handlers


async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    db = Database(settings.db_path)
    await db.init()

    setup_handlers(dp)

    print("🤖 GPT Chat Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
